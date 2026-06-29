#!/usr/bin/env python3
"""
TRAIL 360° ANALYZER — Jose / Temporada 2026
Strava → Plan Completo → HTML Dashboard
Carreras objetivo:
  • Maratón MTN Palencia — 44km / 3500m D+
  • TP60               — 63km / 2500m D+
Uso: python trail_analyzer.py
"""

import json, os, sys, math, time, webbrowser, threading
import http.server, urllib.parse, urllib.request
from datetime import datetime, date, timedelta
from pathlib import Path

# Fix Windows console encoding for Unicode output
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN — ⚠ ACTUALIZA FECHAS DE CARRERA SI ES NECESARIO
# ═══════════════════════════════════════════════════════════════════════════════
CLIENT_ID     = "114720"

def load_strava_credentials():
    """Resolve Strava credentials: env vars first, then gitignored token file.
    Raises RuntimeError if no client secret is available."""
    cid     = os.environ.get("STRAVA_CLIENT_ID", CLIENT_ID)
    secret  = os.environ.get("STRAVA_CLIENT_SECRET")
    refresh = os.environ.get("STRAVA_REFRESH_TOKEN")
    if (not secret or not refresh) and TOKEN_FILE.exists():
        data = json.loads(TOKEN_FILE.read_text())
        secret  = secret  or data.get("client_secret")
        refresh = refresh or data.get("refresh_token")
    if not secret:
        raise RuntimeError(
            "Strava client secret not found. Set STRAVA_CLIENT_SECRET env var "
            "or add a 'client_secret' key to strava_token.json.")
    return {"client_id": cid, "client_secret": secret, "refresh_token": refresh}

REDIRECT_URI  = "http://localhost:8888/callback"
TOKEN_FILE    = Path("strava_token.json")
OUTPUT_FILE   = Path("dashboard.html")
OUTPUT_PLAN   = Path("plan_completo.html")
WEEKS_HISTORY = 16   # semanas de historial Strava a analizar

ATHLETE = {
    "name": "Jose",
    "weight_kg": 82,
    "target_weight_kg": 76,
    "vdot": 57,
    "best_10k_sec": 2340,
    "best_half_sec": 5700,
    # ── Datos de laboratorio (prueba de esfuerzo) ──
    "hr_max_lab": 194,   # FC máxima real
    "vt1": 152,          # Umbral ventilatorio 1 (aeróbico) — techo Z2
    "vt2": 172,          # Umbral ventilatorio 2 (anaeróbico) — techo Z3/inicio Z4
    "races": [
        {"id":"palencia","name":"Maratón MTN Palencia",
         "date":"2026-09-12","km":44,"d_plus":3500,"accent":"#f97316"},
        {"id":"tp60","name":"TP60",
         "date":"2026-10-11","km":63,"d_plus":2500,"accent":"#22d3ee"},
    ]
}

PLAN_START = date(2026, 6, 29)  # Monday — W1 of the TP60/Palencia block

# ═══════════════════════════════════════════════════════════════════════════════
# STRAVA OAUTH
# ═══════════════════════════════════════════════════════════════════════════════
_auth_code = None

