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
CLIENT_SECRET = ""
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
    "races": [
        {"id":"palencia","name":"Maratón MTN Palencia",
         "date":"2026-09-12","km":44,"d_plus":3500,"accent":"#f97316"},
        {"id":"tp60","name":"TP60",
         "date":"2026-10-11","km":63,"d_plus":2500,"accent":"#22d3ee"},
    ]
}

PLAN_START = date(2026, 3, 23)  # Monday

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
    if TOKEN_FILE.exists():
        tok = json.loads(TOKEN_FILE.read_text())
        if tok.get("expires_at",0) > time.time()+60:
            print("✓ Token Strava válido"); return tok
        print("↻ Renovando token Strava...")
        data = urllib.parse.urlencode({"client_id":CLIENT_ID,"client_secret":CLIENT_SECRET,
            "grant_type":"refresh_token","refresh_token":tok["refresh_token"]}).encode()
        with urllib.request.urlopen(urllib.request.Request(
                "https://www.strava.com/oauth/token",data=data,method="POST")) as r:
            tok = json.loads(r.read())
        TOKEN_FILE.write_text(json.dumps(tok)); return tok
    global _auth_code
    url=(f"https://www.strava.com/oauth/authorize?client_id={CLIENT_ID}"
         f"&redirect_uri={REDIRECT_URI}&response_type=code&scope=activity:read_all&approval_prompt=auto")
    srv = http.server.HTTPServer(("localhost",8888),_CB)
    t = threading.Thread(target=srv.handle_request); t.daemon=True; t.start()
    print("\n🔑 Abriendo Strava en el navegador..."); webbrowser.open(url); t.join(timeout=120)
    srv.server_close()
    if not _auth_code: raise RuntimeError("No se recibió código de autorización")
    data = urllib.parse.urlencode({"client_id":CLIENT_ID,"client_secret":CLIENT_SECRET,
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
    # Estimate hrmax from data or fallback
    if hr_max < 150: hr_max = 186  # fallback for VDOT57 runner
    # Build zone names from Strava if available
    hr_zones = None
    if zones_data and "heart_rate" in zones_data:
        hr_zones = zones_data["heart_rate"]["zones"]
    return {"weeks": sorted_weeks, "hr_max": hr_max, "hr_zones": hr_zones}

# ═══════════════════════════════════════════════════════════════════════════════
# PLAN DE ENTRENAMIENTO COMPLETO (28 semanas)
# Base científica:
#   Seiler 2010: distribución polarizada 80/20
#   Koop 2016: back-to-back specificity trail
#   Beattie 2017: HST mejora economía de carrera
#   Mujika 2003: taper óptimo 2 semanas
#   Jeukendrup 2014: nutrición durante carrera 60-90g CHO/h
#   Giovanelli 2016: power hiking eficiencia en pendientes >15%
# ═══════════════════════════════════════════════════════════════════════════════
PLAN = [
  # ─── FASE 1: BASE AERÓBICA (Sem 1-7 | 24 Mar – 10 May) ────────────────────
  {"week":1,"phase":1,"phase_name":"Base Aeróbica","load":"LOW",
   "title":"Recuperación activa post-media","km":42,"d_plus":500,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso total. Crioterapia si tienes acceso."},
    {"day":"M","type":"EASY","km":8,"d":0,"desc":"8km Z1 (<130bpm). Cadencia >170spm. GYM FASE A después."},
    {"day":"X","type":"EASY","km":12,"d":0,"desc":"12km Z1–Z2 (<140bpm). Plano. Foco en relajación y cadencia."},
    {"day":"J","type":"GYM","km":0,"d":0,"desc":"GYM FASE A (45min). Sin rodaje hoy."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso. Movilidad 15min (hip flexors, gemelos)."},
    {"day":"S","type":"LONG","km":16,"d":300,"desc":"16km Z1–Z2 suave. Busca alguna subida. Sin geles (fomenta oxidación de grasas)."},
    {"day":"D","type":"EASY","km":10,"d":200,"desc":"10km Z1 recovery. Si hay agujetas reduce a 8km."},
   ],"notes":"⚠ Prioridad absoluta: regeneración. No superes Z2 en ningún momento."},

  {"week":2,"phase":1,"phase_name":"Base Aeróbica","load":"LOW-MED",
   "title":"Reactivación aeróbica","km":55,"d_plus":700,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":0,"desc":"10km Z1–Z2 + GYM FASE A."},
    {"day":"X","type":"TEMPO","km":14,"d":100,"desc":"14km progresivos: 3km Z1 → 6km Z2–Z3 progresivo (↑10s/km cada 2km) → 3km Z2 → 2km Z1 + 4×20s strides."},
    {"day":"J","type":"EASY","km":10,"d":200,"desc":"10km Z1–Z2 con cuestas suaves. GYM FASE A después."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso o 30min movilidad/yoga runner."},
    {"day":"S","type":"LONG","km":20,"d":400,"desc":"20km Z1–Z2. Máximo D+ disponible. 1 gel en km12. <5:50/km en llano."},
    {"day":"D","type":"EASY","km":12,"d":0,"desc":"12km Z1 recovery."},
   ],"notes":"Reintroduce volumen progresivamente. FC media debería bajar 3-5bpm vs sem1 al mismo ritmo."},

  {"week":3,"phase":1,"phase_name":"Base Aeróbica","load":"MED",
   "title":"Primera carga + tempo real","km":60,"d_plus":900,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":0,"desc":"10km Z1–Z2 + GYM FASE A. Foco squat búlgaro y step-up."},
    {"day":"X","type":"TEMPO","km":15,"d":200,"desc":"15km: 2km Z1 → 3×15min @Z3 (RPE 7/10) con 3min Z1 recuperación → 2km Z1. Un bloque en cuesta si posible."},
    {"day":"J","type":"EASY","km":12,"d":300,"desc":"12km Z1–Z2 con 3×5min subida Z3. GYM FASE A después."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":22,"d":400,"desc":"22km Z1–Z2. 2 geles (km12, km18). Objetivo: finalizar sin fatiga severa."},
    {"day":"D","type":"EASY","km":12,"d":0,"desc":"12km Z1. Recovery. Evalúa sensaciones para semana 4."},
   ],"notes":"Primera semana con carga real. Monitoriza FC reposo cada mañana."},

  {"week":4,"phase":1,"phase_name":"Base Aeróbica","load":"LOW",
   "title":"Deload planificado — sem 4","km":45,"d_plus":500,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":8,"d":0,"desc":"8km Z1 + GYM FASE A cargas −10%."},
    {"day":"X","type":"EASY","km":12,"d":100,"desc":"12km Z1–Z2 suave. Sin calidad. Técnica y cadencia."},
    {"day":"J","type":"GYM","km":0,"d":0,"desc":"GYM FASE A (40min). Solo fuerza."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":18,"d":400,"desc":"18km Z1–Z2. Long reducido. Prueba equipo trail."},
    {"day":"D","type":"EASY","km":10,"d":0,"desc":"10km Z1 recovery."},
   ],"notes":"🔄 DELOAD: −25% volumen. Evidencia: Meeusen 2013 — deload cada 3-4 semanas previene sobreentrenamiento."},

  {"week":5,"phase":1,"phase_name":"Base Aeróbica","load":"MED",
   "title":"Aeróbico + intro colinas","km":62,"d_plus":1200,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":0,"desc":"10km Z1–Z2 + GYM FASE B (intro). Primera sesión con más carga fuerza."},
    {"day":"X","type":"INTERVAL","km":14,"d":400,"desc":"Hill reps: 2km Z1 warm-up → 6×3min subida Z4 (RPE 8/10, bajada trote Z1) → 2km Z1. Evidencia: Patoz 2020 — hill reps mejoran economía trail."},
    {"day":"J","type":"EASY","km":12,"d":300,"desc":"12km Z2 con subidas. GYM FASE B después."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":24,"d":500,"desc":"24km Z1–Z2. Busca Pedriza/Navacerrada si puedes. 2-3 geles. Practica nutrition race-day."},
    {"day":"D","type":"EASY","km":12,"d":0,"desc":"12km Z1. Recovery. Cadencia >172spm."},
   ],"notes":"Inicio de colinas. FC en hill reps debería llegar a Z4–Z5."},

  {"week":6,"phase":1,"phase_name":"Base Aeróbica","load":"MED-HIGH",
   "title":"Carga alta + primer B2B trail","km":65,"d_plus":1500,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":12,"d":0,"desc":"12km Z1–Z2 + GYM FASE B. Squat pesado 4×5@80%1RM."},
    {"day":"X","type":"TEMPO","km":16,"d":300,"desc":"16km: 3km Z1 → 2×20min @Z3 con 5min Z1 recuperación → 3km Z1. Si posible, 2ª parte en subida larga."},
    {"day":"J","type":"EASY","km":12,"d":300,"desc":"12km Z1–Z2 trail o parque. GYM FASE B."},
    {"day":"V","type":"REC","km":8,"d":0,"desc":"8km regenerativo Z1. Decisión según HRV Coros."},
    {"day":"S","type":"LONG","km":26,"d":900,"desc":"26km Z1–Z2 trail. Pedriza o Manzanares si posible. D+>800m. 3 geles. Prueba bastones si los llevas en Palencia."},
    {"day":"D","type":"TRAIL","km":14,"d":300,"desc":"14km Z1–Z2 trail B2B. Piernas cargadas. Simula segunda jornada de carrera. Evidencia: Hoffman 2016 — B2B weekends mejoran tolerancia fatiga acumulada."},
   ],"notes":"Primera sesión B2B real. Nota sensaciones del segundo día."},

  {"week":7,"phase":1,"phase_name":"Base Aeróbica","load":"LOW",
   "title":"Deload + evaluación FC","km":48,"d_plus":600,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":0,"desc":"10km Z1 + GYM FASE B 50% carga."},
    {"day":"X","type":"EASY","km":12,"d":200,"desc":"12km Z1–Z2. Sin calidad. Técnica bajada trail: zancada corta, peso atrás."},
    {"day":"J","type":"GYM","km":0,"d":0,"desc":"GYM FASE B (40min)."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":18,"d":400,"desc":"18km Z1–Z2. TEST: anota FC media y ritmo, compara con semana 1 → muestra progreso base aeróbica."},
    {"day":"D","type":"EASY","km":10,"d":0,"desc":"10km Z1."},
   ],"notes":"🔄 DELOAD + EVALUACIÓN. Compara Strava: misma ruta, ¿FC media bajó 3-5bpm? → adaptación verificada."},

  # ─── FASE 2: DESARROLLO TRAIL / PALENCIA PREP (Sem 8-12 | 11 May – 14 Jun) ─
  {"week":8,"phase":2,"phase_name":"Desarrollo Trail — Palencia Prep","load":"MED",
   "title":"Intro Fase 2 — Trail específico","km":65,"d_plus":1800,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":0,"desc":"10km Z1–Z2 + GYM FASE B."},
    {"day":"X","type":"INTERVAL","km":14,"d":600,"desc":"Hill reps Palencia-specific: 2km Z1 → 8×3min subida >8% pendiente Z4–Z5 con bajada activa → 2km Z1. RPE 8-9 en subidas."},
    {"day":"J","type":"TRAIL","km":12,"d":500,"desc":"12km trail técnico Z2. Power hiking rampas >15%. GYM FASE B."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":28,"d":1200,"desc":"28km Z1–Z2 trail. D+>1000m. Nutrition: gel c/40min, 60g CHO/h. Equipa como Palencia."},
    {"day":"D","type":"B2B","km":16,"d":500,"desc":"16km trail Z1–Z2 B2B. RPE ≤6/10. Registra sensaciones."},
   ],"notes":"Evidencia power hiking: Giovanelli 2016 — power hiking eficiente en pendientes >15% vs correr."},

  {"week":9,"phase":2,"phase_name":"Desarrollo Trail — Palencia Prep","load":"HIGH",
   "title":"VK simulado + volumen alto","km":70,"d_plus":2500,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":0,"desc":"10km Z1 + GYM FASE B (squat pesado, hip thrust, nordic curl)."},
    {"day":"X","type":"VK","km":12,"d":1000,"desc":"VK simulado: 6km subida continua apuntando 1000m D+ total, Z4–Z5. Bajada trote Z1. Tiempo objetivo <65min. Sin montaña: 5×8min cinta al 10%."},
    {"day":"J","type":"TRAIL","km":14,"d":600,"desc":"14km trail técnico Z2–Z3 con bajadas técnicas. GYM FASE B."},
    {"day":"V","type":"REC","km":8,"d":0,"desc":"8km Z1 o descanso según HRV."},
    {"day":"S","type":"LONG","km":30,"d":1500,"desc":"30km Z1–Z2 trail. Primera vez 30km esta temporada. D+>1200m. Nutrition completa. Simula equipación Palencia."},
    {"day":"D","type":"B2B","km":18,"d":900,"desc":"18km trail B2B Z1–Z2. Segunda jornada crucial."},
   ],"notes":"⚠ Semana alta carga. Monitoriza HRV Coros cada mañana. Drop >10%: reduce siguiente sesión."},

  {"week":10,"phase":2,"phase_name":"Desarrollo Trail — Palencia Prep","load":"HIGH",
   "title":"Pico carga pre-Palencia","km":72,"d_plus":3000,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":0,"desc":"10km Z1 + GYM FASE B (última sesión pesada antes de taper)."},
    {"day":"X","type":"INTERVAL","km":15,"d":800,"desc":"Umbral trail: 3km Z1 → 3×20min @Z3–Z4 (RPE 7-8) con 5min Z1, incluye subidas y bajadas → 3km Z1."},
    {"day":"J","type":"TRAIL","km":15,"d":700,"desc":"15km trail técnico Z2–Z3. Máximo terreno irregular disponible."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":32,"d":1800,"desc":"32km Z1–Z2 trail. SESIÓN CLAVE PRE-PALENCIA. Simula esfuerzo carrera. Nutrition: 0.8g CHO/kg/h ≈ 66g CHO/h. Bastones si los llevas."},
    {"day":"D","type":"B2B","km":18,"d":700,"desc":"18km Z1–Z2 B2B piernas cargadas."},
   ],"notes":"Semana pico. Señales sobreentrenamiento: FC reposo +5bpm, insomnio, falta de motivación."},

  {"week":11,"phase":2,"phase_name":"Taper Palencia","load":"MED-LOW",
   "title":"TAPER Palencia — 1/2","km":52,"d_plus":1200,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":0,"desc":"10km Z1. Sin gym, solo activación 15min."},
    {"day":"X","type":"TEMPO","km":12,"d":300,"desc":"12km: 3km Z1 → 4×8min @Z3 con 3min Z1 → 2km Z1. Mantén intensidad, baja volumen."},
    {"day":"J","type":"TRAIL","km":10,"d":400,"desc":"10km trail Z1–Z2 suave. Piernas ágiles."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":20,"d":500,"desc":"20km Z1–Z2 trail. Long reducido −38% vs pico. 3-4 aceleraciones 2min @pace carrera."},
    {"day":"D","type":"EASY","km":10,"d":0,"desc":"10km Z1 recovery."},
   ],"notes":"Evidencia taper: Mujika & Padilla 2003 — 2 semanas, −40-50% volumen, mantener intensidad."},

  {"week":12,"phase":2,"phase_name":"Race Week Palencia","load":"RACE",
   "title":"🏁 RACE WEEK — Maratón MTN Palencia","km":69,"d_plus":4200,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso. Carga CHO día 1/3: 8g CHO/kg ≈ 656g. Arroz, pasta, plátano, pan blanco. Evita fibra."},
    {"day":"M","type":"EASY","km":8,"d":0,"desc":"8km Z1. 4×20s strides. Repasa estrategia y plan nutricional."},
    {"day":"X","type":"EASY","km":6,"d":100,"desc":"6km Z1 + 3×1min @pace objetivo. Activación neuromuscular."},
    {"day":"J","type":"REST","km":0,"d":0,"desc":"Descanso. Prepara mochila, bastones, geles (1 c/40min). Cena: 150g arroz + 120g pollo."},
    {"day":"V","type":"REC","km":3,"d":0,"desc":"3km activación muy suave. Viaje si aplica."},
    {"day":"S","type":"RACE","km":44,"d":3500,"desc":"🏁 MARATÓN MTN PALENCIA (44km/3500m D+). Estrategia: Z2 cómodo primeros 10km, power hike >15%, gel c/35-40min desde km10. OBJETIVO: finalizar fuerte y aprender para TP60."},
    {"day":"D","type":"REC","km":4,"d":0,"desc":"Caminata suave. Proteína 2g/kg en las primeras 24h."},
   ],"notes":"⚠ Palencia es objetivo B — sirve de test para TP60. No la corras como carrera A."},

  # ─── FASE 3: RECUPERACIÓN + SIERRA (Sem 13-24 | 15 Jun – 6 Sep) ────────────
  {"week":13,"phase":3,"phase_name":"Recuperación Palencia","load":"LOW",
   "title":"Recuperación post-Palencia","km":35,"d_plus":400,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso total."},
    {"day":"M","type":"REC","km":6,"d":0,"desc":"6km caminata/trote Z1. Masaje si tienes acceso."},
    {"day":"X","type":"EASY","km":8,"d":0,"desc":"8km Z1 muy suave."},
    {"day":"J","type":"GYM","km":0,"d":0,"desc":"GYM Fase B mantenimiento (50% carga). Movilidad 20min."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"EASY","km":14,"d":300,"desc":"14km Z1–Z2 trail suave. Sin exigencia."},
    {"day":"D","type":"EASY","km":10,"d":100,"desc":"10km Z1."},
   ],"notes":"Evidencia post-maratón montaña: Burt 2011 — daño muscular persiste 5-7 días. Mínimo 10-14 días regeneración."},

  {"week":14,"phase":3,"phase_name":"Rebuild + Sierra Prep","load":"MED",
   "title":"Rebuild aeróbico","km":58,"d_plus":1400,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":0,"desc":"10km Z1–Z2 + GYM FASE C (inicio bloque TP60)."},
    {"day":"X","type":"TEMPO","km":14,"d":400,"desc":"14km: 2km Z1 → 3×15min @Z3 con 4min Z1 → 2km Z1. Primera calidad post-Palencia."},
    {"day":"J","type":"TRAIL","km":12,"d":500,"desc":"12km trail Z2. GYM FASE C."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":22,"d":500,"desc":"22km Z1–Z2. Long moderado en rebuild."},
    {"day":"D","type":"EASY","km":12,"d":0,"desc":"12km Z1 recovery."},
   ],"notes":"Cambia el mindset: de carrera de montaña a ultra (63km). Mayor énfasis en D+ sostenido."},

  {"week":15,"phase":3,"phase_name":"Rebuild + Sierra Prep","load":"MED-HIGH",
   "title":"Carga media-alta + inicio sierra semanal","km":65,"d_plus":2000,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":0,"desc":"10km Z1 + GYM FASE C."},
    {"day":"X","type":"INTERVAL","km":14,"d":700,"desc":"Hill repeats TP60-spec: 10×3min subida Z4 con bajada activa. Foco en técnica de bajada (frena excéntrico)."},
    {"day":"J","type":"TRAIL","km":14,"d":600,"desc":"14km trail Z2. GYM FASE C."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":27,"d":1100,"desc":"27km Z1–Z2 trail. Primer long TP60 del ciclo."},
    {"day":"D","type":"B2B","km":16,"d":600,"desc":"16km trail B2B Z1–Z2."},
   ],"notes":"Si tienes fin de semana en sierra, ambas sesiones allí."},

  {"week":16,"phase":3,"phase_name":"Bloque Sierra","load":"HIGH",
   "title":"🏔 SIERRA — sem 1 (julio)","km":70,"d_plus":3500,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"VK","km":10,"d":1000,"desc":"VK Sierra: subida continua 6km / 1000m D+. Pedriza o Manzanares. Z4–Z5. Tiempo objetivo <65min."},
    {"day":"X","type":"TRAIL","km":16,"d":800,"desc":"16km técnico Z2–Z3 en sierra. Incluye bajada técnica en roca/tierra."},
    {"day":"J","type":"GYM","km":0,"d":0,"desc":"GYM FASE C o sesión peso corporal sierra: pistols, step-ups, jump squats."},
    {"day":"V","type":"REC","km":8,"d":200,"desc":"8km Z1 suave."},
    {"day":"S","type":"LONG","km":30,"d":2000,"desc":"30km Z1–Z2 sierra. D+>1800m. Bastones + mochila hidratación. Nutrition race-simulation completa."},
    {"day":"D","type":"B2B","km":18,"d":1000,"desc":"18km trail B2B Z1–Z2. Objetivo: terminar bien, no rápido."},
   ],"notes":"🏔 Inicio bloque sierra (La Ponderosa / Manzanares). Aprovecha el acceso directo desde casa."},

  {"week":17,"phase":3,"phase_name":"Bloque Sierra","load":"MED",
   "title":"🏔 SIERRA — deload","km":52,"d_plus":2200,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":300,"desc":"10km Z1 sierra suave + GYM FASE C reducido."},
    {"day":"X","type":"TEMPO","km":12,"d":500,"desc":"12km con 2×15min @Z3 en terreno ondulado sierra."},
    {"day":"J","type":"TRAIL","km":10,"d":400,"desc":"10km trail Z1–Z2 técnico."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":22,"d":1200,"desc":"22km deload long. D+ reducido."},
    {"day":"D","type":"EASY","km":10,"d":0,"desc":"10km Z1 recovery."},
   ],"notes":"🔄 DELOAD en bloque sierra. La montaña añade estrés sistémico extra (calor, terreno, altitud)."},

  {"week":18,"phase":3,"phase_name":"Bloque Sierra","load":"HIGH",
   "title":"🏔 SIERRA — pico carga agosto","km":80,"d_plus":4500,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"VK","km":12,"d":1200,"desc":"VK avanzado: 7km / 1200m D+ continuo. Z4–Z5. Objetivo tiempo < sem16. GYM FASE C si posible."},
    {"day":"X","type":"TRAIL","km":18,"d":1000,"desc":"18km técnico Z2–Z3. Máxima dificultad de terreno. Foco bajadas: cadencia >180spm, peso atrás, zancada corta."},
    {"day":"J","type":"TRAIL","km":14,"d":600,"desc":"14km Z2. Recovery activo con D+."},
    {"day":"V","type":"REC","km":8,"d":200,"desc":"8km Z1 suave."},
    {"day":"S","type":"LONG","km":35,"d":2500,"desc":"35km Z1–Z2. SESIÓN REINA del ciclo. D+>2200m. Simula primer 55km TP60. Nutrition completa c/35-40min. Todo el equipo de carrera."},
    {"day":"D","type":"B2B","km":20,"d":1000,"desc":"20km trail B2B Z1–Z2. Segunda jornada dura. RPE máx 7/10."},
   ],"notes":"⚠ SEMANA PICO máximo del ciclo. D+ total ~4500m. HRV, sueño y apetito son semáforos de carga."},

  {"week":19,"phase":3,"phase_name":"Bloque Sierra","load":"LOW-MED",
   "title":"🏔 SIERRA — deload agosto","km":50,"d_plus":2000,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":300,"desc":"10km Z1 + movilidad 20min."},
    {"day":"X","type":"TRAIL","km":12,"d":500,"desc":"12km Z2 técnico suave."},
    {"day":"J","type":"GYM","km":0,"d":0,"desc":"GYM FASE C mantenimiento."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":22,"d":1200,"desc":"22km Z1–Z2 deload long."},
    {"day":"D","type":"EASY","km":10,"d":0,"desc":"10km Z1."},
   ],"notes":"Supercompensación requiere 10-14 días post-semana pico. Este deload es tan importante como el pico."},

  {"week":20,"phase":3,"phase_name":"Bloque Sierra","load":"HIGH",
   "title":"🏔 SIERRA — segundo bloque TP60","km":75,"d_plus":4000,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"VK","km":12,"d":1200,"desc":"VK race-pace TP60: simula esfuerzo sostenible 6-7h. No Z5 total, Z4 controlado."},
    {"day":"X","type":"INTERVAL","km":16,"d":800,"desc":"TP60-specific: 4×10min @Z4 en subidas con 5min bajada activa. Simula repechos TP60."},
    {"day":"J","type":"TRAIL","km":14,"d":600,"desc":"14km Z2 técnico. GYM FASE C."},
    {"day":"V","type":"REC","km":8,"d":200,"desc":"8km Z1."},
    {"day":"S","type":"LONG","km":34,"d":2200,"desc":"34km Z1–Z2 sierra. Race-conditions TP60 completas. Objetivo: terminar en Z2 cómodo."},
    {"day":"D","type":"B2B","km":18,"d":1000,"desc":"18km B2B Z1–Z2."},
   ],"notes":"Segundo bloque pico TP60. Semanas 18 y 20 son las más importantes del ciclo."},

  {"week":21,"phase":3,"phase_name":"Bloque Sierra","load":"MED",
   "title":"🏔 SIERRA — deload septiembre","km":55,"d_plus":2200,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":300,"desc":"10km Z1 + GYM FASE C última sesión pesada."},
    {"day":"X","type":"TEMPO","km":14,"d":600,"desc":"14km: 3×15min @Z3 en ondulado. Fresco y controlado."},
    {"day":"J","type":"TRAIL","km":12,"d":500,"desc":"12km Z2 técnico."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":22,"d":1200,"desc":"22km Z1–Z2. Deload long."},
    {"day":"D","type":"EASY","km":10,"d":0,"desc":"10km Z1."},
   ],"notes":"Último deload antes del taper TP60. Baja gym a mantenimiento."},

  {"week":22,"phase":3,"phase_name":"Pre-Taper","load":"MED-HIGH",
   "title":"Pre-taper — última carga","km":68,"d_plus":3200,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"VK","km":10,"d":900,"desc":"VK final: 5km / 900m D+. Último estímulo de alta intensidad antes del taper."},
    {"day":"X","type":"TRAIL","km":15,"d":700,"desc":"15km Z2–Z3 técnico. GYM FASE C mantenimiento."},
    {"day":"J","type":"EASY","km":10,"d":300,"desc":"10km Z1–Z2."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":28,"d":1800,"desc":"28km Z1–Z2. Último long run serio antes taper. D+>1500m."},
    {"day":"D","type":"B2B","km":15,"d":500,"desc":"15km trail B2B suave."},
   ],"notes":"Última semana de carga alta. A partir de aquí solo bajamos."},

  # ─── FASE 4: TAPER TP60 (Sem 23-25 | 7 Sep – 10 Oct) ──────────────────────
  {"week":23,"phase":4,"phase_name":"Taper TP60","load":"MED-LOW",
   "title":"TAPER TP60 — 1/3","km":55,"d_plus":1800,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":200,"desc":"10km Z1–Z2. Solo mantenimiento."},
    {"day":"X","type":"INTERVAL","km":12,"d":500,"desc":"12km: 4×6min @Z4 con 4min Z1. Mantén intensidad, reduce volumen."},
    {"day":"J","type":"TRAIL","km":10,"d":400,"desc":"10km trail Z2."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":24,"d":1000,"desc":"24km Z1–Z2 trail −30% vs pico. 4 aceleraciones 3min @pace TP60."},
    {"day":"D","type":"EASY","km":10,"d":0,"desc":"10km Z1 recovery."},
   ],"notes":"Taper inicio. Evidencia: Bosquet 2007 — reducción volumen 41-60% óptima. Intensidad: mantener."},

  {"week":24,"phase":4,"phase_name":"Taper TP60","load":"LOW",
   "title":"TAPER TP60 — 2/3","km":40,"d_plus":900,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":8,"d":100,"desc":"8km Z1. Sin presión."},
    {"day":"X","type":"TEMPO","km":10,"d":300,"desc":"10km: 2km Z1 → 3×8min @Z3 con 3min Z1 → 2km Z1. Siente el cuerpo reactivo."},
    {"day":"J","type":"EASY","km":8,"d":200,"desc":"8km Z1–Z2 trail suave."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":16,"d":400,"desc":"16km Z1–Z2. Long muy reducido. 2-3 aceleraciones 2min @pace TP60."},
    {"day":"D","type":"EASY","km":8,"d":0,"desc":"8km Z1."},
   ],"notes":"Sensaciones de piernas pesadas normales y transitorias. No añadas km extra aunque tengas energía."},

  {"week":25,"phase":4,"phase_name":"Race Week TP60","load":"RACE",
   "title":"🏁 RACE WEEK — TP60","km":83,"d_plus":3400,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso. CHO loading día 1/3: 8g CHO/kg ≈ 656g. Arroz, pasta, plátano. Sin fibra ni grasas."},
    {"day":"M","type":"EASY","km":6,"d":0,"desc":"6km Z1. 4×30s strides. CHO loading día 2/3: 9g CHO/kg."},
    {"day":"X","type":"EASY","km":4,"d":0,"desc":"4km activación + 3×1min @pace TP60. CHO loading día 3/3: 10g CHO/kg."},
    {"day":"J","type":"REST","km":0,"d":0,"desc":"Descanso. Prepara material completo: mochila, bastones, 10 geles (1 c/35min), electrolitos, frontales, drop bag si aplica."},
    {"day":"V","type":"REC","km":2,"d":0,"desc":"2km caminata o descanso total. Cena 18:30-19:00h: 180g arroz + 150g pollo + plátano."},
    {"day":"S","type":"RACE","km":63,"d":2500,"desc":"🏁 TP60 (63km/2500m D+). Estrategia: Z2 cómodo primeros 20km, power hike >15%, gel c/35min desde km15, electrolitos en cada CP. OBJETIVO A: completar en 7-8h sintiéndote bien."},
    {"day":"D","type":"REC","km":2,"d":0,"desc":"Caminata suave. Proteína 2g/kg. CHO 1.2g/kg c/hora × 4h. Descanso total."},
   ],"notes":"🎯 OBJETIVO PRINCIPAL del ciclo. Estrategia conservadora primeros 30km → negativa split última parte."},
]

