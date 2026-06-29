# PlanTrail — Living Training Plan

> **Source of truth.** This file is the authoritative training plan. It is maintained
> chat-driven: the athlete asks to "review the last weeks and propose adjustments," the
> assistant pulls real Strava data, computes load signals, proposes a next week, and —
> after the athlete approves — edits §D (current week) and appends to §E (adjustment log).
> Design: `docs/superpowers/specs/2026-06-29-living-plan-md-design.md`.

**Athlete:** Jose · 77 kg (→ 76 kg target) · Madrid
**Lab:** HRmax 194 · VT1 152 · VT2 172 · half-marathon 1:35 (VDOT ~57)
**Last updated:** 2026-06-29

---

## A. Goals & constraints

| Race | Date | Distance | D+ | Role |
|---|---|---|---|---|
| Maratón MTN Palencia | 2026-09-12 (Sat) | 44 km | 3,500 m | **B-race** — vertical tune-up, mini-taper, raced hard |
| **TP60** | **2026-10-11 (Sun)** | **63 km** | **2,500 m** | **A-race — peak here** |

- **15 training weeks**, Mon 2026-06-29 → TP60. Palencia (more vertical than the A-race)
  doubles as the peak climbing stimulus, 4 weeks out.
- **Availability:** 5–6 days/week (runs + gym).
- **History note:** recurring low-grade niggles (knee / hip / back), no current injury.
  Self-described as "training poorly" lately → **ramp conservatively, protect tissue.**

### Heart-rate zones (anchored to lab VT1/VT2 — physiological, not %HRmax)

| Zone | bpm | Use |
|---|---|---|
| **Z1** Recovery | < 142 | recovery jogs, easy aerobic, fat oxidation |
| **Z2** Aerobic base | 142–152 (ceiling = VT1) | the bulk of all volume |
| **Z3** Tempo/threshold | 152–172 (VT1→VT2) | tempo, sustained climbs — *the gray zone to ration* |
| **Z4** VO2/threshold | 172–185 (> VT2) | structured intervals, hard efforts |
| **Z5** Max | > 185 | strides/sprints only |

Pace reference (from Strava race-pace zones, flat): **easy ≥ 5:36/km**, tempo ~4:20–4:50/km.
On climbs, **govern by HR/effort, not pace.**

---

## B. Training philosophy — the *why* (the modern core)

Each principle below is named, justified, and tied to **how it changes the week**. This is
what makes the plan evidence-based rather than a generic template.

1. **Polarized 80/20 (Seiler).** ~80% of *time* below VT1 (Z1–Z2), ~20% genuinely hard
   (Z4+), and **as little as possible in the Z3 "gray zone."** The common amateur failure
   is running easy days too hard and hard days too easy. → *We measure actual time-in-zone
   from Strava each week and correct drift; easy means easy (≥ 5:36/km / < 142 bpm).*

2. **ACWR — acute:chronic workload ratio.** The modern injury-and-fitness governor: keep
   the 7-day load vs the 28-day rolling average in the **0.8–1.3 sweet spot.** Below 0.8 =
   detraining/loss; above 1.3 = sharply elevated injury risk. → *Every weekly recalculation
   targets a ratio inside this band — this is the primary driver of how much next week grows.*

3. **Vertical load is its own axis.** Mountain fitness is governed by **climbing volume
   (D+)** and **eccentric descent load**, not km. → *We periodize D+ separately from distance;
   a "big week" can mean more climbing at the same mileage.*

4. **Durability & aerobic decoupling.** The real marker of endurance base is **how little
   HR drifts up at a fixed pace late in a long run** (decoupling < 5% = well-developed
   aerobic base). Pace alone lies. → *We track decoupling on long runs; rising same-pace HR
   = back off; falling = aerobic system improving, safe to progress.*

5. **Strength for economy (Beattie).** Heavy lifting + plyometrics improve running economy
   and tendon stiffness (more free speed per heartbeat) and protect against injury. →
   *2×/week heavy in base/build, converted to power, tapered to nothing in race weeks.*

6. **Eccentric / descent-specific preparation.** Downhill running causes the muscle damage
   that destroys late-race performance in long mountain events. → *We deliberately build
   descent tolerance so the quads survive Palencia's 3,500 m and TP60's descents.*

7. **Fueling progression (Jeukendrup).** The gut is trainable. → *Practice in-run carbs
   every long run, building 50 → 90 g CHO/h, rehearsing exact race products before each race.*

8. **Taper (Mujika).** Cut **volume** ~40–60%, **keep intensity** touches. → *Sharpness is
   retained while fatigue clears; no new fitness is built in the last 2 weeks — only freshness.*

---

## C. Periodization map (15 weeks)

| Phase | Weeks | Dates | Focus | km/wk | Peak D+/wk |
|---|---|---|---|---|---|
| 1. Rebuild base + climbing | W1–4 | Jun 29 – Jul 26 | re-establish volume, polarize, weekend B2B, GYM A | 40 → 58 (deload 44) | ~1,500 |
| 2. Specific build | W5–8 | Jul 27 – Aug 23 | peak volume + D+, long → 32 km, fueling, GYM B | 58 → 72 (deload 52) | ~2,400 |
| 3. Palencia sharpen | W9–11 | Aug 24 – Sep 12 | peak vertical week, back off, mini-taper → **race** | 66 → 50 → 34+race | ~2,800 |
| 4. Recover + TP60 bridge | W12–13 | Sep 14 – Sep 27 | recover, then final TP60-specific big week (long 38 km) | 30 → 60 | ~1,600 |
| 5. Taper TP60 | W14–15 | Sep 28 – Oct 11 | 2-wk Mujika taper, hold sharpness → **race** | 42 → 28+race | low |