class _CB(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global _auth_code
        p = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        _auth_code = p.get("code",[None])[0]
        self.send_response(200); self.send_header("Content-type","text/html"); self.end_headers()
        self.wfile.write(b"<h2 style='font-family:monospace;padding:40px'>OK - puedes cerrar esta pesta\xc3\xb1a</h2>")
    def log_message(self,*a): pass

def get_token():
    creds = load_strava_credentials()
    if TOKEN_FILE.exists():
        tok = json.loads(TOKEN_FILE.read_text())
        if tok.get("expires_at",0) > time.time()+60:
            print("✓ Token Strava válido"); return tok
        print("↻ Renovando token Strava...")
        data = urllib.parse.urlencode({"client_id":creds["client_id"],"client_secret":creds["client_secret"],
            "grant_type":"refresh_token","refresh_token":tok.get("refresh_token") or creds["refresh_token"]}).encode()
        with urllib.request.urlopen(urllib.request.Request(
                "https://www.strava.com/oauth/token",data=data,method="POST")) as r:
            new = json.loads(r.read())
        tok.update(new)               # keep client_secret + any extra keys already in the file
        TOKEN_FILE.write_text(json.dumps(tok)); return tok
    # first-time browser auth path
    global _auth_code
    url=(f"https://www.strava.com/oauth/authorize?client_id={creds['client_id']}"
         f"&redirect_uri={REDIRECT_URI}&response_type=code&scope=activity:read_all&approval_prompt=auto")
    srv = http.server.HTTPServer(("localhost",8888),_CB)
    t = threading.Thread(target=srv.handle_request); t.daemon=True; t.start()
    print("\n🔑 Abriendo Strava en el navegador..."); webbrowser.open(url); t.join(timeout=120)
    srv.server_close()
    if not _auth_code: raise RuntimeError("No se recibió código de autorización")
    data = urllib.parse.urlencode({"client_id":creds["client_id"],"client_secret":creds["client_secret"],
        "code":_auth_code,"grant_type":"authorization_code"}).encode()
    with urllib.request.urlopen(urllib.request.Request(
            "https://www.strava.com/oauth/token",data=data,method="POST")) as r:
        tok = json.loads(r.read())
    TOKEN_FILE.write_text(json.dumps(tok)); print("✓ Autenticado con Strava"); return tok

def fetch_activities(tok):
    after = int((datetime.now()-timedelta(weeks=WEEKS_HISTORY)).timestamp())
    url = f"https://www.strava.com/api/v3/athlete/activities?after={after}&per_page=200&page=1"
    req = urllib.request.Request(url,headers={"Authorization":f"Bearer {tok['access_token']}"})
    with urllib.request.urlopen(req) as r: acts = json.loads(r.read())
    print(f"✓ {len(acts)} actividades cargadas ({WEEKS_HISTORY} semanas)")
    return acts

def fetch_athlete(tok):
    req = urllib.request.Request("https://www.strava.com/api/v3/athlete",
        headers={"Authorization":f"Bearer {tok['access_token']}"})
    with urllib.request.urlopen(req) as r: return json.loads(r.read())

def fetch_zones(tok):
    try:
        req = urllib.request.Request("https://www.strava.com/api/v3/athlete/zones",
            headers={"Authorization":f"Bearer {tok['access_token']}"})
        with urllib.request.urlopen(req) as r: return json.loads(r.read())
    except: return {}

# ═══════════════════════════════════════════════════════════════════════════════
# ANÁLISIS ACTIVIDADES
# ═══════════════════════════════════════════════════════════════════════════════
def analyze(acts, zones_data):
    weeks = {}
    hr_max = 0
    for a in acts:
        if a.get("type") not in ("Run","TrailRun","Hike"): continue
        d = datetime.strptime(a["start_date_local"][:10],"%Y-%m-%d").date()
        wstart = d - timedelta(days=d.weekday())
        k = wstart.isoformat()
        if k not in weeks: weeks[k] = {"km":0,"d_plus":0,"time_min":0,"runs":0,
                                         "hr_avg_list":[],"types":[]}
        w = weeks[k]
        w["km"]       += round(a.get("distance",0)/1000,1)
        w["d_plus"]   += int(a.get("total_elevation_gain",0))
        w["time_min"] += int(a.get("moving_time",0)//60)
        w["runs"]     += 1
        if a.get("average_heartrate"): w["hr_avg_list"].append(a["average_heartrate"])
        if a.get("max_heartrate"): hr_max = max(hr_max, a["max_heartrate"])
        t = "Trail" if a.get("sport_type") in ("TrailRun","Hike") or a.get("total_elevation_gain",0)>100 else "Road"
        w["types"].append(t)
    for k,w in weeks.items():
        w["hr_avg"] = round(sum(w["hr_avg_list"])/len(w["hr_avg_list"])) if w["hr_avg_list"] else 0
        del w["hr_avg_list"]
        w["trail_pct"] = round(100*w["types"].count("Trail")/max(w["runs"],1))
    sorted_weeks = sorted(weeks.items())
    # Use lab-tested HR max if available, else Strava, else fallback
    lab_max = ATHLETE.get("hr_max_lab", 0)
    if lab_max > 0:
        hr_max = lab_max
    elif hr_max < 150:
        hr_max = 194  # fallback
    # Build zone names from Strava if available
    hr_zones = None
    if zones_data and "heart_rate" in zones_data:
        hr_zones = zones_data["heart_rate"]["zones"]
    return {"weeks": sorted_weeks, "hr_max": hr_max, "hr_zones": hr_zones}

# ═══════════════════════════════════════════════════════════════════════════════
# PLAN DE ENTRENAMIENTO COMPLETO (15 semanas)
# Base científica:
#   Seiler 2010: distribución polarizada 80/20
#   Koop 2016: back-to-back specificity trail
#   Beattie 2017: HST mejora economía de carrera
#   Mujika 2003: taper óptimo 2 semanas
#   Jeukendrup 2014: nutrición durante carrera 60-90g CHO/h
#   Giovanelli 2016: power hiking eficiencia en pendientes >15%
# ═══════════════════════════════════════════════════════════════════════════════
PLAN = [
  # ── FASE 1: RECONSTRUCCIÓN BASE + CLIMBING (W1-4 | 29 Jun – 26 Jul) ──
  {"week":1,"phase":1,"phase_name":"Reconstrucción base","load":"LOW-MED","title":"Re-entrada","km":46,"d_plus":800,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso / movilidad 15 min."},
    {"day":"M","type":"EASY","km":8,"d":0,"desc":"8km Z2 (≤152). Run first → GYM Fase A."},
    {"day":"X","type":"TEMPO","km":11,"d":250,"desc":"11km: 3km Z1 + 5×3min Z3 en cuesta (2min Z1 bajada) + 2km Z1."},
    {"day":"J","type":"TRAIL","km":8,"d":200,"desc":"8km Z2 trail rolling."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":13,"d":350,"desc":"13km Z1–Z2, busca 350m D+. 1 gel km10."},
    {"day":"D","type":"EASY","km":6,"d":0,"desc":"6km Z1 recovery."},
   ],"notes":"Re-entrada controlada desde la base de junio. Registra FC reposo cada mañana."},

  {"week":2,"phase":1,"phase_name":"Reconstrucción base","load":"MED","title":"Volumen on","km":54,"d_plus":1100,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":9,"d":0,"desc":"9km Z2. Run first → GYM Fase A."},
    {"day":"X","type":"TEMPO","km":13,"d":100,"desc":"13km: 3km Z1 + 2×12min Z3 (3min Z1) + 2km Z1 + 4×20s strides."},
    {"day":"J","type":"TRAIL","km":9,"d":200,"desc":"9km Z2 trail. Run first → GYM Fase A."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso / 30min movilidad."},
    {"day":"S","type":"LONG","km":18,"d":800,"desc":"18km Z1–Z2, máximo D+ disponible. 2 geles."},
    {"day":"D","type":"EASY","km":5,"d":0,"desc":"5km Z1 recovery."},
   ],"notes":"FC media al mismo ritmo debería bajar 2-4 bpm vs sem 1."},

  {"week":3,"phase":1,"phase_name":"Reconstrucción base","load":"MED-HIGH","title":"Primera carga de desnivel","km":60,"d_plus":1500,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":0,"desc":"10km Z2. Run first → GYM Fase A."},
    {"day":"X","type":"TEMPO","km":14,"d":400,"desc":"14km: 2km Z1 + 3×15min Z3 en cuesta (3min Z1) + 2km Z1."},
    {"day":"J","type":"TRAIL","km":10,"d":300,"desc":"10km Z2 trail. Run first → GYM Fase A."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":20,"d":800,"desc":"20km Z1–Z2 trail ~800m. Power-hike >15%. 50g CHO/h."},
    {"day":"D","type":"EASY","km":6,"d":0,"desc":"6km Z1 recovery."},
   ],"notes":"Primera semana con desnivel real. Acabar el largo controlado, no vaciado."},

  {"week":4,"phase":1,"phase_name":"Reconstrucción base","load":"LOW","title":"DELOAD","km":44,"d_plus":700,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":8,"d":0,"desc":"8km Z2. GYM Fase A cargas −10%."},
    {"day":"X","type":"EASY","km":10,"d":100,"desc":"10km Z2 + 6×20s strides (sin bloque duro)."},
    {"day":"J","type":"TRAIL","km":8,"d":200,"desc":"8km Z2 trail suave."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":14,"d":400,"desc":"14km Z1–Z2 relajado."},
    {"day":"D","type":"EASY","km":4,"d":0,"desc":"4km Z1 recovery."},
   ],"notes":"Semana de absorción planificada. Llegar fresco al domingo."},

  # ── FASE 2: CONSTRUCCIÓN ESPECÍFICA (W5-8 | 27 Jul – 23 Ago) ──
  {"week":5,"phase":2,"phase_name":"Construcción específica","load":"HIGH","title":"Reinicio build + fueling","km":60,"d_plus":1500,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":0,"desc":"10km Z2. GYM Fase B (fuerza máxima)."},
    {"day":"X","type":"INTERVAL","km":14,"d":450,"desc":"14km: 4×8min Z3–Z4 en cuesta (3min rec) + strides."},
    {"day":"J","type":"TRAIL","km":10,"d":250,"desc":"10km Z2 trail. GYM Fase B."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":22,"d":800,"desc":"22km Z1–Z2 ~800m. Ensayo fueling 60g CHO/h + electrolitos."},
    {"day":"D","type":"EASY","km":4,"d":0,"desc":"4km Z1 shakeout."},
   ],"notes":"Desde aquí ensaya nutrición de carrera cada sábado."},

  {"week":6,"phase":2,"phase_name":"Construcción específica","load":"HIGH","title":"Intro back-to-back","km":68,"d_plus":2000,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":11,"d":0,"desc":"11km Z2. GYM Fase B."},
    {"day":"X","type":"TEMPO","km":15,"d":400,"desc":"15km: 3×12min Z3 cuesta sostenida + 2km Z1."},
    {"day":"J","type":"TRAIL","km":9,"d":300,"desc":"9km Z2 trail."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso o 4km recovery."},
    {"day":"S","type":"LONG","km":22,"d":900,"desc":"22km Z1–Z2 trail ~900m. 70g CHO/h."},
    {"day":"D","type":"B2B","km":11,"d":400,"desc":"11km Z2 trail con piernas cansadas (B2B real)."},
   ],"notes":"Fin de semana B2B = especificidad TP60/Palencia. Come y duerme para absorber."},

  {"week":7,"phase":2,"phase_name":"Construcción específica","load":"HIGH","title":"Pico de volumen","km":72,"d_plus":2400,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":11,"d":0,"desc":"11km Z2. GYM Fase B."},
    {"day":"X","type":"INTERVAL","km":16,"d":500,"desc":"16km: 5×6min Z4 en cuesta (3min rec) + 2km Z1."},
    {"day":"J","type":"TRAIL","km":11,"d":400,"desc":"11km Z2 trail + pliometría."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":26,"d":1100,"desc":"26km Z1–Z2 trail ~1100m. Ensayo completo de carrera (geles+bebida, 80g CHO/h)."},
    {"day":"D","type":"B2B","km":8,"d":400,"desc":"8km Z2 trail B2B."},
   ],"notes":"Semana de mayor volumen del bloque. Si FC reposo +7 o mal sueño, recorta el domingo."},

  {"week":8,"phase":2,"phase_name":"Construcción específica","load":"LOW-MED","title":"DELOAD","km":52,"d_plus":1200,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":9,"d":0,"desc":"9km Z2. GYM Fase B −10%."},
    {"day":"X","type":"EASY","km":12,"d":100,"desc":"12km Z2 + 6×20s strides."},
    {"day":"J","type":"TRAIL","km":9,"d":300,"desc":"9km Z2 trail."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":18,"d":700,"desc":"18km Z1–Z2 ~700m."},
    {"day":"D","type":"EASY","km":4,"d":100,"desc":"4km Z1 recovery."},
   ],"notes":"Absorber la construcción antes de la semana pico de Palencia."},

  # ── FASE 3: AFINADO PALENCIA (W9-11 | 24 Ago – 12 Sep) ──
  {"week":9,"phase":3,"phase_name":"Afinado Palencia","load":"HIGH","title":"Simulación Palencia (pico vertical)","km":66,"d_plus":2800,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":0,"desc":"10km Z2. GYM Fase C (potencia, bajo volumen)."},
    {"day":"X","type":"TEMPO","km":14,"d":600,"desc":"14km: 40min Z3 sostenido en cuesta + técnica de bajada."},
    {"day":"J","type":"TRAIL","km":10,"d":400,"desc":"10km Z2 trail."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":26,"d":1800,"desc":"26km de montaña ~1800m D+. Chaleco + fueling completo. Ensayo Palencia."},
    {"day":"D","type":"EASY","km":6,"d":0,"desc":"6km Z1 recovery (piernas cansadas a propósito)."},
   ],"notes":"Semana de mayor desnivel. Estímulo clave específico de Palencia."},

  {"week":10,"phase":3,"phase_name":"Afinado Palencia","load":"MED","title":"Bajada de carga","km":50,"d_plus":1400,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":9,"d":0,"desc":"9km Z2. GYM Fase C (última sesión de fuerza real)."},
    {"day":"X","type":"TEMPO","km":12,"d":400,"desc":"12km: 3×8min Z3 en cuesta (afinar, no vaciar)."},
    {"day":"J","type":"TRAIL","km":8,"d":300,"desc":"8km Z2 trail."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":18,"d":700,"desc":"18km Z1–Z2 ~700m."},
    {"day":"D","type":"EASY","km":3,"d":0,"desc":"3km Z1 recovery."},
   ],"notes":"Empieza a soltar fatiga; piernas progresivamente más vivas."},

  {"week":11,"phase":3,"phase_name":"Afinado Palencia","load":"RACE","title":"Mini-taper + PALENCIA","km":63,"d_plus":3600,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":8,"d":0,"desc":"8km Z2 + 4×20s strides (sin gym)."},
    {"day":"X","type":"EASY","km":6,"d":100,"desc":"6km Z1 + 3×2min Z3 (aperturas)."},
    {"day":"J","type":"EASY","km":5,"d":0,"desc":"5km Z1 muy suave + 4 strides."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso. Viaje/prep, prepara material, carga de carbohidratos."},
    {"day":"S","type":"RACE","km":44,"d":3500,"desc":"🌄 PALENCIA — 44km / 3500m D+. Z2 en subidas / power-hike >15%, primera mitad controlada Z1–Z2, 60–90g CHO/h, baja con cabeza para proteger cuádriceps de cara a TP60."},
    {"day":"D","type":"REST","km":0,"d":0,"desc":"Descanso total o 20min caminando."},
   ],"notes":"Sólo mini-taper: suficiente para rendir sin perder el bloque."},

  # ── FASE 4: RECUPERAR + PUENTE TP60 (W12-13 | 14 Sep – 27 Sep) ──
  {"week":12,"phase":4,"phase_name":"Recuperar + puente TP60","load":"LOW","title":"Recuperación post-Palencia","km":30,"d_plus":500,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":6,"d":0,"desc":"6km Z1 muy suave (evalúa cuádriceps)."},
    {"day":"X","type":"REST","km":0,"d":0,"desc":"Descanso o 30min movilidad."},
    {"day":"J","type":"EASY","km":8,"d":100,"desc":"8km Z1–Z2 llano."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":12,"d":400,"desc":"12km Z1–Z2 suave, poco D+."},
    {"day":"D","type":"EASY","km":4,"d":0,"desc":"4km Z1 + GYM mantenimiento ligero."},
   ],"notes":"Prioriza recuperar tejido tras 3500m de bajada. Sin calidad hasta tener piernas limpias."},

  {"week":13,"phase":4,"phase_name":"Recuperar + puente TP60","load":"HIGH","title":"Pico específico TP60 (distancia)","km":60,"d_plus":1600,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":8,"d":0,"desc":"8km Z2. GYM mantenimiento ligero."},
    {"day":"X","type":"TEMPO","km":9,"d":300,"desc":"9km: 2×15min Z3 en terreno rolling (TP60 es más llano que Palencia)."},
    {"day":"J","type":"EASY","km":5,"d":0,"desc":"5km Z2."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":38,"d":1300,"desc":"38km / ~5h Z1–Z2, perfil tipo TP60. Ensayo completo de fueling y material."},
    {"day":"D","type":"REST","km":0,"d":0,"desc":"Descanso o caminar suave."},
   ],"notes":"Tirada más larga del bloque. Énfasis en distancia/tiempo en pie. Último estímulo grande antes del taper."},

  # ── FASE 5: TAPER TP60 (W14-15 | 28 Sep – 11 Oct) ──
  {"week":14,"phase":5,"phase_name":"Taper TP60","load":"MED","title":"Taper 1","km":42,"d_plus":900,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":8,"d":0,"desc":"8km Z2 + 4×20s strides. Última sesión de gym ligera, luego stop."},
    {"day":"X","type":"TEMPO","km":12,"d":300,"desc":"12km: 3×6min Z3 (mantener chispa)."},
    {"day":"J","type":"TRAIL","km":8,"d":300,"desc":"8km Z2 trail."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":14,"d":300,"desc":"14km Z1–Z2 ~300m."},
    {"day":"D","type":"REST","km":0,"d":0,"desc":"Descanso."},
   ],"notes":"Volumen −40% vs W13, se mantienen toques de intensidad (Mujika)."},

  {"week":15,"phase":5,"phase_name":"Taper TP60","load":"RACE","title":"Taper 2 + TP60","km":86,"d_plus":2600,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":8,"d":0,"desc":"8km Z2 + 4×20s strides."},
    {"day":"X","type":"EASY","km":6,"d":100,"desc":"6km Z1 + 3×90s Z3 (aperturas)."},
    {"day":"J","type":"EASY","km":5,"d":0,"desc":"5km Z1 muy suave."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso. Carga de carbohidratos, material, plan de avituallamientos."},
    {"day":"S","type":"EASY","km":4,"d":0,"desc":"4km Z1 shakeout + 3 strides."},
    {"day":"D","type":"RACE","km":63,"d":2500,"desc":"🏁 TP60 — 63km / 2500m D+. Ritmo uniforme Z1–Z2, power-hike subidas, 60–90g CHO/h desde el inicio, electrolitos, estrategia de bolsa de avituallamiento. Intención de negative split."},
   ],"notes":"Llega fresco y confiado — el trabajo ya está hecho."},
]

# ═══════════════════════════════════════════════════════════════════════════════
# PLAN DE FUERZA
# Base científica: Beattie 2017, Blagrove 2018, Petersen 2011, Mikkola 2007
# ═══════════════════════════════════════════════════════════════════════════════
STRENGTH = [
  {"id":"A","name":"FASE A — Adaptación Anatómica","weeks":"1–8",
   "goal":"Construir base tendinosa y muscular. Prevenir lesiones. Activar glúteo y core.",
   "freq":"2×/semana (Mar+Jue)","intensity":"3×12-15 reps | 60-70% 1RM | RIR 3-4",
   "ref":"Blagrove 2018 — HST reduce lesiones 50% y mejora economía +3% en fondistas",
   "exercises":[
    {"name":"Sentadilla Goblet","sets":3,"reps":"15","focus":"Glúteo medio, cuádriceps","notes":"Kettlebell frontal. Profundidad completa. Activa glúteo."},
    {"name":"Romanian Deadlift","sets":3,"reps":"12","focus":"Isquios + glúteo mayor","notes":"Cadena posterior. Clave economía trail. Rodillas ligeramente flexionadas."},
    {"name":"Step-Up con mancuerna","sets":3,"reps":"12/lado","focus":"Cuádriceps unilateral","notes":"Banco 40-50cm. Simula subida trail."},
    {"name":"Hip Thrust con barra","sets":3,"reps":"15","focus":"Glúteo máximo","notes":"Base de toda la cadena posterior. Progresión carga semanal."},
    {"name":"Nordic Hamstring Curl","sets":3,"reps":"6-8","focus":"Isquios excéntrico","notes":"El más importante. Evidencia Petersen 2011: −70% lesiones isquio."},
    {"name":"Calf Raise unilateral","sets":3,"reps":"15/lado","focus":"Sóleo + gastrocnemio","notes":"Excéntrico en la bajada (3s). Protege tendón de Aquiles."},
    {"name":"Dead Bug","sets":3,"reps":"10/lado","focus":"Core anti-extensión","notes":"Lumbar pegada al suelo siempre. Base estabilidad."},
    {"name":"Banded Clamshells","sets":3,"reps":"20/lado","focus":"Abductor cadera","notes":"Prevención IT band y rodilla corredor."},
    {"name":"Farmer Carries","sets":3,"reps":"30m","focus":"Core + trapecio","notes":"Simula mochila trail. Estabilidad lumbar en carga."},
   ]},
  {"id":"B","name":"FASE B — Fuerza Máxima","weeks":"9–16",
   "goal":"Aumentar fuerza máxima y potencia neuromuscular. Mejora directa de economía de carrera.",
   "freq":"2×/semana (Mar+Jue)","intensity":"4×4-6 reps | 80-85% 1RM | RIR 1-2",
   "ref":"Beattie 2017 — HST 16 sem: economía de carrera +4.6%, potencia +8.6%",
   "exercises":[
    {"name":"Sentadilla trasera","sets":4,"reps":"5","focus":"Potencia pierna global","notes":"Progresión lineal +2.5kg/sem. Técnica impecable."},
    {"name":"Peso Muerto convencional","sets":4,"reps":"4","focus":"Cadena posterior total","notes":"Carga máxima semana a semana. Cinturón si >85%1RM."},
    {"name":"Split Squat Búlgaro","sets":4,"reps":"6/lado","focus":"Unilateral trail-specific","notes":"Imprescindible. Con mancuernas o barra."},
    {"name":"Hip Thrust pesado","sets":4,"reps":"6","focus":"Glúteo mayor potencia","notes":"Velocity concéntrica máxima."},
    {"name":"Nordic Hamstring Curl","sets":4,"reps":"5","focus":"Isquios excéntrico","notes":"Mantiene protección lesional."},
    {"name":"Box Jump","sets":4,"reps":"5","focus":"Potencia concéntrica","notes":"Intro plyometría. Caída suave amortiguada. Evidencia: Mikkola 2007 — plyometría mejora RE 4.1%."},
    {"name":"Copenhagen Plank","sets":3,"reps":"20s/lado","focus":"Aductores + core lateral","notes":"Muy específico trail técnico. Progresión 5s/sem."},
    {"name":"Paloff Press","sets":3,"reps":"10/lado","focus":"Anti-rotación core","notes":"Estabilidad en terreno irregular."},
    {"name":"Single-leg RDL con mancuerna","sets":3,"reps":"8/lado","focus":"Isquio+glúteo+equilibrio","notes":"Propiocepción trail. Imprescindible."},
   ]},
  {"id":"C","name":"FASE C — Potencia + Específica Trail","weeks":"17–22",
   "goal":"Potencia explosiva, tolerancia excéntrica bajadas, mantenimiento fuerza bloque alto volumen.",
   "freq":"2×/sem (o 1× en semanas pico de volumen)","intensity":"3×4-6 fuerza + 3×8 plyométrico",
   "ref":"Heisten 2021 — plyometría+fuerza mejoran rendimiento ultra-trail en corredores experimentados",
   "exercises":[
    {"name":"Sentadilla + salto (Jump Squat)","sets":3,"reps":"5","focus":"Potencia pierna","notes":"Barra vacía o 20-30%1RM. Máxima velocidad concéntrica."},
    {"name":"Peso Muerto rumano unilateral","sets":3,"reps":"5/lado","focus":"Fuerza + propiocepción","notes":"Clave para control en bajadas técnicas."},
    {"name":"Depth Jump","sets":3,"reps":"5","focus":"Stiffness tendinosa","notes":"Cajón 50cm, caída + rebote mínimo. Simula impacto bajada trail."},
    {"name":"Hip Thrust explosivo","sets":3,"reps":"6","focus":"Potencia glúteo subidas","notes":"Velocidad en concéntrico máxima."},
    {"name":"Step-up Jump","sets":3,"reps":"6/lado","focus":"Específico subida trail","notes":"Impulso + aterrizaje controlado."},
    {"name":"Nordic Hamstring Curl","sets":3,"reps":"5","focus":"Mantenimiento isquios","notes":"No negociar. Semanas pico: 2 sets."},
    {"name":"Lateral Bound","sets":3,"reps":"8/lado","focus":"Estabilidad lateral","notes":"Trail técnico lateral. Aterriza suave."},
    {"name":"Copenhagen Plank progresivo","sets":3,"reps":"30s/lado","focus":"Aductores core","notes":"Progresión desde Fase B."},
    {"name":"Bear Crawl con peso","sets":3,"reps":"20m","focus":"Core + hombros","notes":"Integración para uso de bastones en carrera."},
   ]},
]

# ═══════════════════════════════════════════════════════════════════════════════
# PLAN NUTRICIONAL
# Base científica: Morton 2018, Burke 2011, Jeukendrup 2014, Phillips 2016, Yeo 2008
# ═══════════════════════════════════════════════════════════════════════════════
NUTRITION = {
  "overview":{
    "protein_g_kg":1.8,"weight":82,"target":76,
    "loss_rate":"~1kg/mes (déficit 300-400kcal solo en días descanso/rodaje suave)",
    "timeline":"6 meses para −6kg → 76kg en octubre",
    "evidence":"Morton 2018: 1.8g/kg proteína preserva masa muscular en déficit. Phillips 2016: proteína alta protege músculo durante pérdida de peso.",
  },
  "day_types":[
    {"type":"Descanso","kcal":2100,"cho":180,"prot":148,"fat":65,
     "color":"#334155","icon":"🌙",
     "desc":"Déficit 400kcal. Bajo en CHO, alto proteína y vegetales. Prioriza verdura no almidón.",
     "example":"Desayuno: 3 huevos + espinacas + café. Comida: 200g pollo + ensalada grande + 50g legumbres. Cena: salmón + brócoli + yogur griego."},
    {"type":"Rodaje Z1 (<10km)","kcal":2400,"cho":250,"prot":148,"fat":70,
     "color":"#0f766e","icon":"🟢",
     "desc":"Déficit leve 200kcal. CHO moderado. Sin gel necesario. Algunos de estos en ayunas (train-low).",
     "example":"Desayuno post-run: 80g avena + plátano + 30g proteína whey. Comida: 150g arroz + 200g pollo + verdura. Cena: 150g salmón + boniato pequeño."},
    {"type":"Sesión calidad / Intervalos","kcal":2900,"cho":380,"prot":148,"fat":65,
     "color":"#b45309","icon":"🟡",
     "desc":"Sin déficit. CHO alto pre y post sesión. Energía disponible para rendir.",
     "example":"Pre-run (2.5h antes): 60g avena + plátano + miel (80g CHO). Post-run <30min: batido 300ml leche + 30g whey + plátano + 30g miel."},
    {"type":"Long Run / B2B","kcal":3400,"cho":480,"prot":165,"fat":80,
     "color":"#1e40af","icon":"🔵",
     "desc":"Superávit leve. Máximo CHO. Recuperación muscular prioritaria.",
     "example":"Pre-long (3h antes): 150g arroz + 100g pollo + plátano. Durante: gel c/35-40min. Post: 200g pasta + 150g carne + 500ml leche chocolatada."},
    {"type":"Carb Loading (3 días pre-carrera)","kcal":4000,"cho":700,"prot":130,"fat":60,
     "color":"#7e22ce","icon":"⚡",
     "desc":"8-10g CHO/kg/día (day1: 8g → day3: 10g). Reduce proteína y grasa. Sin fibra. Sin alimentos nuevos.",
     "example":"Día 3 (víspera): 200g pasta (almuerzo) + 200g arroz (cena) + 3 plátanos + 2 bebidas isotónicas + pan blanco + mermelada."},
  ],
  "race_nutrition":{
    "target_cho_hr":70,"target_g_per_gel":22,
    "gel_frequency_min":35,
    "gels_palencia":6,"gels_tp60":10,
    "hydration_ml_hr":600,
    "electrolytes":"Sodio 500-700mg/h en carrera >3h. Tabletas electrolitos en avituallamientos.",
    "evidence":"Jeukendrup 2014 — ratio glucosa:fructosa 2:1 permite absorción hasta 90g CHO/h. Para 82kg: 66-74g CHO/h óptimo.",
    "notes":[
      "Practica EXACTAMENTE el mismo gel/bebida que usarás en carrera (stomach training).",
      "No probar nada nuevo en race day.",
      "Si sensación de náusea: reduce CHO/h a 45-50g y aumenta electrolitos.",
      "Cafeína 3mg/kg (≈250mg) en segunda mitad de carrera si la usas habitualmente.",
    ],
  },
  "supplements":{
    "evidence_based":[
      {"name":"Proteína Whey","dose":"30-40g post-sesión","evidence":"Morton 2018 — óptimo. Prioridad si no alcanzas 1.8g/kg/día con comida."},
      {"name":"Cafeína","dose":"3mg/kg (≈250mg) 45min antes sesión calidad / segunda mitad carrera","evidence":"Spriet 2014 — mejora rendimiento 2-4% en endurance. Solo si toleras bien."},
      {"name":"Beta-Alanina","dose":"3.2g/día (en 2 tomas para reducir parestesias)","evidence":"Hobson 2012 — mejora rendimiento en esfuerzos 1-10min Z4-Z5. Útil para intervalos."},
      {"name":"Creatina","dose":"3-5g/día (no requiere carga)","evidence":"Rawson 2011 — mejora fuerza máxima y recuperación. Compatible con resistencia. Puede añadir 0.5-1kg de agua."},
      {"name":"Vitamina D3","dose":"2000-4000 UI/día en invierno/primavera","evidence":"Larson-Meyer 2010 — déficit frecuente en deportistas. Afecta fuerza y recuperación."},
      {"name":"Omega-3","dose":"2-3g EPA+DHA/día","evidence":"Philpott 2018 — reduce inflamación post-esfuerzo. Mejora recuperación en bloque alto."},
    ],
    "not_recommended":["BCAA (innecesario si proteína total adecuada)","Pre-workouts con estimulantes mezclados","Antioxidantes dosis altas (pueden bloquear adaptaciones)"],
  },
}

# ═══════════════════════════════════════════════════════════════════════════════
# GENERADOR HTML
# ═══════════════════════════════════════════════════════════════════════════════
PHASE_COLORS = {1:"#f97316",2:"#f59e0b",3:"#22d3ee",4:"#a78bfa",5:"#34d399"}
SESSION_CONFIG = {
    "REST":    {"bg":"#1e293b","border":"#334155","label":"REST"},
    "EASY":    {"bg":"#0f2d2d","border":"#22d3ee","label":"EASY Z1-Z2"},
    "REC":     {"bg":"#1a1f2e","border":"#475569","label":"RECOVERY"},
    "TEMPO":   {"bg":"#1a2f0f","border":"#84cc16","label":"TEMPO Z3"},
    "INTERVAL":{"bg":"#2d1a0f","border":"#f97316","label":"INTERVALOS Z4"},
    "LONG":    {"bg":"#0f1a2d","border":"#6366f1","label":"LONG RUN"},
    "TRAIL":   {"bg":"#1a1008","border":"#d97706","label":"TRAIL Z2"},
    "GYM":     {"bg":"#1a0f2d","border":"#a78bfa","label":"GYM FUERZA"},
    "B2B":     {"bg":"#2d1010","border":"#ef4444","label":"B2B TRAIL"},
    "RACE":    {"bg":"#2d1f00","border":"#fbbf24","label":"🏁 CARRERA"},
    "VK":      {"bg":"#2d0f1a","border":"#f43f5e","label":"VERTICAL KM"},
}

def fmt_date(week_num, day_idx):
    """Get formatted date for a given week and day (0=Mon)."""
    start = PLAN_START + timedelta(weeks=week_num-1, days=day_idx)
    return start.strftime("%d %b")

def generate_html(strava_data, athlete_profile):
    weekly_data = strava_data.get("weeks", [])
    hr_max      = strava_data.get("hr_max", 186)
    
    # Build Strava chart data
    chart_labels   = [w[0][5:] for w in weekly_data[-12:]]  # last 12 weeks
    chart_km       = [round(w[1]["km"],1) for w in weekly_data[-12:]]
    chart_d_plus   = [w[1]["d_plus"] for w in weekly_data[-12:]]
    chart_time     = [w[1]["time_min"] for w in weekly_data[-12:]]
    chart_trail    = [w[1]["trail_pct"] for w in weekly_data[-12:]]

    # Plan phase colors for HTML
    def session_html(s, week_num, day_idx):
        cfg = SESSION_CONFIG.get(s["type"], SESSION_CONFIG["EASY"])
        date_str = fmt_date(week_num, ["L","M","X","J","V","S","D"].index(s["day"]))
        km_str = f"<span class='sess-km'>{s['km']}km" + (f" ↑{s['d']}m" if s["d"]>0 else "") + "</span>" if s["km"]>0 else ""
        return f"""
        <div class='session-card' style='background:{cfg["bg"]};border-left:3px solid {cfg["border"]}'>
          <div class='sess-header'>
            <span class='sess-day'>{s["day"]}</span>
            <span class='sess-type' style='color:{cfg["border"]}'>{cfg["label"]}</span>
            {km_str}
            <span class='sess-date'>{date_str}</span>
          </div>
          <p class='sess-desc'>{s["desc"]}</p>
        </div>"""

    def week_html(w):
        pc = PHASE_COLORS.get(w["phase"], "#666")
        load_colors = {"LOW":"#22d3ee","LOW-MED":"#84cc16","MED":"#f59e0b",
                       "MED-HIGH":"#f97316","HIGH":"#ef4444","RACE":"#fbbf24","RACE":"#fbbf24"}
        lc = load_colors.get(w["load"],"#666")
        sessions = "".join(session_html(s, w["week"], i) for i,s in enumerate(w["sessions"]))
        notes_html = f"<div class='week-notes'>📌 {w['notes']}</div>" if w.get("notes") else ""
        wstart = (PLAN_START + timedelta(weeks=w["week"]-1)).strftime("%d %b")
        wend   = (PLAN_START + timedelta(weeks=w["week"]-1, days=6)).strftime("%d %b")
        return f"""
        <details class='week-item'>
          <summary class='week-summary'>
            <span class='wk-num' style='background:{pc}22;color:{pc}'>Sem {w["week"]}</span>
            <span class='wk-dates'>{wstart} – {wend}</span>
            <span class='wk-title'>{w["title"]}</span>
            <span class='wk-stats'>{w["km"]}km · ↑{w["d_plus"]}m D+</span>
            <span class='wk-load' style='background:{lc}22;color:{lc}'>{w["load"]}</span>
          </summary>
          <div class='week-body'>
            {notes_html}
            <div class='sessions-grid'>{sessions}</div>
          </div>
        </details>"""

    # Group weeks by phase
    phases = {}
    for w in PLAN:
        p = w["phase"]
        if p not in phases: phases[p] = []
        phases[p].append(w)

    phase_names = {1:"BASE AERÓBICA",2:"DESARROLLO TRAIL",
                   3:"BLOQUE SIERRA",4:"TAPER + PALENCIA",5:"RECOVERY + TP60"}

    phases_html = ""
    for pid, weeks in phases.items():
        pc = PHASE_COLORS[pid]
        pname = phase_names[pid]
        w_start = weeks[0]["week"]; w_end = weeks[-1]["week"]
        total_km = sum(w["km"] for w in weeks)
        total_d  = sum(w["d_plus"] for w in weeks)
        wks_html = "".join(week_html(w) for w in weeks)
        phases_html += f"""
        <div class='phase-block'>
          <div class='phase-header' style='border-left:4px solid {pc}'>
            <div class='phase-title' style='color:{pc}'>FASE {pid}: {pname}</div>
            <div class='phase-meta'>
              Semanas {w_start}–{w_end} &nbsp;·&nbsp; {total_km} km totales &nbsp;·&nbsp; {total_d:,}m D+ acumulado
            </div>
          </div>
          <div class='weeks-list'>{wks_html}</div>
        </div>"""

    # Strength HTML
    def strength_phase_html(sp):
        exs = "".join(f"""
          <tr>
            <td class='ex-name'>{e["name"]}</td>
            <td>{e["sets"]}×{e["reps"]}</td>
            <td class='ex-focus'>{e["focus"]}</td>
            <td class='ex-notes'>{e["notes"]}</td>
          </tr>""" for e in sp["exercises"])
        return f"""
        <div class='strength-phase'>
          <div class='sp-header'>
            <span class='sp-id'>FASE {sp["id"]}</span>
            <span class='sp-name'>{sp["name"]}</span>
            <span class='sp-weeks'>Sem {sp["weeks"]}</span>
          </div>
          <div class='sp-meta'>
            <span>🎯 {sp["goal"]}</span>
            <span>📅 {sp["freq"]}</span>
            <span>⚡ {sp["intensity"]}</span>
          </div>
          <div class='sp-ref'>📚 {sp["ref"]}</div>
          <table class='ex-table'>
            <thead><tr><th>Ejercicio</th><th>Series×Reps</th><th>Foco</th><th>Notas</th></tr></thead>
            <tbody>{exs}</tbody>
          </table>
        </div>"""

    strength_html = "".join(strength_phase_html(sp) for sp in STRENGTH)

    # Nutrition HTML
    def nutr_day_html(dt):
        return f"""
        <div class='nutr-day' style='border-top:3px solid {dt["color"]}'>
          <div class='nd-header'>
            <span class='nd-icon'>{dt["icon"]}</span>
            <span class='nd-type'>{dt["type"]}</span>
            <span class='nd-kcal'>{dt["kcal"]} kcal</span>
          </div>
          <div class='nd-macros'>
            <span class='macro cho'>CHO: {dt["cho"]}g</span>
            <span class='macro prot'>Prot: {dt["prot"]}g</span>
            <span class='macro fat'>Grasa: {dt["fat"]}g</span>
          </div>
          <p class='nd-desc'>{dt["desc"]}</p>
          <p class='nd-example'>{dt["example"]}</p>
        </div>"""

    nutr_html = "".join(nutr_day_html(dt) for dt in NUTRITION["day_types"])

    supps_html = "".join(f"""
      <div class='supp-item'>
        <div class='supp-name'>{s["name"]}</div>
        <div class='supp-dose'>{s["dose"]}</div>
        <div class='supp-ev'>{s["evidence"]}</div>
      </div>""" for s in NUTRITION["supplements"]["evidence_based"])

    # Race countdown
    today = date.today()
    races_countdown = ""
    for r in ATHLETE["races"]:
        rd = date.fromisoformat(r["date"])
        days_left = (rd - today).days
        races_countdown += f"""
        <div class='race-card' style='border-color:{r["accent"]}'>
          <div class='rc-name' style='color:{r["accent"]}'>{r["name"]}</div>
          <div class='rc-info'>{r["km"]}km · {r["d_plus"]:,}m D+</div>
          <div class='rc-days' style='color:{r["accent"]}'>{days_left}</div>
          <div class='rc-label'>días</div>
          <div class='rc-date'>{rd.strftime("%d %b %Y")}</div>
        </div>"""

    # Strava profile
    prof = athlete_profile or {}
    name = prof.get("firstname","") + " " + prof.get("lastname","")
    city = prof.get("city","Madrid")
    ytd  = prof.get("ytd_run_totals",{})
    ytd_km = round(ytd.get("distance",0)/1000,1) if ytd else "—"

    plan_data_json = json.dumps([{"week":w["week"],"phase":w["phase"],"km":w["km"],"d_plus":w["d_plus"]} for w in PLAN])

    chart_data = json.dumps({
        "labels": chart_labels, "km": chart_km,
        "d_plus": chart_d_plus, "time": chart_time, "trail": chart_trail,
        "hr_max": hr_max
    })

    # Zones based on VT1/VT2 lab data (not generic % FCmax)
    vt1 = ATHLETE.get("vt1", 152)
    vt2 = ATHLETE.get("vt2", 172)
    zones_ref = [
        {"lo": 0,       "hi": vt1-10, "name":"Z1 Recuperación",  "color":"#64748b", "desc":f"< {vt1-10} bpm — Regenerativo, conversación fácil"},
        {"lo": vt1-10,  "hi": vt1,    "name":"Z2 Aeróbico",      "color":"#22d3ee", "desc":f"{vt1-10}–{vt1} bpm — Base aeróbica, justo debajo de VT1"},
        {"lo": vt1,     "hi": vt2,    "name":"Z3 Tempo",         "color":"#84cc16", "desc":f"{vt1}–{vt2} bpm — Entre umbrales, frases cortas"},
        {"lo": vt2,     "hi": vt2+8,  "name":"Z4 Umbral",        "color":"#f97316", "desc":f"{vt2}–{vt2+8} bpm — Por encima de VT2, insostenible >20min"},
        {"lo": vt2+8,   "hi": hr_max, "name":"Z5 VO2max",        "color":"#ef4444", "desc":f"{vt2+8}–{hr_max} bpm — Máximo esfuerzo"},
    ]

    zones_html = "".join(f"""
      <div class='zone-row'>
        <span class='z-dot' style='background:{z["color"]}'></span>
        <span class='z-name'>{z["name"]}</span>
        <span class='z-range'>{z["lo"]}–{z["hi"]} bpm</span>
        <span class='z-pct'>{z["desc"]}</span>
      </div>""" for z in zones_ref)

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Trail 360° — Jose / Temporada 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Crimson+Pro:wght@400;500&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
:root{{
  --bg:#080d16;--surface:#0d1421;--surface2:#111827;--surface3:#1e293b;
  --border:#1e2d45;--text:#e2e8f0;--muted:#64748b;--accent:#22d3ee;
  --amber:#f59e0b;--orange:#f97316;--red:#ef4444;--green:#84cc16;
  --purple:#a78bfa;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{background:var(--bg);color:var(--text);font-family:'Crimson Pro',serif;font-size:15px;line-height:1.6;min-height:100vh}}
body::before{{content:'';position:fixed;inset:0;background:
  radial-gradient(ellipse 80% 50% at 20% 0%,#0c1f3a 0%,transparent 60%),
  radial-gradient(ellipse 60% 40% at 80% 100%,#0a1a2e 0%,transparent 55%);
  pointer-events:none;z-index:0}}

/* TOPOGRAPHIC PATTERN */
body::after{{content:'';position:fixed;inset:0;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cpath d='M0 100 Q50 70 100 100 Q150 130 200 100' fill='none' stroke='%230f2040' stroke-width='1.5'/%3E%3Cpath d='M0 130 Q50 100 100 130 Q150 160 200 130' fill='none' stroke='%230f2040' stroke-width='1'/%3E%3Cpath d='M0 70 Q50 40 100 70 Q150 100 200 70' fill='none' stroke='%230f2040' stroke-width='1'/%3E%3Cpath d='M0 160 Q50 130 100 160 Q150 190 200 160' fill='none' stroke='%230c1a30' stroke-width='1'/%3E%3Cpath d='M0 40 Q50 10 100 40 Q150 70 200 40' fill='none' stroke='%230c1a30' stroke-width='1'/%3E%3C/svg%3E");
  opacity:.4;pointer-events:none;z-index:0}}

/* LAYOUT */
#app{{position:relative;z-index:1;max-width:1200px;margin:0 auto;padding:0 20px 60px}}

/* HEADER */
header{{padding:32px 0 20px;border-bottom:1px solid var(--border);margin-bottom:28px}}
.header-top{{display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;gap:16px}}
.brand{{display:flex;flex-direction:column;gap:4px}}
.brand-title{{font-family:'Rajdhani',sans-serif;font-size:28px;font-weight:700;
  letter-spacing:3px;text-transform:uppercase;
  background:linear-gradient(135deg,var(--accent),var(--amber));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent}}
.brand-sub{{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--muted);letter-spacing:2px}}
.races-header{{display:flex;gap:12px;flex-wrap:wrap}}
.race-card{{background:var(--surface2);border:1px solid var(--border);border-radius:10px;
  padding:14px 18px;text-align:center;min-width:140px;
  transition:transform .2s,box-shadow .2s;cursor:default}}
.race-card:hover{{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.5)}}
.rc-name{{font-family:'Rajdhani',sans-serif;font-size:11px;font-weight:600;letter-spacing:1px;margin-bottom:2px}}
.rc-info{{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--muted);margin-bottom:8px}}
.rc-days{{font-family:'Rajdhani',sans-serif;font-size:42px;font-weight:700;line-height:1}}
.rc-label{{font-size:10px;color:var(--muted);letter-spacing:2px;text-transform:uppercase;margin-bottom:4px}}
.rc-date{{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--muted)}}

/* TABS */
.tabs{{display:flex;gap:4px;margin-bottom:28px;border-bottom:1px solid var(--border);padding-bottom:0;overflow-x:auto}}
.tab-btn{{font-family:'Rajdhani',sans-serif;font-weight:600;letter-spacing:1px;font-size:13px;
  text-transform:uppercase;background:transparent;border:none;color:var(--muted);
  padding:10px 18px;cursor:pointer;border-bottom:2px solid transparent;
  transition:color .2s,border-color .2s;white-space:nowrap}}
.tab-btn:hover{{color:var(--text)}}
.tab-btn.active{{color:var(--accent);border-bottom-color:var(--accent)}}
.tab-panel{{display:none}}
.tab-panel.active{{display:block}}

/* STRAVA ANALYSIS */
.stats-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin-bottom:28px}}
.stat-card{{background:var(--surface2);border:1px solid var(--border);border-radius:10px;padding:16px;text-align:center}}
.stat-value{{font-family:'JetBrains Mono',monospace;font-size:28px;font-weight:500;
  background:linear-gradient(135deg,var(--accent),var(--amber));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent}}
