#!/usr/bin/env python3
"""
PLAN COMPLETO — Trail 360° Temporada 2026
Genera un HTML detallado con:
  • Plan semanal con objetivos, contexto del mesociclo y razonamiento
  • Programa de fuerza con vídeos de referencia y justificación trail
  • Plan de suplementación periodizado con productos HSN
Uso: python plan_completo.py
"""

import json, sys, webbrowser
from datetime import date, timedelta
from pathlib import Path
from plan_loader import load_plan
from tp_render import format_tp_block

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

OUTPUT_FILE = Path("plan_completo.html")
PLAN_START, PLAN = load_plan("plan.md")

ATHLETE = {
    "name": "Jose",
    "weight_kg": 82,
    "target_weight_kg": 76,
    "hr_max": 188,
    "races": [
        {"id":"palencia","name":"Maratón MTN Palencia",
         "date":"2026-09-12","km":44,"d_plus":3500,"accent":"#f97316"},
        {"id":"tp60","name":"TP60",
         "date":"2026-10-11","km":63,"d_plus":2500,"accent":"#22d3ee"},
    ]
}

# ═══════════════════════════════════════════════════════════════════════════════
# PLAN DE FUERZA — Con vídeos de referencia y justificación trail
# ═══════════════════════════════════════════════════════════════════════════════
STRENGTH = [
  {"id":"A","name":"FASE A — Adaptación Anatómica","weeks":"1–4",
   "goal":"Construir base tendinosa y muscular. Prevenir lesiones. Activar glúteo y core.",
   "freq":"2x/semana (Mar+Jue)","intensity":"3x12-15 reps | 60-70% 1RM | RIR 3-4",
   "ref":"Blagrove 2018 — HST reduce lesiones 50% y mejora economía +3% en fondistas",
   "rationale":"Fase de adaptación: tendones y ligamentos necesitan 6-8 semanas para adaptarse a cargas. Empezar pesado sin esta fase = lesión casi garantizada. Los ejercicios son de patrón básico: sentadilla, bisagra de cadera, unilateral, core. Esta fase también corrige desequilibrios musculares acumulados.",
   "progression":"Semana 1: 60% 1RM. Semana 2: 65% 1RM. Semanas 3-4: 70% 1RM. Subir carga solo si la técnica es impecable.",
   "exercises":[
    {"name":"Sentadilla Goblet","sets":3,"reps":"15","focus":"Glúteo medio + cuádriceps",
     "why_trail":"Patrón básico de empuje de pierna. Base de toda subida en trail. El peso frontal enseña postura vertical.",
     "mistakes":"No dejar que las rodillas colapsen hacia dentro. Profundidad completa (cadera bajo rodillas). Talones en el suelo.",
     "video":"sentadilla goblet kettlebell tecnica correcta"},
    {"name":"Peso Muerto Rumano (RDL)","sets":3,"reps":"12","focus":"Isquiosurales + glúteo mayor",
     "why_trail":"Cadena posterior es el motor de la subida en trail. Los isquios previenen lesiones en bajadas. Clave para economía de carrera.",
     "mistakes":"No redondear la espalda. Mantener barra/mancuernas pegadas a las piernas. Rodillas ligeramente flexionadas, no bloqueadas.",
     "video":"romanian deadlift proper form technique"},
    {"name":"Step-Up con mancuerna","sets":3,"reps":"12/lado","focus":"Cuádriceps unilateral",
     "why_trail":"Simula directamente el patrón de subida en trail. Cada paso en una subida es esencialmente un step-up. Trabajar unilateral corrige desequilibrios.",
     "mistakes":"No empujar con la pierna de abajo. Subir completamente antes de bajar. Banco 40-50cm (ajustar a que el muslo quede paralelo).",
     "video":"step up con mancuerna ejercicio unilateral"},
    {"name":"Hip Thrust con barra","sets":3,"reps":"15","focus":"Glúteo máximo",
     "why_trail":"El glúteo mayor es el motor principal de la extensión de cadera. Cada zancada de subida lo activa. Los trail runners con glúteos débiles compensan con cuádriceps → lesión de rodilla.",
     "mistakes":"No hiperextender la lumbar al final. Apoyar escápulas en el banco. Pies separados anchura de hombros.",
     "video":"hip thrust barbell glute exercise technique"},
    {"name":"Nordic Hamstring Curl","sets":3,"reps":"6-8","focus":"Isquiosurales excéntrico",
     "why_trail":"EL ejercicio más importante para prevención de lesiones. Petersen 2011: -70% incidencia de lesiones de isquio. En trail, las bajadas castigan los isquios excéntricamente. Sin Nordic curls, riesgo de lesión en bajadas largas.",
     "mistakes":"No dejar caer el cuerpo sin control. Bajar lo más lento posible (3-5 segundos). Usar las manos para frenar al principio si es necesario.",
     "video":"nordic hamstring curl progression beginner"},
    {"name":"Calf Raise unilateral","sets":3,"reps":"15/lado","focus":"Sóleo + gastrocnemio",
     "why_trail":"El tendón de Aquiles es la estructura más cargada en trail running. Las elevaciones excéntricas (3s bajada) fortalecen el tendón y previenen tendinopatía.",
     "mistakes":"Excéntrico lento (3 segundos bajando). Rango completo (subir máximo, bajar máximo). No rebotar abajo.",
     "video":"calf raise unilateral excentric achilles"},
    {"name":"Dead Bug","sets":3,"reps":"10/lado","focus":"Core anti-extensión",
     "why_trail":"Estabilidad del tronco durante la carrera. Cada paso en trail genera fuerzas rotacionales que el core debe controlar. Dead bug enseña al core a estabilizar mientras las extremidades se mueven.",
     "mistakes":"Lumbar SIEMPRE pegada al suelo. Si la espalda se despega, estás yendo demasiado lejos. Exhala al extender.",
     "video":"dead bug exercise core antiextension"},
    {"name":"Clamshell con banda","sets":3,"reps":"20/lado","focus":"Abductor de cadera / glúteo medio",
     "why_trail":"El glúteo medio estabiliza la pelvis en cada paso. Si es débil: la rodilla colapsa hacia dentro → IT band syndrome, dolor de rodilla. Especialmente importante en bajadas técnicas donde el pie aterriza en ángulos irregulares.",
     "mistakes":"No rotar el tronco al abrir. Mantener pies juntos. Banda justo encima de las rodillas.",
     "video":"clamshell exercise band glute medius"},
    {"name":"Farmer Carry","sets":3,"reps":"30m","focus":"Core + trapecio + agarre",
     "why_trail":"Simula correr con mochila trail. Estabilidad lumbar bajo carga. Resistencia de agarre para bastones. Postura vertical bajo fatiga.",
     "mistakes":"Hombros atrás y abajo, no encogidos. Pasos cortos y controlados. Mirada al frente. Abdomen tenso.",
     "video":"farmer carry exercise proper form core"},
   ]},

  {"id":"B","name":"FASE B — Fuerza Máxima","weeks":"5–8",
   "goal":"Aumentar fuerza máxima y potencia neuromuscular. Mejora directa de economía de carrera.",
   "freq":"2x/semana (Mar+Jue)","intensity":"4x4-6 reps | 80-85% 1RM | RIR 1-2",
   "ref":"Beattie 2017 — HST 16 sem: economía de carrera +4.6%, potencia +8.6%",
   "rationale":"Fuerza máxima mejora la economía de carrera porque cada paso requiere menos % de tu fuerza total. Si tu sentadilla 1RM sube de 80kg a 100kg, cada paso en una subida (que requiere ~20kg de fuerza) pasa de ser 25% 1RM a 20% 1RM → menos fatiga por paso → más pasos antes de agotar → mejor rendimiento en trail.",
   "progression":"Semana 5: 80% 1RM. Semana 6: 82% 1RM. Semana 7: 84-85% 1RM. Semana 8 (deload): −10% carga. Progresión +2.5kg/semana si la técnica lo permite.",
   "exercises":[
    {"name":"Sentadilla Trasera (Back Squat)","sets":4,"reps":"5","focus":"Potencia pierna global",
     "why_trail":"El rey de los ejercicios de pierna. Trabaja toda la cadena: cuádriceps, glúteos, core. La sentadilla pesada construye la fuerza que luego transferimos a potencia en Fase C.",
     "mistakes":"No dejar que las rodillas se metan hacia dentro. Profundidad: al menos paralelo. Espalda neutra. Mirada al frente. Cinturón si >85% 1RM.",
     "video":"barbell back squat proper form depth"},
    {"name":"Peso Muerto Convencional","sets":4,"reps":"4","focus":"Cadena posterior total",
     "why_trail":"El ejercicio que más fuerza absoluta construye. Cadena posterior completa: glúteos, isquios, erectores, trapecio. En trail, esta fuerza se traduce en capacidad de empuje en subidas largas.",
     "mistakes":"La barra SIEMPRE pegada al cuerpo. No redondear la espalda. Empujar el suelo con los pies, no tirar con la espalda. Cinturón si >85% 1RM.",
     "video":"conventional deadlift technique heavy"},
    {"name":"Split Squat Búlgaro","sets":4,"reps":"6/lado","focus":"Unilateral trail-specific",
     "why_trail":"El ejercicio unilateral más importante para trail. Cada paso en montaña es un split squat con carga. Trabaja equilibrio, fuerza y estabilidad de cadera simultáneamente. Imprescindible.",
     "mistakes":"Pie delantero lo suficientemente adelante para que la rodilla no pase la punta del pie. Torso erguido. Bajar vertical, no adelante.",
     "video":"bulgarian split squat dumbbell technique"},
    {"name":"Hip Thrust Pesado","sets":4,"reps":"6","focus":"Glúteo mayor — potencia",
     "why_trail":"Hip thrust pesado produce la máxima activación del glúteo mayor (Contreras 2015). Velocidad concéntrica máxima: el objetivo es mover la barra explosivamente en la subida.",
     "mistakes":"Pausa 1 segundo arriba en cada rep. No hiperextender. Barra en el pliegue de la cadera con pad.",
     "video":"heavy hip thrust barbell glute activation"},
    {"name":"Nordic Hamstring Curl","sets":4,"reps":"5","focus":"Isquiosurales excéntrico",
     "why_trail":"Mantiene la protección lesional de Fase A pero con más volumen (4 sets). No negociable: este ejercicio nunca sale del programa.",
     "mistakes":"Progresar añadiendo lastre solo cuando controlas 5 reps de 5 segundos excéntricos. Si aún no controlas la bajada, mantén asistencia con manos.",
     "video":"nordic hamstring curl eccentric progression"},
    {"name":"Box Jump","sets":4,"reps":"5","focus":"Potencia concéntrica",
     "why_trail":"Introducción a la plyometría. El box jump enseña al sistema nervioso a reclutar fibras musculares rápidamente. Mikkola 2007: plyometría mejora economía de carrera +4.1%. Aterriza suave y amortiguado.",
     "mistakes":"Caída suave: absorber con las piernas. Resetear entre cada salto (no hacer rebotes). Empezar con cajón bajo e ir subiendo.",
     "video":"box jump exercise plyometric proper landing"},
    {"name":"Copenhagen Plank","sets":3,"reps":"20s/lado","focus":"Aductores + core lateral",
     "why_trail":"Los aductores estabilizan la pelvis en terreno lateral (senderos con inclinación lateral, piedras, raíces). El Copenhagen plank es el ejercicio más eficaz para fortalecer aductores.",
     "mistakes":"No dejar que la cadera se hunda. Cuerpo recto de cabeza a pies. Progresar 5 segundos por semana.",
     "video":"copenhagen plank adductor exercise"},
    {"name":"Pallof Press","sets":3,"reps":"10/lado","focus":"Anti-rotación core",
     "why_trail":"Estabilidad en terreno irregular: cada paso en trail técnico genera fuerzas rotacionales. El Pallof Press enseña al core a resistir rotación bajo carga.",
     "mistakes":"No rotar el tronco. Presionar las manos al frente lentamente. Mantener 2 segundos con brazos extendidos.",
     "video":"pallof press cable antirotation core"},
    {"name":"Single-Leg RDL con mancuerna","sets":3,"reps":"8/lado","focus":"Isquio + glúteo + equilibrio",
     "why_trail":"Propiocepción trail: cada paso en terreno irregular es un single-leg RDL con impacto. Este ejercicio construye la estabilidad específica que necesitas en bajadas técnicas.",
     "mistakes":"No girar la cadera. Pierna trasera recta, formando línea con el tronco. Mirada a un punto fijo.",
     "video":"single leg romanian deadlift balance"},
   ]},

  {"id":"C","name":"FASE C — Potencia + Específica Trail","weeks":"9–10 (+ mant. 11–15)",
   "goal":"Potencia explosiva, tolerancia excéntrica bajadas, mantenimiento fuerza en bloque alto volumen.",
   "freq":"2x/sem (o 1x en semanas pico de volumen)","intensity":"3x4-6 fuerza + 3x8 plyométrico",
   "ref":"Heisten 2021 — plyometría+fuerza mejoran rendimiento ultra-trail en corredores experimentados",
   "rationale":"Fase C convierte la fuerza máxima de Fase B en potencia aplicable. El focus cambia de levantar pesado a mover rápido: jump squats con 20-30% 1RM, depth jumps para stiffness tendinosa (que absorbe impacto en bajadas), lateral bounds para estabilidad en terreno técnico. Esta fase coincide con el bloque sierra: gym se reduce a 1x/semana en las semanas pico de trail.",
   "progression":"Semana 9: potencia, 3 sets. Semana 10: 2 sets (última sesión de fuerza real). Semanas 11-15: solo mantenimiento ligero, sin gym en semanas de carrera (11 Palencia, 15 TP60). En plyometría, progresar altura de cajón mientras dure la fase.",
   "exercises":[
    {"name":"Jump Squat (Sentadilla + salto)","sets":3,"reps":"5","focus":"Potencia pierna",
     "why_trail":"Transforma la fuerza de sentadilla en potencia explosiva. Cada paso en una subida empinada es un mini-jump squat. Con barra vacía o 20-30% 1RM: máxima velocidad concéntrica es el objetivo.",
     "mistakes":"Aterrizar suave con rodillas flexionadas. Resetear entre cada rep. No usar más del 30% 1RM: el objetivo es velocidad, no carga.",
     "video":"jump squat barbell explosive power"},
    {"name":"Peso Muerto Rumano Unilateral","sets":3,"reps":"5/lado","focus":"Fuerza + propiocepción",
     "why_trail":"Control excéntrico en bajadas técnicas: cada paso de bajada es un RDL unilateral con impacto. Este ejercicio construye la fuerza específica para controlar el cuerpo en descenso.",
     "mistakes":"No rotar caderas. Pierna trasera recta. Bajar controlado (3 segundos). Subir con impulso de glúteo.",
     "video":"single leg rdl heavy trail running"},
    {"name":"Depth Jump","sets":3,"reps":"5","focus":"Stiffness tendinosa — bajadas",
     "why_trail":"ESPECÍFICO PARA BAJADAS. Al caer de un cajón y rebotar, los tendones absorben y devuelven energía elástica. Esto es exactamente lo que pasa en cada paso de bajada en trail. Stiffness tendinosa = bajadas más eficientes y menos daño muscular.",
     "mistakes":"Cajón 40-50cm, no más. Contacto con el suelo mínimo (< 0.2s): cae y rebota. No doblar mucho las rodillas al aterrizar. Si el aterrizaje es blando, el cajón es demasiado alto.",
     "video":"depth jump plyometric stiffness tendon"},
    {"name":"Hip Thrust Explosivo","sets":3,"reps":"6","focus":"Potencia glúteo — subidas",
     "why_trail":"Potencia de extensión de cadera para subidas explosivas. Carga moderada (60-70% 1RM) con velocidad concéntrica máxima.",
     "mistakes":"Velocidad explosiva en la subida, control en la bajada. Pausa 0 arriba: arriba y abajo inmediatamente. No rebotar con la cadera.",
     "video":"explosive hip thrust power glute"},
    {"name":"Step-Up Jump","sets":3,"reps":"6/lado","focus":"Específico subida trail",
     "why_trail":"El ejercicio más específico de trail que existe: subir un escalón con impulso y aterrizar controlado. Replica exactamente el patrón motor de subir por senderos con escalones de roca.",
     "mistakes":"Impulso completo con la pierna del cajón. Aterrizar controlado. Alternar piernas o hacer todas de un lado primero.",
     "video":"step up jump exercise explosive single leg"},
    {"name":"Nordic Hamstring Curl","sets":3,"reps":"5","focus":"Mantenimiento isquios",
     "why_trail":"No negociar nunca. En semanas pico: reducir a 2 sets. Pero nunca eliminar. La protección de isquio es un seguro de salud que no expira.",
     "mistakes":"Mantener el nivel de semanas anteriores. No progresar en carga durante Fase C: el volumen de trail es suficiente estímulo excéntrico.",
     "video":"nordic hamstring curl maintenance"},
    {"name":"Lateral Bound","sets":3,"reps":"8/lado","focus":"Estabilidad lateral — trail técnico",
     "why_trail":"Trail técnico requiere saltos laterales constantes: esquivar piedras, raíces, cambios de dirección en senderos estrechos. Los lateral bounds construyen la potencia lateral que ningún ejercicio sagital puede replicar.",
     "mistakes":"Aterrizar en una pierna, estabilizar 2 segundos. No dejar que la rodilla colapse hacia dentro al aterrizar. Progresar distancia del salto.",
     "video":"lateral bound single leg stability"},
    {"name":"Copenhagen Plank progresivo","sets":3,"reps":"30s/lado","focus":"Aductores + core lateral",
     "why_trail":"Progresión de Fase B: de 20s a 30s. Añadir movimiento de pierna libre si dominas la estática.",
     "mistakes":"Si 30s es fácil: añadir flexión-extensión de pierna libre. Si duele la rodilla: volver a versión estática.",
     "video":"copenhagen plank progression dynamic"},
    {"name":"Bear Crawl con peso","sets":3,"reps":"20m","focus":"Core + hombros — bastones",
     "why_trail":"Integración de tren superior para uso de bastones en carrera. En Palencia y TP60, los bastones reducen la carga de piernas ~15% en subidas (Giovanelli 2016). Bear crawl construye la resistencia de hombros y core para usar bastones durante 7-8h.",
     "mistakes":"Rodillas a 2cm del suelo. Espalda plana. Pasos cortos y alternos. El lastre va en chaleco, no en manos.",
     "video":"bear crawl exercise weighted core"},
   ]},
]