> The macro map is stable. Weekly recalculation tunes *within* the current phase — it does
> not discard the periodization.

---

## D. Current & upcoming week

> Current week and all 15 weeks live in the Plan data block below; the dashboard renders them.

---

## E. Adjustment log

### 2026-06-29 — Baseline analysis + W1 recalculated (start of block)

**Data:** last 4 weeks (Jun 1–28), Strava MCP.

| Week | km | D+ | Run time | Load (ΣRE) |
|---|---|---|---|---|
| Jun 1–7 | 27.0 | 287 m | 2.6 h | 157 |
| Jun 8–14 | 49.6 | 792 m | 5.0 h | 308 |
| Jun 15–21 | 35.9 | 654 m | 3.5 h | 194 |
| Jun 22–28 | 30.7 | 973 m | 3.7 h | 162 |

**Diagnosis (through the §B lenses):**
- **ACWR ≈ 0.8–1.0** (acute Jun 22–28 vs 28-day avg, load proxy = relative effort / moving
  time). Healthy — no spike, slight room to ramp.
- **Chronic base ≈ 36 km/wk, ~677 m D+/wk.** D+ is trending up well (287 → 973 m); climbing
  capacity is the strength to build on.
- **Polarization (provisional):** several road runs sit at RE 62–75 / adjusted 4:45–5:45/km
  — likely **gray-zone (Z3)**, not truly easy. Suspected too-few genuinely-easy Z1 days and
  no *structured* hard sessions. *To confirm: pull HR streams next review for real
  time-in-zone + decoupling.*
- **Tissue:** athlete reports recurring knee/hip/back niggles → favor conservative ramp.

**Decision:** start W1 at **~40 km / ~700 m** instead of the original 46 km (avoids the
+28% / ACWR ≈ 1.3 jump → keeps ACWR ≈ 1.1). Reinforce *easy = easy* and reintroduce one
clean structured quality session (Wed). Hold the macro map unchanged.

**Next review:** after W1 (≈ Jul 6) — pull HR streams to verify the 80/20 split and long-run
decoupling, then set W2.

---

## Plan data (single source — edited per re-plan)