.stat-label{{font-family:'Rajdhani',sans-serif;font-size:11px;color:var(--muted);letter-spacing:1px;text-transform:uppercase;margin-top:4px}}
.charts-grid{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:28px}}
.chart-box{{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px}}
.chart-title{{font-family:'Rajdhani',sans-serif;font-size:13px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;margin-bottom:16px}}
.chart-box canvas{{max-height:200px}}
.zones-panel{{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:16px}}
.zones-title{{font-family:'Rajdhani',sans-serif;font-size:13px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;margin-bottom:16px}}
.zone-row{{display:flex;align-items:center;gap:12px;padding:8px 0;border-bottom:1px solid var(--border)}}
.zone-row:last-child{{border-bottom:none}}
.z-dot{{width:10px;height:10px;border-radius:50%;flex-shrink:0}}
.z-name{{flex:1;font-family:'Rajdhani',sans-serif;font-weight:600;font-size:13px}}
.z-range{{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--accent);min-width:100px}}
.z-pct{{font-size:12px;color:var(--muted)}}

/* PLAN */
.phase-block{{margin-bottom:32px}}
.phase-header{{padding:16px 20px;background:var(--surface2);border-radius:10px 10px 0 0;margin-bottom:2px}}
.phase-title{{font-family:'Rajdhani',sans-serif;font-size:16px;font-weight:700;letter-spacing:2px;text-transform:uppercase}}
.phase-meta{{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--muted);margin-top:4px}}
.weeks-list{{display:flex;flex-direction:column;gap:2px}}
.week-item{{background:var(--surface2);border-radius:0}}
.week-item:last-child{{border-radius:0 0 10px 10px}}
.week-summary{{list-style:none;display:flex;align-items:center;gap:12px;padding:12px 16px;
  cursor:pointer;flex-wrap:wrap;transition:background .15s}}