# ═══════════════════════════════════════════════════════════════════════════════
# PLAN DE SUPLEMENTACIÓN — Periodizado con productos HSN
# Base científica: Rawson 2011, Hobson 2012, Spriet 2014, Larson-Meyer 2010
# ═══════════════════════════════════════════════════════════════════════════════
SUPPLEMENTS = {
    "overview": {
        "philosophy": "Solo suplementos con evidencia Grado A/B (ISSN/AIS). No existen atajos: la suplementación complementa un plan de nutrición sólido, no lo sustituye. Prioridad 1: comida real. Prioridad 2: sueño. Prioridad 3: suplementación.",
        "hsn_note": "Todos los productos recomendados están disponibles en HSN (hsnstore.com). HSN es marca española con buena relación calidad/precio y certificaciones de pureza.",
    },
    "base_stack": [
        {
            "name": "Creatina Monohidrato",
            "hsn_product": "Creatina Monohidrato (Creapure) HSN",
            "dose": "5g/día, todos los días, sin ciclar",
            "timing": "Con cualquier comida. No importa el momento del día.",
            "phase": "Todas (semanas 1-15)",
            "evidence": "Rawson & Volek 2003: mejora fuerza máxima +8% y potencia +14%. Compatible con resistencia. En trail: mejora la fuerza de las sesiones de gym y la recuperación entre sesiones. Puede añadir 0.5-1kg de agua intracelular (no grasa).",
            "notes": "NO requiere fase de carga (5g/día satura en ~28 días vs 7 días con carga). El peso extra del agua es irrelevante en trail donde la fuerza importa más que el peso. Creapure es la forma más pura y estudiada.",
            "cost_month": "~8€/mes (HSN Creatina Monohidrato 500g)",
        },
        {
            "name": "Beta-Alanina",
            "hsn_product": "Beta-Alanina HSN Raw Series",
            "dose": "3.2g/día en 2 tomas de 1.6g (para reducir parestesias)",
            "timing": "1.6g con desayuno + 1.6g con comida.",
            "phase": "Semanas 5-13 (fases de intensidad)",
            "evidence": "Hobson 2012: mejora rendimiento +2.85% en esfuerzos de 1-10min en Z4-Z5. Ideal para hill repeats y VK simulados. No mejora esfuerzos Z1-Z2 (el 80% de tu entrenamiento), pero sí los intervalos y subidas intensas.",
            "notes": "Se acumula con el tiempo (necesita 4-6 semanas para saturar). Por eso empezamos en semana 5 (coincide con inicio de hill repeats). La parestesia (hormigueo en piel) es inofensiva y se reduce dividiendo la dosis. Dejar de tomar 3 semanas antes de TP60: no aporta beneficio en ultra Z2.",
            "cost_month": "~7€/mes (HSN Beta-Alanina 150g)",
        },
        {
            "name": "Vitamina D3",
            "hsn_product": "Vitamina D3 4000UI HSN",
            "dose": "4000 UI/día (marzo-junio). 2000 UI/día (julio-octubre, más sol).",
            "timing": "Con comida que contenga grasa (absorción).",
            "phase": "Todas",
            "evidence": "Larson-Meyer 2010: déficit de Vit D frecuente en deportistas, incluso en climas soleados (entrenamiento indoor/gym, horarios). Afecta fuerza muscular, sistema inmune y recuperación ósea. Madrid tiene buen sol, pero pasas mucho tiempo indoor.",
            "notes": "Ideal: análisis sanguíneo para confirmar nivel (objetivo: 40-60 ng/mL). Si >50 ng/mL en verano, puede reducir a 1000 UI o suspender julio-agosto.",
            "cost_month": "~5€/mes (HSN Vitamina D3 4000UI 120 cáps)",
        },
        {
            "name": "Omega-3 (EPA+DHA)",
            "hsn_product": "Omega 3 EPA/DHA HSN Essentials",
            "dose": "2-3g EPA+DHA/día (normalmente 3-4 cápsulas según concentración)",
            "timing": "Con comida principal. Dividir en 2 tomas si >2 cápsulas.",
            "phase": "Todas, especialmente bloques de alta carga (sem 8-12, 16-20)",
            "evidence": "Philpott 2018: reduce inflamación y dolor muscular post-esfuerzo. Mejora recuperación en bloques de alto volumen. En trail: semanas de 70-80km con 3000-4500m D+ generan inflamación sistémica severa. Omega-3 modula esa respuesta.",
            "notes": "Buscar productos con alta concentración EPA+DHA (>60%). Los omega-3 baratos tienen poca concentración y necesitas muchas cápsulas. Alternativa: 2-3 raciones de pescado azul/semana.",
            "cost_month": "~10€/mes (HSN Omega 3 120 softgels)",
        },
        {
            "name": "Proteína Whey",
            "hsn_product": "EvoWhey Protein 2.0 HSN / Evolate (Isolate) HSN",
            "dose": "30-40g post-sesión cuando no puedes comer comida real en <1h",
            "timing": "Inmediatamente post-entrenamiento o como snack cuando no alcanzas 1.8g/kg/día.",
            "phase": "Todas",
            "evidence": "Morton 2018: 1.6-2.2g/kg/día de proteína es óptimo para preservar músculo y promover recuperación. Si tu dieta cubre 1.8g/kg con comida real, el whey es prescindible. Si no, es la forma más práctica de llegar.",
            "notes": "EvoWhey 2.0: buena relación calidad/precio, 23g proteína/30g. Evolate (isolate): más puro, menos lactosa, para sesiones con estómago sensible. Sabor chocolate o vainilla mezcla bien con leche o agua.",
            "cost_month": "~18€/mes (HSN EvoWhey 2kg, ~66 servings)",
        },
    ],
    "phase_specific": [
        {
            "name": "Cafeína Anhidra",
            "hsn_product": "Cafeína Anhidra 200mg HSN",
            "dose": "200-250mg (1 cápsula) 45min antes de sesión clave",
            "timing": "Solo antes de sesiones de calidad (tempo, intervalos, VK, long run). NO en easy runs.",
            "phase": "Semanas 5-15, solo sesiones clave (2-3x/semana máximo)",
            "evidence": "Spriet 2014: mejora rendimiento endurance +2-4%. Reduce percepción de esfuerzo. En trail: útil para long runs y hill repeats. NO crear dependencia usándola a diario.",
            "notes": "Si tomas café habitualmente (2-3/día), la cafeína anhidra solo aporta beneficio extra en días de sesión clave. Evitar después de las 14:00 para no afectar sueño. El día de carrera: 250mg en segunda mitad (km30+ en TP60).",
            "cost_month": "~4€/mes (HSN Cafeína 120 cáps)",
        },
        {
            "name": "Citrulina Malato",
            "hsn_product": "L-Citrulina Malato HSN Raw Series",
            "dose": "6-8g, 60min antes de sesión intensa",
            "timing": "Pre-entrenamiento: hill repeats, VK, long runs con D+ alto.",
            "phase": "Semanas 6-13 (bloques de alta intensidad trail)",
            "evidence": "Pérez-Guisado 2010: reduce dolor muscular post-esfuerzo ~40% y mejora rendimiento en series de alta intensidad. Precursor de óxido nítrico: vasodilatación → mejor flujo sanguíneo a músculos activos.",
            "notes": "Combina bien con beta-alanina y cafeína para sesiones clave. Tomar con agua 60min antes. Sabor ácido: mezclar con zumo si es polvo. No tomar en días de descanso (innecesario).",
            "cost_month": "~9€/mes (HSN Citrulina Malato 150g)",
        },
        {
            "name": "Electrolitos / Sales",
            "hsn_product": "HSN Electrolitos / Sales minerales en polvo",
            "dose": "1 servicio en 500ml agua durante sesiones >90min",
            "timing": "Durante long runs, B2B, y sesiones en calor. Imprescindible en verano (julio-septiembre).",
            "phase": "Semanas 5-15, sesiones >90min",
            "evidence": "Sawka 2007: deshidratación >2% peso corporal reduce rendimiento. En trail con calor de Madrid (35°C+), la pérdida de sodio puede alcanzar 1g/hora. Reponer es obligatorio.",
            "notes": "Objetivo: 500-700mg sodio/hora en esfuerzos >3h. En TP60: electrolitos en cada avituallamiento. Practica en long runs para confirmar que toleras el producto. Alternativa casera: 1/4 cucharadita sal + zumo en 500ml agua.",
            "cost_month": "~6€/mes",
        },
    ],
    "race_protocol": {
        "palencia": {
            "name": "Protocolo Carrera — Palencia (44km/3500m D+)",
            "pre_race": "Desayuno 3h antes: 80-100g CHO conocido (avena + plátano + miel). Cafeína 100mg con desayuno.",
            "during": [
                "Gel cada 35-40min desde km10 (6 geles totales)",
                "Objetivo: 60-70g CHO/hora (glucosa:fructosa 2:1)",
                "Electrolitos en cada avituallamiento (500-700mg sodio/hora)",
                "Hidratación: 400-600ml/hora según calor",
                "Cafeína 150mg extra en km25-30 (segunda mitad)",
            ],
            "post_race": "30min post: batido 40g proteína + 80g CHO. 2-4h post: comida sólida rica en proteína y CHO. 24h: objetivo 2g/kg proteína y 10g/kg CHO.",
        },
        "tp60": {
            "name": "Protocolo Carrera — TP60 (63km/2500m D+)",
            "pre_race": "Desayuno 3h antes: 100-120g CHO conocido. Cafeína 100mg con desayuno si habitual.",
            "during": [
                "Gel cada 35min desde km15 (10 geles totales)",
                "Objetivo: 70-80g CHO/hora (glucosa:fructosa 2:1 — entrenado desde semana 5)",
                "Electrolitos cada 45min (700-1000mg sodio/hora si calor)",
                "Hidratación: 500-700ml/hora",
                "Comida sólida opcional en avituallamientos km25-35 (mini sándwich, fruta)",
                "Cafeína 250mg en km35-40 (segunda mitad: mejora concentración y reduce RPE)",
                "Si náuseas: reducir CHO a 45-50g/h, aumentar electrolitos, sorbos pequeños",
            ],
            "post_race": "Inmediato: caldo caliente + proteína líquida. 1h: comida completa. 24h: proteína 2g/kg, CHO 10g/kg, sueño >9h.",
        },
    },
    "not_recommended": [
        {"name": "BCAA (aminoácidos ramificados)", "reason": "Innecesario si la proteína total es adecuada (1.8g/kg). Los BCAAs son un subconjunto de la proteína whey que ya tomas. Doble gasto sin beneficio."},
        {"name": "Pre-workouts complejos (con mezcla estimulantes)", "reason": "La mayoría tienen dosis sub-óptimas de ingredientes activos ('prop blend'). Mejor tomar cada ingrediente por separado a la dosis correcta: cafeína + citrulina + beta-alanina."},
        {"name": "Antioxidantes dosis altas (Vit C >500mg, Vit E)", "reason": "Ristow 2009: antioxidantes en dosis altas pueden BLOQUEAR las adaptaciones al entrenamiento. El estrés oxidativo del ejercicio es la señal que produce la adaptación. Bloquearla = menos mejora."},
        {"name": "L-Carnitina", "reason": "Evidencia inconsistente para rendimiento. La carnitina dietética es suficiente en una dieta con proteína animal."},
        {"name": "Glutamina", "reason": "No mejora recuperación ni sistema inmune en deportistas bien alimentados (Gleeson 2008). Innecesaria con proteína adecuada."},
    ],
    "monthly_cost": "Coste mensual total estimado HSN: ~61-67€/mes (stack completo base + fase-specific). Solo base: ~48€/mes.",
}

