# Montaña Palentina: catálogo de rutas, datos verificados y huecos

**El dominio "Montaña Palentina" se puede construir hoy con un núcleo oficial sólido y una periferia amplia, ya cuantificada, que todavía hay que verificar sobre el terreno.** El documento reúne **182 fichas de ruta** (§16): **154 a pie** (6 de ellas fuera de Palencia o del ámbito, marcadas) y **28 de BTT y cicloturismo**. El núcleo son las **13 sendas del plano oficial 2025 de la Junta**: 9 PR/PRC-P homologadas y 4 "PR." sin número. Se completa con el **GR-1 (85,38 km oficiales en 6 etapas, +2.652 / −2.094 m)**, el **Camino Natural del Románico Palentino (~103 km, GPX del MAPA)**, el **Camino Olvidado**, el **Camino Lebaniego Castellano** y las **40 ascensiones de la guía de la Diputación**, que traen cifras MIDE para las 40 y waypoints completos para 16 ([Plano Junta 2025](https://patrimonionatural.org/ficheros/Parque%20Natural%20Monta%C3%B1a%20Palentina-%28sin%20senda%20Ruesga%29_compressed-20250621-104951.pdf); [Guía Diputación](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf)). La v2 añade **41 rutas a pie y 24 de BTT/cicloturismo** de Terranostrum y palenciaturismo, con **estadísticas propias de 127 ficheros GPX** (inicio, fin, distancia, D+ y altitudes, marcadas como "cálculo propio"). Las coordenadas de las cumbres son fiables porque salen de Mendikat, leído directamente, y coinciden con los waypoints de la guía. En cambio, **no hay ningún GPX oficial descargable en dominios de la Junta**: solo palenciaturismo ofrece dos GPX sueltos y el MAPA los del Camino Natural. Wikiloc no se ha leído (protección anti-bot, no se intentó saltar), así que sus descargas y comentarios solo se conocen por el buscador. Los refugios son todos libres, sin guarda: **Mazobre (~10 plazas) y los de pescadores del valle de Pineda siguen en uso**, el Golobar no es utilizable y el del club Espigüete desapareció en 2015. Ninguna fuente de agua tiene control sanitario y las crestas apenas tienen agua. La extracción de POI de OSM sigue sin hacerse porque la red bloquea Geofabrik y Overpass. Sí se pueden ingerir legalmente en la app el terreno (MDT02/MDT05 y PNOA del IGN, CC BY 4.0), los POI de OSM (ODbL) y los tracks propios. Los tracks y textos de Wikiloc, Mendikat, Komoot, Terranostrum y la guía de La Pedrera Pindia solo se pueden enlazar. Este documento es la referencia de trabajo. La lista concreta de lo que falta está en la sección final, **"Pendientes / lo que falta"**.

## Changelog v2 (2026-11-21)

- **Fuentes nuevas:** fichas de Terranostrum (115 revisadas; 127 ficheros GPX de 111 fichas analizados), fichas de rutas y lugares de palenciaturismo, el libro y el mapa "Montaña Palentina" 2026, refugioslibres.com (13 fichas), Wikipedia (datos reformulados), komoot (consejos de usuarios), Pyrenaica n.º 286 (Integral de Fuentes Carrionas) y la memoria invernal 2026 de un club. Notas de origen: `terranostrum_pedrera_libro2026.md`, `terranostrum_gpx_estadisticas.json` y `blogs_refugios_comentarios.md`.
- **Fichas:** de 117 a **182**. Nuevas: 41 a pie (§16.7) y 24 de BTT/cicloturismo (§16.8). 80 fichas existentes enriquecidas con coordenadas de inicio, cifras de contraste, GPX (cálculo propio) con discrepancias marcadas, itinerario por tramos, agua, refugios, avisos, comentarios y contexto de geología, glaciarismo, historia y toponimia.
- **Resuelto:** Senda de La Pedrosa (inicio, tipo y cifras); cifras oficiales del GR-1 por etapa (85,38 km); etapas del Camino Natural del Románico, Camino Olvidado E5–E7 y Lebaniego Castellano E6–E11; Fuente Cobre es circular; Las Tuerces Amarilla (8,3 km) y Azul (9,2 km) confirmadas, y las cinco rutas de colores son lineales; coordenada del Pozo de las Lomas; inicios de Ursi, Pinar de Velilla y Venganza del Conde; el "Gigante" del PR-P 7 es una leyenda, no un árbol; **Quejigar de Hérmedes está en el Cerrato y sale del dominio**.
- **Refugios (§4):** nuevas Cabaña de Mollorente y Refugio de Cristo Sierra; Mazobre ~10 plazas y en uso; Pescadores probablemente abierto; Santa Marina ~8 plazas; Golobar no utilizable; alud que destruyó el refugio del club Espigüete fechado (9–13-02-2015); candidato a Tenadas de Lores.
- **Avisos nuevos:** **Cueva de los Franceses cerrada por obras** (§12); no pisar el Pozo de las Lomas helado; error de orientación habitual en el Espigüete S; agua solo en Cardaño de Abajo para el Espigüete S.
- **Secciones actualizadas:** §1 (tablas maestras, GR-1, BTT), §2 (lagos y notas de altitud), §3, §4, §5, §6 (más de 50 trailheads nuevos y enclaves del libro 2026), §7, §12, §14, §15, Pendientes y Siguientes pasos. Leyenda ampliada con 🟨 periferia y "cálculo propio".
- **Sigue bloqueado:** OSM (Geofabrik y Overpass con *connection reset*), lapedrerapindia.com, Wikiloc, SummitPost y Guía Repsol, enlaces goo.gl del libro.

---

## Cómo leer este documento

**Leyenda de confianza**, aplicada a cada dato o fila:

| Marca | Significado |
|---|---|
| ✅ | Verificado en fuente oficial o primaria leída directamente: patrimonionatural.org (fichas, folletos con texto y plano 2025), BOCyL/BOE, PDF de la guía de la Diputación, AEMET, Mendikat (JSON de la página) |
| ⚠️ | Fuente secundaria (Terranostrum, Komoot, AllTrails, blogs o prensa), resumen de buscador, o fuentes oficiales que se contradicen |
| ❓ | Sin verificar: dato de memoria, URL construida o fuente que no se pudo abrir |
| 🟧 LEÓN / 🟦 CANTABRIA / 🟪 BURGOS | Elemento total o parcialmente **fuera de Palencia** |
| 🟨 PERIFERIA | En Palencia, pero al sur o al borde del ámbito de trabajo (Guardo sur, Fresno del Río, Ojeda, Herrera) |
| (cálculo propio) | Cifra calculada por nosotros a partir de un GPX de terceros (inicio/fin, distancia haversine, D+ con histéresis de 5 m, rango de altitud). Sirve de contraste, no es cifra oficial |

**Jerarquía de fuentes para las cifras canónicas de la app:**

1. Plano oficial 2025 de la Junta para las sendas del Parque Natural.
2. Ficha web y folleto de cada senda.
3. Guía de la Diputación (MIDE) para ascensiones.
4. Mendikat para coordenadas de cumbre.
5. Agregadores, solo como contraste.

Las fichas web y los folletos de 2010–2012 dan longitudes y desniveles algo distintos del plano: hasta **110 m de diferencia de D+ en la Senda del Oso** ([Plano 2025](https://patrimonionatural.org/ficheros/Parque%20Natural%20Monta%C3%B1a%20Palentina-%28sin%20senda%20Ruesga%29_compressed-20250621-104951.pdf)).

**Fichas y fuentes.** La sección 16 contiene una **ficha autocontenida por ruta**, con slug estable `mp-…`, pensada para que la app la ingiera directamente. Para aligerar las tablas, solo se dejan 1–2 enlaces por celda o ficha; todas las demás URLs están en el **Anexo: Fuentes** ("+N en Fuentes").

**Ámbito geográfico.** Parque Natural Montaña Palentina (10 municipios según el art. 3 de la Ley 4/2000) y sector palentino del Geoparque Las Loras. Bbox de trabajo: lat 42.75–43.05, lon −4.85 a −4.05. Fecha de consulta de todas las fuentes: 21-11-2026 (v1 y v2).

---

## 1. Catálogo maestro de rutas

### 1.1 Red oficial del Parque Natural: 13 sendas en el plano 2025, con códigos que no coinciden entre documentos

Hay 12 sendas con ficha y folleto en [patrimonionatural.org/senderos](https://patrimonionatural.org/senderos). El plano 2025 añade una 13.ª, la **Senda de La Pedrosa**, que no tiene ficha web. La red homologada por FDMESCYL (criterios FEDME) suma **63,8 km en 9 senderos**; la homologación se completó en 2019 con el PRC-P 9 y el PR-P 10 ([Montaña Palentina Hoy](https://www.montanapalentinahoy.com/2019/12/el-parque-natural-montana-palentina.html)) ⚠️.

Los códigos difieren entre fuentes:

- El Programa de Uso Público 2018 da Tosande como **PRC-P 03** y Fuente Cobre como **PRC-P 08** ([PUP 2018](https://patrimonionatural.org/ficheros/5b0be95e3407c_Parque-Natural-Montana-Palentina_Plan-Uso-Publico-vers_2018.pdf)).
- Turismo CyL usa otra numeración: Lomas "P3", Tosande "P4" y Mazobre "P9" ([Turismo CyL P9](https://www.turismocastillayleon.com/es/naturaleza/p9-senda-cascada-mazobre)).
- **Se adoptan los códigos del plano 2025.**

Ninguna ficha ofrece GPX, KML ni KMZ. Todas enlazan al perfil de Wikiloc de la Fundación (https://es.wikiloc.com/wikiloc/user.do?id=4448395) ❓, que no se pudo abrir.

Las coordenadas de inicio son las de la ficha oficial (sexagesimales WGS84 convertidas a decimal) ✅. Cifras de km, D+, tiempo y dificultad: **plano 2025** ✅. Si la ficha o el folleto dan otra cifra, va entre paréntesis.

| Código (plano 2025) | Senda | Zona / municipio | Inicio y coordenadas | Km | D+ (m) | Tiempo | Dific. | Tipo | Temporada / avisos | Enlaces |
|---|---|---|---|---|---|---|---|---|---|---|
| PRC-P 2 | Senda del escultor "Ursi" | Valle de Santullán, Barruelo / Brañosera | ✅ 42.89167, −4.30889. Aparcamiento Senda Ursi, Valle de Santullán (ruta 36 de la Diputación: 42.90353, −4.34705) ⚠️ | 11,6 (ficha 11) | 370 | 3 h 40 (ficha 4 h) | Media | Circular ⚠️ | 39 esculturas. Cierres por cacería el 21 y el 22-11-2026 ✅ | [ficha](https://patrimonionatural.org/senderos/senda-del-escultor-ursi) · [folleto 2025](https://patrimonionatural.org/ficheros/FOLLETO%20Senda%20del%20escultor%20Ursi-20250621-104214.pdf) ⚠️ (+2 en Fuentes) |
| PR-P 3 | Senda de la Tejeda de Tosande | Dehesa de Montejo / Cervera | ✅ 42.82611, −4.51528. Aparcamiento CL-626, a ~6 km de Cervera (42.8258, −4.5165 ⚠️ park4night/Mendikat). Solo de día; se llena | 10 (ficha 11) | 400 | 3 h 30 (ficha 3 h) | Media | Circular ⚠️ | ZULA 5. Tramo mirador–pasarela restringido del 1-oct a fin de febrero (PUP 2018) ✅. Cierres por caza el 12-12-2026 y el 28-02-2027 ✅. Pasarela en la tejeda. Mejor en otoño | [ficha](https://patrimonionatural.org/senderos/senda-de-la-tejeda-de-tosande) · [folleto](https://patrimonionatural.org/ficheros/folletosendatosandepdf240512_091402.pdf) ⚠️ (+5 en Fuentes) |
| PRC-P 4 | Senda del Roblón de Estalaya | Estalaya / Cervera | ✅ 42.925, −4.46944. Aparcamiento a ~2 km por la carretera que sale a la derecha tras el puente de Vañes | 4,6 (ficha 4,64) | 140 (folleto 125) | 1 h 30 | Baja | Circular ✅ | Obras de mantenimiento anunciadas en 2023 ❓ | [ficha](https://patrimonionatural.org/senderos/senda-del-roblon-de-estalaya) · [folleto](https://patrimonionatural.org/ficheros/El_Roblon.pdf) ❓ (+1 en Fuentes) |
| PRC-P 5 | Senda del Oso (Cervera–Arbejal) | Cervera de Pisuerga | ✅ 42.87306, −4.50139. Tres inicios: La Bárcena–Cervera, Arbejal y Mirador de las Matas | 12,2 (ficha 12) | 380 (ficha 270) | 4 h | Media | Circular: Cervera – Noria 0,7 – Arbejal 2,5 – embalse de Requejada 6,2 – chozo del Tremedal 8,5 – Cervera 12,2 ✅ | De mayo a otoño ✅. **Cierres intermitentes por obras desde el 4-6-2026 "hasta nuevo aviso"** ✅. El PDF del 20-11-2026 ya no los recoge: estado actual ⚠️ | [ficha](https://patrimonionatural.org/senderos/senda-del-oso) · [folleto](https://patrimonionatural.org/ficheros/folletosendadelosopdf130111_100115.pdf) ⚠️ (+2 en Fuentes) |
| PR-P 6 | Senda de la Cascada de Mazobre | Cardaños / Velilla del Río Carrión | ✅ 42.95167, −4.75889. Aparcamiento en el km 2,5 de la carretera Cardaño de Abajo–Cardaño de Arriba (Pino Llano). Pocas plazas | 6,6 i/v (ficha 7) | 270 (ficha 250) | 2 h | Baja (más en invierno) | Lineal hasta el mirador ✅ | Mejor en primavera, con el deshielo. Cierre por cacería el 21-11-2026 ✅ | [ficha](https://patrimonionatural.org/senderos/senda-de-la-cascada-de-mazobre) · [folleto](https://patrimonionatural.org/ficheros/sendamazobrepdf140111_131913.pdf) ⚠️ (+4 en Fuentes) |
| PR-P 7 | Senda del Gigante del Valle Estrecho | Santibáñez de Resoba / La Pernía–Cervera | ✅ 42.90639, −4.62639. Aparcamiento en el km 15,5 de la "Ruta de los Pantanos", pasado Santibáñez de Resoba | 4,4 (ficha 4) | 150 (folleto 113) | 1 h 15 (folleto 1 h 06, ficha 2 h) | Baja | Lineal ✅ | — | [ficha](https://patrimonionatural.org/senderos/senda-del-gigante-del-valle-estrecho) · [folleto](https://patrimonionatural.org/ficheros/5e7112e99cc33_Folleto-Senda-del-Gigante-del-Valle-Estrecho.pdf) |
| PR-P 8 | Senda de Fuente Cobre | Santa María de Redondo / La Pernía | ✅ 42.99139, −4.42667. Aparcamiento a la salida de Santa María de Redondo, tras el puente del arroyo Lombatero (palenciaturismo 42.99156, −4.42791) ✅ | 12,3 | 420 | 4 h 30 | Media | **Circular** ✅ (palenciaturismo 13 km; GPX cerrado, 11,6 km, cálculo propio) | Barro frecuente (ver §4). La ficha oficial no da cifras | [ficha](https://patrimonionatural.org/senderos/senda-de-fuente-cobre) · [folleto](https://patrimonionatural.org/ficheros/sendafuentecobrepdf240512_091321.pdf) ⚠️ (+7 en Fuentes) |
| PRC-P 9 | Senda del Bosque Fósil | Verdeña / Cervera | ✅ 42.94361, −4.45722. Aparcamiento junto a Verdeña | 3,5 (ficha 3) | 120 | 1 h | Baja | Circular, interpretativa ✅ | Apta para familias (inferencia) | [ficha](https://patrimonionatural.org/senderos/senda-del-bosque-fosil) · [folleto](https://patrimonionatural.org/ficheros/sendabosquefosilverdenapdf140111_131636.pdf) ⚠️ (+3 en Fuentes) |
| PR-P 10 | Senda de la Laguna de las Lomas | Cardaño de Arriba / Velilla | ✅ 42.97167, −4.75583. Aparcamiento de Cardaño de Arriba (Diputación: 42.97113, −4.75757, 1415 m) | 12,3 i/v (ficha 12) | 650 (ficha 640; Diputación 620) | 5 h | Media-alta (más en invierno) | Lineal ✅ | Laguna a ~2.080 m. Nieve en invierno | [ficha](https://patrimonionatural.org/senderos/senda-de-la-laguna-de-las-lomas) · [folleto](https://patrimonionatural.org/ficheros/Lago-Lomas.pdf) ⚠️ (+3 en Fuentes) |
| PR. (s/n) | Senda del Pinar autóctono de Velilla | Velilla del Río Carrión | ✅ 42.8575, −4.8175. Aparcamiento junto a la Ciudad del Brezo (Diputación: 42.85067, −4.83329) | 3,5 (ficha 4) | 180 (ficha 150) | 1 h 20 (ficha 2 h) | Baja | Circular en lazo ✅ | — | [ficha](https://patrimonionatural.org/senderos/senda-del-pinar-autoctono-de-velilla) · [folleto](https://patrimonionatural.org/ficheros/Pinar-Velilla.pdf) |
| PR. (s/n) | Senda de la Venganza del Conde | San Salvador de Cantamuda / La Pernía | ✅ Junto a la colegiata y el puente medieval de San Salvador de Cantamuda, 42.96686, −4.49547 (Terranostrum) ⚠️ | 7,2 | 300 | 2 h 20 | Baja | Circular, pista y senda ✅ | Todo el año. Nieve o hielo en el mirador de la Leyenda (cara N de Peña Tremaya) hasta comienzos de la primavera ✅. Cerrada por cacería el 7-3-2026 ✅ | [ficha](https://patrimonionatural.org/senderos/senda-de-la-venganza-del-conde) · [folleto 2024](https://patrimonionatural.org/ficheros/Senda%20de%20La%20Venganza%20del%20Conde%20-20241211-124505.pdf) |
| PR. (s/n) | Senda del Monte Mayor | Salcedillo / Brañosera | ✅ Tres inicios: Salcedillo 8,8 km / 280 m / 2 h 45; Aparcamiento de Grullos 14 km / 360 m / 4 h 15; Valberzoso 12,5 km / 340 m / 3 h 50 | 8,8 | 280 | 2 h 45 | Media-baja | Circular con 2 ramales ✅ | Todo el año. Mirador y aparcamiento de Grullos adjudicados por ~113.000 € ✅ | [ficha](https://patrimonionatural.org/senderos/senda-del-monte-mayor) · [folleto nov-2025](https://patrimonionatural.org/ficheros/Folleto%20Senda%20Monte%20Mayor-20251129-105354.pdf) (+1 en Fuentes) |
| PR. (s/n) | Senda de La Pedrosa | Barruelo de Santullán (barrio de San Pedro) → Brañosera (ermita de San Roque), junto al río Rubagón ✅ | ✅ 42.91139, −4.28831 (cartel en Barruelo, GPX Terranostrum). Palenciaturismo ubica el marcador en 42.93411, −4.30461 (Brañosera) ⚠️ | 5 (palenciaturismo 9 i/v; Terranostrum 7,2 i/v) | 150 | 1 h 30 (palenciaturismo 3 h 30 i/v) | Baja | Lineal, ida y vuelta ✅ | A pie o BTT. Raquetas en invierno. Coincide con el GR-1 E2 ✅ | [plano 2025](https://patrimonionatural.org/ficheros/Parque%20Natural%20Monta%C3%B1a%20Palentina-%28sin%20senda%20Ruesga%29_compressed-20250621-104951.pdf) · [Diputación senderismo](https://www.diputaciondepalencia.es/sitio/turismo/rutas-naturaleza/senderismo) (+1 en Fuentes) |
| (proyecto) | Sendero circular del embalse de Ruesga | Ruesga–Ventanilla / Cervera | Aparcamiento de Ruesga (cota 1031 m). Sin coordenadas | 10,82 | desnivel máx. 38 | — | Fácil | Circular ✅ | Proyecto FEDER (607.825 €, ficha del 25-07-2025). Incluye una pasarela de ~200 m sobre el agua, el mirador de La Roca y un pantalán de ~35 m. **Estado de obra a finales de 2026 desconocido**: el plano 2025 se rotula "sin senda Ruesga" | [Proyecto FEDER](https://patrimonionatural.org/proyectos/feder-sendero-embalse-de-ruesga) |

Notas sobre la red:

- El proyecto FTJ (2023, 1.050.000 €) describe la red con **11 PR y 1 GR, 6 miradores y 4 refugios**. Prevé restaurar 10 chozos. La red tiene la Q de Calidad desde 2007 y aforadores en 6 sendas desde 2008 ([Proyecto FTJ](https://patrimonionatural.org/proyectos/ftj-ampliacion-y-mejora-de-la-red-de-senderos-e-instalaciones-de-uso-publico-asociadas-en-parque-natural-montana-palentina)) ✅.
- Hay una licitación de mejora del uso público en Brañosera ([noticia](https://patrimonionatural.org/noticias/noticia/la-junta-ha-publicado-la-licitacion-para-la-mejora-del-uso-publico-en-el-termino-municipal-de-branosera)) ✅.
- En 2024 la ruta de Herreros estuvo cerrada por obras y falta de señalización ([PDF jul-2024](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural-20240705-101959.pdf)) ✅. Es una ruta que no figura en el plano 2025.
- **Senderos homologados municipales fuera del plano (v2):** Terranostrum publica el **PRC-P 12 Roblón del Monasterio** (Velilla, 11,8 km) y el **PRC-P 14 Valdelobos** (Fresno del Río 🟨, 11,8 km). No figuran en el plano de la Junta porque no son de la red del parque; falta confirmar su homologación en FDMESCYL ⚠️. Fichas `mp-roblon-monasterio` y `mp-valdelobos`.
- **Error en una nota de investigación:** una nota afirmaba que la "Senda del Oso" es solo la vía verde asturiana. Es falso para este dominio: el **PRC-P 5 Senda del Oso** es una senda oficial palentina ✅. La homónima asturiana (Proaza–Teverga) es otra ruta distinta ❓.

### 1.2 Largo recorrido: el GR-1 vertebra el parque de este a oeste en unos 85 km

**GR-1 Sendero Histórico, trayecto palentino.** Palenciaturismo publica ahora **cifras oficiales por etapa** ✅: **85,38 km, +2.652 / −2.094 m, dificultad moderada, "homologado: sí"**, de Salcedillo al Alto de la Cruz Armada ([GR-1 palenciaturismo](https://palenciaturismo.es/que-hacer/rutas/gr1)). El plano 2025 redondea a **87 km** ✅ y el GPX completo de Terranostrum da 85,2 km / ~2.380 m (cálculo propio). Entra desde Cantabria por Mata de Hoz (los primeros ~2,4 km son cántabros 🟦) y sale a León por el collado de la Cruz Armada (~1.621–1.632 m). Temporada recomendada: de marzo a principios de noviembre. Todo el itinerario admite BTT, con variantes señalizadas en los tramos de sendero, y hay que respetar las restricciones temporales por oso ✅. El libro-guía oficial ([PDF](https://patrimonionatural.org/ficheros/58dce5a62bd0a_Libro-GR1-en-PALENCIA.pdf)) y el folleto ([PDF](https://patrimonionatural.org/ficheros/5f1aa02ff066d_Folleto_gr-1.pdf)) siguen sin leer ❓. Turismo CyL da otras cifras para E2, E3 y E5 ([Turismo CyL](https://www.turismocastillayleon.com/douro/pt/espacos-naturais/parque-natural-da-serra-palentina)). Las coordenadas de palenciaturismo parecen centroides de pueblo ⚠️.

| Etapa | Tramo | Km oficial ✅ | D+ / D− oficial ✅ | Terranostrum ⚠️ | GPX (cálculo propio) | Inicio → fin (palenciaturismo) | Avisos | Fuente |
|---|---|---|---|---|---|---|---|---|
| E1 | Salcedillo (o Mata de Hoz 🟦) – Valberzoso – Alto de los Grullos – Brañosera | 8,0 | +430 / −200 | 8,1 km · 2 h 30 · media | 8,1 km · +319 · 1.058–1.375 m · inicio en el puente de Rojadillo 42.93557, −4.24144 | 42.94084, −4.27340 → 42.93680, −4.30836 | — | [Terranostrum E1](https://www.terranostrum.es/senderismo/gr-1-palencia-etapa-1-cantabria-branosera) · [palenciaturismo E1](https://palenciaturismo.es/que-hacer/etapas/etapa-1-gr1-salcedillo-branosera) |
| E2 | Brañosera – Barruelo – Mina del Calero – Herreruela – San Felices – Estalaya | 23,5 | +660 / −800 | 24,3 km · 7 h 30 · media | 24,3 km · +710 · máx. 1.619 m | 42.93680, −4.30836 → 42.92768, −4.47515 | **Cierre por cacería entre San Felices y Herreruela el 22-11-2026** ✅ | [Terranostrum E2](https://www.terranostrum.es/senderismo/palencia/montana-palentina/estalaya/gr1-palencia-etapa-2-branosera-estalaya) · [palenciaturismo E2](https://palenciaturismo.es/que-hacer/etapas/etapa-2-gr1-branosera-estalaya) |
| E3 | Estalaya – Vañes – Requejada – Arbejal – Cervera | 11,5 | +170 / −250 | 10,6 km · 3 h | 11,1 km · +139 · máx. 1.161 m | 42.92768, −4.47515 → 42.86689, −4.49929 | Comparte tramos con la Senda del Oso (obras intermitentes) | [Terranostrum E3](https://www.terranostrum.es/senderismo/palencia/montana-palentina/arbejal/gr1-palencia-etapa-3-estalaya-cervera-de-pisuerga) · [palenciaturismo E3](https://palenciaturismo.es/que-hacer/etapas/etapa-3-gr1-estalaya-cervera-pisuerga) |
| E4 | Cervera – Ruesga – Ventanilla – Rebanal de las Llantas – La Lastra – Triollo | 23,0 | +540 / −300 | 22,4 km · 6 h 40 · +574 / −275 | 22,35 km · +577 · máx. 1.432 m | 42.86689, −4.49929 → 42.92464, −4.68056 | Pasa por ZR2; pista Rabanal–Alto de la Varga permitida (PUP) ✅ | [Terranostrum E4](https://www.terranostrum.es/senderismo/palencia/montana-palentina/cervera-de-pisuerga/gr1-palencia-etapa-4-cervera-de-pisuerga-triollo) · [palenciaturismo E4](https://palenciaturismo.es/que-hacer/etapas/etapa-4-gr1-cervera-pisuerga-triollo) |
| E5 | Triollo – vega del Carrión – valle de Miranda – Camporredondo de Alba | 10,7 | +140 / −200 | 10,5 km · 3 h | 10,5 km · +153 · máx. 1.407 m | 42.92464, −4.68056 → 42.89521, −4.74651 | Última etapa íntegramente palentina | [Terranostrum E5](https://www.terranostrum.es/senderismo/palencia/montana-palentina/gr1-palencia-etapa-5-triollo-camporredondo-de-alba) · [palenciaturismo E5](https://palenciaturismo.es/que-hacer/etapas/etapa-5-gr1-triollo-camporredondo-alba) |
| E6 | Camporredondo – pradera de Valdegullas – collado de la Cruz Armada | — (no figura) | — | 9 km · 2 h 45 · +430 / −100 · media | 9,0 km · +486 · **máx. 1.621 m**; fin 42.92916, −4.81033 | 42.89521, −4.74651 → 42.93095, −4.80978 | Termina en el límite con León 🟧; recibe el ramal de Cardaño de Abajo | [Terranostrum E6](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camporredondo-de-alba/gr1-palencia-etapa-6-camporredondo-de-alba-cruz-armada) · [palenciaturismo E6](https://palenciaturismo.es/que-hacer/etapas/etapa-6-gr1-camporredondo-alba-alto-cruz-armada) |

**Otros itinerarios de largo recorrido:**

| Itinerario | Tramo palentino | Km / D+ | Tipo | Datos y GPX | Confianza |
|---|---|---|---|---|---|
| **Camino Olvidado** (Camino de Santiago del Norte por la Montaña) | E5 Olea 🟦 – Néstar – Grijera – Aguilar (en Palencia solo Néstar–Aguilar) | 24,3 km / +452 / 6 h, baja (GPX 24,6 km, cálculo propio) | Lineal, ciclable | [Terranostrum E5](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-olvidado-en-palencia-etapa-5) | ⚠️ |
| ″ | E6 Aguilar – Corvio – Matamorisca – Salinas – Barcenilla – Quintanaluengos – Ligüérzana – Vado – Cervera | 28,7 km / +427 / 7 h, baja | Lineal, ciclable | GPX en [Terranostrum E6](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-olvidado-en-palencia-etapa-6). El tramo lo usan también los peregrinos a Santo Toribio de Liébana 🟦 | ⚠️ |
| ″ | E7 Cervera – Cantoral – Cubillo de Castrejón – Traspeña – Santibáñez de la Peña – Las Heras – Villanueva de Arriba – Muñeca – Guardo | 39,3 km / +851 / 8–9 h, baja | Lineal, ciclable | [Terranostrum E7](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-olvidado-en-palencia-etapa-7) | ⚠️ |
| ″ | Rotulado en el plano oficial 2025 | — | — | [Plano 2025](https://patrimonionatural.org/ficheros/Parque%20Natural%20Monta%C3%B1a%20Palentina-%28sin%20senda%20Ruesga%29_compressed-20250621-104951.pdf) | ✅ |
| **Camino Natural del Románico Palentino** (MAPA) | Principal + ramales. Arranca de la etapa 2 de la Ruta del Carbón de Cok, cerca de Cozuelos de Ojeda. Cervera queda a 2 km de desvío del final de la etapa II | ~103 km (MAPA). Terranostrum, bajo el nombre "Ruta del Carbón de Cok": E1 Alar–Cozuelos 16,9 km · E2 Cozuelos–Vado 32,3 km · Variante 2 Cozuelos–Dehesa de Montejo 22,5 km · E3 Vado–Herreruela 21,2 km; GPX completo 131,6 km (cálculo propio, con variantes) | Lineal por etapas | [Guía MAPA](https://servicio.mapa.gob.es/ca/desarrollo-rural/temas/caminos-naturales/guia_cnromanicopalentinonipo_tcm34-636970.pdf) · [Etapa II](https://www.mapa.gob.es/en/desarrollo-rural/temas/caminos-naturales/caminos-naturales/sector-noroeste/romanico-palentino/etapa-ii/default.aspx) · [Etapa V](https://www.mapa.gob.es/en/desarrollo-rural/temas/caminos-naturales/caminos-naturales/sector-noroeste/romanico-palentino/etapa-v/default.aspx) · [Folleto](https://servicio.mapama.gob.es/es/desarrollo-rural/temas/caminos-naturales/romanicopalentinoes_tcm30-146891.pdf) · **GPX por etapa vía IDEE** ([metadatos](https://idee.es/csw-inspire-idee/static/api/records/spaignCNT)) | ✅ / ⚠️ cifras de etapa de Terranostrum (falta contrastar con el GPX del MAPA) |
| **Camino Natural de los Puertos de Pineda** | Accesos por Resoba y Vidrieros | — | Pista | Regulación y permisos de vehículos enlazados desde la [página del parque](https://patrimonionatural.org/espacios-naturales/parque-natural/parque-natural-montana-palentina) (documento no extraído). **Cierre por cacería el 22-11-2026** ✅ | ✅/❓ |
| **Camino Lebaniego Castellano** | E6 Alar – Perazancas 24,8 km · E7 Perazancas – Cervera 18,2 km · E8 Cervera – San Salvador de Cantamuda 18 km · E9 San Salvador – Camasobres 12,4 km · E10–11 Camasobres – Santo Toribio 🟦 41,4 km | ~73 km palentinos (E6–E9), todas de dificultad baja | Lineal | [Plano 2025](https://patrimonionatural.org/ficheros/Parque%20Natural%20Monta%C3%B1a%20Palentina-%28sin%20senda%20Ruesga%29_compressed-20250621-104951.pdf) · fichas y GPX en Terranostrum (información: Diputación de Palencia), ver `mp-cn-lebaniego` | ✅ existencia / ⚠️ cifras |
| **Camino Natural Lebaniego de Pineda** | Rotulado en el plano 2025 | ❓ | — | Sin ficha en Terranostrum ni en palenciaturismo | ✅ existencia / ❓ datos |

No se encontró en la zona ningún GR-85, ninguna vía verde ni una "Ruta de los Pantanos" homologada como sendero: la "Ruta de los Pantanos" es una ruta escénica de 81 km por carretera (palenciaturismo; ficha `mp-ruta-pantanos`) ✅. **Nuevo en v2:** la **Calzada de los Blendios (GR-73)** entra por el sur, de Herrera de Pisuerga 🟨 a Aguilar por Mave, en dos etapas de 21,3 y 11 km (Terranostrum; fichas `mp-blendios-e1` y `mp-blendios-e2`) ⚠️.

### 1.3 Guía de la Diputación: 40 ascensiones con MIDE, pero solo 16 completas en la versión gratuita

"Ascensiones en la Montaña Palentina. 40 rutas circulares de baja y media dificultad a más de 75 cumbres" (D. Villegas y V. Rioja, ©La Pedrera Pindia 2016, ISBN 978-84-608-9822-1). Datos generales:

- Más de 500 km y casi 40.000 m de D+. Todas las rutas tienen track GPS grabado por los autores.
- El PDF de 2024 es **idéntico byte a byte** al de 2016 ([PDF 2016](https://www.diputaciondepalencia.es/system/files/publicacion-pdf/20160817/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf)): no hay revisión de campo posterior a 2016.
- Las rutas van numeradas de oeste a este. Cada una tiene variante ida y vuelta (IV) y variante circular (C).
- En las rutas **01, 12, 29 y 33** se describe la subida por la vía difícil. Hay que invertirlas para hacer la vía fácil.
- El tiempo es el MIDE, no el del track. El MIDE se da como S-O-D-E (severidad, orientación, desplazamiento, esfuerzo).
- Todas están pensadas para el **periodo estival** con buen tiempo ([Guía p.4–6](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf)) ✅.

Las cifras salen de la tabla del anexo, PDF p.60 ✅. La **zona** se infiere de la ordenación oeste→este ⚠️. Inicio, coordenadas y QR (decodificado del mapa impreso) solo existen para las 16 rutas libres. Las URL de los QR apuntan a lapedrerapindia.com y **no se han comprobado** ❓: en la v2 el host respondió con *connection reset* en todos los intentos. Estas rutas no están balizadas: en la app deben ir como "ruta de montaña no señalizada".

| Nº | Ruta / cumbre | Zona (inferida ⚠️) | Inicio y coordenadas (WGS84) ✅ | IV km / D+ / t / MIDE | C km / D+ / t / MIDE | Dificultades señaladas | ¿Completa? · enlace |
|---|---|---|---|---|---|---|---|
| 01 | Espigüete (2451) | Fuentes Carrionas | Cardaño de Abajo, plaza, 1314 m · 42.92095, −4.76391 | 10,3 / 1249 / 5h10' / 3-3-4-3 | 11,3 / 1249 / 5h45' / 3-3-4-3 | Arista E: destrepes II+ y II, terreno aéreo. Bajada por la pedrera S, "muy estropeada" | Sí (p.9–11) · [QR](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Espiguete) |
| 02 | Alto de la Hoya de Martín Vaquero | Fuentes Carrionas | — | 11,14 / 771 / 4h40' / 3-3-3-3 | 12 / 1000 / 5h10' / 3-3-3-3 | — | No |
| 03 | Pico Murcia (2351) + La Cerezuela (2206) | Fuentes Carrionas | Cardaño de Arriba, aparcamiento del PR-P 10, 1415 m · 42.97113, −4.75757 | 12,32 / 936 / 5h / 3-3-3-3 | 12,5 / 1008 / 5h15' / 3-3-3-3 | Desvío "Pico Murcia. Senda no balizada". Arista SE | Sí (p.12–14) · [QR](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Pico-Murcia) |
| 04 | Peñas Malas | Fuentes Carrionas | — | 11,4 / 867 / 4h40' / 3-3-3-3 | 11,9 / 962 / 5h / 3-3-3-3 | — | No |
| 05 | Pico Las Cuartas | Fuentes Carrionas | Aparcamiento de Cardaño de Arriba (deducido de la ruta 06) ⚠️ | 15,74 / 1042 / 6h10' / 3-3-3-4 | 15,4 / 1227 / 6h30' / 3-3-3-4 | — | No |
| 06 | Peña del Infierno (2537, techo de Palencia) | Fuentes Carrionas 🟦 (límite) | Cardaño de Arriba, aparcamiento, 1415 m · 42.97077, −4.75754 | 17,98 / 1222 / 7h / 3-3-3-4 | 24,2 / 1787 / 9h45' / 3-3-3-4 | Larga. Vuelta por la laguna de Fuentes Carrionas y el Collado del Ves; vadeo de arroyo | Sí (p.15–18) · [QR](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/peña-del-infierno) |
| 07 | Alto del Calderón | Fuentes Carrionas | — | 12,2 / 860 / 4h40' / 2-3-3-3 | 15,4 / 1215 / 6h20' / 3-3-3-3 | — | No |
| 08 | Curruquilla | Fuentes Carrionas | — | 18,56 / 1001 / 6h45' / 3-3-3-4 | 16,4 / 1411 / 7h / 3-3-3-4 | — | No |
| 09 | Peña del Tejo (1998) + Coto Blanco (2004) | Fuentes Carrionas | Puente Agudín, 1298 m · 42.92981, −4.75844 | 7,28 / 700 / 3h20' / 3-3-3-3 | 10 / 828 / 4h20' / 3-3-3-3 | — | Sí (p.19–21) · [QR](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/la-peña-del-tejo) |
| 10 | Peña María | Fuentes Carrionas | — | 17,6 / 680 / 5h40' / 2-3-3-3 | 13,1 / 780 / 4h50' / 3-3-3-3 | — | No |
| 11 | Canchas de Ojeda | Fuentes Carrionas | — | 16,6 / 893 / 5h / 2-3-3-3 | 16,3 / 1015 / 5h / 2-3-3-3 | — | No |
| 12 | Curavacas (2524) | Fuentes Carrionas | Vidrieros, plaza, 1325 m · 42.94238, −4.66465 | 12,28 / 1600 / 6h30' / 3-3-5-4 | 11,1 / 1400 / 5h45' / 3-3-5-3 | Subida descrita por la vía difícil: trepadas, Brecha Muerta, "terrazas de hierba muy expuestas". Vía normal = Horcada del Callejo Grande | Sí (p.22–25) · [QR](http://www.lapedrerapindia.com/rutas-montana-palentina/ascensiones/curavacas) |
| 13 | Monte de Las Huelgas | Fuentes Carrionas | — | 10,2 / 914 / 3h / 2-3-2-3 | 10,6 / 1063 / 3h30' / 3-3-4-3 | — | No |
| 14 | Santa Lucía (1854) + Peña Escrita (1762) | Resoba (transición a La Peña) | Santibáñez de Resoba, explanada de la iglesia de San Cristóbal, 1207 m · 42.90640, −4.60950 | 10,8 / 650 / 4h / 2-3-2-2 | 10 / 880 / 4h30' / 3-4-5-3 | Circular: arista con pasos de III; barranco con destrepes III+, "impracticable y muy difícil con agua". Peña Escrita tuvo restricción por osos en 2022 | Sí (p.26–27) · [QR](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Santa-lucia) |
| 15 | Peña Lampa | Velilla 🟧 (límite) | — | 5,92 / 652 / 2h50' / 3-3-3-3 | 9,7 / 686 / 3h50' / 3-3-3-3 | — | No |
| 16 | Peñas Mayores: P. Mayor de Velilla (1869) y P. Mayor de Guardo (1835) | Sierra del Brezo | Ciudad del Brezo, aparcamiento de la Senda del Pinar, 1159 m · 42.85067, −4.83329 | 5,66 / 710 / 3h30' / 3-3-3-3 | 9,2 / 878 / 4h30' / 3-3-3-3 | Paso tallado en la roca. "Vaguada cerrada por vegetación" en el WP14 | Sí (p.28–30) · [QR](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peñas-Mayores) |
| 17 | La Tuda | Sierra del Brezo / La Peña | — | 12,4 / 706 / 3h55' / 2-3-3-3 | 13,2 / 834 / 5h / 2-3-3-3 | — | No |
| 18 | Peña del Fraile (2001) + Peña Grande (1833) + Peña Cueto (1951) | Sierra del Brezo | Santibáñez de la Peña, 1108 m · 42.81049, −4.72966 | 12,1 / 896 / 4h30' / 3-3-3-3 | 11,9 / 1070 / 5h / 3-3-3-3 | Cueva de la Virgen opcional, por un recorrido "escarpado y aéreo" | Sí (p.31–33) · [QR](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-del-Fraile) |
| 19 | Peña Blanca | La Peña | — | 7,86 / 553 / 3h10' / 3-3-3-2 | 11,8 / 729 / 4h25' / 3-3-3-3 | — | No |
| 20 | Pico Traslosvocines | La Peña | — | 5,68 / 296 / 2h / 2-2-2-2 | 11,7 / 583 / 4h15' / 2-3-2-2 | — | No |
| 21 | Sierra Canales | La Peña | — | 15 / 634 / 4h30' / 2-3-3-3 | 16,6 / 827 / 5h30' / 2-3-3-3 | — | No |
| 22 | Pico Rebanal | La Peña | — | 16 / 780 / 5h30' / 2-3-3-3 | 13,7 / 834 / 5h / 3-3-3-3 | — | No |
| 23 | Peña Redonda (1996) + Castros del Mediodía (1874) + Peña Urtejas (1771) | La Peña (Sierra del Brezo) | Villanueva de la Peña, 1177 m · 42.82929, −4.62401 | 10,4 / 819 / 4h20' / 3-3-3-3 | 11,6 / 940 / 4h40' / 3-3-4-3 | Circular con una "aérea horcada y algún destrepe por terreno expuesto" | Sí (p.34–36) · [QR](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-Redonda) |
| 24 | Pico Las Cruces (1566) + Pico Almonga (1519) | La Peña / Tosande | Aparcamiento de Tosande, 1152 m · 42.82578, −4.51656 | 11,6 / 590 / 4h / 2-3-3-3 | 13,2 / 921 / 5h / 2-3-3-3 | Pasa por la Tejeda de Tosande (aplican sus restricciones) | Sí (p.37–39) · [QR](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Pico-Las-Cruces) |
| 25 | Pico de la Celada | La Pernía | — | 10,6 / 642 / 4h / 3-3-3-3 | 14,2 / 710 / 5h / 3-3-3-3 | — | No |
| 26 | Peña Carazo (2012) + Horca de Lores (2021) | La Pernía | Abadía de Lebanza, 1361 m · 42.96297, −4.55346 | 9,5 / 650 / 3h30' / 2-3-3-3 | 15 / 980 / 5h30' / 3-4-3-3 | Brecha rocosa | Sí (p.40–42) · [QR](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-Carazo) |
| 27 | Pico Lezna | La Pernía | — (desde el valle del arroyo Arauz ⚠️) | 21,7 / 1310 / 6h / 3-3-3-4 | 23,4 / 1310 / 6h45' / 3-3-3-4 | — | No |
| 28 | Bistruey | La Pernía 🟦 (límite) | — | 20 / 850 / 7h / 2-3-3-4 | 21,7 / 1180 / 8h / 3-4-3-4 | — | No |
| 29 | Peña Labra (2029) | Peña Labra 🟦 (límite) | Mirador de Piedrasluengas, 1354 m · 43.04156, −4.45860 | 7,8 / 830 / 3h30' / 3-3-5-3 | 8,9 / 818 / 4h / 3-3-5-3 | Subida descrita por el "Callejón": resaltes III, III+ y II+. Vía normal de bajada | Sí (p.43–44) · [QR](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-Labra) |
| 30 | Peña Abismo | La Pernía | — | 9,8 / 510 / 3h30' / 3-3-3-3 | 12,8 / 827 / 5h / 3-4-3-3 | ZR6 Peña del Abismo, sin limitaciones (PUP) | No |
| 31 | Pico Tres Mares (2171) + Cuchillón (2174) | Alto Pisuerga 🟦 (cumbre en el límite) | Aparcamiento exterior de una mina abandonada, 1260 m ("Aparcamiento de la Cueva del Cobre", valle de Los Redondos). **Coordenadas erróneas en el PDF** | 13,2 / 1000 / 4h / 3-3-3-3 | 15 / 1200 / 6h / 3-4-3-3 | "Aérea travesía de la cara norte", "en invierno es muy expuesto". Pistas de esquí de Alto Campoo 🟦 | Sí (p.45–48) · [QR](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Pico-Tres-Mares) |
| 32 | Cotomañinos | La Braña | — | 18,8 / 1094 / 7h / 3-3-3-3 | 15,2 / 1150 / 6h15' / 3-3-3-3 | — | No |
| 33 | La Verdiana | La Braña | — | 10,4 / 1040 / 5h / 3-3-5-3 | 10,8 / 874 / 4h30' / 3-3-5-3 | Subida descrita por la vía difícil (MIDE D 5) | No |
| 34 | Peña Tejedo | La Braña | — | 12,4 / 690 / 4h30' / 2-3-3-3 | 11,2 / 745 / 4h30' / 2-4-4-3 | — | No |
| 35 | Cueto de Comunales | La Braña | — | 14,4 / 900 / 5h15' / 2-3-2-3 | 14,3 / 965 / 5h30' / 2-4-3-3 | — | No |
| 36 | Peña Cildá (1616) + Cueto Morales (1662) | La Braña (Santullán) | Valle de Santullán, aparcamiento Senda Ursi, 1244 m · 42.90353, −4.34705 | 7,84 / 372 / 2h45' / 2-3-3-2 | 21,4 / 868 / 7h10' / 2-3-3-4 | Escombreras de las minas McKinley. Comparte PRC-P 2 y GR-1 | Sí (p.49–51) · [QR](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-Cilda) |
| 37 | Valdecebollas (2142) | La Braña / Sierra de Híjar | Brañosera, 1226 m · 42.93663, −4.30992 | 15,18 / 916 / 5h45' / 2-3-3-3 | 16,8 / 1026 / 6h20' / 3-3-3-4 | Ruinas del Refugio de Golobar | Sí (p.52–54) · [QR](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Valdecebollas) |
| 38 | Peña Rubia | La Lora | — | 8,4 / 690 / 3h30' / 2-3-3-2 | 11,5 / 780 / 4h30' / 3-3-3-3 | — | No |
| 39 | Sierra Corisa | La Lora | — | 11,8 / 470 / 4h / 2-3-3-3 | 19,3 / 1038 / 7h / 2-3-3-4 | ZULA 4 Sierra de Corisa | No |
| 40 | Peña Mesa (1071) + Pico Castillo (1100) | La Lora / Las Tuerces | Villaescusa de las Torres, aparcamiento tras el puente del Pisuerga, 883 m · 42.75961, −4.25488 | 3 / 190 / 1h15' / 2-2-3-1 | 13,8 / 535 / 4h30' / 2-3-3-3 | **La cima de Peña Mesa exige escalar 10 m (IV)**. Tramo pinar-vaguada sin sendero | Sí (p.55–57) · [QR](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-Mesa) |

**Fichero `waypoints_guia_diputacion.json`** (en la carpeta de notas):

- Contiene **318 waypoints de las 16 rutas completas**. El encargo hablaba de "~330", pero el recuento real es 318.
- Cada waypoint lleva nombre, km acumulado, altitud, UTM ETRS89 30T, lat/lon WGS84 (convertidas con pyproj EPSG:25830→4326) y página del PDF.
- **Hay que excluir 25 waypoints erróneos**: los 23 de la **ruta 31**, el **WP7 de la ruta 06** y el **WP25 de la ruta 36**. En el JSON **no están vacíos**: llevan convertidas las coordenadas del aparcamiento de la ruta 16 (42.85067, −4.83329, Ciudad del Brezo), así que hay que filtrarlos de forma explícita. El criterio más simple es descartar los UTM "30T 350208 4745862" y "30T 350191 4745740" fuera de la ruta 16.
- La ruta 06 empieza a numerar en el WP5, porque los WP1–4 son los de la ruta 05.
- Quedan **293 waypoints utilizables** ✅. Los nombres y las altitudes de la ruta 31 parecen correctos.

### 1.4 Rutas de cumbre: tres itinerarios concentran la demanda

Por número de tracks y descargas, las rutas estrella son el **Curavacas por el Callejo Grande desde Vidrieros**, el **Espigüete por la cara sur desde Cardaño de Abajo** y **Peña Prieta / Infierno / Tres Provincias desde Cardaño de Arriba por el Pozo de las Lomas**.

Los tracks de Mendikat con más descargas en la zona ✅:

| Track | Descargas |
|---|---|
| Peña Prieta por el Pozo Lomas | 4.922 |
| Peña Mayor – Fraile | 2.459 |
| Piedrasluengas – Peñalabra – Tres Mares | 2.450 |
| Curavacas desde Vidrieros | 2.300 |
| Valdecebollas desde Brañosera | 2.192 |

En la tabla siguiente, las cifras [M] están verificadas en Mendikat ✅. Las [W] son resúmenes de buscador de Wikiloc ⚠️. Las de terceros, ⚠️.

| Ruta | Zona | Salida (coord.) | Km / D+ | Tiempo | Dificultad | Tipo | Temporada | Tracks / enlaces |
|---|---|---|---|---|---|---|---|---|
| **Curavacas, vía normal S (Callejo Grande)** | Fuentes Carrionas | Vidrieros 42.9425, −4.6642 (GeoNames + Mendikat, ±200 m) ✅ | [M] 12,5 / 1364 circular · [M] 9,5 / 1170 i/v · HikingIberia 11,0 / 1200 i/v ⚠️ | ~6–8 h | "Alta (9/15)"; solo experimentados y sin nieve ⚠️. Diputación MIDE 3-3-5-4 (vía difícil) ✅ | Circular o i/v | Verano sin nieve | [M 17352](https://www.mendikat.net/track/curavacas-vidrieros-curavacas-hospital-vidrieros/17352) · [M 14197](https://www.mendikat.net/track/curavacas-vidrieros-curavacas-por-el-callejo-grande/14197) (+9 en Fuentes) |
| Curavacas, Canal Sur (invernal) | Fuentes Carrionas | Vidrieros | [W] 9,42 km | — | II/1; canal de 400 m a ~38° con tramos de 60°; "solo expertos" ⚠️ | Alpinismo | Invierno-primavera | [W 99549660](https://es.wikiloc.com/rutas-alpinismo/canal-sur-del-curavacas-desde-vidrieros-99549660) · [W 68926959](https://es.wikiloc.com/rutas-alpinismo/invernal-al-curavacas-por-canal-sur-directo-y-vuelta-por-callejo-grande-68926959) (+5 en Fuentes) |
| **Espigüete, cara sur (pedrera)** | Fuentes Carrionas | Cardaño de Abajo ~42.921, −4.764 (Mendikat; Diputación 42.92095, −4.76391 ✅) | [M] 11,2 / 1183 · Terranostrum 12,2 / 1050 ⚠️ · SummitPost ~1150 ⚠️ | ~5 h 45 | Alta. Más de 400 m de D+ en menos de 1 km de pedrera ⚠️ | i/v | Verano | [M 6152](https://www.mendikat.net/track/espiguete-cardano-de-abajo-pista-pedrera-cara-sur-espiguete-inicio/6152) · [W 11896919](https://www.wikiloc.com/hiking-trails/espiguete-cara-sur-11896919) (+4 en Fuentes) |
| Espigüete, arista E / cara N | Fuentes Carrionas | Parking de Pino Llano / Mazobre (~42.95, −4.762, baja precisión) ⚠️ | [M] 10,2 / 1128 · Terranostrum 9,2 / 1050 | 6 h | Cresta E PD inf.; arista O con paso de II | Circular | Verano (canales N en invierno = alpinismo) | [M 25741](https://www.mendikat.net/track/espiguete-parking-cascada-mazobre-cresta-e-pd-inf-espiguete-canales-norte-f/25741) · [W 29960126](https://www.wikiloc.com/hiking-trails/espiguete-2-451-m-subida-por-arista-este-y-bajada-por-canal-de-la-cara-norte-cascada-de-mazobre-29960126) (+6 en Fuentes) |
| **Peña Prieta / Infierno / Tres Provincias** 🟦🟧 | Fuentes Carrionas | Cardaño de Arriba ~42.970, −4.756 ✅ | [M] 8,4 / 1440 (Pozo Lomas) · [M] 20,5 / 1427 circular · [M] 19,3 / 1282 (Tío Celestino) · [W] ~18 / ~1150–1200 (Canal de Agujas) | 7–10 h | Alta; "sencilla sin pasos técnicos, pero larga" (usuario) ⚠️ | i/v o circular | Verano | [M 2698](https://www.mendikat.net/track/pena-prieta-cardano-de-arriba-pozo-lomas-pena/2698) · [M 8280](https://www.mendikat.net/track/pena-prieta-cardano-de-arriba-tres-provincias-pena/8280) (+11 en Fuentes) |
| Peña Prieta desde Llánaves de la Reina 🟧 | Vadinia (León) | Llánaves (León) | [W] ~21,7 km / ~1250 | — | Difícil | — | Verano | [W 28662748](https://www.wikiloc.com/hiking-trails/llanaves-de-la-reina-pena-prieta-tres-provincias-pico-del-infierno-28662748) · [Turismo CyL](https://www.turismocastillayleon.com/es/rural-naturaleza/rutas-naturaleza/pena-prieta-llanaves-reina) |
| Peña Prieta desde San Glorio 🟧🟦 | Puerto de San Glorio (fuera del bbox) | — | — | Travesía a Cardaño ~7 h 45 | — | Lineal | Verano | [W 51964148](https://es.wikiloc.com/rutas-senderismo/pena-prieta-desde-san-glorio-51964148) · [W 84958242](https://es.wikiloc.com/rutas-senderismo/pena-prieta-san-glorio-cubil-de-can-tres-provincias-pena-prieta-pico-del-infierno-san-glorio-cantab-84958242) (+1 en Fuentes) |
| Cordal Lomas – Cuartas – Guadañas – Matas – Murcia + Peña Prieta | Fuentes Carrionas | Cardaño de Arriba | [W] ~24 km / ~2400 acumulado | — | Larga, "alguna ligera dificultad" | Circular | Verano | [W 11808759](https://www.wikiloc.com/mountaineering-trails/laguna-de-las-lomas-pena-prieta-pico-infierno-tres-provincias-cuartas-guadanas-matas-y-murcia-11808759) |
| Pico Murcia por Valcabe y Las Cerezuelas | Fuentes Carrionas | Cardaño de Arriba | [M] 15,4 / 1014 (16-07-2023) | — | — | Circular | Verano | [M 28231](https://www.mendikat.net/track/murcia-pico-cardano-de-arriba-pico-murcia-valcabe-las-cerezuelas-cardano-de-arriba-2023-07-16/28231) |
| **Integral de Fuentes Carrionas** (Curavacas – Agujas de Cardaño – Peña Prieta – Espigüete) | Fuentes Carrionas | Vidrieros → Cardaño de Abajo (~15 km por carretera entre ambos). Pyrenaica: Pino Llano → Vidrieros | ~33 km ⚠️ · **Pyrenaica 286: 35 km / +3.400 m / 14 h 30, PD+** ✅ | 1 día o 2–3 días | Muy exigente. Curavacas–collado del Ves con "terreno complicado"; escasez de agua | Lineal o circular; diseñada por Luis Alejos en 1981 | Verano | [W 1782833](https://www.wikiloc.com/hiking-trails/integral-fuentes-carrionas-circular-2-noches-1782833) · [W 141106061](https://www.wikiloc.com/trail-running-trails/recorrido-a-las-5-pozas-de-fuentes-carrionas-con-cima-en-pena-prieta-141106061) (+3 en Fuentes) |
| Pico Lezna (2208) | La Pernía / 🟦 desde Cucayo | Lores (Palencia) o Cucayo (Cantabria) | [M] 21,6 / 1550 (Cucayo) · [W] 21,43 / 1138 (Lores, ida) · Terranostrum desde Lores 21,6 i/v / 997 (GPX ida 10,8 / +1.071, cálculo propio) | ≥8 h | Difícil | Lineal o semicircular | Verano | [M 20006](https://www.mendikat.net/track/lezna-cucayo-pico-pumar-lezna-pena/20006) · [W 5376595](https://es.wikiloc.com/rutas-senderismo/lores-pico-lezna-2208-m-cucayo-5376595) (+2 en Fuentes) |
| **Valdecebollas** | Brañosera / Sierra de Híjar | Brañosera 42.9350, −4.3078 (AEMET) ✅ | [M] 16,9 / 1015 · [M] 18,9 / 1105 · [W] 16,78 / 977 · corta desde el Golobar [W] 6,23 / 394 | ~6 h (corta ~2 h) | Media; corta fácil | Circular | Verano; clásico de raquetas en invierno | [M 9607](https://www.mendikat.net/track/valdecebollas-valdecebollas-y-sestil-desde-branosera/9607) · [M 16481](https://www.mendikat.net/track/valdecebollas-branosera-sestil-alto-valdecebollas-cueto/16481) (+7 en Fuentes) |
| **Peña Labra + Tres Mares** 🟦 | La Pernía / límite Cantabria | Mirador de Piedrasluengas 43.0417, −4.4593 ✅ | [M] 13,1 / 1019 · [M] 15,3 / 998 (travesía a Sta. María de Redondo) | ~5 h | Media; la vía del Callejón tiene III+ | Circular o travesía | Verano | [M 9610](https://www.mendikat.net/track/penalabra-mirador-de-piedrasluengas-penalabra-tres-mares/9610) · [URL truncada](https://www.mendikat.net/track/penalabra-mirador-pidedrasluengas-penalabra-tres-mares-sta-maria-de-redondo-travesia-jon-hueso-) (+1 en Fuentes) |
| Tres Mares + Cuchillón desde Santa María de Redondo | Alto Pisuerga | Sta. María de Redondo ~42.988, −4.383 ⚠️ | [M] 18,8 / 1224 | — | — | Circular (incluye Fuente Cobre) | Verano | [M 14232](https://www.mendikat.net/track/tres-mares-santa-maria-de-redondo-pico-tres-mares-cuchillon-santa-maria-de/14232) |
| Pico Cordel 🟦 | Alto Campoo (Cantabria) | Brañavieja (Cantabria) | [W] ~5,1 km ida / ~469 | — | — | — | — | [W 3285945](https://www.wikiloc.com/hiking-trails/ascension-al-pico-cordel-2061-m-desde-branavieja-ida-3285945) · [W 76749509](https://www.wikiloc.com/hiking-trails/pico-cordel-76749509) (+1 en Fuentes) |
| **Peña Redonda** | Sierra del Brezo / La Peña | Traspeña ~42.819, −4.589 · Villanueva de la Peña 42.82929, −4.62401 ✅ · parking de Tosande | [M] 12,7 / 1011 (Traspeña) · [M] 10,1 / 1118 (Tosande) · [W] ~12 / ~904 (Burrián) · [W] ~15,7 / 1028 | ~5 h | Moderada; sendas poco marcadas por el barranco | Circular | Romería el 1.er domingo de agosto | [M 14227](https://www.mendikat.net/track/pena-redonda-traspena-pena-redonda-burrian-barranco-de-santa-eulalia-traspena/14227) · [M 2696](https://www.mendikat.net/track/pena-redonda-ascension-a-la-pena-redonda-por-el-valle/2696) (+4 en Fuentes) |
| **Pico / Peña del Fraile** | Sierra del Brezo | Cristo Sierra · Santuario del Brezo · Santibáñez de la Peña | [M] 7,9 / 572 (19-07-2025, el más reciente) · [M] 11,5 / 940 · Terranostrum desde Santibáñez 12 / 898 · Komoot 12,9 km | — | Media | Circular | Verano | [M 28948](https://www.mendikat.net/track/fraile-pena-del-cristo-sierra-pena-del-fraile-cueto-cristo-sierra/28948) · [URL truncada](https://www.mendikat.net/track/fraile-pena-del-santuario-del-brezo-pico-del-fraile-pena-cueto-cueto-herrera-santuar) (+2 en Fuentes) |
| Peñas Mayores / cordal Sierra del Brezo | Velilla / Guardo | Campos de la Peña · poblado de Compuerto · Ciudad del Brezo | [M] 18,9 / 1271 (con el Fraile) · [W] ~9,7 · [W] ~22,2 / ~1457 (cordal) | — | — | Circular | Verano | [M 14584](https://www.mendikat.net/track/mayor-pena-campos-de-la-pena-pena-mayor-pico-del-fraile-campos-de/14584) · [W 71294743](https://www.wikiloc.com/hiking-trails/pena-mayor-1-836-m-desde-poblado-de-compuerto-sierra-del-brezo-xi-71294743) (+1 en Fuentes) |
| **Peña Lampa** 🟧 (límite) | Velilla | Velilla (aparcar en la carretera de Besande) | [M] 9,9 / 748 · [W] 9,68 / 657 · [W] 15,5 circular | — | Moderada; cresta afilada | Circular | — | [M 16265](https://www.mendikat.net/track/pena-lampa-velilla-del-rio-carrion-monte-valdehaya/16265) · [W 14213545](https://es.wikiloc.com/rutas-senderismo/asc15-pena-lampa-14213545) (+4 en Fuentes) |
| Peña Tremaya | La Pernía | Tremaya · San Salvador de Cantamuda · Brañosera | [W] ~5 / ~269 · [W] 4,78 / 263 · [W] 8,88 circular · [M] 22,7 / 908 (travesía desde Brañosera) · Terranostrum 4,7 semicircular desde el puente de Tremaya 42.97937, −4.46532 (GPX 6,9 / +301, cálculo propio) | ~1 h 30 (corta) | Fácil | Circular / travesía | Todo el año | [W 108980041](https://www.wikiloc.com/hiking-trails/pena-tremaya-108980041) · [W 4596617](https://es.wikiloc.com/rutas-senderismo/pena-tremaya-montana-palentina-4596617) (+4 en Fuentes) |
| Monte Bernorio | La Lora / Valdivia | Villarén de Valdivia ~42.777, −4.185 (baja precisión) | [M] 8,1 / 242 i/v · Recorrepicos ~8 km / ~3 h | ~3 h | Fácil | i/v | Todo el año | [M 20178](https://www.mendikat.net/track/bernorio-villaren-de-valdibia-bernorio/20178) · [W 23841391](https://es.wikiloc.com/rutas-senderismo/vueltiviri-covalagua-y-monte-bernorio-27-3-18-23841391) (+2 en Fuentes) |
| Monte Cildá – Las Tuerces | La Lora | Mave / Olleros | [M] 10,0 / 373 (13-05-2023) | — | Fácil | Circular | Todo el año | [M 25561](https://www.mendikat.net/track/monte-cilda-monte-cilda-las-tuerces/25561) |
| Peña Amaya 🟪 (FUERA) | Burgos | Amaya | PRC-BU 200: 12 km / 400 / 3 h | — | — | — | — | [Terranostrum](https://www.terranostrum.es/senderismo/sendero-de-pena-amaya) · [Recorrepicos](https://www.recorrepicos.com/Rutas/Pena_Amaya.htm) (+2 en Fuentes) |
| Monte Coriscao (1.569) 🆕 | Alto Carrión | Camporredondo de Alba 42.89467, −4.74735 | Terranostrum 10 / 320 (GPX +440, cálculo propio) | 3 h 30 | Media | Circular | Todo el año | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/subida-al-monte-coriscao-fuentes-carrionas) ⚠️ |
| Cueva Dorada 🆕 | Alto Carrión | Camporredondo de Alba 42.89511, −4.74564 | 8 i/v / 325 | 3 h | Media | i/v | Todo el año | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cueva-dorada-fuentes-carrionas) ⚠️ |
| Collado del Pinar (Pinar de Velilla) 🆕 | Sierra del Brezo | Ciudad del Brezo 42.84860, −4.83557 | 10,7 / 400 (GPX +703, máx. 1.611 m) ⚠️ | 4 h | Media | Circular | Todo el año | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-collado-del-pinar-fuentes-carrionas) ⚠️ |
| El Pinar de Peña Mayor 🆕 | Sierra del Brezo | Poblado de Compuerto | 4 km (ida) · +400 al collado, +700 a Peña Mayor · sin GPX | 2 h 30 | Media | Lineal | — | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/el-pinar-de-pena-mayor) ⚠️ |
| El Sabinar de Peña Lampa 🆕 🟧 (límite) | Velilla | Velilla 42.84085, −4.85707 | 10,2 / 554 (GPX +688, máx. 1.803 m) | 3 h 30 | Media | Circular | Todo el año | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-el-sabinar-de-pena-lampa) ⚠️ |
| Picos Almonga y de las Cruces desde Cervera 🆕 | Cervera | Cruz Roja de Cervera (CL-627) 42.85709, −4.49949 | 9,5 i/v / 424 (GPX +634) ⚠️ | 3 h | Media-baja | i/v | Todo el año | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cervera-de-pisuerga-pico-de-las-cruces) ⚠️ |
| Golobar – Collado de Canaleja – Sel de la Fuente – Fuente Cobre 🆕 | Sierra de Híjar | Golobar 42.96718, −4.33678 (1.775 m) | 11,3 / 525 (GPX +862) ⚠️ | 5 h | Baja-media | Circular | Verano | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-golobar-valdecebollas-sel-de-la-fuente) ⚠️ |
| De Vidrieros a los pies del Curavacas 🆕 | Fuentes Carrionas | Vidrieros, plaza 42.94283, −4.66461 | 4,8 / 346 (GPX +393) · lineal | 1 h 20 | Baja | Lineal (aproximación) | Todo el año | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-vidrieros-pie-del-curavacas) ⚠️ |

Para fichas por cima, la guía alpina **"Hitos alpinos: Curavacas y Espigüete"** (T. Lagunilla, 2018, más de 100 vías, incluye corredores invernales) está en [PDF Diputación](https://www.diputaciondepalencia.es/system/files/2024-05/guia_de_curavacas_y_espiguete-interactivo.pdf) ✅. Hay además un índice de "dosmiles" en [A Esgalla](http://aesgalla.blogspot.com/2012/02/2000s-de-la-montana-palentina-indice.html) ⚠️.

### 1.5 Rutas de valle y naturaleza: tres o cuatro clásicas por zona, con cifras muy dispares entre fuentes

Las sendas oficiales (Mazobre, Lomas, Fuente Cobre, Bosque Fósil, Tosande, Roblón, Gigante y Velilla) están en §1.1. Esta tabla recoge las rutas no oficiales de la Junta. Las cifras conviene darlas como **rangos**.

| Ruta | Zona | Salida (coord.) | Km / D+ | Tiempo | Dific. | Tipo | Temporada / avisos | Enlaces |
|---|---|---|---|---|---|---|---|---|
| Senda de los Pescadores (Velilla) | 1 Alto Carrión | Centro de Interpretación de la Trucha ("paraje del Soto"), Velilla, 42.82599, −4.84857 ✅ | Palenciaturismo 6 km circular / +39 ✅; GPX 6,35 km (cálculo propio); 6–6,4 km, desnivel mínimo ⚠️. El folleto del Centro da 4,3 km (presa de Compuerto – c/ La Fragua) | 2–3 h | Fácil | Ida por una orilla y vuelta por la otra, hasta el "puente del ahorcado" | Posible nieve en invierno. Buena para familias y perros (inferencia) | [palenciaturismo](https://www.palenciaturismo.es/que-hacer/rutas/senda-pescadores) · [Terranostrum](https://www.terranostrum.es/senderismo/senda-de-los-pescadores-en-la-ribera-del-rio-carrion) (+5 en Fuentes) |
| Valle de Pineda desde Vidrieros | 1 | Vidrieros | [W] 12,63 / 108 | — | Fácil | Circular | En BTT, el camino es impracticable pasada la Vega de Cantos | [W 77588245](https://es.wikiloc.com/rutas-senderismo/vidrieros-rio-carrion-valle-de-pineda-77588245) · [W 7433651 MTB](https://www.wikiloc.com/mountain-biking-trails/pozo-curavacas-por-el-valle-de-pineda-7433651) |
| Pozo Curavacas por el valle de Pineda | 1 | Vidrieros 42.94177, −4.66229 | Terranostrum 19 km solo ida / +500 (GPX 18,98 / +487, cálculo propio) · [W] ~20,9 solo ida; ~37 i/v / ~490 | ~8 h | Difícil (por longitud) | Lineal, a pie o BTT | Cara N del Curavacas: restricciones por osos (§13) | [W 19631676](https://es.wikiloc.com/rutas-senderismo/vidrieros-pozo-curavacas-19631676) · [W 2778852](https://www.wikiloc.com/hiking-trails/vidrieros-pozo-curavacas-2778852) (+2 en Fuentes) |
| Circular de los lagos: Lomas, Fuentes Carrionas, Pozo Curavacas, Ves, Hoya Contina | 1 (alta montaña) | Cardaño de Arriba | Nemus: 16 km / 1.100 desde Vidrieros ⚠️ | — | Alta | Circular | No es un paseo | [W 175034497](https://es.wikiloc.com/rutas-senderismo/circular-cardano-de-arriba-pozo-de-las-lomas-laguna-de-fuentes-carrionas-pozo-del-curavacas-collado-175034497) · [W 82945106](https://www.wikiloc.com/mountaineering-trails/pozo-las-lomas-laguna-de-fuentes-carrionas-pozo-curavacas-pozos-del-ves-circular-montana-palentina-82945106) (+3 en Fuentes) |
| Mazobre circular con 2.ª cascada y refugio | 1 | Pino Llano | [W] 8,6 / 379 | <2 h (versión corta) | Fácil | Circular | Nieve en invierno | [W 177185185](https://es.wikiloc.com/rutas-senderismo/cascada-y-refugio-de-mazobre-177185185) |
| Triollo – La Lastra – Hornamiel | 2 / La Pernía | Puente del Carrión en Triollo 42.92303, −4.67943 ✅ | 9,7 / 284 (GPX +375, cálculo propio) | 2 h 45 | Baja | Circular, no ciclable | Zona de berrea | [Terranostrum](https://www.terranostrum.es/senderismo/sendero-triollo-hornamiel) ⚠️ |
| Desde la Abadía de Lebanza: Refugio de Linares – Hoyo de la Braguilla | 2 / La Pernía | Abadía de Lebanza 42.96297, −4.55346 ✅ | [W] 11,6 / ~446 | — | — | — | Sustituye a las "Cascadas de Lebanza", que no se encontraron como ruta | [W 147075263](https://www.wikiloc.com/hiking-trails/abadia-de-lebanza-refugio-de-linares-hoyo-de-la-braguilla-147075263) · [W 51590770 Carazo](https://es.wikiloc.com/rutas-senderismo/pena-carazo-y-horca-de-lores-desde-el-monasterio-de-sta-maria-de-lebanza-circular-51590770) |
| Embalse de Ruesga (paseo / berrea) | 2 | Ruesga | — | — | Fácil | — | Berrea del 15-sep al 15-oct | [siempredepaso](https://siempredepaso.es/disfruta-de-la-berrea-en-la-montana-palentina) · senda oficial en proyecto (§1.1) |
| Cascada de Covalagua (corta) | 3 Las Loras | Revilla de Pomar, junto a la iglesia 42.77071, −4.15124 ✅ | [Komoot] 5,79 / 140 · Terranostrum 5,2 / 90 (GPX 5,04 / +94) | 1 h 40 | Fácil | Circular, señalizada | Mejor en primavera y otoño; **puede ir casi seca en estiaje** | [Komoot](https://blog.komoot.nl/smarttour/e1068341662/cascada-de-covalagua-desde-revilla-de-pomar-paisaje-protegido-de-covalagua) · [Terranostrum](https://www.terranostrum.es/senderismo/sendero-cascada-de-covalagua) (+2 en Fuentes) |
| Integral de Covalagua | 3 | Revilla de Pomar | 19,7 / 270 ⚠️ (GPX +480, cálculo propio: **discrepancia**) · [M] 14,6 / 369 (Cueva de los Franceses – Valcabado – Covalagua) | 5 h | Media | Circular | Primavera y otoño | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/revilla-de-pomar/integral-espacio-natural-de-covalagua) · [M 12349](https://www.mendikat.net/track/valcabado-cueva-de-los-franceses-canto-hito-valcabado-covalagua-cueva-de-los-franceses/12349) (+2 en Fuentes) |
| Cueva de los Franceses – Mirador de Valcabado – Pozo de los Lobos | 3 | Junto a la Cueva de los Franceses 42.77212, −4.11582 ✅ | 6,2 i/v / 72 (antes 5,2 ⚠️) | 2 h | Baja | i/v, ciclable al 90 % | **Cueva cerrada temporalmente por obras** (21-11-2026) | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/revilla-de-pomar/1) |
| Hayedo de Monte Ahedo – Pozo de los Lobos – Mirador de Valcabado | 3 | Valcabado (Mendikat 42.78174, −4.10273). Pozo de los Lobos 42.77353, −4.09419 (Terranostrum) ✅ | Diputación 10 km / 225, media · [W] corta 3,51 / 151 · Komoot 16,1 / 360 | — | Fácil a media | Circular | Sin agua en el páramo | [Diputación](https://www.diputaciondepalencia.es/sitio/turismo/rutas-naturaleza/senderismo) · [W 24446341](https://es.wikiloc.com/rutas-senderismo/valcabado-hayedo-monte-aedo-pozo-de-los-lobos-valcabado-24446341) (+3 en Fuentes) |
| Revelillas – Pozo de los Lobos 🟦 | Valderredible (Cantabria) | Revelillas | 10,51 km | 4 h | Moderada | Circular; el tramo hasta el pozo no está balizado | — | [Valderredible](https://www.valderredible.es/rutas/revelillas-pozo-de-los-lobos) · [PDF](https://www.valderredible.es/uploads/editor/files/266/revelilla_-_pozo_de_los_lobos.pdf) (+1 en Fuentes) |
| **Las Tuerces, 5 rutas por colores** (balizadas por el Ayto. de Aguilar) | 3 | Mave / Aguilar / Gama | Roja 5,6 km / 2 h · Amarilla 8,3 km / 3 h 30 · Verde 7,3 km / 2 h (ciclable) · Rosa 6,9 km / 2 h · Azul 9,2 km / 3 h 30 ✅ (confirmadas en Terranostrum y en sus GPX) | — | Baja | **Las cinco son lineales**; cuatro terminan en Peña Mesa y la Azul en Gama | Todo el año. Llevar agua; borde del cañón y paso a nivel peligroso | [Terranostrum Tuerces](https://www.terranostrum.es/senderismo/monumento-natural-de-las-tuerces) · [Roja](https://www.terranostrum.es/senderismo/palencia/montana-palentina/las-tuerces-ruta-roja) (+5 en Fuentes) |
| Las Tuerces desde Aguilar | 3 | Aguilar de Campoo | [W] 12,33 / ~215 | — | Moderada | Circular | — | [W 133377939](https://es.wikiloc.com/rutas-senderismo/las-tuerces-desde-aguilar-de-campoo-133377939) |
| Geo-ruta del Anticlinal de Villaescusa de Ecla | 3 (Geoparque) | Santibáñez / Villaescusa de Ecla | Sin cifras ✅ | — | — | Señalizada con QR. Pasa por el castro cántabro y la cascada de La Cervigada (20 m, activa en lluvias) | — | [Geoparque](https://geoparquelasloras.es/anticlinal-de-villaescusa-de-ecla-geotrack-english-version/) |
| Entre Nestar y Cordovilla de Aguilar (ornitológica) | 3 (Geoparque) | Nestar | 6,1 km ✅ | 1,3 h | — | Circular; puente romano de Puente Perdiz | — | [Turismo CyL](https://www.turismocastillayleon.com/es/naturaleza/nestar-cordovilla-aguilar) |
| Río Pisuerga en Villaescusa de las Torres (ornitológica) | 3 (Geoparque) | Villaescusa de las Torres | 3,3 km ✅ | 1,3 h | — | Circular | — | [Turismo CyL](https://www.turismocastillayleon.com/es/naturaleza/rio-pisuerga-villaescusa-torres) |
| Brañosera – Senda de La Pedrosa / Valdecebollas | 3 | Barruelo / Brañosera | Brañosera–Valdecebollas ~17 km / 6 h ⚠️ | — | — | — | — | [tuscasasrurales](https://www.tuscasasrurales.com/blog/rutas-senderismo-palencia/) |
| Quejigar de Hérmedes 🟪 **FUERA** | Cerrato (Hérmedes de Cerrato, 41.82003, −4.17598) | Área recreativa del arroyo de San Juan | 2,9 km | 1 h | Fácil | Circuito ornitológico con GPX | **No es Montaña Palentina**: retirar del dominio ✅ | [palenciaturismo rutas naturales](https://www.palenciaturismo.es/que-hacer/rutas-naturales) |
| Las Tuerces, circular corta desde Villaescusa 🆕 | 3 | Parking de Villaescusa de las Torres 42.75741, −4.24754 | 5 / 200 | 2 h | Fácil | Circular (SL) | Requiere algo de orientación | [palenciaturismo](https://palenciaturismo.es/que-hacer/rutas/monumento-natural-tuerces) |
| La Escalera del Tiempo (Geoparque) 🆕 | 3 | Villaescusa de las Torres | 2 km, sin GPX | 1 h | Fácil | Geológica | — | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/la-escalera-del-tiempo) |
| Cardaño de Abajo – Collado de la Cruz Armada 🆕 | 1 | Plaza de Cardaño de Abajo 42.92073, −4.76413 | 12 / 437 (GPX +512) | 3 h 30 | Media-baja | Circular | Enlaza con el GR-1 E6 | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cardano-de-abajo-a-la-cruz-armada) |
| Arroyo de Mazobre y Sima del Anillo 🆕 | 1 | Puente Agudín 42.92980, −4.75852 | 13 / 549 (GPX) | 5 h | Media | Circular | Bajo la cara N del Espigüete | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/el-arroyo-de-manzobres-y-sima-del-anillo) |
| Proyecto Lobo: Camporredondo – Valsurbio 🆕 | 1 | Camporredondo 42.89507, −4.74557 | 11,3 / 469 (GPX) | 3 h | Media-baja | Circular | Evitar el invierno | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/de-camporredondo-de-alba-a-valsurbio) |
| Por el despoblado de Valsurbio 🆕 | 1 | Embalse de Compuerto (km 52) 42.85679, −4.80806 | 15,5 / 496 (GPX) | 5 h | Media | Lineal (fin en Camporredondo) | — | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/por-el-despoblado-de-valsurbio) |
| Sendero del Roblón del Monasterio (PRC-P 12) 🆕 | 1 / Velilla | Campo de tiro de Velilla 42.83371, −4.84872 | 11,8 / 310 (GPX +394) | 3 h 30 | Baja | Circular, señalizado | Homologación por confirmar | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-roblon-del-monasterio-prc-p-12) |
| Sendero de Valdelobos (PRC-P 14) 🆕 🟨 | Fresno del Río | Área recreativa 42.68089, −4.82386 | 11,8 / 78 | 2 h 45 | Baja | Circular | Periferia sur | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-de-valdelobos-prc-p-14) |
| Guardo, "Senderos de Leyenda" y rutas locales (7) 🆕 🟨 | Guardo | Guardo ≈ 42.790, −4.844 (Doncellas: Muñeca 42.79202, −4.80148) | 6,2–22 km / 147–396 (ver §16.7) | 1 h 30–6 h | Baja-media | Circulares | — | [palenciaturismo (Doncellas)](https://palenciaturismo.es/que-hacer/rutas/senda-doncellas-hoyal) |
| El Ribero Pintado 🆕 | 2 / La Pernía | Parking de Fuente Cobre 42.99148, −4.42837 | 6–6,2 / 107–157 (GPX +174) | 1 h 30 | Baja | i/v o circular | Sin señalizar; GPX oficial descargable | [palenciaturismo](https://palenciaturismo.es/que-hacer/rutas/ruta-ribero-pintado) |
| Bocarón de Casavegas / Ojo de Caloca 🆕 | 2 / La Pernía | Fuente de Casavegas 43.02222, −4.51268 | 8,4 i/v / 308 | 3 h 30 | Baja | i/v | — | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/bocaron-de-casavegas) |
| San Juan de Redondo – Corrala de Bismo 🆕 | 2 / La Pernía | Iglesia 42.98999, −4.44842 | 9,5 / 371 | 3 h | Baja | Circular | — | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-san-juan-de-redondo-corrala-de-bismo) |
| Polentinos – Abadía de Lebanza 🆕 | 2 / La Pernía | Plaza de Polentinos 42.93841, −4.52466 | 8,9 i/v / 211 (GPX +384) ⚠️ | 2 h 10 | Baja | i/v, ciclable | Zona de oso y lobo | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-polentinos-abadia-de-lebanza) |
| La Braña, Brañosera, Barruelo y Mudá (8 rutas) 🆕 | 3 / La Braña | Salcedillo, Valberzoso, Barruelo, San Cebrián de Mudá, Mudá (ver §16.7) | 5–19 km / 109–466 | 1 h 15–4 h 30 | Baja-media | Varias | — | [Terranostrum (Salcedillo)](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-salcedillo-rojadillo-y-branosera) |
| Valle del Pisuerga, Valdivia y Calzada de los Blendios (6 rutas) 🆕 | 3 / Las Loras | Ligüérzana, Cillamayor, Canduela, Menaza, Herrera 🟨, Mave (ver §16.7) | 6–21,3 km / 77–269 | 2–6 h | Baja | Varias | — | [Terranostrum (Ligüérzana)](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-ligueerzana-a-la-vega-de-quintanaluengos) |

**Fuera del ámbito**, para marcarlo así en la app: Orbaneja del Castillo, Sedano y el Cañón del Ebro (🟪 Burgos); la mayor parte de las geo-rutas del Geoparque (Valle Ciego, Fuentes del Odra y Camino de Vallejo y Monte, en 🟪 Burgos, [Fuentes del Odra](https://geoparquelasloras.es/las-fuentes-del-odra-geotrack/)); el centro del Geoparque en Villadiego (🟪); y el "Pozo de los Humos", que está en Las Arribes (Salamanca) ❓ de memoria.

**BTT y cicloturismo** (catálogo complementario):

- Guía Diputación "25 rutas circulares" (©La Pedrera Pindia 2016). Solo están libres las rutas 1, 3, 4, 7, 9, 13, 16, 18, 21 y 24 ([PDF](https://www.diputaciondepalencia.es/system/files/publicacion-pdf/20161221/guia_btt_cicloturismo.pdf)) ✅.
- "Pedaleando por el Románico Palentino": 59,7 km, dificultad alta ([PDF](https://palenciaturismo.es/system/files/2020-04/Pedaleando.pdf); [Terranostrum GPX](https://www.terranostrum.es/senderismo/palencia/montana-palentina/matalbaniega/ruta-btt-pedaleando-por-el-romanico-palentino)) ✅/⚠️.
- Itinerario ciclista del Geoparque Villaescusa – Aguilar por Las Tuerces y Recuevas, de 2025 ([Ecoticias](https://www.ecoticias.com/naturaleza/geoparque-loras-itinerario-ciclista)) ⚠️.
- BTT Las Tuerces – Covalagua ([Komoot](https://blog.komoot.de/smarttour/e1494750275/mountain-biking-through-las-tuerces-and-covalagua)) ⚠️.
- **Terranostrum (v2): 24 rutas BTT de la Montaña Palentina**, casi todas de la Agrupación Comarcal de Desarrollo Montaña Palentina y cuatro de Turismo CyL, todas con GPX ⚠️. Las cifras de km, D+, tiempo y dificultad son las de la ficha; la columna de GPX es cálculo propio. Recordar que la bici solo está permitida por pistas y caminos aptos para vehículos (PUP 6.2.6). Fichas breves en §16.8.

| Slug | Ruta | Km ficha / GPX | D+ ficha | Tiempo | Dific. | Salida (GPX) | GPX (cálculo propio) | Enlace |
|---|---|---|---|---|---|---|---|---|
| `mp-btt-pedaleando-romanico` | Pedaleando por el Románico Palentino (Diputación) | 59,7 / 56,15 | 1.069 | 3 h 30 | Alta | Aguilar 42.79632, −4.27297 | 56,15 km · +722 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-pedaleando-por-el-romanico-palentino) |
| `mp-btt-alto-muda` | Alto Valle de Mudá | 12,2 / 12,15 | 266 | 1 h 20 | Baja | San Cebrián de Mudá 42.89712, −4.38624 | 12,15 km · +200 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-alto-valle-de-muda) |
| `mp-btt-barruelo-cervera` | Barruelo – Cervera (Turismo CyL) | 29,3 / 30,57 | 153 | — | Media | Barruelo de Santullán 42.90167, −4.28789 | 30,57 km · +341 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-barruelo-de-santullan-cervera-de-pisuerga) |
| `mp-btt-cervera-triollo` | Cervera – Triollo (Turismo CyL) | 24,3 / 23,68 | 440 | — | Alta | Cervera de Pisuerga 42.86211, −4.4987 | 23,68 km · +548 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-cervera-de-pisuerga-triollo) |
| `mp-btt-carbon` | Del Carbón | 19 / 19,09 | 255 | 1 h 55 | Baja | Salinas de Pisuerga 42.8485, −4.37923 | 19,09 km · +150 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-del-carbon) |
| `mp-btt-robla` | El Ferrocarril de La Robla | 34 / 33,96 | 669 | 3 h 30 | Alta | Las Heras de la Peña 42.80015, −4.73802 | 33,96 km · +411 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-el-ferrocarril-de-la-robla) |
| `mp-btt-gotico-pena` | Gótico y Románico en La Peña | 17,5 / 17,57 | 156 | 1 h 40 | Baja | Castrejón de la Peña 42.80801, −4.5989 | 17,57 km · +111 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-gotico-y-romanico-en-la-pena) |
| `mp-btt-guardo-almuhey` | Guardo – Puente Almuhey (Turismo CyL) 🟧 | 21,3 / 21,39 | 230 | — | Media-alta | Guardo 42.79768, −4.84809 | 21,39 km · +293 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-guardo-puente-almuhey) |
| `mp-btt-despensa-abad` | La Despensa del Abad | 25,4 / 25,36 | 450 | 2 h 30 | Baja | Cillamayor 42.86263, −4.27773 | 25,36 km · +293 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-la-despensa-del-abad) |
| `mp-btt-horca-ojeda` | La Horca de la Ojeda 🟨 | 22 / 22,02 | 375 | 2 h 15 | Baja | San Andrés de Arroyo 42.70195, −4.38255 | 22,02 km · +275 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-la-horca-de-la-ojeda) |
| `mp-btt-ermitas-aguilar` | Las Ermitas del Embalse de Aguilar | 21,6 / 21,41 | 419 | 2 h 15 | Baja | Vallespinoso de Aguilar 42.77399, −4.36764 | 21,41 km · +316 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-las-ermitas-del-embalse-de-aguilar) |
| `mp-btt-tamaricas` | Las Fuentes Tamáricas | 13,5 / 13,47 | 198 | 1 h 20 | Baja | Velilla del Río Carrión 42.82771, −4.844 | 13,47 km · +87 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-las-fuentes-tamaricas) |
| `mp-btt-valdavia` | Las Ranas del Río Valdavia 🟨 | 20 / 19,93 | 325 | 2 h | Baja | Respenda de la Peña 42.76368, −4.68649 | 19,93 km · +209 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-las-ranas-del-rio-valdavia) |
| `mp-btt-burejo` | Los Valles de Burejo | 20 / 20,07 | 317 | 2 h | Baja | Dehesa de Montejo 42.81944, −4.50994 | 20,07 km · +233 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-los-valles-de-burejo) |
| `mp-btt-karsticos` | Monumentos Kársticos | 17,7 / 17,73 | 371 | 1 h 50 | Baja | Villaescusa de las Torres 42.75905, −4.25095 | 17,73 km · +254 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-monumentos-karsticos) |
| `mp-btt-vega-carrion` | Por la Vega del Carrión | 20 / 20,03 | 254 | 2 h | Baja | Guardo 42.79109, −4.84814 | 20,03 km · +100 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-por-la-vega-del-carrion) |
| `mp-btt-ventas-pernia` | Por las Ventas de La Pernía | 9,2 / 9,27 | 160 | 55 min | Baja | San Salvador de Cantamuda 42.96864, −4.49503 | 9,27 km · +107 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-por-las-ventas-de-la-pernia) |
| `mp-btt-valle-estrecho` | Por Valle Estrecho | 17,3 / 8,55 | 295 | 1 h 45 | Baja | Ruesga 42.86402, −4.52766 | 8,55 km · +91 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-por-valle-estrecho) |
| `mp-btt-santullan` | Románico en Tierras de Santullán | 17 / 16,91 | 350 | 1 h 45 | Baja | Barruelo de Santullán 42.8979, −4.28264 | 16,91 km · +273 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-romanico-en-tierras-de-santullan) |
| `mp-btt-senda-pisuerga` | Senda del Pisuerga | 19 / 19,18 | 184 | 1 h 55 | Baja | Cervera de Pisuerga 42.86289, −4.49639 | 19,18 km · +66 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-senda-del-pisuerga) |
| `mp-btt-jano` | Tras las Huellas de Jano | 27,3 / 27,33 | 264 | 3 h | Alta | Guardo 42.7964, −4.84771 | 27,33 km · +799 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-tras-las-huellas-de-jano) |
| `mp-btt-triollo-guardo` | Triollo – Guardo (Turismo CyL) | 30 / 29,87 | 570 | — | Alta | Triollo 42.92486, −4.6809 | 29,87 km · +560 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-triollo-guardo) |
| `mp-btt-vuelta-bernorio` | Vuelta al Monte Bernorio | 20,4 / 20,55 | 280 | 2 h | Baja | Pomar de Valdivia 42.77484, −4.16699 | 20,55 km · +220 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-vuelta-al-monte-bernorio) |
| `mp-btt-aguilar` | "Ruta BTT" de Aguilar de Campoo | 13,4 / 13,4 | 104 | 1 h 20 | Baja | Aguilar de Campoo 42.79577, −4.27137 | 13,4 km · +22 m | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt) |

- **Ruta de los Pantanos** (palenciaturismo): ruta escénica de **81 km por carretera** (P-210 / CL-626 / CL-627) para coche, moto o bici, sin señalizar, que enlaza los embalses de Aguilar, Requejada, Ruesga, Camporredondo y Compuerto y los miradores del Alto de la Varga y de Alba de los Cardaños ([ficha](https://palenciaturismo.es/que-hacer/rutas/ruta-pantanos)) ✅. No es un sendero: ficha `mp-ruta-pantanos` en §16.8.
- Fuera de interés: "Cyclope Palencia Road Bike", ruta de carretera de 489 km por toda la provincia.

---

## 2. Cumbres: Mendikat y la guía coinciden en menos de 30 m

Las coordenadas son WGS84 y salen del JSON de cada página de Mendikat ✅. Cuando existe, la columna "Contraste" da el waypoint de cumbre de la guía de la Diputación ✅.

| Cumbre | Lat | Lon | Alt (m) | Prominencia | Ascensiones / visitas | Provincia | Contraste | Fuente |
|---|---|---|---|---|---|---|---|---|
| Peña Prieta | 43.02385 | −4.73001 | 2539 | 929 | 319 / – | 🟦 Cantabria (límite con León) | PeakVisor 43.023843, −4.730018 | [Mendikat 2132](https://www.mendikat.net/mount/pena-prieta-cantabria-espana/2132) |
| Pico del Infierno ("Monte Infierno", Peña Prieta Sur) | 43.02245 | −4.73088 | 2537 | 9 (antecima) | 94 / 9.294 | 🟦/Palencia. **Techo de Palencia** | Diputación 43.02226, −4.73091 | [Mendikat 4277](https://www.mendikat.net/mount/monte-infierno-cantabria-espana-and-palencia-espana/4277) |
| Curavacas | 42.97635 | −4.67397 | 2524 | 472 | 330 / 54.394 | Palencia (Triollo/Velilla). Cumbre más alta íntegramente palentina | Diputación 42.97634, −4.67395 · Mendiak 42.977234, −4.673280 ⚠️ | [Mendikat 8377](https://www.mendikat.net/mount/curavacas-palencia-espana/8377) |
| Tres Provincias | 43.02104 | −4.73803 | 2499 | 56 | 274 / 16.942 | 🟦🟧 mojón tripartito | Diputación 43.02096, −4.73782 | [Mendikat 2133](https://www.mendikat.net/mount/tres-provincias-cantabria-espana-and-palencia-espana-and-leon-espana/2133) |
| Espigüete | 42.94461 | −4.79622 | 2451 | 474 | 327 / 46.218 | Palencia (Velilla) | Diputación 42.94462, −4.79617 · Wikipedia 42.94472, −4.79611 | [Mendikat 8376](https://www.mendikat.net/mount/espiguete-palencia-espana/8376) |
| Alto del Tío Celestino | 43.01194 | −4.73247 | 2396 | 34 | 23 / 6.312 | Palencia | — | [Mendikat 14039](https://www.mendikat.net/mount/tio-celestino-alto-del-palencia-espana/14039) |
| Pico de Hoya Contina | 42.97827 | −4.71145 | 2395 | 182 | 6 / 3.900 | Palencia | — | [Mendikat 15947](https://www.mendikat.net/mount/hoya-contina-pico-de-palencia-espana/15947) |
| Pico Murcia | 42.98048 | −4.79452 | 2351 | 228 | 175 / 18.841 | Palencia / 🟧 León | Diputación 42.98047, −4.79449 | [Mendikat 8409](https://www.mendikat.net/mount/murcia-pico-palencia-espana-and-leon-espana/8409) |
| Lezna | 43.00689 | −4.64670 | 2208 | 473 | 71 / 14.089 | Palencia | — | [Mendikat 8378](https://www.mendikat.net/mount/lezna-palencia-espana/8378) |
| Cuchillón | — | — | 2174 (Diputación) | — | — | 🟦 límite | ID Mendikat 2028 (no consultado) ❓ | [Mendikat región](https://www.mendikat.net/region/palencia) |
| Tres Mares | 43.03800 | −4.40429 | 2171 | 103 | 230 / 36.564 | 🟦/Palencia | — (coordenadas de la ruta 31 erróneas) | [Mendikat 8386](https://www.mendikat.net/mount/tres-mares-cantabria-espana-and-palencia-espana/8386) |
| Valdecebollas | 42.96676 | −4.36542 | 2143 (Diputación 2142) | 292 | 208 / 21.976 | Palencia | Diputación 42.96676, −4.36541 | [Mendikat 8382](https://www.mendikat.net/mount/valdecebollas-palencia-espana/8382) |
| Peña Labra (Peñalabra) | 43.04556 | −4.43221 | 2029 | 77 | 158 / 25.556 | 🟦/Palencia | Diputación 43.04559, −4.43214 | [Mendikat 2129](https://www.mendikat.net/mount/penalabra-cantabria-espana-and-palencia-espana/2129) |
| Horca de Lores | 42.98628 | −4.58296 | 2021 | — | — | Palencia | Diputación ✅ (Mendikat ID 8379, no consultado) | [Guía p.41](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) |
| Peña Carazo | 42.97621 | −4.57844 | 2012 | — | — | Palencia | Solo Diputación ✅ | [Guía p.41](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) |
| Coto Blanco / Peña del Tejo | 42.94296, −4.7356 / 42.93772, −4.7402 | — | 2004 / 1998 | — | — | Palencia | Solo Diputación ✅ | [Guía p.20](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) |
| Pico / Peña del Fraile | 42.83289 | −4.76550 | 2001 | 595 | 87 / 12.667 | Palencia | Diputación 42.83271, −4.76555 | [Mendikat 8699](https://www.mendikat.net/mount/fraile-pena-del-palencia-espana/8699) |
| Peña Redonda | 42.85160 | −4.61330 | 1995 (Diputación 1996) | 366 | 84 / 24.254 | Palencia | Diputación 42.85161, −4.61329 | [Mendikat 8698](https://www.mendikat.net/mount/pena-redonda-palencia-espana/8698) |
| Peña Mayor de Velilla | 42.83819 | −4.82034 | 1869 | 154 | 17 / 8.205 | Palencia | Diputación 42.83811, −4.82032 | [Mendikat 13099](https://www.mendikat.net/mount/mayor-pena-palencia-espana/13099) |
| Santa Lucía | 42.91849 | −4.63884 | 1854 | — | — | Palencia | Solo Diputación ✅ | [Guía p.26](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) |
| Peña Mayor de Guardo | 42.8314 | −4.80353 | 1835 | — | — | Palencia | Solo Diputación ✅ | [Guía p.29](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) |
| Peña Lampa | 42.86069 | −4.86546 | 1804 | 488 | 20 / 10.685 | Palencia / 🟧 León (fuera del bbox por el oeste) | — | [Mendikat 8705](https://www.mendikat.net/mount/pena-lampa-palencia-espana-and-leon-espana/8705) |
| Cueto Morales / Peña Cildá | 42.92771, −4.33678 / 42.91684, −4.34241 | — | 1662 / 1616 | — | — | Palencia | Solo Diputación ✅ | [Guía p.50](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) |
| Pico Las Cruces / Pico Almonga | 42.84478, −4.53206 / 42.8493, −4.52158 | — | 1566 / 1519 | — | — | Palencia | Solo Diputación ✅ | [Guía p.38](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) |
| Peña Tremaya | 42.97741 | −4.48031 | 1441 | 176 | 18 / 7.750 | Palencia | — | [Mendikat 12903](https://www.mendikat.net/mount/pena-tremaya-palencia-espana/12903) |
| Valcabado (mirador de Ahedo) | 42.78174 | −4.10273 | 1221 | 306 | 22 / 6.545 | Palencia | — | [Mendikat 8260](https://www.mendikat.net/mount/valcabado-palencia-espana/8260) |
| Monte Bernorio | 42.79454 | −4.19491 | 1178 | 256 | 19 / 5.640 | Palencia | Wikiloc 1169–1178 ⚠️ | [Mendikat 8261](https://www.mendikat.net/mount/bernorio-palencia-espana/8261) |
| Pico Castillo / Peña Mesa | 42.74335, −4.2074 / 42.754, −4.25731 | — | 1100 / 1071 | — | — | Palencia | Solo Diputación ✅ | [Guía p.55–56](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) |
| Monte Cildá | 42.75157 | −4.27733 | 985 | 70 | 2 / 1.840 | Palencia | — | [Mendikat 20865](https://www.mendikat.net/mount/monte-cilda-palencia-espana/20865) |
| Pico Cordel | ❓ | ❓ | 2051 / 2061 ⚠️ | — | — | 🟦 Cantabria | Wikiloc | [Wikiloc waypoint](https://es.wikiloc.com/waypoints/3cnaOM/pico-cordel) |

Otros IDs de Mendikat (región Palencia) que **no se han consultado** ❓: Peña Mayor Oriental 13101, Cuartas 8787, Pico Pumar 15950, Cuchillón 2028, Peña Sestil 8388, Horca de Lores 8379, Curavacas Oeste 15954, Torre del Callejo Grande 12935 y Espigüete Este 23636 ([Mendikat región Palencia](https://www.mendikat.net/region/palencia)).

**Correcciones a valores previos.** Algunas notas daban coordenadas aproximadas de memoria que **eran erróneas** y no deben usarse:

| Punto | Valor previo (erróneo) | Valor correcto |
|---|---|---|
| Cardaño de Abajo | "42.958, −4.765" | ~42.921, −4.764 |
| Peña Prieta | "43.0125, −4.7340" | 43.02385, −4.73001 |
| Cardaño de Arriba | "42.988, −4.735" | ~42.970, −4.756 |

**Lagos glaciares (POI):**

| Lago | Altitud | Coordenadas | Fuente |
|---|---|---|---|
| Pozo de las Lomas | ~2.078–2.080 m (GPX 2.078; komoot 2.115) | 43.01047, −4.74287 (Terranostrum) · 43.01029, −4.74284 (komoot). La publicada 43.010628, −4.743068 queda a <50 m: **se da por buena** ✅/⚠️ | [komoot 1651543](https://www.komoot.com/highlight/1651543) |
| Laguna de Fuentes Carrionas | 2.206 m (Wikipedia ~2.220) | 43.01578, −4.73146 ✅ | Diputación ruta 06, WP14 |
| Pozo Curavacas | ~1.785–1.800 m | 42.99035, −4.68658 (punto de mapa de Terranostrum; fin del GPX a 1.785 m) ⚠️ | [Wikiloc 175034497](https://es.wikiloc.com/rutas-senderismo/circular-cardano-de-arriba-pozo-de-las-lomas-laguna-de-fuentes-carrionas-pozo-del-curavacas-collado-175034497) ⚠️ |

| Lago del Ves / Lagos del Ves | ~2.050 m (Wikipedia) | Sin coordenadas. Entre el Hoya Contina y la Curruquilla, cerca del Pozo Curavacas (libro 2026) | Wikipedia (Fuentes Carrionas) ⚠️ |

**Notas v2 de altitud y posición** (Wikipedia, libro 2026 y Terranostrum, contrastados con Mendikat; se mantienen los valores de la tabla salvo indicación):

- **Peña Labra:** el libro 2026 y Wikipedia dan **2.018 m** para la cima y 2.028,7 m para el vértice; Mendikat y la Diputación, 2.029. La diferencia probablemente es cima frente a vértice ⚠️.
- **Pico del Infierno:** Wikipedia lo sitúa a 171 m al sur de Peña Prieta, en 43.02218, −4.73184 (~80 m de Mendikat). Se mantiene Mendikat. Las cotas de Peña Prieta varían entre artículos (2.538 / 2.539 / 2.540,5 m).
- **Pico del Fraile:** Wikipedia (Sierra del Brezo) da 2.025 m frente a 2.001 de Mendikat y la Diputación ⚠️. Peña Cueto, según Terranostrum: 42.83689, −4.74850.
- **Peña Tremaya:** Terranostrum da 1.437 m y sitúa la cumbre en 42.97739, −4.47976, con caseta de vigilancia de incendios y antenas (Mendikat 1.441 m).
- **Valdecebollas:** Wikipedia 2.144 m (vértice 2.139). En la cima está el "Torreón", torre cilíndrica con vértice y buzón. **Tres Mares:** 2.171–2.172,6 m. **Monte Bernorio:** Wikipedia 1.170 m. **Pico Murcia:** Wikipedia 2.352 m. **Espigüete:** el libro 2026 dice 2.450 m.
- **Cumbres nuevas en v2:** Monte Coriscao 1.569 m (42.90374, −4.74454, Terranostrum) · Alto de Hornamiel 1.478 m (42.89713, −4.67082) · Peña El Cocoto (42.90407, −4.25846) · Alto Canalejas 2.096 m y El Cueto 2.083 m (cordal del Valdecebollas).
- **Macizo de Fuentes Carrionas** (Wikipedia): 52 cumbres de más de 2.000 m con al menos 30 m de prominencia, 11 por encima de 2.400 m; las 5 con más de 300 m de prominencia son Peña Prieta, Curavacas, Espigüete, Lezna y Horca de Lores.

---

## 3. Comentarios de usuarios y avisos por ruta

Casi no hay comentarios recientes accesibles. Wikiloc no se ha leído directamente (protección anti-bot, no se intentó saltar): lo que consta sale de fragmentos del buscador ⚠️. Los 20 tracks de Mendikat revisados no tienen comentarios: el 9607 solo tiene una nota de moderación de 2018. **En la v2 se añaden consejos de usuarios de komoot (leídos en su página ✅), la crónica de la Integral de Pyrenaica, la memoria de un club de 2026 y avisos de las fichas de Terranostrum.** No se encontraron crónicas de blog de 2024–2026 accesibles para Curavacas, Peña Prieta, Peña Redonda, Las Tuerces, Covalagua ni Fuente Cobre.

| Ruta | Comentario / aviso | Fecha | Fuente | Icono sugerido |
|---|---|---|---|---|
| Tejeda de Tosande | "Una de las rutas más bonitas e interesantes"; "espectaculares los tejos y el hayedo, y además es fácil"; el cartel dice "Tejal". Quejas: "la masificación hace perder su encanto"; calor en julio | 2024 | [W 24657668](https://es.wikiloc.com/rutas-senderismo/montana-palentina-tejeda-de-tosande-parque-natural-de-fuentes-carrionas-y-fuente-cobre-24657668) · [W 141704149](https://es.wikiloc.com/rutas-senderismo/tejeda-de-tosande-desde-el-parking-141704149) (+1 en Fuentes) | Masificación, calor |
| Tejeda de Tosande | Ruta cortada; hubo que volver desde el mirador. ¿Restricción por riesgo de incendio? (inferencia) | ago-2025 | [TripAdvisor](https://www.tripadvisor.com/Attraction_Review-g2559173-d21206556-Reviews-Tejeda_de_Tosande-La_Estacion_Province_of_Salamanca_Castile_and_Leon.html) (ficha mal ubicada en "Salamanca") ⚠️ | Cierre posible |
| Tosande (aparcamiento) | Se llena de día; prohibido pernoctar desde ~2020 | — | [park4night](https://park4night.com/es/place/70783) ⚠️ | Aparcamiento limitado |
| Fuente Cobre | "Puede estar embarrada", "más exigente de lo que parece", muy bien marcada; una pareja vio un oso (testimonio único) | — | [AllTrails](https://www.alltrails.com/trail/spain/palencia/pr-p-8-senda-de-fuente-cobre) ⚠️ | Barro, oso |
| Mazobre | Aparcamiento con pocas plazas (madrugar); en invierno la nieve dificulta la subida | — | [hoteles.net](https://www.hoteles.net/palencia/cervera-de-pisuerga/cascada-mazobre-palencia.html) · [W 150311857](https://www.wikiloc.com/hiking-trails/cascada-de-mazobre-cardano-de-arriba-150311857) ⚠️ | Aparcamiento, nieve |
| Curavacas normal | Sin señalización, solo algún hito; la pedrera del Callejo Grande es lo más duro; la trepada final no es para principiantes. El autor de un track pide sumar un grado si se tiene poca experiencia | — | [W 11774659](https://www.wikiloc.com/hiking-trails/pico-curavacas-montana-palentina-11774659) · [W 133695529](https://es.wikiloc.com/rutas-senderismo/curavacas-desde-vidrieros-por-callejo-grande-133695529) (+1 en Fuentes) | Pedrera, trepada, sin balizar |
| Curavacas Canal Sur | 38° de media con tramos de 60°; piolet y crampones; "solo expertos" | 2021 | [W 99549660](https://es.wikiloc.com/rutas-alpinismo/canal-sur-del-curavacas-desde-vidrieros-99549660) · [W 68926959](https://es.wikiloc.com/rutas-alpinismo/invernal-al-curavacas-por-canal-sur-directo-y-vuelta-por-callejo-grande-68926959) ⚠️ | Material invernal |
| Curavacas (conglomerado) | Caída continua de piedrecillas en las canales | — | [Pyrenaica 112](https://pyrenaica.emf.eus/wp-content/uploads/hemeroteka/112/pdf/pyrenaica_112_62.pdf) ⚠️ | Caída de piedras |
| Espigüete norte | "Totalmente desaconsejable tras una nevada por riesgo de aludes"; "muy exigente, pedrera y trepadas"; un montañero desaconsejó subir por la norte | 2015, 2017 | [W 9110380](https://es.wikiloc.com/rutas-alpinismo/espiguete-invernal-por-el-corredor-norte-9110380) · [W 19857255](https://es.wikiloc.com/rutas-alpinismo/espiguete-cara-norte-19857255) ⚠️ | Aludes, material invernal |
| Espigüete (accidentes) | El 16-05-2025, caída a ~500 m de la cumbre con evacuación en helicóptero. Ese mismo día, dos montañeros enriscados en el corredor NE con nieve. En otra fecha, tres rescates (goulotte N y cara S). Muerte de un montañero en mayo de 2024 | 2024–2025 | [Diario de León](https://www.diariodeleon.es/castilla-y-leon/250516/2048292/grupo-rescate-junta-auxilia-montanero-herido-espiguete.html) · [El Español](https://www.elespanol.com/castilla-y-leon/region/palencia/20250516/rescatado-helicoptero-montanero-herido-aparatosa-caida-pico-espiguete/1003743761154_0.html) (+4 en Fuentes) | Mayo = nieve primavera |
| Peña Prieta desde Cardaño | "Sencilla, sin tramos difíciles ni pasos técnicos, pero larga" | — | [W 220720071](https://es.wikiloc.com/rutas-senderismo/techo-de-palencia-pico-del-infierno2537m-por-canalagujas-de-cardanocon-pena-prieta2539m-y-tres-prov-220720071) ⚠️ | Longitud |
| Integral Fuentes Carrionas | Curavacas–collado del Ves con "terreno complicado"; poca agua; acampada junto a lagos sugerida por los relatos, **pero prohibida por la normativa** (§11) | — | [W 1782833](https://www.wikiloc.com/hiking-trails/integral-fuentes-carrionas-circular-2-noches-1782833) · [recmountain](https://recmountain.com/integral-de-fuentes-carrionas/) ⚠️ | Agua escasa, vivac no permitido |
| Peña Redonda | Sendas por el barranco poco marcadas, fácil perderse; bajada calurosa; desde Rebanal, tramo final mal marcado | — | [W 78127949](https://es.wikiloc.com/rutas-senderismo/importantes-cimas-de-la-sierra-del-brezo-circular-a-la-pena-redonda-y-pico-rebanal-por-el-barranco-78127949) · [W 91646014](https://www.wikiloc.com/hiking-trails/penarredonda-1-993-m-desde-rebanal-de-las-llantas-sierra-del-brezo-xiii-91646014) ⚠️ | Orientación |
| Peña Lampa | Pista con tráfico de camiones de una mina; aparcar en la carretera de Besande | — | [W 140549177](https://es.wikiloc.com/rutas-senderismo/pena-lampa-torre-magalana-roblon-el-monasterio-y-sabinar-de-pena-lampa-140549177) ⚠️ | Tráfico |
| Lezna desde Lores | "Al menos 8 h y 22 km" | — | [W 12093110](https://www.wikiloc.com/hiking-trails/ruta-semicircular-desde-lores-hasta-el-pico-lezna-y-el-pumar-12093110) ⚠️ | Longitud |
| Covalagua | Cascada casi seca (octubre de 2018; invierno seco de 2017) | 2017–18 | [W 16686613](https://www.wikiloc.com/hiking-trails/pomar-de-valdivia-pena-corvera-menhir-cueva-de-los-franceses-cascada-de-covalagua-16686613) ⚠️ | Estiaje |
| Valle de Pineda (BTT) | Pasada la Vega de Cantos, demasiado empinado y pedregoso para la bici | — | [W 7433651](https://www.wikiloc.com/mountain-biking-trails/pozo-curavacas-por-el-valle-de-pineda-7433651) ⚠️ | No ciclable |
| Pozo de los Lobos desde Revelillas 🟦 | Tramo no balizado; sin agua en el páramo | — | [Valderredible](https://www.valderredible.es/rutas/revelillas-pozo-de-los-lobos) ⚠️ | Sin balizar, sin agua |
| General (prados) | "Prados de diente con abundante ganado vacuno según las épocas del año" | — | [Diputación](https://www.diputaciondepalencia.es/sitio/turismo/rutas-naturaleza/senderismo) ✅ | Ganado |
| General | Zona casi libre de masificación, salvo Tosande y Mazobre | — | [somospalencia](https://www.somospalencia.es/tres-apasionantes-rutas-para-descubrir-la-montana-palentina/) ⚠️ | — |
| **Pozo de las Lomas** | **Un usuario cuenta que lo vio helado y "caminó sobre él"** → aviso de seguridad en la app: **no pisar nunca el hielo del lago**. Otro lo describe como un lago glaciar precioso bajo las Agujas de Cardaño; en invierno y a principios de primavera la nieve complica la subida | 14-02-2025 · 26-06-2026 · 15-05-2023 | [komoot 1651543](https://www.komoot.com/highlight/1651543) ✅ | Hielo, nieve |
| Mazobre | Mayor salto de agua de Palencia; mejor tras lluvias; desde el mirador una senda corta baja a la base; los 3 km desde Pino Llano son buena pista, también ciclable | 2022–2024 | [komoot 3487275](https://www.komoot.com/highlight/3487275) ✅ | — |
| Roblón de Estalaya | "Roble de más de 600 años; paseo fácil y bien señalizado". Otra fuente dice más de 500 años: edad discrepante | 03-04-2026 | [komoot Palencia](https://www.komoot.com/es-es/guide/50235/rutas-de-senderismo-en-palencia) ✅ | — |
| Espigüete (invernal) | Salida de club con dos grupos: huella aceptable en la cara N; la Pala Sur hubo que abrirla y en la bajada estaba "bastante penosa" (nieve de primavera) | mar-2026 | [Montaña Pegaso, memoria](https://montanapegaso.es/carteles/2026/Espiguete2026_memo.pdf) ⚠️ | Nieve, material invernal |
| Espigüete S (con perro) | Llenar agua en la gran fuente de Cardaño de Abajo, porque no hay más; subir la pedrera por el **lado derecho del canal**, con roca más firme; **perro atado**; las aristas E y N no son para mascotas | ~2024 | [Guía Repsol](https://www.guiarepsol.com/es/viajar/con-mi-mascota/ruta-con-perro-espiguete-palencia/) (solo buscador) ⚠️ | Sin agua, perros |
| Espigüete S | Error de orientación habitual: el vallejo de un arroyuelo que baja de la montaña **no** es el camino; hay que seguir la pista principal hasta la pedrera | — | [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ascension-pico-espiguete-por-la-cara-sur) ⚠️ | Orientación |
| Curavacas normal | "Ascensión muy dura por la pedrera; hace falta alguna trepada" | 21-09-2022 | [komoot](https://www.komoot.com/smarttour/e1068189616/curavacas-desde-vidrieros-parque-natural-montana-palentina) ✅ | Pedrera, trepada |
| Integral Fuentes Carrionas | El único punto de recarga fue el Pozo de las Lomas (agua de lago con pastillas); no encontraron el manantial bajo las Agujas; con calor se quedaron sin agua antes del Pico Cuartas. Destrepes expuestos en el Curavacas Oeste | — | [Pyrenaica 286](https://pyrenaica.emf.eus/wp-content/uploads/aldizkariak/286/artikulua_5998.pdf) ✅ | Agua, destrepe |
| Refugio de Pescadores (valle de Pineda) | "No es un hotel, pero te ayuda a pasar la noche"; chimenea pequeña que tira mal; plataforma elevada para dormir | 31-05-2021 · 20-06-2023 | [komoot 5837344](https://www.komoot.com/highlight/5837344) ✅ | Abrigo libre |
| Golobar | Edificio abandonado con vistas; hoy lo usan pastores y ganado. Carretera asfaltada con poco tráfico | 2022–2023 | [komoot 3394566](https://www.komoot.com/highlight/3394566) ✅ | No es refugio |
| Peña Labra / Tres Mares | Mirador de Piedrasluengas, "gran recompensa tras una larga subida"; desde Tres Mares se ve el camino a Peña Labra | 13-09-2026 · 28-09-2026 | [komoot cumbres PN](https://www.komoot.com/guide/415494) ✅ | — |
| Embalse de Ruesga | Baño permitido, zona de arena y alquiler de patines; pista agradable por la orilla | 2022 · 20-06-2026 | [komoot lagos PN](https://www.komoot.com/guide/3798621) ✅ | — |
| Peña Tremaya | Dejar las portillas como se encuentran; fuera del trazado hay aulagas | — | Terranostrum ⚠️ | Ganado |
| Pico Murcia (Terranostrum) | Tramo final entre Peña del Castillo y Cardaño con retamas altas, incómodo | — | Terranostrum ⚠️ | Vegetación |
| Las Tuerces (Amarilla y Verde) | Tramo intermedio laberíntico y sin senda; paso a nivel con muy poca visibilidad antes de Villaescusa; senda de pescadores con una roca pulida que entra en el agua | — | Terranostrum ⚠️ | Orientación, vía férrea |
| Las Tuerces (Roja) | Subir a Peña Mesa por los clavos es posible, pero **bajar es delicado** | — | Terranostrum ⚠️ | Trepada |
| Pico Lezna desde Lores | Tramo final campo a través, sin camino pero cómodo | — | Terranostrum ⚠️ | Orientación |

---

## 4. Refugios y chozos: ninguno guardado; Mazobre y los de pescadores siguen en uso

**En la vertiente palentina no hay refugios guardados.** El proyecto FTJ habla de 4 refugios y prevé restaurar 10 chozos ✅. Los nombres "Refugio de Vidrieros", "del Ves", "de Pineda" y "Collado de Fuentes Carrionas" **no aparecen en ninguna fuente**: probablemente se confunden con alojamientos como el Hostal Pineda o la Casa Cardiel ⚠️. En la app conviene usar la categoría "abrigo libre / estado no verificado", con la fecha del último dato.

**Novedades v2.** Se leyeron 13 fichas de refugioslibres.com: en la vertiente palentina solo hay 5 (Mazobre, Pescadores-Campoluengo, Santa Marina y las nuevas **Cabaña de Mollorente** y **Refugio de Cristo Sierra**). **Las coordenadas públicas de refugioslibres son una "zona aproximada"** (en Mazobre falla por ~5 km) y las exactas solo se ven con cuenta, que no se creó ❓. Casi todas las reseñas de su libro de visitas parecen **generadas o de relleno** (cuentas tipo "Test Meta" y frases de plantilla): no se usan como estado real. Sí se usan las descripciones de las fichas (sin fecha) y una reseña genuina de julio de 2026 (Cabaña de Naranco, León). Komoot aporta posiciones de highlight orientativas ✅.

| Nombre | Ubicación / acceso | Coordenadas | Capacidad / estado | Último dato | Fuente | Conf. |
|---|---|---|---|---|---|---|
| Refugio de Medio Ambiente del Postil de Soña | 1.526 m; ~1 h desde Vidrieros (según la guía alpina). Rotulado en el plano 2025 ✅. Toponimia: el Postil de Soña es también una cumbre del cordal Curruquilla–Hoya Contina, y el collado de Soña (2.217 m) queda sobre el Pozo del Ves | ❓ | Libre, 20 plazas (2018); "solo sirve de abrigo con mal tiempo". Sin ficha en refugioslibres ni datos posteriores a 2018 | 2018 / agregador | [Guía alpina](https://www.diputaciondepalencia.es/system/files/2024-05/guia_de_curavacas_y_espiguete-interactivo.pdf) · [refuge.camp](https://refuge.camp/es/refuge/refugio-del-postil-de-sona) | ⚠️ |
| Refugio de Medio Ambiente de Santa Marina | Valle de Pineda, junto a la confluencia del arroyo de Arauz con el Carrión; ~2 h por el valle. Rotulado en el plano 2025 ✅ | Zona aprox. 42.9640, −4.5565 (refugioslibres, no vale como posición) ❓ | Refugio de pescadores de dos niveles: abajo chimenea, mesa y sillas; arriba, por trampilla, **sitio para ~8 personas**. Leña escasa, río a <100 m. Guía alpina 2018: 20 plazas (probablemente de abrigo) | ficha sin fecha / 2018 | [refugioslibres](https://www.refugioslibres.com/refugios/refugio-de-santa-marina) · [Guía alpina](https://www.diputaciondepalencia.es/system/files/2024-05/guia_de_curavacas_y_espiguete-interactivo.pdf) | ✅ existencia / ⚠️ estado |
| Refugio de Mazobre (= refugio de la cara NE del Espigüete) | Majada de Espigüete, 1.559 m. Desvío a la izquierda hacia la mitad del camino Pino Llano–cascada, ~30 min desde el aparcamiento. Rotulado en el plano 2025 ✅ | ❓ La zona de refugioslibres (42.9607, −4.7347) es errónea. Estimación: entre Pino Llano (42.95100, −4.76174) y la cascada (42.95929, −4.79297) | **En uso, ~10 plazas para dormir** ✅ (refugioslibres): dos plantas, abajo chimenea, mesas y bancos; arriba altillo. "Buenas condiciones", señalizado. Las 20 plazas de la guía alpina serían de abrigo | ficha sin fecha / 2018 | [refugioslibres](https://www.refugioslibres.com/refugios/refugio-mazobre) · [walkaholic](https://www.walkaholic.me/es/refugio/espana/castilla-y-leon/palencia/234-refugio-mazobre) (+3 en Fuentes) | ✅ estado / ❓ posición |
| Refugio de los Pescadores (Campoluengo) | Pista del Carrión aguas arriba de Vidrieros, 1.357–1.490 m (se llega en coche) | **Posición sin resolver:** 42.9384, −4.64265 (walkaholic, a 1,6 km de Vidrieros) **o** ~42.9605, −4.6058 (komoot 42.96051, −4.60581 y 42.96098, −4.60563; zona de refugioslibres 42.9602, −4.5982), a ~5 km por la pista ⚠️ | **Probablemente abierto** ⚠️: refugioslibres lo da libre, 6 plazas, buen estado, chimenea, mesa, río a <100 m y "a menudo ocupado" por lo fácil del acceso; dos usuarios de komoot lo usaron como abrigo (2021 y 2023). La guía alpina de 2018 decía "cerrado, llaves en Vidrieros, 10 plazas" y no hay menciones de llave posteriores. Etiqueta: "abrigo libre, estado no verificado (2023)" | 2021–2023 / 2018 | [refugioslibres](https://www.refugioslibres.com/refugios/refugio-de-pescadores-campoluengo) · [walkaholic](https://www.walkaholic.me/shelter/spain/castile-and-leon/palencia/306-refugio-de-los-pescadores) (+2 en Fuentes) | ⚠️ |
| Refugio del Corral (ruta 18) | Santibáñez de la Peña, WP5, 1288 m | 42.8214, −4.74731 ✅ | "Refugio abierto, mesas de picnic, corral, abrevadero y fuente" | 2016 | [Guía p.32](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) | ✅ (2016) |
| Refugio de San Román (ruta 18) | Collado de San Román | ❓ | Citado sin detalle | 2016 | [Guía](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) | ✅/❓ |
| Chozo / Refugio de la Majada de Fuentes Carrionas | 1.878 m | 43.00948, −4.7172 ✅ (Diputación ruta 06, WP17) | "Estado deficiente": solo vivac de fortuna | 2026 (agregador) | [wikitrekk](https://wikitrekk.com/palencia/chozo-de-la-majada-de-fuentes-carrionas) · [peakvisor](https://peakvisor.com/mountain-hut/refugio-de-majadas-de-fuentes-carrionas.html) | ⚠️ |
| Chozo del Ves (roca) / Chozo de la Majada de Arriba / cueva del Tío Vicente (ruta 06) | Valle del Ves | 42.99576, −4.69013 / 42.99553, −4.7028 ✅ | Sin estado | 2016 | [Guía p.17](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) | ✅ posición / ❓ estado |
| Chozo de Tierraconcejo (ruta 09) | 1558 m | 42.92788, −4.74824 ✅ | Sin estado | 2016 | [Guía p.20](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) | ✅/❓ |
| Chozo del collado (ruta 14) | 1532 m | 42.92116, −4.61802 ✅ | Sin estado | 2016 | [Guía p.26](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) | ✅/❓ |
| Chozo de Vidal (ruta 16) | 1638 m | 42.83397, −4.80188 ✅ | Sin estado | 2016 | [Guía p.29](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) | ✅/❓ |
| Chozo Peñablanca (ruta 37) | 1559 m | 42.94679, −4.34859 ✅ | Sin estado | 2016 | [Guía p.54](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) | ✅/❓ |
| Refugio de Golobar | Final de la carretera del Golobar (Wikipedia: PP-2203, 1.840 m, la más alta de la provincia, sin mantenimiento y con desprendimientos) | 42.96718, −4.33678 (Terranostrum; 1.775 m en la página) · 42.96744, −4.33746 (komoot, 1.791 m) ⚠️ | **No apto como refugio** ✅: edificio del Parador inacabado (1973), propiedad de la Diputación, usado hoy como **corral de ganado** (Wikipedia; komoot 2022–2023). Sí es trailhead y salida para raquetas | 2016–2023 | [Guía p.53](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) · [komoot 3394566](https://www.komoot.com/highlight/3394566) (+1 en Fuentes) | ✅ |
| Chozos de la ruta 31 (WP5, WP22) | Valle de Los Redondos | **Coordenadas erróneas en el PDF** | — | 2016 | [Guía p.46–48](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) | ❓ |
| Chozo de las Tenadas de Lores | Valle de Lores, en la subida al Lezna (Terranostrum lo cita a 1 km o más de Lores) | ❓ **Candidato:** "refugio libre" de komoot en 43.02377, −4.55316 (1.614 m), con chimenea, leña y mesa (2022) | "Muy bueno", 8–10 plazas (2017). Identidad del candidato sin confirmar | ago-2017 / 2022 | [blog](http://subiendodosmilesenpalencia.blogspot.com/p/los-chozos-de-la-montana-palentina.html) · [komoot 4976372](https://www.komoot.com/highlight/4976372) | ⚠️/❓ |
| Chozo de Valcaliente | — | — | **Hundido** | — | ídem | ⚠️ |
| Refugio del club Espigüete (Cardaño de Arriba) | Al norte del pueblo, entre el camino al Pico Murcia y el arroyo que baja del Pozo de las Lomas ⚠️ | — | **Destruido por un alud entre el 9 y el 13-02-2015** (más de 2 m de nieve; el alud dañó también el camino, la iglesia y el tendido). Sin rastro de reconstrucción. **No mostrar como refugio** (Terranostrum aún lo cita en la ruta del Murcia) | 2015 / 2018 | [Guía alpina](https://www.diputaciondepalencia.es/system/files/2024-05/guia_de_curavacas_y_espiguete-interactivo.pdf) · [UVa, nieve y aludes](https://uvadoc.uva.es/bitstream/handle/10324/40660/Nieve-aludes-Monta%c3%b1a-Cant%c3%a1brica.pdf.pdf?sequence=1) (+2 en Fuentes) | ✅ |
| Refugio de Linares | Desde la Abadía de Lebanza | ❓ | Sin estado | — | [W 147075263](https://www.wikiloc.com/hiking-trails/abadia-de-lebanza-refugio-de-linares-hoyo-de-la-braguilla-147075263) | ❓ |
| Cabañas de pastores en las vegas de Correcaballos y Cantos | Valle de Pineda | ❓ | — | 2018 | [Guía alpina](https://www.diputaciondepalencia.es/system/files/2024-05/guia_de_curavacas_y_espiguete-interactivo.pdf) | ⚠️ |
| "Casa Hobbit" / Casa Enterrada | Alba de los Cardaños | ❓ | Abrigo libre | — | [komoot guide](https://www.komoot.com/el-gr/guide/366047) | ⚠️ |
| Vivac de las Agujas de Cardaño | Agujas de Cardaño | — | Vivac sin construcción (**solo autorizable**, §11) | — | [komoot guide](https://www.komoot.com/el-gr/guide/366047) | ⚠️ |
| Chozo de Peñalba (1600 m) / Caseta de Aguasalió (1720 m) 🟧 | Vertiente leonesa | — | — | 2018 | [Guía alpina](https://www.diputaciondepalencia.es/system/files/2024-05/guia_de_curavacas_y_espiguete-interactivo.pdf) | ⚠️ |
| Refugio Cubil del Can 🟦🟧 | Cerca de Peña Prieta | — | — | — | [peakvisor](https://peakvisor.com/peak/pena-prieta.html) | ⚠️ |
| **Cabaña de Mollorente (o del Pano)** 🆕 | Ladera sur del Pico Pando, estribaciones del Curavacas, 1.829 m. Desde Vidrieros por una pista que sale de la iglesia, **en mal estado y no apta para vehículos** | Zona aprox. 42.9399, −4.6367 ❓ | 3 plazas; chimenea, mesa, cama, leña escasa, **fuente a <100 m** | ficha sin fecha | [refugioslibres](https://www.refugioslibres.com/refugios/cabana-de-mollorente) | ✅ descripción / ❓ estado |
| **Refugio de Cristo Sierra** 🆕 | Cruce de pistas entre Valcobero y Valsurbio, 1.635 m; salida de la variante corta al Pico del Fraile | Zona aprox. 42.8276, −4.7681 ❓ | 6 plazas; sala con chimenea y mesa, y una pequeña **capilla**; leña; **fuente a <1 km** | ficha sin fecha | [refugioslibres](https://www.refugioslibres.com/refugios/refugio-de-cristo-sierra) | ✅ / ❓ |
| Dos refugios de pescadores de la Senda de los Pescadores (Velilla) 🆕 | Ribera del Carrión entre el Centro de la Trucha y el puente del Ahorcado | ❓ | Citados por palenciaturismo, sin detalle | 2026 | [palenciaturismo](https://www.palenciaturismo.es/que-hacer/rutas/senda-pescadores) | ⚠️ |
| Chozo de la Majada de las Vacas (PR-P 10) 🆕 | Senda del Pozo de las Lomas | ❓ | **En ruinas** | 2026 | [palenciaturismo](https://palenciaturismo.es/que-hacer/rutas/senda-laguna-lomas) | ⚠️ |
| Chozos de la subida al Lezna 🆕 | Majada de Tañuga y chozos de San Salvador (uno antiguo y otro moderno) | ❓ | Sin estado | — | Terranostrum (`mp-lezna`) | ⚠️ |
| "Refugio de Covalagua" (merendero) 🆕 | Paisaje Protegido de Covalagua, 1.081 m | 42.76982, −4.13132 (komoot) | Abrigo con mesas alrededor; para pasar el día, no para pernoctar | 2022–2024 | [komoot 6659058](https://www.komoot.com/highlight/6659058) | ⚠️ |
| Chozo del Prau del Toru 🆕 | Zona de Brañosera / Valdecebollas, 1.417 m | 42.93861, −4.33156 (komoot) | Chozo apoyado en una gran roca; algunos se siguen usando como refugio | 2022 | [komoot 4444419](https://www.komoot.com/highlight/4444419) | ⚠️ |
| Chozo Tonino (cueva) 🆕 | Barruelo, junto a un camino, 1.288 m | 42.92741, −4.25569 (komoot) | **POI histórico, no abrigo**: pequeña cueva donde se escondió un vecino en la posguerra | 2023 | [komoot 4444414](https://www.komoot.com/highlight/4444414) | ⚠️ |
| Refugios de la vertiente leonesa y cántabra 🟧🟦 🆕 | Cabaña de Naranco (Llánaves, 1.534 m, 6 plazas, buen estado; reseña genuina de ~jul-2026), Cabaña Linarucas (vacía), Refugio Majada de los Cantos (chimenea), Refugio del Pico del Calar (litera en mal estado), Cabaña Machorril, Refugio Rozalacalle; en Cantabria, Braña de los Tejos (mal estado) y El Murón | ❓ zonas aproximadas | Útiles para Peña Prieta desde Llánaves, Lechada y Barniedo | ficha sin fecha / 2026 | [Cabaña de Naranco](https://www.refugioslibres.com/refugios/cabana-de-naranco) (+7 en Fuentes) | ⚠️ |

Para preguntar por el estado actual de los refugios: Casa del Parque, 979 13 94 01 / 676 210 231 ([Horario 2026](https://patrimonionatural.org/ficheros/Horario%202026.pdf)) ✅.

---

## 5. Puntos de agua: ninguna fuente con control sanitario y el plano oficial desaconseja beber de los arroyos

**No hay ningún inventario de fuentes con caudal estacional ni potabilidad.** El plano oficial 2025 aconseja literalmente **"no beber agua de arroyos"** ✅ ([Plano 2025](https://patrimonionatural.org/ficheros/Parque%20Natural%20Monta%C3%B1a%20Palentina-%28sin%20senda%20Ruesga%29_compressed-20250621-104951.pdf)). Hay ganado extensivo en los puertos en verano ([palenciaturismo](https://www.palenciaturismo.es/system/files/2019-08/Casa%20parque%201.pdf)). Mensaje para la app: **tratar o filtrar siempre el agua**. Los abrevaderos no son agua potable. La **Fuente del Cobre no es un punto de agua**: es la cueva-surgencia del Pisuerga y debe ir como POI geológico ([fmdva.org](https://www.fmdva.org/media/oi1nwveq/07-docente-fuente-del-cobre.pdf)).

Puntos de agua con posición, todos de la guía de la Diputación (2016) ✅ posición / ❓ fiabilidad:

| Punto | Ruta | Coordenadas | Alt | Tipo |
|---|---|---|---|---|
| "Fuentes" (varios pequeños manantiales) | 09 Peña del Tejo, WP5 | 42.93032, −4.74299 | 1664 | Manantial |
| "Fuente" | 09, WP14 | 42.94831, −4.73463 | 1773 | Fuente |
| Arroyo, toma de aguas | 09, WP15 | 42.95067, −4.7471 | 1468 | Arroyo |
| Refugio del Corral: abrevadero y fuente | 18 Peña del Fraile, WP5 | 42.8214, −4.74731 | 1288 | Fuente + abrevadero |
| Manantial (sin WP) y fuente dentro de la Cueva de la Virgen | 18 | ❓ | — | Manantial |
| Abrevadero en pradera | 24 Pico Las Cruces, WP13 | 42.8435, −4.54983 | 1193 | Abrevadero |
| Abrevadero | 29 Peña Labra, WP5 | 43.0406, −4.44095 | 1642 | Abrevadero |
| Hoya y cascada | 29, WP10 | 43.04072, −4.4283 | 1744 | Agua superficial |
| Merendero con fuente de la Mina del Calero | 36 Peña Cildá, WP15 | 42.92842, −4.31267 | 1274 | Fuente |
| Fuentes de la Bodegona de Peñalba / Fuente de Peñablanca | 37 Valdecebollas (WP15, chozo) | 42.94679, −4.34859 (chozo) | 1559 | Manantial |
| Laguna de Fuentes Carrionas / Pozo de las Lomas | 06 / PR-P 10 | 43.01578, −4.73146 | 2206 | Lago (no potable) |

En los lugares de baja cota, el agua se toma en los pueblos de salida, como Cardaño, Vidrieros, Brañosera o Santibáñez. La consulta Overpass preparada incluye `natural=spring` y `amenity=drinking_water`.

**Puntos de agua citados en otras fuentes (v2).** Ninguno tiene control sanitario: **tratar o filtrar siempre**. La fiabilidad es la que declara la fuente. La crónica de la Integral de Pyrenaica, de primera mano, **confirma la escasez de agua en las crestas** ✅.

| Punto | Ruta / slug | Ubicación | Fiabilidad según la fuente | Fuente | Conf. |
|---|---|---|---|---|---|
| Gran fuente de Cardaño de Abajo | mp-espiguete-sur, mp-cardano-cruz-armada | Plaza o entrada del pueblo | Recomendada para llenar: **no hay más agua en la ruta del Espigüete S** | Guía Repsol (fragmento) | ⚠️ |
| Fuente del aparcamiento de Pino Llano | mp-espiguete-norte, mp-of-mazobre, mp-integral-fuentes-carrionas | Km 2,5 de la carretera de los Cardaños | Funcionamiento actual sin confirmar | SummitPost (fragmento) | ⚠️ |
| Pozo de las Lomas y arroyuelo del lago | mp-integral-fuentes-carrionas, mp-of-lomas | 43.01029, −4.74284 | **Único punto de recarga de la Integral**; agua de lago, tratada con pastillas | Pyrenaica 286 | ✅ |
| Manantial bajo las Agujas de Cardaño | mp-integral-fuentes-carrionas | Encima del Pozo de las Lomas | **No lo encontraron** en verano | Pyrenaica 286 | ✅ (negativo) |
| Fuente junto al arroyo de Cabriles | mp-curavacas-vidrieros, mp-integral-fuentes-carrionas | Bajada del Callejo Grande, cerca de Vidrieros | Existía cuando pasó el autor | Pyrenaica 286 | ✅ |
| Fuente a ~0,8 km de Cardaño de Arriba | mp-murcia-valcabe | Salida hacia el arroyo Valcabe | Sin dato de caudal | Terranostrum | ⚠️ |
| Fuente a <100 m de la Cabaña de Mollorente | — (Pico Pando, desde Vidrieros) | ~1.829 m | Según la ficha, sin fecha | refugioslibres | ✅/❓ |
| Río a <100 m de los refugios de Pescadores y Santa Marina | mp-valle-pineda, mp-pozo-curavacas-pineda | Carrión / Arauz | Río permanente (no potable sin tratar) | refugioslibres | ✅ |
| Fuente a <1 km del refugio de Cristo Sierra | mp-fraile (variante Cristo Sierra) | Entre Valcobero y Valsurbio | Según la ficha | refugioslibres | ✅/❓ |
| Cascada y arroyo de Mazobre | mp-of-mazobre | Cascada 42.95929, −4.79297 | Más caudal tras lluvias y en deshielo; **tramos de arroyo secos** porque la caliza filtra el agua | komoot · Terranostrum | ✅/⚠️ |
| Manantial potable junto al cartel de Villaescusa de las Torres | mp-tuerces-roja, -verde, -amarilla | Cruce de las rutas roja, verde y amarilla | "Potable" según Terranostrum; **en la meseta de Las Tuerces no hay manantiales**: cargar en Mave o Villaescusa | Terranostrum | ⚠️ |
| Fuente de la Flor y manantiales | mp-of-pedrosa | Bosque de La Pedrosa | "Famosa por la calidad de su agua" | Terranostrum | ⚠️ |
| Fuente Deshondonada / Fuente de la Sondonada | mp-of-gigante | Bajo la sierra de la Peña | Citada por palenciaturismo y por la leyenda del Gigante (Wikipedia); sin dato de caudal | palenciaturismo · Wikipedia | ❓ |
| Fuente, lavadero y pilón de Casavegas | mp-bocaron-casavegas | 43.02222, −4.51268 | Inicio de ruta | Terranostrum | ⚠️ |
| Abrevadero en el alto Polentinos–Lebanza | mp-polentinos-lebanza | Antes del collado Mojoncillo | Abrevadero (no potable) | Terranostrum | ⚠️ |
| Fuente de la Salud · Fuente Ferruginosa | mp-guardo-balcon-judas · mp-guardo-merendillas | Alrededores de Guardo | Sin dato de potabilidad | Terranostrum | ⚠️ |
| Agua en Mave y en los pueblos | mp-tuerces-azul, mp-tuerces-rosa | — | **Sin agua en la ruta** salvo en los pueblos | Terranostrum | ⚠️ |


---

## 6. Trailheads, aparcamientos y miradores

**Miradores oficiales del plano 2025** ✅ (sin coordenadas en el plano):

| Código | Mirador | Situación | Coordenadas |
|---|---|---|---|
| M01 | Piedrasluengas | Puerto (CL-627), aparcamiento propio | 43.0416715, −4.459259 ⚠️ ([soyecoturista](https://soyecoturista.com/en/actividad/equipamientos-de-uso-publico)). Diputación 43.04156, −4.45860 ✅ · palenciaturismo 43.04168, −4.45863 ✅. Salida de la "Senda de los Rojos" (límite con Cantabria, sin ficha) |
| M02 | El Campo | La Pernía | ❓ |
| M03 | Las Matas | Entre Cervera y Vañes; también inicio de la Senda del Oso | ❓ |
| M04 | Alto de la Varga | Ruta de los Pantanos, sobre la carretera Velilla–Cardaño; vista clásica del Espigüete (libro 2026) | 42.9085021, −4.7276461 ⚠️ ([soyecoturista](https://soyecoturista.com/en/actividad/equipamientos-de-uso-publico); [komoot](https://www.komoot.com/highlight/5786112)) |
| M05 | Alba de los Cardaños | — | ❓ |
| M06 | Ermita de la Peña | Perapertú | ❓ |
| M07 | Grullos | Entre Brañosera y Salcedillo (Monte Mayor) | ❓ |
| M08 | Bosque de los Municipios | Carretera del Golobar, Brañosera | ❓ |

Otros miradores: Mirador del Pinar (Velilla) 42.84934, −4.82944 ✅ (Diputación ruta 16). Mirador de Tosande 42.83719, −4.55003, a 1.404 m ✅ (ruta 24). Mirador de Valcabado (Mendikat) 42.78174, −4.10273 ✅. Mirador de la Leyenda en la Venganza del Conde ❓.

**Trailheads con coordenadas.** "Oficial" = ficha de la Junta. "Dip." = guía de la Diputación. "M" = Mendikat.

| Trailhead | Coordenadas | Fuente | Rutas |
|---|---|---|---|
| Cardaño de Arriba, aparcamiento | 42.97113, −4.75757 (Dip.) · 42.97167, −4.75583 (oficial) | ✅ | PR-P 10, rutas 03/05/06, Peña Prieta, Murcia |
| Cardaño de Abajo, plaza | 42.92095, −4.76391 | ✅ Dip. | Espigüete S, Integral (final) |
| Pino Llano (Mazobre), km 2,5 carretera de los Cardaños | 42.95167, −4.75889 | ✅ oficial | PR-P 6, Espigüete N |
| Puente Agudín | 42.92981, −4.75844 | ✅ Dip. | Ruta 09 |
| Vidrieros, plaza | 42.94238, −4.66465 (Dip.) · 42.9425, −4.6642 (GeoNames) | ✅ | Curavacas, Pineda, Pozo Curavacas |
| Santibáñez de Resoba, iglesia | 42.90640, −4.60950 | ✅ Dip. | Ruta 14 |
| Gigante del Valle Estrecho, km 15,5 Ruta de los Pantanos | 42.90639, −4.62639 | ✅ oficial | PR-P 7 |
| Ciudad del Brezo (Pinar de Velilla) | 42.85067, −4.83329 (Dip.) · 42.8575, −4.8175 (oficial) | ✅ (discrepancia ~1,3 km) | Pinar de Velilla, ruta 16 |
| Santibáñez de la Peña | 42.81049, −4.72966 | ✅ Dip. | Ruta 18 |
| Villanueva de la Peña | 42.82929, −4.62401 | ✅ Dip. | Ruta 23 |
| Traspeña de la Peña | ~42.819, −4.589 | ⚠️ M | Peña Redonda |
| Aparcamiento de Tosande (CL-626) | 42.82578, −4.51656 (Dip.) · 42.82611, −4.51528 (oficial) | ✅ | PR-P 3, ruta 24, Peña Redonda |
| Cervera (La Bárcena), Senda del Oso | 42.87306, −4.50139 | ✅ oficial | PRC-P 5, GR-1 |
| Estalaya / Roblón | 42.925, −4.46944 | ✅ oficial | PRC-P 4 |
| Verdeña | 42.94361, −4.45722 | ✅ oficial | PRC-P 9 |
| Abadía de Lebanza | 42.96297, −4.55346 | ✅ Dip. | Ruta 26 |
| Santa María de Redondo (Fuente Cobre) | 42.99139, −4.42667 (oficial) · ~42.988, −4.383 (M, baja) | ✅/⚠️ | PR-P 8, Tres Mares |
| Mirador de Piedrasluengas | 43.04156, −4.45860 | ✅ Dip. | Ruta 29, Peña Labra |
| Valle de Santullán, aparcamiento Senda Ursi | 42.90353, −4.34705 (Dip.) · 42.89167, −4.30889 (oficial) | ✅ (discrepancia: ¿inicios distintos?) | PRC-P 2, ruta 36 |
| Brañosera | 42.93663, −4.30992 (Dip.) · 42.9350, −4.3078 (AEMET) | ✅ | Ruta 37, Valdecebollas, Monte Mayor (ramal) |
| Villaescusa de las Torres, puente del Pisuerga | 42.75961, −4.25488 | ✅ Dip. | Ruta 40, Tuerces |
| Villarén de Valdivia | ~42.777, −4.185 | ⚠️ M (baja) | Bernorio |
| Velilla del Río Carrión | caja 42.841–42.864 / −4.892 a −4.857 | ⚠️ M (baja) | Peña Lampa |
| **Nuevos en v2** (TN = Terranostrum, inicio del GPX; PT = marcador de palenciaturismo) | | | |
| Cardaño de Arriba, junto a la iglesia | 42.97106, −4.75758 (TN) · 42.97079, −4.75741 (PT) | ✅ | PR-P 10, Murcia |
| Pino Llano | 42.95100, −4.76174 (PT) · 42.95120, −4.76168 (TN) | ✅ | PR-P 6, Espigüete N |
| Cardaño de Abajo, plaza | 42.92073, −4.76413 · 42.92153, −4.76374 (TN) | ✅ | Cruz Armada, Espigüete S |
| Triollo, puente del Carrión | 42.92303, −4.67943 (TN) | ✅ | Triollo–Hornamiel, GR-1 E4/E5 |
| Camporredondo de Alba | 42.89511, −4.74564 (TN) | ✅ | Cueva Dorada, Coriscao, Valsurbio, GR-1 E5/E6 |
| Embalse de Compuerto, plataforma antes del túnel (km 52) | 42.85679, −4.80806 (TN) | ✅ | Valsurbio |
| Poblado de Compuerto / Ciudad del Brezo | 42.85064, −4.83302 (PT) · 42.84860, −4.83557 y 42.84970, −4.83507 (TN) | ✅ (coincide con la Diputación; la coordenada de la ficha de la Junta queda ~1,3 km al NE ⚠️) | Pinar de Velilla, Collado del Pinar, ruta 16 |
| Velilla, Centro de la Trucha ("paraje del Soto") | 42.82599, −4.84857 (PT) | ✅ | Senda de los Pescadores |
| Velilla, campo de tiro | 42.83371, −4.84872 (TN) | ✅ | PRC-P 12 Roblón del Monasterio |
| Guardo (centro) / Muñeca (plaza) | 42.78995, −4.84311 (TN) / 42.79202, −4.80148 (PT) | ✅ | Senderos de Leyenda |
| Fresno del Río, área recreativa 🟨 | 42.68089, −4.82386 (TN) | ✅ | PRC-P 14 Valdelobos |
| Santibáñez de la Peña, antiguas escuelas | 42.80945, −4.72989 (TN) | ✅ | Peña del Fraile |
| Cervera, puente de San Roque | 42.87235, −4.50293 (PT) · 42.87209, −4.50276 (TN) | ✅ | Senda del Oso |
| Cervera, puesto de Cruz Roja (CL-627) | 42.85709, −4.49949 (TN) | ✅ | Almonga y Las Cruces |
| Cervera (centro, Camino Olvidado / Lebaniego) | 42.86210, −4.49855 (TN) | ✅ | CO E6/E7, Lebaniego E7/E8 |
| Casa del Parque (Cervera) | 42.86314, −4.49554 (PT) | ✅ | — |
| Ruesga | 42.86402, −4.52766 (TN, BTT) | ⚠️ | Embalse de Ruesga |
| Estalaya / Roblón (PP-2173, tras el puente de Requejada) | 42.92422, −4.47202 (PT) · 42.92417, −4.47207 (TN) | ✅ | PRC-P 4, GR-1 E2/E3 |
| Verdeña, entrada | 42.94307, −4.46424 (PT) · 42.94297, −4.46199 (TN) | ✅ | PRC-P 9 |
| Gigante del Valle Estrecho | 42.90541, −4.62797 (PT) · fin en el Mirador de Caldacio 42.89526, −4.61463 (TN) | ✅ | PR-P 7 |
| San Salvador de Cantamuda, colegiata | 42.96686, −4.49547 (TN) | ✅ | Venganza del Conde, Lebaniego E8/E9 |
| Tremaya, puente sobre el Pisuerga (PP-2176) | 42.97937, −4.46532 (TN) | ✅ | Peña Tremaya |
| Santa María de Redondo, parking de Fuente Cobre | 42.99156, −4.42791 (PT) · 42.99148, −4.42837 (TN) | ✅ | PR-P 8, Ribero Pintado, Tres Mares |
| San Juan de Redondo, iglesia | 42.98999, −4.44842 (TN) | ✅ | Corrala de Bismo |
| Casavegas, fuente y lavadero | 43.02222, −4.51268 (TN) | ✅ | Bocarón |
| Lores | 42.99656, −4.53308 (TN) | ✅ | Pico Lezna |
| Polentinos, plaza del Ayuntamiento | 42.93841, −4.52466 (TN) | ✅ | Polentinos–Lebanza |
| Abadía de Lebanza | 42.96283, −4.55313 (TN) | ✅ | coincide con la Diputación |
| Vidrieros, plaza | 42.94283, −4.66461 (TN) · aparcamiento 42.94161, −4.66191 (komoot) | ✅ | Curavacas, Pineda |
| Puente Agudín | 42.92980, −4.75852 (TN) | ✅ | Sima del Anillo, ruta 09 |
| El Golobar (final de la PP-2203) | 42.96718, −4.33678 (TN) · 42.96744, −4.33746 (komoot) | ✅/⚠️ | Valdecebollas corta, Sel de la Fuente |
| Brañosera | 42.93659, −4.31027 (TN) · 42.93680, −4.30836 (PT, GR-1) | ✅ | Valdecebollas, GR-1 |
| Barruelo, barrio de San Pedro / puente de Peñacorva | 42.91139, −4.28831 / 42.91143, −4.28835 (TN) | ✅ | La Pedrosa, Calero, Ujapero |
| Villabellaco, iglesia de San Pedro | 42.89109, −4.31070 (PT) · 42.89342, −4.31060 (TN) | ✅ | **Inicio principal de la Senda Ursi** |
| Salcedillo | 42.94084, −4.27340 (PT) · 42.94085, −4.27437 (TN) | ✅ | GR-1 E1, Monte Mayor, Rojadillo |
| Valberzoso (a 1 km del pueblo) | 42.92382, −4.23767 (TN) | ✅ | Rojadillo, Somahoz, Monte Mayor |
| Puente romano de Rojadillo | 42.93549, −4.24146 (TN) | ✅ | GR-1 E1 |
| San Cebrián de Mudá, Centro del bisonte | 42.89711, −4.38622 (TN) · Reserva del Bisonte 42.89728, −4.38597 (PT) | ✅ | Minas de San Cebrián, BTT Mudá |
| San Martín de Perapertú (Monte Ciruelo) | 42.91746, −4.36875 (TN) | ✅ | Monte Ciruelo |
| Mudá, puente del arroyo de la Pradera | 42.87619, −4.39526 (TN) | ✅ | Mudá–Monasterio |
| Ligüérzana, puente del Pisuerga | 42.85677, −4.45841 (TN) | ✅ | Mariposas |
| Cillamayor, teleclub | 42.86254, −4.27877 (TN) | ✅ | Matabuena, BTT |
| Canduela / Menaza | 42.83439, −4.18623 / 42.83134, −4.21617 (TN) | ✅ | Valdelobera, Menaza |
| Aguilar de Campoo, zona deportiva (cartel) | 42.78994, −4.25874 (TN) · Aguilar centro 42.79282, −4.25910 | ✅ | Tuerces Verde, CO E5/E6 |
| Mave (cartel de rutas) | 42.73644, −4.27328 (TN) | ✅ | Tuerces Roja, Amarilla, Azul |
| Gama (cartel) | 42.74776, −4.20809 (TN) | ✅ | Tuerces Rosa |
| Villaescusa de las Torres, parking a la entrada | 42.75741, −4.24754 (PT) | ✅ | Tuerces circular |
| Revilla de Pomar, iglesia | 42.77071, −4.15124 (TN) | ✅ | Covalagua |
| Cueva de los Franceses | 42.77212, −4.11582 (TN) · 42.77255, −4.11672 (PT) | ✅ | Franceses–Lobos |
| Pomar de Valdivia | 42.77484, −4.16699 (TN, BTT) | ✅ | Vuelta al Bernorio |

**Siguen sin coordenadas** ❓: Lebanza (pueblo), el aparcamiento y mirador de Grullos (M07) y los miradores M02, M03, M05, M06 y M08. Las coordenadas de palenciaturismo marcan a veces el centro del pueblo y no el aparcamiento ⚠️. El puerto de San Glorio (~43.07, −4.76) queda **fuera del bbox, en León/Cantabria** 🟧🟦 ❓.

**Libro "Montaña Palentina. Coordenadas de Luz de un Territorio" (Diputación, 2026).** Leído en la v2 ✅. Es un **catálogo fotográfico de 40 enclaves**, no una guía de rutas: el propio libro dice que no trae tracks, horarios ni itinerarios y que sus coordenadas y accesos "solo orientan". Fotografías de Juan García Lucas; depósito legal P 30-2026; 31 páginas en PDF; financiado por el Plan de Sostenibilidad Turística en Destino (NextGenerationEU); acompañó una exposición en Guardo (18-6 al 15-7-2026). **El enlace antiguo `/system/files/2026-05/…` devuelve 403**; el vigente está en `/system/files/2026-06/…` ([libro ES](https://palenciaturismo.es/system/files/2026-06/LIBRO%20MONTA%C3%91A%20PALENTINA%20%28versi%C3%B3n%20espa%C3%B1ol%29%20%281%29.pdf)), junto con la versión inglesa, el mapa interactivo y la nota de prensa (+3 en Fuentes). Datos sueltos útiles ⚠️: el tejo principal de Tosande ("Árbol rey") superaría los 1.200 años; el Ojo de la Lastra (arco al pie de Santa Lucía) coincide con el WP8 de la ruta 14; Pozo Merino es una poza en la desembocadura del Rubagón; el puente romano de Rojadillo cruza el Camesa (GR-1 E1); la Mina de Carracedo es una brecha minera a la que no hay que asomarse; el Pino Enroscao está en el Pinar de Velilla; Peñalabra se presenta como el mejor mirador, a 1 km de El Campo.

**Enclaves del mapa interactivo del libro.** Cada enclave lleva un enlace corto de Google Maps (`maps.app.goo.gl`) que **no se ha podido resolver a coordenadas** (host no permitido) ❓. Se emparejaron por posición en el PDF; los n.º 8 y 31 quedaron sin rótulo seguro. Licencia: solo nombres y enlace.

| Nº | Enclave | Enlace | Slug relacionado |
|---|---|---|---|
| 1 | Pico Curavacas | https://maps.app.goo.gl/CPchniJD2Tz63XEY8 | mp-curavacas-vidrieros |
| 2 | Pico Espigüete | https://maps.app.goo.gl/tZayfZUGR4LJL81y6 | mp-espiguete-sur |
| 3 | Peña del Fraile | https://maps.app.goo.gl/gRiKc3zSynSsMuKb7 | mp-fraile |
| 4 | Peña Redonda | https://maps.app.goo.gl/j5dX5HUN8ggdU7Ai6 | mp-pena-redonda |
| 5/32 | Peñalabra | https://maps.app.goo.gl/1M1nYGpkhjaPMVxN9 | mp-penalabra-tresmares |
| 6 | Sinclinal de la Verdiana | https://maps.app.goo.gl/EKea3EogTwnxed2S8 | mp-dip-33 |
| 7 | Peña Tremaya | https://maps.app.goo.gl/sZtojx7TTpU49Xjv8 | mp-tremaya |
| 8 / 31 | Ojo de la Lastra / Cara sur de Peña Redonda (sin emparejar) | https://maps.app.goo.gl/13HADbYCigeJUpmZ9 · https://maps.app.goo.gl/i5oZX4zaqwWKtPDG7 | mp-dip-14 / mp-pena-redonda |
| 9 | Río Pisuerga | https://maps.app.goo.gl/qcCoA4SX7aciE7SB6 | — |
| 10 | Río Carrión | https://maps.app.goo.gl/ETiNcwHA8aosnTjW8 | — |
| 11 | Río Rubagón | https://maps.app.goo.gl/rRWcfG8eonYysJ7z9 | mp-of-pedrosa |
| 12 | Río Camesa | https://maps.app.goo.gl/LtrPM4DJdt3akFqk8 | mp-gr1-e1 |
| 13 | Valle de Pineda y Pozo de Fuentes Carrionas | https://maps.app.goo.gl/V7haWCTSddZ3j82G6 | mp-valle-pineda |
| 14 | Pozo de las Lomas | https://maps.app.goo.gl/kMqwgAydBDUzQ7Ln8 | mp-of-lomas |
| 15 | Agujas de Cardaño | https://maps.app.goo.gl/z2Qpdy5RRbV3pWZz9 | mp-of-lomas |
| 16 | Lagos del Ves | https://maps.app.goo.gl/pEqqjKRNFMS6x9377 | mp-circular-lagos |
| 17 | Fuente del Cobre | https://maps.app.goo.gl/vFTTDGNkbVJ3gVia6 | mp-of-fuente-cobre |
| 18 | Alto de la Miranda | https://maps.app.goo.gl/wqoQZiVwSmG55cHM7 | mp-gr1-e5 ⚠️ |
| 19 | Ribero Pintado | https://maps.app.goo.gl/t7cEaD7vHaqVUeeJA | mp-ribero-pintado |
| 20 | Tejeda de Tosande | https://maps.app.goo.gl/Jh15UqWATKiGG3BJA | mp-of-tosande |
| 21 | Senda de los Rojos | https://maps.app.goo.gl/PBSgibjLBJw7a5iN7 | — (sin ficha) |
| 22 | Roblón de Herreruela | https://maps.app.goo.gl/4WtK824GkNSZZFsk7 | mp-gr1-e2 ⚠️ |
| 23 | Pozo Merino | https://maps.app.goo.gl/4EABgjsSRrYvQrgG8 | — |
| 24 | Puente Rojadillo | https://maps.app.goo.gl/M5XKwKsiTAR4PiAb6 | mp-valberzoso-rojadillo |
| 25 | Cascadas de Mazobre | https://maps.app.goo.gl/dCYpX5ez1bYbtPn68 | mp-of-mazobre |
| 26 | Castros Negros | https://maps.app.goo.gl/asRJidBKnMbUHj52A | ❓ |
| 27 | Camporredondo | https://maps.app.goo.gl/pRXNLxnJhGHh6ogE8 | mp-gr1-e5 |
| 28/40 | Alba de los Cardaños | https://maps.app.goo.gl/iMHGYyW82NDkgzse6 | — (mirador M05) |
| 29 | Cara norte del Curavacas | https://maps.app.goo.gl/inUWEdWE8FX9fAgz6 | mp-pozo-curavacas-pineda |
| 30 | Espigüete desde el Alto de la Varga | https://maps.app.goo.gl/yS2sZYAYY4fsyc8w7 | — (mirador M04) |
| 33 | Peña Abismo | https://maps.app.goo.gl/6uQNtXQY9Fsa42eB7 | mp-dip-30 |
| 34 | La Verdiana | https://maps.app.goo.gl/jLGCSQrUXWRXX2kBA | mp-dip-33 |
| 35 | Pino Enroscao | https://maps.app.goo.gl/mX1YHaiz24EcSM5r9 | mp-of-pinar-velilla |
| 36 | Árbol Rey de Tosande | https://maps.app.goo.gl/s5jh7m4ddZ7Ls1aF9 | mp-of-tosande |
| 37 | Reflejos de Camporredondo | https://maps.app.goo.gl/sXsgRGV4ABjvKBbY7 | — |
| 38 | Ojo de Caloca (Bocarón) | https://maps.app.goo.gl/XqELXxqV36jCAJZVA | mp-bocaron-casavegas |
| 39 | Mina de Carracedo | https://maps.app.goo.gl/jqjsPQzMppWuyMkEA | ❓ |

**Campings, albergues y autocaravanas.** No hay datos verificados. El PUP dice que **no hay campings dentro del parque** y que el área de Ruesga estuvo cerrada como zona de acampada ✅. Hay carteles de prohibido pernoctar en los aparcamientos ⚠️.

---

## 7. Casas del Parque y centros de interpretación

| Centro | Dirección / contacto | Horario | Notas | Fuente | Conf. |
|---|---|---|---|---|---|
| **Casa del Parque Natural Montaña Palentina ("Zona Oso")** | C/ El Plantío s/n, 34840 Cervera de Pisuerga · **979 139 401** · cp.montanapalentina@patrimonionatural.org · grupos 676 210 231 | 12/02–30/06 y 01/09–13/12: jueves a sábado 10–14 y 17–20, domingo 10–14 · 01/07–31/08: martes a sábado 10–14 y 17–20, domingo 10–14 · abierta el 8-dic · **cerrada del 14/12/2026 al 11/02/2027** (inferido del horario) | Exposición "Zona Oso", maqueta y audiovisual; informa sobre senderos y cierres. La coordenada de la ficha ("42º 5' 50" N 4º 29' 41" W") es una **errata**; palenciaturismo la sitúa en 42.86314, −4.49554 ✅ | [Casa del Parque](https://patrimonionatural.org/casas-del-parque/casas-del-parque/casa-del-parque-de-fuentes-carrionas-y-fuente-cobre-montana-palentina) · [Horario 2026](https://patrimonionatural.org/ficheros/Horario%202026.pdf) · [Turismo CyL](https://www.turismocastillayleon.com/es/naturaleza/casa-parque-natural-montana-palentina) | ✅ |
| Oficina comarcal de turismo de Cervera | Tel. 979 870 688. La guía alpina de 2018 lo atribuía a la Casa del Parque (**discrepancia**) | ❓ | — | [Turismo CyL](https://www.turismocastillayleon.com/es/servicios/oficinas-turismo-4ec3/oficina-comarcal-turismo-cervera-pisuerga) | ⚠️ |
| Casa del Parque "KARST" (Aguilar de Campoo) | Proyecto FTJ de 1.323.000 € | ❓ | Centro de referencia previsto para Tuerces y Covalagua. Estado de apertura desconocido | citado en Patrimonio Natural | ⚠️ |
| Centro de Interpretación de la Minería (Barruelo de Santullán) | C/ Cerrada s/n, 34820 · 979 607 294 · oficina de turismo de Barruelo: Av. Constitución 20, 979 606 045 | Agregador: miércoles a viernes 10:00–13:30 y 16:00–19:30; cierra lunes y martes; cierre invernal del 12/12 al 28/02 ⚠️ | Mina visitable. Obras de rehabilitación energética licitadas | [Turismo CyL](https://www.turismocastillayleon.com/es/patrimonio-cultura/centro-interpretacion-mineria) · [turismobarruelo](https://turismobarruelo.com/cim/mina-visitable-en.php) · [whichmuseum](https://whichmuseum.com/museum/centro-de-interpretacion-de-la-mineria-barruelo-de-santullan-34726/opening-hours) · [licitación](https://barruelo.com/descargas_breves/licitacion-cim.pdf) | ✅/⚠️ |
| Centro de Interpretación de la Trucha (Velilla) | — | ❓ | Inicio de la Senda de los Pescadores | [palenciaturismo](https://www.palenciaturismo.es/que-hacer/rutas/senda-pescadores) | ⚠️ |
| Cueva de los Franceses (Revilla de Pomar) | 659 949 998 · turismo@dip-palencia.es | **Cerrada temporalmente por obras** según palenciaturismo (consultado el 21-11-2026) ✅. Fuera de obras: cierra lunes y del 9-ene al 28-feb; reserva imprescindible; ~3 €; ~45 min | No accesible para movilidad reducida. Abierta al turismo desde 1974; se entra por un túnel artificial y la sima original de 6 m está clausurada. Coordenadas 42.77255, −4.11672 | [palenciaturismo](https://palenciaturismo.es/visitar/lugares-interes/cueva-franceses) · [Terranostrum](https://www.terranostrum.es/turismo/palencia/montana-palentina/revilla-de-pomar/visita-cueva-de-los-franceses) · [Spain.info](https://www.spain.info/es/lugares-interes/cueva-franceses/) | ⚠️ |
| Reserva del Bisonte Europeo (San Cebrián de Mudá) | 42.89728, −4.38597 | Visita siempre guiada, 2 h, a 2 km del centro de interpretación | Inicio de `mp-minas-san-cebrian` y de la BTT del Alto Valle de Mudá | [palenciaturismo](https://palenciaturismo.es/visitar/lugares-interes/reserva-bisonte-europeo-bison-bonasus) | ✅ |
| Geoparque Las Loras: app **"Las Loras 360"** (lanzada el 19-11-2026) | [App Store](https://apps.apple.com/es/app/las-loras-360/id6761060682) · [Google Play](https://play.google.com/store/apps/details?id=com.argeol.lasloras360) | — | Por ahora con contenidos burgaleses; las rutas palentinas "se irán incluyendo". Salidas guiadas mensuales "Descubriendo el Geoparque" ([PDF 2026](https://geoparquelasloras.es/wp-content/uploads/2026/06/Descubriendo-el-geoparque-2026.pdf), no leído) | [Noticia](https://geoparquelasloras.es/2026/11/19/el-geoparque-las-loras-lanza-las-loras-360-una-nueva-aplicacion-para-descubrir-el-territorio-a-traves-de-rutas-turisticas/) | ✅ |
| Centro del Geoparque, Villadiego 🟪 | Burgos | — | Fuera del ámbito | [Turismo CyL](https://www.turismocastillayleon.com/es/rural-naturaleza/geoparques/geoparque-mundial-unesco-loras) | ✅ |

---

## 8. Emergencias: 112, sin GREIM en Palencia

| Elemento | Dato | Fuente | Conf. |
|---|---|---|---|
| Número | **112 Castilla y León**. Funciona con la cobertura de cualquier operadora, pero necesita alguna | [FEMECV](https://www.femecv.com/sites/default/files/uploads/files/Opciones%20comunicacion%20montana.pdf) · [senditur](https://www.senditur.com/es/blog/como-comunicar-una-emergencia-cuando-hacemos-senderismo-o-montana/) | ✅/⚠️ |
| Rescate | **No hay GREIM en Palencia.** Actúan el GREIM de Sabero 🟧 (23 rescates y 38 personas en 2025), el Grupo de Rescate y Salvamento de la Junta / Protección Civil con helicóptero, y los bomberos de la Diputación | [Guardia Civil montaña](https://web.guardiacivil.es/pdflink/es/fb46b663-4062-11eb-8bde-6d0b3e4c7555/Especialidad-Montana.pdf) · [Diario de León](https://www.diariodeleon.es/leon/provincia/250805/2056076/greim-sabero-leon-interviene-23-rescates-montana-38-personas-2025.html) · [The Objective](https://theobjective.com/actualidad/2023-02-27/rescate-cadaver-montanero-palencia/) · [El Mirón de Soria](https://elmirondesoria.es/soria/sucesos/fallece-montanero-en-monte-curavacas/amp) · [Vozpópuli](https://www.vozpopuli.com/sucesos/muere-un-escalador-de-30-anos-tras-sufrir-una-indisposicion-mientras-ascendia-el-pico-curavacas-en-palencia.html) · [El Mirón (Espigüete)](https://elmirondesoria.es/soria/sucesos/rescatados-dos-montaneros-enriscados-en-pico-espigueete/amp) | ⚠️ |
| Centro de salud de Cervera | C/ Felipe Calvo s/n · 979 870 291 (otro directorio: 979 870 494) | [saludcastillayleon](https://www.saludcastillayleon.es/CAPalencia/en/area-influencia/z-b-s-cervera-pisuerga) | ✅/⚠️ |
| Centro de salud de Aguilar | Av. Ciudad Deportiva s/n · 979 122 088 (otro: 979 125 440) | [saludcastillayleon](https://www.saludcastillayleon.es/CAPalencia/es/area-influencia/z-b-s-aguilar-campoo) | ✅/⚠️ |
| Centro de salud de Guardo (Velilla es consultorio de su ZBS) | 979 851 505 | [saludcastillayleon](https://www.saludcastillayleon.es/es/citaprevia/centros-adscritos-sistema-cita-previa/palencia) | ✅ |
| Hospital de referencia | Complejo Asistencial Universitario de Palencia (Hospital Río Carrión) | [saludcastillayleon](https://www.saludcastillayleon.es/CAPalencia/fr/cartera-servicios/urgencias) | ✅ |
| Protocolo para la app (inferencia) | 1) Llamar al 112 dando las coordenadas WGS84. 2) Sin cobertura, subir a un collado o probar por SMS. 3) Usar el SOS satelital. El helicóptero de la Junta es probablemente el medio más rápido | — | ❓ |
| Cobertura | Sin datos. Probablemente mala en Vidrieros, Lebanza, Pineda y Cardaño | — | ❓ |

---

## 9. Transporte

| Medio | Dato | Fuente | Conf. |
|---|---|---|---|
| Autobús regional | Concesiones VACL-111 (Cervera–Palencia) y VACL-079 (Guardo–Palencia) | [BOCCL](https://sirdoc.ccyl.es/SIRDOC/PDF/PUBLOFI/BO/CCL/11L/BOCCL1100248/BOCCL-11-008044.pdf) | ✅ |
| Palencia–Guardo | Autocares Abagón (abagon.es), unos 5 días a la semana | [rome2rio](https://www.rome2rio.com/es/Autob%C3%BAs/Palencia/Guardo) | ⚠️ |
| Guardo–Velilla | Horario municipal; horario de verano del 1/07 al 30/09; sin servicio en festivos | [Velilla](https://velilladelriocarrion.es/municipio/autobuses/) · [Guardo (antiguo)](https://guardo.org/conoce-guardo/como-llegar-horarios-de-transporte/) | ✅/⚠️ |
| Bilbao–Cervera | Alsa | [omio](https://www.omio.es/autobuses/bilbao/cervera-de-pisuerga) · [Alsa](https://www.alsa.com/pt/estacoes/estacao-palencia) | ⚠️ |
| Tren | Estación de Aguilar de Campoo (línea Palencia–Santander) | conocimiento general | ❓ |
| Carreteras | CL-627 (Aguilar–Cervera–Piedrasluengas); P-210 "Ruta de los Pantanos" (Cervera–Triollo–Velilla); P-217; CL-626 (Tosande); PP-2204 (Golobar); N-621 por San Glorio 🟧 (fuera del bbox) | [publico.es](https://www.publico.es/sociedad/nieve-obliga-cerrar-al-trafico.html) · [Diario de León](https://www.diariodeleon.es/leon/provincia/210109/736160/diecisiete-carreteras-provincia-afectadas-nieve-siete-cadenas-intransitable.html) · [DGT](https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/nota_prensa/20251119-Imprescindible-consultar-el-estado-de-vialidad-de-las-carreteras-antes-de-realizar-desplazamientos/NP-AVISO-DGT-NIEVE.pdf) · [W 15111234](https://es.wikiloc.com/rutas-alpinismo/pico-valdecebollas-desde-el-refugio-del-golobar-15111234) | ⚠️ |
| Vialidad invernal | San Glorio: cadenas frecuentes y prohibido a camiones; denominación discrepante (N-621 / LE-621 / N-625, [Wikipedia](https://Www.Wikipedia.org/wiki/San_Glorio)). Estado en tiempo real en infocar.dgt.es / nap.dgt.es ❓ | ver arriba | ⚠️ |

---

## 10. Meteorología y aludes: ninguna zona AEMET cubre Fuentes Carrionas

| Servicio | Enlace | Notas | Conf. |
|---|---|---|---|
| Predicción de montaña "Picos de Europa" (peu1), la zona más próxima | [AEMET peu1](https://www.aemet.es/es/eltiempo/prediccion/montana?w=&p=peu1) · días siguientes con ?w=1…5&p=peu1 · XML `/xml/montana/AAAAMMDD_predmmon_peu1.xml` ([ejemplo](https://www.aemet.es/xml/montana/20261121_predmmon_peu1.xml)) · [boletín ampliado](https://www.aemet.es/es/eltiempo/prediccion/montana/boletin_montana/ampliacion) | No hay zona específica de la Montaña Palentina. No consta que peu1 incluya la vertiente palentina | ✅ |
| Boletín de aludes **Sierras del Cordel y Peña Labra (Alto Campoo)** | [PDF fijo](https://www.aemet.es/documentos/es/eltiempo/prediccion/montana/boletin_peligro_aludes/BPA_sierra_Cordel_PLabra.pdf) | El más pertinente para el sector oriental (Peña Labra, Tres Mares, Valdecebollas). Campaña 2025-26 cerrada el 9-4-2026; la 2026-27 no había empezado el 21-11-2026 | ✅ |
| Boletín de aludes Picos de Europa | [PDF fijo](https://www.aemet.es/documentos/es/eltiempo/prediccion/montana/boletin_peligro_aludes/BPA_PN_Picos_Europa.pdf) | Aproximación para Curavacas y Espigüete. Campaña cerrada el 20-4-2026 | ✅ |
| Página de aludes y escala de peligro | [Boletines](https://www.aemet.es/es/eltiempo/prediccion/montana/boletin_peligro_aludes) · [Escala](https://www.aemet.es/es/conocermas/montana/detalles/escala_peligro_aludes) · [servicios de montaña](https://www.aemet.es/es/conocermas/montana/detalles/serv_meteo) | Los PDF se sobrescriben en la misma URL, así que la app puede enlazarlos de forma fija | ✅ |
| Predicción municipal | [Cervera id34056](https://www.aemet.es/es/eltiempo/prediccion/municipios/cervera-de-pisuerga-id34056) · [Velilla id34199](https://www.aemet.es/es/eltiempo/prediccion/municipios/velilla-del-rio-carrion-id34199) · [Aguilar id34004](https://www.aemet.es/es/eltiempo/prediccion/municipios/aguilar-de-campoo-id34004) · [Brañosera id34036](https://www.aemet.es/gl/eltiempo/prediccion/municipios/branosera-id34036) | La Casa del Parque usa la de Cervera | ✅ |
| Clima (contexto) | La vertiente palentina es más continental; esquí de montaña y raquetas de diciembre a abril en los circos | [Picuco](https://www.picuco.com/es-es/regions/parque-natural-de-las-fuentes-carrionas-y-fuente-cobre-monta/) | ⚠️ |

**Guía invernal.** La guía "Montañismo invernal en la Montaña Palentina" (262 descensos, 70 rutas y 12 travesías en 18 sectores) aparece citada con una URL de la Diputación ([PDF](https://www.diputaciondepalencia.es/system/files/publicacion-pdf/20171220/guia_de_montanismo_invernal_en_la_montana_palentina.pdf)) ⚠️. Sin embargo, una búsqueda posterior en el buscador interno de la Diputación y en palenciaturismo **no la localizó** ([buscador](https://www.diputaciondepalencia.es/buscar?search_api_fulltext=esqu%C3%AD+de+monta%C3%B1a)). Las notas se contradicen: el PDF no se ha abierto ❓. Otras referencias invernales:

- Esquí de travesía desde Brañosera ([Wikiloc](https://www.wikiloc.com/trails/back-country-skiing/spain/castille-and-leon/branosera)).
- Raquetas: [Guías Zona Centro](https://www.guiaszonacentro.com/montana-palentina-fin-de-semana-con-raquetas-de-nieve/), [12 rutas de Luis Crespo](https://www.luiscrespofernandez.com/post/raquetasnievepalencia) y [fclm 2016](https://www.fclm.com/2016/02/23/las-raquetas-de-nieve-y-el-esqui-aterrizan-en-la-montana-palentina/).
- [Desnivel](https://www.desnivel.com/alpinismo/la-bella-desconocida-montana-palentina-invernal/).

La estación de San Glorio nunca se construyó, por una sentencia del Tribunal Constitucional ([Wikipedia](https://es.wikipedia.org/wiki/Estaci%C3%B3n_de_esqu%C3%AD_de_San_Glorio)) ⚠️. La antigua estación de Brañosera/Valdecebollas está cerrada; solo queda el aparcamiento ⚠️.

---

## 11. Normativa: el PORN prohíbe acampar y volar por debajo de 1.000 m, y el PUP concreta perros, drones y grupos

**Textos vigentes** ✅:

- **Ley 4/2000**, de 27 de junio, de declaración del parque: BOCyL nº 129 del 05-07-2000 y BOE nº 169 del 15-07-2000, BOE-A-2000-13439 ([BOCyL](https://bocyl.jcyl.es/boletines/2000/07/05/pdf/BOCYL-D-05072000-1.pdf); [BOE consolidado](https://www.boe.es/buscar/act.php?id=BOE-A-2000-13439); [ELI](https://www.boe.es/eli/es-cl/l/2000/06/27/4)).
- **Decreto 140/1998**, de 16 de julio, del PORN: BOCyL nº 137 del 21-07-1998, con corrección de errores del 11-09-1998 ([BOCyL PDF](https://bocyl.jcyl.es/boletines/1998/07/21/pdf/BOCYL-D-21071998-7.pdf); [HTML](https://bocyl.jcyl.es/html/1998/07/21/html/BOCYL-D-21071998-7.do); [.doc Fundación](https://patrimonionatural.org/ficheros/01005190825350carrionas3doc190510_082535.doc)).
- Cambio de nombre a «Montaña Palentina» por la disposición final 4.ª de la **Ley 4/2020** ([BOE-A-2021-908](https://boe.es//boe/dias/2021/01/22/pdfs/BOE-A-2021-908.pdf)) ⚠️.
- Marco general: **Ley 4/2015** del Patrimonio Natural de CyL ([BOE-A-2015-4103](https://boe.es/buscar/act.php?id=BOE-A-2015-4103)) ⚠️.
- Posible modificación por la Ley 5/2010 ([BOE-A-2010-9353](https://boe.es/boe/dias/2010/06/14/pdfs/BOE-A-2010-9353.pdf)), sin comprobar ❓.
- Superficie: ~78.360 ha ([Spain.info](https://www.spain.info/es/naturaleza/parque-natural-fuentes-carrionas-fuente-cobre-montana-palentina/)) ⚠️.
- ZEC ES4140011 ([formulario](https://rednatura.jcyl.es/natura2000/LIC/Formularios%20oficiales/PDF%20LIC%20resumen/ES4140011.pdf)) ✅. Que la ZEPA tenga el mismo código ❓.

| Norma / artículo | Contenido | Conf. |
|---|---|---|
| Ley 4/2000 art. 3 | 10 municipios: Velilla del Río Carrión, Aguilar de Campoo, San Cebrián de Mudá, Cervera de Pisuerga, Triollo, Polentinos, Brañosera, La Pernía, Castrejón de la Peña y Dehesa de Montejo | ✅ |
| Ley 4/2000 art. 4 | Régimen: Ley 8/1991, el PORN y sus instrumentos de desarrollo | ✅ |
| PORN art. 37 | Zonas de Reserva: R1 Curavacas–Altos del Calderón–Laguna de Fuentes Carrionas; R2 Peña Redonda; R3 Milares; R4 Montejerino; R5 Polentinos; R6 Peña del Abismo; R7 Peña de las Agujas | ✅ |
| PORN art. 39 | Zonas de Uso Limitado A: 1 Cabecera de Resoba; 2 Tañuga–Piedrasluengas; 3 Redondo–Castillería; 4 Sierra de Corisa y Peña Cilda; 5 Tejeda de Tosande | ✅ |
| PORN art. 45.1 | Prohibido hacer fuego salvo en lugares y formas autorizados | ✅ |
| PORN art. 45.2 / 52.1 | Prohibido abandonar residuos y arrojar, enterrar o incinerar basuras fuera de zonas habilitadas | ✅ |
| PORN art. 45.4 | Prohibido perseguir o capturar fauna no cinegética | ✅ |
| **PORN art. 45.6** | **Prohibida la acampada fuera de los lugares señalados al efecto** | ✅ |
| PORN art. 45.7 / 54.A | Prohibido recolectar flora catalogada amenazada; la Administración puede regular otras especies | ✅ |
| PORN art. 45.8 | Vehículos a motor (el texto dice "en los lugares destinados", probable errata por "no destinados") | ✅ (errata) |
| PORN art. 45.9 | Prohibido introducir especies no autóctonas | ✅ |
| **PORN art. 53** | Vehículos a motor prohibidos en Reserva y ULA (salvo usos agrosilvoganaderos, de gestión o autorizados); en ULB, prohibidos fuera de pistas | ✅ |
| PORN art. 54.B | Quema de vegetación prohibida en Reserva y ULA; en ULB requiere autorización | ✅ |
| PORN art. 54.C.5 | Prohibido cortar árboles y sacar leña en el enebral de Peña Lampa y en la Tejeda de Tosande | ✅ |
| PORN art. 56.1 | Prohibidos cepos, lazos, reclamos y redes | ✅ |
| **PORN art. 62** | En Reserva y ULA el acceso puede restringirse. Uso público por pistas, sendas o vías señalizadas, evitando las áreas críticas del oso. 62.B: se puede restringir el acceso a cuevas | ✅ |
| PORN art. 63.1 | Prohibidas las pruebas deportivas con vehículos motorizados | ✅ |
| **PORN art. 63.2** | **Prohibido sobrevolar a menos de 1.000 m** sobre el terreno, salvo salvamento o gestión. En la práctica cubre los drones | ✅ |
| PORN art. 63.3 | Las demás competiciones necesitan autorización; puede haber normas para montañismo, escalada, BTT, caballo y nieve | ✅ |
| PORN art. 63.4 | Prohibidas las nuevas infraestructuras de esquí alpino | ✅ |
| PUP 2018 (documento de trabajo v1.2) §6.2.1 | Acampada, pernocta y vivac **prohibidos** fuera de las zonas de uso general. Vivac solo autorizable junto a refugios o vías de escalada de las principales cumbres. **No hay zonas de acampada ni campings en el parque** | ✅ (valor orientativo) |
| PUP §6.2.4 | **Drones sometidos a autorización.** No se autoriza ninguna actividad recreativa con aeronave de motor. Vuelo libre autorizable fuera de Reserva; Castrejón de la Peña exenta | ✅ |
| PUP §6.2.6 | Bici solo por carreteras, pistas y caminos aptos para vehículos; puede prohibirse en pistas con mucho uso peatonal | ✅ |
| PUP §6.2.7 | Prohibido el tránsito turístico a caballo por los senderos de la red, salvo tramos de pista | ✅ |
| PUP §6.2.9 | Cueva del Cobre de libre acceso en su colector principal | ✅ |
| PUP §6.2.12 | Fotografía de fauna: sin autorización no se permiten esperas, hides, cebado, reclamos, focos ni fotografía de nidos | ✅ |
| PUP §6.2.16 | Autorización obligatoria para grupos de **más de 120 personas, 30 bicicletas o caballerías, 10 vehículos o 5 embarcaciones**, y para cualquier prueba deportiva | ✅ |
| PUP §6.2.17 | ULA Tañuga–Piedrasluengas restringida al oeste de Casavegas y en el Monte Peñota. **ZR2 Peña Redonda, ZR3 Milares, ZR4 Montejerino y ZR5 Polentinos con acceso restringido**, con excepciones: GR-1 y pistas de Rabanal y San Martín de los Herreros, balizado de Peña Redonda; en ZR4, la pista Lores–Pineda por Secarro del 1-oct al 15-ago; en ZR5, el camino de San Salvador al Cueto del 1-jul al 30-sep. ZR1, ZR6 y ZR7 sin limitaciones | ✅ |
| PUP (perros) | Controlados siempre; **atados** en aparcamientos, picnic, refugios, vivac, miradores, **sendas interpretativas y todas las Zonas de Reserva y ULA transitables** | ✅ |
| Plano 2025 (consejos) | No acampar; no hacer fuego; perro controlado; no arrancar plantas; cerrar las portillas; no beber de los arroyos | ✅ |
| Folletos de sendas | Pistas y sendas señalizadas; a pie (caballo o BTT solo en algunos tramos); vehículos solo por asfalto | ✅ ([Velilla](https://patrimonionatural.org/ficheros/Pinar-Velilla.pdf), [Gigante](https://patrimonionatural.org/ficheros/5e7112e99cc33_Folleto-Senda-del-Gigante-del-Valle-Estrecho.pdf)) |
| RD 1180/2018 art. 19 | Drones sobre espacios protegidos: autorización previa del gestor | ⚠️ ([Aragón](https://www.aragon.es/-/vuelo-drones-espacios-naturales-protegidos)) |
| Camino Natural Puertos de Pineda | Regulación y permisos de vehículos | ✅ existencia ([página del parque](https://patrimonionatural.org/espacios-naturales/parque-natural/parque-natural-montana-palentina)) / ❓ contenido |

Fuentes del PORN: [BOCyL](https://bocyl.jcyl.es/boletines/1998/07/21/pdf/BOCYL-D-21071998-7.pdf). Fuentes del PUP: [PUP 2018](https://patrimonionatural.org/ficheros/5b0be95e3407c_Parque-Natural-Montana-Palentina_Plan-Uso-Publico-vers_2018.pdf). **No consta ningún PRUG aprobado** ni la versión definitiva del PUP: las reglas del PUP son de gestión, no norma publicada. Las setas no tienen regulación específica en el PORN más allá del art. 54.A ❓.

Mensaje recomendado para la app: «Acampada libre y vivac no permitidos dentro del parque (PORN art. 45.6); el vivac solo es autorizable. Drones: requieren autorización (PORN art. 63.2, PUP 6.2.4, normativa AESA). Perros atados en sendas interpretativas y en zonas de Reserva y Uso Limitado.»

---

## 12. Fauna, caza y cierres: los cierres cambian cada semana

**Cierres de sendas.** El PDF oficial se actualiza **semanalmente** y el nombre del fichero cambia en cada versión: hay que enlazar la **página de la Casa del Parque**, no un PDF fijo ([Casa del Parque](https://patrimonionatural.org/casas-del-parque/casas-del-parque/casa-del-parque-de-fuentes-carrionas-y-fuente-cobre-montana-palentina); [senderos](https://patrimonionatural.org/senderos)). El PDF no indica horarios ni coordenadas de los tramos.

| Versión | Contenido | Fuente |
|---|---|---|
| **20-11-2026 (vigente)** | Por cacería: Mazobre el 21/11; Ursi el 21 y 22/11; GR-1 San Felices–Herreruela el 22/11; Camino Natural de Pineda (accesos de Resoba y Vidrieros) el 22/11; Tosande el 12/12/2026 y el 28/02/2027 | [PDF](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural_20-11-2026-20261120-105650.pdf) ✅ |
| 04-06-2026 | Senda del Oso, Cervera–Arbejal: cierres intermitentes por obras "hasta nuevo aviso" | [PDF](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural_4-6-2026-20260604-121346.pdf) ✅ |
| 16-04-2026 | Caza y otros motivos, incluida la Senda del Oso | [PDF](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural_2026_4_16-20260417-104844.pdf) ✅ |
| 06-03-2026 | Venganza del Conde, cacería el 7-3 | [PDF](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural-20260306-114659.pdf) ✅ |
| 14-11-2025 | Senda del Oso, cacería el 16-11-2025. Según un fragmento del buscador, también **Tosande el 13-12-2025 y el 22-02-2026** ⚠️ | [PDF](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural_2025_11_14-20251113-155300.pdf) ✅ |
| 2024 | Ruta de Herreros cerrada por obras y señalización | [jul-2024](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural-20240705-101959.pdf) · [nov-2024](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural_2024_11_29-20241129-102558.pdf) ✅ |

**Otros cierres (fuera del PDF de la Junta):**

| Elemento | Estado | Fecha | Fuente |
|---|---|---|---|
| **Cueva de los Franceses** (Revilla de Pomar) | **Cerrada temporalmente por obras**. Afecta a `mp-covalagua-integral` y `mp-franceses-lobos`: el sendero exterior sigue siendo practicable, pero la visita no ✅ | 21-11-2026 (fecha de inicio y de reapertura desconocidas) | [palenciaturismo](https://palenciaturismo.es/visitar/lugares-interes/cueva-franceses) ✅ |
| Carretera del Golobar (PP-2203) | Sin mantenimiento; ha sufrido desprendimientos; cortada a menudo por nieve | — | Wikipedia (El Golobar) ⚠️ |

**Restricciones por oso:**

- **Curavacas.** Resolución del Servicio Territorial que limita el tránsito fuera de senderos y vías, prohíbe perros sueltos y restringe el acceso **por encima de 1.800 m en la cara norte**. Se fijó hasta el 30-jun y se amplió hasta el 30-jul por tres familias de osos; año sin confirmar ([Palencia en la Red](https://www.palenciaenlared.es/establecen-limitaciones-temporales-de-transito-en-el-curavacas-por-la-presencia-de-osos/); [Valderrueda](https://www.diariodevalderrueda.es/texto-diario/mostrar/5917422/restricciones-pico-curavacas-proteger-tres-familias-osos); [ampliación](https://www.diariodevalderrueda.es/texto-diario/mostrar/5938807/ampliadas-mes-restricciones-curavacas-tres-familias-osos)) ⚠️.
- **Peña Escrita**, 2022: acceso regulado hasta el 15-jun ([ileon](https://ileon.eldiario.es/tierra-verde/presencia-familias-oso-pardo-lleva-junta-impedir-visitantes-pena-escrita-montana-palentina_1_9538826.html); [Soria Noticias](https://sorianoticias.com/noticia/2022-04-27-la-junta-regula-el-acceso-al-parque-natural-de-la-montana-palentina-para-proteger-dos-grupos-familiares-de-osos-89142)) ⚠️.
- **Reserva y ULA de La Pernía, Polentinos y Cervera**: limitación del **1-feb al 31-may** ([Wikipedia](https://es.wikipedia.org/wiki/Parque_natural_Monta%C3%B1a_Palentina)) ⚠️.

En la app conviene modelarlas como **capas temporales** actualizables cada año.

**Oso pardo:**

- La Montaña Palentina pertenece a la subpoblación **oriental**, estimada en ~40–50 individuos ([Faunatura](https://www.faunatura.com/oso-pardo-cantabrico-donde-vive-y-por-que-su-recuperacion-es-una-buena-noticia.html)). Otras fuentes dan 120 ([Terabithia](https://terabithia.es/renacer-en-la-montana-aumenta-el-impulso-del-oso-pardo-a-la-economia-local-en-2025/)) o 30–40 ([Picuco](https://www.picuco.com/es-es/regions/parque-natural-de-las-fuentes-carrionas-y-fuente-cobre-monta/)) ⚠️.
- En 2025 se contaron **11 osas con 18 crías** en la oriental ([Infobierzo](https://www.infobierzo.com/provincia/danos-oso-pardo-provincia-leon-2025_1035407_102.html)) ⚠️. Población cantábrica total: ~370 o más de 400 ([FOP ficha](https://fundacionosopardo.org/wp-content/uploads/2025/04/ficha1_2025_ESP-1.pdf); [Asturias Mundial](https://www.asturiasmundial.com/noticia/144945/oso-pardo-podria-superar-ya-400-ejemplares-asturias-necesita-nuevo-censo-conocer-poblacion-real/)).
- Nuevo **Protocolo de intervención con osos cantábricos** del 22-06-2026 ([MITECO](https://www.miteco.gob.es/content/dam/miteco/es/biodiversidad/temas/conservacion-de-especies/esp-prot-especial/ProtocoloIntervencion_osos_cantabricos_aprobadoCSMA_20260622.pdf), no leído).
- Pautas ante un encuentro ([FOP](https://fundacionosopardo.org/what-to-do-if-encountering-a-bear/); [infografía](https://fundacionosopardo.org/wp-content/uploads/2023/10/Infografia_AEFONA-FOP_enviada.pdf); [Quercus](https://www.revistaquercus.es/adjuntos/7669/DESCARGABLE_OSOS_EXT2.pdf)) ✅: observar de lejos; ir por sendas señalizadas; alejarse despacio y en silencio; no correr nunca; ante una carga, mantener la posición; no acercarse a carroñas; no ponerse nunca entre una osa y sus crías.

**Otra fauna** ❓, de memoria y sin verificar: lobo, urogallo (cantaderos de abril a junio), rebeco en las grandes cumbres y águila real. La **berrea** va aproximadamente del 15-sep al 15-oct, con Ruesga como zona recomendada ([siempredepaso](https://siempredepaso.es/disfruta-de-la-berrea-en-la-montana-palentina); [Patrimonio Natural](https://patrimonionatural.org/noticias/noticia/la-berrea-en-fuentes-carrionas-y-en-la-casa-del-parque-de-cervera-de-pisuerga); [Valderrueda](https://www.diariodevalderrueda.es/texto-diario/mostrar/856487/asi-ve-berrea-fuentes-carrionas-montana-palentina)) ⚠️. Mastines y ganado en los puertos en verano: pauta general, sin fuente local ❓.

**Caza: Reserva Regional de Caza Fuentes Carrionas.**

- Gestión técnica: Avda. Casado del Alisal 27, Palencia, tel. **979 715 515** ([Cesefor](https://dev.subastasdecaza.cesefor.com/en/node/832)) ⚠️.
- Último plan de caza localizado: 2021-22, desactualizado ([PDF](https://dev.subastasdecaza.cesefor.com/sites/default/files/plan_de_caza_rrc_2021_2022.pdf)).
- **No hay calendario público de batidas**: la fuente práctica es el PDF semanal de cierres. Las batidas suelen ir de octubre a febrero, en fines de semana ❓.

---

## 13. Carreras de trail

| Prueba | Fecha / lugar | Distancias | Fuente | Conf. |
|---|---|---|---|---|
| **Ultra Montaña Palentina 2026** | 12-09-2026, Camporredondo de Alba | Ultra 65 km / +4.400; Maratón 44 km / +3.400 (11 h máximo); Trail Fuentes Carrionas 21 km; Start y Young Trail 6 km. 500 plazas agotadas | [COPE](https://www.cope.es/emisoras/castilla-y-leon/palencia-provincia/palencia/noticias/ultra-montana-palentina-agota-500-plazas-edicion-2026-20260905_3430677.html) · [Valderrueda](https://www.diariodevalderrueda.es/texto-diario/mostrar/6003539/cuenta-atras-retadora-ultra-montana-palentina-2026) · [TrailRunTemple](https://trailruntemple.com/carreras/espana/castilla-y-leon/ultra-montana-palentina/inscripcion/) | ⚠️ (VerticalEspaña da 80 km / +9.000 en agosto: **discrepancia**, [fuente](https://verticalespana.com/trail-running/)). **Recorrido oficial y web no localizados** |
| Trail Pico Almonga | 03-10, Cervera | 10,5 km / +600 | [DaleDeporte](https://www.daledeporte.es/events/palencia) · [La Bolsa del Corredor](https://www.labolsadelcorredor.com/calendario-carreras-trail-running-2026/) | ⚠️ |
| Trail El Calero | 03-10, Barruelo | 25 km / +1.000 | ídem | ⚠️ |
| Trail Camporredondo | 15-09 (año sin confirmar) | — | ídem | ❓ |
| Campeonato de España de carreras por montaña (RFEA) | 02-05-2026: vertical Barruelo–Brañosera; 03-05-2026: clásicas en Aguilar | — | ídem | ⚠️ |

No se encontró ningún "Desafío Curavacas" ni un "Maratón de Montaña Palentina" independiente. La guía de la Diputación marca para cada ruta si es apta para carrera por montaña y raquetas, pero son iconos gráficos y no se transcribieron.

---

## 14. Cartografía y datos abiertos para el 3D

| Capa | Producto | Licencia / atribución | Enlace | Conf. |
|---|---|---|---|---|
| Terreno de alta resolución | **MDT02** (2.ª cobertura LiDAR PNOA, 2 m) para cumbres (Curavacas, Espigüete, Peña Prieta) | CC BY 4.0 (la presentación de 2019 decía CC BY 3.0 ES: discrepancia de versión) | [Centro de Descargas MDT02](https://centrodedescargas.cnig.es/CentroDescargas/modelo-digital-terreno-mdt02-segunda-cobertura) · [EEA](https://cis2.eea.europa.eu/data/912) · [JIIDE 2019](https://idee.es/resources/presentaciones/JIIDE19/dia_24/AUDITORIO_PRINCIPAL/1.Sesion_1_Nuevos_Desarrollos/2_MapaLidar_JIIDE2019.pdf) · [datos.gob.es](https://datos.gob.es/es/aplicaciones/centro-de-descargas) | ✅/⚠️ |
| Terreno general | **MDT05** (5 m, LiDAR 1.ª cobertura). MDT25 para el resto | "MDT05 CC BY 4.0 SCNE" | [INSPIRE spaignMDT05](https://inspire-geoportal.ec.europa.eu/srv/api/records/spaignMDT05) · [WCS MDT](https://inspire-geoportal.ec.europa.eu/srv/api/records/spaignwcs_mdt) | ✅ |
| Superficie / vegetación | MDS05; Mapa LiDAR 2,5 m; nubes de puntos PNOA-LiDAR | CC BY 4.0 | [MDS](https://idee.es/csw-inspire-idee/static/api/records/spaignMDS) · [Mapa LiDAR](https://datos.gob.es/es/catalogo/e00125901-spaign-mapa-lidar) · [Nubes de puntos](https://pnoa.ign.es/resources/archivos/pdf/Procesado_distribucion_nubes_puntos_proyecto_PNOA-LiDAR.pdf) | ✅ |
| Textura | Ortofoto PNOA (WMTS `https://www.ign.es/wmts/pnoa-ma`) | CC BY 4.0 | — | ❓ URL no verificada |
| MDT autonómico | MDT de Castilla y León (IDECyL) | ❓ | [IDECyL](https://idecyl.jcyl.es/geonetwork/srv/api/records/SPAGOBCYLCITDTSELMDT0811) | ⚠️ |
| Senderos homologados | Dataset "Senderos de la FEDME" (GR/PR/SL; GPX, KML y SHP por etapa), CNIG | Condiciones IGN; datos aportados por la FEDME | [IDEE FEDME](https://www.idee.es/csw-inspire-idee/srv/api/records/spaignFEDME) | ✅ existencia / ❓ si incluye los PR-P palentinos |
| Caminos Naturales | GPX por etapa (Románico Palentino, Pineda, Lebaniego) | ❓ licencia | [IDEE CNT](https://idee.es/csw-inspire-idee/static/api/records/spaignCNT) | ✅/❓ |
| Equipamientos de uso público | Capa oficial de aparcamientos, miradores y áreas recreativas (soyecoturista / IDECyL). ZNE con "otras restricciones" | ❓ | [soyecoturista](https://soyecoturista.com/en/actividad/equipamientos-de-uso-publico) · [IDECyL ZNE](https://idecyl.jcyl.es:443/geonetwork/docs/api/records/SPAGOBCYLMNADTSPSZNE) | ⚠️ (URL del servicio sin localizar) |
| POI | **OSM**: consulta `overpass_query_poi.overpassql` lista (shelter, alpine/wilderness_hut, viewpoint, camp_site, hostel, information, museum, picnic, spring, drinking_water, parking, salud, bus, helipad, landing_site, railway station; bbox 42.75,−4.85,43.05,−4.05) | ODbL 1.0, «© OpenStreetMap contributors» | Ejecutar: `curl --data-urlencode data@overpass_query_poi.overpassql https://overpass-api.de/api/interpreter -o osm_poi.json` · [OSM wiki senderismo ES](https://wiki.openstreetmap.org/wiki/ES:Espa%C3%B1a/Senderismo) | ✅ consulta / ❓ **no ejecutada**: en la v2 tanto overpass-api.de como download.geofabrik.de dieron *connection reset* desde el entorno. Alternativa: subir `castilla-y-leon-latest.osm.pbf` o ejecutar el `.overpassql` en local |
| Relaciones de senderos en OSM | Waymarked Trails | ODbL | https://hiking.waymarkedtrails.org/#search?query=GR%201 (URL construida) | ❓ |
| Hojas IGN | MTN50 0081, 0082, 0106, 0107, 0132 y 0133. MTN25: 81, 106, 107, 132 y 133 con subdivisiones | — | — | ❓ verificar en el visor CNIG |
| Datos abiertos JCyL | datosabiertos.jcyl.es: **inaccesible** (connection reset). Licencia habitual IGCYL-NC (sin uso comercial) ❓ | — | — | ❓ |
| Otro dataset "senderos" | datos.gob.es a17002943 (**no es** de CyL) | — | [datos.gob.es](https://datos.gob.es/es/catalogo/a17002943-senderos) | ⚠️ |

---

## 15. Licencias de reutilización

| Fuente | ¿Se puede ingerir? | Condición | Fuente | Conf. |
|---|---|---|---|---|
| **IGN / CNIG** (MDT, PNOA, BTN, MTN) | **Sí** | CC BY 4.0 (Orden FOM/2807/2015). Atribución «<producto> <fecha> CC-BY 4.0 <productor>» y, en obras derivadas, «Obra derivada de…» | [Condiciones IGN](https://www.ign.es/resources/licencia/Condiciones_licenciaUso_IGN.pdf) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.es) | ✅ |
| **OpenStreetMap** | **Sí** | ODbL 1.0: atribución y share-alike sobre la base de datos derivada | conocimiento general | ❓ (estable) |
| **Tracks propios** grabados por el equipo | **Sí** | Licencia propia | — | — |
| Senderos FEDME (CNIG) y Caminos Naturales (MAPA) | Probablemente sí | Revisar antes las condiciones IGN y MAPA que se enlazan | [IDEE FEDME](https://www.idee.es/csw-inspire-idee/srv/api/records/spaignFEDME) | ❓ |
| Datos fácticos (coordenadas de inicio, altitudes, cifras km/D+) | Sí, como hechos | Reescribir; no copiar descripciones | inferencia | ⚠️ |
| **Wikiloc** | **No** (solo enlazar) | Sus condiciones prohíben obtener contenido por medios no previstos y usar el sitio sin autorización | [Términos ES](https://es.wikiloc.com/wikiloc/terms_es.html) · [EN](https://www.wikiloc.com/wikiloc/terms_en.html) | ✅ |
| **Mendikat** | Solo enlazar (tracks y datos de usuarios) | Términos no revisados | — | ❓ |
| Komoot, AllTrails, Terranostrum, SummitPost, blogs | **No** (solo enlazar) | Contenido de terceros | inferencia | ⚠️ |
| **Guía Diputación / La Pedrera Pindia** (40 ascensiones, BTT) | **No** para textos, fotos, croquis y GPX | "Ejemplar digital gratuito de libre distribución… Queda prohibida la venta". ©La Pedrera Pindia. Sin licencia CC. Se puede redistribuir el PDF íntegro y gratis; extraer contenido requiere permiso | [Guía p.3](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf) | ✅ |
| `waypoints_guia_diputacion.json` | Uso interno y de validación | Son coordenadas fácticas, pero extraídas en bloque de una obra protegida. Para republicarlas tal cual, pedir permiso (inferencia) | — | ⚠️ |
| Guía alpina Curavacas y Espigüete | Reproducción parcial **sin ánimo de lucro** citando autor; una app comercial necesita permiso | "© Reservados todos los derechos. Autorizada la reproducción parcial… sin ánimo de lucro" | [PDF](https://www.diputaciondepalencia.es/system/files/2024-05/guia_de_curavacas_y_espiguete-interactivo.pdf) | ✅ |
| PDF y folletos de la Junta (patrimonionatural.org) | Enlazar; no reutilizar mapas | Sin licencia abierta localizada; aviso legal no revisado | — | ❓ |
| Libro y mapa "Montaña Palentina" 2026 (palenciaturismo) | Enlazar | Derechos de autor (Diputación / Juan PIXELECTA); declara expresamente que no incluye tracks. **Los enlaces `2026-05` devuelven 403**: usar los de `2026-06` | [Libro ES](https://palenciaturismo.es/system/files/2026-05/LIBRO%20MONTA%C3%91A%20PALENTINA%20%28versi%C3%B3n%20espa%C3%B1ol%29.pdf) · [EN](https://palenciaturismo.es/system/files/2026-05/LIBRO%20MONTAN%CC%83A%20PALENTINA%20%28versio%CC%81n%20Ingle%CC%81s%29.pdf) · [Libro 2026-06](https://www.palenciaturismo.es/system/files/2026-06/LIBRO%20MONTA%C3%91A%20PALENTINA%20%28versi%C3%B3n%20espa%C3%B1ol%29%20%281%29.pdf) · [Mapa interactivo](https://www.palenciaturismo.es/system/files/2026-06/MAPA%20MONTA%C3%91A%20PALENTINA%20%28formato%20interactivo%20digital%29%20INTERNET_0.pdf) | ✅ |
| Tracks de carreras | Pedir permiso a la organización | — | inferencia | ❓ |
| GPX de palenciaturismo (Ribero Pintado, Doncellas del Hoyal) | Enlazar; pedir permiso para ingerir | Descargables desde la ficha, sin licencia declarada | [GPX Ribero Pintado](https://palenciaturismo.es/system/files/2020-06/santa-maria-de-redondo-ribero-pintado.gpx) · [GPX Doncellas](https://palenciaturismo.es/system/files/2022-10/senda-de-las-doncellas-del-hoyal_0.gpx) | ⚠️ |
| GPX y fichas de Terranostrum (111 GPX) | **No** redistribuir; enlazar | © Terranostrum o de la entidad citada en cada ficha. Las estadísticas (cálculo propio) de `terranostrum_gpx_estadisticas.json` son hechos derivados para contraste | — | ⚠️ |
| refugioslibres.com | Hechos de las fichas (nombre, plazas, servicios); no copiar textos | Coordenadas públicas solo aproximadas; reseñas poco fiables | — | ⚠️ |
| Wikipedia | Hechos, sí; texto literal solo con atribución y misma licencia | CC BY-SA 4.0. En este documento todo está reformulado | — | ✅ |

---

## Conclusión

El cuello de botella del dominio no es la falta de rutas, sino la **falta de geometría reutilizable**. Las cifras oficiales están, y el catálogo (13 sendas oficiales, 40 ascensiones de la Diputación y, desde la v2, más de 60 rutas a pie y en bici de Terranostrum y palenciaturismo) cubre de sobra la Montaña Palentina. Pero las únicas trazas descargables están en plataformas cuyos términos impiden ingerirlas (Wikiloc, editorial privada) o tienen un alcance parcial (Caminos Naturales, quizá FEDME). La decisión estratégica para la app es invertir en **grabar o digitalizar tracks propios sobre MDT02/PNOA**, empezando por las 13 sendas oficiales y las 5 ascensiones estrella: Curavacas, Espigüete, Peña Prieta, Valdecebollas y Peña Labra. El resto debe vivir como enlaces.

El segundo hallazgo es que **la información más valiosa para el usuario es la más volátil**: cierres semanales por cacería, restricciones por osas con crías que cambian cada año, campañas de aludes y una Casa del Parque cerrada dos meses en invierno. Un dominio que solo publique rutas estáticas quedará desactualizado en semanas. Por eso la arquitectura debe tratar normativa, cierres y meteo como **capas fechadas con fuente oficial enlazada**, y marcar con honestidad (✅/⚠️/❓) lo que todavía no se ha verificado sobre el terreno.

---

## 16. Fichas de rutas (un bloque autocontenido por ruta)

Cada ficha tiene la misma estructura para que la app pueda ingerirla sin volver a las fuentes. Reglas de lectura:

- **Identificador:** el slug `mp-…` es estable.
- **Confianza:** ✅/⚠️/❓, como en el resto del documento.
- **Coordenadas:** WGS84 en grados decimales.
- **Waypoints de la guía de la Diputación:** salen de `waypoints_guia_diputacion.json`. Ya están **filtrados los 25 erróneos** (ruta 31 entera, 06-WP7 y 36-WP25).
- **D−:** en rutas circulares e ida-vuelta es igual al D+.
- **Enlaces:** cada ficha lleva como máximo 1–2. El resto de URLs está en el anexo **"Fuentes"**.
- **Licencia:** se refiere a la fuente de la que procede el contenido de la ficha. Los hechos (cifras, coordenadas) se pueden usar; los textos, fotos y tracks de terceros, no.

### 16.1 Red oficial del Parque Natural (Junta de Castilla y León)

#### mp-of-ursi · Senda del escultor "Ursi" (PRC-P 2)
- **Zona / municipio · Provincia:** Valle de Santullán (Barruelo de Santullán / Brañosera) · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular ⚠️ · 11,6 km (plano 2025; ficha 11 km) · +370 / −370 m · altitud ❓ · 3 h 40 (plano; ficha 4 h) · media ✅.
- **Inicio · Fin:** coordenada de la ficha oficial: 42.89167, −4.30889 ✅ (zona de Villabellaco). La guía de la Diputación cita otro acceso, el "aparcamiento Senda Ursi, Valle de Santullán": 42.90353, −4.34705 ✅. Probablemente son dos inicios de la misma red ⚠️. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓. **Cierres por cacería el 21 y el 22-11-2026** ✅. Coincide en parte con el GR-1.
- **Agua · Refugios:** sin datos. Cerca de la ruta 36 está el merendero con fuente de la Mina del Calero (42.92842, −4.31267).
- **Waypoints clave:** cruces con la Senda Ursi según la ruta 36 de la Diputación: 42.90621, −4.34347 (1269 m) y "Bifurcación Senda Ursi Villabe[llaco]" 42.89506, −4.30913 (1138 m).
- **Descripción:** senda circular por el valle de Santullán, en la cuenca minera del norte de Palencia. Se recorre entre robledales y jalonan el camino **39 esculturas**: las obras originales del escultor Ursi más tres nuevas de Diego Calleja y Francisco Gómez Antolín. La Junta publica una relación de obras y ubicaciones. Comparte tramos con el GR-1 y con la ascensión a Peña Cildá (ruta 36 de la Diputación), entre escombreras de antiguas minas.
- **Comentarios de usuarios:** no se encontraron.
- **Cifras de contraste (v2):** palenciaturismo 11 km circular / +300 / 3 h 40, moderada, homologada ✅ · Terranostrum 11 km / +300 / 3 h 30, media ⚠️.
- **GPX Terranostrum (cálculo propio):** 11,28 km · +385 m · alt. 1.063–1.380 m · inicio 42.89342, −4.3106 · track cerrado (fin a 6 m del inicio).
- **Inicio canónico (v2):** **Villabellaco, iglesia de San Pedro**, 42.89109, −4.31070 (palenciaturismo) ✅, que coincide con la ficha oficial y con el GPX. Palenciaturismo cita tres accesos: Villabellaco, Valle de Santullán (el aparcamiento de la ruta 36 de la Diputación) y el Santuario del Carmen. Se resuelve así la discrepancia de inicio.
- **Waypoints y contenido (v2):** miradores de Rulaya y La Solana. Palenciaturismo habla de **30 esculturas** frente a las 39 de la ficha de la Junta: discrepancia, probablemente por las obras añadidas ⚠️.
- **Enlaces:** [ficha oficial](https://patrimonionatural.org/senderos/senda-del-escultor-ursi).
- **Licencia · Confianza · Pendiente:** folleto de la Junta sin licencia abierta (solo enlazar) · ✅ cifras e inicio · Pendiente: OCR del folleto 2025 (escaneado), número exacto de esculturas y track propio.

#### mp-of-tosande · Senda de la Tejeda de Tosande (PR-P 3)
- **Zona / municipio · Provincia:** Dehesa de Montejo, valle de Tosande (cerca de Cervera de Pisuerga) · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular ⚠️ · 10 km (plano; ficha 11; Komoot 9,14; MAPA 11) · +400 / −400 m · mín. ~1.150 m, mirador a ~1.404–1.410 m · 3 h 30 (plano; ficha 3 h) · media ✅.
- **Inicio · Fin:** aparcamiento de tierra en la CL-626, a ~6 km de Cervera. Coordenadas: 42.82611, −4.51528 (ficha) ✅ o 42.82578, −4.51656 (guía de la Diputación, 1152 m) ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** la mejor época es el otoño (tejos, robles y hayas en color). Es zona de uso limitado A (ZULA 5): **prohibido salir de la senda**. El tramo mirador–pasarela está restringido del 1-oct a finales de febrero (PUP 2018) ✅. **Cierres por cacería el 12-12-2026 y el 28-02-2027** ✅. El aparcamiento se llena de día y es solo diurno (carteles de prohibido pernoctar). Calor en julio. En agosto de 2025 se registró un corte, posiblemente por riesgo de incendio ⚠️. En la tejeda se prohíbe cortar árboles o sacar leña (PORN art. 54.C.5).
- **Agua · Refugios:** abrevadero en una pradera del valle, 42.8435, −4.54983 (ruta 24 de la Diputación). No es potable garantizado.
- **Waypoints clave** (ruta 24 de la Diputación, que comparte el tramo): aparcamiento 42.82578, −4.51656 · panel informativo de la tejeda 42.8422, −4.55211 (1230 m) · mirador 42.83719, −4.55003 (1404 m) · puente y pista 42.83896, −4.54287.
- **Descripción:** el sendero remonta el valle del arroyo de Tosande desde la carretera. La vegetación pasa del encinar al hayedo y desemboca en la tejeda, una de las mayores concentraciones de tejos de la Península y de Europa occidental, con ejemplares de cientos de años y alguno de más de mil. Una pasarela de madera atraviesa la tejeda para que los visitantes no erosionen el suelo. El mirador, a unos 1.410 m, domina el valle antes de regresar por el lado opuesto. Es el espacio más protegido del parque fuera de las zonas de reserva.
- **Comentarios de usuarios** (2024, Wikiloc ⚠️): "una de las rutas más bonitas e interesantes de la Montaña Palentina"; "espectaculares los tejos y el hayedo, y además es fácil". Un usuario apunta que el cartel dice "Tejal". Hay quejas por masificación ("hace perder su encanto") y por calor en julio. Se recomienda en otoño.
- **Cifras de contraste (v2):** palenciaturismo 10,5 km circular / +300 / 3 h 30, moderada ✅ · Terranostrum 10 km / +400 / 3 h 30, baja-media · escapadarural ~10 km / +400 ⚠️. Inicio palenciaturismo 42.82557, −4.51688.
- **GPX Terranostrum (cálculo propio):** 9,45 km · +429 m · alt. 1.073–1.410 m · inicio 42.82574, −4.51656 · track cerrado (fin a 0 m del inicio).
- **Contexto (v2, Wikipedia y libro 2026, reformulado):** la tejeda ocupa la ladera norte de Peña Oracada (1.818 m), en la sierra de la Peña. Los tejos crecen entre 1.300 y 1.500 m dentro de un hayedo, sobre sustrato paleozoico, y se consideran un bosque relicto del Terciario. Tres ejemplares están en el catálogo regional de árboles singulares y el tejo tiene protección de "atención preferente" (Decreto 63/2007). Hay troncos de hasta 1,5 m de diámetro, y el libro 2026 atribuye al "Árbol rey" más de 1.200 años ⚠️. Pasarelas y mallas protegen el suelo.
- **Avisos (v2):** el PDF de cierres de noviembre de 2025 incluía también cacerías en Tosande el 13-12-2025 y el 22-02-2026 (fragmento ⚠️). Esto refuerza que el corte de agosto de 2025 tuvo otra causa, porque la caza se concentra de octubre a febrero ❓.
- **Enlaces:** [ficha oficial](https://patrimonionatural.org/senderos/senda-de-la-tejeda-de-tosande) · [Wikiloc 141704149](https://es.wikiloc.com/rutas-senderismo/tejeda-de-tosande-desde-el-parking-141704149).
- **Licencia · Confianza · Pendiente:** Junta (enlazar); Wikiloc (solo enlazar) · ✅ · Pendiente: OCR del folleto escaneado, track propio y confirmar el motivo del corte de 2025.

#### mp-of-roblon · Senda del Roblón de Estalaya (PRC-P 4)
- **Zona / municipio · Provincia:** Estalaya (Cervera de Pisuerga) · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular ✅ · 4,6 km (ficha 4,64) · +140 / −140 m (folleto 125) · altitud ❓ · 1 h 30 · baja.
- **Inicio · Fin:** aparcamiento situado a ~2 km por la carretera que sale a la derecha tras el puente de Vañes. Coordenada de la ficha: 42.925, −4.46944 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓. Obras de mantenimiento anunciadas en 2023 ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** solo el inicio.
- **Descripción:** paseo corto y circular hasta el Roblón de Estalaya, un roble monumental, uno de los árboles singulares del parque. Arranca en un aparcamiento del valle, cerca de Vañes, y cruza bosque de robles. Es la única senda oficial con track enlazado expresamente desde la ficha de la Junta. Apta para familias por su longitud y su desnivel (inferencia).
- **Comentarios de usuarios:** no se encontraron.
- **Cifras de contraste (v2):** palenciaturismo 4,6 km circular / +125 / 1 h 30, fácil, homologada ✅ · Terranostrum 4,5 km / +100 / 1 h 30. Inicio palenciaturismo **42.92422, −4.47202**, a ~2 km por la PP-2173 tras el puente de Requejada (la ficha de la Junta dice "puente de Vañes") ✅.
- **GPX Terranostrum (cálculo propio):** 4,51 km · +147 m · alt. 1.079–1.227 m · inicio 42.92417, −4.47207 · track cerrado (fin a 7 m del inicio).
- **El árbol (v2):** roble albar de **17 m de altura y ~10,6 m de perímetro** (palenciaturismo, escapadarural) ✅. Edad discrepante: "más de 500 años" (escapadarural) o "más de 600" (comentario de komoot, 03-04-2026) ❓. El tramo final tiene fuerte pendiente. Hayedo y robledal, muy vistoso en otoño.
- **Enlaces:** [ficha oficial](https://patrimonionatural.org/senderos/senda-del-roblon-de-estalaya) · [track oficial en Wikiloc](https://es.wikiloc.com/rutas-senderismo/senda-del-roblon-de-estalaya-parque-natural-montana-palentina-43488041) ❓.
- **Licencia · Confianza · Pendiente:** Junta / Wikiloc (enlazar) · ✅ · Pendiente: verificar el track oficial y la edad del roble.

#### mp-of-oso · Senda del Oso, Cervera–Arbejal (PRC-P 5)
- **Zona / municipio · Provincia:** Cervera de Pisuerga y Arbejal · Palencia. No es la vía verde asturiana del mismo nombre.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular ✅ · 12,2 km (ficha 12) · +380 / −380 m (ficha 270: discrepancia de 110 m) · altitud ❓ · 4 h · media.
- **Inicio · Fin:** tres inicios señalizados: La Bárcena (Cervera), 42.87306, −4.50139 ✅; Arbejal; y el Mirador de las Matas (M03). Fin = inicio.
- **Temporada · Riesgos / avisos:** de mayo a otoño ✅. **Cierres intermitentes por obras en Cervera–Arbejal desde el 4-6-2026, "hasta nuevo aviso"** ✅; el PDF del 20-11-2026 ya no los recoge, así que el estado actual es dudoso ⚠️. Se cierra a menudo por cacería (por ejemplo, el 16-11-2025).
- **Agua · Refugios:** chozo del Tremedal en el km 8,5 ✅ (estado ❓).
- **Waypoints clave** (km según el sentido recomendado) ✅: Cervera 0 · Noria 0,7 · Arbejal 2,5 · embalse de Requejada 6,2 · chozo del Tremedal 8,5 · Cervera 12,2. Sin coordenadas, salvo el inicio.
- **Descripción:** sale de La Bárcena, en Cervera, y sube por la Noria hasta el pueblo de Arbejal. Desde allí gana el entorno de la Peña del Oso, las Peñas Negras y el Cordel Cerverano ⚠️. Baja después hacia el embalse de Requejada y regresa a Cervera por el chozo del Tremedal. Tiene amplias vistas sobre la cabecera del Pisuerga y comparte tramos con la etapa 3 del GR-1 (Estalaya–Cervera). Según AllTrails es la ruta mejor valorada del parque ⚠️.
- **Comentarios de usuarios:** "la mejor valorada" en AllTrails, sin texto disponible ⚠️.
- **Cifras de contraste (v2):** palenciaturismo 12,2 km / **+270** (coincide con la ficha, no con el plano) ✅ · Terranostrum 11,7 km / +300 / 4 h, baja ⚠️.
- **GPX Terranostrum (cálculo propio):** 11,7 km · +346 m · alt. 999–1.267 m · inicio 42.87209, −4.50276 · track cerrado (fin a 21 m del inicio).
- **Inicio (v2):** puente de San Roque, Cervera, 42.87235, −4.50293 (palenciaturismo; panel junto al puente) ✅.
- **Itinerario por tramos (v2, resumen propio):** Cervera → margen derecha del Pisuerga → Arbejal → vallejo de Congosto → antigua cantera de la presa de Requejada → cimas de Peñas Negras → Cervera.
- **Enlaces:** [ficha oficial](https://patrimonionatural.org/senderos/senda-del-oso).
- **Licencia · Confianza · Pendiente:** Junta (enlazar) · ✅ / ⚠️ (estado de obras) · Pendiente: confirmar la reapertura, OCR de los folletos y track propio.

#### mp-of-mazobre · Senda de la Cascada de Mazobre (PR-P 6)
- **Zona / municipio · Provincia:** entre Cardaño de Abajo y Cardaño de Arriba (Velilla del Río Carrión), Alto Carrión · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** lineal hasta un mirador, ida y vuelta ✅ · 6,6 km i/v (plano; ficha 7; otras fuentes dicen "más de 8" u 11, en conflicto) · +270 / −270 m (ficha 250; otra fuente 320) · mín. ~1.340 m ⚠️ · 2 h · baja (más en invierno).
- **Inicio · Fin:** aparcamiento de Pino Llano, en el km 2,5 de la carretera Cardaño de Abajo–Cardaño de Arriba, 42.95167, −4.75889 ✅. Tiene pocas plazas. Fin = inicio.
- **Temporada · Riesgos / avisos:** la mejor época es la primavera, con el deshielo. En invierno la nieve complica la subida. **Cierre por cacería el 21-11-2026** ✅. La bajada final a la base de la cascada es estrecha.
- **Agua · Refugios:** **Refugio de Mazobre**, en la majada de Espigüete al pie de la cara NE del Espigüete: libre, de dos plantas, **~10 plazas para dormir y en uso** (refugioslibres, v2) ✅; la guía alpina de 2018 daba 20 plazas.
- **Waypoints clave:** solo el inicio. La variante circular de 8,6 km / 379 m (Wikiloc) pasa por una segunda cascada y por el refugio ⚠️.
- **Descripción:** sendero balizado en blanco y amarillo (PR-P 6) que remonta el valle hasta un mirador frente a la cascada de Mazobre, que se presenta como "el mayor salto de agua de toda Palencia". Se tarda alrededor de 1 h hasta el mirador. Desde ahí, una bajada corta lleva a la base del salto. El paisaje es de alta montaña, con la cara norte y la cresta este del Espigüete al fondo. Este mismo aparcamiento sirve de base para las ascensiones al Espigüete por el norte.
- **Comentarios de usuarios:** aparcamiento pequeño ("madrugar"); en invierno la nieve dificulta la subida ⚠️.
- **Cifras de contraste (v2):** palenciaturismo 6,6 km i/v / +250 / 2 h, fácil, homologada ✅; Terranostrum igual. Inicio palenciaturismo 42.95100, −4.76174 (km 2,5 de la P-217).
- **GPX Terranostrum (cálculo propio):** 5,86 km · +276 m · alt. 1.343–1.613 m · inicio 42.9512, −4.76168 · track cerrado (fin a 1 m del inicio) · ⚠️ **discrepancia:** distancia 5,86 frente a 6,6 km publicados.
- **Cascada (v2):** komoot la sitúa en **42.95929, −4.79297, a 1.613 m**, y Terranostrum en 42.95927, −4.79282. Está a ~2,6 km en línea recta del aparcamiento y a la misma cota que el máximo del GPX (1.613 m): **las dos fuentes son coherentes** con un recorrido de ~2,9 km por sentido (cálculo propio) ✅/⚠️. El mirador de madera está a poco más de 3 km según palenciaturismo.
- **Agua · refugios (v2):** **Refugio de Mazobre en uso, ~10 plazas para dormir**, dos plantas, chimenea, señalizado (refugioslibres); se llega por un desvío a la izquierda hacia la mitad del camino, ~30 min desde Pino Llano. El arroyo puede ir seco en tramos por filtración en la caliza, pero la cascada lleva agua casi todo el año, con más caudal tras lluvias. Fuente en el aparcamiento de Pino Llano según SummitPost (sin confirmar) ⚠️.
- **Comentarios (v2, komoot ✅):** "el mayor salto de agua de Palencia"; mejor después de lluvias (04-2023); senda corta del mirador a la base (10-2023); 3 km de buena pista, también ciclable (10-2022); agua fresca para refrescarse (08-2024). En invierno, raquetas; posible oso (palenciaturismo).
- **Enlaces:** [ficha oficial](https://patrimonionatural.org/senderos/senda-de-la-cascada-de-mazobre) · [Wikiloc 177185185 (circular con refugio)](https://es.wikiloc.com/rutas-senderismo/cascada-y-refugio-de-mazobre-177185185).
- **Licencia · Confianza · Pendiente:** Junta / Wikiloc (enlazar) · ✅ cifras del plano / ⚠️ cascada · Pendiente: coordenada exacta del refugio y del mirador.

#### mp-of-gigante · Senda del Gigante del Valle Estrecho (PR-P 7)
- **Zona / municipio · Provincia:** pasado Santibáñez de Resoba, en la "Ruta de los Pantanos" (P-210) · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** lineal ✅ · 4,4 km (ficha 4) · +150 / −150 m (folleto 113) · altitud ❓ · 1 h 15 (folleto 1 h 06; ficha 2 h) · baja.
- **Inicio · Fin:** aparcamiento en el km 15,5 de la Ruta de los Pantanos, 42.90639, −4.62639 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** solo el inicio.
- **Descripción:** sendero corto por el Valle Estrecho, un valle de hayedos según el título de la ruta BTT homónima de la Diputación ("Los Hayedos del Valle Estrecho"). Lleva a los miradores que cuentan la leyenda del "Gigante" (no es un árbol: ver la corrección v2). Queda muy cerca de la ascensión a Santa Lucía y Peña Escrita (ruta 14), que sale de Santibáñez de Resoba.
- **Comentarios de usuarios:** no se encontraron.
- **Cifras de contraste (v2):** palenciaturismo 4,4 km i/v / +113 / 1 h, fácil, homologada ✅ · Terranostrum 4,3 km / 1 h 10. Inicio palenciaturismo 42.90541, −4.62797.
- **GPX Terranostrum (cálculo propio):** 4,25 km · +157 m · alt. 1.335–1.444 m · inicio 42.90549, −4.62794 · track cerrado (fin a 2 m del inicio) · fin en el Mirador de Caldacio 42.89526, −4.61463 (punto de Terranostrum).
- **Corrección (v2):** **el "Gigante" no es un árbol, es una leyenda** (palenciaturismo) ✅. Según la tradición recogida en Wikipedia, un gigante de San Martín de los Herreros huyó a la sierra tras perder a su hija, que se fugó con su amado, y murió tendido en la cumbre: el perfil de la sierra de la Peña sería su cuerpo, con Peña Redonda como la barriga, y sus lágrimas brotarían en la Fuente de la Sondonada.
- **Waypoints (v2):** mirador de Peñalbilla (a 2 km) · mirador de Caldacio (panel con la leyenda) · Peña Negra (1.445 m) · Fuente Deshondonada (palenciaturismo).
- **Enlaces:** [ficha oficial](https://patrimonionatural.org/senderos/senda-del-gigante-del-valle-estrecho).
- **Licencia · Confianza · Pendiente:** Junta (enlazar) · ✅ cifras y leyenda · Pendiente: track propio.

#### mp-of-fuente-cobre · Senda de Fuente Cobre (PR-P 8)
- **Zona / municipio · Provincia:** Santa María de Redondo (La Pernía), cabecera del Pisuerga · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** ⚠️ circular según palenciaturismo, ida y vuelta según el Ayto. de Cervera · 12,3 km (plano; otras fuentes 10–14; AllTrails 11,7) · +420 / −420 m (AllTrails 458) · altitud ❓ · 4 h 30 · media.
- **Inicio · Fin:** aparcamiento a la salida de Santa María de Redondo, tras el puente sobre el arroyo Lombatero ⚠️. Coordenada de la ficha: 42.99139, −4.42667 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** barro frecuente en el hayedo después de lluvias; "más exigente de lo que parece". Es zona osera (un avistamiento reportado). Zona ULA 3 Redondo–Castillería.
- **Agua · Refugios:** la "Fuente del Cobre" **no es una fuente para beber**: es la cueva-surgencia kárstica del Pisuerga.
- **Waypoints clave:** inicio. Cueva del Cobre sin coordenadas ❓.
- **Descripción:** desde Santa María de Redondo, el sendero se adentra en el valle de Los Redondos entre prados y hayedo hasta la **Cueva del Cobre**, el nacimiento tradicional del río Pisuerga. Es un sistema kárstico en el que el río usa la cueva como zona de paso, con sumidero y surgencia. El colector principal de la cueva es de libre acceso según el PUP. Es una de las rutas emblemáticas del parque y punto de partida de la ascensión al Tres Mares y al Cuchillón.
- **Comentarios de usuarios** (AllTrails, 22 reseñas ⚠️): embarrada, muy bien marcada, más dura de lo esperado; una pareja vio un oso.
- **Tipo resuelto (v2):** **circular** ✅. Palenciaturismo 13 km circular / +400 / 4 h 30, moderada, homologada; Terranostrum 11,6 km / +400, con vuelta alternativa; el GPX cierra a 3 m del inicio. Inicio palenciaturismo 42.99156, −4.42791 (junto a una antigua mina, tras el puente del Lombatero).
- **GPX Terranostrum (cálculo propio):** 11,61 km · +440 m · alt. 1.224–1.604 m · inicio 42.99156, −4.42803 · track cerrado (fin a 3 m del inicio).
- **Cueva del Cobre (v2):** 42.98691, −4.37307 (Terranostrum) o 42.98732, −4.37233 (otra ficha); difieren ~80 m ⚠️.
- **Itinerario por tramos (v2, resumen propio):** puente del Lombatero → pista junto a la escombrera de la mina → puente sobre el Pisuerga → tercer puente → bifurcación con señal de acceso restringido (a la ida, por la derecha) → confluencia con el arroyo de Tejedo → senda por el fondo del valle entre hayas, acebos y abedules, con pequeñas cascadas → cueva bajo farallones calizos. Vuelta por una senda de ladera con vista de Peña Labra, una majada y un robledal. Palenciaturismo cita una vuelta alternativa por el Collado de Pando.
- **Contexto (v2, Wikipedia y Terranostrum, reformulado):** el Pisuerga nace en el circo glaciar de Covarrés, al pie del Valdecebollas; se sume en el Sel de la Fuente y resurge en la cueva. La distancia entre sumidero y surgencia varía según la fuente: ~1 km en línea recta (Terranostrum) o ~3 km (Wikipedia) ⚠️. Madoz cita la cueva en 1849; en 1980 unos vecinos cruzaron a nado el sifón durante una sequía y en 1982 se confirmó el origen en Covarrés. Las exploraciones superan los 7,5 km de galerías.
- **Avisos (v2):** nieve y agua pueden dificultar el acceso en invierno y a principios de primavera (Terranostrum). No hay avisos recientes de oso.
- **Enlaces:** [ficha oficial](https://patrimonionatural.org/senderos/senda-de-fuente-cobre) · [Wikiloc 17946364](https://www.wikiloc.com/hiking-trails/senda-de-fuente-cobrepr-p-8-17946364).
- **Licencia · Confianza · Pendiente:** Junta / Wikiloc (enlazar) · ✅ plano y tipo · Pendiente: OCR del folleto y coordenada única de la cueva.

#### mp-of-bosque-fosil · Senda del Bosque Fósil (PRC-P 9)
- **Zona / municipio · Provincia:** Verdeña (Cervera de Pisuerga) · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular interpretativa ✅ · 3,5 km (plano; ficha y folleto 3) · +120 / −120 m · altitud ❓ · 1 h · baja.
- **Inicio · Fin:** aparcamiento a la entrada de Verdeña, 42.94361, −4.45722 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓. Perros atados (senda interpretativa, PUP).
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** inicio. Mirador de Peña Celada y pared fósil, sin coordenadas.
- **Descripción:** paseo circular por un robledal hasta el mirador de Peña Celada y una pared rocosa (180 o 250 m según la fuente) con troncos fosilizados del Carbonífero, de unos 300 millones de años. Es una de las sendas homologadas más recientes (2019) e ideal para familias. Verdeña es también una localidad ligada a la divulgación del oso pardo.
- **Comentarios de usuarios:** no se encontraron.
- **Cifras de contraste (v2):** palenciaturismo 3 km / +120 / 1 h, fácil, balizada ✅ · Terranostrum 3 km / 1 h. Inicio palenciaturismo 42.94307, −4.46424.
- **GPX Terranostrum (cálculo propio):** 3,13 km · +110 m · alt. 1.183–1.297 m · inicio 42.94297, −4.46199 · track cerrado (fin a 3 m del inicio) · ⚠️ **discrepancia:** distancia 3,13 frente a 3,5 km publicados.
- **Waypoints y contenido (v2):** tres miradores (Peña Celada, Bosque Fósil y La Pernía). Los troncos fósiles son de *Sigillaria* y *Cordaites*, del Carbonífero (palenciaturismo).
- **Enlaces:** [ficha oficial](https://patrimonionatural.org/senderos/senda-del-bosque-fosil).
- **Licencia · Confianza · Pendiente:** Junta (enlazar) · ✅ · Pendiente: coordenadas de la pared fósil.

#### mp-of-lomas · Senda de la Laguna (Pozo) de las Lomas (PR-P 10)
- **Zona / municipio · Provincia:** Cardaño de Arriba (Velilla del Río Carrión), macizo de Fuentes Carrionas · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** lineal, ida y vuelta ✅ · 12,3 km (plano; ficha 12) · +650 / −650 m (ficha 640; Diputación 620) · de 1.415 a ~2.080 m · 5 h (con paradas ~6 h) · media-alta (más en invierno).
- **Inicio · Fin:** aparcamiento de Cardaño de Arriba: 42.97113, −4.75757 (Diputación, 1415 m) ✅; ficha 42.97167, −4.75583. Fin = inicio.
- **Temporada · Riesgos / avisos:** sin nieve de junio a octubre (inferencia). Con nieve la dificultad aumenta claramente. Es alta montaña en zona de reserva R1. Prohibido acampar o vivaquear junto a la laguna.
- **Agua · Refugios:** arroyo de las Lomas a lo largo del recorrido (sin tratar no es potable). Majada de las Lomas (1863 m), 43.00033, −4.74268. Chozos pastoriles; hay uno reconstruido en Cardaño de Arriba.
- **Waypoints clave** (ruta 03 de la Diputación, tramo común): bifurcación 42.97758, −4.75586 · puente Hontanillas 42.98239, −4.75846 (1514 m) · puente Valcaliente 42.98373, −4.7738 (1610 m) · puente Zahurdias 42.98272, −4.77833 (1655 m). Ruta 06: Majada Las Lomas 43.00033, −4.74268 (1863 m). Coordenada publicada del Pozo de las Lomas: 43.010628, −4.743068 (sospechosa ⚠️).
- **Descripción:** sale de Cardaño de Arriba y remonta el valle del arroyo de las Lomas entre prados y abedules, cruzando varios puentes de madera. Pasado el desvío señalizado al Pico Murcia ("senda no balizada"), el camino sigue hasta la Majada de las Lomas. Termina en unos zigzags que suben al circo glaciar, donde está el Pozo de las Lomas a unos 2.080 m, bajo Peña Prieta y el cordal de las Agujas de Cardaño. Es la puerta de entrada a Peña Prieta, al Pico del Infierno y a la circular de los lagos.
- **Comentarios de usuarios:** no se encontraron comentarios nuevos.
- **Cifras de contraste (v2):** palenciaturismo 12 km i/v / +640 / 5 h, moderada ✅; escapadarural igual. Inicio palenciaturismo 42.97079, −4.75741; Terranostrum, junto a la iglesia, 42.97106, −4.75758.
- **GPX Terranostrum (cálculo propio):** 6,19 km · +671 m · alt. 1.414–2.078 m · inicio 42.97106, −4.75758 · fin 43.0107, −4.74271 (a 4,6 km en línea recta del inicio) · GPX de ida; fin en el lago.
- **Coordenada del lago resuelta (v2):** Pozo de las Lomas 43.01047, −4.74287 (Terranostrum) y 43.01029, −4.74284 (komoot): la publicada antes como sospechosa queda a menos de 50 m ✅.
- **Itinerario por tramos (v2, resumen propio):** iglesia de Cardaño de Arriba → praderas junto al río, con varios arroyos que cruzar → desvío al Pico Murcia → puente sobre el arroyo → Majada de las Vacas (chozo en ruinas) → Alto de La Lomba, con vista al circo → zigzags → lago, rodeado por el Tío Celestino, las Agujas de Cardaño y el Alto de las Lomas.
- **Avisos (v2):** ⚠️ **no caminar nunca sobre el lago helado** (un usuario de komoot cuenta que lo hizo en febrero de 2025). En invierno y a principios de primavera hacen falta raquetas, crampones y piolet (palenciaturismo, Terranostrum). Los vehículos de visitantes solo pueden circular por los tramos asfaltados. Al norte del pueblo estuvo el refugio del club Espigüete, destruido por un alud en febrero de 2015.
- **Contexto (v2, Wikipedia):** es uno de los cuatro lagos glaciares del macizo, junto con la laguna de Fuentes Carrionas (~2.220 m), el lago del Ves (~2.050 m) y el Pozo Curavacas (~1.800 m). El glaciarismo cuaternario dejó circos, valles en artesa y morrenas.
- **Comentarios (v2, komoot ✅):** "precioso lago glaciar bajo las Agujas de Cardaño" (26-06-2026); la nieve complica la subida en primavera (15-05-2023).
- **Enlaces:** [ficha oficial](https://patrimonionatural.org/senderos/senda-de-la-laguna-de-las-lomas).
- **Licencia · Confianza · Pendiente:** Junta (enlazar) · ✅ (incluida la coordenada del lago) · Pendiente: track propio.

#### mp-of-pinar-velilla · Senda del Pinar autóctono de Velilla (PR., sin número)
- **Zona / municipio · Provincia:** Velilla del Río Carrión, Sierra del Brezo · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular en lazo ✅ · 3,5 km (plano; ficha 4) · +180 / −180 m (ficha 150) · ~1.160–1.340 m ⚠️ · 1 h 20 (ficha 2 h) · baja.
- **Inicio · Fin:** aparcamiento junto a la Ciudad del Brezo. Coordenadas: ficha 42.8575, −4.8175; guía de la Diputación 42.85067, −4.83329 (1159 m) ✅. Hay una discrepancia de ~1,3 km. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave** (ruta 16 de la Diputación, tramo común): bifurcaciones de pistas 42.84957, −4.83347 y 42.84703, −4.83378 · inicio del sendero del funicular 42.84488, −4.83409 · Mirador del Pinar 42.84934, −4.82944 (1256 m).
- **Descripción:** paseo por uno de los escasos pinares autóctonos de la montaña cantábrica, en la falda de las Peñas Mayores. El trazado se cruza con el antiguo sendero de un funicular y llega al Mirador del Pinar, sobre el valle del Carrión. Desde aquí sale la ascensión a las Peñas Mayores (ruta 16).
- **Comentarios de usuarios:** no se encontraron.
- **Cifras de contraste (v2):** palenciaturismo 3,5 km circular / +150 / 2 h, fácil, no homologada ✅ · Terranostrum 3,5 km i/v / +150 / 2 h (sin GPX).
- **Inicio resuelto (v2):** poblado de Compuerto, a 2 km de Velilla por la P-210, **42.85064, −4.83302** (palenciaturismo), prácticamente igual que la guía de la Diputación ✅. Terranostrum: Ciudad del Brezo, 42.84970, −4.83507. La coordenada de la ficha de la Junta (42.8575, −4.8175) queda descartada ⚠️.
- **Contexto (v2):** dos miradores (de Compuerto y del Pinar) con vista al Espigüete, Peña Lampa y la presa. Es uno de los pocos pinares naturales de la Cordillera Cantábrica (Wikipedia). En el pinar está el **Pino Enroscao**, un pino retorcido sobre sí mismo (libro 2026). Relacionadas: `mp-collado-pinar` y `mp-pinar-pena-mayor`.
- **Enlaces:** [ficha oficial](https://patrimonionatural.org/senderos/senda-del-pinar-autoctono-de-velilla).
- **Licencia · Confianza · Pendiente:** Junta (enlazar) · ✅ (inicio resuelto) · Pendiente: track propio.

#### mp-of-venganza-conde · Senda de la Venganza del Conde (PR., sin número)
- **Zona / municipio · Provincia:** San Salvador de Cantamuda (La Pernía) · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular por pista y senda, uso peatonal ✅ · 7,2 km · +300 / −300 m · altitud ❓ (Peña Tremaya 1.441 m queda por encima del mirador) · 2 h 20 · baja.
- **Inicio · Fin:** San Salvador de Cantamuda, junto al río Pisuerga. El sendero cruza la CL-627. Sin coordenadas ❓.
- **Temporada · Riesgos / avisos:** todo el año. Puede haber **nieve y hielo en el mirador de la Leyenda** (cara norte de Peña Tremaya) hasta comienzos de la primavera ✅. Cierres por cacería (por ejemplo, el 7-3-2026).
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** mirador de la Leyenda, sin coordenadas.
- **Descripción:** senda de nueva creación (obra FEDER de ~141.164 €) que sale de San Salvador de Cantamuda, junto al Pisuerga, y sube por la umbría de Peña Tremaya hasta el mirador de la Leyenda. El nombre alude a una leyenda local cuyo contenido no se ha documentado. En el pueblo está la colegiata románica del siglo XII ❓.
- **Comentarios de usuarios:** no se encontraron.
- **Inicio (v2):** junto a la colegiata románica y el puente medieval de San Salvador de Cantamuda, **42.96686, −4.49547** (Terranostrum) ✅.
- **Cifras de contraste (v2):** Terranostrum 7,7 km circular / 2 h 30, baja; alt. 1.102–1.424 m.
- **GPX Terranostrum (cálculo propio):** 7,66 km · +323 m · alt. 1.102–1.424 m · inicio 42.96686, −4.49547 · track cerrado (fin a 138 m del inicio).
- **GPX Terranostrum, variante con cumbre (cálculo propio):** 9,55 km · +641 m · alt. 1.102–1.424 m · inicio 42.96686, −4.49547 · fin 42.97645, −4.47701 (a 1,8 km en línea recta del inicio) · variante con la cumbre de Peña Tremaya.
- **Waypoints (v2):** robledal de Matacastillo · supuesto emplazamiento del castillo del Conde Munio · **Mirador de la Leyenda** (escultura de doña Elvira, la criada sordomuda y la mula) · cumbre opcional de Peña Tremaya, 42.97739, −4.48015 (último tramo más empinado y **sin señalizar**) · Estrecho de San Roque · Collaín de la Corte · calero · embotelladora "Fuentes de Lebanza" · paso bajo la carretera.
- **Itinerario por tramos (v2, resumen propio):** cruce de la CL-627 en Venta Campa → prados y robledal → base de las calizas → cara norte de Peña Tremaya hasta el mirador, con vista de Areños, Los Llazos, el valle de los Redondos y Peña Sagra → retroceso de 450 m → bajada entre escobas al Estrecho de San Roque → pista a San Salvador.
- **Enlaces:** [ficha oficial](https://patrimonionatural.org/senderos/senda-de-la-venganza-del-conde).
- **Licencia · Confianza · Pendiente:** Junta / Terranostrum (enlazar) · ✅ · Pendiente: texto completo de la leyenda.

#### mp-of-monte-mayor · Senda del Monte Mayor (PR., sin número)
- **Zona / municipio · Provincia:** Salcedillo, Valberzoso y Grullos (Brañosera) · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular con dos ramales, por pistas y caminos antiguos ✅ · desde Salcedillo 8,8 km / +280 m / 2 h 45 · desde el aparcamiento de Grullos 14 km / +360 m / 4 h 15 · desde Valberzoso 12,5 km / +340 m / 3 h 50 · media-baja.
- **Inicio · Fin:** Salcedillo (inicio principal), Valberzoso o el aparcamiento de Grullos (mirador M07, entre Brañosera y Salcedillo). Sin coordenadas ❓.
- **Temporada · Riesgos / avisos:** todo el año ✅.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** mirador de Grullos (M07), sin coordenadas.
- **Descripción:** circuito por las brañas del Monte Mayor, en el entorno de Brañosera (tradicionalmente considerado el municipio más antiguo de España), con patrimonio arqueológico. La Junta adjudicó en 2025 la obra del mirador y del aparcamiento de Grullos (~113.000 €). Comparte territorio con la etapa 1 del GR-1 (Valberzoso, Salcedillo).
- **Comentarios de usuarios:** no se encontraron.
- **Inicios con coordenadas (v2):** Salcedillo 42.94084, −4.27340 (palenciaturismo, inicio del GR-1 E1) · Valberzoso, a 1 km del pueblo, 42.92382, −4.23767 (Terranostrum) ✅. El aparcamiento de Grullos sigue sin coordenada ❓. El GR-1 E1 cruza el bosque del Monte Mayor hasta el Alto de los Grullos. Relacionadas: `mp-salcedillo-rojadillo`, `mp-valberzoso-rojadillo`.
- **Enlaces:** [ficha oficial](https://patrimonionatural.org/senderos/senda-del-monte-mayor).
- **Licencia · Confianza · Pendiente:** Junta (enlazar) · ✅ · Pendiente: coordenadas de los tres inicios.

#### mp-of-pedrosa · Senda de La Pedrosa (PR., sin número)
- **Zona / municipio · Provincia:** Barruelo de Santullán – Brañosera, río Rubagón · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** lineal, ida y vuelta ✅ · plano 2025 5 km / +150 m / 1 h 30 (probablemente solo ida) ✅ · palenciaturismo **9 km i/v** / +150 / 3 h 30, fácil, PR no homologado ✅ · Terranostrum 7,2 km i/v / 2 h, baja, ciclable ⚠️ · alt. 1.048–1.211 m.
- **GPX Terranostrum (cálculo propio):** 3,72 km de ida · +171 m · alt. 1.048–1.211 m · inicio 42.91139, −4.28831 · fin 42.93529, −4.30771 (Brañosera).
- **Inicio · Fin:** cartel del barrio de San Pedro, Barruelo de Santullán, **42.91139, −4.28831** ✅ → ermita de San Roque, Brañosera (~42.9353, −4.3077). Palenciaturismo pone el marcador en el "Parque de La Pedrosa", 42.93411, −4.30461, que cae en Brañosera ⚠️. Acceso alternativo desde la carretera por la senda de la Fuente de la Flor.
- **Temporada · Riesgos / avisos:** todo el año; en invierno la nieve cubre el bosque y se usa con raquetas. Señalizada. Si uno se pierde, basta seguir el río aguas abajo. Admite BTT.
- **Agua · Refugios:** varios manantiales y la **Fuente de la Flor**, apreciada por su agua (sin control sanitario ⚠️).
- **Waypoints clave:** Barruelo (San Pedro) 42.91139, −4.28831 · puente de madera de las piscinas y El Helechar (GR-1 E2) · ermita de San Roque (Brañosera).
- **Itinerario por tramos (resumen propio):** Barruelo → bosque de robles de La Pedrosa junto al Rubagón, paralelo a la carretera, con saltos de agua → enlace con la senda de la Fuente de la Flor y con la ruta del Calero de Brañosera → ermita de San Roque. Vuelta por el mismo camino. Coincide con el GR-1 E2 en sentido inverso.
- **Descripción:** paseo de ribera por el robledal de La Pedrosa (el "Bosque de La Pedrosa" de palenciaturismo) entre los dos pueblos mineros. Es la 13.ª senda del plano oficial 2025 y sigue sin ficha en la web de la Junta. El Pozo Merino, poza natural en la desembocadura del Rubagón, aparece en el libro 2026.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [plano oficial 2025](https://patrimonionatural.org/ficheros/Parque%20Natural%20Monta%C3%B1a%20Palentina-%28sin%20senda%20Ruesga%29_compressed-20250621-104951.pdf) · [palenciaturismo](https://palenciaturismo.es/que-hacer/rutas/bosque-pedrosa).
- **Licencia · Confianza · Pendiente:** Junta, Diputación y Ayto. de Barruelo / Terranostrum (enlazar) · ✅ trazado, inicio y tipo / ⚠️ longitud canónica · Pendiente: aclarar si el plano da 5 km de ida y track propio.

#### mp-of-ruesga · Sendero circular del embalse de Ruesga (en proyecto)
- **Zona / municipio · Provincia:** Ruesga – Ventanilla (Cervera de Pisuerga) · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular ✅ · 10,82 km · desnivel máximo 38 m · cotas de 1.031 a 1.069 m · tiempo ❓ · fácil.
- **Inicio · Fin:** aparcamiento de Ruesga (1031 m). Sin coordenadas.
- **Temporada · Riesgos / avisos:** **estado de obra y apertura desconocidos** a finales de 2026. El plano 2025 se rotula "sin senda Ruesga". Coincide en tramos con el GR-1 y con la carretera P-210.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** pasarela de ~200 m sobre el agua cerca de Ventanilla · mirador de La Roca · pantalán de ~35 m · plataformas en voladizo en la P-210.
- **Descripción:** proyecto FEDER (607.825 €, ficha del 25-07-2025) de sendero perimetral al embalse de Ruesga. Incluye una pasarela de madera sobre el agua, un mirador y un pantalán. El entorno del embalse es el punto recomendado para escuchar la berrea, de mediados de septiembre a mediados de octubre.
- **Comentarios de usuarios:** no aplica.
- **Datos de contexto (v2):** el embalse de Ruesga es el más pequeño del sistema (1923, construido para el Canal de Castilla; palenciaturismo, Ruta de los Pantanos). Según komoot se permite el baño, con zona de arena y alquiler de patines, y la pista de la orilla es agradable (20-06-2026). Coordenada orientativa de Ruesga: 42.86402, −4.52766 (salida de la BTT "Por Valle Estrecho").
- **Enlaces:** [proyecto FEDER](https://patrimonionatural.org/proyectos/feder-sendero-embalse-de-ruesga).
- **Licencia · Confianza · Pendiente:** Junta (enlazar) · ✅ proyecto · Pendiente: confirmar la apertura.

### 16.2 Largo recorrido

#### mp-gr1-e1 · GR-1 Etapa 1: Mata de Hoz – Brañosera
- **Zona · Provincia:** La Braña · sale de Cantabria 🟦 (Mata de Hoz) y entra en Palencia.
- **Datos:** lineal · 8,0 km oficiales (Terranostrum 8,1) · +430 / −200 m · 2 h 30 (Terranostrum) · media.
- **Inicio · Fin:** Mata de Hoz 🟦 → Brañosera, 42.9350, −4.3078 (AEMET) ✅.
- **Riesgos:** sin datos.
- **Hitos:** Valberzoso y Salcedillo, ambos inicios de la Senda del Monte Mayor.
- **Descripción:** primera etapa palentina del Sendero Histórico GR-1. Entra desde Cantabria y cruza los pueblos de La Braña hasta Brañosera.
- **Cifras oficiales (v2, palenciaturismo):** 8,0 km · +430 / −200 m ✅. Total del GR-1 en Palencia: 85,38 km, +2.652 / −2.094 m, homologado.
- **Inicio → fin (v2, palenciaturismo, probables centroides de pueblo ⚠️):** 42.94084, −4.27340 → 42.93680, −4.30836.
- **GPX Terranostrum (cálculo propio):** 8,1 km · +319 m · alt. 1.058–1.375 m · inicio 42.93557, −4.24144 · fin 42.9359, −4.30814 (a 5,4 km en línea recta del inicio) · ⚠️ **discrepancia:** D+ 319 frente a 430 m publicados.
- **Itinerario por tramos (v2, resumen propio):** Remonta el río Camesa desde Mata de Hoz (Valdeolea, Cantabria 🟦) y entra en Palencia por una portilla → puente romano de Rojadillo → bosque del Monte Mayor → Alto de los Grullos (variantes a Valberzoso y Salcedillo) → bajada por pista de solana a Brañosera (capilla de San Miguel).
- **Enlaces:** [libro-guía GR-1 Palencia](https://patrimonionatural.org/ficheros/58dce5a62bd0a_Libro-GR1-en-PALENCIA.pdf) (no leído).
- **Licencia · Confianza · Pendiente:** Diputación (cifras, hechos) / Terranostrum (enlazar) · ✅ cifras oficiales / ⚠️ coordenadas · Pendiente: libro-guía de la Junta y track propio.

#### mp-gr1-e2 · GR-1 Etapa 2: Brañosera – Estalaya
- **Zona · Provincia:** Castillería · Palencia.
- **Datos:** lineal · 23,5 km oficiales (Terranostrum 24,3) · +660 / −800 m · 7 h 30 · moderada.
- **Inicio · Fin:** Brañosera → Estalaya. El Roblón está en el entorno de Estalaya (42.925, −4.46944).
- **Riesgos:** **cierre por cacería entre San Felices y Herreruela de Castillería el 22-11-2026** ✅.
- **Hitos:** San Felices de Castillería, Herreruela de Castillería.
- **Descripción:** la etapa más larga del GR-1 en Palencia. Atraviesa el valle de Castillería por pueblos de montaña hasta Estalaya.
- **Cifras oficiales (v2, palenciaturismo):** 23,5 km · +660 / −800 m · moderada ✅. Total del GR-1 en Palencia: 85,38 km, +2.652 / −2.094 m, homologado.
- **Inicio → fin (v2, palenciaturismo, probables centroides de pueblo ⚠️):** 42.93680, −4.30836 → 42.92768, −4.47515.
- **GPX Terranostrum (cálculo propio):** 24,29 km · +710 m · alt. 1.050–1.619 m · inicio 42.93568, −4.30814 · fin 42.92696, −4.47475 (a 13,6 km en línea recta del inicio).
- **Itinerario por tramos (v2, resumen propio):** Senda de La Pedrosa hasta Barruelo (puente de madera de las piscinas, El Helechar) → subida a la mina del Calero → ancha pista minera en ascenso largo (máx. ~1.619 m) → Herreruela de Castillería (ermita de N.ª S.ª del Monte; Roblón de Herreruela) → San Felices → aparcamiento de la Senda del Roblón, a 500 m de Estalaya.
- **Enlaces:** véase Fuentes (Terranostrum E2).
- **Licencia · Confianza · Pendiente:** Diputación (cifras, hechos) / Terranostrum (enlazar) · ✅ cifras oficiales / ⚠️ coordenadas · Pendiente: libro-guía de la Junta y track propio.

#### mp-gr1-e3 · GR-1 Etapa 3: Estalaya – Cervera de Pisuerga
- **Zona · Provincia:** Cervera · Palencia.
- **Datos:** lineal · 11,5 km oficiales (Terranostrum 10,6) · +170 / −250 m · 3 h · moderada.
- **Inicio · Fin:** Estalaya → Cervera (La Bárcena, 42.87306, −4.50139).
- **Hitos:** Arbejal. Comparte tramo con la Senda del Oso.
- **Riesgos:** posibles obras de la Senda del Oso.
- **Descripción:** etapa corta que baja desde Estalaya por Arbejal hasta Cervera de Pisuerga, capital del parque y sede de la Casa del Parque.
- **Cifras oficiales (v2, palenciaturismo):** 11,5 km · +170 / −250 m · moderada ✅. Total del GR-1 en Palencia: 85,38 km, +2.652 / −2.094 m, homologado.
- **Inicio → fin (v2, palenciaturismo, probables centroides de pueblo ⚠️):** 42.92768, −4.47515 → 42.86689, −4.49929.
- **GPX Terranostrum (cálculo propio):** 11,07 km · +139 m · alt. 998–1.161 m · inicio 42.92696, −4.47475 · fin 42.8666, −4.49882 (a 7 km en línea recta del inicio).
- **Itinerario por tramos (v2, resumen propio):** Vañes → borde del embalse de Requejada → antigua cantera de la presa → enlace con la Senda del Oso → portillo de El Collao → Arbejal (mirador) → Cervera.
- **Licencia · Confianza · Pendiente:** Diputación (cifras, hechos) / Terranostrum (enlazar) · ✅ cifras oficiales / ⚠️ coordenadas · Pendiente: libro-guía de la Junta y track propio.

#### mp-gr1-e4 · GR-1 Etapa 4: Cervera de Pisuerga – Triollo
- **Zona · Provincia:** La Pernía / Alto Carrión · Palencia.
- **Datos:** lineal · 23,0 km oficiales (Terranostrum 22,4) · +540 / −300 m (Terranostrum +574) · 6 h 40 · moderada.
- **Inicio · Fin:** Cervera → Triollo (coordenadas en el bloque v2).
- **Hitos:** Ventanilla, embalse de Ruesga, Alto de la Varga (mirador M04, 42.9085, −4.7276 ⚠️).
- **Riesgos:** cruza la zona de reserva ZR2 (Peña Redonda) por la pista Rabanal–Alto de la Varga, que está permitida.
- **Descripción:** etapa de transición entre la cuenca del Pisuerga y la del Carrión. Bordea el embalse de Ruesga, pasa por Ventanilla y cruza el Alto de la Varga para bajar a Triollo.
- **Cifras oficiales (v2, palenciaturismo):** 23,0 km · +540 / −300 m · moderada ✅. Total del GR-1 en Palencia: 85,38 km, +2.652 / −2.094 m, homologado.
- **Inicio → fin (v2, palenciaturismo, probables centroides de pueblo ⚠️):** 42.86689, −4.49929 → 42.92464, −4.68056.
- **GPX Terranostrum (cálculo propio):** 22,35 km · +577 m · alt. 998–1.432 m · inicio 42.8666, −4.49884 · fin 42.9239, −4.67993 (a 16,1 km en línea recta del inicio).
- **Itinerario por tramos (v2, resumen propio):** Cervera (iglesia de Santa María del Castillo) → Ruesga → orilla derecha del embalse (playas fluviales, áreas recreativas, pinar) → Ventanilla → antiguo camino a San Martín de los Herreros (puente de piedra de dos ojos) → Rebanal de las Llantas → La Lastra → Triollo.
- **Licencia · Confianza · Pendiente:** Diputación (cifras, hechos) / Terranostrum (enlazar) · ✅ cifras oficiales / ⚠️ coordenadas · Pendiente: libro-guía de la Junta y track propio.

#### mp-gr1-e5 · GR-1 Etapa 5: Triollo – Camporredondo de Alba
- **Zona · Provincia:** Alto Carrión · Palencia (última etapa íntegramente palentina).
- **Datos:** lineal · 10,7 km oficiales (Terranostrum 10,5) · +140 / −200 m · 3 h · moderada.
- **Inicio · Fin:** Triollo → Camporredondo de Alba (sin coordenadas).
- **Descripción:** etapa corta por el valle del Carrión, con vistas al embalse de Camporredondo y al Curavacas.
- **Cifras oficiales (v2, palenciaturismo):** 10,7 km · +140 / −200 m · moderada ✅. Total del GR-1 en Palencia: 85,38 km, +2.652 / −2.094 m, homologado.
- **Inicio → fin (v2, palenciaturismo, probables centroides de pueblo ⚠️):** 42.92464, −4.68056 → 42.89521, −4.74651.
- **GPX Terranostrum (cálculo propio):** 10,48 km · +153 m · alt. 1.224–1.407 m · inicio 42.92395, −4.68 · fin 42.89554, −4.74429 (a 6,1 km en línea recta del inicio).
- **Itinerario por tramos (v2, resumen propio):** Pista por la vega del Carrión con vistas al embalse de Camporredondo y al Curavacas → valle de Miranda → pasarela de madera → rampa de casi 1 km hasta Camporredondo de Alba.
- **Licencia · Confianza · Pendiente:** Diputación (cifras, hechos) / Terranostrum (enlazar) · ✅ cifras oficiales / ⚠️ coordenadas · Pendiente: libro-guía de la Junta y track propio.

#### mp-gr1-e6 · GR-1 Etapa 6: Camporredondo de Alba – Cruz Armada
- **Zona · Provincia:** Fuentes Carrionas · termina en el límite con León 🟧.
- **Datos:** lineal · ~9 km · +430–486 / −100 m · 2 h 45 · media (Terranostrum y cálculo propio; palenciaturismo no publica km) ⚠️.
- **Inicio · Fin:** Camporredondo → collado de la Cruz Armada, al sur del Espigüete.
- **Descripción:** última etapa palentina. Rodea por el sur el macizo del Espigüete hasta la divisoria con León.
- **Cifras oficiales (v2, palenciaturismo):** km no publicados por palenciaturismo · Terranostrum 9 km / +430 / −100 / 2 h 45, media ✅. Total del GR-1 en Palencia: 85,38 km, +2.652 / −2.094 m, homologado.
- **Inicio → fin (v2, palenciaturismo, probables centroides de pueblo ⚠️):** 42.89521, −4.74651 → 42.93095, −4.80978.
- **GPX Terranostrum (cálculo propio):** 9 km · +486 m · alt. 1.227–1.621 m · inicio 42.89551, −4.74427 · fin 42.92916, −4.81033 (a 6,6 km en línea recta del inicio).
- **Itinerario por tramos (v2, resumen propio):** Camino de Valdegullas, que sale por encima del cementerio con fuerte subida inicial → desvío al Monte Coriscao → pradera de Valdegullas → unión con el ramal de Cardaño de Abajo (`mp-cardano-cruz-armada`) → rampa recta al collado de la Cruz Armada (1.632 m según la ficha; 1.621 m en el GPX) → senda hacia Valverde de la Sierra (León 🟧).
- **Licencia · Confianza · Pendiente:** Diputación (cifras, hechos) / Terranostrum (enlazar) · ✅ cifras oficiales / ⚠️ coordenadas · Pendiente: libro-guía de la Junta y track propio.

#### mp-co-e5 · Camino Olvidado Etapa 5 (llegada a Aguilar de Campoo)
- **Zona · Provincia:** Aguilar · Palencia (procede de Cantabria 🟦).
- **Datos:** lineal · 24,3 km · +452 m · 6 h · baja (v2) ⚠️.
- **Descripción:** variante norte del Camino de Santiago por la montaña. Llega a Aguilar de Campoo por Nestar.
- **Cifras (v2):** Lineal · 24,3 km · desnivel acumulado 452 m · 6 h · baja · ciclable · todo el año (Terranostrum) ✅. Inicio en Olea (Cantabria 🟦) 42.93862, −4.17917 → Aguilar 42.79282, −4.25910. Casi toda la etapa va por Valdeolea y Valderredible; en Palencia solo el tramo Néstar–Aguilar.
- **GPX Terranostrum (cálculo propio):** 24,61 km · +715 m · alt. 719–1.025 m · inicio 42.93862, −4.17917 · fin 42.79282, −4.2591 (a 17,5 km en línea recta del inicio) · ⚠️ **discrepancia:** D+ 715 frente a 452 m publicados.
- **Itinerario por tramos (v2, resumen propio):** Olea → Casasola → La Cuadra → Las Quintanillas → La Quintana → Las Henestrosas (Santa María la Real) → Bercedo → Cuena (último pueblo cántabro) → **Néstar**, con entrada en Palencia por el puente romano de Puenteperdiz (42.84195, −4.23770) → Grijera (castro cántabro, 42.81400, −4.24577) → Aguilar. Patrimonio: calzada romana Pisoraca–Portus Blendium y menhires de La Matorra.
- **Enlaces:** véase Fuentes (Terranostrum E5).
- **Licencia · Confianza · Pendiente:** ⚠️ · Pendiente: cifras.

#### mp-co-e6 · Camino Olvidado Etapa 6: Aguilar de Campoo – Cervera de Pisuerga
- **Zona · Provincia:** Aguilar – Cervera · Palencia.
- **Datos:** lineal · 28,7 km · +427 m · 7 h · baja ⚠️.
- **Hitos:** Santa María la Real (Aguilar), Corvio (necrópolis rupestre), Matamorisca, Salinas de Pisuerga, Barcenilla, Quintanaluengos, Ligüérzana, Vado y Cervera.
- **Descripción:** etapa larga por los pueblos del valle del Pisuerga, con patrimonio románico y rupestre. La comparten los peregrinos que van a Santo Toribio de Liébana (Cantabria 🟦). Terranostrum ofrece GPX.
- **Cifras (v2):** Lineal · 28,7 km · acumulado 427 m · 7 h · baja · ciclable (Terranostrum) ✅. Aguilar 42.79282, −4.25910 → Cervera 42.86210, −4.49855.
- **GPX Terranostrum (cálculo propio):** 28,7 km · +369 m · alt. 884–1.007 m · inicio 42.79282, −4.2591 · fin 42.8621, −4.49855 (a 21 km en línea recta del inicio).
- **Itinerario por tramos (v2, resumen propio):** Aguilar (monasterio de Santa María la Real, paseo de los Cinco Caños, camino sobre la presa) → Corvio (necrópolis rupestre de unas veinte tumbas, 42.82207, −4.27981 ⚠️) → Matamorisca → Salinas de Pisuerga → Barcenilla → Quintanaluengos → Ligüérzana → Vado (eremitorio rupestre de San Vicente o Cueva de los Moros) → Cervera, donde cruza el Camino Lebaniego.
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ⚠️.

#### mp-co-e7 · Camino Olvidado Etapa 7: Cervera de Pisuerga – Guardo
- **Zona · Provincia:** La Peña · Palencia.
- **Datos:** lineal · 39,3 km · +851 m · 8–9 h · dificultad baja; ciclable ⚠️.
- **Hitos:** Cantoral, Cubillo de Castrejón, Traspeña, Santibáñez de la Peña, Las Heras, Villanueva de Arriba, Muñeca y Guardo.
- **Descripción:** recorre el piedemonte sur de la Sierra del Brezo por los pueblos de La Peña hasta Guardo. Pasa por Traspeña y Santibáñez, inicios de las ascensiones a Peña Redonda y Peña del Fraile.
- **Cifras (v2):** Lineal · 39,3 km · acumulado 851 m · 8–9 h · baja · ciclable, aunque el primer tramo hasta Tosande puede complicarse en bici (Terranostrum) ✅. Cervera 42.86202, −4.49835 → Guardo 42.78388, −4.85674.
- **GPX Terranostrum (cálculo propio):** 38,88 km · +626 m · alt. 990–1.199 m · inicio 42.86202, −4.49835 · fin 42.78388, −4.85674 (a 30,5 km en línea recta del inicio) · ⚠️ **discrepancia:** D+ 626 frente a 851 m publicados.
- **Itinerario por tramos (v2, resumen propio):** Cervera → valle de Tosande → Cantoral → Cubillo de Castrejón → Traspeña (crucero) → Villanueva de la Peña → Tarilonte → Aviñante → San Román de Entrepeñas (ruinas) → Santibáñez de la Peña (castro de La Loma, asedio romano del 25 a. C.) → Las Heras → Villanueva de Arriba → Muñeca → Guardo (pila románica en San Juan, Casa Grande barroca). La E8 continúa a Puente Almuhey (León 🟧).
- **Licencia · Confianza · Pendiente:** ⚠️.

#### mp-cn-romanico · Camino Natural del Románico Palentino (MAPA)
- **Zona · Provincia:** Ojeda / Boedo / Aguilar–Cervera · Palencia.
- **Datos:** red lineal por etapas · ~103 km con ramales ✅ · cifras por etapa en el bloque v2 ⚠️.
- **Inicio · Fin:** arranca de la etapa 2 de la Ruta del Carbón de Cok, cerca de Cozuelos de Ojeda. Cervera queda a 2 km de desvío del final de la etapa II.
- **Descripción:** Camino Natural del Ministerio de Agricultura que une iglesias románicas del norte de Palencia. Tiene guía por etapas y **GPX oficial por etapa** en IDEE: es la única traza oficial descargable de la zona.
- **Etapas (v2, Terranostrum bajo el nombre engañoso "Ruta del Carbón de Cok"; información: Caminos Naturales/MAPA):** dificultad media, ciclable al 100 %, todo el año ⚠️.

  | Tramo | Km (ficha) | Tiempo | GPX (cálculo propio) | Inicio → fin (GPX) | Pueblos |
  |---|---|---|---|---|---|
  | E1 Alar del Rey – Cozuelos de Ojeda | 16,9 | 5 h | 16,86 km / +333 / 851–1.065 m | 42.65863, −4.30906 → 42.75541, −4.39280 | Prádanos de Ojeda, Santibáñez de Ecla, Villaescusa de Ecla |
  | E2 Cozuelos de Ojeda – Vado | 32,3 | 9 h | 27,8 km / +569 / 990–1.229 m ⚠️ (4,5 km menos que la ficha) | 42.75541, −4.39281 → 42.85415, −4.48349 | Vallespinoso de Aguilar, barrios de San Pedro y Santa María, Dehesa de Montejo |
  | Variante 2 Cozuelos – Dehesa de Montejo | 22,5 | 6 h 30 | 22,3 km / +397 / 978–1.101 m | 42.76432, −4.39716 → 42.81855, −4.50581 | Perazancas, Montoto, Pisón y Colmenares de Ojeda |
  | E3 Vado – Herreruela de Castillería | 21,2 | 6 h | 21,0 km / +444 / 951–1.330 m | 42.85415, −4.48349 → 42.92933, −4.39066 | Barcenilla, Rueda de Pisuerga, Vallespinoso de Cervera, San Cebrián de Mudá |

- **Longitud total (v2):** el GPX completo de Terranostrum mide 131,6 km / ~2.000 m (cálculo propio), frente a ~103 km del MAPA: probablemente por las variantes ⚠️.
- **Enlaces:** [guía MAPA](https://servicio.mapa.gob.es/ca/desarrollo-rural/temas/caminos-naturales/guia_cnromanicopalentinonipo_tcm34-636970.pdf) · [GPX vía IDEE](https://idee.es/csw-inspire-idee/static/api/records/spaignCNT).
- **Licencia · Confianza · Pendiente:** MAPA / IDEE (licencia por revisar; probablemente reutilizable) · ✅ existencia / ⚠️ cifras de etapa de Terranostrum · Pendiente: contrastar con el GPX oficial del MAPA y revisar su licencia.

#### mp-cn-pineda · Camino Natural de los Puertos de Pineda
- **Zona · Provincia:** valle de Pineda, Alto Carrión · Palencia.
- **Datos:** pista ❓.
- **Inicio · Fin:** accesos por Resoba y por Vidrieros ✅.
- **Riesgos:** **cierre por cacería el 22-11-2026** ✅. Circulación de vehículos sujeta a permiso y regulación propia.
- **Descripción:** pista del valle de Pineda que remonta el alto Carrión hacia las vegas de Correcaballos y Cantos y el Refugio de Santa Marina. Es la base de las rutas a pie y en BTT hacia el Pozo Curavacas.
- **Refugios (v2):** en la vega están los refugios de pescadores de **Campoluengo** (~6 plazas, probablemente abierto) y **Santa Marina** (~8 plazas para dormir), ambos con el río a menos de 100 m (refugioslibres) ⚠️. Ver §4.
- **Enlaces:** [página del parque (regulación)](https://patrimonionatural.org/espacios-naturales/parque-natural/parque-natural-montana-palentina).
- **Licencia · Confianza · Pendiente:** ✅ existencia · Pendiente: texto de la regulación y GPX (IDEE).

#### mp-cn-lebaniego · Camino Lebaniego Castellano y Camino Natural Lebaniego de Pineda
- **Zona · Provincia:** Ojeda – Cervera – La Pernía · Palencia → Liébana 🟦.
- **Datos:** Camino Lebaniego Castellano, etapas palentinas E6–E9 ≈ 73 km, todas de dificultad baja (Terranostrum; información: Diputación de Palencia) ⚠️. El Camino Natural Lebaniego de Pineda solo está rotulado en el plano 2025 ✅ y no tiene ficha ❓.
- **Etapas (v2):**

  | Etapa | Km (ficha) | Tiempo | GPX (cálculo propio) | Inicio → fin (GPX) | Pueblos |
  |---|---|---|---|---|---|
  | E6 Alar del Rey – Perazancas de Ojeda | 24,8 | 5 h 30 | 24,76 km / +483 / 847–1.066 m | 42.65864, −4.30915 → 42.78485, −4.42130 | Prádanos, Santibáñez de Ecla, San Andrés de Arroyo, Villaescusa de Ecla, Cozuelos |
  | E7 Perazancas – Cervera de Pisuerga | 18,2 | 4 h 30 | 18,26 km / +352 / 987–1.163 m | 42.78522, −4.42115 → 42.86389, −4.49794 | Dehesa de Montejo, Vado |
  | E8 Cervera – San Salvador de Cantamuda | 18 | 4 h 30 | 18,07 km / +459 / 995–1.297 m | 42.86391, −4.49793 → 42.96494, −4.49840 | Arbejal, Vañes, Estalaya |
  | E9 San Salvador – Camasobres | 12,4 | 3 h 30 | 12,42 km / +524 / 1.106–1.401 m | 42.96493, −4.49790 → 43.01521, −4.48818 | El Campo, Lores, Casavegas |
  | E10–11 Camasobres – Pesaguero – Santo Toribio 🟦 | 17,4 + 24 | 4 h 30 + 7 h | 41,84 km / +1.076 / 287–1.454 m | 43.01507, −4.48749 → 43.14995, −4.65439 | Entra en Liébana. La ficha numera estas etapas como 11 y 12, de forma incoherente ⚠️ |

- **Notas:** cada ficha de Terranostrum enlaza dos GPX: el de la etapa y uno del camino completo (223,6 km desde 42.00874, −4.53674, cálculo propio). El tramo Cervera–San Salvador comparte territorio con el GR-1 y la Senda del Oso.
- **Descripción:** itinerario de peregrinación a Santo Toribio de Liébana que cruza la Montaña Palentina de sur a norte, por la Ojeda, Cervera y La Pernía, hasta el puerto de Piedrasluengas y Liébana.
- **Enlaces:** [Terranostrum E8](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-lebaniego-castellano-etapa-8-cervera-de-pisuerga-san-salvador-de-cantamuda) (+4 en Fuentes).
- **Licencia · Confianza · Pendiente:** Diputación / Terranostrum (enlazar) · ⚠️ cifras · Pendiente: Camino Natural Lebaniego de Pineda (sin fuente) y track propio.

### 16.3 Guía "Ascensiones en la Montaña Palentina" (Diputación de Palencia / La Pedrera Pindia, 2016)

Datos comunes a las 40 fichas:

- **Fuente:** tabla del anexo, PDF p.60, para las cifras. Cabecera y rutómetro de cada ruta para el resto.
- **Licencia:** ©La Pedrera Pindia. Se puede redistribuir el PDF íntegro y gratis, pero no extraer textos, fotos ni tracks: se reutilizan solo los hechos.
- **Señalización:** ninguna de estas rutas está balizada.
- **Temporada:** periodo estival con buen tiempo. En invierno, el MIDE no aplica.
- **Formato de las cifras:** IV = ida y vuelta, C = circular. MIDE = severidad-orientación-desplazamiento-esfuerzo.
- **Waypoints:** se dan como `WPn · km · nombre · alt · lat, lon`.
- **Enlace común:** [PDF de la guía](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf).
- **GPX:** QR a lapedrerapindia.com, sin comprobar ❓.

#### mp-dip-01 · Espigüete (2.451 m) por la arista este, desde Cardaño de Abajo
- **Zona · Provincia:** Fuentes Carrionas, Velilla del Río Carrión · Palencia.
- **Datos:** C 11,3 km / +1249 / −1249 m / 5 h 45 / MIDE 3-3-4-3 · IV 10,3 km / +1249 / 5 h 10 / 3-3-4-3 · alt. mín/máx 1314–2451 m.
- **Inicio · Fin:** Cardaño de Abajo, plaza (1314 m), 42.92095, −4.76391 ✅. Fin = inicio.
- **Temporada · Riesgos:** solo en verano sin nieve. La subida descrita es la vía difícil (arista este): **destrepe de una brecha de 3 m (II+)** y de una **canaleta de 2 m (II)**, con terreno aéreo. La bajada por la pedrera sur tiene el sendero "muy estropeado" y es de mucha pendiente. Para la vía fácil hay que invertir el sentido (pedrera sur = vía normal). El Espigüete concentra accidentes en mayo, con nieve de primavera.
- **Agua · Refugios:** ruinas de chozo en el WP14. Sin fuentes citadas.
- **Waypoints:** 
  - WP1 · km 0 · Cardaño De Abajo / Plaza · 1314 m · 42.92095, -4.76391
  - WP2 · km 0,36 · Bifurcación · 1364 m · 42.922, -4.76691
  - WP3 · km 0,88 · Balcón Dehesa De Cardaño · 1489 m · 42.92618, -4.76543
  - WP4 · km 1,63 · Fin Prados Inicio Sendero · 1596 m · 42.93098, -4.76929
  - WP5 · km 2,31 · Collado Valdopila · 1667 m · 42.93647, -4.77129
  - WP6 · km 2,63 · Inicio Subida · 1663 m · 42.93928, -4.77219
  - WP7 · km 3,61 · Collado Arista Este · 2138 m · 42.94445, -4.77958
  - WP8 · km 4,13 · Destrepe Brecha · 2265 m · 42.94422, -4.78503
  - WP9 · km 4,62 · Cima Este · 2441 m · 42.94513, -4.7904
  - WP10 · km 4,81 · Destrepe Canaleta · 2406 m · 42.94487, -4.79255
  - WP11 · km 5,03 · Collado Pedrera · 2415 m · 42.94512, -4.7949
  - WP12 · km 5,15 · Espigüete · 2451 m · 42.94462, -4.79617
  - WP13 · km 6,24 · Fin Pedrera · 1903 m · 42.93873, -4.79102
  - WP14 · km 6,46 · Ruinas Chozo · 1834 m · 42.93696, -4.79103
  - WP15 · km 6,99 · Pista · 1665 m · 42.93264, -4.79262
  - WP16 · km 7,84 · Curva Loma Soña · 1580 m · 42.93062, -4.78444
  - WP17 · km  · Bifurcación · 1440 m · 42.92557, -4.77209
  - WP18 · km 11,3 · Cardaño De Abajo / Plaza · 1314 m · 42.92096, -4.76394
- **Descripción:** desde la plaza de Cardaño de Abajo, una pista lleva por el balcón de la Dehesa de Cardaño hasta el final de los prados (km 1,6). Un sendero sube entonces al collado Valdopila (1667 m). En el km 2,6 empieza la subida fuerte al collado de la arista este (2138 m), junto a la Torre Díaz-Caneja (2272 m). Desde ahí se recorre la arista: destrepe de la brecha, Cima Este (2441 m), destrepe de la canaleta y collado de la Pedrera, hasta la cumbre (2451 m), con vértice geodésico, buzón y cruz. El descenso baja por la gran pedrera sur hasta las ruinas de un chozo, enlaza con la pista y vuelve por la loma de Soña. Es la montaña más reconocible de la vertiente palentina, una pirámide caliza aislada con circos glaciares en su cara norte.
- **Comentarios de usuarios:** véase mp-espiguete-sur (pedrera durísima en descenso).
- **Contraste (v2):** ver `mp-espiguete-sur` y `mp-espiguete-norte` (GPX de Terranostrum, Wikipedia y crónicas 2026). La Torre Díaz-Caneja recuerda a Juan Díaz-Caneja, a quien Pyrenaica atribuye la primera ascensión de la cara este (1915).
- **Enlaces:** [QR GPX](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Espiguete) ❓.
- **Confianza · Pendiente:** ✅ · Pendiente: comprobar que el GPX sigue disponible.

#### mp-dip-02 · Alto de la Hoya de Martín Vaquero
- **Zona · Provincia:** Fuentes Carrionas (inferida) · Palencia.
- **Datos:** IV 11,14 km / +771 / 4 h 40 / 3-3-3-3 · C 12 km / +1000 / 5 h 10 / 3-3-3-3.
- **Inicio, waypoints y descripción:** no disponibles en la versión gratuita ❓.
- **Confianza · Pendiente:** ✅ cifras · Pendiente: libro completo.

#### mp-dip-03 · Pico Murcia (2.351 m) y La Cerezuela (2.206 m), desde Cardaño de Arriba
- **Zona · Provincia:** Fuentes Carrionas (Agujas de Cardaño), Velilla · Palencia (la cumbre linda con León 🟧).
- **Datos:** C 12,5 km / +1008 / −1008 / 5 h 15 / 3-3-3-3 · IV 12,32 / +936 / 5 h / 3-3-3-3 · alt. mín/máx 1409–2351 m.
- **Inicio · Fin:** aparcamiento de la senda del Pozo de las Lomas, Cardaño de Arriba (1415 m), 42.97113, −4.75757 ✅.
- **Temporada · Riesgos:** verano. Desde el desvío del PR-P 10, la senda **no está balizada**. La arista sureste sube por terreno de montaña.
- **Agua · Refugios:** arroyos de las Lomas, Valcaliente y Zahurdias. Majada de Arrilla. La cumbre tiene buzón y un **vivac** de piedra (pernoctar solo con autorización).
- **Waypoints:** 
  - WP1 · km 0 · Cardaño De Arriba · 1415 m · 42.97113, -4.75757
  - WP2 · km 0,82 · Bifurcacion Sendero · 1448 m · 42.97758, -4.75586
  - WP3 · km 0,97 · Bifurcación Sendero · 1462 m · 42.9785, -4.75579
  - WP4 · km 1,53 · Puente Hontanillas · 1514 m · 42.98239, -4.75846
  - WP5 · km 2,82 · Puente Valcaliente · 1610 m · 42.98373, -4.7738
  - WP6 · km 3,23 · Puente Zahurdias · 1655 m · 42.98272, -4.77833
  - WP7 · km 3,44 · Inicio Senda · 1705 m · 42.98232, -4.78077
  - WP8 · km 3,98 · Portillo · 1843 m · 42.98272, -4.78435
  - WP9 · km 4,64 · Arista Sureste · 1985 m · 42.97966, -4.78679
  - WP10 · km 5,85 · Inicio Travesía Hacia Arista · 2247 m · 42.98015, -4.79335
  - WP11 · km 6,02 · Arista Sureste · 2296 m · 42.97891, -4.79442
  - WP12 · km 6,16 · Pico Murcia · 2351 m · 42.98047, -4.79449
  - WP13 · km 6,41 · Enlace Senda Vía Normal · 2246 m · 42.97873, -4.795
  - WP14 · km 6,88 · La Cerezuela · 2206 m · 42.97469, -4.796
  - WP15 · km 7,1 · Collado · 2151 m · 42.97335, -4.79437
  - WP16 · km 7,81 · Castillo De Arrilla · 2048 m · 42.96901, -4.78898
  - WP17 · km 8,41 · Colladín · 1894 m · 42.96436, -4.79001
  - WP18 · km 8,79 · El Sillareto · 1815 m · 42.96199, -4.78711
  - WP19 · km 9,64 · Collado · 1633 m · 42.9599, -4.77767
  - WP20 · km 9,9 · Puente Arrilla · 1607 m · 42.96157, -4.77915
  - WP21 · km 10,36 · Majada De Arrilla · 1579 m · 42.96234, -4.77409
  - WP22 · km 12,21 · Carretera · 1409 m · 42.96868, -4.75786
  - WP23 · km 12,5 · Cardaño De Arriba · 1415 m · 42.97109, -4.75763
- **Descripción:** sigue el PR-P 10 por el valle de las Lomas cruzando los puentes de Hontanillas, Valcaliente y Zahurdias. En el km 3,4 toma el desvío señalizado "Pico Murcia. Senda no balizada". Sube por un portillo a la arista sureste y la recorre con una travesía hasta la cumbre (2351 m). Vuelve por La Cerezuela (2206 m), el Castillo de Arrilla, El Sillareto y la Majada de Arrilla hasta la carretera. Un recuadro de la guía explica los chozos pastoriles; hay uno reconstruido en Cardaño de Arriba.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [QR GPX](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Pico-Murcia) ❓.
- **Confianza · Pendiente:** ✅.

#### mp-dip-04 · Peñas Malas
- **Zona:** Fuentes Carrionas (cordal Agujas de Cardaño) · Palencia.
- **Datos:** IV 11,4 / +867 / 4 h 40 / 3-3-3-3 · C 11,9 / +962 / 5 h / 3-3-3-3.
- **Inicio, waypoints y descripción:** no disponibles ❓.
- **Confianza:** ✅ cifras.

#### mp-dip-05 · Pico Las Cuartas
- **Zona:** Fuentes Carrionas · Palencia.
- **Datos:** IV 15,74 / +1042 / 6 h 10 / 3-3-3-4 · C 15,4 / +1227 / 6 h 30 / 3-3-3-4.
- **Inicio:** aparcamiento de Cardaño de Arriba (lo indica la ruta 06, cuyos WP1–6 siguen esta ruta) ⚠️. Llega a la Majada de las Lomas (43.00033, −4.74268) ✅.
- **Confianza · Pendiente:** ✅ cifras · Pendiente: libro completo.

#### mp-dip-06 · Peña del Infierno (2.537 m, techo de Palencia), desde Cardaño de Arriba
- **Zona · Provincia:** Fuentes Carrionas · Palencia / límite con Cantabria 🟦 y León 🟧.
- **Datos:** C 24,2 km / +1787 / −1787 / 9 h 45 / 3-3-3-4 · IV 17,98 / +1222 / 7 h / 3-3-3-4 · alt. mín/máx 1168–2537 m. El "Puente del Ves" figura con 1168 m, una cota sospechosa: probable errata, ~1600 m.
- **Inicio · Fin:** aparcamiento de Cardaño de Arriba (1415 m), 42.97077, −4.75754 ✅.
- **Temporada · Riesgos:** verano. Ruta muy larga. Hay que **vadear un arroyo** (WP28). La vertiente de Peña Prieta es zona de reserva R1. El vértice de Peña Prieta está deteriorado.
- **Agua · Refugios:** Laguna de Fuentes Carrionas (2206 m), Charca de las Ninfas, arroyos. **Chozo de la Majada de Fuentes Carrionas** (1878 m, en estado deficiente según una fuente de 2026), chozo y cueva del Tío Vicente, roca-chozo del Ves, chozo de la Majada de Arriba. Hito y vivac en el Mojón de Tres Provincias.
- **Waypoints** (WP1–4 = ruta 05; WP7 excluido por coordenada errónea): 
  - WP5 · km 0 · Cardaño De Arriba, Aparcamiento · 1415 m · 42.97077, -4.75754
  - WP6 · km 4,62 · Majada Las Lomas · 1863 m · 43.00033, -4.74268
  - WP7 · km 5,85 · Senda Peña Prieta · 2056 m · COORDENADA ERRÓNEA EN PDF (excluir)
  - WP8 · km 5,95 · Inicio Subida La Panda · 2074 m · 43.00794, -4.73859
  - WP9 · km 7,34 · Collado · 2372 m · 43.01295, -4.73616
  - WP10 · km 7,88 · Collado El Campo De Gibraltar · 2405 m · 43.01709, -4.73825
  - WP11 · km 8,37 · Mojón De Tres Provincias · 2499 m · 43.02096, -4.73782
  - WP12 · km 8,99 · Peña Del Infierno Peña Prieta Sur · 2537 m · 43.02226, -4.73091
  - WP13 · km 9,15 · Horcada · 2484 m · 43.02109, -4.73027
  - WP14 · km 9,84 · Laguna De Fuentes Carrionas · 2206 m · 43.01578, -4.73146
  - WP15 · km 10,18 · Rocas Portal De Belén · 2217 m · 43.01476, -4.72855
  - WP16 · km 10,99 · Inicio Senda · 1963 m · 43.01016, -4.72359
  - WP17 · km 11,55 · Majada De Fuentes Carrionas · 1878 m · 43.00948, -4.7172
  - WP18 · km 11,96 · Inicio Pista · 1826 m · 43.00945, -4.71282
  - WP19 · km 13,66 · Bifurcación Pista Matapiojos · 1743 m · 43.00886, -4.69259
  - WP20 · km 14 · Alto De Matapiojos · 1742 m · 43.00734, -4.68911
  - WP21 · km 14,61 · Puente · 1620 m · 43.00389, -4.6881
  - WP22 · km 16,11 · Roca Chozo Del Ves · 1728 m · 42.99576, -4.69013
  - WP23 · km 17,22 · Chozo De La Majada De Arriba · 1797 m · 42.99553, -4.7028
  - WP24 · km 18,44 · Collado Del Ves · 2069 m · 42.99429, -4.71525
  - WP25 · km 19,4 · Prados De Holmas · 1913 m · 42.98739, -4.72082
  - WP26 · km 19,69 · Giro Derecha (Noroeste) · 1892 m · 42.98626, -4.7237
  - WP27 · km 20,36 · Inicio Senda · 1748 m · 42.98838, -4.73094
  - WP28 · km 20,59 · Vadeo Arroyo · 1680 m · 42.9892, -4.73292
  - WP29 · km 20,85 · Bifurcacion Senda · 1656 m · 42.99014, -4.73528
  - WP30 · km 21,24 · Puente Del Ves · 1168 m · 42.9887, -4.73924
  - WP31 · km 24,2 · Cardaño De Arriba · 1415 m · 42.97112, -4.75757
- **Descripción:** sigue la ruta 05 y el PR-P 10 hasta la Majada de las Lomas y el Pozo de las Lomas. Después toma una marca roja "P PRIETA" y sube en zetas por La Panda El Macho hasta el collado El Campo de Gibraltar (2405 m). Alcanza el Mojón de Tres Provincias (2499 m), con hito y vivac, y luego la Peña del Infierno (2537 m), con buzón e hito; desde ahí es opcional subir a Peña Prieta (2539 m, en Cantabria). La circular baja a la Laguna de Fuentes Carrionas, donde nace el Carrión, y sigue por la Charca de las Ninfas y las rocas del Portal de Belén. Continúa por la Majada de Fuentes Carrionas, el Alto de Matapiojos y el puente sobre el Carrión, el chozo del Ves y la Majada de Arriba. Remonta al Collado del Ves (2069 m) y regresa por los Prados de Holmas y el Puente del Ves. La guía aclara que el techo de Palencia es la Peña del Infierno, no el Curavacas.
- **Comentarios de usuarios:** véase mp-pena-prieta-cardano.
- **Enlaces:** [QR GPX](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/peña-del-infierno) ❓.
- **Confianza · Pendiente:** ✅ · Pendiente: corregir el WP7 y la cota del Puente del Ves.

#### mp-dip-07 · Alto del Calderón
- **Zona:** Fuentes Carrionas (zona de reserva R1) · Palencia.
- **Datos:** IV 12,2 / +860 / 4 h 40 / 2-3-3-3 · C 15,4 / +1215 / 6 h 20 / 3-3-3-3.
- **Inicio, waypoints y descripción:** no disponibles ❓.

#### mp-dip-08 · Curruquilla
- **Zona:** Fuentes Carrionas · Palencia.
- **Datos:** IV 18,56 / +1001 / 6 h 45 / 3-3-3-4 · C 16,4 / +1411 / 7 h / 3-3-3-4.
- **Inicio, waypoints y descripción:** no disponibles ❓.

#### mp-dip-09 · Peña del Tejo (1.998 m) y Coto Blanco (2.004 m), desde el Puente Agudín
- **Zona · Provincia:** Fuentes Carrionas, entre los Cardaños · Palencia.
- **Datos:** C 10 km / +828 / −828 / 4 h 20 / 3-3-3-3 · IV 7,28 / +700 / 3 h 20 / 3-3-3-3 · alt. mín/máx 1298–2004 m.
- **Inicio · Fin:** Puente Agudín (1298 m), 42.92981, −4.75844 ✅.
- **Temporada · Riesgos:** verano. Montaña de dificultad media, sin pasos técnicos descritos.
- **Agua · Refugios:** **varios pequeños manantiales** (WP5, 1664 m) y **una fuente** (WP14, 1773 m); toma de aguas en un arroyo (WP15). Chozo de Tierraconcejo (WP3) y Tenada de Lamas.
- **Waypoints:** 
  - WP1 · km 0 · Puente Agudín · 1298 m · 42.92981, -4.75844
  - WP2 · km 0,84 · Inicio Sendero · 1380 m · 42.92399, -4.75279
  - WP3 · km 1,66 · Chozo De Tierraconcejo · 1558 m · 42.92788, -4.74824
  - WP4 · km 2,04 · Collado. Inicio Subida · 1591 m · 42.92873, -4.74387
  - WP5 · km 2,27 · Fuentes · 1664 m · 42.93032, -4.74299
  - WP6 · km 2,62 · Sendero · 1769 m · 42.93284, -4.74317
  - WP7 · km 2,80 · Fin Sendero · 1817 m · 42.93417, -4.74443
  - WP8 · km 3,07 · Giro Derecha (Este) · 1901 m · 42.93606, -4.74518
  - WP9 · km 3,5 · Cota 1995 · 1995 m · 42.93693, -4.74103
  - WP10 · km 3,64 · Peña Del Tejo (1998 M) · 1998 m · 42.93772, -4.7402
  - WP11 · km 4,19 · Collado. Paso Escobas · 1916 m · 42.94103, -4.73739
  - WP12 · km 4,51 · Coto Blanco (2004 M) · 2004 m · 42.94296, -4.7356
  - WP13 · km 5,04 · Collado · 1900 m · 42.9461, -4.73136
  - WP14 · km 5,42 · Fuente · 1773 m · 42.94831, -4.73463
  - WP15 · km 6,6 · Arroyo. Toma De Aguas · 1468 m · 42.95067, -4.7471
  - WP16 · km 7,17 · Pista Tenada De Lamas · 1399 m · 42.95076, -4.75381
  - WP17 · km 7,57 · Pista Pino Llano · 1350 m · 42.94956, -4.75824
  - WP18 · km 10 · Puente Agudín · 1298 m · 42.92982, -4.75849
- **Descripción:** desde el Puente Agudín, un sendero sube al chozo de Tierraconcejo y a un collado. Pasa por los manantiales y gana la cota 1995 y la cumbre de la Peña del Tejo (1998 m). Por el paso de Escobas se llega al Coto Blanco (2004 m). La bajada pasa por una fuente y una toma de aguas y vuelve por las pistas de la Tenada de Lamas y de Pino Llano. Es una ruta cómoda frente al Espigüete, con buenas vistas a su cara este.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [QR GPX](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/la-peña-del-tejo) ❓.
- **Confianza:** ✅.

#### mp-dip-10 · Peña María
- **Zona:** Fuentes Carrionas · Palencia.
- **Datos:** IV 17,6 / +680 / 5 h 40 / 2-3-3-3 · C 13,1 / +780 / 4 h 50 / 3-3-3-3.
- **Inicio, waypoints y descripción:** no disponibles ❓.

#### mp-dip-11 · Canchas de Ojeda
- **Zona:** Fuentes Carrionas · Palencia.
- **Datos:** IV 16,6 / +893 / 5 h / 2-3-3-3 · C 16,3 / +1015 / 5 h / 2-3-3-3.
- **Inicio, waypoints y descripción:** no disponibles ❓.

#### mp-dip-12 · Curavacas (2.524 m) por la Pedrera Pindia y la Brecha Muerta, desde Vidrieros
- **Zona · Provincia:** Fuentes Carrionas, Triollo / Velilla · Palencia.
- **Datos:** C 11,1 km / +1400 / −1400 / 5 h 45 / 3-3-5-3 · IV 12,28 / +1600 / 6 h 30 / 3-3-5-4 · alt. mín/máx 1325–2524 m.
- **Inicio · Fin:** plaza de Vidrieros (1325 m), 42.94238, −4.66465 ✅.
- **Temporada · Riesgos:** verano sin nieve. **MIDE de desplazamiento 5**: trepadas en corredor, Brecha Muerta, **"terrazas de hierba muy expuestas"** y una "aérea vira" en la terraza sur. Caída de piedras en el conglomerado. Para la vía normal, subir y bajar por la Horcada del Callejo Grande.
- **Agua · Refugios:** arroyo de Cabriles (vadeo en el WP5). Sin refugio. El Refugio de los Pescadores queda a ~2 km de Vidrieros.
- **Waypoints:** 
  - WP1 · km 0 · Vidrieros Plaza · 1325 m · 42.94238, -4.66465
  - WP2 · km 0,59 · Puente · 1338 m · 42.94543, -4.66994
  - WP3 · km 1,24 · Bifurcación · 1432 m · 42.9509, -4.67016
  - WP4 · km 1,96 · Prados De Cabriles · 1526 m · 42.95654, -4.67007
  - WP5 · km 2,48 · Vadeo Arroyo · 1591 m · 42.96095, -4.67176
  - WP6 · km 2,56 · Inicio Senda · 1607 m · 42.96148, -4.67149
  - WP7 · km 3,88 · Inicio Callejo Grande · 2075 m · 42.97164, -4.67022
  - WP8 · km 4,15 · Collado Del Hospital · 2154 m · 42.97238, -4.66719
  - WP9 · km 4,67 · Roca Placa Faquires · 2021 m · 42.97615, -4.66772
  - WP10 · km 4,83 · Pedrera Pindia · 1967 m · 42.97756, -4.6677
  - WP11 · km 5,3 · Inicio Trepadas · 2220 m · 42.97906, -4.67199
  - WP12 · km 5,46 · Brecha Muerta · 2341 m · 42.98026, -4.67312
  - WP13 · km 5,64 · Trepadas A La Llana · 2375 m · 42.97876, -4.67368
  - WP14 · km 5,98 · Inicio Terraza Sur · 2471 m · 42.97595, -4.67485
  - WP15 · km 6,14 · Curavacas · 2524 m · 42.97634, -4.67395
  - WP16 · km 6,36 · Horcada Callejo Grande · 2465 m · 42.97713, -4.67241
  - WP17 · km 11,1 · Vidrieros Plaza · 1325 m · 42.94237, -4.66464
- **Descripción:** desde Vidrieros, un puente y una pista llevan a los Prados de Cabriles. Tras vadear el arroyo, una senda sube al inicio del Callejo Grande y al Collado del Hospital (2154 m). La vía difícil cruza a la vertiente norte por la roca Placa Faquires (el Escudo) y la **Pedrera Pindia**, de la que toma nombre la editorial. Remonta un corredor con trepadas hasta la Brecha Muerta (2341 m), sigue por la Llana y la terraza sur y llega a la cumbre (2524 m), con vértice geodésico y varios buzones. La bajada destrepa a la Horcada del Callejo Grande y desciende por la vía normal. El Curavacas es una mole de conglomerado silíceo, la cumbre más alta íntegramente palentina.
- **Comentarios de usuarios:** véase mp-curavacas-vidrieros.
- **Contraste (v2):** ver `mp-curavacas-vidrieros` (komoot, Wikipedia, Pyrenaica). El primer tramo coincide con la aproximación `mp-vidrieros-pie-curavacas`. La Cabaña de Mollorente (3 plazas, fuente) está en la ladera sur del Pico Pando, sobre la bajada por el collado Mollorente ⚠️.
- **Enlaces:** [QR GPX](http://www.lapedrerapindia.com/rutas-montana-palentina/ascensiones/curavacas) ❓.
- **Confianza:** ✅.

#### mp-dip-13 · Monte de Las Huelgas
- **Zona:** Fuentes Carrionas (macizo de Curavacas) · Palencia.
- **Datos:** IV 10,2 / +914 / 3 h / 2-3-2-3 · C 10,6 / +1063 / 3 h 30 / 3-3-4-3.
- **Inicio:** ❓. Un track de Wikiloc lo combina con el Curavacas y el Pico Hospital desde Vidrieros ⚠️.
- **Nota (v2):** Terranostrum tiene el Monte Coriscao (1.569 m) desde Camporredondo (`mp-coriscao`), pero no consta que sea la misma cumbre que el Monte de Las Huelgas ❓. lapedrerapindia.com siguió inaccesible en la v2.

#### mp-dip-14 · Santa Lucía (1.854 m) y Peña Escrita (1.762 m), desde Santibáñez de Resoba
- **Zona · Provincia:** Resoba (zona ULA 1, cabecera de Resoba) · Palencia.
- **Datos:** C 10 km / +880 / −880 / 4 h 30 / 3-4-5-3 · IV 10,8 / +650 / 4 h / 2-3-2-2 · alt. mín/máx 1207–1854 m.
- **Inicio · Fin:** explanada junto a la iglesia de San Cristóbal, Santibáñez de Resoba (1207 m), 42.90640, −4.60950 ✅.
- **Temporada · Riesgos:** la circular tiene **arista con pasos de III** y un **barranco con destrepes de III+**, "impracticable y muy difícil con agua". La versión de ida y vuelta es sencilla (MIDE 2-3-2-2). Peña Escrita tuvo restricción por familias de oso en 2022.
- **Agua · Refugios:** chozo en el collado (WP5). Cueva en la brecha (WP12).
- **Waypoints:** 
  - WP1 · km 0 · Santibáñez De Resoba · 1207 m · 42.9064, -4.6095
  - WP2 · km 0,97 · Cruce (Izq) · 1310 m · 42.91182, -4.60553
  - WP3 · km 1,8 · Cruce De Caminos · 1407 m · 42.9165, -4.61046
  - WP4 · km 2,14 · Bifurcación (Izq) · 1463 m · 42.91834, -4.61338
  - WP5 · km 2,65 · Collado Y Chozo · 1532 m · 42.92116, -4.61802
  - WP6 · km 4,28 · Collado · 1686 m · 42.92391, -4.63308
  - WP7 · km 5,32 · Santa Lucía · 1854 m · 42.91849, -4.63884
  - WP8 · km 5,82 · El Ojo De La Lastra · 1748 m · 42.91589, -4.64258
  - WP9 · km 6,18 · Prado Y Bloques · 1555 m · 42.9132, -4.64285
  - WP10 · km 7,56 · Pradera En Collado · 1727 m · 42.91425, -4.62808
  - WP11 · km 7,86 · Peña Escrita · 1762 m · 42.91415, -4.62482
  - WP12 · km 8,13 · Brecha Y Cueva · 1697 m · 42.91471, -4.62226
  - WP13 · km 8,42 · Collado · 1586 m · 42.91422, -4.6199
  - WP14 · km 9,13 · Inicio Barranco · 1350 m · 42.91209, -4.61399
  - WP15 · km 9,27 · Fin Barranco · 1300 m · 42.91091, -4.61386
  - WP16 · km 10 · Santibáñez De Resoba · 1207 m · 42.9064, -4.6095
- **Descripción:** desde Santibáñez de Resoba, unas pistas suben a un collado con chozo y a un segundo collado. Desde ahí se alcanza Santa Lucía (1854 m) y la curiosa ventana rocosa del Ojo de la Lastra. La circular cruza a una pradera en collado, sube a Peña Escrita (1762 m) y sigue la arista con pasos de III por una brecha con cueva. Termina bajando por un barranco técnico hasta el pueblo. El ida y vuelta a Santa Lucía es una excursión fácil con vistas al Curavacas.
- **Comentarios de usuarios:** no se encontraron.
- **Nota (v2):** el **Ojo de la Lastra** (WP8) es la foto 8 del libro "Montaña Palentina" 2026, que lo describe como un arco natural de piedra al pie de Santa Lucía.
- **Enlaces:** [QR GPX](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Santa-lucia) ❓.
- **Confianza:** ✅.

#### mp-dip-15 · Peña Lampa (guía)
- **Zona · Provincia:** Velilla · Palencia / León 🟧.
- **Datos:** IV 5,92 / +652 / 2 h 50 / 3-3-3-3 · C 9,7 / +686 / 3 h 50 / 3-3-3-3.
- **Inicio, waypoints y descripción:** no disponibles. Véase mp-pena-lampa.
- **Nota (v2):** Terranostrum ofrece la circular "El Sabinar de Peña Lampa" (`mp-sabinar-pena-lampa`), que sube al cordal hasta 1.803 m.

#### mp-dip-16 · Peñas Mayores de Velilla (1.869 m) y de Guardo (1.835 m), desde la Ciudad del Brezo
- **Zona · Provincia:** Sierra del Brezo, Velilla del Río Carrión · Palencia.
- **Datos:** C 9,2 km / +878 / −878 / 4 h 30 / 3-3-3-3 · IV 5,66 / +710 / 3 h 30 / 3-3-3-3 · alt. mín/máx 1159–1869 m.
- **Inicio · Fin:** aparcamiento de la Senda del Pinar, Ciudad del Brezo (1159 m), 42.85067, −4.83329 ✅.
- **Temporada · Riesgos:** paso tallado en la roca. Vaguada **cerrada por vegetación** (WP14), con mala orientación.
- **Agua · Refugios:** la cumbre de Peña Mayor de Velilla tiene una "construcción de piedra para abrigarse del viento". Chozo de Vidal (WP12, 1638 m).
- **Waypoints:** 
  - WP1 · km 0 · Ciudad Del Brezo. Aparcamiento · 1159 m · 42.85067, -4.83329
  - WP2 · km 0,15 · Bifurcación Pistas · 1168 m · 42.84957, -4.83347
  - WP3 · km 0,45 · Bifurcación Pistas · 1206 m · 42.84703, -4.83378
  - WP4 · km 0,70 · Inicio Sendero Funicular · 1222 m · 42.84488, -4.83409
  - WP5 · km 1,26 · Estación Superior Funicular Y · 1375 m · 42.84375, -4.83171
  - WP6 · km 1,58 · Paso Tallado En La Roca · 1445 m · 42.84157, -4.83152
  - WP7 · km 2,01 · Gran Hito De Piedras · 1617 m · 42.84169, -4.82811
  - WP8 · km 2,83 · Peña Mayor De Velilla · 1869 m · 42.83811, -4.82032
  - WP9 · km 3,99 · Portillo. Collado · 1764 m · 42.83283, -4.80864
  - WP10 · km 4,45 · Peña Mayor De Guardo,Peña · 1835 m · 42.8314, -4.80353
  - WP11 · km 4,95 · Portillo Rocoso · 1725 m · 42.83038, -4.7986
  - WP12 · km 5,46 · Chozo De Vidal · 1638 m · 42.83397, -4.80188
  - WP13 · km 5,6 · Inicio Pista · 1605 m · 42.83504, -4.80256
  - WP14 · km 6,3 · Vaguada Cerrada Por Vegetación · 1485 m · 42.83839, -4.80952
  - WP15 · km 7,17 · Collado Del Pinar. Inicio Sendero · 1526 m · 42.84309, -4.81764
  - WP16 · km 8,19 · Bifurcación Pista/Senda · 1267 m · 42.84716, -4.82763
  - WP17 · km 8,48 · Mirador Del Pinar · 1256 m · 42.84934, -4.82944
  - WP18 · km 8,65 · Bifurcación Pistas · 1233 m · 42.84806, -4.82947
  - WP19 · km 8,73 · Bifurcación Pistas · 1223 m · 42.84858, -4.83009
  - WP20 · km 9,2 · Ciudad Del Brezo. Aparcamiento · 1159 m · 42.85057, -4.83342
- **Descripción:** sale por la Senda del Pinar de Velilla, que está balizada, y toma el sendero del antiguo funicular hasta su estación superior. Pasa un paso tallado en la roca y un gran hito y llega a la Peña Mayor de Velilla (1869 m), con buzón en forma de casita. Por un portillo se sigue a la Peña Mayor de Guardo, también llamada Peña Lugar o Peñica Blanca (1835 m), con un buzón de tubo en una hornacina. La bajada pasa por el Chozo de Vidal y una vaguada cerrada por la vegetación hasta el Collado del Pinar y el Mirador del Pinar. Son las cumbres calizas que dominan Velilla y Guardo.
- **Comentarios de usuarios:** véase mp-penas-mayores-cordal.
- **Enlaces:** [QR GPX](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peñas-Mayores) ❓.
- **Confianza:** ✅.

#### mp-dip-17 · La Tuda
- **Zona:** Sierra del Brezo / La Peña · Palencia.
- **Datos:** IV 12,4 / +706 / 3 h 55 / 2-3-3-3 · C 13,2 / +834 / 5 h / 2-3-3-3.
- **Inicio, waypoints y descripción:** no disponibles ❓.

#### mp-dip-18 · Peña del Fraile (2.001 m), Peña Grande (1.833 m) y Peña Cueto (1.951 m), desde Santibáñez de la Peña
- **Zona · Provincia:** Sierra del Brezo · Palencia.
- **Datos:** C 11,9 km / +1070 / −1070 / 5 h / 3-3-3-3 · IV 12,1 / +896 / 4 h 30 / 3-3-3-3 · alt. mín/máx 1108–2001 m.
- **Inicio · Fin:** Santibáñez de la Peña (1108 m), 42.81049, −4.72966 ✅.
- **Temporada · Riesgos:** verano. La visita opcional a la Cueva de la Virgen se hace por un recorrido "escarpado y aéreo".
- **Agua · Refugios:** **Refugio del Corral** (WP5, 1288 m), abierto, con mesas de picnic, corral, **abrevadero y fuente**. Refugio de San Román. Un manantial. **Fuente dentro de la Cueva de la Virgen**. Restos de chozo en la Majada Anillo Encimero.
- **Waypoints:** 
  - WP1 · km 0 · Santibañez De La Peña · 1108 m · 42.81049, -4.72966
  - WP2 · km 0,27 · Bifurcación Molino · 1117 m · 42.81221, -4.73093
  - WP3 · km 0,55 · Bifurcación San Román · 1139 m · 42.81427, -4.7323
  - WP4 · km 1,22 · Bifurcación El Chimbo · 1208 m · 42.81899, -4.7355
  - WP5 · km 2,54 · Refugio Del Corral · 1288 m · 42.8214, -4.74731
  - WP6 · km 3,56 · Bifurcación Peñas De Santibañez · 1476 m · 42.81568, -4.75495
  - WP7 · km 4,14 · Collado De San Román · 1523 m · 42.81737, -4.76037
  - WP8 · km 5,35 · Peña Grande · 1833 m · 42.82713, -4.76242
  - WP9 · km 6,07 · Peña Del Fraile · 2001 m · 42.83271, -4.76555
  - WP10 · km 6,69 · Collado · 1841 m · 42.83514, -4.75973
  - WP11 · km 7,68 · Peña Cueto · 1951 m · 42.83703, -4.74861
  - WP12 · km 7,88 · Balcón Rocoso. · 1898 m · 42.83722, -4.74624
  - WP13 · km 8,75 · Majada Anillo Encimero · 1568 m · 42.83175, -4.7412
  - WP14 · km 9,26 · Inicio Camino · 1407 m · 42.82774, -4.74019
  - WP15 · km 9,72 · Fin Camino · 1332 m · 42.82572, -4.73684
  - WP16 · km 9,9 · Bifurcación El Calero · 1297 m · 42.82417, -4.73626
  - WP17 · km 11,92 · Santibañez De La Peña · 1108 m · 42.81049, -4.72966
- **Descripción:** desde Santibáñez de la Peña, un camino pasa por el molino y por el desvío de San Román hasta el Refugio del Corral. Sube por las Peñas de Santibáñez al Collado de San Román, la Peña Grande (1833 m) y la cumbre de la Peña del Fraile (2001 m), la más alta de la Sierra del Brezo según Mendikat. Sigue a Peña Cueto (1951 m) y a un balcón rocoso. Baja por la Majada Anillo Encimero y la bifurcación de El Calero. Las vistas abarcan La Peña y el páramo hacia el sur, y Fuentes Carrionas hacia el norte.
- **Comentarios de usuarios:** no se encontraron.
- **Contraste (v2):** Terranostrum publica la misma salida (antiguas escuelas, 42.80945, −4.72989) en circular de 12 km / +898 / 5 h: ver `mp-fraile`.
- **Enlaces:** [QR GPX](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-del-Fraile) ❓.
- **Confianza:** ✅.

#### mp-dip-19 · Peña Blanca
- **Datos:** IV 7,86 / +553 / 3 h 10 / 3-3-3-2 · C 11,8 / +729 / 4 h 25 / 3-3-3-3.
- **Zona:** La Peña (inferida).
- **Inicio, waypoints y descripción:** no disponibles ❓.

#### mp-dip-20 · Pico Traslosvocines
- **Datos:** IV 5,68 / +296 / 2 h / 2-2-2-2 · C 11,7 / +583 / 4 h 15 / 2-3-2-2.
- **Zona:** La Peña (inferida).
- **Notas:** es una de las rutas más fáciles de la guía. Inicio no disponible ❓.

#### mp-dip-21 · Sierra Canales
- **Datos:** IV 15 / +634 / 4 h 30 / 2-3-3-3 · C 16,6 / +827 / 5 h 30 / 2-3-3-3.
- **Zona:** La Peña (inferida).
- **Inicio:** no disponible ❓.

#### mp-dip-22 · Pico Rebanal
- **Datos:** IV 16 / +780 / 5 h 30 / 2-3-3-3 · C 13,7 / +834 / 5 h / 3-3-3-3.
- **Zona:** La Peña / Sierra del Brezo.
- **Notas:** un track de Wikiloc lo combina con Peña Redonda por el barranco (véase mp-pena-redonda) ⚠️.

#### mp-dip-23 · Peña Redonda (1.996 m), Castros del Mediodía (1.874 m) y Peña Urtejas (1.771 m), desde Villanueva de la Peña
- **Zona · Provincia:** Sierra del Brezo / La Peña (zona de reserva R2 Peña Redonda; el balizamiento de acceso está permitido) · Palencia.
- **Datos:** C 11,6 km / +940 / −940 / 4 h 40 / 3-3-4-3 · IV 10,4 / +819 / 4 h 20 / 3-3-3-3 · alt. mín/máx 1170–1996 m.
- **Inicio · Fin:** Villanueva de la Peña (1177 m), 42.82929, −4.62401 ✅.
- **Temporada · Riesgos:** la circular tiene una "aérea horcada y algún destrepe por terreno expuesto". La ZR2 tiene acceso restringido fuera del balizamiento.
- **Agua · Refugios:** sin datos.
- **Waypoints:** 
  - WP1 · km 0 · Villanueva De La Peña · 1177 m · 42.82929, -4.62401
  - WP2 · km 0,28 · Bifurcación Pista · 1172 m · 42.82874, -4.62124
  - WP3 · km 0,41 · Bifurcación Pista · 1178 m · 42.82875, -4.61985
  - WP4 · km 0,73 · Bifurcación Pista · 1170 m · 42.82756, -4.61626
  - WP5 · km 1,36 · Final Pista · 1191 m · 42.83143, -4.61104
  - WP6 · km 1,97 · Cruce Pistas · 1227 m · 42.83337, -4.60483
  - WP7 · km 2,37 · Pista Hitos · 1252 m · 42.83633, -4.60211
  - WP8 · km 2,65 · Inicio Sendero · 1288 m · 42.83824, -4.60386
  - WP9 · km 3,37 · Inicio Paso Rocas · 1441 m · 42.84354, -4.60054
  - WP10 · km 4,26 · Collado · 1701 m · 42.84986, -4.60348
  - WP11 · km 5,22 · Peña Redonda (1996 M) · 1996 m · 42.85161, -4.61329
  - WP12 · km 5,88 · Castros Del Mediodía (1874 M) · 1874 m · 42.85504, -4.61869
  - WP13 · km 6,46 · Peña Urtejas (1771 M) · 1771 m · 42.85942, -4.62009
  - WP14 · km 7,11 · El Collado · 1672 m · 42.86188, -4.62519
  - WP15 · km 7,55 · Cruce Vaguada Pared Rocosa · 1552 m · 42.85849, -4.62575
  - WP16 · km 8,52 · Collado · 1521 m · 42.85101, -4.62734
  - WP17 · km 9,35 · Fin Vaguada · 1360 m · 42.8452, -4.62443
  - WP18 · km 9,76 · Inicio Pista · 1304 m · 42.84201, -4.62263
  - WP19 · km 10,02 · Barranquera · 1249 m · 42.839, -4.61908
  - WP20 · km 10,79 · Pista · 1193 m · 42.83401, -4.62059
  - WP21 · km 10,96 · Bifurcación Pistas · 1202 m · 42.83266, -4.6203
  - WP22 · km 11,6 · Villanueva De La Peña · 1177 m · 42.82926, -4.62403
- **Descripción:** desde Villanueva de la Peña se sube por pistas y senda hasta la cumbre de Peña Redonda (1996 m). La cima tiene vértice geodésico y una gran cruz metálica de unos 14 m, con buzón y altar; el primer domingo de agosto se celebra allí una romería. La circular sigue la cresta por los Castros del Mediodía y la Peña Urtejas. Baja por El Collado, una vaguada junto a una pared rocosa y una barranquera hasta la pista y el pueblo. Peña Redonda es la cumbre más visible desde la meseta palentina.
- **Comentarios de usuarios:** véase mp-pena-redonda.
- **Enlaces:** [QR GPX](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-Redonda) ❓.
- **Confianza:** ✅.

#### mp-dip-24 · Pico Las Cruces (1.566 m) y Pico Almonga (1.519 m), desde el aparcamiento de Tosande
- **Zona · Provincia:** La Peña / Tosande, Dehesa de Montejo · Palencia.
- **Datos:** C 13,2 km / +921 / −921 / 5 h / 2-3-3-3 · IV 11,6 / +590 / 4 h / 2-3-3-3 · alt. mín/máx 1043–1566 m.
- **Inicio · Fin:** aparcamiento de Tosande (1152 m), 42.82578, −4.51656 ✅.
- **Temporada · Riesgos:** pasa por la Tejeda de Tosande (ZULA 5), así que aplican sus restricciones de octubre a febrero y los cierres por cacería.
- **Agua · Refugios:** abrevadero en una pradera (WP13).
- **Waypoints:** 
  - WP1 · km 0 · Aparcamiento De Tosande · 1152 m · 42.82578, -4.51656
  - WP2 · km 0,9 · Bifurcación · 1073 m · 42.83201, -4.52131
  - WP3 · km 1,32 · Mina Abandonada (Ruinas) · 1065 m · 42.83405, -4.51715
  - WP4 · km 2,26 · Desvío Pradera · 1048 m · 42.84058, -4.5104
  - WP5 · km 2,51 · Inicio Camino · 1043 m · 42.84218, -4.51046
  - WP6 · km 3,77 · Senda Bajo Franja Rocosa · 1256 m · 42.84559, -4.51873
  - WP7 · km 4,3 · Salida Del Bosque · 1377 m · 42.8472, -4.52063
  - WP8 · km 4,55 · Prado En Balcón · 1484 m · 42.84786, -4.52268
  - WP9 · km 4,78 · Pico Almonga · 1519 m · 42.8493, -4.52158
  - WP10 · km 5,82 · Pico Las Cruces · 1566 m · 42.84478, -4.53206
  - WP11 · km 6,54 · Cordal · 1472 m · 42.84372, -4.53889
  - WP12 · km 7,06 · Collado · 1358 m · 42.8453, -4.54396
  - WP13 · km 7,64 · Abrevadero En Pradera · 1193 m · 42.8435, -4.54983
  - WP14 · km 7,93 · Panel Informativo De La Tejeda De · 1230 m · 42.8422, -4.55211
  - WP15 · km 9,13 · Mirador · 1404 m · 42.83719, -4.55003
  - WP16 · km 10,14 · Puente Y Pista · 1152 m · 42.83896, -4.54287
  - WP17 · km 13,14 · Aparcamiento De Tosande · 1152 m · 42.82578, -4.51656
- **Descripción:** sale del aparcamiento por el camino de Cantoral y pasa junto a las ruinas de una mina abandonada. Sube al Pico Almonga (1519 m), que da nombre a una carrera de trail de Cervera, y al Pico Las Cruces (1566 m). Baja al valle de Tosande por un abrevadero y el panel de la Tejeda, sube al mirador (1404 m) y regresa por el puente y la pista. Combina cumbre fácil y tejeda en una misma jornada.
- **Comentarios de usuarios:** véase mp-of-tosande.
- **Variante (v2):** subida a los mismos picos desde Cervera por pista forestal, 9,5 km i/v: ver `mp-cruces-almonga-cervera`. Terranostrum llama a la cima "Pico de las Cruceras" (42.84470, −4.53206).
- **Enlaces:** [QR GPX](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Pico-Las-Cruces) ❓.
- **Confianza:** ✅.

#### mp-dip-25 · Pico de la Celada
- **Datos:** IV 10,6 / +642 / 4 h / 3-3-3-3 · C 14,2 / +710 / 5 h / 3-3-3-3.
- **Zona:** La Pernía (inferida).
- **Inicio:** no disponible ❓.

#### mp-dip-26 · Peña Carazo (2.012 m) y Horca de Lores (2.021 m), desde la Abadía de Lebanza
- **Zona · Provincia:** La Pernía · Palencia.
- **Datos:** C 15 km / +980 / −980 / 5 h 30 / 3-4-3-3 · IV 9,5 / +650 / 3 h 30 / 2-3-3-3 · alt. mín/máx 1224–2021 m.
- **Inicio · Fin:** Abadía de Lebanza (1361 m), 42.96297, −4.55346 ✅.
- **Temporada · Riesgos:** brecha rocosa. La orientación de la circular es exigente (O = 4).
- **Agua · Refugios:** prado con lagunas.
- **Waypoints:** 
  - WP1 · km 0 · Abadía · 1361 m · 42.96297, -4.55346
  - WP2 · km 1,27 · Cruce Arroyo · 1437 m · 42.9684, -4.56089
  - WP3 · km 1,68 · Prado · 1473 m · 42.96711, -4.56491
  - WP4 · km 2,44 · Prado Alto · 1605 m · 42.96679, -4.57388
  - WP5 · km 3,8 · Collado Hontanillas · 1838 m · 42.97211, -4.58486
  - WP6 · km 4,34 · Brecha Rocosa · 1954 m · 42.97502, -4.58305
  - WP7 · km 4,78 · Peña Carazo · 2012 m · 42.97621, -4.57844
  - WP8 · km 5,49 · Collado Horcada · 1894 m · 42.98123, -4.58171
  - WP9 · km 6,18 · Horca De Lores · 2021 m · 42.98628, -4.58296
  - WP10 · km 6,35 · Collado · 1970 m · 42.98754, -4.58301
  - WP11 · km 6,8 · Pequeño Prado · 1836 m · 42.98798, -4.57893
  - WP12 · km 7,52 · El Jardín Sin Flores · 1681 m · 42.98528, -4.57361
  - WP13 · km 7,87 · Prado Con Lagunas · 1666 m · 42.98524, -4.56988
  - WP14 · km 8 · Sendero Escobas · 1671 m · 42.98455, -4.56883
  - WP15 · km 8,21 · Cercado Y Camino · 1689 m · 42.98406, -4.56675
  - WP16 · km 9,06 · Cruce Con Pista · 1511 m · 42.98478, -4.55709
  - WP17 · km 9,44 · Cruce De Pistas · 1488 m · 42.9823, -4.55667
  - WP18 · km 10,4 · Robles Gigantes · 1368 m · 42.98004, -4.54903
  - WP19 · km 11,97 · Bifurcación · 1243 m · 42.97184, -4.5386
  - WP20 · km 12,72 · Bifurcación · 1224 m · 42.96826, -4.53164
  - WP21 · km 15 · Abadía Fin · 1361 m · 42.96297, -4.55346
- **Descripción:** desde la antigua abadía de Santa María de Lebanza, se sube al collado de Hontanillas y por una brecha rocosa a la Peña Carazo (2012 m). Se sigue por el collado de la Horcada hasta la Horca de Lores (2021 m). La bajada pasa por "El Jardín sin Flores", un prado con lagunas y el sendero de Escobas. Regresa entre **robles gigantes** hasta la abadía.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [QR GPX](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-Carazo) ❓.
- **Confianza:** ✅.

#### mp-dip-27 · Pico Lezna (guía)
- **Datos:** IV 21,7 / +1310 / 6 h / 3-3-3-4 · C 23,4 / +1310 / 6 h 45 / 3-3-3-4.
- **Zona:** La Pernía.
- **Inicio:** subida larga desde el valle del arroyo Arauz ⚠️. Véase mp-lezna.
- **Contraste (v2):** Terranostrum "Lores – Pico Lezna" (21,6 km i/v / 997 m / 6 h, media), con GPX: ver `mp-lezna`.

#### mp-dip-28 · Bistruey
- **Datos:** IV 20 / +850 / 7 h / 2-3-3-4 · C 21,7 / +1180 / 8 h / 3-4-3-4.
- **Zona:** La Pernía, límite con Cantabria 🟦.
- **Notas:** hay un track de Wikiloc Piedrasluengas–Peña Bistruey (Astruya)–Cucayo ⚠️. Inicio en la guía no disponible ❓.

#### mp-dip-29 · Peña Labra (2.029 m) por el Callejón, desde el Mirador de Piedrasluengas
- **Zona · Provincia:** La Pernía · Palencia / Cantabria 🟦 (la cumbre está en el límite).
- **Datos:** C 8,9 km / +818 / −818 / 4 h / 3-3-5-3 · IV 7,8 / +830 / 3 h 30 / 3-3-5-3 · alt. mín/máx 1354–2029 m.
- **Inicio · Fin:** Mirador de Piedrasluengas (1354 m), 43.04156, −4.45860 ✅.
- **Temporada · Riesgos:** la subida descrita por el **"Callejón"** obliga a **trepar tres resaltes (III, III+ y II+)**. La vía normal se reserva para la bajada; para subir fácil hay que invertir el sentido. Es zona ULA 2 Tañuga–Piedrasluengas.
- **Agua · Refugios:** **abrevadero** (WP5, 1642 m). Hoya y cascada (WP10).
- **Waypoints:** 
  - WP1 · km 0 · Mirador De Piedrasluengas · 1354 m · 43.04156, -4.4586
  - WP2 · km 0,37 · Caseta · 1383 m · 43.04076, -4.45559
  - WP3 · km 0,7 · Collado · 1440 m · 43.03961, -4.45239
  - WP4 · km 1,41 · Llano Antena · 1573 m · 43.0392, -4.44622
  - WP5 · km 1,94 · Abrevadero · 1642 m · 43.0406, -4.44095
  - WP6 · km 3 · Gran Bloque · 1963 m · 43.04518, -4.43255
  - WP7 · km 3,61 · Callejón · 1954 m · 43.04739, -4.43342
  - WP8 · km 3,93 · Peña Labra · 2029 m · 43.04559, -4.43214
  - WP9 · km 4,44 · Acceso Vía Normal · 1973 m · 43.04477, -4.42698
  - WP10 · km 5,04 · Hoya Y Cascada · 1744 m · 43.04072, -4.4283
  - WP11 · km 6,23 · Camino Ancho · 1505 m · 43.0337, -4.43678
  - WP12 · km 6,86 · Bifurcación · 1492 m · 43.03355, -4.44412
  - WP13 · km 7,38 · Bifurcación · 1432 m · 43.03338, -4.45018
  - WP14 · km 9 · Mirador De Piedrasluengas · 1354 m · 43.04156, -4.4586
- **Descripción:** desde el mirador del puerto de Piedrasluengas, se pasa por una caseta y el llano de la antena hasta un abrevadero y un gran bloque. La vía difícil remonta el Callejón con trepadas y sale a la cumbre de Peña Labra (2029 m), divisoria entre Cantabria y Palencia, con vistas a Picos de Europa. Baja por la vía normal, una hoya y una cascada. El boletín de aludes de AEMET "Sierras del Cordel y Peña Labra" cubre esta zona.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [QR GPX](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-Labra) ❓.
- **Confianza:** ✅.

#### mp-dip-30 · Peña Abismo
- **Datos:** IV 9,8 / +510 / 3 h 30 / 3-3-3-3 · C 12,8 / +827 / 5 h / 3-4-3-3.
- **Zona:** La Pernía, zona de reserva ZR6 Peña del Abismo (sin limitaciones de tránsito según el PUP).
- **Inicio:** no disponible ❓.
- **Nota (v2):** Peña Abismo es la foto 33 del libro 2026; sin datos de ruta.

#### mp-dip-31 · Pico Tres Mares (2.171 m) y Cuchillón (2.174 m), desde el valle de Los Redondos
- **Zona · Provincia:** Alto Pisuerga, La Pernía · Palencia / Cantabria 🟦 (estación de Alto Campoo).
- **Datos:** C 15 km / +1200 / −1200 / 6 h / 3-4-3-3 · IV 13,2 / +1000 / 4 h / 3-3-3-3 · alt. 1.260–2.174 m.
- **Inicio · Fin:** aparcamiento exterior de una mina abandonada (1260 m), rotulado "Aparcamiento de la Cueva del Cobre". **Coordenadas no disponibles: todas las del PDF son erróneas.**
- **Temporada · Riesgos:** "aérea travesía de la cara norte" que **en invierno es muy expuesta**. Laberinto rocoso. Pistas de esquí y telesilla de Alto Campoo 🟦.
- **Agua · Refugios:** chozos en los WP5 (1550 m) y WP22 (1663 m), sin coordenadas.
- **Waypoints** (sin coordenadas: excluir las del JSON): WP1 Mina 0 km 1260 · WP2 Puente 1,74 · WP5 Chozo 3,9 / 1550 · WP6 Piedra en equilibrio y cárcava 4,4 · WP9 Cota y horcada 5,76 / 2026 · WP11 Collado de la pista de esquí 6,43 / 2100 · **WP12 Tres Mares 6,7 / 2171** · WP13 Acceso a la senda de la franja rocosa 7,22 · WP16 Acceso al laberinto rocoso 8,51 / 2100 · **WP18 Cuchillón 9,05 / 2174** · WP19 Collado 9,54 / 2060 · WP22 Chozo 10,97 / 1663 · WP23 Mina 15 / 1260. Coordenadas de referencia de la cumbre de Tres Mares (Mendikat): 43.03800, −4.40429.
- **Descripción:** desde una antigua mina del valle de Los Redondos, cerca de la Cueva del Cobre, se cruza un puente y por pista y senda se sube por chozos y prados calizos. Se alcanza una horcada, un collado en la arista y el collado de la pista de esquí. La cumbre del Pico Tres Mares (2171 m) es divisoria de aguas hacia el Cantábrico, el Atlántico (Duero) y el Mediterráneo (Ebro). La travesía de la franja rocosa y el laberinto calizo llega al Cuchillón (2174 m). La vuelta baja por un sendero muy marcado, un llano herboso y un chozo hasta la mina.
- **Comentarios de usuarios:** véase mp-tres-mares-redondo.
- **Enlaces:** [QR GPX](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Pico-Tres-Mares) ❓.
- **Confianza · Pendiente:** ✅ cifras / ❓ geometría · Pendiente: obtener el GPX o digitalizar.

#### mp-dip-32 · Cotomañinos
- **Datos:** IV 18,8 / +1094 / 7 h / 3-3-3-3 · C 15,2 / +1150 / 6 h 15 / 3-3-3-3.
- **Zona:** La Braña (inferida).
- **Inicio:** no disponible ❓.

#### mp-dip-33 · La Verdiana
- **Datos:** IV 10,4 / +1040 / 5 h / 3-3-5-3 · C 10,8 / +874 / 4 h 30 / 3-3-5-3.
- **Zona:** La Braña (inferida).
- **Notas:** la subida se describe por la vía difícil (MIDE de desplazamiento 5); hay que invertir el sentido para hacer la fácil. Figura como punto fotográfico 34 del mapa de palenciaturismo. Inicio no disponible ❓.
- **Nota (v2):** el sinclinal de la Verdiana aparece en las fotos 6 y 34 del libro 2026; sin datos de ruta.

#### mp-dip-34 · Peña Tejedo
- **Datos:** IV 12,4 / +690 / 4 h 30 / 2-3-3-3 · C 11,2 / +745 / 4 h 30 / 2-4-4-3.
- **Zona:** La Braña (inferida).
- **Inicio:** no disponible ❓.

#### mp-dip-35 · Cueto de Comunales
- **Datos:** IV 14,4 / +900 / 5 h 15 / 2-3-2-3 · C 14,3 / +965 / 5 h 30 / 2-4-3-3.
- **Zona:** La Braña / Sierra de Híjar.
- **Notas:** se combina con Valdecebollas (Mendikat 16481). Inicio no disponible ❓.

#### mp-dip-36 · Peña Cildá (1.616 m) y Cueto Morales (1.662 m), desde el Valle de Santullán
- **Zona · Provincia:** La Braña / Santullán, zona ULA 4 Sierra de Corisa y Peña Cilda · Palencia.
- **Datos:** C 21,4 km / +868 / −868 / 7 h 10 / 2-3-3-4 · IV 7,84 / +372 / 2 h 45 / 2-3-3-2 · alt. mín/máx 1066–1662 m.
- **Inicio · Fin:** aparcamiento Senda Ursi, Valle de Santullán (1244 m), 42.90353, −4.34705 ✅.
- **Temporada · Riesgos:** circular larga por pistas. Escombreras mineras.
- **Agua · Refugios:** **merendero con fuente de la Mina del Calero** (WP15, 1274 m). Abrevadero.
- **Waypoints** (WP25 excluido; el fin coincide con el WP1): 
  - WP1 · km 0 · Valle De Santullán · 1244 m · 42.90353, -4.34705
  - WP2 · km 0,48 · Bifurcación Senda Ursi · 1269 m · 42.90621, -4.34347
  - WP3 · km 1,33 · Bifurcación Pista Pradera · 1337 m · 42.91043, -4.33712
  - WP4 · km 2,17 · Bifurcación Pista Alto Del Cerro · 1440 m · 42.91375, -4.32993
  - WP5 · km 2,39 · Collado Camportillo Inicio Pista · 1464 m · 42.9151, -4.33134
  - WP6 · km 3,19 · Bifurcación Pista Minas Mckinley · 1536 m · 42.91668, -4.33952
  - WP7 · km 3,33 · Escombrera Mina · 1558 m · 42.91764, -4.33908
  - WP8 · km 3,53 · Portillo Rocoso · 1607 m · 42.91897, -4.33942
  - WP9 · km 3,92 · Peña Cildá · 1616 m · 42.91684, -4.34241
  - WP10 · km 5,42 · Cueto Morales · 1662 m · 42.92771, -4.33678
  - WP11 · km 5,91 · Pista Collado · 1566 m · 42.92794, -4.33116
  - WP12 · km 7,16 · Bifurcacion Pista Mata Del Fraile · 1420 m · 42.92348, -4.31957
  - WP13 · km 7,69 · Bifurcacion Pista · 1434 m · 42.92726, -4.31851
  - WP14 · km 8,9 · Bifurcacion Pista Camino De La · 1314 m · 42.93219, -4.31827
  - WP15 · km 9,67 · Mina Del Calero · 1274 m · 42.92842, -4.31267
  - WP16 · km 12,73 · Bifurcacion Pista · 1067 m · 42.91547, -4.29328
  - WP17 · km 13,14 · Bifurcacion Sendero · 1066 m · 42.91256, -4.29313
  - WP18 · km 13,29 · Bifurcación Sendero · 1066 m · 42.91176, -4.29353
  - WP19 · km 13,95 · Bifurcación Pistas · 1088 m · 42.90957, -4.29982
  - WP20 · km 14,2 · Bifurcacion Pista · 1114 m · 42.90958, -4.29689
  - WP21 · km 14,53 · Cruce Pistas Escombreras · 1116 m · 42.90763, -4.29909
  - WP22 · km 15,24 · Bifurcacion Cortafuegos · 1104 m · 42.90307, -4.29377
  - WP23 · km 15,85 · Bifurcacion Pista · 1218 m · 42.90192, -4.30021
  - WP24 · km 16,99 · Bifurcacion Senda Ursi Villabe- · 1138 m · 42.89506, -4.30913
  - WP25 · km 21,4 · Valle De Santullán · 1244 m · COORDENADA ERRÓNEA EN PDF (excluir)
- **Descripción:** sigue las marcas del PRC-P 2 (Senda Ursi) y del GR-1 hasta el collado Camportillo. Por la pista de las minas McKinley y sus escombreras se llega a un portillo rocoso y a Peña Cildá (1616 m), con vértice geodésico. La circular continúa al Cueto Morales (1662 m) y baja por pistas de la Mata del Fraile hasta la Mina del Calero, con merendero y fuente. Vuelve por cortafuegos y la Senda Ursi por Villabellaco. Es un paisaje de cuenca minera del carbón, con el Centro de Interpretación de la Minería en Barruelo.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [QR GPX](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-Cilda) ❓.
- **Confianza:** ✅.

#### mp-dip-37 · Valdecebollas (2.142 m), desde Brañosera
- **Zona · Provincia:** La Braña / Sierra de Híjar, Brañosera · Palencia.
- **Datos:** C 16,8 km / +1026 / −1026 / 6 h 20 / 3-3-3-4 · IV 15,18 / +916 / 5 h 45 / 2-3-3-3 · alt. mín/máx 1183–2142 m.
- **Inicio · Fin:** Brañosera (1226 m), 42.93663, −4.30992 ✅.
- **Temporada · Riesgos:** verano. En invierno es un clásico de raquetas y de esquí suave (fuera del MIDE).
- **Agua · Refugios:** **Fuentes de la Bodegona de Peñalba**. Majada de la Fuente de Peñablanca con el **Chozo Peñablanca** (WP15). Refugio de Golobar **en ruinas**.
- **Waypoints:** 
  - WP1 · km 0 · Brañosera · 1226 m · 42.93663, -4.30992
  - WP2 · km 0,2 · Inicio Pista · 1244 m · 42.93778, -4.31133
  - WP3 · km 1,91 · Bifurcación Pista · 1321 m · 42.95233, -4.31266
  - WP4 · km 2,45 · Bifurcación Pista · 1356 m · 42.9564, -4.31547
  - WP5 · km 3,01 · Majada · 1420 m · 42.95956, -4.31983
  - WP6 · km 4,96 · Cruce Arroyo · 1753 m · 42.96578, -4.34064
  - WP7 · km 5,37 · Senda Golobar Valdecebollas · 1830 m · 42.96856, -4.34207
  - WP8 · km 6,14 · Collado Sestil · 2039 m · 42.97032, -4.35031
  - WP9 · km 6,82 · Bifurcación Pista · 2062 m · 42.96665, -4.3566
  - WP10 · km 7,59 · Valdecebollas Torreón · 2142 m · 42.96676, -4.36541
  - WP11 · km 8,31 · Giro Izquierda (Sur) · 2065 m · 42.96432, -4.37203
  - WP12 · km 9,39 · Rocas Cascada · 1895 m · 42.95659, -4.3675
  - WP13 · km 10,73 · Rocas Pradera · 1692 m · 42.9496, -4.35797
  - WP14 · km 10,94 · Inicio Sendero · 1657 m · 42.94806, -4.35639
  - WP15 · km 11,63 · Chozo Peñablanca · 1559 m · 42.94679, -4.34859
  - WP16 · km 13,03 · Bifurcación Pista · 1434 m · 42.94611, -4.33517
  - WP17 · km 14,62 · Bifurcación Pista · 1363 m · 42.94079, -4.32599
  - WP18 · km 16,17 · Bifurcación Puente · 1183 m · 42.93801, -4.31636
  - WP19 · km 16,59 · Bifurcación Pista · 1202 m · 42.93619, -4.31233
  - WP20 · km 16,8 · Brañosera · 1226 m · 42.93661, -4.30991
- **Descripción:** desde Brañosera, una pista sube a una majada y cruza un arroyo hasta la senda Golobar–Valdecebollas y el Collado Sestil (2039 m). La cumbre de Valdecebollas (2142 m) tiene torreón, vértice geodésico, altar y grandes hitos. Es el balcón de la Sierra de Híjar sobre el embalse del Ebro y el páramo. La bajada pasa por las rocas de una cascada, una pradera y el Chozo Peñablanca, y regresa por pistas y un puente a Brañosera. La antigua estación de esquí junto a Valdecebollas está cerrada y solo queda el aparcamiento.
- **Comentarios de usuarios:** véase mp-valdecebollas-branosera.
- **Contraste (v2):** ver `mp-valdecebollas-branosera` y `mp-valdecebollas-golobar`. El Refugio de Golobar no es utilizable: es el edificio de un parador inacabado (1973) que hoy se usa como corral (Wikipedia, komoot).
- **Enlaces:** [QR GPX](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Valdecebollas) ❓.
- **Confianza:** ✅.

#### mp-dip-38 · Peña Rubia
- **Datos:** IV 8,4 / +690 / 3 h 30 / 2-3-3-2 · C 11,5 / +780 / 4 h 30 / 3-3-3-3.
- **Zona:** La Lora (inferida).
- **Inicio:** no disponible ❓.

#### mp-dip-39 · Sierra Corisa
- **Datos:** IV 11,8 / +470 / 4 h / 2-3-3-3 · C 19,3 / +1038 / 7 h / 2-3-3-4.
- **Zona:** zona ULA 4 Sierra de Corisa.
- **Inicio:** no disponible ❓.

#### mp-dip-40 · Peña Mesa (1.071 m) y Pico Castillo (1.100 m), desde Villaescusa de las Torres
- **Zona · Provincia:** La Lora / Monumento Natural de Las Tuerces (Pomar de Valdivia – Aguilar) · Palencia.
- **Datos:** C 13,8 km / +535 / −535 / 4 h 30 / 2-3-3-3 · IV 3 km / +190 / 1 h 15 / 2-2-3-1 · alt. mín/máx 883–1100 m.
- **Inicio · Fin:** aparcamiento tras el puente sobre el Pisuerga, Villaescusa de las Torres (883 m), 42.75961, −4.25488 ✅.
- **Temporada · Riesgos:** todo el año (cota baja, inferencia). **Subir a la cima de Peña Mesa exige escalar 10 m (IV).** El tramo pinar-vaguada va sin sendero y es "el tramo más técnico".
- **Agua · Refugios:** sin datos.
- **Waypoints:** 
  - WP1 · km 0 · Villaescusa De Las Torres · 883 m · 42.75961, -4.25488
  - WP2 · km 0,47 · Inicio Senda · 914 m · 42.75801, -4.25011
  - WP3 · km 1,1 · Pradera Y Callejones · 1039 m · 42.75565, -4.2559
  - WP4 · km 1,41 · Peña Mesa · 1071 m · 42.754, -4.25731
  - WP5 · km 2,08 · Pista Y Pinar · 1066 m · 42.74976, -4.25337
  - WP6 · km 3,52 · Bifurcación Pista · 1035 m · 42.74356, -4.23913
  - WP7 · km 5,44 · Desvío Pradera · 1029 m · 42.73881, -4.21692
  - WP8 · km 6,1 · Pista · 1079 m · 42.74298, -4.21246
  - WP9 · km 6,56 · Pico Castillo · 1100 m · 42.74335, -4.2074
  - WP10 · km 7,13 · Ruinas Del Castillo De Gama · 1067 m · 42.74548, -4.20839
  - WP11 · km 7,72 · Gama · 955 m · 42.74769, -4.20847
  - WP12 · km 8,35 · Collado Gama · 1035 m · 42.74655, -4.21297
  - WP13 · km 8,84 · Collado Recuevas · 1021 m · 42.74911, -4.21629
  - WP14 · km 9,35 · Entrada A Recuevas · 928 m · 42.75191, -4.22016
  - WP15 · km 9,93 · Pradera De Recuevas · 979 m · 42.74846, -4.22389
  - WP16 · km 10,23 · Pinar Y Vaguada · 1039 m · 42.74787, -4.2273
  - WP17 · km 10,72 · Cruce De Caminos Zona Alta · 1077 m · 42.7475, -4.23267
  - WP18 · km 11,07 · Bifurcación · 1075 m · 42.7495, -4.23585
  - WP19 · km 12,84 · Cruce De Pistas · 933 m · 42.75718, -4.24294
  - WP20 · km 13,9 · Villaescusa De Las Torres · 883 m · 42.75961, -4.25488
- **Descripción:** desde Villaescusa de las Torres se entra en el **laberinto kárstico de Las Tuerces**, un páramo calizo erosionado en callejones, pasillos y bloques. Por una pradera y callejones se sube a Peña Mesa (1071 m). Se sigue por pista y pinar hasta el Pico Castillo (1100 m) y las ruinas del castillo de Gama, y se baja al pueblo de Gama. El regreso cruza los collados de Gama y Recuevas y entra en el **valle de Recuevas**, "paraíso para los escaladores". Después sube por pinar y vaguada a la zona alta y vuelve por pistas. La zona forma parte del Geoparque Mundial UNESCO Las Loras.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [QR GPX](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-Mesa) ❓.
- **Confianza:** ✅.

### 16.4 Ascensiones y travesías de terceros

#### mp-curavacas-vidrieros · Curavacas por la vía normal (Callejo Grande), desde Vidrieros
- **Zona · Provincia:** Fuentes Carrionas, Triollo / Velilla · Palencia.
- **Datos:** circular o i/v · Mendikat 12,5 km / +1364 m circular (Vidrieros–Curavacas–Hospital), alt. 1.327–2.519 m, ~7 h 56 en total ✅ · i/v 9,5 km / +1170 ✅ · HikingIberia 11,0 km / +1200, "alta (9/15)" ⚠️ · Wikiloc ~11,1 km / ~1196 m, unas 2 h 30 de subida y 2 h de bajada ⚠️.
- **Inicio · Fin:** Vidrieros, 42.9425, −4.6642 ✅. Cumbre 42.97635, −4.67397 (2524 m) ✅.
- **Temporada · Riesgos:** **solo excursionistas experimentados y sin nieve.** Sin señalización, solo algún hito. La pedrera del Callejo Grande es lo más duro, y la trepada final no es para principiantes. Caída de piedras en el conglomerado. **Restricciones por familias de oso** en la cara norte por encima de 1.800 m (resoluciones temporales, hasta el 30-jun o el 30-jul). Zona de reserva R1.
- **Agua · Refugios:** arroyo de Cabriles en la parte baja. No hay agua arriba. Refugio de los Pescadores (posición discutida, ~2–5 km sobre Vidrieros por la pista del Carrión, en coche; probablemente abierto). Fuente junto al arroyo de Cabriles en la bajada (Pyrenaica).
- **Waypoints clave** (comunes con mp-dip-12): Vidrieros 42.94238, −4.66465 · Prados de Cabriles 42.95654, −4.67007 · vadeo 42.96095, −4.67176 · inicio del Callejo Grande 42.97164, −4.67022 (2075 m) · Collado del Hospital 42.97238, −4.66719 (2154 m) · Horcada del Callejo Grande 42.97713, −4.67241 (2465 m) · cumbre 42.97634, −4.67395.
- **Descripción:** es el itinerario más repetido del parque. Desde Vidrieros se sube por el valle del arroyo Cabriles y sus prados hasta el pie del macizo. Se remonta la pedrera del **Callejo Grande**, un largo canal de conglomerado, hasta la Horcada, y una trepada final corta lleva a la cumbre (2524 m). Desde ella se ven el Espigüete, Peña Prieta y los lagos de la vertiente norte. Se puede cerrar en circular por el Pico Hospital y el Monte de las Huelgas, bajando por el collado Mollorente.
- **Comentarios de usuarios** ⚠️: "no hay señalización, solo algún hito"; "inicio fácil, luego pedrera y trepada final". El autor de un track recomienda sumar un grado si se tiene poca experiencia. Un track de Wikiloc acumula unas 83.880 visitas.
- **Cifras de contraste (v2):** komoot 10,17 km / +1.064 / ~5 h 40, difícil, desde el aparcamiento de Vidrieros (42.94161, −4.66191; 1.335 m) ✅ · otra ruta de komoot 10,3 km / +1.090 ⚠️ · Gulliver +1.204 ⚠️. Es la ruta más popular de la zona de Triollo según komoot.
- **Itinerario y avisos (v2):** se cruza varias veces el arroyo de Cabriles por piedras (con deshielo puede complicarse ❓); al final del Callejo Grande, trepada corta. Varias fuentes la limitan a **junio–octubre y sin nieve** sin conocimientos de alpinismo. Al bajar, fuente junto al arroyo de Cabriles, cerca de Vidrieros (Pyrenaica 286). Hay dos variantes de nombre propio: Callejo Grande y "senda del notario". Rebecos frecuentes en el Callejo Grande.
- **Contexto (v2, Wikipedia, reformulado):** es la cumbre más alta situada íntegramente en Palencia. Es de conglomerado oscuro (el "conglomerado de Curavacas"), cubierto de líquenes que le dan un tono verdinegro, y tiene tres cimas: Este (la más alta), Medio y Oeste. La cara sur es la fácil; la noreste es una de las paredes más difíciles de la Cordillera Cantábrica. Al pie de la cara norte quedan lagunas glaciares (Pozo Curavacas y Pozos del Ves). La primera ascensión deportiva conocida es de agosto de 1947, del notario de Cervera Luis García Guinea, de ahí la "senda del notario". En abril de 1957 una nevada atrapó a la "Cordada de los Faquires" y murieron tres montañeros; en enero de 2010 un alud mató a dos escaladores. En el Alto del Ves se explora desde el 2000 una sima de −322 m. Flora: siempreviva en el piso alpino; brezo y arándano en las faldas.
- **Comentarios (v2):** "ascensión muy dura por la pedrera; hace falta alguna trepada" (komoot, 21-09-2022); vistas del Pozo Curavacas y de la Curruquilla (15-05-2023). Rescates en la cara N sin fecha verificada (Vozpópuli, El Mirón de Soria) ⚠️.
- **Refugios (v2):** Cabaña de Mollorente (ladera S del Pico Pando, 3 plazas, fuente a <100 m; pista desde la iglesia de Vidrieros no apta para vehículos) ⚠️.
- **Enlaces:** [Mendikat 17352](https://www.mendikat.net/track/curavacas-vidrieros-curavacas-hospital-vidrieros/17352).
- **Licencia · Confianza · Pendiente:** Mendikat / Wikiloc (solo enlazar) · ✅ Mendikat / ⚠️ resto · Pendiente: track propio.

#### mp-curavacas-canal-sur · Curavacas por la Canal Sur (invernal)
- **Zona · Provincia:** Fuentes Carrionas · Palencia.
- **Datos:** alpinismo · ~9,4 km · canal recta de más de 400 m con ~38° de media y 45–60° arriba; sale a ~2.470 m · invernal II/1 (Canal Sur + Callejo Grande) ⚠️. La canal sur central, en roca, llega a III con un paso de V.
- **Inicio · Fin:** Vidrieros. Bajada por el Callejo Grande.
- **Temporada · Riesgos:** de invierno a primavera. **Piolet y crampones imprescindibles** (algunos recomiendan 2 piolets). "Solo expertos". Riesgo de aludes y de caída de piedras. Consultar el boletín de aludes de AEMET (Picos de Europa como aproximación).
- **Descripción:** es la línea invernal clásica del Curavacas: una canal directa en la cara sur hasta la arista cimera. Hay otras vías invernales documentadas: el Corredor Oblicuo ("los tres Curavacas", 13,3 km / +1561 m en Mendikat) y "La Diagonal".
- **Comentarios de usuarios:** "solo expertos" (2021); tramo superior de 35–60° ⚠️.
- **Contexto (v2):** Wikipedia recuerda el alud mortal de enero de 2010 y la tragedia de la Cordada de los Faquires (abril de 1957), atrapada por una nevada repentina: refuerzan el icono "aludes / material invernal".
- **Enlaces:** [Wikiloc 99549660](https://es.wikiloc.com/rutas-alpinismo/canal-sur-del-curavacas-desde-vidrieros-99549660).
- **Licencia · Confianza · Pendiente:** solo enlazar · ⚠️.

#### mp-espiguete-sur · Espigüete por la cara sur (pedrera), desde Cardaño de Abajo
- **Zona · Provincia:** Fuentes Carrionas, Velilla · Palencia.
- **Datos:** i/v · Mendikat 11,2 km / +1183 m ✅ · Terranostrum 12,2 km / +1050 m / ~5 h 45, alta ⚠️ · SummitPost ~1.150 m ⚠️ · alt. ~1.300–2.451 m.
- **Inicio · Fin:** Cardaño de Abajo, ~42.921, −4.764 (plaza 42.92095, −4.76391 ✅). Cumbre 42.94461, −4.79622 ✅.
- **Temporada · Riesgos:** verano. **En la pedrera se superan más de 400 m de desnivel en menos de 1 km**, sobre piedra suelta, peligrosa en descenso. Con nieve, en mayo, hay muchos rescates.
- **Agua · Refugios:** ruinas de chozo en la base de la pedrera (42.93696, −4.79103). **Sin agua en la ruta: llenar en la fuente de Cardaño de Abajo.**
- **Waypoints clave** (de mp-dip-01, bajada): cumbre 42.94462, −4.79617 · fin de la pedrera 42.93873, −4.79102 (1903 m) · ruinas del chozo 42.93696, −4.79103 · pista 42.93264, −4.79262 · loma de Soña 42.93062, −4.78444.
- **Descripción:** es la vía más accesible y frecuentada al Espigüete. Desde Cardaño de Abajo, por la Dehesa de Cardaño y una pista, se llega a la base de la montaña a unos 4 km. Allí empieza la gran pedrera sur, que sube directa a la cumbre: vértice geodésico, buzón y cruz, y vistas a todo Fuentes Carrionas y a la meseta.
- **Comentarios de usuarios** ⚠️: es la vía más frecuentada; un track de Wikiloc acumula unas 25.800 visitas.
- **Cifras de contraste (v2):** Terranostrum 12,2 km i/v / +1.050 / 5 h 45, alta (información: M. Á. Madrid Gómez) · Guía Repsol ~5,5 km y 3 h 30 a la cumbre, ~2 h de bajada ⚠️ · prensa (jun-2025) ~6 km de ida y casi 1.000 m ⚠️.
- **GPX Terranostrum (cálculo propio):** 6,18 km · +1.137 m · alt. 1.323–2.444 m · inicio 42.92153, −4.76374 · fin 42.94459, −4.7962 (a 3,7 km en línea recta del inicio) · GPX solo de subida; termina en la cumbre.
- **Itinerario por tramos (v2, resumen propio):** plaza de Cardaño de Abajo (llenar agua en la gran fuente) → pista de hormigón → a ~500 m, desvío a la izquierda por pista forestal hasta la base (~200 m de desnivel; **no confundir con el vallejo de un arroyuelo**: hay que seguir la pista principal) → pedrera de menos de 1 km y más de 400 m de desnivel, mejor por el **lado derecho del canal**, con roca más firme → cresta ancha final de ~100 m → cumbre. Bajada por el mismo camino.
- **Avisos (v2):** **no hay agua en toda la ruta**. Perro siempre atado; el collado está concurrido en hora punta; las aristas E y N no son para perros (Guía Repsol ⚠️). En marzo de 2026 un club subió en invernal: la Pala Sur hubo que abrirla y la bajada fue penosa con nieve de primavera ⚠️.
- **Contexto (v2, Wikipedia, reformulado):** pirámide caliza aislada, la silueta más reconocible del parque; la vertiente oeste es leonesa (Valverde de la Sierra). Por dentro es muy kárstica. Sus límites geológicos: al norte, el cabalgamiento que encauza el arroyo de Mazobre; al este, el sinclinorio de las Lomas; al sur, las pizarras y areniscas de la Formación Cervera. Tiene un endemismo exclusivo, *Sempervivum giuseppii*, descrito en 1935. La primera ascensión documentada es del geólogo Casiano de Prado (1854); Aymar de Saint-Saud subió en 1892.
- **Enlaces:** [Mendikat 6152](https://www.mendikat.net/track/espiguete-cardano-de-abajo-pista-pedrera-cara-sur-espiguete-inicio/6152).
- **Licencia · Confianza:** solo enlazar · ✅/⚠️.

#### mp-espiguete-norte · Espigüete por la arista este y la cara norte, desde Pino Llano / Mazobre
- **Zona · Provincia:** Fuentes Carrionas · Palencia.
- **Datos:** circular · Mendikat 10,2 km / +1128 m, cresta E "PD inf." y bajada por las canales norte (14-07-2023) ✅ · Terranostrum 9,2 km / +1050 / 6 h ⚠️. Goulotte Norte: 10,2 km / +1090 m (03-2026) ⚠️.
- **Inicio · Fin:** parking de Pino Llano / cascada de Mazobre (42.95167, −4.75889) ✅.
- **Temporada · Riesgos:** en verano, arista PD inf. y paso de II en la arista oeste. **En invierno, los corredores N y NE son alpinismo**: "totalmente desaconsejable tras una nevada por riesgo de aludes", con piolet y crampones imprescindibles. El 16-05-2025 dos montañeros quedaron enriscados en el corredor NE. Hubo rescates en la goulotte norte.
- **Agua · Refugios:** **Refugio de Mazobre** al pie de la cara NE (~10 plazas, en uso). Posible fuente en el aparcamiento de Pino Llano (sin confirmar).
- **Descripción:** combina la subida por la arista este, con la Torre Díaz-Caneja, la Cima Este y destrepes, y la bajada por las canales de la cara norte hacia la cascada de Mazobre. La cara norte tiene circos glaciares bien definidos y conservó nieve permanente durante la Pequeña Edad del Hielo.
- **Comentarios de usuarios:** "muy exigente, mucha pedrera y trepadas"; un montañero desaconsejó subir por la norte en diciembre (2017) ⚠️.
- **Cifras de contraste (v2):** Terranostrum 9,2 km circular / +1.050 / 6 h, alta; **con nieve, piolet y crampones** (información: Pedro Yubero Rivas) · komoot circular 10,1 km · escapadarural "muy alta", +1.050 ⚠️.
- **GPX Terranostrum (cálculo propio):** 9,18 km · +1.197 m · alt. 1.344–2.444 m · inicio 42.95139, −4.76164 · track cerrado (fin a 0 m del inicio).
- **Notas técnicas (v2, Pyrenaica 286 ✅):** la arista este es agradable incluso de noche; la caliza adhiere muy bien; hay un resalte con trepada sencilla antes de la Cima Este y un destrepe corto en un corte de la arista. La bajada por las viras de la cara oeste tiene un destrepe de ~6 m algo comprometido. SummitPost (solo buscador) sitúa una fuente en el aparcamiento de Pino Llano ⚠️.
- **Avisos (v2):** rescates adicionales sin fecha verificable (un montañero con una pierna fracturada en la cara N, evacuado a Riaño; dos enriscados; una montañera herida por una roca) ⚠️. Invernal de marzo de 2026: huella aceptable en la cara N ⚠️. El Refugio de Mazobre, al pie de la cara NE, está en uso (~10 plazas).
- **Enlaces:** [Mendikat 25741](https://www.mendikat.net/track/espiguete-parking-cascada-mazobre-cresta-e-pd-inf-espiguete-canales-norte-f/25741).
- **Licencia · Confianza:** solo enlazar · ✅/⚠️.

#### mp-pena-prieta-cardano · Peña Prieta, Pico del Infierno y Tres Provincias, desde Cardaño de Arriba
- **Zona · Provincia:** Fuentes Carrionas · Palencia / Cantabria 🟦 / León 🟧. La cumbre de Peña Prieta es cántabra.
- **Datos:** Mendikat: por el Pozo Lomas 8,4 km / +1440 m (2009; el track más descargado de la zona, con 4.922 descargas) ✅ · circular por Tres Provincias y el Alto del Ves 20,5 km / +1427 ✅ · por el Tío Celestino 19,3 km / +1282 ✅ · Wikiloc por el Canal de Agujas ~18 km / ~1.150–1.200 ⚠️ · tiempo 7–10 h · dificultad alta por longitud.
- **Inicio · Fin:** Cardaño de Arriba, ~42.970, −4.756 ✅.
- **Cumbres:** Peña Prieta 43.02385, −4.73001 (2539 m) · Infierno 43.02245, −4.73088 (2537 m) · Tres Provincias 43.02104, −4.73803 (2499 m) · Tío Celestino 43.01194, −4.73247 (2396 m) ✅.
- **Temporada · Riesgos:** verano. Sin pasos técnicos, pero larga y en terreno de alta montaña. Zona de reserva R1. Vivac y acampada no permitidos.
- **Agua · Refugios:** Pozo de las Lomas y Laguna de Fuentes Carrionas (tratar el agua). Chozo de la Majada de Fuentes Carrionas.
- **Waypoints clave:** véase mp-dip-06.
- **Descripción:** sube por el valle de las Lomas hasta el Pozo de las Lomas. Desde allí se puede ganar la cresta por la canal de las Agujas de Cardaño, por La Panda o por el Collado del Concejo (2394 m), para alcanzar el cordal fronterizo de Tres Provincias, Pico del Infierno y Peña Prieta. Es el techo de la Cordillera Cantábrica al este de Picos de Europa. Las circulares bajan por el Tío Celestino y el Alto de Fuentes Carrionas, o por la laguna y el Alto del Ves.
- **Comentarios de usuarios:** "sencilla sin tramos difíciles ni pasos técnicos, pero larga" ⚠️.
- **Cifras de contraste (v2):** komoot circular Peña Prieta–Infierno–Tres Provincias ~16,5–17 km, más de 7 h ⚠️ · viajaporlibre ~18 km / +1.600 / 8 h ⚠️.
- **Itinerario (v2, SummitPost por buscador ⚠️):** remontar el río de las Lomas, cruzar un puente, subir a las praderas de la Campiza, dejar la laguna a la izquierda y llegar al collado bajo la cara sur.
- **Contexto (v2, Wikipedia, reformulado):** Peña Prieta es la cumbre más alta del macizo y de la Cordillera Cantábrica fuera de Picos de Europa; la cima es cántabra (Vega de Liébana). "Prieta" significa oscura, por el conglomerado que se ennegrece a la intemperie. De ella arrancan el circo de Riofrío, al norte, y el de la laguna de Fuentes Carrionas, al sur, donde nace el Carrión. El Pico del Infierno, a 171 m al sur, es de facto el techo de Palencia; el Mojón de Tres Provincias une León, Cantabria y Palencia. Plinio el Viejo ya hablaba de un "campo carrinense" con dos fuentes, que se cree que eran estas lagunas.
- **Avisos (v2):** no pisar el Pozo de las Lomas helado. El refugio del club Espigüete, a la salida del pueblo, ya no existe (alud de 2015).
- **Enlaces:** [Mendikat 2698](https://www.mendikat.net/track/pena-prieta-cardano-de-arriba-pozo-lomas-pena/2698).
- **Licencia · Confianza:** solo enlazar · ✅.

#### mp-pena-prieta-llanaves · Peña Prieta desde Llánaves de la Reina 🟧
- **Zona · Provincia:** Vadinia · **León (fuera de Palencia)**.
- **Datos:** ~21,7 km / ~+1.250 m, difícil ⚠️.
- **Descripción:** acceso leonés a Peña Prieta, Tres Provincias y el Infierno. Tiene ficha en Turismo CyL. Interesa como alternativa transfronteriza.
- **Refugios (v2) 🟧:** Cabaña de Naranco (Vega del Naranco, ~3 km al E de Llánaves, 1.534 m, 6 plazas, buen estado; reseña genuina de ~jul-2026), Cabaña Linarucas y Refugio Majada de los Cantos (arroyo Culebrejas) según refugioslibres ⚠️. Por esta ruta se pasa por el Cubil del Can (2.419 m).
- **Enlaces:** [Wikiloc 28662748](https://www.wikiloc.com/hiking-trails/llanaves-de-la-reina-pena-prieta-tres-provincias-pico-del-infierno-28662748).
- **Licencia · Confianza:** ⚠️.

#### mp-pena-prieta-san-glorio · Peña Prieta desde el puerto de San Glorio 🟧🟦
- **Zona · Provincia:** León / Cantabria, fuera del bbox.
- **Datos:** travesía San Glorio → Tres Provincias → Peña Prieta → Cardaño de Arriba, ~7 h 45 ⚠️. Variante por el Cubil del Can.
- **Descripción:** acceso norte por la N-621 (San Glorio, que suele exigir cadenas en invierno). La estación de esquí de San Glorio nunca se construyó.
- **Enlaces:** [Wikiloc 51964148](https://es.wikiloc.com/rutas-senderismo/pena-prieta-desde-san-glorio-51964148).
- **Licencia · Confianza:** ⚠️.

#### mp-cordal-lomas-murcia · Circular Laguna de las Lomas – Peña Prieta – Infierno – Tres Provincias – Cuartas – Guadañas – Matas – Murcia
- **Zona · Provincia:** Fuentes Carrionas · Palencia / límites 🟦🟧.
- **Datos:** ~24 km / ~+2.400 m acumulados ⚠️.
- **Inicio · Fin:** Cardaño de Arriba.
- **Riesgos:** "larga excursión con importante desnivel acumulado y alguna ligera dificultad". Se puede subir y bajar por el mismo sitio.
- **Descripción:** encadena el cordal fronterizo con la cresta de las Agujas de Cardaño (Cuartas, Guadañas, Peñas Malas, Zamurdias, Murcia). Es la mitad occidental de la Integral.
- **Tramos (v2, Pyrenaica 286, en sentido inverso):** Pico Murcia → collado de Peñas Caburdas (2.127 m) → Zamurdias (2.171) → Peñas Malas (2.282) → Frontino (2.197) → Guadañas (2.248) → Cuartas (2.451, buzón con forma de esquís) → Pico de las Lomas (2.444) → lago del Pozo de las Lomas. El único punto de agua es el lago.
- **Enlaces:** [Wikiloc 11808759](https://www.wikiloc.com/mountaineering-trails/laguna-de-las-lomas-pena-prieta-pico-infierno-tres-provincias-cuartas-guadanas-matas-y-murcia-11808759).
- **Licencia · Confianza:** ⚠️.

#### mp-murcia-valcabe · Pico Murcia por Valcabe y Las Cerezuelas
- **Zona · Provincia:** Fuentes Carrionas · Palencia / León 🟧.
- **Datos:** circular · 15,4 km / +1014 m (Mendikat, 16-07-2023) ✅.
- **Inicio · Fin:** Cardaño de Arriba. Cumbre 42.98048, −4.79452 (2351 m).
- **Descripción:** variante reciente de la ruta 03 de la Diputación, por Valcabe y Las Cerezuelas.
- **Variante Terranostrum (v2):** circular de 11,8 km / +1.144 (pág.) / 5 h, media; inicio en el aparcamiento 42.97024, −4.75714; cumbre 42.98045, −4.79450. Pasa por una fuente a ~0,8 km y por el puente del arroyo Valcabe (~0,9 km). La ficha aún cita el "refugio Espigüete" a la salida del pueblo, **destruido en 2015**. Tramo final entre Peña del Castillo y Cardaño con retamas altas ⚠️.
- **GPX Terranostrum (cálculo propio):** 11,8 km · +947 m · alt. 1.410–2.345 m · inicio 42.97024, −4.75714 · track cerrado (fin a 66 m del inicio).
- **Contexto (v2):** el vértice está en el límite León–Palencia, en el cordal Murcia–Cuartas–Las Lomas, con buzón. Dificultad media-baja, **pero con varios accidentes en invierno** (Wikipedia). Desde el collado de Valcabe se suben ~200 m en 350 m hasta una cima rocosa (Pyrenaica).
- **Enlaces:** [Mendikat 28231](https://www.mendikat.net/track/murcia-pico-cardano-de-arriba-pico-murcia-valcabe-las-cerezuelas-cardano-de-arriba-2023-07-16/28231).
- **Licencia · Confianza:** ✅.

#### mp-integral-fuentes-carrionas · Integral de Fuentes Carrionas
- **Zona · Provincia:** Fuentes Carrionas · Palencia / límites 🟦🟧.
- **Datos:** lineal Vidrieros → Cardaño de Abajo o circular · ~33 km · 1 día o 2–3 días · muy exigente ⚠️. **Versión Pyrenaica n.º 286 (I. Ruiz Rotaeche) ✅: 35 km · +3.400 m · 14 h 30 en total · PD+ · más de 20 cotas de más de 2.000 m**, lineal de Pino Llano (1.350 m) a Vidrieros (1.326 m), con dos coches.
- **Inicio · Fin:** Vidrieros → Cardaño de Abajo, con ~15 km de carretera entre ambos para la logística de coches.
- **Temporada · Riesgos:** verano. El tramo Curavacas–collado del Ves es "terreno complicado". **Hay poca agua.** No hay refugio guardado. **El vivac solo es autorizable y la acampada está prohibida** (PORN art. 45.6, PUP 6.2.1), aunque los relatos aconsejen acampar junto a los lagos. El refugio del club Espigüete de Cardaño fue destruido por un alud en 2015.
- **Descripción:** la gran travesía clásica del macizo, diseñada por Luis Alejos en 1981. Sube el Curavacas por el Callejo Grande, baja al collado del Ves y recorre el cordal de las Agujas de Cardaño (Lomas, Cuartas, Guadañas, Peñas Malas, Zamurdias, Murcia). Añade Peña Prieta y termina en el Espigüete, con descenso a Cardaño de Abajo. Una versión de trail enlaza las 5 pozas de Fuentes Carrionas con Peña Prieta.
- **Comentarios de usuarios:** "terreno complicado" entre el Curavacas y el Ves; posible falta de agua ⚠️.
- **Itinerario por tramos (v2, Pyrenaica 286, resumen propio):**
  1. Pino Llano → arista E del Espigüete (de noche, con frontal) → Cima E (2.443 m, trepada sencilla) → **Espigüete** (2.451 m, ~2 h).
  2. Bajada por las viras de la cara O, con un **destrepe de ~6 m** algo comprometido → hitos hasta la arista NO → collado de Arra (1.999) → Pico de la Arra (2.034) → Cutulillos (2.041; terreno roto y escobas).
  3. Hoya de Martín Vaquero (2.112) → Peña del Águila (2.136; canal con algo de ambiente) → Valcabe (2.204) → **Pico Murcia** (2.351; ~200 m en 350 m).
  4. Collado de Peñas Caburdas (2.127) → Zamurdias (2.171) → Peñas Malas (2.282) → Frontino (2.197) → Guadañas (2.248) → **Cuartas** (2.451) → Pico de las Lomas (2.444) → lago del Pozo de las Lomas (mitad de la ruta; única recarga de agua).
  5. Canal empinada al collado de las Agujas de Cardaño / Alto del Concejo → **Tres Provincias** (2.499) → Monte Infierno (2.537) → **Peña Prieta** (2.539) → Alto del Concejo (2.432) → Tío Celestino (2.396) → Calderón (2.274) → Alto del Ves (2.192) → collado del Ves (2.067).
  6. **Hoya Contina** (2.395) → tramo más técnico: destrepe al collado de Soña (2.217) y terrazas y canales de conglomerado (PD) → Curruquilla (2.416) → **Curavacas Oeste** (2.502), "la más vertiginosa", con un destrepe expuesto al bajar → Pico Medio (2.494; se puede rodear por la cara N) → **Curavacas** (2.524).
  7. Brecha y destrepe sencillo a la Torre del Callejo Grande → zigzags y pedrera del Callejo Grande → arroyo de Cabriles (fuente) → Vidrieros.
- **Agua (v2):** la única recarga fue el Pozo de las Lomas (agua de lago filtrada y con pastillas). No encontraron el manantial bajo las Agujas de Cardaño. El autor había bebido 3,5 L a mitad de ruta y con calor se quedaron sin reservas antes del Pico Cuartas. Fuente final junto al arroyo de Cabriles.
- **Consejos (v2):** el verano puede ser caluroso; sube y baja constante por pedregales calizos y trepadas en conglomerado; exige muy buena preparación física y mental. Los autores durmieron en furgoneta en Pino Llano: **pernoctar en vehículo o vivaquear está regulado** (§11) y la app no debe presentarlo como práctica recomendada.
- **Enlaces:** [Wikiloc 1782833](https://www.wikiloc.com/hiking-trails/integral-fuentes-carrionas-circular-2-noches-1782833).
- **Licencia · Confianza:** ⚠️.

#### mp-lezna · Pico Lezna (2.208 m)
- **Zona · Provincia:** La Pernía / Lores · Palencia. Acceso alternativo desde Cucayo 🟦.
- **Datos:** desde Cucayo por el Pumar 21,6 km / +1550 m (Mendikat 2020) ✅ · desde Lores 21,43 km solo ida / +1138, difícil ⚠️ · semicircular desde Lores ~22 km, al menos 8 h ⚠️.
- **Inicio · Fin:** Lores (Palencia) o Cucayo (Cantabria). Cumbre 43.00689, −4.64670 ✅.
- **Riesgos:** muy larga. En la vertiente de Lores pasa por la zona de reserva ZR4 Montejerino (la pista Lores–Pineda por Secarro está permitida del 1-oct al 15-ago).
- **Agua · Refugios:** Chozo de las Tenadas de Lores (8–10 plazas en 2017) ⚠️; candidato localizado en komoot (ver bloque v2).
- **Descripción:** cumbre aislada al norte del valle de Lores, con 473 m de prominencia. La subida casi entera por pista es exigente por el desnivel.
- **Comentarios de usuarios:** "al menos 8 h y 22 km" ⚠️.
- **Variante Terranostrum desde Lores (v2):** i/v 21,6 km / +997 (pág.) / 6 h, media; inicio en Lores 42.99656, −4.53308; cumbre 43.00672, −4.64687 (información: Ayto. de La Pernía) ✅.
- **GPX Terranostrum (cálculo propio):** 10,83 km · +1.071 m · alt. 1.205–2.202 m · inicio 42.99656, −4.53308 · fin 43.00699, −4.64642 (a 9,3 km en línea recta del inicio) · GPX solo de ida.
- **Itinerario por tramos (v2, resumen propio):** pista del arroyo Gerino (a 1 km, no tomar el desvío al molino) → Tenadas de Lores y chozo → Majada de Tañuga → chozos de San Salvador (uno antiguo y otro moderno) → pista en zigzag con el arroyo del Lezna a la izquierda → **tramo final campo a través**, sin camino pero cómodo → cumbre. Vuelta por el mismo camino.
- **Refugios (v2):** candidato a Chozo de las Tenadas de Lores en un "refugio libre" de komoot (43.02377, −4.55316; 1.614 m; chimenea, leña y mesa, 2022) ❓.
- **Contexto (v2, Wikipedia):** separa La Pernía de Cervera, junto a los puertos de Pineda; al sur, la vega de Correcaballos. El Pumar (2.066 m) está a 1,2 km. Las rutas directas salen de Cucayo y de Lores.
- **Enlaces:** [Mendikat 20006](https://www.mendikat.net/track/lezna-cucayo-pico-pumar-lezna-pena/20006).
- **Licencia · Confianza:** ✅/⚠️.

#### mp-valdecebollas-branosera · Valdecebollas desde Brañosera (circular por el Sestil)
- **Zona · Provincia:** Sierra de Híjar · Palencia.
- **Datos:** Mendikat 16,9 km / +1015 m, alt. 1.191–2.142 m (2015, 2.192 descargas) ✅ · por el Cueto de Comunales 18,9 km / +1105 ✅ · Wikiloc 16,78 km / 977 m, "difícil", ~6 h 08 ⚠️ · Komoot 20,5 km / ~1.020 m ⚠️.
- **Inicio · Fin:** Brañosera, 42.9350, −4.3078 ✅ (cementerio, según un track). Cumbre 42.96676, −4.36542 (2143 m).
- **Temporada · Riesgos:** verano. En invierno, raquetas o esquí con el boletín de aludes de Cordel–Peña Labra.
- **Agua · Refugios:** véase mp-dip-37.
- **Descripción:** clásica de la Montaña Palentina oriental. Sube por el valle del Rubagón y el Sestil Alto hasta el torreón cimero. Se puede volver por el Cueto de Comunales. Un track sigue expresamente el libro de la Diputación.
- **Comentarios de usuarios:** sin comentarios. El track de Mendikat solo tiene una nota de moderación.
- **Variante Terranostrum (v2):** "Valdecebollas y El Cueto", lineal o semicircular de 13 km / 4 h 30, del Golobar (42.96736, −4.33682) a Brañosera (42.93659, −4.31027): +300 hasta la cima y −940 hasta Brañosera (pág.) ✅.
- **GPX Terranostrum (cálculo propio):** 13,15 km · +969 m · alt. 1.183–2.138 m · inicio 42.93659, −4.31027 · fin 42.96728, −4.33704 (a 4 km en línea recta del inicio) · recorrido en sentido Brañosera → Golobar.
- **Itinerario por tramos (v2, resumen propio):** Golobar → senda junto al arroyo del Canal hasta el collado entre el Rubagón y el Pisuerga → cordal al Alto Canalejas (2.096 m) → Valdecebollas (2.139 m, plataforma con hitos y vértice) → bajada al SO a El Cueto (2.083 m) y al collado de Pamporquero → pista al E por el valle de Pamporquero → a media ladera, elegir Barruelo (hayedo-robledal) o Brañosera (siguiendo la línea de alta tensión).
- **Contexto (v2, Wikipedia, reformulado):** el macizo de La Cebollera es un contrafuerte sur de la sierra de Híjar. En la cima está el "Torreón", torre cilíndrica escalonada con vértice, placa y buzón. **Desde 1965 se celebra una misa en la cumbre el primer domingo de agosto**: ese día habrá gente. Su vertiente norte cierra el circo glaciar de Covarrés, donde nace el Pisuerga. En invierno nieva mucho y se forman cascadas de hielo. Terranostrum cita túmulos megalíticos de unos 5.000 años en el cordal.
- **Enlaces:** [Mendikat 9607](https://www.mendikat.net/track/valdecebollas-valdecebollas-y-sestil-desde-branosera/9607).
- **Licencia · Confianza:** ✅.

#### mp-valdecebollas-golobar · Valdecebollas desde el refugio del Golobar (corta)
- **Zona · Provincia:** Sierra de Híjar · Palencia.
- **Datos:** 6,23 km / +394 m, fácil ⚠️ · Komoot 5,25 km / ~2 h ⚠️.
- **Inicio:** edificio abandonado del Golobar (no es refugio utilizable; ver v2). Se llega en coche desde Brañosera o Salcedillo por la PP-2204, o desde la Collada si la carretera está cortada por nieve.
- **Temporada:** todo el año. Es el **clásico de raquetas** en invierno.
- **Descripción:** la subida más corta a Valdecebollas, aprovechando la cota del Golobar. Cerca está el mirador M08 del Bosque de los Municipios.
- **Inicio (v2):** Refugio de El Golobar, **42.96718, −4.33678** (Terranostrum; 1.775 m según la página) o 42.96744, −4.33746 (komoot, 1.791 m) ⚠️. **No es un refugio utilizable:** es el edificio de un parador inacabado (1973), propiedad de la Diputación, que hoy se usa como corral (Wikipedia; komoot 2022–2023).
- **Carretera (v2):** Wikipedia la llama **PP-2203** (6,5 km desde el desvío de Salcedillo, 1.840 m, la más alta de la provincia), sin mantenimiento y con desprendimientos; este documento decía PP-2204 ⚠️. La estación de esquí de los años 60 nunca se terminó.
- **Cifras (v2):** komoot ~5,25 km / +380 / ~2 h, la ruta más popular de Brañosera (actualizada en 2026) ⚠️. Variante circular por el Sel de la Fuente: `mp-golobar-sel-fuente-cobre`.
- **Enlaces:** [Wikiloc 15111234](https://es.wikiloc.com/rutas-alpinismo/pico-valdecebollas-desde-el-refugio-del-golobar-15111234).
- **Licencia · Confianza:** ⚠️.

#### mp-penalabra-tresmares · Peña Labra y Tres Mares desde el Mirador de Piedrasluengas
- **Zona · Provincia:** La Pernía · Palencia / Cantabria 🟦.
- **Datos:** circular 13,1 km / +1019 m (Mendikat 2015, 2.450 descargas) ✅ · travesía hasta Santa María de Redondo 15,3 km / +998 m (2023) ✅ · ~5 h.
- **Inicio · Fin:** Mirador de Piedrasluengas, 43.04156, −4.45860 ✅. Cumbres: Peña Labra 43.04556, −4.43221 (2029 m) y Tres Mares 43.03800, −4.40429 (2171 m) ✅.
- **Riesgos:** por la vía normal, media. La vía del Callejón tiene III+. Peña Labra y Tres Mares están en el límite con Cantabria, junto a la estación de Alto Campoo.
- **Agua · Refugios:** abrevadero (43.0406, −4.44095).
- **Descripción:** recorre la divisoria cantábrica desde el puerto de Piedrasluengas, con vistas a Liébana y Picos de Europa. Encadena Peña Labra con el Tres Mares, la cumbre divisoria de las tres vertientes. La variante en travesía baja al valle de Los Redondos y a Fuente Cobre.
- **Contexto (v2, Wikipedia y libro 2026, reformulado):** Peña Labra aparece como "Peña Luenga" en el Libro de la Montería; la cima es palentina y la cresta hace de límite con Cantabria, con una cruz junto al vértice. Wikipedia y el libro dan **2.018 m** para la cima (vértice 2.028,7 m). Hay una disputa toponímica: el IGN llama "sierra de Peña Labra" a lo que tradicionalmente es la **sierra de Híjar**. **Tres Mares es la única cumbre peninsular que vierte a tres mares**: Nansa (Cantábrico), Híjar–Ebro (Mediterráneo) y Pisuerga–Duero (Atlántico). Antes se llamaba "Pico Negro" o "Pico de los Asnos"; su cresta es de conglomerado cuarcítico triásico y una pista de Alto Campoo llega a la cima. La sierra de Híjar tiene más de diez cuencas glaciares de entre 70.000 y 18.000 años.
- **Comentarios (v2, komoot ✅):** el mirador de Piedrasluengas, "gran recompensa tras una larga subida" (13-09-2026); desde Tres Mares se ve el arranque del camino a Peña Labra (28-09-2026). El libro 2026 presenta Peñalabra como el mejor mirador del parque, a 1 km de El Campo. Desde el mirador sale también la "Senda de los Rojos", por el límite con Cantabria (sin ficha).
- **Enlaces:** [Mendikat 9610](https://www.mendikat.net/track/penalabra-mirador-de-piedrasluengas-penalabra-tres-mares/9610).
- **Licencia · Confianza:** ✅.

#### mp-tres-mares-redondo · Tres Mares y Cuchillón desde Santa María de Redondo
- **Zona · Provincia:** Alto Pisuerga · Palencia / Cantabria 🟦.
- **Datos:** circular 18,8 km / +1224 m (Mendikat 2018) ✅.
- **Inicio · Fin:** Santa María de Redondo, ~42.988, −4.383 (caja de Mendikat) ⚠️. El aparcamiento real de Fuente Cobre está en 42.99156, −4.42791 (palenciaturismo, v2) ✅; la caja de Mendikat parece desplazada.
- **Descripción:** circular por la cabecera del Pisuerga que incluye la Cueva del Cobre. Equivale a la ruta 31 de la Diputación, cuyas coordenadas son erróneas.
- **De paso (v2):** a ~3 km del aparcamiento, por el camino hacia el Tres Mares, queda el Ribero Pintado (`mp-ribero-pintado`).
- **Enlaces:** [Mendikat 14232](https://www.mendikat.net/track/tres-mares-santa-maria-de-redondo-pico-tres-mares-cuchillon-santa-maria-de/14232).
- **Licencia · Confianza:** ✅.

#### mp-pico-cordel · Pico Cordel 🟦
- **Zona · Provincia:** Alto Campoo · **Cantabria (fuera de Palencia)**.
- **Datos:** desde Brañavieja ~5,1 km solo ida / ~+469 m ⚠️. Altitud 2.051 o 2.061 m según la fuente.
- **Descripción:** no hay una ruta "Pico Cordel desde Piedrasluengas" como tal. El acceso fácil es por Brañavieja o Palombera. Da nombre al boletín de aludes de AEMET.
- **Enlaces:** [Wikiloc 3285945](https://www.wikiloc.com/hiking-trails/ascension-al-pico-cordel-2061-m-desde-branavieja-ida-3285945).
- **Licencia · Confianza:** ⚠️.

#### mp-pena-redonda · Peña Redonda (variantes de Traspeña, Tosande, Burrián y Rebanal)
- **Zona · Provincia:** Sierra del Brezo · Palencia.
- **Datos:** desde Traspeña por el Burrián y el barranco de Santa Eulalia: 12,7 km / +1011 m (Mendikat 2018) ✅ · por el valle de Tosande desde su aparcamiento: 10,1 km / +1118 m (Mendikat 2009) ✅ · desde Villanueva por el collado de Burrián: ~12 km / ~904 m ⚠️ · circular con el Pico Rebanal: ~15,7 km / 1028 m ⚠️ · moderada.
- **Inicio · Fin:** Traspeña ~42.819, −4.589 ⚠️ · Tosande 42.82578, −4.51656 ✅ · Villanueva de la Peña 42.82929, −4.62401 ✅. Cumbre 42.85160, −4.61330 (1995 m) ✅.
- **Riesgos:** **las sendas del barranco están poco marcadas y es fácil perderse.** La bajada es calurosa. Desde Rebanal, el tramo final está mal marcado. Zona de reserva ZR2.
- **Descripción:** la ruta más usada por los locales sale de Traspeña. En la cumbre hay una cruz metálica de unos 14 m, y se sube en romería el primer domingo de agosto.
- **Comentarios de usuarios:** véase el riesgo de orientación ⚠️.
- **Contexto (v2, Wikipedia, reformulado):** caliza, entre Castrejón de la Peña y Cervera; la cruz metálica de la cima le hace "superar" los 2.000 m. Tiene vértice y una caseta con una Virgen. **Por la mañana suele estar cubierta de niebla** (refuerza el aviso de orientación). Acceso habitual desde Traspeña por pista hasta una cantera abandonada y luego senda con hitos por la cara sur hasta el hombro este. Romería a la Virgen de las Cumbres el primer domingo de agosto. Es la "barriga" del Gigante de la leyenda (ver `mp-of-gigante`).
- **Cifras de contraste (v2):** komoot ~13,8 km / +820, difícil ⚠️. No hay ficha en Terranostrum ni crónicas de 2024–2026.
- **Enlaces:** [Mendikat 14227](https://www.mendikat.net/track/pena-redonda-traspena-pena-redonda-burrian-barranco-de-santa-eulalia-traspena/14227).
- **Licencia · Confianza:** ✅/⚠️.

#### mp-fraile · Pico o Peña del Fraile (variantes de Cristo Sierra y del Santuario del Brezo)
- **Zona · Provincia:** Sierra del Brezo · Palencia.
- **Datos:** Cristo Sierra – Peña del Fraile – Cueto: 7,9 km / +572 m (Mendikat, 19-07-2025, el track más reciente) ✅ · desde el Santuario del Brezo: 11,5 km / +940 m ✅ (Komoot 12,9 km) · desde Santibáñez: véase mp-dip-18.
- **Cumbre:** 42.83289, −4.76550 (2001 m, 595 m de prominencia) ✅.
- **Descripción:** es la cumbre más alta de la Sierra del Brezo. La variante corta desde Cristo Sierra es la de menor desnivel. El Santuario de Nuestra Señora del Brezo es punto de partida de una versión de trail.
- **Variante Terranostrum (v2):** circular desde Santibáñez de la Peña (antiguas escuelas, 42.80945, −4.72989): 12 km / +898 / 5 h, media-alta; en nieve, extremar la precaución. Pasa por un túnel bajo la vía del tren, las ruinas de San Román de Entrepeñas (s. X) y Peña Cueto (42.83689, −4.74850); cumbre 42.83277, −4.76553.
- **GPX Terranostrum (cálculo propio):** 11,81 km · +3.173 m · alt. 1.120–2.002 m · inicio 42.80945, −4.72989 · track cerrado (fin a 0 m del inicio) · ⚠️ **discrepancia:** D+ 3.173 frente a 898 m publicados · **altitudes ruidosas: D+ no fiable**.
- **Refugio (v2):** el **Refugio de Cristo Sierra** (6 plazas, chimenea, capilla, fuente a <1 km), en el cruce de pistas entre Valcobero y Valsurbio, es la salida de la variante corta (refugioslibres) ⚠️.
- **Contexto (v2, Wikipedia):** la Sierra del Brezo mide ~30 km entre Guardo y Cervera; es caliza y casi sin árboles (gayuba y brezo). Allí nacen el Valdavia, el Boedo y el Burejo. Wikipedia da 2.025 m al Fraile (frente a 2.001) ⚠️.
- **Enlaces:** [Mendikat 28948](https://www.mendikat.net/track/fraile-pena-del-cristo-sierra-pena-del-fraile-cueto-cristo-sierra/28948).
- **Licencia · Confianza:** ✅.

#### mp-penas-mayores-cordal · Peñas Mayores y cordal de la Sierra del Brezo
- **Zona · Provincia:** Velilla / Guardo · Palencia.
- **Datos:** circular desde Campos de la Peña con el Pico del Fraile: 18,9 km / +1271 m (Mendikat, 2.459 descargas) ✅ · desde el poblado de Compuerto: ~9,7 km ⚠️ · cordal Peñas Mayores–Fraile: ~22,2 km / ~1457 m ⚠️.
- **Descripción:** recorre la cresta caliza de la Sierra del Brezo entre las Peñas Mayores y el Fraile. Se puede acortar volviendo por el asfalto en lugar del pinar.
- **Relacionadas (v2):** `mp-collado-pinar` (Collado del Pinar, 10,7 km) y `mp-pinar-pena-mayor` (subida directa desde Compuerto, sin GPX).
- **Enlaces:** [Mendikat 14584](https://www.mendikat.net/track/mayor-pena-campos-de-la-pena-pena-mayor-pico-del-fraile-campos-de/14584).
- **Licencia · Confianza:** ✅/⚠️.

#### mp-pena-lampa · Peña Lampa (1.804 m)
- **Zona · Provincia:** Velilla · Palencia / León 🟧 (fuera del bbox por el oeste).
- **Datos:** desde Velilla por el Monte Valdehaya y el Collado Verdugo: 9,9 km / +748 m (Mendikat 2019) ✅ · Wikiloc 9,68 km / 657 m, moderada ⚠️ · por la arista SE: 15,5 km circular ⚠️.
- **Cumbre:** 42.86069, −4.86546 ✅.
- **Riesgos:** **cresta afilada**; se gana la arista por la derecha. Hay tráfico de camiones de una mina en la pista: aparcar en la carretera de Besande. En el enebral de Peña Lampa está prohibido cortar árboles o sacar leña (PORN art. 54.C.5).
- **Descripción:** cumbre fronteriza con León sobre Velilla. Tiene un sabinar o enebral protegido y se puede combinar con la Torre Magalana y el Roblón.
- **Comentarios de usuarios:** camiones de mina en la pista; aparcar en la carretera de Besande ⚠️.
- **Relacionada (v2):** `mp-sabinar-pena-lampa` (Terranostrum, 10,2 km circular, máx. 1.803 m). Peña Lampa tiene tres cotas escalonadas y se reparte entre Besande (León) y Velilla. Su sabinar albar es el más septentrional y fue uno de los motivos de la declaración del parque (Wikipedia).
- **Enlaces:** [Mendikat 16265](https://www.mendikat.net/track/pena-lampa-velilla-del-rio-carrion-monte-valdehaya/16265).
- **Licencia · Confianza:** ✅.

#### mp-tremaya · Peña Tremaya (1.441 m)
- **Zona · Provincia:** La Pernía · Palencia.
- **Datos:** circular corta desde Tremaya: ~4,7–5 km / ~+263–269 m / ~1 h 30, sin dificultad, casi todo por pista ⚠️ · desde San Salvador de Cantamuda: 8,88 km circular ⚠️ · travesía desde Brañosera: 22,7 km / +908 m (Mendikat) ✅.
- **Cumbre:** 42.97741, −4.48031 ✅.
- **Riesgos:** la cara norte (mirador de la Leyenda) puede tener hielo.
- **Descripción:** cima fácil y panorámica sobre La Pernía y el valle del Pisuerga. Se combina con la Senda de la Venganza del Conde.
- **Variante Terranostrum (v2):** semicircular desde el puente sobre el Pisuerga, 200 m antes de Tremaya (PP-2176), **42.97937, −4.46532**; final en el molino de Sopeña, a ~1 km por carretera. Pág. 4,7 km / 1 h 30, baja.
- **GPX Terranostrum (cálculo propio):** 6,87 km · +301 m · alt. 1.126–1.424 m · inicio 42.97937, −4.46532 · track cerrado (fin a 7 m del inicio) · ⚠️ **discrepancia:** distancia 6,87 frente a 4,7 km publicados.
- **Itinerario (v2, resumen propio):** camino al sur con un paso canadiense → meseta con una casa de campo → portilla ganadera → senda que rodea la peña hasta la cumbre (42.97739, −4.47976; caseta de vigilancia de incendios y antenas) → bajada rodeando la peña al revés. Fuera del trazado hay aulagas; dejar las portillas como se encuentran.
- **Enlaces:** [Mendikat 10936](https://www.mendikat.net/track/pena-tremaya-branosera-pena-tremaya-tremaya/10936).
- **Licencia · Confianza:** ✅/⚠️.

#### mp-bernorio · Monte Bernorio (1.178 m)
- **Zona · Provincia:** La Lora / Valdivia (Pomar de Valdivia) · Palencia.
- **Datos:** ida y vuelta desde Villarén de Valdivia: 8,1 km / +242 m (Mendikat 2020) ✅ · ~3 h con paradas interpretativas · fácil.
- **Inicio:** Villarén de Valdivia, ~42.777, −4.185 (baja precisión). Hay aparcamiento en la cima. Cumbre 42.79454, −4.19491 ✅.
- **Descripción:** castro prerromano y escenario de las Guerras Cántabras, con recorrido interpretativo de escaso desnivel. Tiene vistas a La Lora, Aguilar y Las Tuerces. Forma parte del catálogo de recursos del Geoparque (F-01).
- **Contexto (v2, Wikipedia, reformulado):** oppidum cántabro de más de 120 ha (la cima plana mide ~28 ha), ocupado del siglo VIII al I a. C. A 2 km, en El Castillejo, hay un campamento romano de más de 18 ha, probablemente de dos legiones, con proyectiles de asedio; tras la conquista fue *castellum* romano. Es BIC desde 1992 y algunos autores lo identifican con la *Bergida* de las guerras cántabras. Quedan parapetos de la Guerra Civil (1936). Está en la Lista Roja de Hispania Nostra por un proyecto eólico. Wikipedia da 1.170 m de altitud.
- **Otras fuentes (v2):** Terranostrum no tiene ruta a pie, solo la BTT `mp-btt-vuelta-bernorio` desde Pomar de Valdivia.
- **Enlaces:** [Mendikat 20178](https://www.mendikat.net/track/bernorio-villaren-de-valdibia-bernorio/20178).
- **Licencia · Confianza:** ✅.

#### mp-cilda-tuerces · Monte Cildá y Las Tuerces (circular)
- **Zona · Provincia:** La Lora, Olleros de Pisuerga / Mave · Palencia.
- **Datos:** circular 10,0 km / +373 m (Mendikat, 13-05-2023) ✅ · fácil.
- **Cumbre:** Monte Cildá 42.75157, −4.27733 (985 m) ✅.
- **Descripción:** une el castro de Monte Cildá (recurso F-02 del Geoparque) con el laberinto de Las Tuerces. Coincide en buena parte con la Ruta Amarilla de Las Tuerces.
- **Waypoint (v2):** castro cántabro-romano de Monte Cildá 42.75140, −4.27740 (Terranostrum, Ruta Amarilla). Desde el Monte Cildá se ve entero el Cañón de la Horadada (Wikipedia).
- **Enlaces:** [Mendikat 25561](https://www.mendikat.net/track/monte-cilda-monte-cilda-las-tuerces/25561).
- **Licencia · Confianza:** ✅.

#### mp-amaya · Peña Amaya 🟪 (FUERA de Palencia)
- **Zona · Provincia:** **Burgos**.
- **Datos:** PRC-BU 200 desde Amaya: 12 km / +400 m / 3 h · circular de 10 km / +540 m desde la iglesia de San Juan Bautista ⚠️. Altitud 1.370–1.377 m.
- **Descripción:** se incluye solo como referencia del Geoparque Las Loras. Hay que marcarla fuera del dominio.
- **Licencia · Confianza:** ⚠️.

### 16.5 Valle y naturaleza

#### mp-pescadores-velilla · Senda de los Pescadores (Velilla del Río Carrión)
- **Zona · Provincia:** Alto Carrión, Velilla · Palencia.
- **Datos:** ida por una orilla y vuelta por la otra · 6 km / 3 h (palenciaturismo) · 6,3 km / 2 h (Terranostrum) · 6,4 km circular, fácil (AllTrails) · el folleto del Centro de la Trucha da 4,3 km · desnivel casi nulo ⚠️.
- **Inicio · Fin:** Centro de Interpretación de la Trucha, en el "paraje del Soto" de Velilla, **42.82599, −4.84857** (palenciaturismo; GPX de Terranostrum 42.82602, −4.84857) ✅. Fin = inicio.
- **Temporada · Riesgos:** todo el año. En invierno puede haber nieve.
- **Descripción:** paseo de ribera por el río Carrión desde el Centro de la Trucha. Recorre unos 3 km por una orilla hasta el "puente del ahorcado" y vuelve por la otra. El folleto lo describe como un tramo entre la presa de Compuerto y la calle La Fragua. Es una buena opción para familias y perros (atados), por ser llano.
- **Comentarios de usuarios:** no hay datos nuevos.
- **Cifras canónicas (v2):** palenciaturismo **6 km circular / +39 m / 3 h, fácil, sendero local no homologado** ✅. El dato de 4,3 km del folleto del Centro parece referirse solo al tramo presa de Compuerto – c/ La Fragua.
- **GPX Terranostrum (cálculo propio):** 6,35 km · +17 m · alt. 1.115–1.140 m · inicio 42.82602, −4.84857 · track cerrado (fin a 33 m del inicio) · ⚠️ **discrepancia:** D+ 17 frente a 39 m publicados.
- **Itinerario y avisos (v2):** ~3 km río arriba hasta el puente del Ahorcado y vuelta por la otra orilla; pasa por la ermita de la Virgen de Areños y por **dos refugios de pescadores**. Las riberas se inundan en crecidas (palenciaturismo).
- **Enlaces:** [palenciaturismo](https://www.palenciaturismo.es/que-hacer/rutas/senda-pescadores).
- **Licencia · Confianza · Pendiente:** Diputación (enlazar) · ✅ cifras e inicio · Pendiente: track propio.

#### mp-valle-pineda · Valle de Pineda desde Vidrieros
- **Zona · Provincia:** Alto Carrión · Palencia.
- **Datos:** circular · 12,63 km / +108 m · fácil ⚠️.
- **Inicio:** Vidrieros, 42.9425, −4.6642.
- **Riesgos:** cierres por cacería en los accesos al Camino Natural de Pineda (22-11-2026).
- **Descripción:** paseo llano por la ribera del alto Carrión, en el valle glaciar de Pineda, al pie del Curavacas. Hacia el Refugio de Santa Marina (libre; ~8 plazas para dormir según refugioslibres, 20 de abrigo según la guía de 2018) se tarda unas 2 h.
- **Refugios (v2):** el Refugio de Santa Marina está junto a la confluencia del arroyo de Arauz con el Carrión, con sitio para dormir ~8 personas; el de Pescadores-Campoluengo (~6 plazas), aguas abajo, probablemente abierto. Ambos con río a <100 m (refugioslibres) ⚠️. Para el trazado completo hasta el Pozo Curavacas ver `mp-pozo-curavacas-pineda` (Terranostrum, con GPX).
- **Enlaces:** [Wikiloc 77588245](https://es.wikiloc.com/rutas-senderismo/vidrieros-rio-carrion-valle-de-pineda-77588245).
- **Licencia · Confianza:** ⚠️.

#### mp-pozo-curavacas-pineda · Pozo Curavacas por el valle de Pineda (a pie o en BTT)
- **Zona · Provincia:** Alto Carrión · Palencia.
- **Datos:** a pie ~20,9 km solo ida, o ~37 km i/v / ~490 m, "difícil", ~8 h ⚠️ · en BTT ~39,9–43 km, 5 h 20 ⚠️ · el lago está a ~1.785–1.800 m.
- **Inicio:** Vidrieros (o Triollo en la versión BTT).
- **Riesgos:** **en BTT, pasada la Vega de Cantos el camino es demasiado empinado y pedregoso**: el final hay que hacerlo a pie. Cara norte del Curavacas, con restricciones temporales por osos.
- **Agua · Refugios:** cabañas de pastores en las vegas de Correcaballos y Cantos. Refugio de Santa Marina.
- **Descripción:** remonta entero el valle de Pineda junto al Carrión hasta la Vega de los Cantos. Una subida final lleva al Pozo Curavacas, la laguna glaciar de la vertiente norte del Curavacas, hacia el chozo del Ves.
- **Cifras Terranostrum (v2):** lineal, **19 km solo ida** / +500 / 6 h 30 (ida), alta por longitud; según la ficha, no ciclable ✅.
- **GPX Terranostrum (cálculo propio):** 18,98 km · +487 m · alt. 1.327–1.785 m · inicio 42.94177, −4.66229 · fin 42.99035, −4.68658 (a 5,8 km en línea recta del inicio).
- **Inicio · Fin (v2):** Vidrieros 42.94177, −4.66229 → **Pozo Curavacas 42.99035, −4.68658** (punto de mapa de Terranostrum) ✅.
- **Itinerario por tramos (v2, resumen propio):** pista del valle de Pineda junto al Carrión, primero al este → puente Pucherín → al norte hasta Santa Marina (refugio, confluencia con el Arauz) → al noroeste por los llanos de la Vega de Correcaballos → El Estrecho, entre el Lezna y el Curavacas → Vega los Cantos, donde el arroyo del Ves baja en cascadas ("Escaleras del Ves") → senda junto a las cascadas hasta el lago glaciar. También se puede seguir la pista, que cruza el río más arriba. Alternativas: Pozo del Ves, Pozo Oscuro y laguna de Fuentes Carrionas.
- **Avisos (v2):** dos vados del Carrión; sin servicios; el invierno exige preparación. La ficha sugiere vivac, pero **el PORN prohíbe acampar** (§11). Fauna citada: oso, lobo, rebeco, tritón alpino y rana bermeja en el pozo, topillo nival.
- **Enlaces:** [Wikiloc 19631676](https://es.wikiloc.com/rutas-senderismo/vidrieros-pozo-curavacas-19631676).
- **Licencia · Confianza:** ⚠️.

#### mp-circular-lagos · Circular de los lagos de Fuentes Carrionas
- **Zona · Provincia:** Fuentes Carrionas · Palencia.
- **Datos:** Nemus da ~16 km / +1.100 m desde Vidrieros como parte de una travesía ⚠️. Las variantes desde Cardaño no tienen cifras.
- **Inicio:** Cardaño de Arriba o Vidrieros.
- **Riesgos:** **alta montaña, no es un paseo.** Zona de reserva R1. No se permite vivac ni acampada.
- **Agua:** lagos (tratar el agua).
- **Descripción:** enlaza el Pozo de las Lomas (~2.080 m), la Laguna de Fuentes Carrionas (2.206 m, 43.01578, −4.73146), el Pozo Curavacas (~1.790 m), los Pozos del Ves y el Pozo de Hoya Contina, que puede estar seco. Recorre el paisaje glaciar mejor conservado del parque: circos, valles en U y lagunas.
- **Datos (v2):** Pozo de las Lomas 43.01047, −4.74287 · Pozo Curavacas 42.99035, −4.68658 (Terranostrum) · Lagos del Ves ~2.050 m, entre el Hoya Contina y la Curruquilla (libro 2026, Wikipedia). Wikipedia da ~2.220 m a la laguna de Fuentes Carrionas (Diputación 2.206). En la Integral, el collado de Soña (2.217 m) queda justo sobre el Pozo del Ves.
- **Enlaces:** [Wikiloc 82945106](https://www.wikiloc.com/mountaineering-trails/pozo-las-lomas-laguna-de-fuentes-carrionas-pozo-curavacas-pozos-del-ves-circular-montana-palentina-82945106).
- **Licencia · Confianza:** ⚠️.

#### mp-mazobre-circular · Cascada y Refugio de Mazobre (circular)
- **Zona:** Alto Carrión · Palencia.
- **Datos:** circular desde Pino Llano · 8,6 km / +379 m ⚠️.
- **Descripción:** amplía el PR-P 6 hasta una segunda cascada y el Refugio de Mazobre, al pie de la cara NE del Espigüete. Véase mp-of-mazobre.
- **Refugio (v2):** el Refugio de Mazobre está en uso, con ~10 plazas para dormir (refugioslibres). Siguiendo el arroyo por una senda de ganado hay más cascadas menores (Terranostrum). Ver `mp-of-mazobre` y la variante larga `mp-mazobre-sima-anillo`.
- **Enlaces:** [Wikiloc 177185185](https://es.wikiloc.com/rutas-senderismo/cascada-y-refugio-de-mazobre-177185185).
- **Licencia · Confianza:** ⚠️.

#### mp-triollo-hornamiel · Triollo – La Lastra – Hornamiel
- **Zona / municipio · Provincia:** Triollo, Alto Carrión / La Pernía · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular ✅ · 9,7 km · +284 m (pág.) · 1.274–1.450 m · 2 h 45 · baja. No ciclable.
- **GPX Terranostrum (cálculo propio):** 9,7 km · +375 m · alt. 1.274–1.450 m · inicio 42.92303, −4.67943 · track cerrado (fin a 3 m del inicio) · ⚠️ **discrepancia:** D+ 375 frente a 284 m publicados.
- **Inicio · Fin:** puente del Carrión en Triollo, 42.92303, −4.67943 (GPX) ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓. Sin dificultades citadas.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** La Lastra 42.91534, −4.66880 · Peña del Oso (vista del valle de Miranda) · Alto de Hornamiel (1.478 m) 42.89713, −4.67082 · puente de hormigón sobre el arroyo de Valderrianes.
- **Itinerario por tramos (resumen propio):** 900 m de pista aguas abajo por la margen izquierda → subida suave a La Lastra → pista al sur → puente de Valderrianes → ladera hasta una pista que sube a la Peña del Oso → rodeo del Alto de Hornamiel → regreso a La Lastra por el fondo de un valle → Triollo.
- **Descripción:** circular por los pueblos del alto Carrión, con vistas al valle de Miranda y al Curavacas. Es zona de berrea; se citan águila real y rastros de lobo.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-triollo-hornamiel).
- **Licencia · Confianza · Pendiente:** Agrupación Comarcal de Desarrollo / Terranostrum (enlazar) · ✅ · Pendiente: track propio.

#### mp-lebanza-linares · Abadía de Lebanza – Refugio de Linares – Hoyo de la Braguilla
- **Zona:** La Pernía · Palencia.
- **Datos:** 11,6 km / ~+446 m ⚠️.
- **Inicio:** Abadía de Lebanza, 42.96297, −4.55346 ✅.
- **Descripción:** alternativa documentada a las "Cascadas de Lebanza", que no aparecen como ruta. Sube desde la abadía hasta el Refugio de Linares (estado ❓) y el Hoyo de la Braguilla.
- **Relacionada (v2):** `mp-polentinos-lebanza` llega a la abadía desde Polentinos (8,9 km i/v). Abadía 42.96283, −4.55313 (Terranostrum), coincidente con la Diputación. La abadía es un edificio neoclásico del s. XVIII, antiguo seminario menor. Las "Cascadas de Lebanza" siguen sin fuente.
- **Enlaces:** [Wikiloc 147075263](https://www.wikiloc.com/hiking-trails/abadia-de-lebanza-refugio-de-linares-hoyo-de-la-braguilla-147075263).
- **Licencia · Confianza:** ⚠️.

#### mp-ruesga-berrea · Embalse de Ruesga (paseo y berrea)
- **Zona:** Cervera · Palencia.
- **Datos:** sin trazado definido. Véase mp-of-ruesga.
- **Temporada:** berrea del 15-sep al 15-oct, al amanecer y al atardecer.
- **Riesgos:** no circular en coche por las pistas (algunas tienen acceso restringido). Contratar empresas de observación autorizadas.
- **Descripción:** es el entorno recomendado para escuchar la berrea del ciervo en el parque.
- **Datos (v2):** se permite el baño en el embalse, con zona de arena y alquiler de patines; la pista de la orilla es agradable (komoot, 2022 y 20-06-2026). Ruesga 42.86402, −4.52766 ⚠️.
- **Licencia · Confianza:** ⚠️.

#### mp-covalagua-corta · Cascada de Covalagua desde Revilla de Pomar
- **Zona · Provincia:** Las Loras, Paisaje Protegido de Covalagua (Pomar de Valdivia) · Palencia.
- **Datos:** circular, señalizada · 5,79 km / +140 m / 1 h 40 · fácil ⚠️.
- **Inicio:** junto a la iglesia de Revilla de Pomar, **42.77071, −4.15124** (GPX de Terranostrum, circular cerrado) ✅.
- **Temporada · Riesgos:** mejor en primavera y otoño. **En estiaje la cascada puede ir casi seca.**
- **Descripción:** paseo por un hayedo muy vistoso en otoño hasta la cascada de Covalagua, un edificio de toba calcárea formado por el agua cargada de carbonatos (recurso C-01 del Geoparque). Sigue un PR, con la cascada a unos 2 km. Cerca está la Cueva de los Franceses, visitable con reserva.
- **Comentarios de usuarios:** cascada casi seca en octubre de 2018 y tras un invierno seco en 2017 ⚠️.
- **Cifras de contraste (v2):** Terranostrum circular señalizada 5,2 km / +90 / 2 h, baja, no ciclable ✅.
- **GPX Terranostrum (cálculo propio):** 5,04 km · +94 m · alt. 994–1.084 m · inicio 42.77071, −4.15124 · track cerrado (fin a 0 m del inicio).
- **Itinerario por tramos (v2, resumen propio):** bajada al fondo del valle → puente de madera → remonte del río Ivia → a ~2 km, balsa y cascada (42.77036, −4.12876) → pasarela hasta la cueva de Covalagua → senda y pista hasta la carretera de Revilla (o vuelta por el mismo camino).
- **Contexto y servicios (v2):** la cueva-surgencia del río Ivia deposita **toba** en gradas que forman pequeñas cascadas; el bosque mezcla hayas en umbría y quejigos en solana, con tejo, acebo y avellano (Wikipedia). Junto a la cascada hay un abrigo con mesas, el "Refugio de Covalagua" (komoot, 42.76982, −4.13132). **La Cueva de los Franceses está cerrada temporalmente por obras** (palenciaturismo, 21-11-2026). La figura de protección vigente (¿Paisaje Protegido o Monumento Natural?) está por confirmar ⚠️.
- **Enlaces:** [Komoot](https://blog.komoot.nl/smarttour/e1068341662/cascada-de-covalagua-desde-revilla-de-pomar-paisaje-protegido-de-covalagua).
- **Licencia · Confianza:** ⚠️.

#### mp-covalagua-integral · Integral de Covalagua (Cueva de los Franceses – Valcabado – Covalagua)
- **Zona:** Las Loras · Palencia.
- **Datos:** Terranostrum 19,7 km / +270 m / 5 h, media ⚠️ · Mendikat 14,6 km / +369 m (2017) ✅, con caja envolvente errónea · variantes desde Pomar de 20,8–27 km ⚠️.
- **Temporada:** primavera y otoño.
- **Descripción:** circular por el páramo de La Lora que enlaza la Cueva de los Franceses, el menhir de Canto Hito, el mirador de Valcabado (1.221 m) y la cascada de Covalagua. Incluye hayedo, karst y megalitismo.
- **Cifras de contraste (v2):** Terranostrum circular 19,7 km / +270 (pág.) / 5 h, media, primavera y otoño. Inicio Revilla de Pomar 42.77094, −4.15180.
- **GPX Terranostrum (cálculo propio):** 19,75 km · +480 m · alt. 956–1.226 m · inicio 42.77094, −4.1518 · track cerrado (fin a 0 m del inicio) · ⚠️ **discrepancia:** D+ 480 frente a 270 m publicados.
- **Itinerario por tramos (v2, resumen propio):** Revilla → cascada (42.77039, −4.12870; salto de 20 m) → Cueva de los Franceses (500 m visitables; **ahora cerrada por obras**) → menhir de Canto Hito (42.76253, −4.11160) y vuelta sobre los pasos → Pozo de los Lobos (42.77374, −4.09390) → pista de regreso a Revilla.
- **Enlaces:** [Mendikat 12349](https://www.mendikat.net/track/valcabado-cueva-de-los-franceses-canto-hito-valcabado-covalagua-cueva-de-los-franceses/12349).
- **Licencia · Confianza:** ⚠️.

#### mp-franceses-lobos · Cueva de los Franceses – Mirador de Valcabado – Pozo de los Lobos
- **Zona / municipio · Provincia:** Revilla de Pomar (Pomar de Valdivia), Las Loras · Palencia (el pozo linda con Cantabria).
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** ida y vuelta · **6,2 km** (el informe daba 5,2 ⚠️) · +72 m (pág.) · 1.125–1.219 m · 2 h · baja · ciclable al 90 % ✅.
- **GPX Terranostrum (cálculo propio):** 3,14 km · +96 m · alt. 1.125–1.219 m · inicio 42.77212, −4.11582 · fin 42.77365, −4.09395 (a 1,8 km en línea recta del inicio) · ⚠️ **discrepancia:** D+ 96 frente a 72 m publicados · GPX solo de ida.
- **Inicio · Fin:** inmediaciones de la Cueva de los Franceses, 42.77212, −4.11582 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año. **La cueva está cerrada temporalmente por obras** (palenciaturismo, 21-11-2026). Sin agua en el páramo. Pequeño cortado junto al pozo.
- **Agua · Refugios:** sin agua.
- **Waypoints clave:** Cueva de los Franceses 42.77306, −4.11672 · **Mirador de Valcabado 42.78185, −4.10251** · **Pozo de los Lobos 42.77353, −4.09419** ✅ (afina la posición anterior, 42.7737, −4.0939).
- **Itinerario por tramos (resumen propio):** pista llana de 1,5 km hasta el mirador de Valcabado → desde su aparcamiento, senda al sureste paralela al cortado unos 830 m → escalones calizos → a ~400 m, un pequeño cortado que da a la ladera de Valderredible, donde está el pozo.
- **Descripción:** une la única cueva turística de Palencia con el mirador del borde del páramo y con una trampa lobera de muros de piedra en embudo. La ficha explica cómo se usaba: una batida con ruido empujaba a los lobos hacia el embudo, que acaba en el pozo.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cueva-de-los-franceses-pozo-de-los-lobos).
- **Licencia · Confianza · Pendiente:** Agrupación Comarcal de Desarrollo / Terranostrum (enlazar) · ✅ · Pendiente: fecha de reapertura de la cueva.

#### mp-ahedo-lobos-valcabado · Hayedo de Monte Ahedo – Pozo de los Lobos – Mirador de Valcabado
- **Zona · Provincia:** Las Loras · Palencia (el Pozo de los Lobos está junto al límite con Cantabria).
- **Datos:** versión de la Diputación: 10 km / +225 m, media ⚠️ · corta desde Valcabado: 3,51 km / +151 m, fácil, 4,7★ con 1 voto ⚠️ · circular larga con Covalagua: ~16 km / 360 m ⚠️.
- **Inicio:** mirador de Valcabado, 42.78174, −4.10273 ✅. Pozo de los Lobos 42.77353, −4.09419 ✅ y mirador de Valcabado 42.78185, −4.10251 (Terranostrum, v2). Monte Ahedo ≈ 42.7824, −4.1029 ⚠️.
- **Riesgos:** sin agua en el páramo.
- **Descripción:** desde el borde del páramo, el único paso practicable y bien marcado baja entre calizas a un hayedo denso. Abajo está el Pozo de los Lobos, una trampa de piedra seca usada entre los siglos VIII y XIX para cazar lobos.
- **Enlaces:** [Wikiloc 24446341](https://es.wikiloc.com/rutas-senderismo/valcabado-hayedo-monte-aedo-pozo-de-los-lobos-valcabado-24446341).
- **Licencia · Confianza:** ⚠️.

#### mp-revelillas-lobos · Revelillas – Pozo de los Lobos 🟦
- **Zona · Provincia:** Valderredible · **Cantabria (fuera de Palencia)**.
- **Datos:** circular · 10,51 km / 4 h · moderada.
- **Riesgos:** el tramo de Revelillas al pozo no está balizado; desde el pozo sigue un PR. Sin agua.
- **Descripción:** sube por robledal y baja por hayedo hasta la trampa lobera, que queda en el límite provincial.
- **Licencia · Confianza:** ⚠️.

#### mp-tuerces-roja · Las Tuerces, Ruta Roja
- **Zona / municipio · Provincia:** Mave → Villaescusa de las Torres → Peña Mesa (Aguilar de Campoo) · Palencia, Monumento Natural de Las Tuerces (Geoparque Las Loras).
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** **lineal** de Mave a Peña Mesa ✅ · 5,6 km · +248 m (cálculo propio) · 883–1.062 m · 2 h · baja · no ciclable.
- **GPX Terranostrum (cálculo propio):** 5,55 km · +248 m · alt. 883–1.062 m · inicio 42.73644, −4.27328 · fin 42.75402, −4.25722 (a 2,4 km en línea recta del inicio).
- **Inicio · Fin:** cartel de rutas de Mave, junto a la carretera a Santa María de Mave, 42.73644, −4.27328 → explanada de Peña Mesa, 42.75402, −4.25722 (Terranostrum) ✅.
- **Temporada · Riesgos / avisos:** todo el año. Tramo junto al borde del cañón (cuidado con niños). Subir a Peña Mesa por los clavos es posible, pero **bajar es delicado**. La antigua harinera de La Horadada es privada: se rodea por arriba.
- **Agua · Refugios:** agua en Mave y en el manantial "potable" junto al cartel de Villaescusa (cruce de las rutas roja, verde y amarilla) ⚠️.
- **Waypoints clave:** Mave 42.73673, −4.27395 · Villaescusa 42.75905, −4.25290 · Peña Mesa 42.75393, −4.25726.
- **Itinerario por tramos (resumen propio):** Mave (marcas rojas) → pista de chopos → harinera de La Horadada (vías de escalada) → senda tallada en la roca al túnel de La Horadada, con vista del cañón del Pisuerga → meseta y borde del cañón → bajada a Villaescusa → subida fuerte al laberinto → Peña Mesa.
- **Descripción:** Pasa por el **Cañón de La Horadada** (recurso D-08 del Geoparque). Las Tuerces es un laberinto kárstico en calizas del Cretácico Superior, en el borde occidental de los páramos de La Lora, donde la Cordillera Cantábrica se encuentra con la cuenca del Duero (Wikipedia). Balizada por el Ayuntamiento de Aguilar.
- **Comentarios de usuarios:** no se encontraron crónicas de 2024–2026.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/las-tuerces-ruta-roja).
- **Licencia · Confianza · Pendiente:** Terranostrum / Ayto. de Aguilar (enlazar) · ✅ · Pendiente: estado del balizado y track propio.

#### mp-tuerces-amarilla · Las Tuerces, Ruta Amarilla
- **Zona / municipio · Provincia:** Mave → Olleros de Pisuerga → Villaescusa → Peña Mesa · Palencia, Monumento Natural de Las Tuerces (Geoparque Las Loras).
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** lineal ✅ · **8,3 km** · +336 m (cálculo propio) · 872–1.062 m · **3 h 30** · baja. Se confirman las cifras dudosas.
- **GPX Terranostrum (cálculo propio):** 8,26 km · +336 m · alt. 872–1.062 m · inicio 42.73542, −4.27509 · fin 42.75402, −4.25725 (a 2,5 km en línea recta del inicio).
- **Inicio · Fin:** Mave 42.73542, −4.27509 → Peña Mesa 42.75402, −4.25725 (Terranostrum) ✅.
- **Temporada · Riesgos / avisos:** todo el año. Tramo intermedio **sin senda y laberíntico** (atención a las marcas). Senda de pescadores estrecha junto al río, con un paso por una roca pulida que entra en el agua. **Paso a nivel con muy poca visibilidad** antes de Villaescusa.
- **Agua · Refugios:** agua en Mave y Villaescusa ⚠️.
- **Waypoints clave:** Olleros (iglesia rupestre de los Santos Justo y Pastor) 42.74454, −4.28612 · Monte Cildá (castro cántabro-romano) 42.75140, −4.27740 · Villaescusa 42.75803, −4.25014.
- **Itinerario por tramos (resumen propio):** carretera hasta Olleros → sendero junto al cementerio hasta una pista que sube al Monte Cildá → borde alto del cañón de La Horadada → bajada sobre los túneles del ferrocarril → chopera (lugar para comer) → senda de pescadores junto al río → puente a Villaescusa → subida a Peña Mesa.
- **Descripción:** Une la ermita rupestre de Olleros, el castro de Monte Cildá y el laberinto. Coincide en buena parte con `mp-cilda-tuerces`.
- **Comentarios de usuarios:** no se encontraron crónicas de 2024–2026.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/las-tuerces-ruta-amarilla).
- **Licencia · Confianza · Pendiente:** Terranostrum / Ayto. de Aguilar (enlazar) · ✅ · Pendiente: estado del balizado y track propio.

#### mp-tuerces-verde · Las Tuerces, Ruta Verde
- **Zona / municipio · Provincia:** Aguilar de Campoo → Villaescusa de las Torres → Peña Mesa · Palencia, Monumento Natural de Las Tuerces (Geoparque Las Loras).
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** lineal ✅ · 7,3 km · +183 m (cálculo propio) · 883–1.069 m · 2 h · baja · **ciclable**.
- **GPX Terranostrum (cálculo propio):** 7,24 km · +183 m · alt. 883–1.069 m · inicio 42.78994, −4.25874 · fin 42.75398, −4.25719 (a 4 km en línea recta del inicio).
- **Inicio · Fin:** zona deportiva de Aguilar de Campoo (cartel), 42.78994, −4.25874 → Peña Mesa 42.75398, −4.25719 (Terranostrum) ✅.
- **Temporada · Riesgos / avisos:** todo el año. Zona árida entre tierras de labor; mismo paso a nivel peligroso que la amarilla.
- **Agua · Refugios:** agua en Aguilar y Villaescusa ⚠️.
- **Waypoints clave:** Aguilar 42.78994, −4.25874 · presa de la piscifactoría · Villaescusa · Peña Mesa.
- **Itinerario por tramos (resumen propio):** pasarela peatonal sobre el río → choperas paralelas al Pisuerga → paso bajo la nacional → a la altura de la presa de la piscifactoría se separa del río → puente a Villaescusa → pista por la base de las paredes → cañón → meseta, donde se une con la rosa → Peña Mesa.
- **Descripción:** La más fácil de las cinco; sigue la ribera del Pisuerga.
- **Comentarios de usuarios:** no se encontraron crónicas de 2024–2026.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/las-tuerces-ruta-verde).
- **Licencia · Confianza · Pendiente:** Terranostrum / Ayto. de Aguilar (enlazar) · ✅ · Pendiente: estado del balizado y track propio.

#### mp-tuerces-rosa · Las Tuerces, Ruta Rosa
- **Zona / municipio · Provincia:** Gama → castillo → pinar → Peña Mesa · Palencia, Monumento Natural de Las Tuerces (Geoparque Las Loras).
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** lineal ✅ · 6,9 km · +180 m (cálculo propio) · 953–1.086 m · 2 h · baja.
- **GPX Terranostrum (cálculo propio):** 6,89 km · +180 m · alt. 953–1.086 m · inicio 42.74776, −4.20809 · fin 42.75399, −4.25717 (a 4,1 km en línea recta del inicio).
- **Inicio · Fin:** cartel de Gama, 42.74776, −4.20809 → Peña Mesa 42.75399, −4.25717 (Terranostrum) ✅.
- **Temporada · Riesgos / avisos:** todo el año.
- **Agua · Refugios:** **no hay manantiales en la meseta**: llevar agua.
- **Waypoints clave:** castillo de Gama (ruinas medievales, gran panorámica) 42.74549, −4.20848 · Peña Mesa.
- **Itinerario por tramos (resumen propio):** senda en revueltas hasta el castillo → pista detrás del castillo → cortafuegos del borde sur del pinar de repoblación, con cruces señalizados (a mitad comparte unos cientos de metros con la azul, que permite volver a Gama por el "camino viejo") → unión con la verde al final del pinar → Peña Mesa.
- **Descripción:** El castillo de Gama corona el Pico Castillo (1.100 m).
- **Comentarios de usuarios:** no se encontraron crónicas de 2024–2026.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/las-tuerces-ruta-rosa).
- **Licencia · Confianza · Pendiente:** Terranostrum / Ayto. de Aguilar (enlazar) · ✅ · Pendiente: estado del balizado y track propio.

#### mp-tuerces-azul · Las Tuerces, Ruta Azul
- **Zona / municipio · Provincia:** Mave → La Rebolleda (🟪 enclave de Burgos) → Villacibio → Gama · Palencia, Monumento Natural de Las Tuerces (Geoparque Las Loras).
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** lineal ✅ · **9,2 km** · +231 m (cálculo propio) · 887–1.069 m · **3 h 30** · baja. Se confirman las cifras dudosas (la ficha general de Las Tuerces dice "de 6 a 10 km, de 2 a 4 h").
- **GPX Terranostrum (cálculo propio):** 9,22 km · +231 m · alt. 887–1.069 m · inicio 42.73563, −4.27225 · fin 42.74775, −4.20811 (a 5,4 km en línea recta del inicio).
- **Inicio · Fin:** Mave 42.73563, −4.27225 → Gama 42.74775, −4.20811 (Terranostrum) ✅.
- **Temporada · Riesgos / avisos:** todo el año. Tramos poco definidos, con marcas en estacas y árboles; la senda se pierde a veces. Subida final a la meseta por una quebrada sin trepada.
- **Agua · Refugios:** **sin agua** salvo en los pueblos.
- **Waypoints clave:** La Rebolleda 42.73184, −4.25667 · ermita rupestre de San Pelayo (Villacibio) · portillo de Villacibio · arroyo de Pradillos (valle de Valseca).
- **Itinerario por tramos (resumen propio):** pista hacia el este y monte bajo → La Rebolleda → senda hasta las rocas de la ermita de San Pelayo → ~400 m de carretera → portillo de Villacibio → bajada al arroyo de Pradillos → subida a la meseta entre encinas → pistas del pinar → bajada a Gama por un cañón bajo el castillo.
- **Descripción:** Única de las cinco que no termina en Peña Mesa; cruza un enclave burgalés.
- **Comentarios de usuarios:** no se encontraron crónicas de 2024–2026.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/las-tuerces-ruta-azul).
- **Licencia · Confianza · Pendiente:** Terranostrum / Ayto. de Aguilar (enlazar) · ✅ · Pendiente: estado del balizado y track propio.

#### mp-tuerces-aguilar · Las Tuerces desde Aguilar de Campoo (circular)
- **Zona:** Aguilar · Palencia.
- **Datos:** 12,33 km / ~+215 m · moderada ⚠️.
- **Descripción:** circular desde Aguilar hasta el laberinto kárstico de Las Tuerces (Monumento Natural y Paisaje Protegido de 782 ha, recurso L-01 del Geoparque). Es zona de escalada, con el sector de Recuevas.
- **Contexto (v2):** las cinco rutas de colores son lineales y cuatro terminan en Peña Mesa; para una circular corta oficial ver `mp-tuerces-villaescusa` (palenciaturismo, 5 km). La figura de protección vigente está por confirmar: Turismo CyL habla de "Paisaje Protegido y Monumento Natural" y palenciaturismo de Monumento Natural "Laberinto de las Tuerces" ⚠️.
- **Enlaces:** [Wikiloc 133377939](https://es.wikiloc.com/rutas-senderismo/las-tuerces-desde-aguilar-de-campoo-133377939).
- **Licencia · Confianza:** ⚠️.

#### mp-geo-villaescusa-ecla · Geo-ruta del Anticlinal de Villaescusa de Ecla
- **Zona · Provincia:** Santibáñez / Villaescusa de Ecla, Geoparque Las Loras · Palencia.
- **Datos:** señalizada y autoguiada con QR · sin cifras ✅.
- **Temporada:** la cascada solo lleva agua en época de lluvias.
- **Descripción:** pasa por el "banco de piedra", los restos de un castro cántabro y el borde de la combe del anticlinal. Llega a la **cascada de La Cervigada** (20 m) y vuelve por el fondo del valle. Es la única geo-ruta palentina documentada en la web del Geoparque (recursos D-11 y C-03).
- **Enlaces:** [Geoparque](https://geoparquelasloras.es/anticlinal-de-villaescusa-de-ecla-geotrack-english-version/).
- **Licencia · Confianza · Pendiente:** Geoparque (enlazar) · ✅ · Pendiente: km, D+ y track.

#### mp-geo-nestar-cordovilla · Entre Nestar y Cordovilla de Aguilar
- **Zona:** Geoparque Las Loras, Aguilar · Palencia.
- **Datos:** circular · 6,1 km / 1,3 h ✅. Ruta ornitológica.
- **Descripción:** pasa por el puente romano de Puente Perdiz.
- **Enlaces:** [Turismo CyL](https://www.turismocastillayleon.com/es/naturaleza/nestar-cordovilla-aguilar).
- **Licencia · Confianza:** ✅.

#### mp-geo-pisuerga-villaescusa · Río Pisuerga en Villaescusa de las Torres
- **Zona:** Geoparque Las Loras · Palencia.
- **Datos:** circular · 3,3 km / 1,3 h ✅. Ruta ornitológica.
- **Descripción:** paseo de ribera por el Pisuerga junto a Las Tuerces.
- **Enlaces:** [Turismo CyL](https://www.turismocastillayleon.com/es/naturaleza/rio-pisuerga-villaescusa-torres).
- **Licencia · Confianza:** ✅.

#### mp-quejigar-hermedes · Quejigar de Hérmedes 🟪 FUERA del ámbito
- **Zona · Provincia:** **El Cerrato** (Hérmedes de Cerrato, 41.82003, −4.17598) · Palencia, pero **fuera de la Montaña Palentina** ✅.
- **Datos:** circuito ornitológico de 2,9 km · 1 h · fácil · con GPX (palenciaturismo).
- **Descripción:** sale del área recreativa del arroyo de San Juan y recorre el páramo y un monte de quejigos (La Dehesa).
- **Enlaces:** [palenciaturismo](https://palenciaturismo.es/que-hacer/rutas/quejigar-hermedes).
- **Licencia · Confianza · Pendiente:** Diputación (enlazar) · ✅ · **Acción: retirar del dominio o marcar como fuera de ámbito.**

### 16.6 BTT y cicloturismo

#### mp-btt-pedaleando-romanico · Pedaleando por el Románico Palentino
- **Zona:** Aguilar / La Lora, Geoparque · Palencia.
- **Datos:** circular · 59,7 km · dificultad alta ✅.
- **Descripción:** ruta BTT de la Diputación entre iglesias románicas del norte de Palencia. Hay GPX en Terranostrum ⚠️.
- **Datos Terranostrum (v2):** 59,7 km / +1.069 / 3 h 30, alta; salida en Aguilar 42.79632, −4.27297.
- **GPX Terranostrum (cálculo propio):** 56,15 km · +722 m · alt. 899–1.086 m · inicio 42.79632, −4.27297 · track cerrado (fin a 6 m del inicio) · ⚠️ **discrepancia:** D+ 722 frente a 1.069 m publicados.
- **Enlaces:** [PDF Diputación](https://palenciaturismo.es/system/files/2020-04/Pedaleando.pdf).
- **Licencia · Confianza:** Diputación (enlazar) · ✅.

#### mp-btt-guia-25 · Guía "Rutas BTT y Cicloturismo en la Montaña Palentina" (25 rutas)
- **Datos:** ©La Pedrera Pindia 2016. Solo están libres las rutas 1, 3, 4, 7, 9, 13, 16, 18, 21 y 24 ✅.
- **Rutas:** 1 Monte Corcos y Valdehaya · 2 Los Campos de la Peña y San Román · 3 Pueblos Abandonados 2.0 · 4 La Sierra del Brezo · 5 Los Hayedos del Valle Estrecho · 6 Los Castros Negros · 7 Valle Aviaos y Río Chico · 8 La Peña de Santa Lucía · 9 La vuelta al Curavacas · 10 Peña del Tejo y El Sillareto · 11 Peña Quebrada · 12 Peña Abismo · 13 Los Valles Oseros · 14 Cueto Polentinos y Peña Tremaya · 15 Sierra Corisa · 16 Valles de Mudá y la Castillería · 17 La vuelta a Peña Cildá · 18 El Golobar, Ujapero y Rojadillo · 19 Valdecebollas · 20 La Vuelta a la Pernía (2 etapas) · 21 La ruta de las Ermitas · 22 La vuelta al pantano de Aguilar · 23 Las Loras · 24 Peña Pico · 25 Gran vuelta a la Montaña Palentina (5 etapas).
- **Riesgos:** la normativa solo permite la bici por pistas y caminos aptos para vehículos (PUP 6.2.6).
- **Enlaces:** [PDF](https://www.diputaciondepalencia.es/system/files/publicacion-pdf/20161221/guia_btt_cicloturismo.pdf).
- **Licencia · Confianza · Pendiente:** ©, solo enlazar · ✅ · Pendiente: fichas de cada ruta.

#### mp-btt-geoparque-tuerces · Itinerario ciclista del Geoparque: Villaescusa – Aguilar por Las Tuerces y Recuevas (2025)
- **Datos:** ❓ ⚠️.
- **Descripción:** itinerario ciclista nuevo del Geoparque por el laberinto de Las Tuerces y el valle de Recuevas.
- **Licencia · Confianza:** ⚠️.

#### mp-btt-tuerces-covalagua · BTT Las Tuerces – Covalagua · y mp-btt-bernorio-gama · Aguilar – Monte Bernorio – Castillo de Gama
- **Datos:** Tuerces–Covalagua ❓ · Aguilar–Bernorio–Gama: 37,9 km, moderada ⚠️.
- **Descripción:** rutas en bici por La Lora que enlazan Las Tuerces, Covalagua, el castro de Bernorio y el castillo de Gama.
- **Nota (v2):** la "Vuelta al Monte Bernorio" de Terranostrum (20,4 km desde Pomar de Valdivia) es otra ruta distinta: ver `mp-btt-vuelta-bernorio`. La BTT "Monumentos Kársticos" (17,7 km desde Villaescusa de las Torres) cubre Las Tuerces: ver `mp-btt-karsticos`.
- **Licencia · Confianza:** Komoot (enlazar) · ⚠️.

### 16.7 Nuevas rutas a pie (v2, 21-11-2026)

Rutas que no estaban en el informe, sacadas de Terranostrum (115 fichas revisadas, 111 con GPX) y de las fichas de palenciaturismo. Mismo formato que el resto. Las cifras "pág." son las de la ficha; las de **GPX (cálculo propio)** salen de `terranostrum_gpx_estadisticas.json`. Las descripciones son resúmenes propios; ⚠️ indica que solo se leyó parte de la ficha. Ninguna de estas rutas está en la red oficial de la Junta salvo que se diga.

**Alto Carrión, Fuentes Carrionas, Velilla y Guardo**

#### mp-cardano-cruz-armada · Cardaño de Abajo – Collado de la Cruz Armada (camino de Binesa)
- **Zona / municipio · Provincia:** Cardaño de Abajo (Velilla del Río Carrión) · Palencia (el collado linda con León 🟧).
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 12 km · +437 m (pág.) · 1.252–1.727 m · 3 h 30 · media-baja.
- **GPX Terranostrum (cálculo propio):** 12,11 km · +512 m · alt. 1.252–1.727 m · inicio 42.92073, −4.76413 · track cerrado (fin a 9 m del inicio).
- **Inicio · Fin:** plaza de Cardaño de Abajo, 42.92073, −4.76413 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año salvo nieve ❓.
- **Agua · Refugios:** fuente grande en la plaza del pueblo (ver §5) ⚠️.
- **Waypoints clave:** collado de la Cruz Armada 42.93251, −4.80969.
- **Itinerario por tramos (resumen propio):** pista al noroeste hacia los Corrales por el "camino de Binesa o Binuesa", entre robledal → collado de la Cruz Armada, donde termina el GR-1 E6 → regreso por otro ramal ⚠️ (descripción leída solo en parte).
- **Descripción:** Circular por la falda sur del Espigüete que enlaza con el final palentino del GR-1. Sirve como alternativa sin cumbre al Espigüete.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cardano-de-abajo-a-la-cruz-armada).
- **Licencia · Confianza · Pendiente:** Agrupación Comarcal de Desarrollo / Terranostrum (enlazar) · ✅ cifras / ⚠️ trazado · Pendiente: track propio.

#### mp-mazobre-sima-anillo · Arroyo de Mazobre y Sima del Anillo, desde Puente Agudín
- **Zona / municipio · Provincia:** Cardaños (Velilla del Río Carrión) · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 13 km · +549 m (cálculo propio) · 1.296–1.794 m · 5 h · media.
- **GPX Terranostrum (cálculo propio):** 12,97 km · +549 m · alt. 1.296–1.794 m · inicio 42.9298, −4.75852 · track cerrado (fin a 0 m del inicio).
- **Inicio · Fin:** aparcamiento de Puente Agudín, 42.92980, −4.75852 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** verano y otoño; con nieve, más difícil ❓. Bajo la cara norte del Espigüete (ver avisos de aludes de `mp-espiguete-norte`).
- **Agua · Refugios:** cascada y arroyo de Mazobre (con tramos secos por filtración); Refugio de Mazobre en uso (~10 plazas).
- **Waypoints clave:** cascada de Mazobre 42.95926, −4.79281 · **Sima del Anillo 42.95505, −4.79818**.
- **Itinerario por tramos (resumen propio):** 3 km por carretera o por el camino de Lamas hasta Pino Llano (antiguo campamento juvenil abandonado) → valle de Mazobre bajo la cara norte del Espigüete → cascada → Sima del Anillo → regreso ⚠️.
- **Descripción:** Versión larga del PR-P 6 que sale desde más abajo, pasa por la cascada y añade la Sima del Anillo, una cavidad kárstica del macizo del Espigüete.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/el-arroyo-de-manzobres-y-sima-del-anillo).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción parcial · Pendiente: estado de la sima (no entrar sin equipo).

#### mp-cueva-dorada · Cueva Dorada desde Camporredondo de Alba
- **Zona / municipio · Provincia:** Camporredondo de Alba (Velilla del Río Carrión) · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** ida y vuelta · 8 km (GPX de ida 3,98) · +325 m · 1.224–1.567 m · 3 h · media.
- **GPX Terranostrum (cálculo propio):** 3,98 km · +343 m · alt. 1.224–1.567 m · inicio 42.89511, −4.74564 · fin 42.89399, −4.71382 (a 2,6 km en línea recta del inicio) · GPX solo de ida.
- **Inicio · Fin:** Camporredondo, 42.89511, −4.74564 → Cueva Dorada, 42.89396, −4.71383 ✅.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** fin en 42.89396, −4.71383.
- **Itinerario por tramos (resumen propio):** monte junto al pueblo, con amplias vistas de las cumbres y del embalse de Camporredondo ⚠️.
- **Descripción:** Excursión corta por el monte que domina Camporredondo, con vistas al Curavacas y al embalse.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cueva-dorada-fuentes-carrionas).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: qué es exactamente la "Cueva Dorada".

#### mp-coriscao · Monte Coriscao (1.569 m) desde Camporredondo de Alba
- **Zona / municipio · Provincia:** Camporredondo de Alba · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 10 km · +320 m (pág.) · 1.234–1.554 m · 3 h 30 · media.
- **GPX Terranostrum (cálculo propio):** 10,14 km · +440 m · alt. 1.234–1.554 m · inicio 42.89467, −4.74735 · fin 42.89564, −4.74925 (a 0,2 km en línea recta del inicio) · ⚠️ **discrepancia:** D+ 440 frente a 320 m publicados.
- **Inicio · Fin:** Camporredondo, 42.89467, −4.74735 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** cerro 42.90374, −4.74454.
- **Itinerario por tramos (resumen propio):** recorrido por bosques hasta la cima. El GR-1 E6 pasa por su desvío ⚠️.
- **Descripción:** Cerro boscoso sobre Camporredondo; buena opción de media montaña cuando las cumbres tienen nieve (inferencia).
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/subida-al-monte-coriscao-fuentes-carrionas).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ D+ · Pendiente: track propio.

#### mp-valsurbio-lobo · Proyecto Lobo: Camporredondo – Valsurbio – Corral de la Valleja
- **Zona / municipio · Provincia:** Camporredondo de Alba · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 11,3 km · +469 m (cálculo propio) · 1.224–1.648 m · 3 h · media-baja.
- **GPX Terranostrum (cálculo propio):** 11,3 km · +469 m · alt. 1.224–1.648 m · inicio 42.89507, −4.74557 · track cerrado (fin a 0 m del inicio).
- **Inicio · Fin:** Camporredondo, 42.89507, −4.74557 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** **evitar el invierno**.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** despoblado de Valsurbio 42.86655, −4.73339 · Corral de la Valleja.
- **Itinerario por tramos (resumen propio):** Camporredondo → Valsurbio (despoblado) → Corral de la Valleja → Camporredondo ⚠️.
- **Descripción:** Ruta del proyecto de cooperación WOLF, que divulga la convivencia entre el lobo y la ganadería.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/de-camporredondo-de-alba-a-valsurbio).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: paneles del proyecto WOLF.

#### mp-valsurbio-compuerto · Por el despoblado de Valsurbio (Compuerto – Valcobero – Valsurbio – Camporredondo)
- **Zona / municipio · Provincia:** Velilla del Río Carrión · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** lineal · 15,5 km · +496 m (cálculo propio) · 1.224–1.690 m · 5 h · media.
- **GPX Terranostrum (cálculo propio):** 15,49 km · +496 m · alt. 1.224–1.690 m · inicio 42.85679, −4.80806 · fin 42.89507, −4.74562 (a 6,6 km en línea recta del inicio).
- **Inicio · Fin:** plataforma del embalse de Compuerto antes del túnel (km 52 de la carretera), 42.85679, −4.80806 ✅ → Camporredondo, 42.89507, −4.74562.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** refugio de Cristo Sierra (6 plazas, fuente a <1 km) en un cruce de pistas entre Valcobero y Valsurbio ⚠️.
- **Waypoints clave:** Valcobero 42.85692, −4.78308 · Valsurbio.
- **Itinerario por tramos (resumen propio):** Compuerto → Valcobero → Valsurbio → Camporredondo (lineal: hace falta dos coches o volver por el mismo camino).
- **Descripción:** Travesía por pueblos abandonados entre los embalses de Compuerto y Camporredondo, al pie de la Sierra del Brezo.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/por-el-despoblado-de-valsurbio).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ · Pendiente: logística de regreso.

#### mp-collado-pinar · Collado del Pinar (Pinar de Velilla) desde Ciudad del Brezo
- **Zona / municipio · Provincia:** Velilla del Río Carrión, Sierra del Brezo · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 10,7 km · +400 m (pág.) · máx. 1.611 m · 4 h · media.
- **GPX Terranostrum (cálculo propio):** 10,67 km · +703 m · alt. 1.160–1.611 m · inicio 42.8486, −4.83557 · track cerrado (fin a 0 m del inicio) · ⚠️ **discrepancia:** D+ 703 frente a 400 m publicados.
- **Inicio · Fin:** aparcamiento de Ciudad del Brezo, 42.84860, −4.83557 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** collado del Pinar (máx. del GPX 1.611 m).
- **Itinerario por tramos (resumen propio):** recorre el pinar autóctono de la ladera noroeste de Peña Mayor desde unos 1.200 m hasta el collado ⚠️.
- **Descripción:** Amplía el PR del Pinar de Velilla hasta el collado bajo las Peñas Mayores. El pinar es uno de los pocos naturales de la Cordillera Cantábrica.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-collado-del-pinar-fuentes-carrionas).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ trazado / ⚠️ D+ · Pendiente: track propio.

#### mp-pinar-pena-mayor · El Pinar de Peña Mayor desde Compuerto
- **Zona / municipio · Provincia:** Velilla del Río Carrión · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** lineal · 4 km · +400 m hasta el collado y +700 hasta Peña Mayor · 2 h 30 · media · **sin GPX**.
- **Inicio · Fin:** poblado de Compuerto ❓ (sin coordenada propia; ver `mp-of-pinar-velilla`).
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** collado del Pinar · Peña Mayor (1.869 m).
- **Itinerario por tramos (resumen propio):** senda pedregosa junto al arroyo, pasada una escombrera → collado → cumbre opcional.
- **Descripción:** Subida directa a las Peñas Mayores por el pinar. Complementa `mp-collado-pinar` y `mp-dip-16`.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/el-pinar-de-pena-mayor).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ⚠️ · Pendiente: GPX y coordenadas.

#### mp-sabinar-pena-lampa · El Sabinar de Peña Lampa (Velilla)
- **Zona / municipio · Provincia:** Velilla del Río Carrión · Palencia / León 🟧 (cumbre compartida con Besande).
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 10,2 km · +554 m (pág.) · 1.140–1.803 m · 3 h 30 · media.
- **GPX Terranostrum (cálculo propio):** 10,16 km · +688 m · alt. 1.140–1.803 m · inicio 42.84085, −4.85707 · track cerrado (fin a 0 m del inicio) · ⚠️ **discrepancia:** D+ 688 frente a 554 m publicados.
- **Inicio · Fin:** Velilla, 42.84085, −4.85707 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓. En el sabinar está prohibido cortar árboles o sacar leña (PORN art. 54.C.5).
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** cordal de Peña Lampa (1.803 m en el GPX; tres cotas escalonadas).
- **Itinerario por tramos (resumen propio):** subida por el sabinar hasta el cordal de Peña Lampa y regreso en circular ⚠️.
- **Descripción:** El sabinar albar de Peña Lampa es el más septentrional de la Península y uno de los motivos de la declaración del parque. Enlaza con `mp-pena-lampa`.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-el-sabinar-de-pena-lampa).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ · Pendiente: track propio.

#### mp-roblon-monasterio · Sendero del Roblón del Monasterio (PRC-P 12)
- **Zona / municipio · Provincia:** Velilla del Río Carrión · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 11,8 km · +310 m (pág.) · 1.139–1.452 m · 3 h 30 · baja · **señalizado (PRC-P 12)**.
- **GPX Terranostrum (cálculo propio):** 11,83 km · +394 m · alt. 1.139–1.452 m · inicio 42.83371, −4.84872 · track cerrado (fin a 10 m del inicio) · ⚠️ **discrepancia:** D+ 394 frente a 310 m publicados.
- **Inicio · Fin:** campo de tiro al noroeste de Velilla, 42.83371, −4.84872 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** Roblón del Monasterio 42.85580, −4.89065.
- **Itinerario por tramos (resumen propio):** sigue el antiguo camino carretero a Besande hasta el roble monumental y vuelve en circular.
- **Descripción:** Sendero de pequeño recorrido municipal homologado que no está en el plano de la Junta. Comparte zona con `mp-pena-lampa`, que también pasa por el Roblón.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-roblon-del-monasterio-prc-p-12).
- **Licencia · Confianza · Pendiente:** CIT Montaña Palentina / Terranostrum (enlazar) · ✅ cifras / ⚠️ homologación · Pendiente: confirmar en FDMESCYL.

#### mp-valdelobos · Sendero de Valdelobos (PRC-P 14), Fresno del Río 🟨
- **Zona / municipio · Provincia:** Fresno del Río · Palencia (periferia sur, al sur de Guardo) 🟨.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 11,8 km · +78 m (pág.) · 1.011–1.089 m · 2 h 45 · baja.
- **GPX Terranostrum (cálculo propio):** 11,85 km · +127 m · alt. 1.011–1.089 m · inicio 42.68089, −4.82386 · track cerrado (fin a 2 m del inicio) · ⚠️ **discrepancia:** D+ 127 frente a 78 m publicados.
- **Inicio · Fin:** área recreativa de Fresno del Río, 42.68089, −4.82386 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** —.
- **Itinerario por tramos (resumen propio):** circular llana por el entorno de Fresno del Río.
- **Descripción:** Sendero homologado municipal en el límite sur del ámbito. En la app, marcar como periferia.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-de-valdelobos-prc-p-14).
- **Licencia · Confianza · Pendiente:** Ayto. de Fresno del Río / Terranostrum (enlazar) · ✅ cifras / ⚠️ homologación · Pendiente: confirmar en FDMESCYL.

**Guardo: red municipal "Senderos de Leyenda" y rutas de J. A. Bardasco** 🟨

#### mp-guardo-brujas · Valle de las Brujas (Guardo)
- **Zona / municipio · Provincia:** Guardo · Palencia (periferia sur del ámbito) 🟨.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 6,2 km · +147 m (pág.) · 1 h 30 · baja.
- **GPX Terranostrum (cálculo propio):** 6,22 km · +212 m · alt. 1.095–1.242 m · inicio 42.78995, −4.84311 · track cerrado (fin a 2 m del inicio) · ⚠️ **discrepancia:** D+ 212 frente a 147 m publicados.
- **Inicio · Fin:** casco de Guardo (≈ 42.790, −4.844; inicio exacto en el GPX).
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** —.
- **Waypoints clave:** robledal de Monte Castro y Fuentefría; senda de las brujas y de los toboganes.
- **Itinerario por tramos (resumen propio):** circular desde Guardo; detalle del trazado en la ficha de origen ⚠️.
- **Descripción:** Evoca la leyenda de las brujas de Cansoles.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-al-valle-de-las-brujas).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: confirmar qué rutas forman la red oficial "Senderos de Leyenda".

#### mp-guardo-balcon-judas · De los Lobos al Balcón de Judas (Guardo)
- **Zona / municipio · Provincia:** Guardo · Palencia (periferia sur del ámbito) 🟨.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 15 km · +396 m (pág.) · 4 h 30 · media.
- **GPX Terranostrum (cálculo propio):** 14,87 km · +628 m · alt. 1.095–1.491 m · inicio 42.78991, −4.84312 · track cerrado (fin a 0 m del inicio) · ⚠️ **discrepancia:** D+ 628 frente a 396 m publicados.
- **Inicio · Fin:** casco de Guardo (≈ 42.790, −4.844; inicio exacto en el GPX).
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** Fuente de la Salud (sin dato de potabilidad) ⚠️.
- **Waypoints clave:** restos de minas de carbón, Monte Castro y la **Fuente de la Salud**.
- **Itinerario por tramos (resumen propio):** circular desde Guardo; detalle del trazado en la ficha de origen ⚠️.
- **Descripción:** Circular larga por el monte minero de Guardo hasta un balcón natural.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-de-los-lobos-al-balcon-de-judas).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: confirmar qué rutas forman la red oficial "Senderos de Leyenda".

#### mp-guardo-merendillas · Ruta de las Merendillas (Guardo)
- **Zona / municipio · Provincia:** Guardo · Palencia (periferia sur del ámbito) 🟨.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 9,8 km · +187 m (pág.) · 2 h 30 · baja.
- **GPX Terranostrum (cálculo propio):** 9,83 km · +256 m · alt. 1.094–1.281 m · inicio 42.78956, −4.84324 · track cerrado (fin a 6 m del inicio) · ⚠️ **discrepancia:** D+ 256 frente a 187 m publicados.
- **Inicio · Fin:** casco de Guardo (≈ 42.790, −4.844; inicio exacto en el GPX).
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** Fuente Ferruginosa (sin dato de potabilidad) ⚠️.
- **Waypoints clave:** mina de Valdecastro, escombreras, **Fuente Ferruginosa** y Cueva del Hoyal (42.80927, −4.81780).
- **Itinerario por tramos (resumen propio):** circular desde Guardo; detalle del trazado en la ficha de origen ⚠️.
- **Descripción:** Circular de patrimonio minero alrededor de Guardo.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-de-las-merendillas-guardo).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: confirmar qué rutas forman la red oficial "Senderos de Leyenda".

#### mp-guardo-corcos · Monte Corcos y Ermita del Cristo del Amparo (Guardo)
- **Zona / municipio · Provincia:** Guardo · Palencia (periferia sur del ámbito) 🟨.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 12 km · +220 m (pág.) · 3 h · baja.
- **GPX Terranostrum (cálculo propio):** 10,78 km · +222 m · alt. 1.090–1.292 m · inicio 42.79048, −4.84548 · fin 42.78995, −4.8555 (a 0,8 km en línea recta del inicio) · ⚠️ **discrepancia:** distancia 10,78 frente a 12 km publicados.
- **Inicio · Fin:** casco de Guardo (≈ 42.790, −4.844; inicio exacto en el GPX).
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** —.
- **Waypoints clave:** Corrales del Sestil (42.80524, −4.88800) y ermita del Cristo del Amparo (42.78030, −4.86632); semicircular (GPX 10,8 km).
- **Itinerario por tramos (resumen propio):** circular desde Guardo; detalle del trazado en la ficha de origen ⚠️.
- **Descripción:** Paseo por el monte de Corcos con final en la ermita.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-monte-corcos-y-ermita-del-cristo).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: confirmar qué rutas forman la red oficial "Senderos de Leyenda".

#### mp-guardo-san-quirce · Valles de San Quirce y Corcos (Guardo)
- **Zona / municipio · Provincia:** Guardo · Palencia (periferia sur del ámbito) 🟨.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 14,3 km · +340 m (pág.) · 4 h · baja.
- **GPX Terranostrum (cálculo propio):** 14,32 km · +344 m · alt. 1.089–1.422 m · inicio 42.79054, −4.84581 · track cerrado (fin a 10 m del inicio).
- **Inicio · Fin:** casco de Guardo (≈ 42.790, −4.844; inicio exacto en el GPX).
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** —.
- **Waypoints clave:** valle de San Quirce y Corcos (42.81521, −4.88809).
- **Itinerario por tramos (resumen propio):** circular desde Guardo; detalle del trazado en la ficha de origen ⚠️.
- **Descripción:** Circular por los valles al oeste de Guardo.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-valles-san-quirce-y-corcos).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: confirmar qué rutas forman la red oficial "Senderos de Leyenda".

#### mp-guardo-circular · Circular de los alrededores de Guardo
- **Zona / municipio · Provincia:** Guardo · Palencia (periferia sur del ámbito) 🟨.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 22 km · +212 m (pág.) · 6 h · media.
- **GPX Terranostrum (cálculo propio):** 21,93 km · +487 m · alt. 1.093–1.291 m · inicio 42.7904, −4.84468 · fin 42.78513, −4.8397 (a 0,7 km en línea recta del inicio) · ⚠️ **discrepancia:** D+ 487 frente a 212 m publicados.
- **Inicio · Fin:** casco de Guardo (≈ 42.790, −4.844; inicio exacto en el GPX).
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** —.
- **Waypoints clave:** Velilla, Muñeca e Intorcisa; necrópolis de Guardo (42.78513, −4.83970); también se puede hacer en bici.
- **Itinerario por tramos (resumen propio):** circular desde Guardo; detalle del trazado en la ficha de origen ⚠️.
- **Descripción:** Gran vuelta a Guardo por los pueblos vecinos.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-circular-alrededores-de-guardo).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: confirmar qué rutas forman la red oficial "Senderos de Leyenda".

#### mp-doncellas-hoyal · Senda de las Doncellas del Hoyal (desde Muñeca)
- **Zona / municipio · Provincia:** Muñeca (Guardo) · Palencia 🟨.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · palenciaturismo 11,97 km / +364 / 3 h 30, fácil, no homologada ✅ · Terranostrum 12 km / +242 / 3 h, media ⚠️.
- **GPX Terranostrum (cálculo propio):** 11,97 km · +391 m · alt. 1.130–1.372 m · inicio 42.79202, −4.80148 · track cerrado (fin a 3 m del inicio) · el GPX descargable de palenciaturismo da el mismo inicio.
- **Inicio · Fin:** plaza de Muñeca, 42.79202, −4.80148 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** —.
- **Itinerario por tramos (resumen propio):** robledal y camino forestal, en circular desde Muñeca.
- **Descripción:** Forma parte de la red municipal "Sendas de Leyenda" de Guardo. **Tiene GPX descargable en palenciaturismo** (ver §15, licencia por confirmar).
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [palenciaturismo](https://palenciaturismo.es/que-hacer/rutas/senda-doncellas-hoyal) · [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/senda-de-las-doncellas-del-hoyal).
- **Licencia · Confianza · Pendiente:** Diputación / Ayto. de Guardo / Terranostrum (enlazar) · ✅ · Pendiente: licencia del GPX.

**La Pernía y Alto Pisuerga**

#### mp-ribero-pintado · El Ribero Pintado (Santa María de Redondo)
- **Zona / municipio · Provincia:** Santa María de Redondo (La Pernía) · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** palenciaturismo: ida y vuelta, 6 km, +107 / −11 (sic), fácil, sendero local sin señalizar ✅ · Terranostrum: circular, 6,2 km, +157, 1 h 30, baja, máx. 1.373 m ⚠️.
- **GPX Terranostrum (cálculo propio):** 6,26 km · +174 m · alt. 1.216–1.373 m · inicio 42.99148, −4.42837 · track cerrado (fin a 0 m del inicio).
- **Inicio · Fin:** parking de Fuente Cobre, 42.99148, −4.42837 ✅ (el GPX de palenciaturismo empieza en 42.99154, −4.42821).
- **Temporada · Riesgos / avisos:** todo el año; evitar las épocas de mucha nieve.
- **Agua · Refugios:** arroyo Lombatero (sin tratar no es potable).
- **Waypoints clave:** **Ribero Pintado 43.01087, −4.41972** ✅.
- **Itinerario por tramos (resumen propio):** a ~3 km por el camino hacia el Tres Mares, junto al arroyo Lombatero, se llega a la antigua explotación; vuelta por el mismo camino o en circular.
- **Descripción:** Antigua explotación a cielo abierto que dejó a la vista estratos de areniscas rojizas (por óxidos de hierro) y lutitas negras ricas en materia orgánica; los colores cambian con la luz y la lluvia. Es la foto 19 del libro 2026. **Tiene GPX descargable en palenciaturismo.**
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [palenciaturismo](https://palenciaturismo.es/que-hacer/rutas/ruta-ribero-pintado) · [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-del-ribero-pintado).
- **Licencia · Confianza · Pendiente:** Ayto. de La Pernía / Diputación / Terranostrum (enlazar) · ✅ · Pendiente: licencia del GPX oficial.

#### mp-bocaron-casavegas · Bocarón de Casavegas / Ojo de Caloca (Mirador de Cerradillo)
- **Zona / municipio · Provincia:** Casavegas (La Pernía) · Palencia (el ojo mira a Cantabria 🟦).
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** ida y vuelta · 8,4 km (GPX de ida 4,23) · +308 m (pág.) · 1.221–1.529 m · 3 h 30 · baja.
- **GPX Terranostrum (cálculo propio):** 4,23 km · +334 m · alt. 1.221–1.529 m · inicio 43.02222, −4.51268 · fin 43.03105, −4.54289 (a 2,6 km en línea recta del inicio) · GPX solo de ida.
- **Inicio · Fin:** fuente, lavadero y pilón de Casavegas, 43.02222, −4.51268 ✅ → **Bocarón 43.03104, −4.54301**.
- **Temporada · Riesgos / avisos:** todo el año ❓. En la bifurcación final, el ramal de la derecha baja a Caloca (Cantabria).
- **Agua · Refugios:** fuente y pilón en Casavegas.
- **Waypoints clave:** Bocarón 43.03104, −4.54301.
- **Itinerario por tramos (resumen propio):** pista con vistas de Peñalabra → bosquete de hayas y robles → collado → bifurcación → arco de roca ⚠️.
- **Descripción:** El "Ojo de Caloca" o Bocarón es un arco de roca desde el que se ve abajo el pueblo cántabro de Caloca (foto 38 del libro 2026).
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/bocaron-de-casavegas).
- **Licencia · Confianza · Pendiente:** Casavegas.es / Terranostrum (enlazar) · ✅ · Pendiente: track propio.

#### mp-redondo-bismo · San Juan de Redondo – Corrala de Bismo
- **Zona / municipio · Provincia:** San Juan de Redondo (La Pernía) · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 9,5 km · +371 m (pág.) · 1.197–1.444 m · 3 h · baja.
- **GPX Terranostrum (cálculo propio):** 9,51 km · +373 m · alt. 1.197–1.444 m · inicio 42.98999, −4.44842 · track cerrado (fin a 14 m del inicio).
- **Inicio · Fin:** iglesia de San Juan de Redondo, 42.98999, −4.44842 ✅ (la ficha pone por error "San Román de Redondo"). Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** Corrala de Bismo 43.02358, −4.44320.
- **Itinerario por tramos (resumen propio):** pista al norte → a 420 m, bifurcación a la izquierda → subida suave de ~700 m → corrala → regreso en circular ⚠️.
- **Descripción:** Circular ganadera por el valle de los Redondos, cerca de Fuente Cobre.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-san-juan-de-redondo-corrala-de-bismo).
- **Licencia · Confianza · Pendiente:** Agrupación Comarcal de Desarrollo / Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: track propio.

#### mp-polentinos-lebanza · Polentinos – Abadía de Lebanza
- **Zona / municipio · Provincia:** Polentinos – Lebanza (La Pernía) · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** ida y vuelta · 8,9 km · +211 m (pág.) · 1.186–1.406 m · 2 h 10 · baja · ciclable.
- **GPX Terranostrum (cálculo propio):** 8,89 km · +384 m · alt. 1.186–1.406 m · inicio 42.93841, −4.52466 · track cerrado (fin a 0 m del inicio) · ⚠️ **discrepancia:** D+ 384 frente a 211 m publicados.
- **Inicio · Fin:** plaza del Ayuntamiento de Polentinos, 42.93841, −4.52466 ✅ → Abadía de Lebanza, 42.96283, −4.55313.
- **Temporada · Riesgos / avisos:** todo el año ❓. Zona de oso y lobo. Polentinos es zona de reserva ZR5 (acceso restringido fuera de pistas autorizadas).
- **Agua · Refugios:** abrevadero en el alto (no potable).
- **Waypoints clave:** alto con abrevadero · collado Mojoncillo · abadía 42.96283, −4.55313.
- **Itinerario por tramos (resumen propio):** pista ganadera al noroeste → alto con abrevadero → collado Mojoncillo → bajada a la abadía; vuelta por el mismo camino.
- **Descripción:** La Abadía de Lebanza es un edificio neoclásico del s. XVIII, antiguo seminario menor, hoy con uso marginal en verano. Vistas al Curavacas. No son las "Cascadas de Lebanza", que siguen sin fuente.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-polentinos-abadia-de-lebanza).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ trazado / ⚠️ D+ · Pendiente: track propio.

#### mp-vidrieros-pie-curavacas · De Vidrieros a los pies del Curavacas
- **Zona / municipio · Provincia:** Vidrieros (Triollo) · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** lineal · 4,8 km · +346 m (pág.) · 1.282–1.671 m · 1 h 20 · baja.
- **GPX Terranostrum (cálculo propio):** 4,81 km · +393 m · alt. 1.282–1.671 m · inicio 42.94283, −4.66461 · fin 42.95483, −4.67381 (a 1,5 km en línea recta del inicio).
- **Inicio · Fin:** plaza de Vidrieros, 42.94283, −4.66461 ✅ → campa final, 42.95493, −4.67389.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** arroyo de Cabriles.
- **Waypoints clave:** campa al pie del Curavacas 42.95493, −4.67389.
- **Itinerario por tramos (resumen propio):** sale al norte dejando la iglesia a la derecha → el último tramo, el más pendiente, va por pista ancha → campa ⚠️.
- **Descripción:** Aproximación familiar al pie del Curavacas; coincide con el primer tramo de `mp-curavacas-vidrieros` y `mp-dip-12`.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-vidrieros-pie-del-curavacas).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ · Pendiente: —.

**La Braña, Brañosera, Barruelo y Mudá**

#### mp-salcedillo-rojadillo · Salcedillo – Puente de Rojadillo – Brañosera
- **Zona / municipio · Provincia:** La Braña / Valle de Santullán / Mudá · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** lineal · 12,5 km · +395 m (cálculo propio) · 1.059–1.451 m · 4 h 30 · baja.
- **GPX Terranostrum (cálculo propio):** 12,4 km · +395 m · alt. 1.059–1.451 m · inicio 42.94085, −4.27437 · fin 42.9359, −4.30814 (a 2,8 km en línea recta del inicio).
- **Inicio · Fin:** Salcedillo, 42.94085, −4.27437 ✅ → Brañosera.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** iglesia románica de Salcedillo (s. XII, pinturas del s. XV) · puente romano de Rojadillo 42.93549, −4.24146.
- **Itinerario por tramos (resumen propio):** Salcedillo → bajada entre hayas y robles al puente romano de Rojadillo → enlace con el GR-1 E1 → Brañosera.
- **Descripción:** Comparte trazado con el GR-1 E1 y con la Senda del Monte Mayor.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-salcedillo-rojadillo-y-branosera).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: track propio.

#### mp-valberzoso-rojadillo · Valberzoso – Puente Romano El Rojadillo
- **Zona / municipio · Provincia:** La Braña / Valle de Santullán / Mudá · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 6,6 km · +125 m (pág.) · 1.062–1.168 m · 1 h 45 · baja.
- **GPX Terranostrum (cálculo propio):** 6,6 km · +149 m · alt. 1.062–1.168 m · inicio 42.92382, −4.23767 · track cerrado (fin a 4 m del inicio).
- **Inicio · Fin:** a 1 km de Valberzoso, 42.92382, −4.23767 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** puente de Rojadillo · collado en U entre Peña Ensillada y Peña Castrillo.
- **Itinerario por tramos (resumen propio):** circular corta al puente romano por el límite con Cantabria.
- **Descripción:** El puente romano de Rojadillo, sobre el río Camesa, aparece en el libro 2026.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-valberzoso-puente-rojadillo).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: track propio.

#### mp-valberzoso-somahoz · Valberzoso – Collado de Somahoz
- **Zona / municipio · Provincia:** La Braña / Valle de Santullán / Mudá · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** ida y vuelta · 10,5 km · +140 m (pág.) · 1.055–1.216 m · 4 h · baja.
- **GPX Terranostrum (cálculo propio):** 5,23 km · +199 m · alt. 1.055–1.216 m · inicio 42.92384, −4.23766 · fin 42.9603, −4.23556 (a 4,1 km en línea recta del inicio) · ⚠️ **discrepancia:** D+ 199 frente a 140 m publicados.
- **Inicio · Fin:** Valberzoso, 42.92384, −4.23766 ✅.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** collado de Somahoz 42.96030, −4.23556 (🟦 límite con Cantabria).
- **Itinerario por tramos (resumen propio):** por la PP-2041 hacia Mata de Hoz hasta el collado; vuelta por el mismo camino.
- **Descripción:** Paseo hasta la divisoria con Cantabria.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/valberzoso-collado-de-somahoz).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: track propio.

#### mp-calero-branosera · La Mata del Fraile y el Calero de Brañosera
- **Zona / municipio · Provincia:** La Braña / Valle de Santullán / Mudá · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 10,5 km · +342 m (cálculo propio) · 1.047–1.330 m · 3 h · baja.
- **GPX Terranostrum (cálculo propio):** 10,5 km · +342 m · alt. 1.047–1.330 m · inicio 42.91143, −4.28835 · track cerrado (fin a 3 m del inicio).
- **Inicio · Fin:** puente de Peñacorva, Barruelo, 42.91143, −4.28835 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** calero de Brañosera.
- **Itinerario por tramos (resumen propio):** pista de ~4 km entre robles centenarios hasta el calero y regreso en circular.
- **Descripción:** Ruta minera y forestal de Barruelo; enlaza con la Senda de La Pedrosa y con el GR-1 E2 (mina del Calero). Cubre la "ruta minera de Barruelo" que el informe daba sin fuente.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-la-mata-del-fraile-y-el-calero-de-branosera).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: track propio.

#### mp-ujapero-cocoto · Ujapero y Cocoto (parque eólico El Pical)
- **Zona / municipio · Provincia:** La Braña / Valle de Santullán / Mudá · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 19 km · +466 m (pág.) · 1.027–1.492 m · 4 h · media.
- **GPX Terranostrum (cálculo propio):** 19,12 km · +505 m · alt. 1.027–1.492 m · inicio 42.90879, −4.28813 · track cerrado (fin a 32 m del inicio).
- **Inicio · Fin:** Barruelo, 42.90879, −4.28813 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** Peña El Cocoto 42.90407, −4.25846.
- **Itinerario por tramos (resumen propio):** Barruelo → Brañosera → carretera de Salcedillo → Ujapero → Peña El Cocoto (parque eólico El Pical) → Barruelo.
- **Descripción:** Circular larga por las lomas al este de Barruelo.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-de-ujapero-y-cocoto).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: track propio.

#### mp-monte-ciruelo · Monte Ciruelo (Perapertú – San Cebrián de Mudá – San Martín de Perapertú)
- **Zona / municipio · Provincia:** La Braña / Valle de Santullán / Mudá · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 11,2 km · +303 m (cálculo propio) · 1.035–1.335 m · 3 h · fácil · ciclable.
- **GPX Terranostrum (cálculo propio):** 11,22 km · +303 m · alt. 1.035–1.335 m · inicio 42.91746, −4.36875 · track cerrado (fin a 7 m del inicio).
- **Inicio · Fin:** 42.91746, −4.36875 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** San Cebrián de Mudá · Perapertú.
- **Itinerario por tramos (resumen propio):** incluye ~3,5 km por carretera entre San Cebrián y Perapertú.
- **Descripción:** Vuelta al Monte Ciruelo por los pueblos de Mudá y Perapertú (mirador M06 Ermita de la Peña, en Perapertú).
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/monte-ciruelo-desde-la-muneca).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: track propio.

#### mp-minas-san-cebrian · Las minas de San Cebrián de Mudá (Tierras del Bisonte)
- **Zona / municipio · Provincia:** La Braña / Valle de Santullán / Mudá · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 5 km · +118 m (pág.) · 1.058–1.181 m · 1 h 15 · baja.
- **GPX Terranostrum (cálculo propio):** 5,09 km · +120 m · alt. 1.058–1.181 m · inicio 42.89711, −4.38622 · track cerrado (fin a 1 m del inicio).
- **Inicio · Fin:** Centro de Interpretación del Bisonte (San Cebrián de Mudá), 42.89711, −4.38622 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** punto de retorno 42.91424, −4.38864.
- **Itinerario por tramos (resumen propio):** circular corta por las antiguas minas.
- **Descripción:** Se combina con la visita guiada a la Reserva del Bisonte Europeo (§7).
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-las-minas-de-san-cebrian-de-muda).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: track propio.

#### mp-muda-monasterio · Mudá – Monasterio
- **Zona / municipio · Provincia:** La Braña / Valle de Santullán / Mudá · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** ida y vuelta · 6,5 km · +109 m (pág.) · 990–1.107 m · 1 h 30 · baja.
- **GPX Terranostrum (cálculo propio):** 6,49 km · +128 m · alt. 990–1.107 m · inicio 42.87619, −4.39526 · track cerrado (fin a 0 m del inicio).
- **Inicio · Fin:** puente del arroyo de la Pradera, Mudá, 42.87619, −4.39526 ✅.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** Monasterio (pueblo) 42.87610, −4.36326.
- **Itinerario por tramos (resumen propio):** Mudá → Monasterio por el valle; vuelta por el mismo camino.
- **Descripción:** Paseo llano entre dos pueblos de Mudá.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-de-muda-a-monasterio).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: track propio.

**Valle del Pisuerga, Valdivia, Aguilar y Las Tuerces**

#### mp-tuerces-villaescusa · Las Tuerces, circular corta desde Villaescusa de las Torres (palenciaturismo)
- **Zona / municipio · Provincia:** Villaescusa de las Torres (Aguilar de Campoo) · Palencia, Monumento Natural de Las Tuerces.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 5 km · +200 / −200 m · 2 h · fácil · sendero local no homologado ✅.
- **Inicio · Fin:** parking a la entrada de Villaescusa de las Torres, 42.75741, −4.24754 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año; posible nieve. Requiere algo de orientación dentro del laberinto.
- **Agua · Refugios:** sin agua en la meseta; manantial junto al cartel del pueblo ⚠️.
- **Waypoints clave:** panel interpretativo a la salida hacia el páramo · Peña Mesa ("roca en forma de seta") 42.75393, −4.25726.
- **Itinerario por tramos (resumen propio):** subida por la ladera al páramo → Peña Mesa → recorrido libre por el laberinto (más de 50 ha) → bajada al pueblo por cualquier senda.
- **Descripción:** Es la única circular corta con ficha institucional en Las Tuerces. Fauna citada: buitre, águila real, halcón peregrino, anfibios en los callejones húmedos y trucha en la Horadada. Palenciaturismo lo presenta como Monumento Natural "Laberinto de las Tuerces".
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [palenciaturismo](https://palenciaturismo.es/que-hacer/rutas/monumento-natural-tuerces).
- **Licencia · Confianza · Pendiente:** Diputación (enlazar) · ✅ · Pendiente: track propio.

#### mp-escalera-tiempo · La Escalera del Tiempo (Geoparque Las Loras)
- **Zona / municipio · Provincia:** Villaescusa de las Torres · Palencia (Geoparque Las Loras).
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** itinerario geológico · 2 km · 1 h · fácil · **sin GPX**.
- **Inicio · Fin:** Villaescusa de las Torres ❓.
- **Temporada · Riesgos / avisos:** todo el año.
- **Agua · Refugios:** —.
- **Waypoints clave:** —.
- **Itinerario por tramos (resumen propio):** itinerario corto que recorre la serie de rocas desde el medio fluvial hasta el marino.
- **Descripción:** Ruta didáctica del Geoparque que explica la sucesión de estratos de Las Tuerces.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/la-escalera-del-tiempo).
- **Licencia · Confianza · Pendiente:** Geoparque / Terranostrum (enlazar) · ⚠️ · Pendiente: GPX y paneles.

#### mp-cruces-almonga-cervera · Picos Almonga y de las Cruces desde Cervera de Pisuerga
- **Zona / municipio · Provincia:** Cervera de Pisuerga · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** ida y vuelta · 9,5 km · +424 m (pág.) · 949–1.560 m · 3 h · media-baja.
- **GPX Terranostrum (cálculo propio):** 9,47 km · +634 m · alt. 949–1.560 m · inicio 42.85709, −4.49949 · track cerrado (fin a 16 m del inicio) · ⚠️ **discrepancia:** D+ 634 frente a 424 m publicados.
- **Inicio · Fin:** puesto de Cruz Roja de Cervera, CL-627 dirección Guardo, 42.85709, −4.49949 ✅.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** cima ("Pico de las Cruceras") 42.84470, −4.53206.
- **Itinerario por tramos (resumen propio):** pista forestal por un robledal y un pastizal cercado hasta las cimas; vuelta por el mismo camino ⚠️ (descripción leída solo en parte).
- **Descripción:** Subida directa desde Cervera a las dos cimas de `mp-dip-24`. El Trail Pico Almonga (§13) recorre esta zona.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cervera-de-pisuerga-pico-de-las-cruces).
- **Licencia · Confianza · Pendiente:** Agrupación Comarcal de Desarrollo / Terranostrum (enlazar) · ⚠️ · Pendiente: track propio.

#### mp-golobar-sel-fuente-cobre · Golobar – Collado de Canaleja – Sel de la Fuente – Fuente Cobre
- **Zona / municipio · Provincia:** Brañosera / La Pernía, Sierra de Híjar · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 11,3 km · +525 m (pág.) · 1.610–2.135 m · 5 h · baja-media.
- **GPX Terranostrum (cálculo propio):** 11,26 km · +862 m · alt. 1.610–2.135 m · inicio 42.96747, −4.337 · track cerrado (fin a 28 m del inicio) · ⚠️ **discrepancia:** D+ 862 frente a 525 m publicados.
- **Inicio · Fin:** Refugio de El Golobar, 42.96718, −4.33678 (1.775 m según la página) ✅/⚠️. Fin = inicio.
- **Temporada · Riesgos / avisos:** verano; con nieve, terreno de raquetas. La carretera del Golobar no tiene mantenimiento y ha sufrido desprendimientos.
- **Agua · Refugios:** sin fuentes; la Fuente del Cobre es una surgencia (no beber sin tratar).
- **Waypoints clave:** Collado de Canaleja (2.033 m) · Sel de la Fuente (sumidero) · Fuente del Cobre 42.98732, −4.37233 · cima del Valdecebollas (2.135 m en el GPX).
- **Itinerario por tramos (resumen propio):** Golobar → collado de Canaleja, con vistas a La Pernía y Picos de Europa → (Valdecebollas, opcional) → bajada al circo glaciar del Sel de la Fuente, donde se sume el agua → resurgencia de la Fuente del Cobre → regreso al Golobar.
- **Descripción:** Acceso montañero a la Fuente del Cobre desde la cabecera del Rubagón. Piso subalpino con enebro rastrero y arándano; túmulos megalíticos de unos 5.000 años. El Valdecebollas es el vértice de primer orden "El Torreón".
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-golobar-valdecebollas-sel-de-la-fuente).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ trazado / ⚠️ D+ · Pendiente: track propio.

#### mp-liguerzana-mariposas · Ligüérzana – Vega de Quintanaluengos (mariposa hormiguera oscura)
- **Zona / municipio · Provincia:** Valle del Pisuerga / Valdivia / Aguilar · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 8,7 km · +86 m (pág.) · 2 h · baja.
- **GPX Terranostrum (cálculo propio):** 8,72 km · +83 m · alt. 965–1.029 m · inicio 42.85677, −4.45841 · track cerrado (fin a 2 m del inicio).
- **Inicio · Fin:** puente del Pisuerga en Ligüérzana (panel), 42.85677, −4.45841 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** **microrreserva de mariposas** 42.84447, −4.42769.
- **Itinerario por tramos (resumen propio):** circular llana por la vega del Pisuerga.
- **Descripción:** Pasa por una microrreserva de la mariposa hormiguera oscura; no salirse del camino en la microrreserva (inferencia).
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-ligueerzana-a-la-vega-de-quintanaluengos).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: track propio.

#### mp-cillamayor-matabuena · Cillamayor – Matabuena (Valle de Santullán)
- **Zona / municipio · Provincia:** Valle del Pisuerga / Valdivia / Aguilar · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 8,7 km · +203 m (pág.) · 2 h · baja.
- **GPX Terranostrum (cálculo propio):** 8,72 km · +250 m · alt. 917–1.035 m · inicio 42.86254, −4.27877 · track cerrado (fin a 18 m del inicio) · ⚠️ **discrepancia:** D+ 250 frente a 203 m publicados.
- **Inicio · Fin:** teleclub de Cillamayor, 42.86254, −4.27877 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** —.
- **Itinerario por tramos (resumen propio):** campos, praderías y rebollar.
- **Descripción:** Paseo agrícola y forestal al sur del valle de Santullán.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cillamayor-montes-de-matabuena).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: track propio.

#### mp-canduela-valdelobera · Canduela – Villanueva de Henares (necrópolis de Valdelobera)
- **Zona / municipio · Provincia:** Valle del Pisuerga / Valdivia / Aguilar · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 8,5 km (o i/v de 5,6–5,7) · +87 m (pág.) · 2 h 15 · baja.
- **GPX Terranostrum (cálculo propio):** 8,53 km · +269 m · alt. 926–1.012 m · inicio 42.83439, −4.18623 · track cerrado (fin a 4 m del inicio) · ⚠️ **discrepancia:** D+ 269 frente a 87 m publicados.
- **Inicio · Fin:** Canduela, 42.83439, −4.18623 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** necrópolis de Valdelobera 42.83648, −4.16537.
- **Itinerario por tramos (resumen propio):** circular entre Canduela y Villanueva de Henares por la necrópolis.
- **Descripción:** Ruta de patrimonio en la Valdivia; Canduela es un conjunto rural de casonas.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-canduela-villanueva-de-henares).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: track propio.

#### mp-menaza · Campos de Menaza
- **Zona / municipio · Provincia:** Valle del Pisuerga / Valdivia / Aguilar · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** circular · 6 km · +77 m (pág.) · 2 h · baja.
- **GPX Terranostrum (cálculo propio):** 6,12 km · +87 m · alt. 914–991 m · inicio 42.83134, −4.21617 · track cerrado (fin a 20 m del inicio).
- **Inicio · Fin:** Menaza, 42.83134, −4.21617 ✅. Fin = inicio.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** sin datos.
- **Waypoints clave:** —.
- **Itinerario por tramos (resumen propio):** robledal y cultivos (la ficha escribe "Mezana" por error).
- **Descripción:** Paseo corto y llano cerca de Aguilar.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-campos-de-menaza).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: track propio.

#### mp-blendios-e1 · Calzada de los Blendios (GR-73) E1: Herrera de Pisuerga – Santa María de Mave 🟨
- **Zona / municipio · Provincia:** Valle del Pisuerga / Valdivia / Aguilar · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** lineal · 21,3 km · +187 m (cálculo propio) · 6 h · baja.
- **GPX Terranostrum (cálculo propio):** 21,32 km · +187 m · alt. 833–1.012 m · inicio 42.59624, −4.32911 · fin 42.72267, −4.27517 (a 14,7 km en línea recta del inicio).
- **Inicio · Fin:** Herrera de Pisuerga, 42.59624, −4.32911 ✅ → Santa María de Mave.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** agua en los pueblos.
- **Waypoints clave:** —.
- **Itinerario por tramos (resumen propio):** sobre la traza de la calzada romana Pisoraca–Portus Blendium hacia el norte.
- **Descripción:** 🟨 La mayor parte queda al sur del ámbito (Herrera, Alar del Rey). Es un GR (GR-73) que el informe no recogía.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/calzada-de-los-blendios-etapa-1).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: track propio.

#### mp-blendios-e2 · Calzada de los Blendios (GR-73) E2: Santa María de Mave – Aguilar de Campoo
- **Zona / municipio · Provincia:** Valle del Pisuerga / Valdivia / Aguilar · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** lineal · 11 km · +141 m (cálculo propio) · 3 h · baja.
- **GPX Terranostrum (cálculo propio):** 10,37 km · +141 m · alt. 871–949 m · inicio 42.72281, −4.27515 · fin 42.79251, −4.26272 (a 7,8 km en línea recta del inicio).
- **Inicio · Fin:** Santa María de Mave, 42.72281, −4.27515 ✅ → Aguilar, 42.79251, −4.26272.
- **Temporada · Riesgos / avisos:** todo el año ❓.
- **Agua · Refugios:** agua en los pueblos.
- **Waypoints clave:** Mave · Olleros · Valoria.
- **Itinerario por tramos (resumen propio):** Mave → Olleros → Valoria → Aguilar, siguiendo la calzada romana.
- **Descripción:** Enlaza con las rutas de Las Tuerces (Mave) y con el Camino Olvidado en Aguilar.
- **Comentarios de usuarios:** no se encontraron.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/calzada-de-los-blendios-etapa-2).
- **Licencia · Confianza · Pendiente:** Terranostrum (enlazar) · ✅ cifras / ⚠️ descripción · Pendiente: track propio.

### 16.8 Nuevas rutas BTT y cicloturismo (v2, 21-11-2026)

Fichas breves de las 23 rutas BTT de Terranostrum que no estaban en el informe (la 24.ª, "Pedaleando por el Románico", ya tenía ficha en §16.6) y de la Ruta de los Pantanos. Datos comunes: casi todas proceden de la Agrupación Comarcal de Desarrollo Montaña Palentina (las marcadas "Turismo CyL", de Turismo Castilla y León); todas tienen GPX en Terranostrum (solo enlazar); la bici solo está permitida por carreteras, pistas y caminos aptos para vehículos (PUP 6.2.6); temporada: todo el año salvo nieve ❓. Tabla resumen en §1.5.

#### mp-btt-alto-muda · BTT Alto Valle de Mudá
- **Zona · Provincia:** La Braña / Mudá · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 12,2 km · +266 m (pág.) · 1 h 20 · baja.
- **GPX Terranostrum (cálculo propio):** 12,15 km · +200 m · alt. 993–1.143 m · inicio 42.89712, −4.38624 · track cerrado (fin a 8 m del inicio) · ⚠️ **discrepancia:** D+ 200 frente a 266 m publicados.
- **Inicio · Fin:** San Cebrián de Mudá, 42.89712, −4.38624 ✅. Fin = inicio.
- **Descripción:** ruta BTT señalizada en la ficha de origen; sin descripción extraída ⚠️.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-alto-valle-de-muda).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-barruelo-cervera · BTT Barruelo – Cervera (Turismo CyL)
- **Zona · Provincia:** La Braña – Cervera · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** lineal · 29,3 km · +153 m (pág.) · — · media.
- **GPX Terranostrum (cálculo propio):** 30,57 km · +341 m · alt. 951–1.106 m · inicio 42.90167, −4.28789 · fin 42.86207, −4.49865 (a 17,7 km en línea recta del inicio) · ⚠️ **discrepancia:** D+ 341 frente a 153 m publicados.
- **Inicio · Fin:** Barruelo de Santullán, 42.90167, −4.28789 ✅.
- **Descripción:** Lineal.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-barruelo-de-santullan-cervera-de-pisuerga).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-cervera-triollo · BTT Cervera – Triollo (Turismo CyL)
- **Zona · Provincia:** Cervera – Alto Carrión · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** lineal · 24,3 km · +440 m (pág.) · — · alta.
- **GPX Terranostrum (cálculo propio):** 23,68 km · +548 m · alt. 996–1.446 m · inicio 42.86211, −4.4987 · fin 42.92491, −4.681 (a 16,4 km en línea recta del inicio) · ⚠️ **discrepancia:** D+ 548 frente a 440 m publicados.
- **Inicio · Fin:** Cervera de Pisuerga, 42.86211, −4.4987 ✅.
- **Descripción:** Lineal.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-cervera-de-pisuerga-triollo).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-carbon · BTT Del Carbón
- **Zona · Provincia:** Valle del Pisuerga · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 19 km · +255 m (pág.) · 1 h 55 · baja.
- **GPX Terranostrum (cálculo propio):** 19,09 km · +150 m · alt. 943–1.053 m · inicio 42.8485, −4.37923 · track cerrado (fin a 11 m del inicio) · ⚠️ **discrepancia:** D+ 150 frente a 255 m publicados.
- **Inicio · Fin:** Salinas de Pisuerga, 42.8485, −4.37923 ✅. Fin = inicio.
- **Descripción:** ruta BTT señalizada en la ficha de origen; sin descripción extraída ⚠️.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-del-carbon).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-robla · BTT El Ferrocarril de La Robla
- **Zona · Provincia:** La Peña · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 34 km · +669 m (pág.) · 3 h 30 · alta.
- **GPX Terranostrum (cálculo propio):** 33,96 km · +411 m · alt. 1.071–1.211 m · inicio 42.80015, −4.73802 · track cerrado (fin a 10 m del inicio) · ⚠️ **discrepancia:** D+ 411 frente a 669 m publicados.
- **Inicio · Fin:** Las Heras de la Peña, 42.80015, −4.73802 ✅. Fin = inicio.
- **Descripción:** ruta BTT señalizada en la ficha de origen; sin descripción extraída ⚠️.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-el-ferrocarril-de-la-robla).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-gotico-pena · BTT Gótico y Románico en La Peña
- **Zona · Provincia:** La Peña · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 17,5 km · +156 m (pág.) · 1 h 40 · baja.
- **GPX Terranostrum (cálculo propio):** 17,57 km · +111 m · alt. 1.106–1.179 m · inicio 42.80801, −4.5989 · track cerrado (fin a 7 m del inicio) · ⚠️ **discrepancia:** D+ 111 frente a 156 m publicados.
- **Inicio · Fin:** Castrejón de la Peña, 42.80801, −4.5989 ✅. Fin = inicio.
- **Descripción:** ruta BTT señalizada en la ficha de origen; sin descripción extraída ⚠️.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-gotico-y-romanico-en-la-pena).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-guardo-almuhey · BTT Guardo – Puente Almuhey (Turismo CyL) 🟧
- **Zona · Provincia:** Guardo → León · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** lineal · 21,3 km · +230 m (pág.) · — · media-alta.
- **GPX Terranostrum (cálculo propio):** 21,39 km · +293 m · alt. 972–1.205 m · inicio 42.79768, −4.84809 · fin 42.78479, −4.97764 (a 10,7 km en línea recta del inicio) · ⚠️ **discrepancia:** D+ 293 frente a 230 m publicados.
- **Inicio · Fin:** Guardo, 42.79768, −4.84809 ✅.
- **Descripción:** Lineal; termina en León.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-guardo-puente-almuhey).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-despensa-abad · BTT La Despensa del Abad
- **Zona · Provincia:** Valle de Santullán · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 25,4 km · +450 m (pág.) · 2 h 30 · baja.
- **GPX Terranostrum (cálculo propio):** 25,36 km · +293 m · alt. 918–993 m · inicio 42.86263, −4.27773 · track cerrado (fin a 5 m del inicio) · ⚠️ **discrepancia:** D+ 293 frente a 450 m publicados.
- **Inicio · Fin:** Cillamayor, 42.86263, −4.27773 ✅. Fin = inicio.
- **Descripción:** ruta BTT señalizada en la ficha de origen; sin descripción extraída ⚠️.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-la-despensa-del-abad).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-horca-ojeda · BTT La Horca de la Ojeda 🟨
- **Zona · Provincia:** La Ojeda (periferia sur) · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 22 km · +375 m (pág.) · 2 h 15 · baja.
- **GPX Terranostrum (cálculo propio):** 22,02 km · +275 m · alt. 901–1.021 m · inicio 42.70195, −4.38255 · track cerrado (fin a 8 m del inicio) · ⚠️ **discrepancia:** D+ 275 frente a 375 m publicados.
- **Inicio · Fin:** San Andrés de Arroyo, 42.70195, −4.38255 ✅. Fin = inicio.
- **Descripción:** ruta BTT señalizada en la ficha de origen; sin descripción extraída ⚠️.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-la-horca-de-la-ojeda).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-ermitas-aguilar · BTT Las Ermitas del Embalse de Aguilar
- **Zona · Provincia:** Aguilar · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 21,6 km · +419 m (pág.) · 2 h 15 · baja.
- **GPX Terranostrum (cálculo propio):** 21,41 km · +316 m · alt. 946–1.106 m · inicio 42.77399, −4.36764 · track cerrado (fin a 5 m del inicio) · ⚠️ **discrepancia:** D+ 316 frente a 419 m publicados.
- **Inicio · Fin:** Vallespinoso de Aguilar, 42.77399, −4.36764 ✅. Fin = inicio.
- **Descripción:** ruta BTT señalizada en la ficha de origen; sin descripción extraída ⚠️.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-las-ermitas-del-embalse-de-aguilar).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-tamaricas · BTT Las Fuentes Tamáricas
- **Zona · Provincia:** Velilla · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 13,5 km · +198 m (pág.) · 1 h 20 · baja.
- **GPX Terranostrum (cálculo propio):** 13,47 km · +87 m · alt. 1.113–1.161 m · inicio 42.82771, −4.844 · track cerrado (fin a 5 m del inicio) · ⚠️ **discrepancia:** D+ 87 frente a 198 m publicados.
- **Inicio · Fin:** Velilla del Río Carrión, 42.82771, −4.844 ✅. Fin = inicio.
- **Descripción:** ruta BTT señalizada en la ficha de origen; sin descripción extraída ⚠️.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-las-fuentes-tamaricas).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-valdavia · BTT Las Ranas del Río Valdavia 🟨
- **Zona · Provincia:** La Peña (periferia sur) · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 20 km · +325 m (pág.) · 2 h · baja.
- **GPX Terranostrum (cálculo propio):** 19,93 km · +209 m · alt. 991–1.144 m · inicio 42.76368, −4.68649 · track cerrado (fin a 5 m del inicio) · ⚠️ **discrepancia:** D+ 209 frente a 325 m publicados.
- **Inicio · Fin:** Respenda de la Peña, 42.76368, −4.68649 ✅. Fin = inicio.
- **Descripción:** ruta BTT señalizada en la ficha de origen; sin descripción extraída ⚠️.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-las-ranas-del-rio-valdavia).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-burejo · BTT Los Valles de Burejo
- **Zona · Provincia:** Dehesa de Montejo · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 20 km · +317 m (pág.) · 2 h · baja.
- **GPX Terranostrum (cálculo propio):** 20,07 km · +233 m · alt. 977–1.112 m · inicio 42.81944, −4.50994 · track cerrado (fin a 3 m del inicio) · ⚠️ **discrepancia:** D+ 233 frente a 317 m publicados.
- **Inicio · Fin:** Dehesa de Montejo, 42.81944, −4.50994 ✅. Fin = inicio.
- **Descripción:** ruta BTT señalizada en la ficha de origen; sin descripción extraída ⚠️.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-los-valles-de-burejo).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-karsticos · BTT Monumentos Kársticos
- **Zona · Provincia:** Las Loras · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 17,7 km · +371 m (pág.) · 1 h 50 · baja.
- **GPX Terranostrum (cálculo propio):** 17,73 km · +254 m · alt. 884–1.044 m · inicio 42.75905, −4.25095 · track cerrado (fin a 10 m del inicio) · ⚠️ **discrepancia:** D+ 254 frente a 371 m publicados.
- **Inicio · Fin:** Villaescusa de las Torres, 42.75905, −4.25095 ✅. Fin = inicio.
- **Descripción:** ruta BTT señalizada en la ficha de origen; sin descripción extraída ⚠️.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-monumentos-karsticos).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-vega-carrion · BTT Por la Vega del Carrión
- **Zona · Provincia:** Guardo · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 20 km · +254 m (pág.) · 2 h · baja.
- **GPX Terranostrum (cálculo propio):** 20,03 km · +100 m · alt. 1.041–1.103 m · inicio 42.79109, −4.84814 · track cerrado (fin a 1 m del inicio) · ⚠️ **discrepancia:** D+ 100 frente a 254 m publicados.
- **Inicio · Fin:** Guardo, 42.79109, −4.84814 ✅. Fin = inicio.
- **Descripción:** ruta BTT señalizada en la ficha de origen; sin descripción extraída ⚠️.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-por-la-vega-del-carrion).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-ventas-pernia · BTT Por las Ventas de La Pernía
- **Zona · Provincia:** La Pernía · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 9,2 km · +160 m (pág.) · 55 min · baja.
- **GPX Terranostrum (cálculo propio):** 9,27 km · +107 m · alt. 1.083–1.181 m · inicio 42.96864, −4.49503 · track cerrado (fin a 6 m del inicio) · ⚠️ **discrepancia:** D+ 107 frente a 160 m publicados.
- **Inicio · Fin:** San Salvador de Cantamuda, 42.96864, −4.49503 ✅. Fin = inicio.
- **Descripción:** ruta BTT señalizada en la ficha de origen; sin descripción extraída ⚠️.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-por-las-ventas-de-la-pernia).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-valle-estrecho · BTT Por Valle Estrecho
- **Zona · Provincia:** Cervera – Resoba · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** lineal · 17,3 km · +295 m (pág.) · 1 h 45 · baja.
- **GPX Terranostrum (cálculo propio):** 8,55 km · +91 m · alt. 1.034–1.081 m · inicio 42.86402, −4.52766 · fin 42.8915, −4.59322 (a 6,2 km en línea recta del inicio) · ⚠️ **discrepancia:** distancia 8,55 frente a 17,3 km publicados; D+ 91 frente a 295 m publicados.
- **Inicio · Fin:** Ruesga, 42.86402, −4.52766 ✅.
- **Descripción:** El GPX parece incompleto o solo de ida.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-por-valle-estrecho).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-santullan · BTT Románico en Tierras de Santullán
- **Zona · Provincia:** Valle de Santullán · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 17 km · +350 m (pág.) · 1 h 45 · baja.
- **GPX Terranostrum (cálculo propio):** 16,91 km · +273 m · alt. 949–1.087 m · inicio 42.8979, −4.28264 · track cerrado (fin a 7 m del inicio) · ⚠️ **discrepancia:** D+ 273 frente a 350 m publicados.
- **Inicio · Fin:** Barruelo de Santullán, 42.8979, −4.28264 ✅. Fin = inicio.
- **Descripción:** ruta BTT señalizada en la ficha de origen; sin descripción extraída ⚠️.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-romanico-en-tierras-de-santullan).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-senda-pisuerga · BTT Senda del Pisuerga
- **Zona · Provincia:** Cervera · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 19 km · +184 m (pág.) · 1 h 55 · baja.
- **GPX Terranostrum (cálculo propio):** 19,18 km · +66 m · alt. 955–997 m · inicio 42.86289, −4.49639 · track cerrado (fin a 6 m del inicio) · ⚠️ **discrepancia:** D+ 66 frente a 184 m publicados.
- **Inicio · Fin:** Cervera de Pisuerga, 42.86289, −4.49639 ✅. Fin = inicio.
- **Descripción:** ruta BTT señalizada en la ficha de origen; sin descripción extraída ⚠️.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-senda-del-pisuerga).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-jano · BTT Tras las Huellas de Jano
- **Zona · Provincia:** Guardo · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 27,3 km · +264 m (pág.) · 3 h · alta.
- **GPX Terranostrum (cálculo propio):** 27,33 km · +799 m · alt. 1.092–1.373 m · inicio 42.7964, −4.84771 · track cerrado (fin a 34 m del inicio) · ⚠️ **discrepancia:** D+ 799 frente a 264 m publicados.
- **Inicio · Fin:** Guardo, 42.7964, −4.84771 ✅. Fin = inicio.
- **Descripción:** ruta BTT señalizada en la ficha de origen; sin descripción extraída ⚠️.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-tras-las-huellas-de-jano).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-triollo-guardo · BTT Triollo – Guardo (Turismo CyL)
- **Zona · Provincia:** Alto Carrión – Guardo · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** lineal · 30 km · +570 m (pág.) · — · alta.
- **GPX Terranostrum (cálculo propio):** 29,87 km · +560 m · alt. 1.098–1.693 m · inicio 42.92486, −4.6809 · fin 42.79771, −4.84822 (a 19,6 km en línea recta del inicio).
- **Inicio · Fin:** Triollo, 42.92486, −4.6809 ✅.
- **Descripción:** Lineal.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-triollo-guardo).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-vuelta-bernorio · BTT Vuelta al Monte Bernorio
- **Zona · Provincia:** La Valdivia · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 20,4 km · +280 m (pág.) · 2 h · baja.
- **GPX Terranostrum (cálculo propio):** 20,55 km · +220 m · alt. 899–1.062 m · inicio 42.77484, −4.16699 · track cerrado (fin a 10 m del inicio) · ⚠️ **discrepancia:** D+ 220 frente a 280 m publicados.
- **Inicio · Fin:** Pomar de Valdivia, 42.77484, −4.16699 ✅. Fin = inicio.
- **Descripción:** Rodea el oppidum; pasa por Quintanilla y el río Camesa hasta Porquera de los Infantes (necrópolis) ⚠️. Es la única ficha de Bernorio en Terranostrum.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-vuelta-al-monte-bernorio).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-btt-aguilar · BTT "Ruta BTT" de Aguilar de Campoo
- **Zona · Provincia:** Aguilar · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** circular · 13,4 km · +104 m (pág.) · 1 h 20 · baja.
- **GPX Terranostrum (cálculo propio):** 13,4 km · +22 m · alt. 883–910 m · inicio 42.79577, −4.27137 · track cerrado (fin a 4 m del inicio) · ⚠️ **discrepancia:** D+ 22 frente a 104 m publicados.
- **Inicio · Fin:** Aguilar de Campoo, 42.79577, −4.27137 ✅. Fin = inicio.
- **Descripción:** ruta BTT señalizada en la ficha de origen; sin descripción extraída ⚠️.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt).
- **Licencia · Confianza:** Terranostrum / Agrupación Comarcal o Turismo CyL (enlazar) · ✅ cifras / ⚠️ trazado.

#### mp-ruta-pantanos · Ruta de los Pantanos (carretera, cicloturismo)
- **Zona · Provincia:** Aguilar – Cervera – Triollo – Velilla – Guardo · Palencia.
- **Tipo · Distancia · D+ · Tiempo · Dificultad:** ruta escénica por carretera (coche, moto o bici) · 81 km · D+ ❓ · sin señalizar ✅.
- **Inicio · Fin:** P-210 / CL-626 / CL-627 (sin punto de salida fijo).
- **Temporada · Riesgos:** tráfico; vialidad invernal (cadenas y cortes por nieve, §9).
- **Waypoints clave:** embalses de Aguilar (247 hm³, 1963), Requejada (95 hm³, 1940), Ruesga (el más pequeño, 1923, construido para el Canal de Castilla), Camporredondo (1930) y Compuerto (95 hm³, 1960) · miradores del Alto de la Varga (M04) y Alba de los Cardaños (M05).
- **Descripción:** encadena los cinco embalses de la Montaña Palentina y sus miradores. No es un sendero homologado: la "Ruta de los Pantanos" del km 15,5 que cita el PR-P 7 es esta carretera.
- **Enlaces:** [palenciaturismo](https://palenciaturismo.es/que-hacer/rutas/ruta-pantanos).
- **Licencia · Confianza:** Diputación (enlazar) · ✅.

---

## Anexo: Fuentes (todas las URLs citadas, agrupadas por dominio)

Este anexo reúne todas las URLs del documento, incluidas las retiradas de las tablas y fichas para aligerarlas ("+N en Fuentes"). El dominio indica el tipo de fuente: patrimonionatural.org, bocyl, boe, aemet, mapa, idee, ign y cnig son fuentes oficiales; diputaciondepalencia y palenciaturismo, editoriales o institucionales con copyright; mendikat, wikiloc, komoot, alltrails, terranostrum y el resto, terceros (solo enlazar).


**patrimonionatural.org** (47)

- [Casa del Parque](https://patrimonionatural.org/casas-del-parque/casas-del-parque/casa-del-parque-de-fuentes-carrionas-y-fuente-cobre-montana-palentina)
- [página del parque](https://patrimonionatural.org/espacios-naturales/parque-natural/parque-natural-montana-palentina)
- [.doc Fundación](https://patrimonionatural.org/ficheros/01005190825350carrionas3doc190510_082535.doc)
- [PDF — 58dce5a62bd0a_Libro-GR1-en-PALENCIA.pdf](https://patrimonionatural.org/ficheros/58dce5a62bd0a_Libro-GR1-en-PALENCIA.pdf)
- [alt. — 58dce81d738fd_Folleto-senda-del-Oso.pdf](https://patrimonionatural.org/ficheros/58dce81d738fd_Folleto-senda-del-Oso.pdf)
- [PUP 2018 — 5b0be95e3407c_Parque-Natural-Montana-Palentina_Plan-Uso-Publico-vers_2018.pdf](https://patrimonionatural.org/ficheros/5b0be95e3407c_Parque-Natural-Montana-Palentina_Plan-Uso-Publico-vers_2018.pdf)
- [folleto — 5e7112e99cc33_Folleto-Senda-del-Gigante-del-Valle-Estrecho.pdf](https://patrimonionatural.org/ficheros/5e7112e99cc33_Folleto-Senda-del-Gigante-del-Valle-Estrecho.pdf)
- [PDF — 5f1aa02ff066d_Folleto_gr-1.pdf](https://patrimonionatural.org/ficheros/5f1aa02ff066d_Folleto_gr-1.pdf)
- [PDF jul-2024 — Cierres de Senderos Parque Natural-20240705-101959.pdf](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural-20240705-101959.pdf)
- [PDF — Cierres de Senderos Parque Natural-20260306-114659.pdf](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural-20260306-114659.pdf)
- [PDF — Cierres de Senderos Parque Natural_20-11-2026-20261120-105650.pdf](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural_20-11-2026-20261120-105650.pdf)
- [nov-2024 — Cierres de Senderos Parque Natural_2024_11_29-20241129-102558.pdf](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural_2024_11_29-20241129-102558.pdf)
- [PDF — Cierres de Senderos Parque Natural_2025_11_14-20251113-155300.pdf](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural_2025_11_14-20251113-155300.pdf)
- [PDF — Cierres de Senderos Parque Natural_2026_4_16-20260417-104844.pdf](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural_2026_4_16-20260417-104844.pdf)
- [PDF — Cierres de Senderos Parque Natural_4-6-2026-20260604-121346.pdf](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural_4-6-2026-20260604-121346.pdf)
- [folleto — El_Roblon.pdf](https://patrimonionatural.org/ficheros/El_Roblon.pdf)
- [folleto 2025 — FOLLETO Senda del escultor Ursi-20250621-104214.pdf](https://patrimonionatural.org/ficheros/FOLLETO%20Senda%20del%20escultor%20Ursi-20250621-104214.pdf)
- [folleto nov-2025](https://patrimonionatural.org/ficheros/Folleto%20Senda%20Monte%20Mayor-20251129-105354.pdf)
- [Horario 2026 — Horario 2026.pdf](https://patrimonionatural.org/ficheros/Horario%202026.pdf)
- [folleto — Lago-Lomas.pdf](https://patrimonionatural.org/ficheros/Lago-Lomas.pdf)
- [Plano Junta 2025](https://patrimonionatural.org/ficheros/Parque%20Natural%20Monta%C3%B1a%20Palentina-%28sin%20senda%20Ruesga%29_compressed-20250621-104951.pdf)
- [folleto — Pinar-Velilla.pdf](https://patrimonionatural.org/ficheros/Pinar-Velilla.pdf)
- [folleto 2024 — Senda de La Venganza del Conde -20241211-124505.pdf](https://patrimonionatural.org/ficheros/Senda%20de%20La%20Venganza%20del%20Conde%20-20241211-124505.pdf)
- [folleto — folletosendadelosopdf130111_100115.pdf](https://patrimonionatural.org/ficheros/folletosendadelosopdf130111_100115.pdf)
- [folleto — folletosendatosandepdf240512_091402.pdf](https://patrimonionatural.org/ficheros/folletosendatosandepdf240512_091402.pdf)
- [obras — relaciondeartistasobrasyubicacionespdf060910_145440.pdf](https://patrimonionatural.org/ficheros/relaciondeartistasobrasyubicacionespdf060910_145440.pdf)
- [folleto — sendabosquefosilverdenapdf140111_131636.pdf](https://patrimonionatural.org/ficheros/sendabosquefosilverdenapdf140111_131636.pdf)
- [folleto — sendafuentecobrepdf240512_091321.pdf](https://patrimonionatural.org/ficheros/sendafuentecobrepdf240512_091321.pdf)
- [folleto — sendamazobrepdf140111_131913.pdf](https://patrimonionatural.org/ficheros/sendamazobrepdf140111_131913.pdf)
- [Patrimonio Natural](https://patrimonionatural.org/noticias/noticia/la-berrea-en-fuentes-carrionas-y-en-la-casa-del-parque-de-cervera-de-pisuerga)
- [noticia — la-junta-adjudica-la-obra-del-mirador-de-la-senda-del-monte-mayor-y-el-aparcamiento-de-los](https://patrimonionatural.org/noticias/noticia/la-junta-adjudica-la-obra-del-mirador-de-la-senda-del-monte-mayor-y-el-aparcamiento-de-los-grullos-por-valor-de-113000-)
- [noticia — la-junta-ha-publicado-la-licitacion-para-la-mejora-del-uso-publico-en-el-termino-municipal](https://patrimonionatural.org/noticias/noticia/la-junta-ha-publicado-la-licitacion-para-la-mejora-del-uso-publico-en-el-termino-municipal-de-branosera)
- [Proyecto FEDER](https://patrimonionatural.org/proyectos/feder-sendero-embalse-de-ruesga)
- [Proyecto FTJ — ftj-ampliacion-y-mejora-de-la-red-de-senderos-e-instalaciones-de-uso-publico-asociadas-en-](https://patrimonionatural.org/proyectos/ftj-ampliacion-y-mejora-de-la-red-de-senderos-e-instalaciones-de-uso-publico-asociadas-en-parque-natural-montana-palentina)
- [patrimonionatural.org/senderos](https://patrimonionatural.org/senderos)
- [ficha — senda-de-fuente-cobre](https://patrimonionatural.org/senderos/senda-de-fuente-cobre)
- [ficha — senda-de-la-cascada-de-mazobre](https://patrimonionatural.org/senderos/senda-de-la-cascada-de-mazobre)
- [ficha — senda-de-la-laguna-de-las-lomas](https://patrimonionatural.org/senderos/senda-de-la-laguna-de-las-lomas)
- [ficha — senda-de-la-tejeda-de-tosande](https://patrimonionatural.org/senderos/senda-de-la-tejeda-de-tosande)
- [ficha — senda-de-la-venganza-del-conde](https://patrimonionatural.org/senderos/senda-de-la-venganza-del-conde)
- [ficha — senda-del-bosque-fosil](https://patrimonionatural.org/senderos/senda-del-bosque-fosil)
- [ficha — senda-del-escultor-ursi](https://patrimonionatural.org/senderos/senda-del-escultor-ursi)
- [ficha — senda-del-gigante-del-valle-estrecho](https://patrimonionatural.org/senderos/senda-del-gigante-del-valle-estrecho)
- [ficha — senda-del-monte-mayor](https://patrimonionatural.org/senderos/senda-del-monte-mayor)
- [ficha — senda-del-oso](https://patrimonionatural.org/senderos/senda-del-oso)
- [ficha — senda-del-pinar-autoctono-de-velilla](https://patrimonionatural.org/senderos/senda-del-pinar-autoctono-de-velilla)
- [ficha — senda-del-roblon-de-estalaya](https://patrimonionatural.org/senderos/senda-del-roblon-de-estalaya)

**mendikat.net** (46)

- [Mendikat 8261](https://www.mendikat.net/mount/bernorio-palencia-espana/8261)
- [Mendikat 8377](https://www.mendikat.net/mount/curavacas-palencia-espana/8377)
- [Mendikat 8376](https://www.mendikat.net/mount/espiguete-palencia-espana/8376)
- [Mendikat 8699](https://www.mendikat.net/mount/fraile-pena-del-palencia-espana/8699)
- [Mendikat 15947](https://www.mendikat.net/mount/hoya-contina-pico-de-palencia-espana/15947)
- [Mendikat 8378](https://www.mendikat.net/mount/lezna-palencia-espana/8378)
- [Mendikat 13099](https://www.mendikat.net/mount/mayor-pena-palencia-espana/13099)
- [Mendikat 20865](https://www.mendikat.net/mount/monte-cilda-palencia-espana/20865)
- [Mendikat 4277](https://www.mendikat.net/mount/monte-infierno-cantabria-espana-and-palencia-espana/4277)
- [Mendikat 8409](https://www.mendikat.net/mount/murcia-pico-palencia-espana-and-leon-espana/8409)
- [Mendikat 8705](https://www.mendikat.net/mount/pena-lampa-palencia-espana-and-leon-espana/8705)
- [Mendikat 2132](https://www.mendikat.net/mount/pena-prieta-cantabria-espana/2132)
- [Mendikat 8698](https://www.mendikat.net/mount/pena-redonda-palencia-espana/8698)
- [Mendikat 12903](https://www.mendikat.net/mount/pena-tremaya-palencia-espana/12903)
- [Mendikat 2129](https://www.mendikat.net/mount/penalabra-cantabria-espana-and-palencia-espana/2129)
- [Mendikat 14039](https://www.mendikat.net/mount/tio-celestino-alto-del-palencia-espana/14039)
- [Mendikat 8386](https://www.mendikat.net/mount/tres-mares-cantabria-espana-and-palencia-espana/8386)
- [Mendikat 2133](https://www.mendikat.net/mount/tres-provincias-cantabria-espana-and-palencia-espana-and-leon-espana/2133)
- [Mendikat 8260](https://www.mendikat.net/mount/valcabado-palencia-espana/8260)
- [Mendikat 8382](https://www.mendikat.net/mount/valdecebollas-palencia-espana/8382)
- [Mendikat región](https://www.mendikat.net/region/palencia)
- [M 20178 — 20178](https://www.mendikat.net/track/bernorio-villaren-de-valdibia-bernorio/20178)
- [M 16931 Corredor Oblicuo](https://www.mendikat.net/track/curavacas-los-tres-curavacas-por-el-corredor-oblicuo-y/16931)
- [M 17352 — 17352](https://www.mendikat.net/track/curavacas-vidrieros-curavacas-hospital-vidrieros/17352)
- [M 14197 — 14197](https://www.mendikat.net/track/curavacas-vidrieros-curavacas-por-el-callejo-grande/14197)
- [M 6152 — 6152](https://www.mendikat.net/track/espiguete-cardano-de-abajo-pista-pedrera-cara-sur-espiguete-inicio/6152)
- [M 25741 — 25741](https://www.mendikat.net/track/espiguete-parking-cascada-mazobre-cresta-e-pd-inf-espiguete-canales-norte-f/25741)
- [M 28948 — 28948](https://www.mendikat.net/track/fraile-pena-del-cristo-sierra-pena-del-fraile-cueto-cristo-sierra/28948)
- [URL truncada — fraile-pena-del-santuario-del-brezo-pico-del-fraile-pena-cueto-cueto-herrera-santuar](https://www.mendikat.net/track/fraile-pena-del-santuario-del-brezo-pico-del-fraile-pena-cueto-cueto-herrera-santuar)
- [M 20006 — 20006](https://www.mendikat.net/track/lezna-cucayo-pico-pumar-lezna-pena/20006)
- [M 14584 — 14584](https://www.mendikat.net/track/mayor-pena-campos-de-la-pena-pena-mayor-pico-del-fraile-campos-de/14584)
- [M 25561 — 25561](https://www.mendikat.net/track/monte-cilda-monte-cilda-las-tuerces/25561)
- [M 28231 — 28231](https://www.mendikat.net/track/murcia-pico-cardano-de-arriba-pico-murcia-valcabe-las-cerezuelas-cardano-de-arriba-2023-07-16/28231)
- [M 16265 — 16265](https://www.mendikat.net/track/pena-lampa-velilla-del-rio-carrion-monte-valdehaya/16265)
- [M 16487 — 16487](https://www.mendikat.net/track/pena-prieta-cardano-de-arriba-alto-del-tio-celestino/16487)
- [M 2698 — 2698](https://www.mendikat.net/track/pena-prieta-cardano-de-arriba-pozo-lomas-pena/2698)
- [M 8280 — 8280](https://www.mendikat.net/track/pena-prieta-cardano-de-arriba-tres-provincias-pena/8280)
- [M 2696 — 2696](https://www.mendikat.net/track/pena-redonda-ascension-a-la-pena-redonda-por-el-valle/2696)
- [M 14227 — 14227](https://www.mendikat.net/track/pena-redonda-traspena-pena-redonda-burrian-barranco-de-santa-eulalia-traspena/14227)
- [M 10936 — 10936](https://www.mendikat.net/track/pena-tremaya-branosera-pena-tremaya-tremaya/10936)
- [M 9610 — 9610](https://www.mendikat.net/track/penalabra-mirador-de-piedrasluengas-penalabra-tres-mares/9610)
- [URL truncada — penalabra-mirador-pidedrasluengas-penalabra-tres-mares-sta-maria-de-redondo-travesia-jon-h](https://www.mendikat.net/track/penalabra-mirador-pidedrasluengas-penalabra-tres-mares-sta-maria-de-redondo-travesia-jon-hueso-)
- [M 14232 — 14232](https://www.mendikat.net/track/tres-mares-santa-maria-de-redondo-pico-tres-mares-cuchillon-santa-maria-de/14232)
- [M 12349 — 12349](https://www.mendikat.net/track/valcabado-cueva-de-los-franceses-canto-hito-valcabado-covalagua-cueva-de-los-franceses/12349)
- [M 16481 — 16481](https://www.mendikat.net/track/valdecebollas-branosera-sestil-alto-valdecebollas-cueto/16481)
- [M 9607 — 9607](https://www.mendikat.net/track/valdecebollas-valdecebollas-y-sestil-desde-branosera/9607)

**wikiloc.com** (44)

- [W 147075263 — abadia-de-lebanza-refugio-de-linares-hoyo-de-la-braguilla-147075263](https://www.wikiloc.com/hiking-trails/abadia-de-lebanza-refugio-de-linares-hoyo-de-la-braguilla-147075263)
- [W 3285945 — ascension-al-pico-cordel-2061-m-desde-branavieja-ida-3285945](https://www.wikiloc.com/hiking-trails/ascension-al-pico-cordel-2061-m-desde-branavieja-ida-3285945)
- [W 54764360 — ascension-al-pico-curavacas-por-callejo-grande-desde-vidrieros-54764360](https://www.wikiloc.com/hiking-trails/ascension-al-pico-curavacas-por-callejo-grande-desde-vidrieros-54764360)
- [150311857 — cascada-de-mazobre-cardano-de-arriba-150311857](https://www.wikiloc.com/hiking-trails/cascada-de-mazobre-cardano-de-arriba-150311857)
- [W 18537267 — cervera-de-pisuerga-tejeda-de-tosande-18537267](https://www.wikiloc.com/hiking-trails/cervera-de-pisuerga-tejeda-de-tosande-18537267)
- [W 104866053 — circular-curavacas-desde-vidrieros-curavacas-pico-hospital-monte-de-las-huelgas-y-descenso](https://www.wikiloc.com/hiking-trails/circular-curavacas-desde-vidrieros-curavacas-pico-hospital-monte-de-las-huelgas-y-descenso-por-coll-104866053)
- [W 55441243 — cordal-de-la-sierra-del-brezo-penas-mayores-y-pena-del-fraile-velilla-del-rio-carrion-pale](https://www.wikiloc.com/hiking-trails/cordal-de-la-sierra-del-brezo-penas-mayores-y-pena-del-fraile-velilla-del-rio-carrion-palencia-55441243)
- [110546072 — cueva-de-fuente-del-cobre-nacimiento-del-rio-pisuerga-110546072](https://www.wikiloc.com/hiking-trails/cueva-de-fuente-del-cobre-nacimiento-del-rio-pisuerga-110546072)
- [W 29960126 — espiguete-2-451-m-subida-por-arista-este-y-bajada-por-canal-de-la-cara-norte-cascada-de-ma](https://www.wikiloc.com/hiking-trails/espiguete-2-451-m-subida-por-arista-este-y-bajada-por-canal-de-la-cara-norte-cascada-de-mazobre-29960126)
- [W 11896919 — espiguete-cara-sur-11896919](https://www.wikiloc.com/hiking-trails/espiguete-cara-sur-11896919)
- [W 1782833 — integral-fuentes-carrionas-circular-2-noches-1782833](https://www.wikiloc.com/hiking-trails/integral-fuentes-carrionas-circular-2-noches-1782833)
- [W 28662748 — llanaves-de-la-reina-pena-prieta-tres-provincias-pico-del-infierno-28662748](https://www.wikiloc.com/hiking-trails/llanaves-de-la-reina-pena-prieta-tres-provincias-pico-del-infierno-28662748)
- [W 2884830 Piedrasluengas–Bistruey–Cucayo](https://www.wikiloc.com/hiking-trails/mirador-de-piedrasluengas-pena-bistruey-o-astruya-cucayo-2884830)
- [W 71294743 — pena-mayor-1-836-m-desde-poblado-de-compuerto-sierra-del-brezo-xi-71294743](https://www.wikiloc.com/hiking-trails/pena-mayor-1-836-m-desde-poblado-de-compuerto-sierra-del-brezo-xi-71294743)
- [W 6559240 — pena-prieta-desde-cardano-de-arriba-6559240](https://www.wikiloc.com/hiking-trails/pena-prieta-desde-cardano-de-arriba-6559240)
- [W 27328345 — pena-redonda-1-995-m-circular-por-el-cdo-de-burrian-desde-villanueva-de-la-pena-palencia-2](https://www.wikiloc.com/hiking-trails/pena-redonda-1-995-m-circular-por-el-cdo-de-burrian-desde-villanueva-de-la-pena-palencia-27328345)
- [W 108980041 — pena-tremaya-108980041](https://www.wikiloc.com/hiking-trails/pena-tremaya-108980041)
- [W 91646014 — penarredonda-1-993-m-desde-rebanal-de-las-llantas-sierra-del-brezo-xiii-91646014](https://www.wikiloc.com/hiking-trails/penarredonda-1-993-m-desde-rebanal-de-las-llantas-sierra-del-brezo-xiii-91646014)
- [W 76749509 — pico-cordel-76749509](https://www.wikiloc.com/hiking-trails/pico-cordel-76749509)
- [W 11774659 — pico-curavacas-montana-palentina-11774659](https://www.wikiloc.com/hiking-trails/pico-curavacas-montana-palentina-11774659)
- [W 36224517 — pico-del-fraile-36224517](https://www.wikiloc.com/hiking-trails/pico-del-fraile-36224517)
- [W 52397436 — pico-valdecebollas-desde-branosera-circular-julio-2020-52397436](https://www.wikiloc.com/hiking-trails/pico-valdecebollas-desde-branosera-circular-julio-2020-52397436)
- [W 40787618 — pomar-de-valdivia-menhir-canto-hito-mirador-de-valcabado-cueva-de-los-franceses-cascadas-d](https://www.wikiloc.com/hiking-trails/pomar-de-valdivia-menhir-canto-hito-mirador-de-valcabado-cueva-de-los-franceses-cascadas-de-covalag-40787618)
- [W 16686613 — pomar-de-valdivia-pena-corvera-menhir-cueva-de-los-franceses-cascada-de-covalagua-16686613](https://www.wikiloc.com/hiking-trails/pomar-de-valdivia-pena-corvera-menhir-cueva-de-los-franceses-cascada-de-covalagua-16686613)
- [W 141879616 — pozo-lomas-laguna-de-fuentes-carrionas-pozo-curavaca-pozos-del-ves-y-pozo-hoya-continua-se](https://www.wikiloc.com/hiking-trails/pozo-lomas-laguna-de-fuentes-carrionas-pozo-curavaca-pozos-del-ves-y-pozo-hoya-continua-seco-141879616)
- [W 178356481 — revelillas-pozo-de-los-lobos-178356481](https://www.wikiloc.com/hiking-trails/revelillas-pozo-de-los-lobos-178356481)
- [W 120952868 — revilla-de-pomar-cascada-de-covalagua-alto-de-ahedo-pozo-de-los-lobos-bosque-ahedo-1209528](https://www.wikiloc.com/hiking-trails/revilla-de-pomar-cascada-de-covalagua-alto-de-ahedo-pozo-de-los-lobos-bosque-ahedo-120952868)
- [10319076 — ruta-circular-sta-maria-de-redondo-cueva-del-cobre-parque-natural-fuentes-carrionas-palenc](https://www.wikiloc.com/hiking-trails/ruta-circular-sta-maria-de-redondo-cueva-del-cobre-parque-natural-fuentes-carrionas-palencia-10319076)
- [W 12093110 — ruta-semicircular-desde-lores-hasta-el-pico-lezna-y-el-pumar-12093110](https://www.wikiloc.com/hiking-trails/ruta-semicircular-desde-lores-hasta-el-pico-lezna-y-el-pumar-12093110)
- [17946364 — senda-de-fuente-cobrepr-p-8-17946364](https://www.wikiloc.com/hiking-trails/senda-de-fuente-cobrepr-p-8-17946364)
- [58921442 — senda-de-la-tejeda-de-tosande-58921442](https://www.wikiloc.com/hiking-trails/senda-de-la-tejeda-de-tosande-58921442)
- [22093550 — senda-de-la-tejeda-de-tosande-p-n-fuentes-carrionas-22093550](https://www.wikiloc.com/hiking-trails/senda-de-la-tejeda-de-tosande-p-n-fuentes-carrionas-22093550)
- [W 148786413 — subida-al-espiguete-por-su-cara-sur-148786413](https://www.wikiloc.com/hiking-trails/subida-al-espiguete-por-su-cara-sur-148786413)
- [W 143075784 — techo-de-palencia-pico-infierno-mojon-de-las-3-provincias-y-pena-prieta-desde-cardano-de-a](https://www.wikiloc.com/hiking-trails/techo-de-palencia-pico-infierno-mojon-de-las-3-provincias-y-pena-prieta-desde-cardano-de-arriba-143075784)
- [W 10221093 — tres-provincias-pena-prieta-pico-del-infierno-desde-cardano-de-arriba-10221093](https://www.wikiloc.com/hiking-trails/tres-provincias-pena-prieta-pico-del-infierno-desde-cardano-de-arriba-10221093)
- [W 2778852 — vidrieros-pozo-curavacas-2778852](https://www.wikiloc.com/hiking-trails/vidrieros-pozo-curavacas-2778852)
- [W 7433651 MTB](https://www.wikiloc.com/mountain-biking-trails/pozo-curavacas-por-el-valle-de-pineda-7433651)
- [W 11808759 — laguna-de-las-lomas-pena-prieta-pico-infierno-tres-provincias-cuartas-guadanas-matas-y-mur](https://www.wikiloc.com/mountaineering-trails/laguna-de-las-lomas-pena-prieta-pico-infierno-tres-provincias-cuartas-guadanas-matas-y-murcia-11808759)
- [W 6759091 — pozo-de-las-lomas-alto-de-fuentes-carrionas-desde-cardano-de-arriba-6759091](https://www.wikiloc.com/mountaineering-trails/pozo-de-las-lomas-alto-de-fuentes-carrionas-desde-cardano-de-arriba-6759091)
- [W 82945106 — pozo-las-lomas-laguna-de-fuentes-carrionas-pozo-curavacas-pozos-del-ves-circular-montana-p](https://www.wikiloc.com/mountaineering-trails/pozo-las-lomas-laguna-de-fuentes-carrionas-pozo-curavacas-pozos-del-ves-circular-montana-palentina-82945106)
- [W 141106061 — recorrido-a-las-5-pozas-de-fuentes-carrionas-con-cima-en-pena-prieta-141106061](https://www.wikiloc.com/trail-running-trails/recorrido-a-las-5-pozas-de-fuentes-carrionas-con-cima-en-pena-prieta-141106061)
- [Wikiloc — branosera](https://www.wikiloc.com/trails/back-country-skiing/spain/castille-and-leon/branosera)
- [W 163522451 — cascada-de-covalagua-desde-revilla-de-pomar-163522451](https://www.wikiloc.com/walking-trails/cascada-de-covalagua-desde-revilla-de-pomar-163522451)
- [EN — terms_en.html](https://www.wikiloc.com/wikiloc/terms_en.html)

**es.wikiloc.com** (43)

- [W 99549660 — canal-sur-del-curavacas-desde-vidrieros-99549660](https://es.wikiloc.com/rutas-alpinismo/canal-sur-del-curavacas-desde-vidrieros-99549660)
- [W 6765286 — canal-sur-directa-al-curavacas-6765286](https://es.wikiloc.com/rutas-alpinismo/canal-sur-directa-al-curavacas-6765286)
- [W 19857255 — espiguete-cara-norte-19857255](https://es.wikiloc.com/rutas-alpinismo/espiguete-cara-norte-19857255)
- [W 260648121 (03-2026)](https://es.wikiloc.com/rutas-alpinismo/espiguete-goulotte-norte-260648121)
- [W 9110380 — espiguete-invernal-por-el-corredor-norte-9110380](https://es.wikiloc.com/rutas-alpinismo/espiguete-invernal-por-el-corredor-norte-9110380)
- [W 68926959 — invernal-al-curavacas-por-canal-sur-directo-y-vuelta-por-callejo-grande-68926959](https://es.wikiloc.com/rutas-alpinismo/invernal-al-curavacas-por-canal-sur-directo-y-vuelta-por-callejo-grande-68926959)
- [W 15111234 Golobar](https://es.wikiloc.com/rutas-alpinismo/pico-valdecebollas-desde-el-refugio-del-golobar-15111234)
- [W 51963484 MTB](https://es.wikiloc.com/rutas-mountain-bike/pozo-curavacas-51963484)
- [W 133781826 MTB](https://es.wikiloc.com/rutas-mountain-bike/pozo-curavacas-desde-vidrieros-valle-de-pineda-montana-palentina-133781826)
- [W 14213545 — asc15-pena-lampa-14213545](https://es.wikiloc.com/rutas-senderismo/asc15-pena-lampa-14213545)
- [6384045 — cascada-de-mazobre-6384045](https://es.wikiloc.com/rutas-senderismo/cascada-de-mazobre-6384045)
- [177185185 — cascada-y-refugio-de-mazobre-177185185](https://es.wikiloc.com/rutas-senderismo/cascada-y-refugio-de-mazobre-177185185)
- [W 175034497 — circular-cardano-de-arriba-pozo-de-las-lomas-laguna-de-fuentes-carrionas-pozo-del-curavaca](https://es.wikiloc.com/rutas-senderismo/circular-cardano-de-arriba-pozo-de-las-lomas-laguna-de-fuentes-carrionas-pozo-del-curavacas-collado-175034497)
- [257716188 — cueva-del-cobre-desde-santa-maria-de-redondo-257716188](https://es.wikiloc.com/rutas-senderismo/cueva-del-cobre-desde-santa-maria-de-redondo-257716188)
- [W 133695529 — curavacas-desde-vidrieros-por-callejo-grande-133695529](https://es.wikiloc.com/rutas-senderismo/curavacas-desde-vidrieros-por-callejo-grande-133695529)
- [W 78127949 — importantes-cimas-de-la-sierra-del-brezo-circular-a-la-pena-redonda-y-pico-rebanal-por-el-](https://es.wikiloc.com/rutas-senderismo/importantes-cimas-de-la-sierra-del-brezo-circular-a-la-pena-redonda-y-pico-rebanal-por-el-barranco-78127949)
- [W 133377939 — las-tuerces-desde-aguilar-de-campoo-133377939](https://es.wikiloc.com/rutas-senderismo/las-tuerces-desde-aguilar-de-campoo-133377939)
- [W 5376595 — lores-pico-lezna-2208-m-cucayo-5376595](https://es.wikiloc.com/rutas-senderismo/lores-pico-lezna-2208-m-cucayo-5376595)
- [172187903 — maravilloso-paseo-por-la-senda-de-los-pescadores-de-velilla-del-rio-carrion-172187903](https://es.wikiloc.com/rutas-senderismo/maravilloso-paseo-por-la-senda-de-los-pescadores-de-velilla-del-rio-carrion-172187903)
- [24657668 — montana-palentina-tejeda-de-tosande-parque-natural-de-fuentes-carrionas-y-fuente-cobre-246](https://es.wikiloc.com/rutas-senderismo/montana-palentina-tejeda-de-tosande-parque-natural-de-fuentes-carrionas-y-fuente-cobre-24657668)
- [W 51590770 Carazo](https://es.wikiloc.com/rutas-senderismo/pena-carazo-y-horca-de-lores-desde-el-monasterio-de-sta-maria-de-lebanza-circular-51590770)
- [W 140549177 — pena-lampa-torre-magalana-roblon-el-monasterio-y-sabinar-de-pena-lampa-140549177](https://es.wikiloc.com/rutas-senderismo/pena-lampa-torre-magalana-roblon-el-monasterio-y-sabinar-de-pena-lampa-140549177)
- [W 51964148 — pena-prieta-desde-san-glorio-51964148](https://es.wikiloc.com/rutas-senderismo/pena-prieta-desde-san-glorio-51964148)
- [W 84958242 — pena-prieta-san-glorio-cubil-de-can-tres-provincias-pena-prieta-pico-del-infierno-san-glor](https://es.wikiloc.com/rutas-senderismo/pena-prieta-san-glorio-cubil-de-can-tres-provincias-pena-prieta-pico-del-infierno-san-glorio-cantab-84958242)
- [W 150328856 — pena-tremaya-desde-san-salvador-de-cantamuda-150328856](https://es.wikiloc.com/rutas-senderismo/pena-tremaya-desde-san-salvador-de-cantamuda-150328856)
- [W 4596617 — pena-tremaya-montana-palentina-4596617](https://es.wikiloc.com/rutas-senderismo/pena-tremaya-montana-palentina-4596617)
- [W 229808953 — penaprieta-y-pena-prieta-sur-o-pico-del-infierno-techo-provincial-palentino-229808953](https://es.wikiloc.com/rutas-senderismo/penaprieta-y-pena-prieta-sur-o-pico-del-infierno-techo-provincial-palentino-229808953)
- [W 95293455 — pico-lezna-y-pico-pumar-desde-cucayo-95293455](https://es.wikiloc.com/rutas-senderismo/pico-lezna-y-pico-pumar-desde-cucayo-95293455)
- [108316180 — senda-de-los-pescadores-en-velilla-del-rio-carrion-108316180](https://es.wikiloc.com/rutas-senderismo/senda-de-los-pescadores-en-velilla-del-rio-carrion-108316180)
- [28162002 — senda-de-los-pescadores-velilla-del-rio-carrion-28162002](https://es.wikiloc.com/rutas-senderismo/senda-de-los-pescadores-velilla-del-rio-carrion-28162002)
- [Wikiloc 33425902](https://es.wikiloc.com/rutas-senderismo/senda-del-bosque-fosil-verdena-33425902)
- [Wikiloc 43488041](https://es.wikiloc.com/rutas-senderismo/senda-del-roblon-de-estalaya-parque-natural-montana-palentina-43488041)
- [W 176630925 — subida-a-pena-lampa-176630925](https://es.wikiloc.com/rutas-senderismo/subida-a-pena-lampa-176630925)
- [W 220720071 — techo-de-palencia-pico-del-infierno2537m-por-canalagujas-de-cardanocon-pena-prieta2539m-y-](https://es.wikiloc.com/rutas-senderismo/techo-de-palencia-pico-del-infierno2537m-por-canalagujas-de-cardanocon-pena-prieta2539m-y-tres-prov-220720071)
- [141704149 — tejeda-de-tosande-desde-el-parking-141704149](https://es.wikiloc.com/rutas-senderismo/tejeda-de-tosande-desde-el-parking-141704149)
- [W 39754333 — tio-celestino-tres-provincias-pico-infierno-pena-prieta-sur-pena-prieta-alto-del-concejo-l](https://es.wikiloc.com/rutas-senderismo/tio-celestino-tres-provincias-pico-infierno-pena-prieta-sur-pena-prieta-alto-del-concejo-laguna-lom-39754333)
- [W 24446341 — valcabado-hayedo-monte-aedo-pozo-de-los-lobos-valcabado-24446341](https://es.wikiloc.com/rutas-senderismo/valcabado-hayedo-monte-aedo-pozo-de-los-lobos-valcabado-24446341)
- [W 15696656 — valdecebollas-desde-branosera-15696656](https://es.wikiloc.com/rutas-senderismo/valdecebollas-desde-branosera-15696656)
- [W 19631676 — vidrieros-pozo-curavacas-19631676](https://es.wikiloc.com/rutas-senderismo/vidrieros-pozo-curavacas-19631676)
- [W 77588245 — vidrieros-rio-carrion-valle-de-pineda-77588245](https://es.wikiloc.com/rutas-senderismo/vidrieros-rio-carrion-valle-de-pineda-77588245)
- [W 23841391 — vueltiviri-covalagua-y-monte-bernorio-27-3-18-23841391](https://es.wikiloc.com/rutas-senderismo/vueltiviri-covalagua-y-monte-bernorio-27-3-18-23841391)
- [Wikiloc waypoint](https://es.wikiloc.com/waypoints/3cnaOM/pico-cordel)
- [Términos ES — terms_es.html](https://es.wikiloc.com/wikiloc/terms_es.html)

**terranostrum.es** (25)

- [Terranostrum — ascension-pico-espiguete-por-la-cara-norte](https://www.terranostrum.es/senderismo/ascension-pico-espiguete-por-la-cara-norte)
- [Terranostrum — ascension-pico-espiguete-por-la-cara-sur](https://www.terranostrum.es/senderismo/ascension-pico-espiguete-por-la-cara-sur)
- [Terranostrum E1](https://www.terranostrum.es/senderismo/gr-1-palencia-etapa-1-cantabria-branosera)
- [Azul — las-tuerces-ruta-azul](https://www.terranostrum.es/senderismo/las-tuerces-ruta-azul)
- [Verde — las-tuerces-ruta-verde](https://www.terranostrum.es/senderismo/las-tuerces-ruta-verde)
- [Terranostrum Tuerces](https://www.terranostrum.es/senderismo/monumento-natural-de-las-tuerces)
- [Terranostrum E3](https://www.terranostrum.es/senderismo/palencia/montana-palentina/arbejal/gr1-palencia-etapa-3-estalaya-cervera-de-pisuerga)
- [Terranostrum E5](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-olvidado-en-palencia-etapa-5)
- [Terranostrum E6](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-olvidado-en-palencia-etapa-6)
- [Terranostrum E7](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-olvidado-en-palencia-etapa-7)
- [Terranostrum E6](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camporredondo-de-alba/gr1-palencia-etapa-6-camporredondo-de-alba-cruz-armada)
- [Terranostrum E4](https://www.terranostrum.es/senderismo/palencia/montana-palentina/cervera-de-pisuerga/gr1-palencia-etapa-4-cervera-de-pisuerga-triollo)
- [Terranostrum E2](https://www.terranostrum.es/senderismo/palencia/montana-palentina/estalaya/gr1-palencia-etapa-2-branosera-estalaya)
- [Terranostrum E5](https://www.terranostrum.es/senderismo/palencia/montana-palentina/gr1-palencia-etapa-5-triollo-camporredondo-de-alba)
- [Roja — las-tuerces-ruta-roja](https://www.terranostrum.es/senderismo/palencia/montana-palentina/las-tuerces-ruta-roja)
- [Terranostrum GPX](https://www.terranostrum.es/senderismo/palencia/montana-palentina/matalbaniega/ruta-btt-pedaleando-por-el-romanico-palentino)
- [Terranostrum — 1](https://www.terranostrum.es/senderismo/palencia/montana-palentina/revilla-de-pomar/1)
- [Terranostrum — integral-espacio-natural-de-covalagua](https://www.terranostrum.es/senderismo/palencia/montana-palentina/revilla-de-pomar/integral-espacio-natural-de-covalagua)
- [Terranostrum — pena-tremaya](https://www.terranostrum.es/senderismo/pena-tremaya)
- [Terranostrum — senda-de-los-pescadores-en-la-ribera-del-rio-carrion](https://www.terranostrum.es/senderismo/senda-de-los-pescadores-en-la-ribera-del-rio-carrion)
- [Terranostrum — sendero-cascada-de-covalagua](https://www.terranostrum.es/senderismo/sendero-cascada-de-covalagua)
- [Terranostrum — sendero-de-pena-amaya](https://www.terranostrum.es/senderismo/sendero-de-pena-amaya)
- [Terranostrum — sendero-triollo-hornamiel](https://www.terranostrum.es/senderismo/sendero-triollo-hornamiel)
- [aproximación Terranostrum](https://www.terranostrum.es/senderismo/sendero-vidrieros-pie-del-curavacas)
- [Terranostrum — visita-cueva-de-los-franceses](https://www.terranostrum.es/turismo/palencia/montana-palentina/revilla-de-pomar/visita-cueva-de-los-franceses)

**lapedrerapindia.com** (16)

- [QR — Espiguete](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Espiguete)
- [QR — Peña-Carazo](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-Carazo)
- [QR — Peña-Cilda](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-Cilda)
- [QR — Peña-Labra](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-Labra)
- [QR — Peña-Mesa](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-Mesa)
- [QR — Peña-Redonda](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-Redonda)
- [QR — Peña-del-Fraile](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peña-del-Fraile)
- [QR — Peñas-Mayores](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Peñas-Mayores)
- [QR — Pico-Las-Cruces](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Pico-Las-Cruces)
- [QR — Pico-Murcia](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Pico-Murcia)
- [QR — Pico-Tres-Mares](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Pico-Tres-Mares)
- [QR — Santa-lucia](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Santa-lucia)
- [QR — Valdecebollas](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/Valdecebollas)
- [QR — la-peña-del-tejo](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/la-peña-del-tejo)
- [QR — peña-del-infierno](http://lapedrerapindia.com/rutas-montana-palentina/ascensiones/peña-del-infierno)
- [QR — curavacas](http://www.lapedrerapindia.com/rutas-montana-palentina/ascensiones/curavacas)

**aemet.es** (12)

- [PDF fijo — BPA_PN_Picos_Europa.pdf](https://www.aemet.es/documentos/es/eltiempo/prediccion/montana/boletin_peligro_aludes/BPA_PN_Picos_Europa.pdf)
- [PDF fijo — BPA_sierra_Cordel_PLabra.pdf](https://www.aemet.es/documentos/es/eltiempo/prediccion/montana/boletin_peligro_aludes/BPA_sierra_Cordel_PLabra.pdf)
- [Escala — escala_peligro_aludes](https://www.aemet.es/es/conocermas/montana/detalles/escala_peligro_aludes)
- [servicios de montaña](https://www.aemet.es/es/conocermas/montana/detalles/serv_meteo)
- [boletín ampliado](https://www.aemet.es/es/eltiempo/prediccion/montana/boletin_montana/ampliacion)
- [Boletines — boletin_peligro_aludes](https://www.aemet.es/es/eltiempo/prediccion/montana/boletin_peligro_aludes)
- [AEMET peu1 — montana?w=&p=peu1](https://www.aemet.es/es/eltiempo/prediccion/montana?w=&p=peu1)
- [Aguilar id34004](https://www.aemet.es/es/eltiempo/prediccion/municipios/aguilar-de-campoo-id34004)
- [Cervera id34056](https://www.aemet.es/es/eltiempo/prediccion/municipios/cervera-de-pisuerga-id34056)
- [Velilla id34199](https://www.aemet.es/es/eltiempo/prediccion/municipios/velilla-del-rio-carrion-id34199)
- [Brañosera id34036](https://www.aemet.es/gl/eltiempo/prediccion/municipios/branosera-id34036)
- [ejemplo — 20261121_predmmon_peu1.xml](https://www.aemet.es/xml/montana/20261121_predmmon_peu1.xml)

**palenciaturismo.es** (11)

- [folleto Diputación](https://palenciaturismo.es/system/files/2019-08/2-SendaLagunaLomas.pdf)
- [PDF — Pedaleando.pdf](https://palenciaturismo.es/system/files/2020-04/Pedaleando.pdf)
- [Libro ES — LIBRO MONTAÑA PALENTINA (versión español).pdf](https://palenciaturismo.es/system/files/2026-05/LIBRO%20MONTA%C3%91A%20PALENTINA%20%28versi%C3%B3n%20espa%C3%B1ol%29.pdf)
- [EN — LIBRO MONTAÑA PALENTINA (versión Inglés).pdf](https://palenciaturismo.es/system/files/2026-05/LIBRO%20MONTAN%CC%83A%20PALENTINA%20%28versio%CC%81n%20Ingle%CC%81s%29.pdf)
- [listado — rutas-naturales](https://www.palenciaturismo.es/que-hacer/rutas-naturales)
- [palenciaturismo](https://www.palenciaturismo.es/que-hacer/rutas/senda-bosque-fosil)
- [palenciaturismo](https://www.palenciaturismo.es/que-hacer/rutas/senda-fuente-cobre)
- [palenciaturismo](https://www.palenciaturismo.es/que-hacer/rutas/senda-pescadores)
- [palenciaturismo](https://www.palenciaturismo.es/system/files/2019-08/Casa%20parque%201.pdf)
- [Libro 2026-06](https://www.palenciaturismo.es/system/files/2026-06/LIBRO%20MONTA%C3%91A%20PALENTINA%20%28versi%C3%B3n%20espa%C3%B1ol%29%20%281%29.pdf)
- [Mapa interactivo](https://www.palenciaturismo.es/system/files/2026-06/MAPA%20MONTA%C3%91A%20PALENTINA%20%28formato%20interactivo%20digital%29%20INTERNET_0.pdf)

**turismocastillayleon.com** (11)

- [Turismo CyL — parque-natural-da-serra-palentina](https://www.turismocastillayleon.com/douro/pt/espacos-naturais/parque-natural-da-serra-palentina)
- [Turismo CyL — casa-parque-natural-montana-palentina](https://www.turismocastillayleon.com/es/naturaleza/casa-parque-natural-montana-palentina)
- [Turismo CyL — nestar-cordovilla-aguilar](https://www.turismocastillayleon.com/es/naturaleza/nestar-cordovilla-aguilar)
- [Turismo CyL P3](https://www.turismocastillayleon.com/es/naturaleza/p3-senda-lagunas-lomas)
- [Turismo CyL P4](https://www.turismocastillayleon.com/es/naturaleza/p4-senda-tejeda-tosande)
- [Turismo CyL P9](https://www.turismocastillayleon.com/es/naturaleza/p9-senda-cascada-mazobre)
- [Turismo CyL — rio-pisuerga-villaescusa-torres](https://www.turismocastillayleon.com/es/naturaleza/rio-pisuerga-villaescusa-torres)
- [Turismo CyL — centro-interpretacion-mineria](https://www.turismocastillayleon.com/es/patrimonio-cultura/centro-interpretacion-mineria)
- [Turismo CyL — geoparque-mundial-unesco-loras](https://www.turismocastillayleon.com/es/rural-naturaleza/geoparques/geoparque-mundial-unesco-loras)
- [Turismo CyL — pena-prieta-llanaves-reina](https://www.turismocastillayleon.com/es/rural-naturaleza/rutas-naturaleza/pena-prieta-llanaves-reina)
- [Turismo CyL — oficina-comarcal-turismo-cervera-pisuerga](https://www.turismocastillayleon.com/es/servicios/oficinas-turismo-4ec3/oficina-comarcal-turismo-cervera-pisuerga)

**diputaciondepalencia.es** (7)

- [buscador — buscar?search_api_fulltext=esquí+de+montaña](https://www.diputaciondepalencia.es/buscar?search_api_fulltext=esqu%C3%AD+de+monta%C3%B1a)
- [Diputación senderismo](https://www.diputaciondepalencia.es/sitio/turismo/rutas-naturaleza/senderismo)
- [Guía Diputación](https://www.diputaciondepalencia.es/system/files/2024-05/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf)
- [PDF Diputación](https://www.diputaciondepalencia.es/system/files/2024-05/guia_de_curavacas_y_espiguete-interactivo.pdf)
- [PDF 2016 — ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf](https://www.diputaciondepalencia.es/system/files/publicacion-pdf/20160817/ascensiones_en_la_montana_palentina_-_version_digital_gratuita.pdf)
- [PDF — guia_btt_cicloturismo.pdf](https://www.diputaciondepalencia.es/system/files/publicacion-pdf/20161221/guia_btt_cicloturismo.pdf)
- [PDF — guia_de_montanismo_invernal_en_la_montana_palentina.pdf](https://www.diputaciondepalencia.es/system/files/publicacion-pdf/20171220/guia_de_montanismo_invernal_en_la_montana_palentina.pdf)

**komoot.com** (6)

- [komoot guide — 366047](https://www.komoot.com/el-gr/guide/366047)
- [Komoot — senda-del-escultor-ursi-pcr-p02-ruta-circular-por-el-parque-natural-montana-palentina](https://www.komoot.com/es-es/smarttour/e1067879553/senda-del-escultor-ursi-pcr-p02-ruta-circular-por-el-parque-natural-montana-palentina)
- [komoot — 5786112](https://www.komoot.com/highlight/5786112)
- [Komoot Tres Mares](https://www.komoot.com/highlight/6230012)
- [Komoot variante con Pico Murcia](https://www.komoot.com/smarttour/31449033)
- [Komoot — aguilar-de-campoo-monte-bernorio-y-castillo-de-gama-circular-por-el-espacio-natural-de-las](https://www.komoot.com/smarttour/e1165088482/aguilar-de-campoo-monte-bernorio-y-castillo-de-gama-circular-por-el-espacio-natural-de-las-tuerces)

**alltrails.com** (5)

- [AllTrails — senda-de-los-pescadores-en-la-ribera-del-rio-carrion](https://www.alltrails.com/en-gb/trail/spain/palencia/senda-de-los-pescadores-en-la-ribera-del-rio-carrion)
- [AllTrails parque](https://www.alltrails.com/parks/spain/palencia/espacio-natural-de-las-tuerces)
- [AllTrails — parque-natural-montana-palentina](https://www.alltrails.com/parks/spain/palencia/parque-natural-montana-palentina)
- [AllTrails — pr-p-8-senda-de-fuente-cobre](https://www.alltrails.com/trail/spain/palencia/pr-p-8-senda-de-fuente-cobre)
- [AllTrails Verde](https://www.alltrails.com/trail/spain/palencia/ruta-verde-las-tuerces)

**blog.komoot.nl** (5)

- [Komoot Brañosera](https://blog.komoot.nl/guide/1544283/hiking-around-branosera)
- [Komoot 2 — curavacas-from-vidrieros-parque-natural-montana-palentina](https://blog.komoot.nl/smarttour/e1068189616/curavacas-from-vidrieros-parque-natural-montana-palentina)
- [Komoot — espigueete-by-the-east-ridge-circular-in-the-parque-natural-montana-palentina](https://blog.komoot.nl/smarttour/e1068198404/espigueete-by-the-east-ridge-circular-in-the-parque-natural-montana-palentina)
- [Komoot — cascada-de-covalagua-desde-revilla-de-pomar-paisaje-protegido-de-covalagua](https://blog.komoot.nl/smarttour/e1068341662/cascada-de-covalagua-desde-revilla-de-pomar-paisaje-protegido-de-covalagua)
- [Komoot Golobar](https://blog.komoot.nl/smarttour/e1093102700/pico-valdecebollas-from-golobar-trail)

**boe.es** (5)

- [BOE-A-2021-908](https://boe.es//boe/dias/2021/01/22/pdfs/BOE-A-2021-908.pdf)
- [BOE-A-2010-9353](https://boe.es/boe/dias/2010/06/14/pdfs/BOE-A-2010-9353.pdf)
- [BOE-A-2015-4103](https://boe.es/buscar/act.php?id=BOE-A-2015-4103)
- [BOE consolidado](https://www.boe.es/buscar/act.php?id=BOE-A-2000-13439)
- [ELI — 4](https://www.boe.es/eli/es-cl/l/2000/06/27/4)

**recorrepicos.com** (5)

- [PDF — Senda_Pescadores_Velilla.pdf](https://www.recorrepicos.com/DATOS/Senda_Pescadores_Velilla.pdf)
- [Recorrepicos — Covalagua.HTM](https://www.recorrepicos.com/Rutas/Covalagua.HTM)
- [Recorrepicos — Monte_Bernorio.htm](https://www.recorrepicos.com/Rutas/Monte_Bernorio.htm)
- [Recorrepicos — PenaLampa_por_Velilla.htm](https://www.recorrepicos.com/Rutas/PenaLampa_por_Velilla.htm)
- [Recorrepicos — Pena_Amaya.htm](https://www.recorrepicos.com/Rutas/Pena_Amaya.htm)

**blog.komoot.de** (4)

- [Komoot — pena-prieta-pena-del-infierno-y-mojon-de-tres-provincias-circular-por-el-parque-natural-mo](https://blog.komoot.de/smarttour/e1068265978/pena-prieta-pena-del-infierno-y-mojon-de-tres-provincias-circular-por-el-parque-natural-montana-palentina)
- [Komoot — curavacas-normal-route-via-callejo-grande](https://blog.komoot.de/smarttour/e1118937486/curavacas-normal-route-via-callejo-grande)
- [Komoot — valcabado-viewpoint-pozo-de-los-lobos-and-covalagua-loop](https://blog.komoot.de/smarttour/e1175902813/valcabado-viewpoint-pozo-de-los-lobos-and-covalagua-loop)
- [Komoot — mountain-biking-through-las-tuerces-and-covalagua](https://blog.komoot.de/smarttour/e1494750275/mountain-biking-through-las-tuerces-and-covalagua)

**diariodevalderrueda.es** (4)

- [Valderrueda — restricciones-pico-curavacas-proteger-tres-familias-osos](https://www.diariodevalderrueda.es/texto-diario/mostrar/5917422/restricciones-pico-curavacas-proteger-tres-familias-osos)
- [ampliación — ampliadas-mes-restricciones-curavacas-tres-familias-osos](https://www.diariodevalderrueda.es/texto-diario/mostrar/5938807/ampliadas-mes-restricciones-curavacas-tres-familias-osos)
- [Valderrueda — cuenta-atras-retadora-ultra-montana-palentina-2026](https://www.diariodevalderrueda.es/texto-diario/mostrar/6003539/cuenta-atras-retadora-ultra-montana-palentina-2026)
- [Valderrueda — asi-ve-berrea-fuentes-carrionas-montana-palentina](https://www.diariodevalderrueda.es/texto-diario/mostrar/856487/asi-ve-berrea-fuentes-carrionas-montana-palentina)

**geoparquelasloras.es** (4)

- [Noticia — el-geoparque-las-loras-lanza-las-loras-360-una-nueva-aplicacion-para-descubrir-el-territor](https://geoparquelasloras.es/2026/11/19/el-geoparque-las-loras-lanza-las-loras-360-una-nueva-aplicacion-para-descubrir-el-territorio-a-traves-de-rutas-turisticas/)
- [Geoparque — anticlinal-de-villaescusa-de-ecla-geotrack-english-version](https://geoparquelasloras.es/anticlinal-de-villaescusa-de-ecla-geotrack-english-version/)
- [Fuentes del Odra](https://geoparquelasloras.es/las-fuentes-del-odra-geotrack/)
- [PDF 2026 — Descubriendo-el-geoparque-2026.pdf](https://geoparquelasloras.es/wp-content/uploads/2026/06/Descubriendo-el-geoparque-2026.pdf)

**idee.es** (4)

- [metadatos — spaignCNT](https://idee.es/csw-inspire-idee/static/api/records/spaignCNT)
- [MDS — spaignMDS](https://idee.es/csw-inspire-idee/static/api/records/spaignMDS)
- [JIIDE 2019 — 2_MapaLidar_JIIDE2019.pdf](https://idee.es/resources/presentaciones/JIIDE19/dia_24/AUDITORIO_PRINCIPAL/1.Sesion_1_Nuevos_Desarrollos/2_MapaLidar_JIIDE2019.pdf)
- [IDEE FEDME — spaignFEDME](https://www.idee.es/csw-inspire-idee/srv/api/records/spaignFEDME)

**saludcastillayleon.es** (4)

- [saludcastillayleon](https://www.saludcastillayleon.es/CAPalencia/en/area-influencia/z-b-s-cervera-pisuerga)
- [saludcastillayleon](https://www.saludcastillayleon.es/CAPalencia/es/area-influencia/z-b-s-aguilar-campoo)
- [saludcastillayleon](https://www.saludcastillayleon.es/CAPalencia/fr/cartera-servicios/urgencias)
- [saludcastillayleon](https://www.saludcastillayleon.es/es/citaprevia/centros-adscritos-sistema-cita-previa/palencia)

**summitpost.org** (4)

- [SummitPost Cardaño](https://summitpost.org/carda-o-de-arriba/188808)
- [SummitPost — 153553](https://summitpost.org/curavacas/153553)
- [SummitPost — espig-ete.html](https://www.summitpost.org/parent/473308/espig-ete.html)
- [SummitPost ruta](https://www.summitpost.org/route/474243/north-face-classic-eastern-ridge.html)

**bocyl.jcyl.es** (3)

- [BOCyL PDF — BOCYL-D-21071998-7.pdf](https://bocyl.jcyl.es/boletines/1998/07/21/pdf/BOCYL-D-21071998-7.pdf)
- [BOCyL — BOCYL-D-05072000-1.pdf](https://bocyl.jcyl.es/boletines/2000/07/05/pdf/BOCYL-D-05072000-1.pdf)
- [HTML — BOCYL-D-21071998-7.do](https://bocyl.jcyl.es/html/1998/07/21/html/BOCYL-D-21071998-7.do)

**datos.gob.es** (3)

- [datos.gob.es — centro-de-descargas](https://datos.gob.es/es/aplicaciones/centro-de-descargas)
- [datos.gob.es — a17002943-senderos](https://datos.gob.es/es/catalogo/a17002943-senderos)
- [Mapa LiDAR — e00125901-spaign-mapa-lidar](https://datos.gob.es/es/catalogo/e00125901-spaign-mapa-lidar)

**diariodeleon.es** (3)

- [Diario de León](https://www.diariodeleon.es/castilla-y-leon/250516/2048292/grupo-rescate-junta-auxilia-montanero-herido-espiguete.html)
- [Diario de León](https://www.diariodeleon.es/leon/provincia/210109/736160/diecisiete-carreteras-provincia-afectadas-nieve-siete-cadenas-intransitable.html)
- [Diario de León](https://www.diariodeleon.es/leon/provincia/250805/2056076/greim-sabero-leon-interviene-23-rescates-montana-38-personas-2025.html)

**fundacionosopardo.org** (3)

- [FOP — what-to-do-if-encountering-a-bear](https://fundacionosopardo.org/what-to-do-if-encountering-a-bear/)
- [infografía — Infografia_AEFONA-FOP_enviada.pdf](https://fundacionosopardo.org/wp-content/uploads/2023/10/Infografia_AEFONA-FOP_enviada.pdf)
- [FOP ficha — ficha1_2025_ESP-1.pdf](https://fundacionosopardo.org/wp-content/uploads/2025/04/ficha1_2025_ESP-1.pdf)

**cerveradepisuerga.eu** (2)

- [Cervera — rutas-detalle.php?idRuta=14](https://www.cerveradepisuerga.eu/rutas-detalle.php?idRuta=14)
- [Cervera — rutas-detalle.php?idRuta=3](https://www.cerveradepisuerga.eu/rutas-detalle.php?idRuta=3)

**dev.subastasdecaza.cesefor.com** (2)

- [Cesefor — 832](https://dev.subastasdecaza.cesefor.com/en/node/832)
- [PDF — plan_de_caza_rrc_2021_2022.pdf](https://dev.subastasdecaza.cesefor.com/sites/default/files/plan_de_caza_rrc_2021_2022.pdf)

**elmirondesoria.es** (2)

- [El Mirón de Soria](https://elmirondesoria.es/soria/sucesos/fallece-montanero-en-monte-curavacas/amp)
- [El Mirón (Espigüete)](https://elmirondesoria.es/soria/sucesos/rescatados-dos-montaneros-enriscados-en-pico-espigueete/amp)

**es.wikipedia.org** (2)

- [Wikipedia — Estación_de_esquí_de_San_Glorio](https://es.wikipedia.org/wiki/Estaci%C3%B3n_de_esqu%C3%AD_de_San_Glorio)
- [Wikipedia — Parque_natural_Montaña_Palentina](https://es.wikipedia.org/wiki/Parque_natural_Monta%C3%B1a_Palentina)

**hikingiberia.com** (2)

- [HikingIberia Híjar](https://www.hikingiberia.com/resources/routes/es/cordillera-cantabrica-sierra-hijar-valdecebollas.pdf)
- [HikingIberia PDF](https://www.hikingiberia.com/resources/routes/es/fuentes-carrionas-curavacas.pdf)

**hoteles.net** (2)

- [hoteles.net — cascada-de-covalagua-ruta-facil-y-como-llegar-a-este-rincon-natural.html](https://www.hoteles.net/palencia/aguilar-de-campoo/cascada-de-covalagua-ruta-facil-y-como-llegar-a-este-rincon-natural.html)
- [hoteles.net — cascada-mazobre-palencia.html](https://www.hoteles.net/palencia/cervera-de-pisuerga/cascada-mazobre-palencia.html)

**ign.es** (2)

- [Condiciones IGN](https://www.ign.es/resources/licencia/Condiciones_licenciaUso_IGN.pdf)
- https://www.ign.es/wmts/pnoa-ma

**inspire-geoportal.ec.europa.eu** (2)

- [INSPIRE spaignMDT05](https://inspire-geoportal.ec.europa.eu/srv/api/records/spaignMDT05)
- [WCS MDT — spaignwcs_mdt](https://inspire-geoportal.ec.europa.eu/srv/api/records/spaignwcs_mdt)

**lagarafa.blogspot.com** (2)

- [La Diagonal — curavacas-la-diagonal.html](http://lagarafa.blogspot.com/2014/03/curavacas-la-diagonal.html)
- [La Garafa — pena-amaya.html](https://lagarafa.blogspot.com/2025/02/pena-amaya.html)

**mapa.gob.es** (2)

- [Etapa II — default.aspx](https://www.mapa.gob.es/en/desarrollo-rural/temas/caminos-naturales/caminos-naturales/sector-noroeste/romanico-palentino/etapa-ii/default.aspx)
- [Etapa V — default.aspx](https://www.mapa.gob.es/en/desarrollo-rural/temas/caminos-naturales/caminos-naturales/sector-noroeste/romanico-palentino/etapa-v/default.aspx)

**palenciaenlared.es** (2)

- [Palencia en la Red](https://www.palenciaenlared.es/establecen-limitaciones-temporales-de-transito-en-el-curavacas-por-la-presencia-de-osos/)
- [Palencia en la Red](https://www.palenciaenlared.es/video-tres-rescates-en-el-espiguete-movilizan-al-grupo-de-rescate-de-la-junta-y-al-greim-de-sabero/)

**peakvisor.com** (2)

- [peakvisor — refugio-de-majadas-de-fuentes-carrionas.html](https://peakvisor.com/mountain-hut/refugio-de-majadas-de-fuentes-carrionas.html)
- [peakvisor — pena-prieta.html](https://peakvisor.com/peak/pena-prieta.html)

**pyrenaica.emf.eus** (2)

- [Pyrenaica 286](https://pyrenaica.emf.eus/wp-content/uploads/aldizkariak/286/artikulua_5998.pdf)
- [Pyrenaica 112](https://pyrenaica.emf.eus/wp-content/uploads/hemeroteka/112/pdf/pyrenaica_112_62.pdf)

**siempredepaso.es** (2)

- [Siempre de paso](https://siempredepaso.es/como-subir-a-pena-tremaya-palencia)
- [siempredepaso](https://siempredepaso.es/disfruta-de-la-berrea-en-la-montana-palentina)

**spain.info** (2)

- [Spain.info — cueva-franceses](https://www.spain.info/es/lugares-interes/cueva-franceses/)
- [Spain.info — parque-natural-fuentes-carrionas-fuente-cobre-montana-palentina](https://www.spain.info/es/naturaleza/parque-natural-fuentes-carrionas-fuente-cobre-montana-palentina/)

**valderredible.es** (2)

- [Valderredible](https://www.valderredible.es/rutas/revelillas-pozo-de-los-lobos)
- [PDF — revelilla_-_pozo_de_los_lobos.pdf](https://www.valderredible.es/uploads/editor/files/266/revelilla_-_pozo_de_los_lobos.pdf)

**walkaholic.me** (2)

- [walkaholic — 234-refugio-mazobre](https://www.walkaholic.me/es/refugio/espana/castilla-y-leon/palencia/234-refugio-mazobre)
- [walkaholic — 306-refugio-de-los-pescadores](https://www.walkaholic.me/shelter/spain/castile-and-leon/palencia/306-refugio-de-los-pescadores)

**aesgalla.blogspot.com** (1)

- [A Esgalla — 2000s-de-la-montana-palentina-indice.html](http://aesgalla.blogspot.com/2012/02/2000s-de-la-montana-palentina-indice.html)

**alsa.com** (1)

- [Alsa — estacao-palencia](https://www.alsa.com/pt/estacoes/estacao-palencia)

**apps.apple.com** (1)

- [App Store — id6761060682](https://apps.apple.com/es/app/las-loras-360/id6761060682)

**aragon.es** (1)

- [Aragón — vuelo-drones-espacios-naturales-protegidos](https://www.aragon.es/-/vuelo-drones-espacios-naturales-protegidos)

**asturiasmundial.com** (1)

- [Asturias Mundial](https://www.asturiasmundial.com/noticia/144945/oso-pardo-podria-superar-ya-400-ejemplares-asturias-necesita-nuevo-censo-conocer-poblacion-real/)

**barruelo.com** (1)

- [licitación — licitacion-cim.pdf](https://barruelo.com/descargas_breves/licitacion-cim.pdf)

**blog.komoot.it** (1)

- [Komoot — pico-del-fraile-desde-el-santuario-de-nuestra-senora-del-brezo-trailrunning-por-el-parque-](https://blog.komoot.it/smarttour/e1119554974/pico-del-fraile-desde-el-santuario-de-nuestra-senora-del-brezo-trailrunning-por-el-parque-natural-montana-palentina)

**casasdegamaylastuerces.com** (1)

- [Casas de Gama](https://casasdegamaylastuerces.com/rutas-por-las-tuerces.php)

**casiaventurilla.com** (1)

- [casiaventurilla](http://www.casiaventurilla.com/fuentes-carrionas-montana-palentina-cascada-de-mazobre)

**centrodedescargas.cnig.es** (1)

- [Centro de Descargas MDT02](https://centrodedescargas.cnig.es/CentroDescargas/modelo-digital-terreno-mdt02-segunda-cobertura)

**cis2.eea.europa.eu** (1)

- [EEA — 912](https://cis2.eea.europa.eu/data/912)

**cope.es** (1)

- [COPE — ultra-montana-palentina-agota-500-plazas-edicion-2026-20260905_3430677.html](https://www.cope.es/emisoras/castilla-y-leon/palencia-provincia/palencia/noticias/ultra-montana-palentina-agota-500-plazas-edicion-2026-20260905_3430677.html)

**creativecommons.org** (1)

- [CC BY 4.0 — deed.es](https://creativecommons.org/licenses/by/4.0/deed.es)

**daledeporte.es** (1)

- [DaleDeporte — palencia](https://www.daledeporte.es/events/palencia)

**desnivel.com** (1)

- [Desnivel — la-bella-desconocida-montana-palentina-invernal](https://www.desnivel.com/alpinismo/la-bella-desconocida-montana-palentina-invernal/)

**dgt.es** (1)

- [DGT — NP-AVISO-DGT-NIEVE.pdf](https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/nota_prensa/20251119-Imprescindible-consultar-el-estado-de-vialidad-de-las-carreteras-antes-de-realizar-desplazamientos/NP-AVISO-DGT-NIEVE.pdf)

**ecoticias.com** (1)

- [Ecoticias — geoparque-loras-itinerario-ciclista](https://www.ecoticias.com/naturaleza/geoparque-loras-itinerario-ciclista)

**elespanol.com** (1)

- [El Español — 1003743761154_0.html](https://www.elespanol.com/castilla-y-leon/region/palencia/20250516/rescatado-helicoptero-montanero-herido-aparatosa-caida-pico-espiguete/1003743761154_0.html)

**faunatura.com** (1)

- [Faunatura — oso-pardo-cantabrico-donde-vive-y-por-que-su-recuperacion-es-una-buena-noticia.html](https://www.faunatura.com/oso-pardo-cantabrico-donde-vive-y-por-que-su-recuperacion-es-una-buena-noticia.html)

**fclm.com** (1)

- [fclm 2016 — las-raquetas-de-nieve-y-el-esqui-aterrizan-en-la-montana-palentina](https://www.fclm.com/2016/02/23/las-raquetas-de-nieve-y-el-esqui-aterrizan-en-la-montana-palentina/)

**femecv.com** (1)

- [FEMECV — Opciones comunicacion montana.pdf](https://www.femecv.com/sites/default/files/uploads/files/Opciones%20comunicacion%20montana.pdf)

**fmdva.org** (1)

- [fmdva.org — 07-docente-fuente-del-cobre.pdf](https://www.fmdva.org/media/oi1nwveq/07-docente-fuente-del-cobre.pdf)

**gataconbotas.com** (1)

- [Gataconbotas — subida-a-pena-amaya](https://gataconbotas.com/subida-a-pena-amaya/)

**guardo.org** (1)

- [Guardo (antiguo)](https://guardo.org/conoce-guardo/como-llegar-horarios-de-transporte/)

**guiarepsol.com** (1)

- [Guía Repsol — ruta-con-perro-espiguete-palencia](https://www.guiarepsol.com/es/viajar/con-mi-mascota/ruta-con-perro-espiguete-palencia/)

**guiaszonacentro.com** (1)

- [Guías Zona Centro](https://www.guiaszonacentro.com/montana-palentina-fin-de-semana-con-raquetas-de-nieve/)

**hiking.waymarkedtrails.org** (1)

- https://hiking.waymarkedtrails.org/#search?query=GR%201

**idecyl.jcyl.es** (1)

- [IDECyL — SPAGOBCYLCITDTSELMDT0811](https://idecyl.jcyl.es/geonetwork/srv/api/records/SPAGOBCYLCITDTSELMDT0811)

**idecyl.jcyl.es:443** (1)

- [IDECyL ZNE — SPAGOBCYLMNADTSPSZNE](https://idecyl.jcyl.es:443/geonetwork/docs/api/records/SPAGOBCYLMNADTSPSZNE)

**ileon.eldiario.es** (1)

- [ileon — presencia-familias-oso-pardo-lleva-junta-impedir-visitantes-pena-escrita-montana-palentina](https://ileon.eldiario.es/tierra-verde/presencia-familias-oso-pardo-lleva-junta-impedir-visitantes-pena-escrita-montana-palentina_1_9538826.html)

**infobierzo.com** (1)

- [Infobierzo — danos-oso-pardo-provincia-leon-2025_1035407_102.html](https://www.infobierzo.com/provincia/danos-oso-pardo-provincia-leon-2025_1035407_102.html)

**labolsadelcorredor.com** (1)

- [La Bolsa del Corredor](https://www.labolsadelcorredor.com/calendario-carreras-trail-running-2026/)

**lagacetadesalamanca.es** (1)

- [La Gaceta — evacuados-dos-montaneros-enriscados-zona-nevada-pico-20250516221200-nt.html](https://www.lagacetadesalamanca.es/sucesos/evacuados-dos-montaneros-enriscados-zona-nevada-pico-20250516221200-nt.html)

**loc.wiki** (1)

- [loc.wiki 3248647](https://www.loc.wiki/mountaineering-trails/invernal-curavacas-canal-sur-callejo-grande-3248647)

**luiscrespofernandez.com** (1)

- [12 rutas de Luis Crespo](https://www.luiscrespofernandez.com/post/raquetasnievepalencia)

**meteosierra.com** (1)

- [Meteosierra — pena-prieta-y-agujas-de-cardano](https://meteosierra.com/montana/cordillera-cantabrica/pena-prieta-y-agujas-de-cardano/)

**miteco.gob.es** (1)

- [MITECO — ProtocoloIntervencion_osos_cantabricos_aprobadoCSMA_20260622.pdf](https://www.miteco.gob.es/content/dam/miteco/es/biodiversidad/temas/conservacion-de-especies/esp-prot-especial/ProtocoloIntervencion_osos_cantabricos_aprobadoCSMA_20260622.pdf)

**montanapalentinahoy.com** (1)

- [Montaña Palentina Hoy](https://www.montanapalentinahoy.com/2019/12/el-parque-natural-montana-palentina.html)

**montanapegaso.es** (1)

- [Montaña Pegaso](https://www.montanapegaso.es/carteles/2016/sanglorio_info.pdf)

**nemus.org** (1)

- [Nemus — 2019-11-01-fuentes-carrionas.html](https://www.nemus.org/2019-11-01-fuentes-carrionas.html)

**ninos.kiddle.co** (1)

- [Kiddle — Peña_Redonda](https://ninos.kiddle.co/Peña_Redonda)

**nuevecuatrouno.com** (1)

- [nuevecuatrouno](https://nuevecuatrouno.com/2024/05/26/sucesos-muere-montanero-riojano-57-anos-espiguete-palencia/)

**ojolince.com** (1)

- [Ojolince — pena-lampa-y-valdehaya-en-otono.html](http://www.ojolince.com/2018/12/pena-lampa-y-valdehaya-en-otono.html)

**omio.es** (1)

- [omio — cervera-de-pisuerga](https://www.omio.es/autobuses/bilbao/cervera-de-pisuerga)

**overpass-api.de** (1)

- https://overpass-api.de/api/interpreter

**park4night.com** (1)

- [park4night — 70783](https://park4night.com/es/place/70783)

**picuco.com** (1)

- [Picuco — parque-natural-de-las-fuentes-carrionas-y-fuente-cobre-monta](https://www.picuco.com/es-es/regions/parque-natural-de-las-fuentes-carrionas-y-fuente-cobre-monta/)

**play.google.com** (1)

- [Google Play — details?id=com.argeol.lasloras360](https://play.google.com/store/apps/details?id=com.argeol.lasloras360)

**pnoa.ign.es** (1)

- [Nubes de puntos](https://pnoa.ign.es/resources/archivos/pdf/Procesado_distribucion_nubes_puntos_proyecto_PNOA-LiDAR.pdf)

**publico.es** (1)

- [publico.es — nieve-obliga-cerrar-al-trafico.html](https://www.publico.es/sociedad/nieve-obliga-cerrar-al-trafico.html)

**puntadelasolas.es** (1)

- [Punta de las Olas 2026](https://puntadelasolas.es/2026/integral-de-fuentes-carrionas/)

**recmountain.com** (1)

- [recmountain — integral-de-fuentes-carrionas](https://recmountain.com/integral-de-fuentes-carrionas/)

**rednatura.jcyl.es** (1)

- [formulario — ES4140011.pdf](https://rednatura.jcyl.es/natura2000/LIC/Formularios%20oficiales/PDF%20LIC%20resumen/ES4140011.pdf)

**refuge.camp** (1)

- [refuge.camp — refugio-del-postil-de-sona](https://refuge.camp/es/refuge/refugio-del-postil-de-sona)

**revistaquercus.es** (1)

- [Quercus — DESCARGABLE_OSOS_EXT2.pdf](https://www.revistaquercus.es/adjuntos/7669/DESCARGABLE_OSOS_EXT2.pdf)

**rome2rio.com** (1)

- [rome2rio — Guardo](https://www.rome2rio.com/es/Autob%C3%BAs/Palencia/Guardo)

**senditur.com** (1)

- [senditur — como-comunicar-una-emergencia-cuando-hacemos-senderismo-o-montana](https://www.senditur.com/es/blog/como-comunicar-una-emergencia-cuando-hacemos-senderismo-o-montana/)

**servicio.mapa.gob.es** (1)

- [Guía MAPA — guia_cnromanicopalentinonipo_tcm34-636970.pdf](https://servicio.mapa.gob.es/ca/desarrollo-rural/temas/caminos-naturales/guia_cnromanicopalentinonipo_tcm34-636970.pdf)

**servicio.mapama.gob.es** (1)

- [Folleto — romanicopalentinoes_tcm30-146891.pdf](https://servicio.mapama.gob.es/es/desarrollo-rural/temas/caminos-naturales/romanicopalentinoes_tcm30-146891.pdf)

**sirdoc.ccyl.es** (1)

- [BOCCL — BOCCL-11-008044.pdf](https://sirdoc.ccyl.es/SIRDOC/PDF/PUBLOFI/BO/CCL/11L/BOCCL1100248/BOCCL-11-008044.pdf)

**somospalencia.es** (1)

- [somospalencia](https://www.somospalencia.es/tres-apasionantes-rutas-para-descubrir-la-montana-palentina/)

**sorianoticias.com** (1)

- [Soria Noticias](https://sorianoticias.com/noticia/2022-04-27-la-junta-regula-el-acceso-al-parque-natural-de-la-montana-palentina-para-proteger-dos-grupos-familiares-de-osos-89142)

**soyecoturista.com** (1)

- [soyecoturista](https://soyecoturista.com/en/actividad/equipamientos-de-uso-publico)

**subiendodosmilesenpalencia.blogspot.com** (1)

- [blog — los-chozos-de-la-montana-palentina.html](http://subiendodosmilesenpalencia.blogspot.com/p/los-chozos-de-la-montana-palentina.html)

**terabithia.es** (1)

- [Terabithia — renacer-en-la-montana-aumenta-el-impulso-del-oso-pardo-a-la-economia-local-en-2025](https://terabithia.es/renacer-en-la-montana-aumenta-el-impulso-del-oso-pardo-a-la-economia-local-en-2025/)

**terrafranca.es** (1)

- [Terrafranca invierno](https://www.terrafranca.es/planes-montana-palentina-invierno/)

**theobjective.com** (1)

- [The Objective](https://theobjective.com/actualidad/2023-02-27/rescate-cadaver-montanero-palencia/)

**trailruntemple.com** (1)

- [TrailRunTemple](https://trailruntemple.com/carreras/espana/castilla-y-leon/ultra-montana-palentina/inscripcion/)

**tribunapalencia.com** (1)

- [Tribuna Palencia](https://www.tribunapalencia.com/noticias/405288/rescatan-a-tres-montaneros-en-el-espiguete)

**tripadvisor.com** (1)

- [TripAdvisor — Attraction_Review-g2559173-d21206556-Reviews-Tejeda_de_Tosande-La_Estacion_Province_of_Sal](https://www.tripadvisor.com/Attraction_Review-g2559173-d21206556-Reviews-Tejeda_de_Tosande-La_Estacion_Province_of_Salamanca_Castile_and_Leon.html)

**turismobarruelo.com** (1)

- [turismobarruelo](https://turismobarruelo.com/cim/mina-visitable-en.php)

**tuscasasrurales.com** (1)

- [tuscasasrurales](https://www.tuscasasrurales.com/blog/rutas-senderismo-palencia/)

**velilladelriocarrion.es** (1)

- [Velilla — autobuses](https://velilladelriocarrion.es/municipio/autobuses/)

**verticalespana.com** (1)

- [fuente — trail-running](https://verticalespana.com/trail-running/)

**viajaporlibre.com** (1)

- [Viaja por libre](https://www.viajaporlibre.com/senderismo/fuentes-carrionas-travesia-por-pena-prieta)

**vozpopuli.com** (1)

- [Vozpópuli — muere-un-escalador-de-30-anos-tras-sufrir-una-indisposicion-mientras-ascendia-el-pico-cura](https://www.vozpopuli.com/sucesos/muere-un-escalador-de-30-anos-tras-sufrir-una-indisposicion-mientras-ascendia-el-pico-curavacas-en-palencia.html)

**web.guardiacivil.es** (1)

- [Guardia Civil montaña](https://web.guardiacivil.es/pdflink/es/fb46b663-4062-11eb-8bde-6d0b3e4c7555/Especialidad-Montana.pdf)

**whichmuseum.com** (1)

- [whichmuseum — opening-hours](https://whichmuseum.com/museum/centro-de-interpretacion-de-la-mineria-barruelo-de-santullan-34726/opening-hours)

**wiki.openstreetmap.org** (1)

- [OSM wiki senderismo ES](https://wiki.openstreetmap.org/wiki/ES:Espa%C3%B1a/Senderismo)

**wikipedia.org** (1)

- [Wikipedia — San_Glorio](https://Www.Wikipedia.org/wiki/San_Glorio)

**wikitrekk.com** (1)

- [wikitrekk — chozo-de-la-majada-de-fuentes-carrionas](https://wikitrekk.com/palencia/chozo-de-la-majada-de-fuentes-carrionas)

### Fuentes añadidas en la v2 (21-11-2026)

URLs nuevas citadas en la v2 (cuerpo del documento y notas de origen), agrupadas por dominio. Incluye la cuenta oficial de Wikiloc de la Fundación, citada en §1.1 sin enlace. Mismos criterios de uso que arriba: los enlaces `maps.app.goo.gl` están sin resolver.

**terranostrum.es** (110)

- [ruta-roja-monumento-natural-de-las-tuerces.gpx](https://www.terranostrum.es/images/Tracks/TU/ruta-roja-monumento-natural-de-las-tuerces.gpx)
- [1](https://www.terranostrum.es/senderismo/palencia/montana-palentina/1)
- [ascension-al-pico-murcia](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ascension-al-pico-murcia)
- [ascension-pena-fraile](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ascension-pena-fraile)
- [ascension-pico-espiguete-por-la-cara-norte](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ascension-pico-espiguete-por-la-cara-norte)
- [ascension-pico-espiguete-por-la-cara-sur](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ascension-pico-espiguete-por-la-cara-sur)
- [bocaron-de-casavegas](https://www.terranostrum.es/senderismo/palencia/montana-palentina/bocaron-de-casavegas)
- [ruta-golobar-valdecebollas-sel-de-la-fuente](https://www.terranostrum.es/senderismo/palencia/montana-palentina/branosera/ruta-golobar-valdecebollas-sel-de-la-fuente)
- [valdecebollas-y-el-cueto](https://www.terranostrum.es/senderismo/palencia/montana-palentina/branosera/valdecebollas-y-el-cueto)
- [calzada-de-los-blendios-etapa-1](https://www.terranostrum.es/senderismo/palencia/montana-palentina/calzada-de-los-blendios-etapa-1)
- [calzada-de-los-blendios-etapa-2](https://www.terranostrum.es/senderismo/palencia/montana-palentina/calzada-de-los-blendios-etapa-2)
- [camino-lebaniego-castellano-etapa-6-alar-del-rey-perazancas-de-ojeda](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-lebaniego-castellano-etapa-6-alar-del-rey-perazancas-de-ojeda)
- [camino-lebaniego-castellano-etapa-7-perazancas-de-ojeda-cervera-de-pisuerga](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-lebaniego-castellano-etapa-7-perazancas-de-ojeda-cervera-de-pisuerga)
- [camino-lebaniego-castellano-etapa-8-cervera-de-pisuerga-san-salvador-de-cantamuda](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-lebaniego-castellano-etapa-8-cervera-de-pisuerga-san-salvador-de-cantamuda)
- [camino-lebaniego-castellano-etapa-9-san-salvador-de-cantamuda-camasobres](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-lebaniego-castellano-etapa-9-san-salvador-de-cantamuda-camasobres)
- [camino-lebaniego-castellano-etapas-10-11-camasobres-monasterio-santo-toribio](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-lebaniego-castellano-etapas-10-11-camasobres-monasterio-santo-toribio)
- [camino-olvidado-en-leon-etapa-8](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-olvidado-en-leon-etapa-8)
- [de-camporredondo-de-alba-a-valsurbio](https://www.terranostrum.es/senderismo/palencia/montana-palentina/de-camporredondo-de-alba-a-valsurbio)
- [el-arroyo-de-manzobres-y-sima-del-anillo](https://www.terranostrum.es/senderismo/palencia/montana-palentina/el-arroyo-de-manzobres-y-sima-del-anillo)
- [el-pinar-de-pena-mayor](https://www.terranostrum.es/senderismo/palencia/montana-palentina/el-pinar-de-pena-mayor)
- [el-pozo-de-las-lomas](https://www.terranostrum.es/senderismo/palencia/montana-palentina/el-pozo-de-las-lomas)
- [el-roblon-de-estalaya](https://www.terranostrum.es/senderismo/palencia/montana-palentina/el-roblon-de-estalaya)
- [el-valle-de-pineda-y-el-pozo-curavacas](https://www.terranostrum.es/senderismo/palencia/montana-palentina/el-valle-de-pineda-y-el-pozo-curavacas)
- [gr-1-palencia-etapa-1-cantabria-branosera](https://www.terranostrum.es/senderismo/palencia/montana-palentina/gr-1-palencia-etapa-1-cantabria-branosera)
- [integral-espacio-natural-de-covalagua](https://www.terranostrum.es/senderismo/palencia/montana-palentina/integral-espacio-natural-de-covalagua)
- [la-escalera-del-tiempo](https://www.terranostrum.es/senderismo/palencia/montana-palentina/la-escalera-del-tiempo)
- [la-fuente-del-cobre](https://www.terranostrum.es/senderismo/palencia/montana-palentina/la-fuente-del-cobre)
- [la-senda-del-bosque-fosil](https://www.terranostrum.es/senderismo/palencia/montana-palentina/la-senda-del-bosque-fosil)
- [la-senda-pena-del-oso](https://www.terranostrum.es/senderismo/palencia/montana-palentina/la-senda-pena-del-oso)
- [la-tejeda-de-tosande](https://www.terranostrum.es/senderismo/palencia/montana-palentina/la-tejeda-de-tosande)
- [las-tuerces-ruta-amarilla](https://www.terranostrum.es/senderismo/palencia/montana-palentina/las-tuerces-ruta-amarilla)
- [las-tuerces-ruta-azul](https://www.terranostrum.es/senderismo/palencia/montana-palentina/las-tuerces-ruta-azul)
- [las-tuerces-ruta-rosa](https://www.terranostrum.es/senderismo/palencia/montana-palentina/las-tuerces-ruta-rosa)
- [las-tuerces-ruta-verde](https://www.terranostrum.es/senderismo/palencia/montana-palentina/las-tuerces-ruta-verde)
- [monte-ciruelo-desde-la-muneca](https://www.terranostrum.es/senderismo/palencia/montana-palentina/monte-ciruelo-desde-la-muneca)
- [pena-tremaya](https://www.terranostrum.es/senderismo/palencia/montana-palentina/pena-tremaya)
- [por-el-despoblado-de-valsurbio](https://www.terranostrum.es/senderismo/palencia/montana-palentina/por-el-despoblado-de-valsurbio)
- [sendero-cascada-de-covalagua](https://www.terranostrum.es/senderismo/palencia/montana-palentina/revilla-de-pomar/sendero-cascada-de-covalagua)
- [ruta-btt](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt)
- [ruta-btt-alto-valle-de-muda](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-alto-valle-de-muda)
- [ruta-btt-barruelo-de-santullan-cervera-de-pisuerga](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-barruelo-de-santullan-cervera-de-pisuerga)
- [ruta-btt-cervera-de-pisuerga-triollo](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-cervera-de-pisuerga-triollo)
- [ruta-btt-del-carbon](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-del-carbon)
- [ruta-btt-el-ferrocarril-de-la-robla](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-el-ferrocarril-de-la-robla)
- [ruta-btt-gotico-y-romanico-en-la-pena](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-gotico-y-romanico-en-la-pena)
- [ruta-btt-guardo-puente-almuhey](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-guardo-puente-almuhey)
- [ruta-btt-la-despensa-del-abad](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-la-despensa-del-abad)
- [ruta-btt-la-horca-de-la-ojeda](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-la-horca-de-la-ojeda)
- [ruta-btt-las-ermitas-del-embalse-de-aguilar](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-las-ermitas-del-embalse-de-aguilar)
- [ruta-btt-las-fuentes-tamaricas](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-las-fuentes-tamaricas)
- [ruta-btt-las-ranas-del-rio-valdavia](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-las-ranas-del-rio-valdavia)
- [ruta-btt-los-valles-de-burejo](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-los-valles-de-burejo)
- [ruta-btt-monumentos-karsticos](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-monumentos-karsticos)
- [ruta-btt-pedaleando-por-el-romanico-palentino](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-pedaleando-por-el-romanico-palentino)
- [ruta-btt-por-la-vega-del-carrion](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-por-la-vega-del-carrion)
- [ruta-btt-por-las-ventas-de-la-pernia](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-por-las-ventas-de-la-pernia)
- [ruta-btt-por-valle-estrecho](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-por-valle-estrecho)
- [ruta-btt-romanico-en-tierras-de-santullan](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-romanico-en-tierras-de-santullan)
- [ruta-btt-senda-del-pisuerga](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-senda-del-pisuerga)
- [ruta-btt-tras-las-huellas-de-jano](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-tras-las-huellas-de-jano)
- [ruta-btt-triollo-guardo](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-triollo-guardo)
- [ruta-btt-vuelta-al-monte-bernorio](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-vuelta-al-monte-bernorio)
- [ruta-circular-alrededores-de-guardo](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-circular-alrededores-de-guardo)
- [ruta-de-las-merendillas-guardo](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-de-las-merendillas-guardo)
- [ruta-del-carbon-de-cok-etapa-1](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-del-carbon-de-cok-etapa-1)
- [ruta-del-carbon-de-cok-etapa-2](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-del-carbon-de-cok-etapa-2)
- [ruta-del-carbon-de-cok-etapa-3](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-del-carbon-de-cok-etapa-3)
- [ruta-del-carbon-de-cok-variante-2](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-del-carbon-de-cok-variante-2)
- [ruta-golobar-valdecebollas-sel-de-la-fuente](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-golobar-valdecebollas-sel-de-la-fuente)
- [ruta-lores-pico-lezna](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-lores-pico-lezna)
- [la-fuente-del-cobre](https://www.terranostrum.es/senderismo/palencia/montana-palentina/santa-maria-de-redondo/la-fuente-del-cobre)
- [senda-de-la-cascada-de-manzobre](https://www.terranostrum.es/senderismo/palencia/montana-palentina/senda-de-la-cascada-de-manzobre)
- [senda-de-la-pedrosa](https://www.terranostrum.es/senderismo/palencia/montana-palentina/senda-de-la-pedrosa)
- [senda-de-las-doncellas-del-hoyal](https://www.terranostrum.es/senderismo/palencia/montana-palentina/senda-de-las-doncellas-del-hoyal)
- [senda-de-los-pescadores-en-la-ribera-del-rio-carrion](https://www.terranostrum.es/senderismo/palencia/montana-palentina/senda-de-los-pescadores-en-la-ribera-del-rio-carrion)
- [senda-del-escultor-ursi](https://www.terranostrum.es/senderismo/palencia/montana-palentina/senda-del-escultor-ursi)
- [senda-del-pinar-de-velilla](https://www.terranostrum.es/senderismo/palencia/montana-palentina/senda-del-pinar-de-velilla)
- [senda-el-gigante-del-valle-estrecho](https://www.terranostrum.es/senderismo/palencia/montana-palentina/senda-el-gigante-del-valle-estrecho)
- [senda-la-venganza-del-conde](https://www.terranostrum.es/senderismo/palencia/montana-palentina/senda-la-venganza-del-conde)
- [sendero-al-valle-de-las-brujas](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-al-valle-de-las-brujas)
- [sendero-campos-de-menaza](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-campos-de-menaza)
- [sendero-canduela-villanueva-de-henares](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-canduela-villanueva-de-henares)
- [sendero-cardano-de-abajo-a-la-cruz-armada](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cardano-de-abajo-a-la-cruz-armada)
- [sendero-cascada-de-covalagua](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cascada-de-covalagua)
- [sendero-cervera-de-pisuerga-pico-de-las-cruces](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cervera-de-pisuerga-pico-de-las-cruces)
- [sendero-cillamayor-montes-de-matabuena](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cillamayor-montes-de-matabuena)
- [sendero-collado-del-pinar-fuentes-carrionas](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-collado-del-pinar-fuentes-carrionas)
- [sendero-cueva-de-los-franceses-pozo-de-los-lobos](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cueva-de-los-franceses-pozo-de-los-lobos)
- [sendero-cueva-dorada-fuentes-carrionas](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cueva-dorada-fuentes-carrionas)
- [sendero-de-los-lobos-al-balcon-de-judas](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-de-los-lobos-al-balcon-de-judas)
- [sendero-de-muda-a-monasterio](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-de-muda-a-monasterio)
- [sendero-de-ujapero-y-cocoto](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-de-ujapero-y-cocoto)
- [sendero-de-valdelobos-prc-p-14](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-de-valdelobos-prc-p-14)
- [sendero-del-ribero-pintado](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-del-ribero-pintado)
- [sendero-el-sabinar-de-pena-lampa](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-el-sabinar-de-pena-lampa)
- [sendero-la-mata-del-fraile-y-el-calero-de-branosera](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-la-mata-del-fraile-y-el-calero-de-branosera)
- [sendero-las-minas-de-san-cebrian-de-muda](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-las-minas-de-san-cebrian-de-muda)
- [sendero-ligueerzana-a-la-vega-de-quintanaluengos](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-ligueerzana-a-la-vega-de-quintanaluengos)
- [sendero-monte-corcos-y-ermita-del-cristo](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-monte-corcos-y-ermita-del-cristo)
- [sendero-polentinos-abadia-de-lebanza](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-polentinos-abadia-de-lebanza)
- [sendero-roblon-del-monasterio-prc-p-12](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-roblon-del-monasterio-prc-p-12)
- [sendero-salcedillo-rojadillo-y-branosera](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-salcedillo-rojadillo-y-branosera)
- [sendero-san-juan-de-redondo-corrala-de-bismo](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-san-juan-de-redondo-corrala-de-bismo)
- [sendero-triollo-hornamiel](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-triollo-hornamiel)
- [sendero-valberzoso-puente-rojadillo](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-valberzoso-puente-rojadillo)
- [sendero-valles-san-quirce-y-corcos](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-valles-san-quirce-y-corcos)
- [sendero-vidrieros-pie-del-curavacas](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-vidrieros-pie-del-curavacas)
- [subida-al-monte-coriscao-fuentes-carrionas](https://www.terranostrum.es/senderismo/palencia/montana-palentina/subida-al-monte-coriscao-fuentes-carrionas)
- [valberzoso-collado-de-somahoz](https://www.terranostrum.es/senderismo/palencia/montana-palentina/valberzoso-collado-de-somahoz)
- [valdecebollas-y-el-cueto](https://www.terranostrum.es/senderismo/palencia/montana-palentina/valdecebollas-y-el-cueto)

**palenciaturismo.es** (38)

- [zona-decargas](https://palenciaturismo.es/guia-practica/zona-decargas)
- [etapa-1-gr1-salcedillo-branosera](https://palenciaturismo.es/que-hacer/etapas/etapa-1-gr1-salcedillo-branosera)
- [etapa-2-gr1-branosera-estalaya](https://palenciaturismo.es/que-hacer/etapas/etapa-2-gr1-branosera-estalaya)
- [etapa-3-gr1-estalaya-cervera-pisuerga](https://palenciaturismo.es/que-hacer/etapas/etapa-3-gr1-estalaya-cervera-pisuerga)
- [etapa-4-gr1-cervera-pisuerga-triollo](https://palenciaturismo.es/que-hacer/etapas/etapa-4-gr1-cervera-pisuerga-triollo)
- [etapa-5-gr1-triollo-camporredondo-alba](https://palenciaturismo.es/que-hacer/etapas/etapa-5-gr1-triollo-camporredondo-alba)
- [etapa-6-gr1-camporredondo-alba-alto-cruz-armada](https://palenciaturismo.es/que-hacer/etapas/etapa-6-gr1-camporredondo-alba-alto-cruz-armada)
- [rutas-naturales](https://palenciaturismo.es/que-hacer/rutas-naturales)
- [bosque-pedrosa](https://palenciaturismo.es/que-hacer/rutas/bosque-pedrosa)
- [cascada-mazobre](https://palenciaturismo.es/que-hacer/rutas/cascada-mazobre)
- [gr1](https://palenciaturismo.es/que-hacer/rutas/gr1)
- [monumento-natural-tuerces](https://palenciaturismo.es/que-hacer/rutas/monumento-natural-tuerces)
- [pinar-velilla](https://palenciaturismo.es/que-hacer/rutas/pinar-velilla)
- [quejigar-hermedes](https://palenciaturismo.es/que-hacer/rutas/quejigar-hermedes)
- [roblon-estalaya](https://palenciaturismo.es/que-hacer/rutas/roblon-estalaya)
- [ruta-pantanos](https://palenciaturismo.es/que-hacer/rutas/ruta-pantanos)
- [ruta-ribero-pintado](https://palenciaturismo.es/que-hacer/rutas/ruta-ribero-pintado)
- [senda-bosque-fosil](https://palenciaturismo.es/que-hacer/rutas/senda-bosque-fosil)
- [senda-doncellas-hoyal](https://palenciaturismo.es/que-hacer/rutas/senda-doncellas-hoyal)
- [senda-escultor-ursi](https://palenciaturismo.es/que-hacer/rutas/senda-escultor-ursi)
- [senda-fuente-cobre](https://palenciaturismo.es/que-hacer/rutas/senda-fuente-cobre)
- [senda-gigante-valle-estrecho](https://palenciaturismo.es/que-hacer/rutas/senda-gigante-valle-estrecho)
- [senda-laguna-lomas](https://palenciaturismo.es/que-hacer/rutas/senda-laguna-lomas)
- [senda-oso](https://palenciaturismo.es/que-hacer/rutas/senda-oso)
- [senda-pescadores](https://palenciaturismo.es/que-hacer/rutas/senda-pescadores)
- [tejeda-tosande](https://palenciaturismo.es/que-hacer/rutas/tejeda-tosande)
- [sendas_de_barruelo.pdf](https://palenciaturismo.es/system/files/2019-08/sendas_de_barruelo.pdf)
- [santa-maria-de-redondo-ribero-pintado.gpx](https://palenciaturismo.es/system/files/2020-06/santa-maria-de-redondo-ribero-pintado.gpx)
- [senda-de-las-doncellas-del-hoyal_0.gpx](https://palenciaturismo.es/system/files/2022-10/senda-de-las-doncellas-del-hoyal_0.gpx)
- [LIBRO MONTAÑA PALENTINA (versión español) (1).pdf](https://palenciaturismo.es/system/files/2026-06/LIBRO%20MONTA%C3%91A%20PALENTINA%20%28versi%C3%B3n%20espa%C3%B1ol%29%20%281%29.pdf)
- [LIBRO MONTAÑA PALENTINA (versión Inglés). (1).pdf](https://palenciaturismo.es/system/files/2026-06/LIBRO%20MONTAN%CC%83A%20PALENTINA%20%28versio%CC%81n%20Ingle%CC%81s%29.%20%281%29.pdf)
- [MAPA MONTAÑA PALENTINA (formato interactivo digital) INTERNET_0.pdf](https://palenciaturismo.es/system/files/2026-06/MAPA%20MONTA%C3%91A%20PALENTINA%20%28formato%20interactivo%20digital%29%20INTERNET_0.pdf)
- [NP_GUIA MONTAÑA PALENTINA.pdf](https://palenciaturismo.es/system/files/2026-06/NP_GUIA%20MONTA%C3%91A%20PALENTINA.pdf)
- [casa-parque-natural-montana-palentina](https://palenciaturismo.es/visitar/lugares-interes/casa-parque-natural-montana-palentina)
- [cueva-franceses](https://palenciaturismo.es/visitar/lugares-interes/cueva-franceses)
- [guia-exposicion-fotografica-montana-palentina](https://palenciaturismo.es/visitar/lugares-interes/guia-exposicion-fotografica-montana-palentina)
- [mirador-piedrasluengas](https://palenciaturismo.es/visitar/lugares-interes/mirador-piedrasluengas)
- [reserva-bisonte-europeo-bison-bonasus](https://palenciaturismo.es/visitar/lugares-interes/reserva-bisonte-europeo-bison-bonasus)

**maps.app.goo.gl** (38)

- [13HADbYCigeJUpmZ9](https://maps.app.goo.gl/13HADbYCigeJUpmZ9)
- [1M1nYGpkhjaPMVxN9](https://maps.app.goo.gl/1M1nYGpkhjaPMVxN9)
- [4EABgjsSRrYvQrgG8](https://maps.app.goo.gl/4EABgjsSRrYvQrgG8)
- [4WtK824GkNSZZFsk7](https://maps.app.goo.gl/4WtK824GkNSZZFsk7)
- [6uQNtXQY9Fsa42eB7](https://maps.app.goo.gl/6uQNtXQY9Fsa42eB7)
- [CPchniJD2Tz63XEY8](https://maps.app.goo.gl/CPchniJD2Tz63XEY8)
- [EKea3EogTwnxed2S8](https://maps.app.goo.gl/EKea3EogTwnxed2S8)
- [ETiNcwHA8aosnTjW8](https://maps.app.goo.gl/ETiNcwHA8aosnTjW8)
- [Jh15UqWATKiGG3BJA](https://maps.app.goo.gl/Jh15UqWATKiGG3BJA)
- [LtrPM4DJdt3akFqk8](https://maps.app.goo.gl/LtrPM4DJdt3akFqk8)
- [M5XKwKsiTAR4PiAb6](https://maps.app.goo.gl/M5XKwKsiTAR4PiAb6)
- [PBSgibjLBJw7a5iN7](https://maps.app.goo.gl/PBSgibjLBJw7a5iN7)
- [V7haWCTSddZ3j82G6](https://maps.app.goo.gl/V7haWCTSddZ3j82G6)
- [XqELXxqV36jCAJZVA](https://maps.app.goo.gl/XqELXxqV36jCAJZVA)
- [asRJidBKnMbUHj52A](https://maps.app.goo.gl/asRJidBKnMbUHj52A)
- [dCYpX5ez1bYbtPn68](https://maps.app.goo.gl/dCYpX5ez1bYbtPn68)
- [gRiKc3zSynSsMuKb7](https://maps.app.goo.gl/gRiKc3zSynSsMuKb7)
- [i5oZX4zaqwWKtPDG7](https://maps.app.goo.gl/i5oZX4zaqwWKtPDG7)
- [iMHGYyW82NDkgzse6](https://maps.app.goo.gl/iMHGYyW82NDkgzse6)
- [inUWEdWE8FX9fAgz6](https://maps.app.goo.gl/inUWEdWE8FX9fAgz6)
- [j5dX5HUN8ggdU7Ai6](https://maps.app.goo.gl/j5dX5HUN8ggdU7Ai6)
- [jLGCSQrUXWRXX2kBA](https://maps.app.goo.gl/jLGCSQrUXWRXX2kBA)
- [jqjsPQzMppWuyMkEA](https://maps.app.goo.gl/jqjsPQzMppWuyMkEA)
- [kMqwgAydBDUzQ7Ln8](https://maps.app.goo.gl/kMqwgAydBDUzQ7Ln8)
- [mX1YHaiz24EcSM5r9](https://maps.app.goo.gl/mX1YHaiz24EcSM5r9)
- [pEqqjKRNFMS6x9377](https://maps.app.goo.gl/pEqqjKRNFMS6x9377)
- [pRXNLxnJhGHh6ogE8](https://maps.app.goo.gl/pRXNLxnJhGHh6ogE8)
- [qcCoA4SX7aciE7SB6](https://maps.app.goo.gl/qcCoA4SX7aciE7SB6)
- [rRWcfG8eonYysJ7z9](https://maps.app.goo.gl/rRWcfG8eonYysJ7z9)
- [s5jh7m4ddZ7Ls1aF9](https://maps.app.goo.gl/s5jh7m4ddZ7Ls1aF9)
- [sXsgRGV4ABjvKBbY7](https://maps.app.goo.gl/sXsgRGV4ABjvKBbY7)
- [sZtojx7TTpU49Xjv8](https://maps.app.goo.gl/sZtojx7TTpU49Xjv8)
- [t7cEaD7vHaqVUeeJA](https://maps.app.goo.gl/t7cEaD7vHaqVUeeJA)
- [tZayfZUGR4LJL81y6](https://maps.app.goo.gl/tZayfZUGR4LJL81y6)
- [vFTTDGNkbVJ3gVia6](https://maps.app.goo.gl/vFTTDGNkbVJ3gVia6)
- [wqoQZiVwSmG55cHM7](https://maps.app.goo.gl/wqoQZiVwSmG55cHM7)
- [yS2sZYAYY4fsyc8w7](https://maps.app.goo.gl/yS2sZYAYY4fsyc8w7)
- [z2Qpdy5RRbV3pWZz9](https://maps.app.goo.gl/z2Qpdy5RRbV3pWZz9)

**es.wikipedia.org** (19)

- [Covalagua](https://es.wikipedia.org/wiki/Covalagua)
- [Curavacas](https://es.wikipedia.org/wiki/Curavacas)
- [El_Golobar](https://es.wikipedia.org/wiki/El_Golobar)
- [Espigüete](https://es.wikipedia.org/wiki/Espig%C3%BCete)
- [Fuente_Cobre](https://es.wikipedia.org/wiki/Fuente_Cobre)
- [Fuentes_Carrionas](https://es.wikipedia.org/wiki/Fuentes_Carrionas)
- [Geoparque_Las_Loras](https://es.wikipedia.org/wiki/Geoparque_Las_Loras)
- [Las_Tuerces](https://es.wikipedia.org/wiki/Las_Tuerces)
- [Monte_Bernorio](https://es.wikipedia.org/wiki/Monte_Bernorio)
- [Peña_Labra](https://es.wikipedia.org/wiki/Pe%C3%B1a_Labra)
- [Peña_Prieta](https://es.wikipedia.org/wiki/Pe%C3%B1a_Prieta)
- [Peña_Redonda](https://es.wikipedia.org/wiki/Pe%C3%B1a_Redonda)
- [Pico_Lezna](https://es.wikipedia.org/wiki/Pico_Lezna)
- [Pico_Murcia](https://es.wikipedia.org/wiki/Pico_Murcia)
- [Pico_Tres_Mares](https://es.wikipedia.org/wiki/Pico_Tres_Mares)
- [Sierra_de_Híjar](https://es.wikipedia.org/wiki/Sierra_de_H%C3%ADjar)
- [Sierra_del_Brezo](https://es.wikipedia.org/wiki/Sierra_del_Brezo)
- [Tejeda_de_Tosande](https://es.wikipedia.org/wiki/Tejeda_de_Tosande)
- [Valdecebollas](https://es.wikipedia.org/wiki/Valdecebollas)

**komoot.com** (17)

- [rutas-de-senderismo-en-palencia](https://www.komoot.com/es-es/guide/50235/rutas-de-senderismo-en-palencia)
- [hiking-around-triollo](https://www.komoot.com/guide/1659696/hiking-around-triollo)
- [3519921](https://www.komoot.com/guide/3519921)
- [3798621](https://www.komoot.com/guide/3798621)
- [415492](https://www.komoot.com/guide/415492)
- [415494](https://www.komoot.com/guide/415494)
- [1651543](https://www.komoot.com/highlight/1651543)
- [3306171](https://www.komoot.com/highlight/3306171)
- [3394566](https://www.komoot.com/highlight/3394566)
- [3487275](https://www.komoot.com/highlight/3487275)
- [3943784](https://www.komoot.com/highlight/3943784)
- [4444414](https://www.komoot.com/highlight/4444414)
- [4444419](https://www.komoot.com/highlight/4444419)
- [4976372](https://www.komoot.com/highlight/4976372)
- [5837344](https://www.komoot.com/highlight/5837344)
- [6659058](https://www.komoot.com/highlight/6659058)
- [curavacas-desde-vidrieros-parque-natural-montana-palentina](https://www.komoot.com/smarttour/e1068189616/curavacas-desde-vidrieros-parque-natural-montana-palentina)

**refugioslibres.com** (13)

- [cabana-de-mollorente](https://www.refugioslibres.com/refugios/cabana-de-mollorente)
- [cabana-de-naranco](https://www.refugioslibres.com/refugios/cabana-de-naranco)
- [cabana-linarucas](https://www.refugioslibres.com/refugios/cabana-linarucas)
- [cabana-machorril](https://www.refugioslibres.com/refugios/cabana-machorril)
- [refugio-brana-de-los-tejos](https://www.refugioslibres.com/refugios/refugio-brana-de-los-tejos)
- [refugio-de-cristo-sierra](https://www.refugioslibres.com/refugios/refugio-de-cristo-sierra)
- [refugio-de-pescadores-campoluengo](https://www.refugioslibres.com/refugios/refugio-de-pescadores-campoluengo)
- [refugio-de-santa-marina](https://www.refugioslibres.com/refugios/refugio-de-santa-marina)
- [refugio-del-muron](https://www.refugioslibres.com/refugios/refugio-del-muron)
- [refugio-del-pico-del-calar](https://www.refugioslibres.com/refugios/refugio-del-pico-del-calar)
- [refugio-majada-de-los-cantos](https://www.refugioslibres.com/refugios/refugio-majada-de-los-cantos)
- [refugio-mazobre](https://www.refugioslibres.com/refugios/refugio-mazobre)
- [refugio-rozalacalle](https://www.refugioslibres.com/refugios/refugio-rozalacalle)

**elmirondesoria.es** (2)

- [amp](https://elmirondesoria.es/soria/sucesos/dos-montaneros-heridos-rescatados-por-proteccion-civil/amp)
- [amp](https://elmirondesoria.es/soria/sucesos/evacuados-dos-escaladores-heridos-en-curavacas/amp)

**es.wikiloc.com** (2)

- [manantial-las-lomas](https://es.wikiloc.com/waypoints/fAgab3/manantial-las-lomas)
- [user.do](https://es.wikiloc.com/wikiloc/user.do?id=4448395)

**lapedrerapindia.com** (1)

- [ascensiones](https://lapedrerapindia.com/rutas-montana-palentina/ascensiones/)

**montanapegaso.es** (2)

- [Espiguete2026_memo.pdf](https://montanapegaso.es/carteles/2026/Espiguete2026_memo.pdf)
- [Espiguete2026_info.pdf](https://www.montanapegaso.es/carteles/2026/Espiguete2026_info.pdf)

**turismocastillayleon.com** (2)

- [paisaje-protegido-monumento-natural-tuerces](https://www.turismocastillayleon.com/douro/es/espacios-naturales/paisaje-protegido-monumento-natural-tuerces)
- [pathway-fuente-cobre-birth-pisuerga-river-672e](https://www.turismocastillayleon.com/en/countryside-nature/nature-routes/pathway-fuente-cobre-birth-pisuerga-river-672e)

**viajaporlibre.com** (2)

- [ruta-curavacas-vidrieros](https://www.viajaporlibre.com/senderismo/ruta-curavacas-vidrieros)
- [rutas-montana-palentina](https://www.viajaporlibre.com/senderismo/rutas-montana-palentina)

**atrochando.com** (1)

- [montana-palentina](https://atrochando.com/rutas-de-senderismo-en-montana/montana-palentina/)

**blog.komoot.nl** (1)

- [pena-redonda-ascent-trail](https://blog.komoot.nl/smarttour/e1068363176/pena-redonda-ascent-trail)

**diariodevalderrueda.es** (1)

- [grandes-cumbres-descubrir-montana-palentina](https://www.diariodevalderrueda.es/texto-diario/mostrar/5259975/grandes-cumbres-descubrir-montana-palentina)

**elcongresista.mx** (1)

- [rescate-montanera-herida-espiguete](https://elcongresista.mx/rescate-montanera-herida-espiguete)

**elcorrelimos.com** (1)

- [montana-palentina](https://elcorrelimos.com/montana-palentina/)

**escapadarural.com** (1)

- [rutas-por-la-montana-palentina](https://www.escapadarural.com/blog/rutas-por-la-montana-palentina)

**foro.tiempo.com** (1)

- [nevadon-en-la-montana-palentina-febrero-2015-t145640.60.html](https://foro.tiempo.com/nevadon-en-la-montana-palentina-febrero-2015-t145640.60.html)

**gulliver.it** (1)

- [gulliver.it](https://www.gulliver.it/?p=351935)

**mountainguidespain.com** (1)

- [trilogia-de-la-montana-palentina](https://www.mountainguidespain.com/trilogia-de-la-montana-palentina/)

**peninsulablog.com** (1)

- [pena-prieta-2-539-m-montana-palentina](https://peninsulablog.com/2020/07/31/pena-prieta-2-539-m-montana-palentina/)

**rutinasvarias.com** (1)

- [montana-palentina](https://www.rutinasvarias.com/category/montana-palentina/)

**sendasycumbres.com** (1)

- [montana-palentina](https://sendasycumbres.com/montana-palentina/)

**summitpost.org** (1)

- [153553](https://www.summitpost.org/curavacas/153553)

**uvadoc.uva.es** (1)

- [Nieve-aludes-Montaña-Cantábrica.pdf.pdf](https://uvadoc.uva.es/bitstream/handle/10324/40660/Nieve-aludes-Monta%c3%b1a-Cant%c3%a1brica.pdf.pdf?sequence=1)

---

## Pendientes / lo que falta

Esta es la lista de huecos concretos que deja la investigación (actualizada en la v2, 21-11-2026). Cada punto dice qué falta, por qué y cómo cerrarlo. Se han retirado los resueltos: Senda de La Pedrosa (ficha, inicio y tipo), cifras oficiales del GR-1 por etapa y su E6, etapas del Camino Natural del Románico, Camino Olvidado E5 y Lebaniego Castellano, Quejigar de Hérmedes (está en el Cerrato, fuera del ámbito), tipo de la Senda de Fuente Cobre (circular), cifras de Las Tuerces Amarilla y Azul, coordenada del Pozo de las Lomas, estado de los refugios de Mazobre, Santa Marina y Golobar, y la mayoría de los trailheads sin coordenadas.

**Bloqueos de acceso**

1. **Extracción OSM bloqueada por la red.** En la v2, tanto `download.geofabrik.de` (extracto regional) como `overpass-api.de` devolvieron *connection reset* desde el entorno. La consulta `overpass_query_poi.overpassql` está lista en la carpeta de notas. **Cómo cerrarlo:** que el usuario suba `castilla-y-leon-latest.osm.pbf` (Geofabrik) para filtrarlo con osmium, o que ejecute el `.overpassql` en local. Con ella se resuelven refugios, fuentes, parkings, miradores, helipuertos y paradas.
2. **lapedrerapindia.com inaccesible** (*connection reset* en HTTPS, con y sin `www`, tres intentos espaciados). Consecuencias: **las 24 rutas de la Diputación sin versión gratuita (02, 04, 05, 07, 08, 10, 11, 13, 15, 17, 19–22, 25, 27, 28, 30, 32–35, 38 y 39) siguen solo con los datos del anexo** (sin inicio, cumbres ni waypoints); las 16 URL de los QR de 2016 siguen **sin comprobar**; la sección BTT de la editorial no se revisó. Cómo cerrarlo: revisión manual en navegador o contacto con la editorial, titular del ©.
3. **Wikiloc no se ha leído** (protección anti-bot; **no se intentó saltar**). Todas las cifras [W], recuentos de descargas, valoraciones y comentarios son resúmenes de buscador sin verificar, y no se sabe qué tracks publica la cuenta oficial de la Fundación.
4. **SummitPost (Cloudflare, 403) y Guía Repsol (Akamai, 418) ilegibles.** Lo citado de ellos (fuente en Pino Llano, ruta con perro al Espigüete) procede solo del buscador ⚠️. Habría que revisarlos a mano.
5. **Enlaces `maps.app.goo.gl` sin resolver.** Los 38 enlaces del mapa interactivo del libro 2026 (§6) no se pudieron convertir en coordenadas (host no permitido). Basta con abrirlos en un navegador. Dos de ellos (n.º 8 y 31) quedaron sin emparejar con su rótulo.
6. **datosabiertos.jcyl.es** y **fdmescyl.com** sin abrir: no se sabe si hay dataset de senderos ni se pudo confirmar la homologación de los **PRC-P 12 (Roblón del Monasterio)** y **PRC-P 14 (Valdelobos)**.
7. **geoparquelasloras.es sin www** bloqueado: sigue sin localizarse la lista de las "7 rutas señalizadas" del Geoparque.
8. **No se descargó ningún GPX de Mendikat** (permiso denegado): sus salidas son cajas envolventes de ±200–500 m (por ejemplo, la de Santa María de Redondo parece desplazada).

**Datos de rutas**

9. **Ruta 31 (Tres Mares)**, **06-WP7** y **36-WP25**: coordenadas erróneas en el PDF; en el JSON llevan las de Ciudad del Brezo y **hay que excluirlas** (25 de 318).
10. **OCR de folletos escaneados** sin capa de texto: Fuente Cobre, Tosande, Ursi, Oso, el folleto de Aguilar del Geoparque y `sendas_de_barruelo.pdf` de palenciaturismo. No hay OCR en el entorno.
11. **Sendero de Ruesga:** estado de obra y apertura a finales de 2026 desconocidos. **Senda del Oso:** no se sabe si siguen los cierres por obras del 4-6-2026.
12. **No se leyeron** el libro-guía y el folleto del GR-1 de la Junta, el programa "Descubriendo el Geoparque 2026" ni el protocolo de osos de 2026.
13. **Camino Natural del Románico:** contrastar las etapas de Terranostrum (que lo llama "Ruta del Carbón de Cok") con el GPX oficial del MAPA y revisar su licencia. **Camino Natural Lebaniego de Pineda:** sin ninguna fuente.
14. Rutas aún sin fuente: Cascadas de Lebanza, Cascada de Atría, Senda del Agua, Ruta de los Molinos, Pozo Oscuro (solo mencionado), Senda de los Rojos (solo foto y mención), Monte Bernorio a pie con ficha oficial (solo hay una vuelta BTT), y Peña Redonda y el Hayedo de Monte Ahedo en Terranostrum.
15. **Desniveles inconsistentes:** varias fichas de Terranostrum dan bastante menos D+ que su propio GPX (Covalagua integral 270 frente a 480; Golobar–Sel de la Fuente 525 frente a 862; Cervera–Las Cruces 424 frente a 634; Collado del Pinar 400 frente a 703). Usar rangos. El GPX de Peña del Fraile tiene altitudes ruidosas (D+ no fiable).
16. **Discrepancias menores abiertas:** número de esculturas de la Senda Ursi (39 frente a 30); edad del Roblón de Estalaya (500 frente a 600 años); distancia sumidero–surgencia del Pisuerga (~1 frente a ~3 km); nombre de la carretera del Golobar (PP-2203 frente a PP-2204); altitud de Peña Labra (2.018 frente a 2.029) y del Fraile (2.025 frente a 2.001); longitud de La Pedrosa en el plano (5 km, ¿solo ida?).
17. Los iconos de la guía de la Diputación (aptitud para carrera y raquetas, "punto decisivo") no se transcribieron, y la guía no da temporada por ruta.

**Coordenadas, refugios e infraestructura**

18. **Coordenadas exactas de los refugios.** refugioslibres solo publica zonas aproximadas (las exactas exigen cuenta, que no se creó) y en Mazobre la zona falla por ~5 km. Faltan las posiciones verificadas de **Mazobre, Pescadores** (¿42.9384, −4.6427 o ~42.9605, −4.6058?), **Santa Marina, Mollorente, Cristo Sierra, Postil de Soña** y el candidato a **Tenadas de Lores** (43.0238, −4.5532). Cruzar con OSM o preguntar en la Casa del Parque (979 13 94 01).
19. **Estado actual:** Pescadores, "probablemente abierto" (evidencia de usuarios 2021–2023, sin confirmar); Postil de Soña sin ningún dato posterior a 2018; no existe inventario oficial de chozos.
20. Siguen sin coordenadas Lebanza (pueblo), el aparcamiento y mirador de Grullos y los miradores M02, M03, M05, M06 y M08. Algunas coordenadas de palenciaturismo son centroides de pueblo.
21. **Fiabilidad de las fuentes de agua** desconocida: sin caudal estacional, potabilidad ni inventario oficial; la fuente de Pino Llano solo consta por SummitPost.
22. Falta la URL del servicio de equipamientos de uso público de IDECyL/soyecoturista.
23. Horarios no verificados: ROM (Aguilar), centros del Geoparque, Casa del Parque KARST, CIM de Barruelo, Centro de la Trucha, Fundación Oso Pardo y Verdeña; fecha exacta del cierre invernal de la Casa del Parque. **Cueva de los Franceses:** cerrada por obras, sin fecha de reapertura.
24. Sin datos de campings, albergues, áreas de autocaravanas, helipuertos ni cobertura móvil.

**Práctico y normativa**

25. **Guía invernal:** notas contradictorias sobre un PDF de la Diputación (262 descensos, 18 sectores) que el buscador interno no localiza. No se ha abierto.
26. Campaña de aludes 2026-27: fecha de inicio desconocida; tampoco consta si la zona AEMET peu1 incluye la vertiente palentina.
27. No se consultaron la corrección de errores del PORN (11-09-1998), sus posibles modificaciones (Ley 5/2010), la regulación del Camino Natural de Pineda, la normativa micológica ni la licencia de datos JCyL. Falta confirmar la figura de protección vigente de Las Tuerces y de Covalagua.
28. Faltan las resoluciones de oso de 2025–2026, el calendario de batidas 2026-27, el plan de caza vigente y los horarios de los cierres.
29. Faltan fuentes primarias para urogallo, lobo, rebeco y berrea en Palencia.
30. **Ultra Montaña Palentina:** sin web oficial ni recorrido; discrepancia de distancias (65 frente a 80 km).
31. Transporte: horarios 2026 de VACL-111 y VACL-079, operador Cervera–Palencia, transporte a la demanda y cierres de Piedrasluengas. Estación de Aguilar no verificada.
32. Hojas MTN25 y MTN50 sin confirmar; fecha del vuelo LiDAR reciente y URL WMTS de PNOA.
33. Licencias: aviso legal de patrimonionatural.org, términos de Mendikat, licencia del dataset FEDME/CNIG, de los GPX de Caminos Naturales y de los GPX descargables de palenciaturismo (Ribero Pintado, Doncellas del Hoyal).
34. Fechas sin verificar: rescates del Curavacas y del Espigüete citados por El Mirón de Soria y Vozpópuli, y número 286 de Pyrenaica.

---
35. **Fichas (§16):** el JSON de waypoints contiene **318** puntos (no ~330). En la ruta 06, el "Puente del Ves" figura con 1168 m, cota probablemente errónea (~1600 m). Las 24 fichas de la Diputación sin versión gratuita y varias fichas nuevas de la v2 con descripción solo parcial (⚠️) quedan pendientes de completar. Las rutas BTT de §16.8 no tienen descripción extraída.

---

## Siguientes pasos para la app

**Ingerir directamente, con licencia clara:**

- Terreno: **MDT02** en las cumbres y **MDT05** en el resto. Textura: **ortofoto PNOA**. Atribución CC BY 4.0 del IGN.
- **POI de OSM** ejecutando la consulta preparada. Atribución ODbL y share-alike si se redistribuye la base derivada.
- **Tracks propios** grabados en campo. Es la única vía limpia para las sendas oficiales, porque la Junta no publica GPX.
- Con revisión previa de licencia: los GPX de **Caminos Naturales** (Románico Palentino), los de **senderos FEDME del CNIG** si incluyen los PR-P, y los dos GPX descargables de **palenciaturismo** (Ribero Pintado, Doncellas del Hoyal).

**Usar como datos fácticos, reescritos:**

- Las cifras canónicas del **plano oficial 2025** (km, D+, tiempo, dificultad) y las coordenadas de inicio de las fichas oficiales.
- Las coordenadas y altitudes de cumbre, contrastadas entre Mendikat y la Diputación.
- Las cifras MIDE de la tabla del anexo de la Diputación, citando la fuente.
- El JSON de waypoints, solo para validar trazados propios. Filtrar antes los 25 erróneos y pedir permiso a La Pedrera Pindia si se quiere republicar.

**Solo enlazar** (deep link, sin copiar tracks, textos ni fotos):

- Wikiloc, incluida la cuenta de la Fundación.
- Mendikat, Komoot, AllTrails, Terranostrum (incluidos sus 111 GPX) y SummitPost. Las estadísticas de GPX calculadas por nosotros (`terranostrum_gpx_estadisticas.json`) sirven solo para contrastar cifras.
- La guía de la Diputación / La Pedrera Pindia (PDF íntegro y QR), la guía alpina, los folletos de la Junta y el libro de palenciaturismo.

**Capas dinámicas que hay que mantener:**

- Cierres de sendas: consultar semanalmente la página de la Casa del Parque, porque el nombre del PDF cambia.
- Boletines de aludes de AEMET (URL fijas) y predicción peu1 en XML.
- Restricciones temporales por oso (feb–jul) y caza (oct–feb) como capas con fecha.
- Horario de la Casa del Parque por fechas.

**Etiquetado obligatorio en la app:**

- Rutas de la Diputación y de terceros: "ruta de montaña no señalizada".
- Refugios: "abrigo libre, estado no verificado (fecha del dato)". El Golobar y el refugio del club Espigüete **no** deben aparecer como refugio.
- Lagos: aviso de **no pisar el hielo** (Pozo de las Lomas y demás lagos glaciares).
- Agua: "sin control sanitario, tratar siempre".
- Indicador de fuera de provincia (León, Cantabria, Burgos) en Peña Prieta, Tres Provincias, Peña Labra, Tres Mares, Cordel, Lampa, Bistruey, San Glorio, Llánaves, Revelillas y Peña Amaya. Marcar como periferia 🟨 Guardo sur, Fresno del Río, la Ojeda y la Calzada de los Blendios E1; y como fuera del dominio 🟪 el Quejigar de Hérmedes.
- Iconos de peligro: trepada (01, 12, 14, 29, 40), caída de piedras (Curavacas), aludes (Espigüete N, canales del Curavacas), orientación (Peña Redonda) y masificación (Tosande, Mazobre).