# ═══════════════════════════════════════════════════════════════════════════════
# PLAN DE FUERZA
# Base científica: Beattie 2017, Blagrove 2018, Petersen 2011, Mikkola 2007
# ═══════════════════════════════════════════════════════════════════════════════
STRENGTH = [
  {"id":"A","name":"FASE A — Adaptación Anatómica","weeks":"1–7",
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
  {"id":"B","name":"FASE B — Fuerza Máxima","weeks":"8–16",
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
  {"id":"C","name":"FASE C — Potencia + Específica Trail","weeks":"17–25",
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
PHASE_COLORS = {1:"#f97316",2:"#f59e0b",3:"#22d3ee",4:"#a78bfa"}
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

    phase_names = {1:"BASE AERÓBICA",2:"DESARROLLO TRAIL — PALENCIA PREP",
                   3:"RECUPERACIÓN + BLOQUE SIERRA",4:"TAPER + TP60"}

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

    zones_ref = []
    for lo, hi, zname, zcolor in [
        (0,65,"Z1 Regenerativo","#64748b"),
        (65,75,"Z2 Aeróbico","#22d3ee"),
        (75,85,"Z3 Tempo","#84cc16"),
        (85,92,"Z4 Umbral","#f97316"),
        (92,100,"Z5 VO2max","#ef4444"),
    ]:
        zones_ref.append({"lo":round(hr_max*lo/100),"hi":round(hr_max*hi/100),
                          "name":zname,"color":zcolor})

    zones_html = "".join(f"""
      <div class='zone-row'>
        <span class='z-dot' style='background:{z["color"]}'></span>
        <span class='z-name'>{z["name"]}</span>
        <span class='z-range'>{z["lo"]}–{z["hi"]} bpm</span>
        <span class='z-pct'>{["0-65","65-75","75-85","85-92","92-100"][i]}% FCmax</span>
      </div>""" for i,z in enumerate(zones_ref))

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
  const planStart = new Date('2026-03-24');
  const tbody = document.getElementById('compliance-body');
  const rows = [];
  const phaseNames = {{1:'Base',2:'Trail/Palencia',3:'Sierra',4:'Taper'}};
  const phaseColors = {{1:'#f97316',2:'#f59e0b',3:'#22d3ee',4:'#a78bfa'}};
  
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
    zones_ref = []
    for lo, hi, zname, zcolor in [
        (0,65,"Z1 Regenerativo","#64748b"),
        (65,75,"Z2 Aeróbico","#22d3ee"),
        (75,85,"Z3 Tempo","#84cc16"),
        (85,92,"Z4 Umbral","#f97316"),
        (92,100,"Z5 VO2max","#ef4444"),
    ]:
        zones_ref.append({"lo":round(hr_max*lo/100),"hi":round(hr_max*hi/100),
                          "name":zname,"color":zcolor})

    zones_html = "".join(f"""
      <div class='zone-row'>
        <span class='z-dot' style='background:{z["color"]}'></span>
        <span class='z-name'>{z["name"]}</span>
        <span class='z-range'>{z["lo"]}–{z["hi"]} bpm</span>
        <span class='z-pct'>{["0-65","65-75","75-85","85-92","92-100"][i]}% FCmax</span>
      </div>""" for i,z in enumerate(zones_ref))

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
const PLAN_START = '2026-03-23';

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
  const phaseNames = {{1:'Base',2:'Trail/Palencia',3:'Sierra',4:'Taper'}};
  const phaseColors = {{1:'#f97316',2:'#f59e0b',3:'#22d3ee',4:'#a78bfa'}};
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

    # Replace old script block
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
    print("  Ejecuta 'python trail_analyzer.py' cada lunes para actualizar.\n")

if __name__ == "__main__":
    main()