# ═══════════════════════════════════════════════════════════════════════════════
# COLORES Y CONFIGURACIÓN
# ═══════════════════════════════════════════════════════════════════════════════
PHASE_COLORS = {1:"#f97316",2:"#f59e0b",3:"#22d3ee",4:"#a78bfa",5:"#34d399"}
PHASE_NAMES = {1:"RECONSTRUCCIÓN BASE",2:"CONSTRUCCIÓN ESPECÍFICA",
               3:"AFINADO PALENCIA",4:"RECUPERAR + PUENTE TP60",5:"TAPER TP60"}
SESSION_CONFIG = {
    "REST":    {"bg":"#1e293b","border":"#334155","label":"REST","emoji":""},
    "EASY":    {"bg":"#0f2d2d","border":"#22d3ee","label":"EASY Z1-Z2","emoji":""},
    "REC":     {"bg":"#1a1f2e","border":"#475569","label":"RECOVERY","emoji":""},
    "TEMPO":   {"bg":"#1a2f0f","border":"#84cc16","label":"TEMPO Z3","emoji":""},
    "INTERVAL":{"bg":"#2d1a0f","border":"#f97316","label":"INTERVALOS Z4","emoji":""},
    "LONG":    {"bg":"#0f1a2d","border":"#6366f1","label":"LONG RUN","emoji":""},
    "TRAIL":   {"bg":"#1a1008","border":"#d97706","label":"TRAIL Z2","emoji":""},
    "GYM":     {"bg":"#1a0f2d","border":"#a78bfa","label":"GYM FUERZA","emoji":""},
    "B2B":     {"bg":"#2d1010","border":"#ef4444","label":"B2B TRAIL","emoji":""},
    "RACE":    {"bg":"#2d1f00","border":"#fbbf24","label":"CARRERA","emoji":""},
    "VK":      {"bg":"#2d0f1a","border":"#f43f5e","label":"VERTICAL KM","emoji":""},
}