.week-summary:hover{{background:var(--surface3)}}
.week-summary::-webkit-details-marker{{display:none}}
details[open] .week-summary{{background:var(--surface3)}}
.wk-num{{font-family:'JetBrains Mono',monospace;font-size:11px;padding:3px 8px;border-radius:4px;flex-shrink:0}}
.wk-dates{{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--muted);min-width:90px}}
.wk-title{{flex:1;font-family:'Rajdhani',sans-serif;font-size:14px;font-weight:600}}
.wk-stats{{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--accent)}}
.wk-load{{font-size:10px;font-family:'Rajdhani',sans-serif;letter-spacing:1px;padding:2px 8px;border-radius:20px;flex-shrink:0}}
.week-body{{padding:12px 16px;border-top:1px solid var(--border)}}
.week-notes{{background:#162032;border-left:3px solid var(--amber);padding:10px 14px;
  border-radius:0 6px 6px 0;margin-bottom:14px;font-size:13px;color:#cbd5e1}}
.sessions-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:8px}}
.session-card{{padding:10px 12px;border-radius:6px}}
.sess-header{{display:flex;align-items:center;gap:8px;margin-bottom:4px;flex-wrap:wrap}}
.sess-day{{font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:500;
  background:var(--surface3);padding:2px 7px;border-radius:4px;flex-shrink:0}}