```yaml
plan_start: '2026-06-29'
weeks:
- week: 1
  phase: 1
  phase_name: Reconstrucción base
  load: LOW-MED
  title: Re-entrada
  km: 46
  d_plus: 800
  notes: Re-entrada controlada desde la base de junio. Registra FC reposo cada mañana.
  objective: Re-anclar la rutina de entrenamiento desde la base de junio sin estrés. Reactivar fuerza
    (GYM Fase A) y cadencia.
  context: 'Semana 1 del bloque de 15 hacia TP60. Vienes de un junio irregular (~36 km/sem) pero sin lesión,
    así que re-entramos por encima de cero, no desde cero. Distribución polarizada 80/20 (Seiler 2010)
    desde el primer día: casi todo Z1–Z2, solo el bloque de cuestas del miércoles toca Z3. El objetivo
    no es cargar, es restablecer el hábito y la mecánica.'
  key_session: X — 5×3min Z3 en cuesta. Primer estímulo de calidad en pendiente, suave. Si las piernas
    no responden, reduce a 3 repeticiones. La cuesta protege articulaciones vs. velocidad en llano.
  coaching: 'Registra FC en reposo cada mañana desde hoy: es tu baseline para las 15 semanas. GYM Fase
    A = adaptación anatómica, cargas ligeras 3×12-15. No superes Z2 en el largo del sábado; sin geles
    para fomentar oxidación de grasas.'
  sessions:
  - day: L
    type: REST
    km: 0
    d: 0
    desc: Descanso / movilidad 15 min.
  - day: M
    type: EASY
    km: 8
    d: 0
    desc: 8km Z2 (≤152). Run first → GYM Fase A.
    tp:
      sport: Run
      title: Easy 8km Z2 (+GYM A)
      steps:
      - {kind: warmup, dist_km: 1, zone: z1}
      - {kind: run, dist_km: 6, zone: z2}
      - {kind: cooldown, dist_km: 1, zone: z1}
  - day: X
    type: TEMPO
    km: 11
    d: 250
    desc: '11km: 3km Z1 + 5×3min Z3 en cuesta (2min Z1 bajada) + 2km Z1.'
    tp:
      sport: TrailRun
      title: Cuestas 5×3min Z3
      steps:
      - {kind: warmup, dist_km: 3, zone: z1}
      - {kind: interval, reps: 5, on: '3:00', on_zone: z3, off: '2:00', off_zone: z1, note: 'en cuesta, trote bajada'}
      - {kind: cooldown, dist_km: 2, zone: z1}
  - day: J
    type: TRAIL
    km: 8
    d: 200
    desc: 8km Z2 trail rolling.
    tp:
      sport: TrailRun
      title: Trail 8km Z2 rolling
      steps:
      - {kind: warmup, dist_km: 1, zone: z1}
      - {kind: run, dist_km: 6, zone: z2}
      - {kind: cooldown, dist_km: 1, zone: z1}
  - day: V
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: S
    type: LONG
    km: 13
    d: 350
    desc: 13km Z1–Z2, busca 350m D+. 1 gel km10.
    tp:
      sport: TrailRun
      title: Long 13km Z1–Z2 +350m
      steps:
      - {kind: warmup, dist_km: 2, zone: z1}
      - {kind: run, dist_km: 9, zone: z2, note: 'busca D+, power-hike >15%; 1 gel km10'}
      - {kind: cooldown, dist_km: 2, zone: z1}
  - day: D
    type: EASY
    km: 6
    d: 0
    desc: 6km Z1 recovery.
    tp:
      sport: Run
      title: Recovery 6km Z1
      steps:
      - {kind: run, dist_km: 6, zone: z1}
- week: 2
  phase: 1
  phase_name: Reconstrucción base
  load: MED
  title: Volumen on
  km: 54
  d_plus: 1100
  notes: FC media al mismo ritmo debería bajar 2-4 bpm vs sem 1.
  objective: Reintroducir volumen aeróbico (+17% vs sem 1). Primera sesión de tempo con bloques definidos.
    Consolidar GYM 2×/sem.
  context: 'Segunda semana: subimos a 54 km manteniendo la base ancha. El cuerpo todavía construye la
    plataforma aeróbica que sostendrá la fase específica. El tempo del miércoles introduce calidad controlada
    sin vaciar; el largo del sábado empieza a acumular tiempo en pie.'
  key_session: S — Largo 18km con máximo D+ disponible. Es el ladrillo aeróbico de la semana; termínalo
    controlado, capaz de seguir.
  coaching: 'A mismo ritmo, tu FC media debería bajar 2-4 bpm respecto a la semana 1: señal de que la
    base mejora. Los strides del tempo son aceleraciones de 20s, no sprints — mejoran economía neuromuscular.'
  sessions:
  - day: L
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: M
    type: EASY
    km: 9
    d: 0
    desc: 9km Z2. Run first → GYM Fase A.
    tp:
      sport: Run
      title: Easy 9km Z2 (+GYM A)
      steps:
      - {kind: warmup, dist_km: 1, zone: z1}
      - {kind: run, dist_km: 7, zone: z2}
      - {kind: cooldown, dist_km: 1, zone: z1}
  - day: X
    type: TEMPO
    km: 13
    d: 100
    desc: '13km: 3km Z1 + 2×12min Z3 (3min Z1) + 2km Z1 + 4×20s strides.'
    tp:
      sport: Run
      title: Tempo 2×12min Z3 + strides
      steps:
      - {kind: warmup, dist_km: 3, zone: z1}
      - {kind: interval, reps: 2, on: '12:00', on_zone: z3, off: '3:00', off_zone: z1}
      - {kind: strides, reps: 4, on: '0:20', on_zone: z4, off: '0:40', off_zone: z1}
      - {kind: cooldown, dist_km: 2, zone: z1}
  - day: J
    type: TRAIL
    km: 9
    d: 200
    desc: 9km Z2 trail. Run first → GYM Fase A.
    tp:
      sport: TrailRun
      title: Trail 9km Z2 (+GYM A)
      steps:
      - {kind: warmup, dist_km: 1, zone: z1}
      - {kind: run, dist_km: 7, zone: z2}
      - {kind: cooldown, dist_km: 1, zone: z1}
  - day: V
    type: REST
    km: 0
    d: 0
    desc: Descanso / 30min movilidad.
  - day: S
    type: LONG
    km: 18
    d: 800
    desc: 18km Z1–Z2, máximo D+ disponible. 2 geles.
    tp:
      sport: TrailRun
      title: Long 18km Z1–Z2 máx D+
      steps:
      - {kind: warmup, dist_km: 2, zone: z1}
      - {kind: run, dist_km: 14, zone: z2, note: 'máximo D+ disponible; 2 geles'}
      - {kind: cooldown, dist_km: 2, zone: z1}
  - day: D
    type: EASY
    km: 5
    d: 0
    desc: 5km Z1 recovery.
    tp:
      sport: Run
      title: Recovery 5km Z1
      steps:
      - {kind: run, dist_km: 5, zone: z1}
- week: 3
  phase: 1
  phase_name: Reconstrucción base
  load: MED-HIGH
  title: Primera carga de desnivel
  km: 60
  d_plus: 1500
  notes: Primera semana con desnivel real. Acabar el largo controlado, no vaciado.
  objective: Primera semana exigente del bloque. Tempo sostenido en cuesta a Z3. Elevar D+ semanal a 1500m.
  context: 'Tercera semana: 60 km y 1500m de D+, la primera carga real. Los 3×15min Z3 en cuesta son el
    primer estímulo de umbral aeróbico con especificidad vertical — exactamente lo que Palencia exige.
    En periodización por bloques (Issurin 2010) estas semanas construyen la casa aeróbica que luego amueblamos
    con calidad específica.'
  key_session: X — 3×15min Z3 en cuesta (RPE 7/10). El estímulo de umbral más largo hasta ahora; un bloque
    en rampa simula las subidas de Palencia.
  coaching: 'La semana 4 es deload, así que puedes empujar esta sabiendo que la siguiente baja. Si la
    FC en reposo del miércoles está elevada, convierte el tempo en rodaje Z2. GYM: foco en squat búlgaro
    y step-up, lo más específico de trail.'
  sessions:
  - day: L
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: M
    type: EASY
    km: 10
    d: 0
    desc: 10km Z2. Run first → GYM Fase A.
    tp:
      sport: Run
      title: Easy 10km Z2 (+GYM A)
      steps:
      - {kind: warmup, dist_km: 1, zone: z1}
      - {kind: run, dist_km: 8, zone: z2}
      - {kind: cooldown, dist_km: 1, zone: z1}
  - day: X
    type: TEMPO
    km: 14
    d: 400
    desc: '14km: 2km Z1 + 3×15min Z3 en cuesta (3min Z1) + 2km Z1.'
    tp:
      sport: TrailRun
      title: Cuestas 3×15min Z3
      steps:
      - {kind: warmup, dist_km: 2, zone: z1}
      - {kind: interval, reps: 3, on: '15:00', on_zone: z3, off: '3:00', off_zone: z1, note: en cuesta}
      - {kind: cooldown, dist_km: 2, zone: z1}
  - day: J
    type: TRAIL
    km: 10
    d: 300
    desc: 10km Z2 trail. Run first → GYM Fase A.
    tp:
      sport: TrailRun
      title: Trail 10km Z2 (+GYM A)
      steps:
      - {kind: warmup, dist_km: 1, zone: z1}
      - {kind: run, dist_km: 8, zone: z2}
      - {kind: cooldown, dist_km: 1, zone: z1}
  - day: V
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: S
    type: LONG
    km: 20
    d: 800
    desc: 20km Z1–Z2 trail ~800m. Power-hike >15%. 50g CHO/h.
    tp:
      sport: TrailRun
      title: Long 20km Z1–Z2 trail +800m
      steps:
      - {kind: warmup, dist_km: 2, zone: z1}
      - {kind: run, dist_km: 16, zone: z2, note: 'power-hike >15%; 50g CHO/h'}
      - {kind: cooldown, dist_km: 2, zone: z1}
  - day: D
    type: EASY
    km: 6
    d: 0
    desc: 6km Z1 recovery.
    tp:
      sport: Run
      title: Recovery 6km Z1
      steps:
      - {kind: run, dist_km: 6, zone: z1}
- week: 4
  phase: 1
  phase_name: Reconstrucción base
  load: LOW
  title: DELOAD
  km: 44
  d_plus: 700
  notes: Semana de absorción planificada. Llegar fresco al domingo.
  objective: Deload para absorber la carga de las semanas 1-3 (−27% volumen) manteniendo frecuencia.
  context: 'Primer deload del bloque. Meeusen 2013: un deload cada 3-4 semanas previene sobreentrenamiento
    y permite supercompensación. No es perder entrenamiento, es consolidar las adaptaciones de las 3 semanas
    previas. Llegarás fresco al sábado.'
  key_session: S — Largo 14km relajado. Aprovecha para probar equipo de trail (zapatillas, mochila, bastones)
    que usarás en Palencia.
  coaching: 'Sin calidad esta semana: técnica y cadencia. GYM Fase A con cargas −10%. Si tienes que elegir,
    prioriza dormir sobre cualquier sesión.'
  sessions:
  - day: L
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: M
    type: EASY
    km: 8
    d: 0
    desc: 8km Z2. GYM Fase A cargas −10%.
    tp:
      sport: Run
      title: Easy 8km Z2 (+GYM A −10%)
      steps:
      - {kind: warmup, dist_km: 1, zone: z1}
      - {kind: run, dist_km: 6, zone: z2}
      - {kind: cooldown, dist_km: 1, zone: z1}
  - day: X
    type: EASY
    km: 10
    d: 100
    desc: 10km Z2 + 6×20s strides (sin bloque duro).
    tp:
      sport: Run
      title: Easy 10km Z2 + strides
      steps:
      - {kind: warmup, dist_km: 1, zone: z1}
      - {kind: run, dist_km: 7, zone: z2}
      - {kind: strides, reps: 6, on: '0:20', on_zone: z4, off: '0:40', off_zone: z1}
      - {kind: cooldown, dist_km: 1, zone: z1}
  - day: J
    type: TRAIL
    km: 8
    d: 200
    desc: 8km Z2 trail suave.
    tp:
      sport: TrailRun
      title: Trail 8km Z2 suave
      steps:
      - {kind: warmup, dist_km: 1, zone: z1}
      - {kind: run, dist_km: 6, zone: z2}
      - {kind: cooldown, dist_km: 1, zone: z1}
  - day: V
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: S
    type: LONG
    km: 14
    d: 400
    desc: 14km Z1–Z2 relajado.
    tp:
      sport: TrailRun
      title: Long 14km Z1–Z2 relajado
      steps:
      - {kind: warmup, dist_km: 2, zone: z1}
      - {kind: run, dist_km: 10, zone: z2}
      - {kind: cooldown, dist_km: 2, zone: z1}
  - day: D
    type: EASY
    km: 4
    d: 0
    desc: 4km Z1 recovery.
    tp:
      sport: Run
      title: Recovery 4km Z1
      steps:
      - {kind: run, dist_km: 4, zone: z1}
- week: 5
  phase: 2
  phase_name: Construcción específica
  load: HIGH
  title: Reinicio build + fueling
  km: 60
  d_plus: 1500
  notes: Desde aquí ensaya nutrición de carrera cada sábado.
  objective: Arrancar la fase específica. Intervalos Z3-Z4 en cuesta. Iniciar GYM Fase B (fuerza máxima)
    y ensayo de nutrición de carrera.
  context: 'La fase específica empieza aquí: de base pura a base con especificidad de trail. Los intervalos
    en cuesta (Patoz 2020) son el puente entre lo aeróbico y lo específico — mejoran economía en pendiente
    y potencia de empuje. Beattie 2017: la fuerza máxima mejora la economía de carrera, por eso la Fase
    B introduce cargas pesadas.'
  key_session: S — Largo 22km con ensayo de fueling 60g CHO/h + electrolitos. Desde esta semana, cada
    sábado ensayas la nutrición exacta de carrera (Jeukendrup 2014).
  coaching: 'Primera sesión de GYM Fase B: empieza con el 70% del peso que crees poder manejar; la técnica
    antes que la carga. Los intervalos pueden dar agujetas las primeras veces — el jueves es trail suave
    a propósito.'
  sessions:
  - day: L
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: M
    type: EASY
    km: 10
    d: 0
    desc: 10km Z2. GYM Fase B (fuerza máxima).
    tp:
      sport: Run
      title: Easy 10km Z2 (+GYM B)
      steps:
      - {kind: warmup, dist_km: 1, zone: z1}
      - {kind: run, dist_km: 8, zone: z2}
      - {kind: cooldown, dist_km: 1, zone: z1}
  - day: X
    type: INTERVAL
    km: 14
    d: 450
    desc: '14km: 4×8min Z3–Z4 en cuesta (3min rec) + strides.'
    tp:
      sport: TrailRun
      title: Intervalos 4×8min Z3–Z4 cuesta
      steps:
      - {kind: warmup, dist_km: 2, zone: z1}
      - {kind: interval, reps: 4, on: '8:00', on_zone: z4, off: '3:00', off_zone: z1, note: 'en cuesta, Z3–Z4'}
      - {kind: strides, reps: 4, on: '0:20', on_zone: z4, off: '0:40', off_zone: z1}
      - {kind: cooldown, dist_km: 2, zone: z1}
  - day: J
    type: TRAIL
    km: 10
    d: 250
    desc: 10km Z2 trail. GYM Fase B.
    tp:
      sport: TrailRun
      title: Trail 10km Z2 (+GYM B)
      steps:
      - {kind: warmup, dist_km: 1, zone: z1}
      - {kind: run, dist_km: 8, zone: z2}
      - {kind: cooldown, dist_km: 1, zone: z1}
  - day: V
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: S
    type: LONG
    km: 22
    d: 800
    desc: 22km Z1–Z2 ~800m. Ensayo fueling 60g CHO/h + electrolitos.
    tp:
      sport: TrailRun
      title: Long 22km Z1–Z2 +800m fueling
      steps:
      - {kind: warmup, dist_km: 2, zone: z1}
      - {kind: run, dist_km: 18, zone: z2, note: '60g CHO/h + electrolitos; ensayo fueling'}
      - {kind: cooldown, dist_km: 2, zone: z1}
  - day: D
    type: EASY
    km: 4
    d: 0
    desc: 4km Z1 shakeout.
    tp:
      sport: Run
      title: Shakeout 4km Z1
      steps:
      - {kind: run, dist_km: 4, zone: z1}
- week: 6
  phase: 2
  phase_name: Construcción específica
  load: HIGH
  title: Intro back-to-back
  km: 68
  d_plus: 2000
  notes: Fin de semana B2B = especificidad TP60/Palencia. Come y duerme para absorber.
  objective: Introducir el fin de semana back-to-back (sábado largo + domingo medio en fatiga). Elevar
    D+ a 2000m.
  context: 'El B2B es la especificidad clave de TP60 y Palencia: correr cansado el domingo enseña al cuerpo
    a oxidar grasa y gestionar fatiga acumulada como en carrera (Koop 2016). Subimos a 68 km con un B2B
    de 22+11. La FC del domingo estará alta a ritmo bajo: es normal y es el objetivo.'
  key_session: S+D — Back-to-back 22km/900m + 11km en piernas cansadas. La combinación, no cada sesión
    por separado, es el estímulo.
  coaching: 'Come y duerme para absorber el B2B: ventana de 30min post-largo con CHO+proteína. Si la FC
    en reposo del lunes está +7, recorta calidad la semana que viene. 70g CHO/h en el largo.'
  sessions:
  - day: L
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: M
    type: EASY
    km: 11
    d: 0
    desc: 11km Z2. GYM Fase B.
  - day: X
    type: TEMPO
    km: 15
    d: 400
    desc: '15km: 3×12min Z3 cuesta sostenida + 2km Z1.'
  - day: J
    type: TRAIL
    km: 9
    d: 300
    desc: 9km Z2 trail.
  - day: V
    type: REST
    km: 0
    d: 0
    desc: Descanso o 4km recovery.
  - day: S
    type: LONG
    km: 22
    d: 900
    desc: 22km Z1–Z2 trail ~900m. 70g CHO/h.
  - day: D
    type: B2B
    km: 11
    d: 400
    desc: 11km Z2 trail con piernas cansadas (B2B real).
- week: 7
  phase: 2
  phase_name: Construcción específica
  load: HIGH
  title: Pico de volumen
  km: 72
  d_plus: 2400
  notes: Semana de mayor volumen del bloque. Si FC reposo +7 o mal sueño, recorta el domingo.
  objective: Semana de mayor volumen del bloque (72 km / 2400m). Intervalos Z4 en cuesta. Ensayo completo
    de carrera en el largo.
  context: Pico de volumen del macrociclo. Los 5×6min Z4 trabajan la potencia aeróbica que necesitas para
    sostener esfuerzo en rampas largas sin reventar. El largo de 26km con ensayo completo (geles + bebida,
    80g CHO/h) es el simulacro de gestión más exigente hasta el bloque de Palencia.
  key_session: S — 26km / 1100m con ensayo completo de carrera. Misma nutrición, mismo equipo, misma hora
    que usarás compitiendo.
  coaching: 'Esta es la semana más dura del volumen: si la FC en reposo sube +7 o el sueño se rompe, recorta
    el domingo. Después viene un deload (sem 8). Confía en la fatiga: es la que dispara la adaptación
    cuando descargues.'
  sessions:
  - day: L
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: M
    type: EASY
    km: 11
    d: 0
    desc: 11km Z2. GYM Fase B.
  - day: X
    type: INTERVAL
    km: 16
    d: 500
    desc: '16km: 5×6min Z4 en cuesta (3min rec) + 2km Z1.'
  - day: J
    type: TRAIL
    km: 11
    d: 400
    desc: 11km Z2 trail + pliometría.
  - day: V
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: S
    type: LONG
    km: 26
    d: 1100
    desc: 26km Z1–Z2 trail ~1100m. Ensayo completo de carrera (geles+bebida, 80g CHO/h).
  - day: D
    type: B2B
    km: 8
    d: 400
    desc: 8km Z2 trail B2B.
- week: 8
  phase: 2
  phase_name: Construcción específica
  load: LOW-MED
  title: DELOAD
  km: 52
  d_plus: 1200
  notes: Absorber la construcción antes de la semana pico de Palencia.
  objective: Deload para absorber el pico de volumen antes de la semana más vertical (Palencia sim).
  context: Segundo deload. Tras el pico de la semana 7, el cuerpo necesita 7-10 días de carga reducida
    para convertir el estímulo en forma. Este deload es lo que te permitirá afrontar la semana 9 (pico
    vertical) con calidad en lugar de arrastrando fatiga.
  key_session: S — Largo 18km a sensaciones, sin forzar. El objetivo de la semana es llegar fresco al
    gran bloque vertical de Palencia.
  coaching: 'GYM Fase B con cargas −10%. Sin calidad real, solo strides para mantener chispa. Si el cuerpo
    pide más descanso, dáselo: el deload bien hecho vale más que una sesión extra.'
  sessions:
  - day: L
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: M
    type: EASY
    km: 9
    d: 0
    desc: 9km Z2. GYM Fase B −10%.
  - day: X
    type: EASY
    km: 12
    d: 100
    desc: 12km Z2 + 6×20s strides.
  - day: J
    type: TRAIL
    km: 9
    d: 300
    desc: 9km Z2 trail.
  - day: V
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: S
    type: LONG
    km: 18
    d: 700
    desc: 18km Z1–Z2 ~700m.
  - day: D
    type: EASY
    km: 4
    d: 100
    desc: 4km Z1 recovery.
- week: 9
  phase: 3
  phase_name: Afinado Palencia
  load: HIGH
  title: Simulación Palencia (pico vertical)
  km: 66
  d_plus: 2800
  notes: Semana de mayor desnivel. Estímulo clave específico de Palencia.
  objective: Semana de mayor desnivel del bloque (2800m). Estímulo vertical específico de Palencia con
    el largo de montaña como simulacro.
  context: 'Palencia (44km/3500m) es más vertical que tu carrera A, así que la usamos como el mayor estímulo
    de subida del macrociclo. El largo de 26km/1800m es el ensayo directo de Palencia: chaleco, fueling
    completo, gestión de rampas. Giovanelli 2016: por encima del 15% de pendiente, el power-hiking con
    bastones es ~10% más eficiente que correr — practícalo aquí.'
  key_session: 'S — 26km de montaña ~1800m D+, vestido de carrera. Ensayo de Palencia: misma nutrición,
    mismo equipo, técnica de bajada para proteger cuádriceps.'
  coaching: 'Es la semana más exigente en D+. El domingo va con piernas cansadas a propósito (B2B). GYM
    Fase C (potencia, bajo volumen): explosividad, no carga. La bajada es tan importante como la subida
    — en Palencia hay 3500m de D-.'
  sessions:
  - day: L
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: M
    type: EASY
    km: 10
    d: 0
    desc: 10km Z2. GYM Fase C (potencia, bajo volumen).
  - day: X
    type: TEMPO
    km: 14
    d: 600
    desc: '14km: 40min Z3 sostenido en cuesta + técnica de bajada.'
  - day: J
    type: TRAIL
    km: 10
    d: 400
    desc: 10km Z2 trail.
  - day: V
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: S
    type: LONG
    km: 26
    d: 1800
    desc: 26km de montaña ~1800m D+. Chaleco + fueling completo. Ensayo Palencia.
  - day: D
    type: EASY
    km: 6
    d: 0
    desc: 6km Z1 recovery (piernas cansadas a propósito).
- week: 10
  phase: 3
  phase_name: Afinado Palencia
  load: MED
  title: Bajada de carga
  km: 50
  d_plus: 1400
  notes: Empieza a soltar fatiga; piernas progresivamente más vivas.
  objective: Empezar a soltar fatiga hacia Palencia manteniendo afilado. Última sesión real de fuerza.
  context: Semana de transición entre el pico vertical y el mini-taper de Palencia. Reducimos volumen
    y D+ pero mantenemos un toque de calidad para no perder chispa. A partir de aquí las piernas deben
    sentirse progresivamente más vivas.
  key_session: 'X — 3×8min Z3 en cuesta. Afilar, no vaciar: mantener la sensación de cambio de marcha
    sin generar fatiga residual.'
  coaching: Última sesión de GYM Fase C de verdad (lunes); luego solo mantenimiento. Empieza a priorizar
    el sueño de cara a la carrera. Si dudas entre hacer más o menos, haz menos.
  sessions:
  - day: L
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: M
    type: EASY
    km: 9
    d: 0
    desc: 9km Z2. GYM Fase C (última sesión de fuerza real).
  - day: X
    type: TEMPO
    km: 12
    d: 400
    desc: '12km: 3×8min Z3 en cuesta (afinar, no vaciar).'
  - day: J
    type: TRAIL
    km: 8
    d: 300
    desc: 8km Z2 trail.
  - day: V
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: S
    type: LONG
    km: 18
    d: 700
    desc: 18km Z1–Z2 ~700m.
  - day: D
    type: EASY
    km: 3
    d: 0
    desc: 3km Z1 recovery.
- week: 11
  phase: 3
  phase_name: Afinado Palencia
  load: RACE
  title: Mini-taper + PALENCIA
  km: 63
  d_plus: 3600
  notes: 'Sólo mini-taper: suficiente para rendir sin perder el bloque.'
  objective: Mini-taper de 4-5 días y correr Palencia (44km/3500m) como carrera de preparación dura —
    el mayor estímulo vertical, no un pico total.
  context: Palencia es tu carrera B y tu mayor bloque vertical, 4 semanas antes de TP60. Hacemos solo
    un mini-taper (no un taper completo) para llegar fresco a rendir sin perder el bloque de entrenamiento
    de cara a TP60. Es una carrera para correrla bien y aprender, no para dejarte entero.
  key_session: 'S (12 Sep) — PALENCIA 44km/3500m. Sal conservador: primeros 10km Z1-Z2 sin dejarte llevar
    por la adrenalina. Power-hike toda rampa >15%, gel cada 35-40min desde km10, baja con cabeza para
    proteger cuádriceps de cara a TP60.'
  coaching: 'El error clásico en montaña es salir rápido en la primera subida. Mejor llegar a mitad de
    carrera pensando ''podría ir más rápido''. Sin gym esta semana. Carga de carbohidratos 36-48h antes.
    Disfruta: el trabajo ya está hecho.'
  sessions:
  - day: L
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: M
    type: EASY
    km: 8
    d: 0
    desc: 8km Z2 + 4×20s strides (sin gym).
  - day: X
    type: EASY
    km: 6
    d: 100
    desc: 6km Z1 + 3×2min Z3 (aperturas).
  - day: J
    type: EASY
    km: 5
    d: 0
    desc: 5km Z1 muy suave + 4 strides.
  - day: V
    type: REST
    km: 0
    d: 0
    desc: Descanso. Viaje/prep, prepara material, carga de carbohidratos.
  - day: S
    type: RACE
    km: 44
    d: 3500
    desc: 🌄 PALENCIA — 44km / 3500m D+. Z2 en subidas / power-hike >15%, primera mitad controlada Z1–Z2,
      60–90g CHO/h, baja con cabeza para proteger cuádriceps de cara a TP60.
  - day: D
    type: REST
    km: 0
    d: 0
    desc: Descanso total o 20min caminando.
- week: 12
  phase: 4
  phase_name: Recuperar + puente TP60
  load: LOW
  title: Recuperación post-Palencia
  km: 30
  d_plus: 500
  notes: Prioriza recuperar tejido tras 3500m de bajada. Sin calidad hasta tener piernas limpias.
  objective: Recuperar el daño muscular de 3500m de bajada. Sin calidad hasta tener piernas limpias.
  context: '3500m de D- en Palencia generan microdaño muscular importante, sobre todo en cuádriceps (Burt
    2011). Esta semana prioriza la reparación: volumen muy bajo, nada de intensidad. Forzar aquí comprometería
    la última semana específica de TP60 (sem 13). La recuperación construye; el entrenamiento solo rompe.'
  key_session: 'S — 12km suave. No es entrenamiento, es evaluación: si los cuádriceps siguen doloridos,
    reduce y camina.'
  coaching: 'Evalúa cuádriceps el martes con un trote muy corto. GYM solo mantenimiento ligero el domingo.
    Crioterapia/masaje si tienes acceso. Paciencia: una semana perdida aquí vale menos que una lesión
    por volver pronto.'
  sessions:
  - day: L
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: M
    type: EASY
    km: 6
    d: 0
    desc: 6km Z1 muy suave (evalúa cuádriceps).
  - day: X
    type: REST
    km: 0
    d: 0
    desc: Descanso o 30min movilidad.
  - day: J
    type: EASY
    km: 8
    d: 100
    desc: 8km Z1–Z2 llano.
  - day: V
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: S
    type: LONG
    km: 12
    d: 400
    desc: 12km Z1–Z2 suave, poco D+.
  - day: D
    type: EASY
    km: 4
    d: 0
    desc: 4km Z1 + GYM mantenimiento ligero.
- week: 13
  phase: 4
  phase_name: Recuperar + puente TP60
  load: HIGH
  title: Pico específico TP60 (distancia)
  km: 60
  d_plus: 1600
  notes: Tirada más larga del bloque. Énfasis en distancia/tiempo en pie. Último estímulo grande antes
    del taper.
  objective: 'Último estímulo grande antes del taper: distancia y tiempo en pie específicos de TP60, menos
    vertical que Palencia.'
  context: 'TP60 (63km/2500m) es más largo pero menos vertical que Palencia, así que el énfasis cambia
    a distancia y tiempo en pie. El largo de 38km/~5h es la tirada más larga del macrociclo: si lo terminas
    cómodo en Z2, completar TP60 en 7-8h es realista. Tras esto, todo baja (taper).'
  key_session: 'S — 38km / ~5h en perfil tipo TP60. Sal a la misma hora que en TP60, con la misma nutrición
    y equipo. Objetivo: terminar en Z2 cómodo.'
  coaching: 'Ya con piernas limpias tras la recuperación, esta es la semana de confianza: demostrarte
    que aguantas la distancia. El tempo del miércoles es en terreno rolling, no en cuesta empinada — TP60
    es más rodador. GYM solo mantenimiento.'
  sessions:
  - day: L
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: M
    type: EASY
    km: 8
    d: 0
    desc: 8km Z2. GYM mantenimiento ligero.
  - day: X
    type: TEMPO
    km: 9
    d: 300
    desc: '9km: 2×15min Z3 en terreno rolling (TP60 es más llano que Palencia).'
  - day: J
    type: EASY
    km: 5
    d: 0
    desc: 5km Z2.
  - day: V
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: S
    type: LONG
    km: 38
    d: 1300
    desc: 38km / ~5h Z1–Z2, perfil tipo TP60. Ensayo completo de fueling y material.
  - day: D
    type: REST
    km: 0
    d: 0
    desc: Descanso o caminar suave.
- week: 14
  phase: 5
  phase_name: Taper TP60
  load: MED
  title: Taper 1
  km: 42
  d_plus: 900
  notes: Volumen −40% vs W13, se mantienen toques de intensidad (Mujika).
  objective: 'Primera semana de taper: −40% volumen vs sem 13 manteniendo toques de intensidad.'
  context: 'Mujika 2003: el taper óptimo reduce volumen ~40-60% en 2 semanas manteniendo algo de intensidad,
    lo que maximiza la forma sin perder afilado. Esta semana recortamos volumen pero conservamos un tempo
    corto para que el cuerpo siga ''recordando'' la velocidad. Empieza la fase de confiar en el trabajo
    hecho.'
  key_session: X — 3×6min Z3. Mantener chispa con muy poco coste de fatiga. Deberías sentirte reactivo
    y fresco.
  coaching: Última sesión de gym ligera el martes; después se acabó el gym hasta TP60. Prioriza sueño
    y comida de calidad. Es normal sentir piernas raras o 'demasiado descanso' en taper — es buena señal.
  sessions:
  - day: L
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: M
    type: EASY
    km: 8
    d: 0
    desc: 8km Z2 + 4×20s strides. Última sesión de gym ligera, luego stop.
  - day: X
    type: TEMPO
    km: 12
    d: 300
    desc: '12km: 3×6min Z3 (mantener chispa).'
  - day: J
    type: TRAIL
    km: 8
    d: 300
    desc: 8km Z2 trail.
  - day: V
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: S
    type: LONG
    km: 14
    d: 300
    desc: 14km Z1–Z2 ~300m.
  - day: D
    type: REST
    km: 0
    d: 0
    desc: Descanso.
- week: 15
  phase: 5
  phase_name: Taper TP60
  load: RACE
  title: Taper 2 + TP60
  km: 86
  d_plus: 2600
  notes: Llega fresco y confiado — el trabajo ya está hecho.
  objective: 'Segunda semana de taper y carrera A: TP60 (63km/2500m). Llegar fresco, sano y confiado.'
  context: 'Race week de TP60, tu objetivo A. Volumen mínimo, solo aperturas para activar sin fatigar.
    Todo el bloque de 15 semanas converge aquí. La estrategia gana ultras: salir conservador y gestionar,
    no salir rápido y sobrevivir.'
  key_session: 'D (11 Oct) — TP60 63km/2500m. Estrategia conservadora: primeros 20km en Z2 cómodo, power-hike
    >15%, 60-90g CHO/h desde el inicio, electrolitos, plan de bolsa de avituallamiento. Intención de negative
    split.'
  coaching: 'El error fatal en ultra es salir rápido los primeros 20km y morir tras el 40. Mejor llegar
    al km40 pensando ''podría ir más rápido''. Carga de carbohidratos 36-48h antes. Material y plan de
    avituallamientos listos el viernes. Confía: el trabajo está hecho.'
  sessions:
  - day: L
    type: REST
    km: 0
    d: 0
    desc: Descanso.
  - day: M
    type: EASY
    km: 8
    d: 0
    desc: 8km Z2 + 4×20s strides.
  - day: X
    type: EASY
    km: 6
    d: 100
    desc: 6km Z1 + 3×90s Z3 (aperturas).
  - day: J
    type: EASY
    km: 5
    d: 0
    desc: 5km Z1 muy suave.
  - day: V
    type: REST
    km: 0
    d: 0
    desc: Descanso. Carga de carbohidratos, material, plan de avituallamientos.
  - day: S
    type: EASY
    km: 4
    d: 0
    desc: 4km Z1 shakeout + 3 strides.
  - day: D
    type: RACE
    km: 63
    d: 2500
    desc: 🏁 TP60 — 63km / 2500m D+. Ritmo uniforme Z1–Z2, power-hike subidas, 60–90g CHO/h desde el inicio,
      electrolitos, estrategia de bolsa de avituallamiento. Intención de negative split.
```