# ═══════════════════════════════════════════════════════════════════════════════
# GENERADOR HTML
# ═══════════════════════════════════════════════════════════════════════════════
def esc(s):
    """Escape HTML special characters."""
    return str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")

def youtube_search_url(query):
    """Generate YouTube search URL for exercise form videos."""
    import urllib.parse
    return "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(query)

def generate_html():
    today = date.today()

    # Race countdown
    races_html = ""
    for r in ATHLETE["races"]:
        rd = date.fromisoformat(r["date"])
        days_left = (rd - today).days
        races_html += f"""
        <div class='race-card' style='border-color:{r["accent"]}'>
          <div class='rc-name' style='color:{r["accent"]}'>{esc(r["name"])}</div>
          <div class='rc-info'>{r["km"]}km / {r["d_plus"]:,}m D+</div>
          <div class='rc-days' style='color:{r["accent"]}'>{days_left}</div>
          <div class='rc-label'>dias</div>
          <div class='rc-date'>{rd.strftime("%d %b %Y")}</div>
        </div>"""

    # ── WEEK HTML ──
    def _tp_html(s):
        block = format_tp_block(s)
        if not block:
            return ""
        return "<div class='tp-label'>📋 Copiar a TrainingPeaks</div><pre class='tp-block'>" + esc(block) + "</pre>"

    def session_html(s, week_num):
        cfg = SESSION_CONFIG.get(s["type"], SESSION_CONFIG["EASY"])
        day_idx = ["L","M","X","J","V","S","D"].index(s["day"])
        d = PLAN_START + timedelta(weeks=week_num-1, days=day_idx)
        date_str = d.strftime("%d %b")
        km_str = f"<span class='sess-km'>{s['km']}km" + (f" ↑{s['d']}m" if s["d"]>0 else "") + "</span>" if s["km"]>0 else ""
        return f"""
        <div class='session-card' style='background:{cfg["bg"]};border-left:3px solid {cfg["border"]}'>
          <div class='sess-header'>
            <span class='sess-day'>{s["day"]}</span>
            <span class='sess-type' style='color:{cfg["border"]}'>{cfg["label"]}</span>
            {km_str}
            <span class='sess-date'>{date_str}</span>
          </div>
          <p class='sess-desc'>{esc(s["desc"])}</p>
          {_tp_html(s)}
        </div>"""

    def week_html(w):
        pc = PHASE_COLORS.get(w["phase"],"#666")
        load_colors = {"LOW":"#22d3ee","LOW-MED":"#84cc16","MED":"#f59e0b",
                       "MED-HIGH":"#f97316","HIGH":"#ef4444","RACE":"#fbbf24"}
        lc = load_colors.get(w["load"],"#666")
        sessions = "".join(session_html(s, w["week"]) for s in w["sessions"])
        wstart = (PLAN_START + timedelta(weeks=w["week"]-1)).strftime("%d %b")
        wend = (PLAN_START + timedelta(weeks=w["week"]-1, days=6)).strftime("%d %b")

        # Enhanced coaching section
        coaching_section = ""
        if w.get("objective"):
            coaching_section += f"""
            <div class='week-coaching'>
              <div class='wc-section'>
                <div class='wc-label'>OBJETIVO DE LA SEMANA</div>
                <div class='wc-text'>{esc(w["objective"])}</div>
              </div>"""
        if w.get("context"):
            coaching_section += f"""
              <div class='wc-section'>
                <div class='wc-label'>CONTEXTO EN EL MESOCICLO</div>
                <div class='wc-text'>{esc(w["context"])}</div>
              </div>"""
        if w.get("key_session"):
            coaching_section += f"""
              <div class='wc-section key-session'>
                <div class='wc-label'>SESIÓN CLAVE</div>
                <div class='wc-text'>{esc(w["key_session"])}</div>
              </div>"""
        if w.get("coaching"):
            coaching_section += f"""
              <div class='wc-section'>
                <div class='wc-label'>COACHING</div>
                <div class='wc-text'>{esc(w["coaching"])}</div>
              </div>"""
        if coaching_section:
            coaching_section += "</div>"

        return f"""
        <details class='week-item' {"open" if w.get("load")=="RACE" else ""}>
          <summary class='week-summary'>
            <span class='wk-num' style='background:{pc}22;color:{pc}'>Sem {w["week"]}</span>
            <span class='wk-dates'>{wstart} – {wend}</span>
            <span class='wk-title'>{esc(w["title"])}</span>
            <span class='wk-stats'>{w["km"]}km / ↑{w["d_plus"]}m</span>
            <span class='wk-load' style='background:{lc}22;color:{lc}'>{w["load"]}</span>
          </summary>
          <div class='week-body'>
            {coaching_section}
            <div class='sessions-grid'>{sessions}</div>
          </div>
        </details>"""

    # Group weeks by phase
    phases_html = ""
    phases = {}
    for w in PLAN:
        p = w["phase"]
        if p not in phases: phases[p] = []
        phases[p].append(w)

    for pid, weeks in phases.items():
        pc = PHASE_COLORS[pid]
        pname = PHASE_NAMES[pid]
        w_start = weeks[0]["week"]; w_end = weeks[-1]["week"]
        total_km = sum(w["km"] for w in weeks)
        total_d = sum(w["d_plus"] for w in weeks)
        wks_html = "".join(week_html(w) for w in weeks)
        ds = (PLAN_START + timedelta(weeks=w_start-1)).strftime("%d %b")
        de = (PLAN_START + timedelta(weeks=w_end-1, days=6)).strftime("%d %b")
        phases_html += f"""
        <div class='phase-block'>
          <div class='phase-header' style='border-left:4px solid {pc}'>
            <div class='phase-title' style='color:{pc}'>FASE {pid}: {pname}</div>
            <div class='phase-meta'>
              Semanas {w_start}–{w_end} ({ds} – {de}) &nbsp;|&nbsp; {total_km} km &nbsp;|&nbsp; {total_d:,}m D+ acumulado
            </div>
          </div>
          <div class='weeks-list'>{wks_html}</div>
        </div>"""

    # ── STRENGTH HTML ──
    def strength_html():
        html = ""
        for sp in STRENGTH:
            exs_html = ""
            for e in sp["exercises"]:
                vid_url = youtube_search_url(e["video"])
                exs_html += f"""
                <div class='exercise-card'>
                  <div class='ex-header'>
                    <div class='ex-name-main'>{esc(e["name"])}</div>
                    <div class='ex-sets'>{e["sets"]}x{e["reps"]}</div>
                    <a href='{vid_url}' target='_blank' class='ex-video-btn' title='Ver técnica en YouTube'>&#9654; Video</a>
                  </div>
                  <div class='ex-focus-tag'>{esc(e["focus"])}</div>
                  <div class='ex-detail'>
                    <div class='ex-detail-section'>
                      <span class='ex-detail-label'>Por qué en trail:</span>
                      <span>{esc(e["why_trail"])}</span>
                    </div>
                    <div class='ex-detail-section mistakes'>
                      <span class='ex-detail-label'>Errores comunes:</span>
                      <span>{esc(e["mistakes"])}</span>
                    </div>
                  </div>
                </div>"""

            html += f"""
            <div class='strength-phase'>
              <div class='sp-header-main'>
                <div class='sp-id-big'>{sp["id"]}</div>
                <div class='sp-info'>
                  <div class='sp-name-main'>{esc(sp["name"])}</div>
                  <div class='sp-meta-line'>Semanas {sp["weeks"]} &nbsp;|&nbsp; {sp["freq"]} &nbsp;|&nbsp; {sp["intensity"]}</div>
                </div>
              </div>
              <div class='sp-rationale'>
                <div class='sp-rationale-label'>POR QUÉ ESTA FASE</div>
                <p>{esc(sp["rationale"])}</p>
              </div>
              <div class='sp-progression'>
                <div class='sp-progression-label'>PROGRESIÓN</div>
                <p>{esc(sp["progression"])}</p>
              </div>
              <div class='sp-ref-line'>{esc(sp["ref"])}</div>
              <div class='sp-goal'>{esc(sp["goal"])}</div>
              <div class='exercises-grid'>{exs_html}</div>
            </div>"""
        return html

    # ── SUPPLEMENTS HTML ──
    def supps_html():
        # Base stack
        base_html = ""
        for s in SUPPLEMENTS["base_stack"]:
            base_html += f"""
            <div class='supp-card'>
              <div class='supp-header'>
                <div class='supp-name-main'>{esc(s["name"])}</div>
                <div class='supp-phase-tag'>{esc(s["phase"])}</div>
              </div>
              <div class='supp-hsn'>HSN: {esc(s["hsn_product"])}</div>
              <div class='supp-detail-grid'>
                <div class='supp-detail-item'>
                  <div class='supp-detail-label'>Dosis</div>
                  <div class='supp-detail-value'>{esc(s["dose"])}</div>
                </div>
                <div class='supp-detail-item'>
                  <div class='supp-detail-label'>Timing</div>
                  <div class='supp-detail-value'>{esc(s["timing"])}</div>
                </div>
                <div class='supp-detail-item'>
                  <div class='supp-detail-label'>Coste</div>
                  <div class='supp-detail-value'>{esc(s["cost_month"])}</div>
                </div>
              </div>
              <div class='supp-evidence'>{esc(s["evidence"])}</div>
              <div class='supp-notes'>{esc(s["notes"])}</div>
            </div>"""

        # Phase-specific
        phase_html = ""
        for s in SUPPLEMENTS["phase_specific"]:
            phase_html += f"""
            <div class='supp-card phase-specific'>
              <div class='supp-header'>
                <div class='supp-name-main'>{esc(s["name"])}</div>
                <div class='supp-phase-tag specific'>{esc(s["phase"])}</div>
              </div>
              <div class='supp-hsn'>HSN: {esc(s["hsn_product"])}</div>
              <div class='supp-detail-grid'>
                <div class='supp-detail-item'>
                  <div class='supp-detail-label'>Dosis</div>
                  <div class='supp-detail-value'>{esc(s["dose"])}</div>
                </div>
                <div class='supp-detail-item'>
                  <div class='supp-detail-label'>Timing</div>
                  <div class='supp-detail-value'>{esc(s["timing"])}</div>
                </div>
                <div class='supp-detail-item'>
                  <div class='supp-detail-label'>Coste</div>
                  <div class='supp-detail-value'>{esc(s["cost_month"])}</div>
                </div>
              </div>
              <div class='supp-evidence'>{esc(s["evidence"])}</div>
              <div class='supp-notes'>{esc(s["notes"])}</div>
            </div>"""

        # Race protocol
        race_html = ""
        for key in ["palencia", "tp60"]:
            rp = SUPPLEMENTS["race_protocol"][key]
            during_items = "".join(f"<li>{esc(d)}</li>" for d in rp["during"])
            race_html += f"""
            <div class='race-protocol-card'>
              <div class='rp-name'>{esc(rp["name"])}</div>
              <div class='rp-section'>
                <div class='rp-label'>PRE-CARRERA</div>
                <p>{esc(rp["pre_race"])}</p>
              </div>
              <div class='rp-section'>
                <div class='rp-label'>DURANTE LA CARRERA</div>
                <ul>{during_items}</ul>
              </div>
              <div class='rp-section'>
                <div class='rp-label'>POST-CARRERA</div>
                <p>{esc(rp["post_race"])}</p>
              </div>
            </div>"""

        # Not recommended
        not_rec_html = ""
        for nr in SUPPLEMENTS["not_recommended"]:
            not_rec_html += f"""
            <div class='not-rec-item'>
              <div class='not-rec-name'>{esc(nr["name"])}</div>
              <div class='not-rec-reason'>{esc(nr["reason"])}</div>
            </div>"""

        return f"""
        <div class='supps-overview'>
          <p class='supps-philosophy'>{esc(SUPPLEMENTS["overview"]["philosophy"])}</p>
          <p class='supps-hsn-note'>{esc(SUPPLEMENTS["overview"]["hsn_note"])}</p>
          <div class='supps-cost'>Coste mensual estimado: {esc(SUPPLEMENTS["monthly_cost"])}</div>
        </div>

        <h3 class='supps-section-title'>Stack Base — Todo el ciclo</h3>
        <div class='supps-grid'>{base_html}</div>

        <h3 class='supps-section-title'>Fase-Specific — Solo cuando aplica</h3>
        <div class='supps-grid'>{phase_html}</div>

        <h3 class='supps-section-title'>Protocolo de Carrera</h3>
        <div class='race-protocols'>{race_html}</div>

        <h3 class='supps-section-title'>NO Recomendados</h3>
        <div class='not-rec-list'>{not_rec_html}</div>
        """

    # ── PERIODIZATION CHART DATA ──
    plan_json = json.dumps([{
        "week": w["week"], "phase": w["phase"], "km": w["km"],
        "d_plus": w["d_plus"], "load": w["load"], "title": w["title"]
    } for w in PLAN])

    # ── FULL HTML ──
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Plan Completo Trail 360° — Jose / Temporada 2026</title>
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
body::after{{content:'';position:fixed;inset:0;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cpath d='M0 100 Q50 70 100 100 Q150 130 200 100' fill='none' stroke='%230f2040' stroke-width='1.5'/%3E%3Cpath d='M0 130 Q50 100 100 130 Q150 160 200 130' fill='none' stroke='%230f2040' stroke-width='1'/%3E%3Cpath d='M0 70 Q50 40 100 70 Q150 100 200 70' fill='none' stroke='%230f2040' stroke-width='1'/%3E%3C/svg%3E");
  opacity:.4;pointer-events:none;z-index:0}}

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
  padding:14px 18px;text-align:center;min-width:140px}}