.sess-type{{font-family:'Rajdhani',sans-serif;font-size:11px;font-weight:600;letter-spacing:1px;flex:1}}
.sess-km{{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--muted)}}
.sess-date{{font-size:10px;color:var(--muted);margin-left:auto}}
.sess-desc{{font-size:13px;color:#94a3b8;line-height:1.5}}

/* FUERZA */
.strength-phase{{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:24px;margin-bottom:20px}}
.sp-header{{display:flex;align-items:center;gap:12px;margin-bottom:12px;flex-wrap:wrap}}
.sp-id{{font-family:'Rajdhani',sans-serif;font-size:20px;font-weight:700;color:var(--purple)}}
.sp-name{{font-family:'Rajdhani',sans-serif;font-size:16px;font-weight:600;flex:1}}
.sp-weeks{{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--muted);
  background:var(--surface3);padding:3px 9px;border-radius:4px}}
.sp-meta{{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:8px}}
.sp-meta span{{font-size:13px;color:#94a3b8}}
.sp-ref{{font-size:12px;color:var(--purple);margin-bottom:16px;font-style:italic}}
.ex-table{{width:100%;border-collapse:collapse;font-size:13px}}
.ex-table th{{font-family:'Rajdhani',sans-serif;font-size:11px;letter-spacing:1px;
  text-transform:uppercase;color:var(--muted);text-align:left;padding:8px 10px;
  border-bottom:1px solid var(--border)}}
.ex-table td{{padding:9px 10px;border-bottom:1px solid var(--border);vertical-align:top}}
.ex-table tr:last-child td{{border-bottom:none}}
.ex-name{{font-weight:600;color:var(--text)}}
.ex-focus{{color:var(--amber);font-size:12px}}
.ex-notes{{color:#94a3b8;font-size:12px}}

/* NUTRICIÓN */
.nutr-overview{{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:20px}}
.nutr-overview h3{{font-family:'Rajdhani',sans-serif;font-size:14px;letter-spacing:1px;
  color:var(--muted);text-transform:uppercase;margin-bottom:12px}}
.nutr-kv{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px}}
.kv-item{{background:var(--surface3);border-radius:8px;padding:10px 14px}}
.kv-label{{font-size:11px;color:var(--muted);margin-bottom:2px}}
.kv-value{{font-family:'Rajdhani',sans-serif;font-size:14px;font-weight:600;color:var(--green)}}
.nutr-days{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px;margin-bottom:24px}}
.nutr-day{{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:18px}}
.nd-header{{display:flex;align-items:center;gap:10px;margin-bottom:10px}}
.nd-icon{{font-size:20px}}
.nd-type{{font-family:'Rajdhani',sans-serif;font-size:14px;font-weight:600;flex:1}}
.nd-kcal{{font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--amber)}}
.nd-macros{{display:flex;gap:8px;margin-bottom:8px;flex-wrap:wrap}}
.macro{{font-family:'JetBrains Mono',monospace;font-size:11px;padding:3px 8px;border-radius:4px;background:var(--surface3)}}
.macro.cho{{color:#f59e0b}}.macro.prot{{color:#22d3ee}}.macro.fat{{color:#a78bfa}}
.nd-desc{{font-size:13px;color:#94a3b8;margin-bottom:6px}}
.nd-example{{font-size:12px;color:var(--muted);font-style:italic;border-top:1px solid var(--border);padding-top:6px;margin-top:6px}}
.race-nutr{{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:20px}}
.race-nutr h3{{font-family:'Rajdhani',sans-serif;font-size:14px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;margin-bottom:14px}}
.rn-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;margin-bottom:14px}}
.rn-item{{background:var(--surface3);border-radius:8px;padding:10px 14px}}
.rn-label{{font-size:11px;color:var(--muted);margin-bottom:2px}}
.rn-val{{font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--orange)}}
.supps{{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px}}
.supps h3{{font-family:'Rajdhani',sans-serif;font-size:14px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;margin-bottom:14px}}
.supp-item{{border-bottom:1px solid var(--border);padding:12px 0}}
.supp-item:last-child{{border-bottom:none}}
.supp-name{{font-family:'Rajdhani',sans-serif;font-size:15px;font-weight:600;margin-bottom:2px}}
.supp-dose{{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--accent);margin-bottom:3px}}
.supp-ev{{font-size:12px;color:var(--muted)}}

/* SEGUIMIENTO */
.compliance-intro{{background:var(--surface2);border:1px solid var(--border);border-radius:12px;
  padding:20px;margin-bottom:20px}}
.compliance-intro p{{font-size:14px;color:#94a3b8;line-height:1.7}}
.compliance-table-wrap{{overflow-x:auto}}
.compliance-table{{width:100%;border-collapse:collapse;font-size:13px}}
.compliance-table th{{font-family:'Rajdhani',sans-serif;font-size:11px;letter-spacing:1px;
  text-transform:uppercase;color:var(--muted);padding:10px 12px;border-bottom:1px solid var(--border);text-align:left;white-space:nowrap}}
.compliance-table td{{padding:10px 12px;border-bottom:1px solid var(--border);vertical-align:middle}}
.compliance-table tr:nth-child(even) td{{background:rgba(255,255,255,.02)}}
.ct-week{{font-family:'JetBrains Mono',monospace;font-size:11px}}
.ct-plan{{color:var(--accent);font-family:'JetBrains Mono',monospace;font-size:12px}}
.ct-actual{{color:var(--amber);font-family:'JetBrains Mono',monospace;font-size:12px}}
.ct-pct{{font-family:'Rajdhani',sans-serif;font-size:13px;font-weight:600}}
.bar-wrap{{width:80px;height:8px;background:var(--surface3);border-radius:4px;overflow:hidden}}
.bar-fill{{height:100%;border-radius:4px;background:var(--accent);transition:width .3s}}
.no-data{{color:var(--muted);font-style:italic;font-size:12px}}

@media(max-width:768px){{
  .charts-grid{{grid-template-columns:1fr}}
  .header-top{{flex-direction:column}}
  .races-header{{gap:8px}}
  .wk-title{{width:100%}}
  .ex-table .ex-focus,.ex-table .ex-notes{{display:none}}
}}
</style>
</head>
<body>
<div id="app">

<header>
  <div class="header-top">
    <div class="brand">
      <div class="brand-title">Trail 360° — Temporada 2026</div>
      <div class="brand-sub">PALENCIA MTN 44km/3500m · TP60 63km/2500m · Madrid, España</div>
    </div>
    <div class="races-header">{races_countdown}</div>
  </div>
</header>

<nav class="tabs">
  <button class="tab-btn active" onclick="switchTab('strava')">📊 Análisis Strava</button>
  <button class="tab-btn" onclick="switchTab('plan')">🗓 Plan Entrenamiento</button>
  <button class="tab-btn" onclick="switchTab('fuerza')">💪 Fuerza</button>
  <button class="tab-btn" onclick="switchTab('nutricion')">🥗 Nutrición</button>
  <button class="tab-btn" onclick="switchTab('seguimiento')">📈 Seguimiento</button>
</nav>

<!-- ═══ TAB: STRAVA ═══ -->
<div id="tab-strava" class="tab-panel active">
  <div class="stats-grid" id="strava-stats">
    <div class="stat-card">
      <div class="stat-value" id="sv-weeks">—</div>
      <div class="stat-label">Semanas analizadas</div>
    </div>
    <div class="stat-card">
      <div class="stat-value" id="sv-km">—</div>
      <div class="stat-label">km totales período</div>
    </div>
    <div class="stat-card">
      <div class="stat-value" id="sv-d">—</div>
      <div class="stat-label">m D+ período</div>
    </div>
    <div class="stat-card">
      <div class="stat-value" id="sv-avg-km">—</div>
      <div class="stat-label">km / semana promedio</div>
    </div>
    <div class="stat-card">
      <div class="stat-value" id="sv-hr">—</div>
      <div class="stat-label">FC máx registrada</div>
    </div>
    <div class="stat-card">
      <div class="stat-value" id="sv-trail">—</div>
      <div class="stat-label">% trail avg</div>
    </div>
  </div>

  <div class="charts-grid">
    <div class="chart-box">
      <div class="chart-title">Volumen semanal — km</div>
      <canvas id="chartKm"></canvas>
    </div>
    <div class="chart-box">
      <div class="chart-title">Desnivel positivo semanal — m</div>
      <canvas id="chartD"></canvas>
    </div>
    <div class="chart-box">
      <div class="chart-title">Tiempo de carrera — minutos</div>
      <canvas id="chartTime"></canvas>
    </div>
    <div class="chart-box">
      <div class="chart-title">% Sesiones Trail vs Road</div>
      <canvas id="chartTrail"></canvas>
    </div>
  </div>

  <div class="zones-panel">
    <div class="zones-title">Zonas de FC para entrenamiento — FCmax: <span id="hr-max-val">—</span> bpm</div>
    {zones_html}
    <p style="font-size:12px;color:var(--muted);margin-top:12px">📚 Zonas calculadas según modelo 5-zonas Seiler/Coggan. 80% del volumen en Z1–Z2, 20% en Z3–Z5 (Seiler 2010 — distribución polarizada).</p>
  </div>
</div>

<!-- ═══ TAB: PLAN ═══ -->
<div id="tab-plan" class="tab-panel">
  <div style="background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:24px">
    <h3 style="font-family:'Rajdhani',sans-serif;font-size:14px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;margin-bottom:12px">Resumen del Plan — 25 semanas</h3>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px">
      <div style="background:var(--surface3);border-radius:8px;padding:12px">
        <div style="font-size:11px;color:var(--muted)">Inicio plan</div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--accent)">24 Mar 2026</div>
      </div>
      <div style="background:var(--surface3);border-radius:8px;padding:12px">
        <div style="font-size:11px;color:var(--muted)">Palencia MTN</div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:13px;color:#f97316">14 Jun 2026 (Sem 12)</div>
      </div>
      <div style="background:var(--surface3);border-radius:8px;padding:12px">
        <div style="font-size:11px;color:var(--muted)">TP60</div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:13px;color:#22d3ee">10 Oct 2026 (Sem 25)</div>
      </div>
      <div style="background:var(--surface3);border-radius:8px;padding:12px">
        <div style="font-size:11px;color:var(--muted)">Volumen pico</div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:13px;color:#f59e0b">80km / 4500m D+ (Sem 18)</div>
      </div>
      <div style="background:var(--surface3);border-radius:8px;padding:12px">
        <div style="font-size:11px;color:var(--muted)">Metodología</div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:13px;color:#84cc16">Polarizada 80/20 + Bloques</div>
      </div>
      <div style="background:var(--surface3);border-radius:8px;padding:12px">
        <div style="font-size:11px;color:var(--muted)">Fuerza</div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:13px;color:#a78bfa">2×/semana todo el ciclo</div>
      </div>
    </div>
  </div>
  {phases_html}
</div>

<!-- ═══ TAB: FUERZA ═══ -->
<div id="tab-fuerza" class="tab-panel">
  <div style="background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:20px">
    <h3 style="font-family:'Rajdhani',sans-serif;font-size:14px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;margin-bottom:12px">Principios base — Evidencia científica</h3>
    <ul style="list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:8px">
      <li style="font-size:13px;color:#94a3b8;padding:8px 12px;background:var(--surface3);border-radius:6px">💪 Beattie 2017: HST 16 sem → economía carrera +4.6%, potencia +8.6%</li>
      <li style="font-size:13px;color:#94a3b8;padding:8px 12px;background:var(--surface3);border-radius:6px">🦵 Petersen 2011: Nordic curl → −70% incidencia lesiones isquiosurales</li>
      <li style="font-size:13px;color:#94a3b8;padding:8px 12px;background:var(--surface3);border-radius:6px">🏃 Blagrove 2018: HST reduce lesiones 50% en fondistas competitivos</li>
      <li style="font-size:13px;color:#94a3b8;padding:8px 12px;background:var(--surface3);border-radius:6px">⚡ Mikkola 2007: plyometría 8 sem → economía carrera +4.1%</li>
      <li style="font-size:13px;color:#94a3b8;padding:8px 12px;background:var(--surface3);border-radius:6px">🏔 Heisten 2021: fuerza+plyometría mejoran rendimiento en ultra-trail</li>
      <li style="font-size:13px;color:#94a3b8;padding:8px 12px;background:var(--surface3);border-radius:6px">📐 Principio: NUNCA fuerza el día antes de sesión calidad o long run</li>
    </ul>
  </div>
  {strength_html}
</div>

<!-- ═══ TAB: NUTRICIÓN ═══ -->
<div id="tab-nutricion" class="tab-panel">
  <div class="nutr-overview">
    <h3>Plan Nutricional — Bases</h3>
    <div class="nutr-kv">
      <div class="kv-item"><div class="kv-label">Proteína objetivo</div><div class="kv-value">1.8g/kg → 148g/día</div></div>
      <div class="kv-item"><div class="kv-label">Peso actual / objetivo</div><div class="kv-value">82kg → 76kg (−6kg)</div></div>
      <div class="kv-item"><div class="kv-label">Ritmo de pérdida</div><div class="kv-value">~1kg/mes (realista)</div></div>
      <div class="kv-item"><div class="kv-label">Timeline</div><div class="kv-value">6 meses → oct 2026</div></div>
      <div class="kv-item"><div class="kv-label">Estrategia déficit</div><div class="kv-value">Solo días descanso/Z1 corto</div></div>
      <div class="kv-item"><div class="kv-label">Evidence base</div><div class="kv-value">Morton 2018 + Burke 2011</div></div>
    </div>
  </div>
  <h3 style="font-family:'Rajdhani',sans-serif;font-size:14px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;margin-bottom:14px">Plantillas por tipo de día</h3>
  <div class="nutr-days">{nutr_html}</div>

  <div class="race-nutr">
    <h3>Nutrición en Carrera</h3>
    <div class="rn-grid">
      <div class="rn-item"><div class="rn-label">CHO objetivo por hora</div><div class="rn-val">70g/h (glucosa:fructosa 2:1)</div></div>
      <div class="rn-item"><div class="rn-label">Frecuencia geles</div><div class="rn-val">Cada 35 minutos</div></div>
      <div class="rn-item"><div class="rn-label">Geles Palencia (44km)</div><div class="rn-val">~6 geles</div></div>
      <div class="rn-item"><div class="rn-label">Geles TP60 (63km)</div><div class="rn-val">~10 geles</div></div>
      <div class="rn-item"><div class="rn-label">Hidratación</div><div class="rn-val">500-700ml/hora</div></div>
      <div class="rn-item"><div class="rn-label">Sodio >3h</div><div class="rn-val">500-700mg/hora</div></div>
    </div>
    <p style="font-size:13px;color:#94a3b8;margin-bottom:8px">📚 Evidencia: Jeukendrup 2014 — ratio glucosa:fructosa 2:1 permite absorción hasta 90g CHO/h sin problemas GI. Para 82kg: 66-74g CHO/h óptimo.</p>
    <ul style="list-style:none">
      <li style="font-size:13px;color:#94a3b8;padding:4px 0">⚠ Practica EXACTAMENTE el mismo gel/bebida que usarás en carrera (stomach training desde sem 5).</li>
      <li style="font-size:13px;color:#94a3b8;padding:4px 0">⚠ No probar nada nuevo en race day. Jamás.</li>
      <li style="font-size:13px;color:#94a3b8;padding:4px 0">☕ Cafeína 3mg/kg (≈250mg) en segunda mitad de carrera si la toleras habitualmente.</li>
    </ul>
  </div>

  <div class="supps">
    <h3>Suplementación — Solo con evidencia (Grado A/B)</h3>
    {supps_html}
    <p style="font-size:12px;color:var(--muted);margin-top:14px;border-top:1px solid var(--border);padding-top:10px">❌ No recomendados: BCAA (innecesario si proteína total es adecuada), pre-workouts con estimulantes mezclados, antioxidantes en dosis altas (pueden bloquear adaptaciones al entrenamiento — Ristow 2009).</p>
  </div>
</div>

<!-- ═══ TAB: SEGUIMIENTO ═══ -->
<div id="tab-seguimiento" class="tab-panel">
  <div class="compliance-intro">
    <p>Este panel compara lo planificado vs lo ejecutado semana a semana usando los datos de Strava. Ejecuta el script semanalmente para actualizar. Los datos en verde indican cumplimiento >90%; en ámbar 70-90%; en rojo &lt;70%.</p>
    <p style="margin-top:8px;font-size:12px;color:var(--muted)">💡 Truco: añade este script a un cron job o tarea programada para ejecutarlo cada lunes automáticamente.</p>
  </div>
  <div class="compliance-table-wrap">
    <table class="compliance-table">
      <thead>
        <tr>
          <th>Semana</th><th>Período</th><th>Fase</th>
          <th>Plan km</th><th>Real km</th><th>% km</th>
          <th>Plan D+</th><th>Real D+</th><th>% D+</th>
          <th>Estado</th>
        </tr>
      </thead>
      <tbody id="compliance-body">
        <tr><td colspan="10" class="no-data" style="text-align:center;padding:20px">
          Cargando datos de Strava...
        </td></tr>
      </tbody>
    </table>
  </div>
</div>

</div><!-- end #app -->

<script>
const CHART_DATA = {chart_data};
const PLAN_DATA = {plan_data_json};

function switchTab(id) {{
  document.querySelectorAll('.tab-btn').forEach((b,i) => b.classList.remove('active'));
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelector(`[onclick="switchTab('${{id}}')"]`).classList.add('active');
  document.getElementById('tab-'+id).classList.add('active');
}}

const CHART_DEFAULTS = {{
  responsive:true, maintainAspectRatio:true,
  plugins:{{legend:{{display:false}}}},
  scales:{{
    x:{{grid:{{color:'#1e2d45'}},ticks:{{color:'#64748b',font:{{size:10,family:'JetBrains Mono'}}}}}},
    y:{{grid:{{color:'#1e2d45'}},ticks:{{color:'#64748b',font:{{size:10,family:'JetBrains Mono'}}}}}}
  }}
}};

window.addEventListener('DOMContentLoaded', () => {{
  const d = CHART_DATA;
  
  // Stats
  const totalKm  = d.km.reduce((a,b)=>a+b,0);
  const totalD   = d.d_plus.reduce((a,b)=>a+b,0);
  const avgKm    = d.km.length ? (totalKm/d.km.length).toFixed(1) : 0;
  const avgTrail = d.trail.length ? Math.round(d.trail.reduce((a,b)=>a+b,0)/d.trail.length) : 0;
  document.getElementById('sv-weeks').textContent = d.labels.length;
  document.getElementById('sv-km').textContent    = totalKm.toFixed(0);
  document.getElementById('sv-d').textContent     = totalD.toLocaleString();
  document.getElementById('sv-avg-km').textContent= avgKm;
  document.getElementById('sv-hr').textContent    = d.hr_max;
  document.getElementById('sv-trail').textContent = avgTrail+'%';
  document.getElementById('hr-max-val').textContent = d.hr_max;

  // Charts
  new Chart(document.getElementById('chartKm').getContext('2d'), {{
    type:'bar', data:{{labels:d.labels,
      datasets:[{{data:d.km,backgroundColor:'#22d3ee33',borderColor:'#22d3ee',borderWidth:2,borderRadius:4}}]}},
    options:{{...CHART_DEFAULTS}}
  }});
  new Chart(document.getElementById('chartD').getContext('2d'), {{
    type:'bar', data:{{labels:d.labels,
      datasets:[{{data:d.d_plus,backgroundColor:'#f9731633',borderColor:'#f97316',borderWidth:2,borderRadius:4}}]}},
    options:{{...CHART_DEFAULTS}}
  }});
  new Chart(document.getElementById('chartTime').getContext('2d'), {{
    type:'line', data:{{labels:d.labels,
      datasets:[{{data:d.time,borderColor:'#84cc16',backgroundColor:'#84cc1620',
        pointBackgroundColor:'#84cc16',tension:.3,fill:true,pointRadius:3}}]}},
    options:{{...CHART_DEFAULTS}}
  }});
  new Chart(document.getElementById('chartTrail').getContext('2d'), {{
    type:'bar', data:{{labels:d.labels,
      datasets:[{{data:d.trail,backgroundColor:'#a78bfa33',borderColor:'#a78bfa',borderWidth:2,borderRadius:4,
        label:'% Trail'}}]}},
    options:{{...CHART_DEFAULTS,scales:{{...CHART_DEFAULTS.scales,
      y:{{...CHART_DEFAULTS.scales.y,max:100,
        ticks:{{...CHART_DEFAULTS.scales.y.ticks,callback:v=>v+'%'}}}}}}}}
  }});

  // Compliance table
  buildCompliance();
}});

function buildCompliance() {{
  const today = new Date();
  const planStart = new Date('{PLAN_START.isoformat()}');
  const tbody = document.getElementById('compliance-body');
  const rows = [];
  const phaseNames = {{1:'Base',2:'Construcción',3:'Afinado Palencia',4:'Puente TP60',5:'Taper TP60'}};
  const phaseColors = {{1:'#f97316',2:'#f59e0b',3:'#22d3ee',4:'#a78bfa',5:'#34d399'}};
  
  for (const pw of PLAN_DATA) {{
    const wStart = new Date(planStart.getTime() + (pw.week-1)*7*86400000);
    const wEnd   = new Date(wStart.getTime() + 6*86400000);
    if (wEnd > today) continue;  // future weeks: skip
    
    // Find matching Strava week
    const wKey = wStart.toISOString().slice(0,10);
    const strava = CHART_DATA.labels.indexOf(wKey.slice(5,10));
    const actualKm  = strava>=0 ? CHART_DATA.km[strava]    : null;
    const actualD   = strava>=0 ? CHART_DATA.d_plus[strava]: null;
    
    const kmPct  = actualKm != null ? Math.round(actualKm/pw.km*100) : null;
    const dPct   = actualD  != null ? Math.round(actualD/pw.d_plus*100) : null;
    const pc = phaseColors[pw.phase];
    
    function pctColor(p) {{ return p==null?'#64748b':p>=90?'#84cc16':p>=70?'#f59e0b':'#ef4444'; }}
    function pctBar(p)   {{ return p==null?'':
      `<div class="bar-wrap"><div class="bar-fill" style="width:${{Math.min(p,100)}}%;background:${{pctColor(p)}}"></div></div>`; }}
    
    const ds = `${{wStart.toLocaleDateString('es-ES',{{day:'2-digit',month:'short'}})}}`;
    rows.push(`<tr>
      <td class="ct-week"><span style="background:${{pc}}22;color:${{pc}};padding:2px 7px;border-radius:4px;font-family:'JetBrains Mono',monospace;font-size:11px">S${{pw.week}}</span></td>
      <td style="font-size:11px;color:#64748b;font-family:'JetBrains Mono',monospace">${{ds}}</td>
      <td style="font-size:11px;color:${{pc}}">${{phaseNames[pw.phase]}}</td>
      <td class="ct-plan">${{pw.km}}km</td>
      <td class="ct-actual">${{actualKm!=null?actualKm+'km':'—'}}</td>
      <td><span style="color:${{pctColor(kmPct)}};font-family:'Rajdhani',sans-serif;font-weight:700">${{kmPct!=null?kmPct+'%':'—'}}</span> ${{pctBar(kmPct)}}</td>
      <td class="ct-plan">${{pw.d_plus}}m</td>
      <td class="ct-actual">${{actualD!=null?actualD+'m':'—'}}</td>
      <td><span style="color:${{pctColor(dPct)}};font-family:'Rajdhani',sans-serif;font-weight:700">${{dPct!=null?dPct+'%':'—'}}</span> ${{pctBar(dPct)}}</td>
      <td style="font-size:12px;color:#64748b">${{kmPct!=null&&kmPct>=90?'✅':kmPct!=null&&kmPct>=70?'⚠️':'❌'}}</td>
    </tr>`);
  }}
  
  if (rows.length === 0) {{
    tbody.innerHTML = '<tr><td colspan="10" style="text-align:center;padding:20px;color:#64748b;font-style:italic">El plan comienza el 24 de marzo 2026. Ejecuta el script la próxima semana para ver tu primer seguimiento.</td></tr>';
  }} else {{
    tbody.innerHTML = rows.join('');
  }}
}}
</script>
</body>
</html>"""
    return html

# ═══════════════════════════════════════════════════════════════════════════════
# GENERADOR PLAN COMPLETO — con Strava integrado
# ═══════════════════════════════════════════════════════════════════════════════
def generate_plan_completo(strava_data, athlete_profile):
    """Read static plan_completo.html and inject Strava analysis + compliance."""
    weekly_data = strava_data.get("weeks", [])
    hr_max      = strava_data.get("hr_max", 186)

    chart_labels = [w[0][5:] for w in weekly_data[-12:]]
    chart_km     = [round(w[1]["km"],1) for w in weekly_data[-12:]]
    chart_d_plus = [w[1]["d_plus"] for w in weekly_data[-12:]]
    chart_time   = [w[1]["time_min"] for w in weekly_data[-12:]]
    chart_trail  = [w[1]["trail_pct"] for w in weekly_data[-12:]]

    chart_data = json.dumps({
        "labels": chart_labels, "km": chart_km,
        "d_plus": chart_d_plus, "time": chart_time, "trail": chart_trail,
        "hr_max": hr_max
    })
    plan_data_json = json.dumps([{"week":w["week"],"phase":w["phase"],"km":w["km"],"d_plus":w["d_plus"]} for w in PLAN])

    # Strava weekly data for raw matching
    strava_weeks_json = json.dumps({w[0]: {"km": round(w[1]["km"],1), "d_plus": w[1]["d_plus"],
        "time_min": w[1]["time_min"], "runs": w[1]["runs"], "hr_avg": w[1]["hr_avg"],
        "trail_pct": w[1]["trail_pct"]} for w in weekly_data})

    # Build zones
    # Zones based on VT1/VT2 lab data
    vt1 = ATHLETE.get("vt1", 152)
    vt2 = ATHLETE.get("vt2", 172)
    zones_ref = [
        {"lo": 0,       "hi": vt1-10, "name":"Z1 Recuperación",  "color":"#64748b", "desc":f"< {vt1-10} bpm — Regenerativo"},
        {"lo": vt1-10,  "hi": vt1,    "name":"Z2 Aeróbico",      "color":"#22d3ee", "desc":f"{vt1-10}–{vt1} bpm — Justo debajo de VT1"},
        {"lo": vt1,     "hi": vt2,    "name":"Z3 Tempo",         "color":"#84cc16", "desc":f"{vt1}–{vt2} bpm — Entre VT1 y VT2"},
        {"lo": vt2,     "hi": vt2+8,  "name":"Z4 Umbral",        "color":"#f97316", "desc":f"{vt2}–{vt2+8} bpm — Por encima de VT2"},
        {"lo": vt2+8,   "hi": hr_max, "name":"Z5 VO2max",        "color":"#ef4444", "desc":f"{vt2+8}–{hr_max} bpm — Máximo esfuerzo"},
    ]

    zones_html = "".join(f"""
      <div class='zone-row'>
        <span class='z-dot' style='background:{z["color"]}'></span>
        <span class='z-name'>{z["name"]}</span>
        <span class='z-range'>{z["lo"]}–{z["hi"]} bpm</span>
        <span class='z-pct'>{z["desc"]}</span>
      </div>""" for z in zones_ref)

    # Race countdown
    today = date.today()
    races_countdown = ""
    for r in ATHLETE["races"]:
        rd = date.fromisoformat(r["date"])
        days_left = (rd - today).days
        races_countdown += f"""
        <div class="race-card" style="border-top-color:{r['accent']}">
          <div class="rc-name" style="color:{r['accent']}">{r['name']}</div>
          <div class="rc-info">{r['km']}km · {r['d_plus']:,}m D+</div>
          <div style="font-family:'Rajdhani',sans-serif;font-size:36px;font-weight:700;color:{r['accent']};line-height:1;margin:6px 0">{days_left}</div>
          <div style="font-size:10px;color:#64748b;letter-spacing:2px;text-transform:uppercase">días</div>
          <div class="rc-date">{rd.strftime('%d %b %Y')}</div>
        </div>"""

    # Strava profile
    prof = athlete_profile or {}
    name = (prof.get("firstname","") + " " + prof.get("lastname","")).strip() or "Jose"

    # Build Strava stats
    total_km  = sum(chart_km)
    total_d   = sum(chart_d_plus)
    avg_km    = round(total_km/len(chart_km), 1) if chart_km else 0
    avg_trail = round(sum(chart_trail)/len(chart_trail)) if chart_trail else 0
    n_weeks   = len(chart_labels)

    # Read the static plan HTML
    static_html = OUTPUT_PLAN.read_text(encoding="utf-8")

    # Inject Strava tab + compliance tab BEFORE the closing </div><!-- end #app -->
    strava_tab_html = f"""
<!-- ═══════════════════════════════════════════════════════════ -->
<!-- TAB: STRAVA ANALYSIS (injected by trail_analyzer.py)      -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div id="tab-strava" class="tab-panel">
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin-bottom:28px">
    <div style="background:var(--surface2);border:1px solid var(--border);border-radius:10px;padding:16px;text-align:center">
      <div style="font-family:'JetBrains Mono',monospace;font-size:28px;font-weight:500;background:linear-gradient(135deg,var(--accent),var(--amber));-webkit-background-clip:text;-webkit-text-fill-color:transparent">{n_weeks}</div>
      <div style="font-family:'Rajdhani',sans-serif;font-size:11px;color:var(--muted);letter-spacing:1px;text-transform:uppercase;margin-top:4px">Semanas analizadas</div>
    </div>
    <div style="background:var(--surface2);border:1px solid var(--border);border-radius:10px;padding:16px;text-align:center">
      <div style="font-family:'JetBrains Mono',monospace;font-size:28px;font-weight:500;background:linear-gradient(135deg,var(--accent),var(--amber));-webkit-background-clip:text;-webkit-text-fill-color:transparent">{total_km:.0f}</div>
      <div style="font-family:'Rajdhani',sans-serif;font-size:11px;color:var(--muted);letter-spacing:1px;text-transform:uppercase;margin-top:4px">km totales período</div>
    </div>
    <div style="background:var(--surface2);border:1px solid var(--border);border-radius:10px;padding:16px;text-align:center">
      <div style="font-family:'JetBrains Mono',monospace;font-size:28px;font-weight:500;background:linear-gradient(135deg,var(--accent),var(--amber));-webkit-background-clip:text;-webkit-text-fill-color:transparent">{total_d:,}</div>
      <div style="font-family:'Rajdhani',sans-serif;font-size:11px;color:var(--muted);letter-spacing:1px;text-transform:uppercase;margin-top:4px">m D+ período</div>
    </div>
    <div style="background:var(--surface2);border:1px solid var(--border);border-radius:10px;padding:16px;text-align:center">
      <div style="font-family:'JetBrains Mono',monospace;font-size:28px;font-weight:500;background:linear-gradient(135deg,var(--accent),var(--amber));-webkit-background-clip:text;-webkit-text-fill-color:transparent">{avg_km}</div>
      <div style="font-family:'Rajdhani',sans-serif;font-size:11px;color:var(--muted);letter-spacing:1px;text-transform:uppercase;margin-top:4px">km / semana promedio</div>
    </div>
    <div style="background:var(--surface2);border:1px solid var(--border);border-radius:10px;padding:16px;text-align:center">
      <div style="font-family:'JetBrains Mono',monospace;font-size:28px;font-weight:500;background:linear-gradient(135deg,var(--accent),var(--amber));-webkit-background-clip:text;-webkit-text-fill-color:transparent">{hr_max}</div>
      <div style="font-family:'Rajdhani',sans-serif;font-size:11px;color:var(--muted);letter-spacing:1px;text-transform:uppercase;margin-top:4px">FC max registrada</div>
    </div>
    <div style="background:var(--surface2);border:1px solid var(--border);border-radius:10px;padding:16px;text-align:center">
      <div style="font-family:'JetBrains Mono',monospace;font-size:28px;font-weight:500;background:linear-gradient(135deg,var(--accent),var(--amber));-webkit-background-clip:text;-webkit-text-fill-color:transparent">{avg_trail}%</div>
      <div style="font-family:'Rajdhani',sans-serif;font-size:11px;color:var(--muted);letter-spacing:1px;text-transform:uppercase;margin-top:4px">% trail avg</div>
    </div>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:28px">
    <div style="background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px">
      <div style="font-family:'Rajdhani',sans-serif;font-size:13px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;margin-bottom:16px">Volumen semanal — km</div>
      <canvas id="chartKm" style="max-height:200px"></canvas>
    </div>
    <div style="background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px">
      <div style="font-family:'Rajdhani',sans-serif;font-size:13px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;margin-bottom:16px">Desnivel positivo — m</div>
      <canvas id="chartD" style="max-height:200px"></canvas>
    </div>
    <div style="background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px">
      <div style="font-family:'Rajdhani',sans-serif;font-size:13px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;margin-bottom:16px">Tiempo carrera — min</div>
      <canvas id="chartTime" style="max-height:200px"></canvas>
    </div>
    <div style="background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px">
      <div style="font-family:'Rajdhani',sans-serif;font-size:13px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;margin-bottom:16px">% Sesiones Trail vs Road</div>
      <canvas id="chartTrail" style="max-height:200px"></canvas>
    </div>
  </div>

  <div style="background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:16px">
    <div style="font-family:'Rajdhani',sans-serif;font-size:13px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;margin-bottom:16px">Zonas FC — FCmax: {hr_max} bpm</div>
    {zones_html}
    <p style="font-size:12px;color:var(--muted);margin-top:12px">Zonas 5-zonas Seiler/Coggan. 80% en Z1-Z2, 20% en Z3-Z5 (polarizada).</p>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- TAB: COMPLIANCE / SEGUIMIENTO                              -->
<!-- ═══════════════════════════════════════════════════════════ -->
<div id="tab-compliance" class="tab-panel">
  <div style="background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:20px">
    <p style="font-size:14px;color:#94a3b8;line-height:1.7">Compara lo planificado vs ejecutado usando datos de Strava. Ejecuta <code style="background:var(--surface3);padding:2px 6px;border-radius:4px;font-size:12px">python trail_analyzer.py</code> semanalmente para actualizar.</p>
    <p style="margin-top:8px;font-size:12px;color:var(--muted)">Verde: >90% | Ambar: 70-90% | Rojo: &lt;70%</p>
  </div>
  <div style="overflow-x:auto">
    <table style="width:100%;border-collapse:collapse;font-size:13px">
      <thead>
        <tr>
          <th style="font-family:'Rajdhani',sans-serif;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--muted);padding:10px 12px;border-bottom:1px solid var(--border);text-align:left">Semana</th>
          <th style="font-family:'Rajdhani',sans-serif;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--muted);padding:10px 12px;border-bottom:1px solid var(--border);text-align:left">Periodo</th>
          <th style="font-family:'Rajdhani',sans-serif;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--muted);padding:10px 12px;border-bottom:1px solid var(--border);text-align:left">Fase</th>
          <th style="font-family:'Rajdhani',sans-serif;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--muted);padding:10px 12px;border-bottom:1px solid var(--border);text-align:left">Plan km</th>
          <th style="font-family:'Rajdhani',sans-serif;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--muted);padding:10px 12px;border-bottom:1px solid var(--border);text-align:left">Real km</th>
          <th style="font-family:'Rajdhani',sans-serif;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--muted);padding:10px 12px;border-bottom:1px solid var(--border);text-align:left">%</th>
          <th style="font-family:'Rajdhani',sans-serif;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--muted);padding:10px 12px;border-bottom:1px solid var(--border);text-align:left">Plan D+</th>
          <th style="font-family:'Rajdhani',sans-serif;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--muted);padding:10px 12px;border-bottom:1px solid var(--border);text-align:left">Real D+</th>
          <th style="font-family:'Rajdhani',sans-serif;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--muted);padding:10px 12px;border-bottom:1px solid var(--border);text-align:left">%</th>
          <th style="font-family:'Rajdhani',sans-serif;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--muted);padding:10px 12px;border-bottom:1px solid var(--border);text-align:left">FC avg</th>
          <th style="font-family:'Rajdhani',sans-serif;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--muted);padding:10px 12px;border-bottom:1px solid var(--border);text-align:left">Runs</th>
        </tr>
      </thead>
      <tbody id="compliance-body">
        <tr><td colspan="11" style="text-align:center;padding:20px;color:#64748b;font-style:italic">Cargando...</td></tr>
      </tbody>
    </table>
  </div>
</div>
"""

    # Inject the Strava tab and compliance tab, add the tab buttons, add Chart.js + scripts
    # Step 1: Add Chart.js CDN before </head>
    inject_head = '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>\n</head>'
    static_html = static_html.replace('</head>', inject_head)

    # Step 2: Add the Strava + Compliance tab buttons
    static_html = static_html.replace(
        '<button class="tab-btn" onclick="switchTab(\'race\')">Estrategia Carrera</button>',
        '<button class="tab-btn" onclick="switchTab(\'race\')">Estrategia Carrera</button>\n'
        '  <button class="tab-btn" onclick="switchTab(\'strava\')">Strava Analysis</button>\n'
        '  <button class="tab-btn" onclick="switchTab(\'compliance\')">Seguimiento</button>'
    )

    # Step 3: Add zone-row styles
    zone_styles = """
.zone-row{display:flex;align-items:center;gap:12px;padding:8px 0;border-bottom:1px solid var(--border)}
.zone-row:last-child{border-bottom:none}
.z-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}
.z-name{flex:1;font-family:'Rajdhani',sans-serif;font-weight:600;font-size:13px}
.z-range{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--accent);min-width:100px}
.z-pct{font-size:12px;color:var(--muted)}
@media(max-width:768px){.strat-grid,.sessions-grid{grid-template-columns:1fr}}
"""
    static_html = static_html.replace(
        '@media(max-width:768px){',
        zone_styles + '\n@media(max-width:768px){'
    )

    # Step 4: Inject Strava tabs before </div><!-- end #app -->
    static_html = static_html.replace(
        '</div><!-- end #app -->',
        strava_tab_html + '\n</div><!-- end #app -->'
    )

    # Step 5: Replace the countdown placeholder with live data
    static_html = static_html.replace(
        '<div class="races-header">\n      <div class="race-card" style="border-top-color:#f97316">\n        <div class="rc-name" style="color:#f97316">Marat&oacute;n MTN Palencia</div>\n        <div class="rc-info">44km &middot; 3,500m D+ &middot; Objetivo B</div>\n        <div class="rc-date">12 Sep 2026</div>\n      </div>\n      <div class="race-card" style="border-top-color:#22d3ee">\n        <div class="rc-name" style="color:#22d3ee">TP60</div>\n        <div class="rc-info">63km &middot; 2,500m D+ &middot; Objetivo A</div>\n        <div class="rc-date">11 Oct 2026</div>\n      </div>\n    </div>',
        f'<div class="races-header">{races_countdown}</div>'
    )

    # Step 6: Replace the simple switchTab JS with the full version including chart rendering
    new_script = f"""<script>
const CHART_DATA = {chart_data};
const PLAN_DATA = {plan_data_json};
const STRAVA_WEEKS = {strava_weeks_json};
const PLAN_START = '{PLAN_START.isoformat()}';

function switchTab(id) {{
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  const btn = document.querySelector(`[onclick="switchTab('${{id}}')"]`);
  if (btn) btn.classList.add('active');
  const panel = document.getElementById('tab-'+id);
  if (panel) panel.classList.add('active');
  // Lazy-init charts on first Strava tab open
  if (id === 'strava' && !window._chartsInit) initCharts();
  if (id === 'compliance' && !window._complianceInit) initCompliance();
}}

const CHART_DEFAULTS = {{
  responsive:true, maintainAspectRatio:true,
  plugins:{{legend:{{display:false}}}},
  scales:{{
    x:{{grid:{{color:'#1e2d45'}},ticks:{{color:'#64748b',font:{{size:10,family:'JetBrains Mono'}}}}}},
    y:{{grid:{{color:'#1e2d45'}},ticks:{{color:'#64748b',font:{{size:10,family:'JetBrains Mono'}}}}}}
  }}
}};

function initCharts() {{
  window._chartsInit = true;
  const d = CHART_DATA;
  if (!d.labels.length) return;

  new Chart(document.getElementById('chartKm').getContext('2d'), {{
    type:'bar', data:{{labels:d.labels,
      datasets:[{{data:d.km,backgroundColor:'#22d3ee33',borderColor:'#22d3ee',borderWidth:2,borderRadius:4}}]}},
    options:{{...CHART_DEFAULTS}}
  }});
  new Chart(document.getElementById('chartD').getContext('2d'), {{
    type:'bar', data:{{labels:d.labels,
      datasets:[{{data:d.d_plus,backgroundColor:'#f9731633',borderColor:'#f97316',borderWidth:2,borderRadius:4}}]}},
    options:{{...CHART_DEFAULTS}}
  }});
  new Chart(document.getElementById('chartTime').getContext('2d'), {{
    type:'line', data:{{labels:d.labels,
      datasets:[{{data:d.time,borderColor:'#84cc16',backgroundColor:'#84cc1620',
        pointBackgroundColor:'#84cc16',tension:.3,fill:true,pointRadius:3}}]}},
    options:{{...CHART_DEFAULTS}}
  }});
  new Chart(document.getElementById('chartTrail').getContext('2d'), {{
    type:'bar', data:{{labels:d.labels,
      datasets:[{{data:d.trail,backgroundColor:'#a78bfa33',borderColor:'#a78bfa',borderWidth:2,borderRadius:4}}]}},
    options:{{...CHART_DEFAULTS,scales:{{...CHART_DEFAULTS.scales,
      y:{{...CHART_DEFAULTS.scales.y,max:100,
        ticks:{{...CHART_DEFAULTS.scales.y.ticks,callback:v=>v+'%'}}}}}}}}
  }});
}}

function initCompliance() {{
  window._complianceInit = true;
  const today = new Date();
  const planStart = new Date(PLAN_START);
  const tbody = document.getElementById('compliance-body');
  const phaseNames = {{1:'Base',2:'Construcción',3:'Afinado Palencia',4:'Puente TP60',5:'Taper TP60'}};
  const phaseColors = {{1:'#f97316',2:'#f59e0b',3:'#22d3ee',4:'#a78bfa',5:'#34d399'}};
  const rows = [];

  for (const pw of PLAN_DATA) {{
    const wStart = new Date(planStart.getTime() + (pw.week-1)*7*86400000);
    const wEnd   = new Date(wStart.getTime() + 6*86400000);
    if (wEnd > today) continue;

    const wKey = wStart.toISOString().slice(0,10);
    const strava = STRAVA_WEEKS[wKey] || null;
    const actualKm  = strava ? strava.km : null;
    const actualD   = strava ? strava.d_plus : null;
    const hrAvg     = strava ? strava.hr_avg : null;
    const runs      = strava ? strava.runs : null;

    const kmPct = actualKm != null ? Math.round(actualKm/pw.km*100) : null;
    const dPct  = actualD  != null && pw.d_plus > 0 ? Math.round(actualD/pw.d_plus*100) : null;
    const pc = phaseColors[pw.phase];

    function pctColor(p) {{ return p==null?'#64748b':p>=90?'#84cc16':p>=70?'#f59e0b':'#ef4444'; }}
    function bar(p) {{ return p==null?'':
      '<div style="width:60px;height:6px;background:#1e293b;border-radius:3px;overflow:hidden;display:inline-block;vertical-align:middle;margin-left:6px"><div style="height:100%;border-radius:3px;width:'+Math.min(p,100)+'%;background:'+pctColor(p)+'"></div></div>'; }}

    const ds = wStart.toLocaleDateString('es-ES',{{day:'2-digit',month:'short'}});
    rows.push('<tr>'+
      '<td style="font-family:JetBrains Mono,monospace;font-size:11px"><span style="background:'+pc+'22;color:'+pc+';padding:2px 7px;border-radius:4px">S'+pw.week+'</span></td>'+
      '<td style="font-size:11px;color:#64748b;font-family:JetBrains Mono,monospace">'+ds+'</td>'+
      '<td style="font-size:11px;color:'+pc+'">'+phaseNames[pw.phase]+'</td>'+
      '<td style="color:#22d3ee;font-family:JetBrains Mono,monospace;font-size:12px">'+pw.km+'km</td>'+
      '<td style="color:#f59e0b;font-family:JetBrains Mono,monospace;font-size:12px">'+(actualKm!=null?actualKm+'km':'—')+'</td>'+
      '<td><span style="color:'+pctColor(kmPct)+';font-family:Rajdhani,sans-serif;font-weight:700">'+(kmPct!=null?kmPct+'%':'—')+'</span>'+bar(kmPct)+'</td>'+
      '<td style="color:#22d3ee;font-family:JetBrains Mono,monospace;font-size:12px">'+pw.d_plus+'m</td>'+
      '<td style="color:#f59e0b;font-family:JetBrains Mono,monospace;font-size:12px">'+(actualD!=null?actualD+'m':'—')+'</td>'+
      '<td><span style="color:'+pctColor(dPct)+';font-family:Rajdhani,sans-serif;font-weight:700">'+(dPct!=null?dPct+'%':'—')+'</span>'+bar(dPct)+'</td>'+
      '<td style="font-family:JetBrains Mono,monospace;font-size:11px;color:#94a3b8">'+(hrAvg?hrAvg+'bpm':'—')+'</td>'+
      '<td style="font-family:JetBrains Mono,monospace;font-size:11px;color:#94a3b8">'+(runs||'—')+'</td>'+
    '</tr>');
  }}

  if (rows.length === 0) {{
    tbody.innerHTML = '<tr><td colspan="11" style="text-align:center;padding:20px;color:#64748b;font-style:italic">El plan comienza el 23 de marzo 2026. Ejecuta el script cada lunes para ver seguimiento.</td></tr>';
  }} else {{
    tbody.innerHTML = rows.join('');
  }}
}}
</script>"""

    # Replace old script block (first run only — subsequent runs skip this no-op)
    static_html = static_html.replace(
        """<script>
function switchTab(id){
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  document.querySelectorAll('.tab-panel').forEach(p=>p.classList.remove('active'));
  document.getElementById('tab-'+id).classList.add('active');
  event.target.classList.add('active');
}
</script>""",
        new_script
    )

    # Idempotent PLAN_START refresh: on re-runs the old script is already replaced,
    # so update the date literal directly (handles both first and subsequent runs).
    import re as _re
    static_html = _re.sub(
        r"const PLAN_START = '\d{4}-\d{2}-\d{2}';",
        f"const PLAN_START = '{PLAN_START.isoformat()}';",
        static_html
    )

    return static_html


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════
def main():
    print("\n" + "═"*60)
    print("  TRAIL 360° ANALYZER — Temporada 2026")
    print("  Jose · Palencia MTN + TP60")
    print("═"*60 + "\n")

    strava_data    = {"weeks": [], "hr_max": 186, "hr_zones": None}
    athlete_profile = {}

    try:
        tok = get_token()
        athlete_profile = fetch_athlete(tok)
        acts = fetch_activities(tok)
        zones_data = fetch_zones(tok)
        strava_data = analyze(acts, zones_data)
    except Exception as e:
        print(f"⚠ Error conectando con Strava: {e}")
        print("  → Generando dashboard con plan completo sin datos Strava.\n")

    # Generate original dashboard
    print("⚙ Generando dashboard HTML...")
    html = generate_html(strava_data, athlete_profile)
    OUTPUT_FILE.write_text(html, encoding="utf-8")
    print(f"  ✓ Dashboard básico: {OUTPUT_FILE.resolve()}")

    # Generate enhanced plan with Strava data
    print("⚙ Generando plan completo con Strava...")
    if OUTPUT_PLAN.exists():
        plan_html = generate_plan_completo(strava_data, athlete_profile)
        OUTPUT_PLAN.write_text(plan_html, encoding="utf-8")
        print(f"  ✓ Plan completo:   {OUTPUT_PLAN.resolve()}")
        print("\n  Abriendo plan completo...")
        webbrowser.open(OUTPUT_PLAN.resolve().as_uri())
    else:
        print(f"  ⚠ {OUTPUT_PLAN} no encontrado. Solo se generó dashboard básico.")
        webbrowser.open(OUTPUT_FILE.resolve().as_uri())

    print("\n" + "═"*60)
    print("  ARCHIVOS GENERADOS:")
    print(f"  • {OUTPUT_FILE} — Dashboard básico con Strava")
    print(f"  • {OUTPUT_PLAN} — Plan detallado + Gym + Supps + Strava + Seguimiento")
    print(f"  • {len(PLAN)} semanas · {sum(len(s['exercises']) for s in STRENGTH)} ejercicios · HSN products")
    print("═"*60 + "\n")

    # Auto-deploy to GitHub Pages — only when explicitly requested.
    # (set PLANTRAIL_DEPLOY=1; Part B's GitHub Action sets this.) Local runs never push.
    import subprocess
    script_dir = str(Path(__file__).parent)
    if not os.environ.get("PLANTRAIL_DEPLOY"):
        print("  (Auto-deploy desactivado — exporta PLANTRAIL_DEPLOY=1 para publicar)")
    else:
        try:
            r = subprocess.run(["git","remote"], capture_output=True, text=True, cwd=script_dir)
            if r.returncode == 0 and r.stdout.strip():
                print("⚙ Desplegando a GitHub Pages...")
                subprocess.run(["git","add","plan_completo.html","dashboard.html","index.html"], cwd=script_dir)
                result = subprocess.run(
                    ["git","commit","-m",f"Update dashboard {date.today().isoformat()}"],
                    capture_output=True, text=True, cwd=script_dir)
                if "nothing to commit" in result.stdout:
                    print("  ✓ Sin cambios — no se necesita deploy.")
                else:
                    push = subprocess.run(["git","push"], capture_output=True, text=True, cwd=script_dir)
                    print("  ✓ Desplegado" if push.returncode == 0 else f"  ⚠ Push falló: {push.stderr.strip()}")
            else:
                print("  (Sin repositorio git — deploy manual necesario)")
        except Exception as e:
            print(f"  ⚠ Auto-deploy saltado: {e}")

    print("\n  Ejecuta 'python trail_analyzer.py' cada lunes para actualizar.\n")

if __name__ == "__main__":
    main()