.rc-name{{font-family:'Rajdhani',sans-serif;font-size:11px;font-weight:600;letter-spacing:1px;margin-bottom:2px}}
.rc-info{{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--muted);margin-bottom:8px}}
.rc-days{{font-family:'Rajdhani',sans-serif;font-size:42px;font-weight:700;line-height:1}}
.rc-label{{font-size:10px;color:var(--muted);letter-spacing:2px;text-transform:uppercase;margin-bottom:4px}}
.rc-date{{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--muted)}}

/* TABS */
.tabs{{display:flex;gap:4px;margin-bottom:28px;border-bottom:1px solid var(--border);overflow-x:auto}}
.tab-btn{{font-family:'Rajdhani',sans-serif;font-weight:600;letter-spacing:1px;font-size:13px;
  text-transform:uppercase;background:transparent;border:none;color:var(--muted);
  padding:10px 18px;cursor:pointer;border-bottom:2px solid transparent;
  transition:color .2s,border-color .2s;white-space:nowrap}}
.tab-btn:hover{{color:var(--text)}}
.tab-btn.active{{color:var(--accent);border-bottom-color:var(--accent)}}
.tab-panel{{display:none}}
.tab-panel.active{{display:block}}

/* PERIODIZATION CHART */
.period-chart-wrap{{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:24px}}
.period-chart-wrap h3{{font-family:'Rajdhani',sans-serif;font-size:14px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;margin-bottom:16px}}
.period-chart-wrap canvas{{max-height:260px}}

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
.wk-dates{{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--muted);min-width:110px}}
.wk-title{{flex:1;font-family:'Rajdhani',sans-serif;font-size:14px;font-weight:600}}
.wk-stats{{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--accent)}}
.wk-load{{font-size:10px;font-family:'Rajdhani',sans-serif;letter-spacing:1px;padding:2px 8px;border-radius:20px;flex-shrink:0}}
.week-body{{padding:12px 16px;border-top:1px solid var(--border)}}

/* COACHING SECTIONS */
.week-coaching{{margin-bottom:16px;display:grid;gap:10px}}
.wc-section{{background:var(--surface3);border-radius:8px;padding:12px 16px}}
.wc-section.key-session{{border-left:3px solid var(--amber);background:#1a1608}}
.wc-label{{font-family:'Rajdhani',sans-serif;font-size:11px;font-weight:600;letter-spacing:1.5px;
  color:var(--muted);text-transform:uppercase;margin-bottom:6px}}
.wc-text{{font-size:14px;color:#cbd5e1;line-height:1.7}}

/* SESSIONS */
.sessions-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:8px}}
.session-card{{padding:10px 12px;border-radius:6px}}
.sess-header{{display:flex;align-items:center;gap:8px;margin-bottom:4px;flex-wrap:wrap}}
.sess-day{{font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:500;
  background:var(--surface3);padding:2px 7px;border-radius:4px;flex-shrink:0}}
.sess-type{{font-family:'Rajdhani',sans-serif;font-size:11px;font-weight:600;letter-spacing:1px;flex:1}}
.sess-km{{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--muted)}}
.sess-date{{font-size:10px;color:var(--muted);margin-left:auto}}
.sess-desc{{font-size:13px;color:#94a3b8;line-height:1.5}}
.tp-label{{font-size:10px;color:var(--muted);letter-spacing:1px;margin-top:6px;text-transform:uppercase}}
.tp-block{{font-family:'JetBrains Mono',monospace;font-size:11px;background:var(--surface3);
  color:#94a3b8;padding:8px 10px;border-radius:4px;white-space:pre;overflow-x:auto;margin:4px 0 0;line-height:1.5}}

/* STRENGTH */
.strength-phase{{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:24px;margin-bottom:24px}}
.sp-header-main{{display:flex;align-items:center;gap:16px;margin-bottom:16px}}
.sp-id-big{{font-family:'Rajdhani',sans-serif;font-size:48px;font-weight:700;color:var(--purple);line-height:1;min-width:50px}}
.sp-info{{flex:1}}
.sp-name-main{{font-family:'Rajdhani',sans-serif;font-size:18px;font-weight:600}}
.sp-meta-line{{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--muted);margin-top:2px}}
.sp-rationale,.sp-progression{{background:var(--surface3);border-radius:8px;padding:12px 16px;margin-bottom:10px}}
.sp-rationale-label,.sp-progression-label{{font-family:'Rajdhani',sans-serif;font-size:11px;font-weight:600;
  letter-spacing:1.5px;color:var(--amber);text-transform:uppercase;margin-bottom:6px}}
.sp-rationale p,.sp-progression p{{font-size:14px;color:#cbd5e1;line-height:1.7}}
.sp-ref-line{{font-size:12px;color:var(--purple);font-style:italic;margin-bottom:8px}}
.sp-goal{{font-size:13px;color:#94a3b8;margin-bottom:16px}}

.exercises-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:12px}}
.exercise-card{{background:var(--surface3);border:1px solid var(--border);border-radius:10px;padding:16px}}
.ex-header{{display:flex;align-items:center;gap:8px;margin-bottom:8px;flex-wrap:wrap}}
.ex-name-main{{font-family:'Rajdhani',sans-serif;font-size:15px;font-weight:600;flex:1}}
.ex-sets{{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--accent);
  background:var(--surface2);padding:2px 8px;border-radius:4px}}
.ex-video-btn{{font-family:'Rajdhani',sans-serif;font-size:11px;font-weight:600;letter-spacing:1px;
  color:#fff;background:#ef4444;padding:3px 10px;border-radius:4px;text-decoration:none;
  transition:background .2s;flex-shrink:0}}
.ex-video-btn:hover{{background:#dc2626}}
.ex-focus-tag{{font-size:12px;color:var(--amber);margin-bottom:10px}}
.ex-detail{{display:grid;gap:8px}}
.ex-detail-section{{font-size:13px;color:#94a3b8;line-height:1.5}}
.ex-detail-section.mistakes{{color:#f87171}}
.ex-detail-label{{font-family:'Rajdhani',sans-serif;font-size:11px;font-weight:600;
  letter-spacing:1px;color:var(--muted);text-transform:uppercase;display:block;margin-bottom:2px}}

/* SUPPLEMENTS */
.supps-overview{{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:24px}}
.supps-philosophy{{font-size:15px;color:#cbd5e1;line-height:1.7;margin-bottom:10px}}
.supps-hsn-note{{font-size:13px;color:var(--muted);margin-bottom:10px;font-style:italic}}
.supps-cost{{font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--green);
  background:var(--surface3);padding:8px 14px;border-radius:6px;display:inline-block}}
.supps-section-title{{font-family:'Rajdhani',sans-serif;font-size:16px;font-weight:600;
  letter-spacing:1px;color:var(--accent);margin:24px 0 14px;
  padding-bottom:8px;border-bottom:1px solid var(--border)}}
.supps-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px;margin-bottom:8px}}
.supp-card{{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:18px}}
.supp-card.phase-specific{{border-left:3px solid var(--amber)}}
.supp-header{{display:flex;align-items:center;gap:10px;margin-bottom:8px;flex-wrap:wrap}}
.supp-name-main{{font-family:'Rajdhani',sans-serif;font-size:16px;font-weight:600;flex:1}}
.supp-phase-tag{{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--accent);
  background:var(--surface3);padding:2px 8px;border-radius:4px}}
.supp-phase-tag.specific{{color:var(--amber)}}
.supp-hsn{{font-size:12px;color:var(--purple);margin-bottom:10px;font-style:italic}}
.supp-detail-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:8px;margin-bottom:10px}}
.supp-detail-item{{background:var(--surface3);border-radius:6px;padding:8px 12px}}
.supp-detail-label{{font-size:10px;color:var(--muted);margin-bottom:2px}}
.supp-detail-value{{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text)}}
.supp-evidence{{font-size:13px;color:#94a3b8;line-height:1.5;margin-bottom:8px;
  padding:8px 12px;background:var(--surface3);border-radius:6px;border-left:2px solid var(--green)}}
.supp-notes{{font-size:12px;color:var(--muted);line-height:1.5}}

/* RACE PROTOCOL */
.race-protocols{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px;margin-bottom:8px}}
.race-protocol-card{{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px;
  border-top:3px solid var(--orange)}}
.rp-name{{font-family:'Rajdhani',sans-serif;font-size:16px;font-weight:600;margin-bottom:14px;color:var(--orange)}}
.rp-section{{margin-bottom:12px}}
.rp-label{{font-family:'Rajdhani',sans-serif;font-size:11px;font-weight:600;letter-spacing:1.5px;
  color:var(--muted);text-transform:uppercase;margin-bottom:6px}}
.rp-section p{{font-size:13px;color:#94a3b8;line-height:1.5}}
.rp-section ul{{list-style:none;padding:0}}
.rp-section li{{font-size:13px;color:#94a3b8;line-height:1.5;padding:3px 0;padding-left:16px;position:relative}}
.rp-section li::before{{content:'>';position:absolute;left:0;color:var(--orange);font-weight:bold}}

/* NOT RECOMMENDED */
.not-rec-list{{display:grid;gap:8px;margin-bottom:24px}}
.not-rec-item{{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:12px 16px;
  border-left:3px solid var(--red)}}
.not-rec-name{{font-family:'Rajdhani',sans-serif;font-size:14px;font-weight:600;color:var(--red);margin-bottom:4px}}
.not-rec-reason{{font-size:13px;color:#94a3b8;line-height:1.5}}

/* SUMMARY GRID */
.summary-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;margin-bottom:24px}}
.summary-card{{background:var(--surface2);border:1px solid var(--border);border-radius:10px;padding:16px;text-align:center}}
.summary-value{{font-family:'JetBrains Mono',monospace;font-size:28px;font-weight:500;
  background:linear-gradient(135deg,var(--accent),var(--amber));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent}}
.summary-label{{font-family:'Rajdhani',sans-serif;font-size:11px;color:var(--muted);letter-spacing:1px;
  text-transform:uppercase;margin-top:4px}}

@media(max-width:768px){{
  .exercises-grid,.supps-grid,.race-protocols{{grid-template-columns:1fr}}
  .header-top{{flex-direction:column}}
  .sp-header-main{{flex-direction:column;text-align:center}}
  .sp-id-big{{font-size:36px}}
}}
</style>
</head>
<body>
<div id="app">

<header>
  <div class="header-top">
    <div class="brand">
      <div class="brand-title">Plan Completo Trail 360° — 2026</div>
      <div class="brand-sub" data-plan-start="{PLAN_START.isoformat()}">PALENCIA MTN 44km/3500m + TP60 63km/2500m | Madrid | {len(PLAN)} semanas</div>
    </div>
    <div class="races-header">{races_html}</div>
  </div>
</header>

<!-- Summary stats -->
<div class="summary-grid">
  <div class="summary-card">
    <div class="summary-value">{len(PLAN)}</div>
    <div class="summary-label">Semanas</div>
  </div>
  <div class="summary-card">
    <div class="summary-value">{sum(w["km"] for w in PLAN):,}</div>
    <div class="summary-label">km totales</div>
  </div>
  <div class="summary-card">
    <div class="summary-value">{sum(w["d_plus"] for w in PLAN):,}</div>
    <div class="summary-label">m D+ totales</div>
  </div>
  <div class="summary-card">
    <div class="summary-value">{sum(len(sp["exercises"]) for sp in STRENGTH)}</div>
    <div class="summary-label">Ejercicios fuerza</div>
  </div>
  <div class="summary-card">
    <div class="summary-value">3</div>
    <div class="summary-label">Fases gym</div>
  </div>
  <div class="summary-card">
    <div class="summary-value">{len(SUPPLEMENTS["base_stack"])+len(SUPPLEMENTS["phase_specific"])}</div>
    <div class="summary-label">Suplementos</div>
  </div>
</div>

<nav class="tabs">
  <button class="tab-btn active" onclick="switchTab('plan')">Plan Entrenamiento</button>
  <button class="tab-btn" onclick="switchTab('fuerza')">Fuerza Trail</button>
  <button class="tab-btn" onclick="switchTab('supps')">Suplementacion</button>
</nav>

<!-- ═══ TAB: PLAN ═══ -->
<div id="tab-plan" class="tab-panel active">
  <div class="period-chart-wrap">
    <h3>Periodizacion — Volumen y D+ semanal</h3>
    <canvas id="chartPeriod"></canvas>
  </div>
  {phases_html}
</div>

<!-- ═══ TAB: FUERZA ═══ -->
<div id="tab-fuerza" class="tab-panel">
  <div style="background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:20px">
    <h3 style="font-family:'Rajdhani',sans-serif;font-size:14px;letter-spacing:1px;color:var(--muted);text-transform:uppercase;margin-bottom:12px">Por que fuerza en trail running</h3>
    <p style="font-size:14px;color:#cbd5e1;line-height:1.7;margin-bottom:12px">La evidencia es clara: los corredores de trail que hacen fuerza 2x/semana mejoran economía de carrera +4-5%, reducen lesiones -50%, y rinden mejor en bajadas técnicas. El gym no es opcional: es la diferencia entre terminar una ultra sufriendo o terminarla fuerte.</p>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:10px">
      <div style="font-size:13px;color:#94a3b8;padding:10px 14px;background:var(--surface3);border-radius:6px;border-left:2px solid var(--purple)">Beattie 2017: HST 16 sem → economía +4.6%, potencia +8.6%</div>
      <div style="font-size:13px;color:#94a3b8;padding:10px 14px;background:var(--surface3);border-radius:6px;border-left:2px solid var(--purple)">Petersen 2011: Nordic curl → -70% lesiones isquiosurales</div>
      <div style="font-size:13px;color:#94a3b8;padding:10px 14px;background:var(--surface3);border-radius:6px;border-left:2px solid var(--purple)">Blagrove 2018: HST reduce lesiones 50% en fondistas</div>
      <div style="font-size:13px;color:#94a3b8;padding:10px 14px;background:var(--surface3);border-radius:6px;border-left:2px solid var(--purple)">Mikkola 2007: plyometria 8 sem → economía carrera +4.1%</div>
      <div style="font-size:13px;color:#94a3b8;padding:10px 14px;background:var(--surface3);border-radius:6px;border-left:2px solid var(--purple)">Regla: NUNCA fuerza pesada el dia antes de sesion clave o long run</div>
      <div style="font-size:13px;color:#94a3b8;padding:10px 14px;background:var(--surface3);border-radius:6px;border-left:2px solid var(--purple)">Nordic curl es NO NEGOCIABLE: aparece en las 3 fases, siempre</div>
    </div>
  </div>
  {strength_html()}
</div>

<!-- ═══ TAB: SUPLEMENTACIÓN ═══ -->
<div id="tab-supps" class="tab-panel">
  {supps_html()}
</div>

</div><!-- end #app -->

<script>
const PLAN_DATA = {plan_json};

function switchTab(id) {{
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelector(`[onclick="switchTab('${{id}}')"]`).classList.add('active');
  document.getElementById('tab-'+id).classList.add('active');
}}

// Periodization chart
window.addEventListener('DOMContentLoaded', () => {{
  const labels = PLAN_DATA.map(w => 'S'+w.week);
  const km = PLAN_DATA.map(w => w.km);
  const dplus = PLAN_DATA.map(w => w.d_plus);
  const phaseColors = {{1:'#f97316',2:'#f59e0b',3:'#22d3ee',4:'#a78bfa'}};
  const bgColors = PLAN_DATA.map(w => phaseColors[w.phase]+'44');
  const borderColors = PLAN_DATA.map(w => phaseColors[w.phase]);

  new Chart(document.getElementById('chartPeriod').getContext('2d'), {{
    type:'bar',
    data:{{
      labels: labels,
      datasets:[
        {{label:'km', data:km, backgroundColor:bgColors, borderColor:borderColors, borderWidth:2, borderRadius:4, yAxisID:'y'}},
        {{label:'D+ (m)', data:dplus, type:'line', borderColor:'#ef444488', backgroundColor:'#ef444422',
          pointBackgroundColor:'#ef4444', tension:.3, fill:true, pointRadius:3, yAxisID:'y1'}},
      ]
    }},
    options:{{
      responsive:true, maintainAspectRatio:true,
      plugins:{{
        legend:{{display:true, labels:{{color:'#64748b',font:{{size:11,family:'JetBrains Mono'}}}}}},
      }},
      scales:{{
        x:{{grid:{{color:'#1e2d45'}},ticks:{{color:'#64748b',font:{{size:10,family:'JetBrains Mono'}}}}}},
        y:{{position:'left',grid:{{color:'#1e2d45'}},ticks:{{color:'#22d3ee',font:{{size:10,family:'JetBrains Mono'}},callback:v=>v+'km'}}}},
        y1:{{position:'right',grid:{{display:false}},ticks:{{color:'#ef4444',font:{{size:10,family:'JetBrains Mono'}},callback:v=>v+'m'}}}}
      }}
    }}
  }});
}});
</script>
</body>
</html>"""
    return html

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════
def main():
    print("\n" + "="*60)
    print("  PLAN COMPLETO TRAIL 360° — Temporada 2026")
    print("  Jose · Palencia MTN + TP60")
    print("="*60 + "\n")

    print("Generando plan completo HTML...")
    html = generate_html()
    OUTPUT_FILE.write_text(html, encoding="utf-8")

    total_km = sum(w["km"] for w in PLAN)
    total_d = sum(w["d_plus"] for w in PLAN)
    total_ex = sum(len(sp["exercises"]) for sp in STRENGTH)

    print(f"  Plan generado: {OUTPUT_FILE.resolve()}")
    print(f"\n  Contenido:")
    print(f"  - {len(PLAN)} semanas de entrenamiento detallado")
    print(f"  - {total_km:,} km totales / {total_d:,}m D+ total")
    print(f"  - {total_ex} ejercicios de fuerza en 3 fases (con videos)")
    print(f"  - Plan de suplementacion periodizado HSN")
    print(f"  - {len(SUPPLEMENTS['base_stack'])} suplementos base + {len(SUPPLEMENTS['phase_specific'])} fase-specific")
    print(f"  - Protocolos de carrera Palencia + TP60")

    print("\n  Abriendo en el navegador...")
    webbrowser.open(OUTPUT_FILE.resolve().as_uri())
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
