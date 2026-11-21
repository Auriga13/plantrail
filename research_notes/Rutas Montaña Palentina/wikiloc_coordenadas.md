# Wikiloc + Mendikat: tracks de referencia, comentarios y coordenadas (Montaña Palentina)

> **Cómo se obtuvo y cuánto fiarse (léelo primero)**
> - **Wikiloc estaba BLOQUEADO para lectura directa.** `curl` a www/es.wikiloc.com devuelve `HTTP 403` con `cf-mitigated: challenge`, es decir, un reto anti-bot de Cloudflare. WebFetch da `ENOTFOUND es.wikiloc.com`. No se intentó saltar el reto. Por eso los datos de Wikiloc (URL, distancia, desnivel, vistas, comentarios) salen solo de **resultados y resúmenes de WebSearch** limitados a wikiloc.com. Las URLs son reales, porque las devolvió el buscador. Las cifras y los comentarios son resúmenes del buscador y **no se han comprobado en la ficha**: hay que contrastarlos antes de publicarlos en la app. Autor, nº de descargas y valoración casi nunca aparecían.
> - **Mendikat sí se pudo leer** (www.mendikat.net, HTTP 200). Las coordenadas y altitudes de cima, y los tracks de Mendikat (autor, fecha, km, D+, visitas y descargas), se han sacado directamente del JSON embebido en cada página. Es la fuente más fiable de este documento.
> - **No se descargó ningún GPX.** Se intentó bajar unos pocos GPX de Mendikat para sacar el punto de inicio exacto, y el sistema de permisos lo denegó; se respetó. Por eso las coordenadas de salida son *aproximadas*: salen de la caja envolvente del track en Mendikat (lat_min/lon_max…) o de fuentes de terceros.
> - Fecha de consulta: 21-11-2026.

## 1. Coordenadas y altitud de cumbres (Mendikat)

### Takeaway
Mendikat da coordenadas WGS84 y altitud para todas las cumbres pedidas, menos Peña Prieta, que figura en la región de Cantabria y también se ha obtenido. "Pico del Infierno" figura en Mendikat como **"Monte Infierno" (2537 m)**. Peña Prieta queda 2 m por encima (2539 m), y la cumbre más alta íntegramente palentina es el Curavacas (2524 m).

### Cited Findings

| Cumbre | Lat | Lon | Alt (m) | Prominencia (m) | Ascensiones registradas / visitas | Fuente |
|---|---|---|---|---|---|---|
| Curavacas | 42.97635 | -4.67397 | 2524 | 472 | 330 / 54.394 | [Mendikat 8377](https://www.mendikat.net/mount/curavacas-palencia-espana/8377) |
| Espigüete | 42.94461 | -4.79622 | 2451 | 474 | 327 / 46.218 | [Mendikat 8376](https://www.mendikat.net/mount/espiguete-palencia-espana/8376) |
| Peña Prieta (Cantabria, límite con León) | 43.02385 | -4.73001 | 2539 | 929 | 319 / – | [Mendikat 2132](https://www.mendikat.net/mount/pena-prieta-cantabria-espana/2132) |
| Pico del Infierno ("Monte Infierno", Cantabria/Palencia) | 43.02245 | -4.73088 | 2537 | 9 | 94 / 9.294 | [Mendikat 4277](https://www.mendikat.net/mount/monte-infierno-cantabria-espana-and-palencia-espana/4277) |
| Tres Provincias (Cantabria/Palencia/León) | 43.02104 | -4.73803 | 2499 | 56 | 274 / 16.942 | [Mendikat 2133](https://www.mendikat.net/mount/tres-provincias-cantabria-espana-and-palencia-espana-and-leon-espana/2133) |
| Alto del Tío Celestino (extra) | 43.01194 | -4.73247 | 2396 | 34 | 23 / 6.312 | [Mendikat 14039](https://www.mendikat.net/mount/tio-celestino-alto-del-palencia-espana/14039) |
| Pico Murcia (Palencia/León) | 42.98048 | -4.79452 | 2351 | 228 | 175 / 18.841 | [Mendikat 8409](https://www.mendikat.net/mount/murcia-pico-palencia-espana-and-leon-espana/8409) |
| Pico de Hoya Contina | 42.97827 | -4.71145 | 2395 | 182 | 6 / 3.900 | [Mendikat 15947](https://www.mendikat.net/mount/hoya-contina-pico-de-palencia-espana/15947) |
| Lezna | 43.00689 | -4.64670 | 2208 | 473 | 71 / 14.089 | [Mendikat 8378](https://www.mendikat.net/mount/lezna-palencia-espana/8378) |
| Peña Lampa (Palencia/León) | 42.86069 | -4.86546 | 1804 | 488 | 20 / 10.685 | [Mendikat 8705](https://www.mendikat.net/mount/pena-lampa-palencia-espana-and-leon-espana/8705) |
| Peña Mayor (de Velilla) | 42.83819 | -4.82034 | 1869 | 154 | 17 / 8.205 | [Mendikat 13099](https://www.mendikat.net/mount/mayor-pena-palencia-espana/13099) |
| Valdecebollas | 42.96676 | -4.36542 | 2143 | 292 | 208 / 21.976 | [Mendikat 8382](https://www.mendikat.net/mount/valdecebollas-palencia-espana/8382) |
| Peña Labra (Peñalabra, Cantabria/Palencia) | 43.04556 | -4.43221 | 2029 | 77 | 158 / 25.556 | [Mendikat 2129](https://www.mendikat.net/mount/penalabra-cantabria-espana-and-palencia-espana/2129) |
| Tres Mares (Cantabria/Palencia) | 43.03800 | -4.40429 | 2171 | 103 | 230 / 36.564 | [Mendikat 8386](https://www.mendikat.net/mount/tres-mares-cantabria-espana-and-palencia-espana/8386) |
| Peña Redonda (Sierra del Brezo) | 42.85160 | -4.61330 | 1995 | 366 | 84 / 24.254 | [Mendikat 8698](https://www.mendikat.net/mount/pena-redonda-palencia-espana/8698) |
| Pico del Fraile (Peña del Fraile) | 42.83289 | -4.76550 | 2001 | 595 | 87 / 12.667 | [Mendikat 8699](https://www.mendikat.net/mount/fraile-pena-del-palencia-espana/8699) |
| Peña Tremaya | 42.97741 | -4.48031 | 1441 | 176 | 18 / 7.750 | [Mendikat 12903](https://www.mendikat.net/mount/pena-tremaya-palencia-espana/12903) |
| Monte Bernorio | 42.79454 | -4.19491 | 1178 | 256 | 19 / 5.640 | [Mendikat 8261](https://www.mendikat.net/mount/bernorio-palencia-espana/8261) |
| Monte Cildá | 42.75157 | -4.27733 | 985 | 70 | 2 / 1.840 | [Mendikat 20865](https://www.mendikat.net/mount/monte-cilda-palencia-espana/20865) |
| Valcabado (mirador de Covalagua/Ahedo; extra) | 42.78174 | -4.10273 | 1221 | 306 | 22 / 6.545 | [Mendikat 8260](https://www.mendikat.net/mount/valcabado-palencia-espana/8260) |

Otros IDs de Mendikat de la región Palencia que pueden servir: Peña Mayor Oriental 13101, Peña Cueto, Cuartas 8787, Pico Pumar 15950, Cuchillón 2028, Peña Sestil 8388, Horca de Lores 8379, Curavacas Oeste 15954, Torre del Callejo Grande 12935, Espigüete Este 23636 (listado en [Mendikat región Palencia](https://www.mendikat.net/region/palencia)).

- Curavacas: el waypoint de Wikiloc da 42.976395, -4.673913, prácticamente igual que Mendikat. Otra nota del proyecto (Mendiak) da 42.977234, -4.673280, a unos 100 m — [Wikiloc waypoint Curavacas](https://es.wikiloc.com/waypoints/vnm6ra/curavacas).
- Monte Bernorio: los resúmenes de Wikiloc dan cotas de 1169/1171/1178 m según la ficha; Mendikat da 1178 m — [Wikiloc waypoint Monte Bernorio](https://fr.wikiloc.com/waypoints/GaeY1n/monte-bernorio).
- Pozo de los Lobos ≈ 42.7737, -4.0939 y Monte Ahedo ≈ 42.7824, -4.1029, según la ficha de Wikiloc citada por el buscador (sin verificar) — [Wikiloc Valcabado–Hayedo Monte Aedo–Pozo de los Lobos](https://es.wikiloc.com/rutas-senderismo/valcabado-hayedo-monte-aedo-pozo-de-los-lobos-valcabado-24446341).

### Inferences
- En la app, a Peña Prieta conviene llamarla "techo de la Montaña Palentina / Fuentes Carrionas", no "techo de Palencia": Mendikat la sitúa en Cantabria. El "techo provincial" suele atribuirse al Pico del Infierno o "Peña Prieta Sur" (2537 m). A ese "Monte Infierno" Mendikat le da solo 9 m de prominencia, así que es una antecima de Peña Prieta.
- Valcabado (1221 m, Mendikat) coincide con la zona Monte Ahedo / mirador de Valcabado y sirve como POI de referencia del hayedo de Ahedo.

### Gaps
- Mendikat no da la coordenada de Pico Cordel (Cantabria) porque no se consultó. Los resúmenes de Wikiloc dan 2051 m o 2061 m según la ficha — [Wikiloc waypoint Pico Cordel](https://es.wikiloc.com/waypoints/3cnaOM/pico-cordel).

## 2. Coordenadas de pueblos / puntos de salida

### Takeaway
Ningún host permitido ofrece coordenadas oficiales de pueblos. Sin descargar GPX, solo se pueden dar valores **aproximados**, deducidos de la caja envolvente de los tracks de Mendikat cuando el pueblo es un extremo del recorrido (lat/lon mínimo o máximo junto a la altitud mínima del track) y contrastados con terceros cuando ha sido posible. Precisión estimada: unos 200–500 m. Antes de usarlos en la app hay que verificarlos con IGN/OSM.

### Cited Findings

| Salida | Lat aprox. | Lon aprox. | Método / fuente | Fiabilidad |
|---|---|---|---|---|
| Vidrieros | 42.9425 | -4.6642 | GeoNames vía [bamwor](https://bamwor.com/en/countries/spain/cities/vidrieros). Cuadra con lat_min 42.94236 del track [Mendikat 17352](https://www.mendikat.net/track/curavacas-vidrieros-curavacas-hospital-vidrieros/17352), altitud mínima 1327 m | Buena |
| Cardaño de Arriba | ~42.970 | ~-4.756 | Extremo SE (lat_min 42.9693–42.9708; lon_max -4.7553/-4.7582) y altitud mínima 1409 m de los tracks [Mendikat 28231](https://www.mendikat.net/track/murcia-pico-cardano-de-arriba-pico-murcia-valcabe-las-cerezuelas-cardano-de-arriba-2023-07-16/28231) y [8280](https://www.mendikat.net/track/pena-prieta-cardano-de-arriba-tres-provincias-pena/8280). [Mapcarta](https://mapcarta.com/18598314) da una altitud de 1422 m para el pueblo | Media |
| Cardaño de Abajo | ~42.921 | ~-4.764 | Extremo S/E (lat_min 42.92075, lon_max -4.76374) y altitud mínima 1297 m del track [Mendikat 6152](https://www.mendikat.net/track/espiguete-cardano-de-abajo-pista-pedrera-cara-sur-espiguete-inicio/6152). El buscador cita una cota de 1315 m para el pueblo ([Wikiloc Espigüete cara sur](https://www.wikiloc.com/hiking-trails/espiguete-cara-sur-11896919)). OJO: la nota previa [cumbres_alta_montana.md] daba 42.958, -4.765 sin verificar, valor que parece erróneo | Media |
| Parking Pino Llano / cascada de Mazobre (entre los dos Cardaños) | ~42.944–42.957 | ~-4.762 | Extremo E (lon_max -4.76159) del track [Mendikat 25741](https://www.mendikat.net/track/espiguete-parking-cascada-mazobre-cresta-e-pd-inf-espiguete-canales-norte-f/25741), altitud mínima 1341 m | Baja |
| Brañosera | 42.9350 | -4.3078 | AEMET: 42°56'6"N 4°18'28"O, 1211 m ([AEMET](https://www.aemet.es/gl/eltiempo/prediccion/municipios/branosera-id34036)). Cuadra con lat_min 42.93518 / lon_max -4.3073 del track [Mendikat 9607](https://www.mendikat.net/track/valdecebollas-valdecebollas-y-sestil-desde-branosera/9607) | Buena |
| Santa María de Redondo | ~42.988 | ~-4.383 | Extremo S/E (lat_min 42.98797, lon_max -4.383) y altitud mínima 1222 m del track [Mendikat 14232](https://www.mendikat.net/track/tres-mares-santa-maria-de-redondo-pico-tres-mares-cuchillon-santa-maria-de/14232) | Media |
| Aparcamiento Tejeda de Tosande (CL-626) | ~42.8254 | ~-4.5166 | Esquina SE del track [Mendikat 2696](https://www.mendikat.net/track/pena-redonda-ascension-a-la-pena-redonda-por-el-valle/2696) (lat_min 42.82537, lon_max -4.51664). Cuadra con 42.8258, -4.5165 de park4night, recogido en rutas_valles_naturaleza.md | Buena |
| Mirador de Piedrasluengas | ~43.042 | ~-4.459 | Extremo W (lon_min -4.4586) del track [Mendikat 9610](https://www.mendikat.net/track/penalabra-mirador-de-piedrasluengas-penalabra-tres-mares/9610). Cuadra con 43.0417, -4.4593 de infraestructura_poi.md | Buena |
| Traspeña de la Peña | ~42.819 | ~-4.589 | Extremo S/E del track [Mendikat 14227](https://www.mendikat.net/track/pena-redonda-traspena-pena-redonda-burrian-barranco-de-santa-eulalia-traspena/14227), altitud mínima 1161 m | Media |
| Villarén de Valdivia (salida a Bernorio) | ~42.777 | ~-4.185 | Extremo S del track [Mendikat 20178](https://www.mendikat.net/track/bernorio-villaren-de-valdibia-bernorio/20178), altitud mínima 929 m | Baja |
| Velilla del Río Carrión | dentro de 42.841–42.864 / -4.892–-4.857 | – | Solo la caja envolvente del track [Mendikat 16265](https://www.mendikat.net/track/pena-lampa-velilla-del-rio-carrion-monte-valdehaya/16265), altitud mínima 1141 m. No se puede precisar más | Baja |

### Inferences
- Vidrieros, Brañosera, el parking de Tosande y Piedrasluengas coinciden entre dos fuentes independientes. Pueden entrar en la app marcados como "verificado ±200 m".

### Gaps
- **Sin coordenadas desde los hosts permitidos:** Triollo, Lebanza, Cervera de Pisuerga, Aguilar de Campoo, Barruelo de Santullán, Pomar de Valdivia, Revilla de Pomar, San Salvador de Cantamuda y Camporredondo de Alba. Mapcarta y la búsqueda no las dieron, y Wikiloc no se pudo abrir. Hay que sacarlas del Nomenclátor IGN, de OSM (Overpass, `place=village`) o de Wikidata.
- El track de Covalagua en Mendikat ([12349](https://www.mendikat.net/track/valcabado-cueva-de-los-franceses-canto-hito-valcabado-covalagua-cueva-de-los-franceses/12349)) tiene la caja envolvente errónea (lon ≈ -1.46, en Navarra) y no sirve para Revilla de Pomar.

## 3. Tracks de referencia por ruta (Wikiloc vía buscador + Mendikat directo)

### Takeaway
Hay tracks de referencia para casi todas las rutas pedidas. Los de **Mendikat** llevan datos verificados (autor, fecha, km, D+, visitas y descargas), pero son en su mayoría de 2014–2019; los más recientes son de 2023, 2025 y 2026. Los de **Wikiloc** son más numerosos y algunos más recientes, pero sus cifras solo se conocen por el resumen del buscador. "Cascadas de Lebanza" no aparece como ruta en Wikiloc.

### Cited Findings

Leyenda: [M] = Mendikat, leído directamente. [W] = Wikiloc, URL del buscador con cifras resumidas por el buscador y sin verificar. "vis/desc" = visitas/descargas.

#### Alta montaña: Fuentes Carrionas

| Ruta | Track | Autor · fecha | Dist · D+ | Popularidad | Notas (resumen) |
|---|---|---|---|---|---|
| Curavacas normal (Vidrieros, Callejo Grande) | [M 17352](https://www.mendikat.net/track/curavacas-vidrieros-curavacas-hospital-vidrieros/17352) | Rafael Bartolomé · 18-07-2019 | 12,5 km · 1364 m | 22.692 vis / 2.300 desc | Circular Vidrieros–Curavacas–Hospital. Altitud de 1327 a 2519 m; unas 7 h 56 min en total |
| ″ | [M 14197](https://www.mendikat.net/track/curavacas-vidrieros-curavacas-por-el-callejo-grande/14197) | Javier Tezanos Díaz · 12-07-2018 | 9,5 km · 1170 m | – | Ida y vuelta por el Callejo Grande |
| ″ | [W 11774659 "Pico Curavacas (Montaña Palentina)"](https://www.wikiloc.com/hiking-trails/pico-curavacas-montana-palentina-11774659) | – | ~11,1 km · ~1196 m | ~83.880 vis | Arroyo Cabriles y Callejo Grande; unas 2:30 de subida y 2:00 de bajada. Un comentario avisa de que no hay señalización, solo algún hito (cairn) |
| ″ | [W 133695529](https://es.wikiloc.com/rutas-senderismo/curavacas-desde-vidrieros-por-callejo-grande-133695529) | – | 10,74 km · 1147 m | – | "Difícil". Inicio fácil, luego pedrera y trepada final |
| ″ | [W 104866053 circular con Hospital y Huelgas](https://www.wikiloc.com/hiking-trails/circular-curavacas-desde-vidrieros-curavacas-pico-hospital-monte-de-las-huelgas-y-descenso-por-coll-104866053) | – | ~12,3 km | – | Bajada por el Collado Mollorente |
| Curavacas Canal Sur (invernal) | [W 99549660](https://es.wikiloc.com/rutas-alpinismo/canal-sur-del-curavacas-desde-vidrieros-99549660) | – | – | – | Canal recta de más de 400 m, media de unos 38° con tramos de 60° arriba; sale a unos 2470 m. Piolet y crampones imprescindibles; bajada por el Callejo Grande |
| ″ | [W 68926959](https://es.wikiloc.com/rutas-alpinismo/invernal-al-curavacas-por-canal-sur-directo-y-vuelta-por-callejo-grande-68926959) | – · 2021 | – | – | Calificada "solo expertos", con un tramo superior de 35–60° |
| ″ | [W 6765286 Canal Sur directa](https://es.wikiloc.com/rutas-alpinismo/canal-sur-directa-al-curavacas-6765286) | – · 05-2014 | 9,42 km | – | 45–50° con final a 60°; se recomiendan 2 piolets |
| ″ | [M 16931 Corredor Oblicuo](https://www.mendikat.net/track/curavacas-los-tres-curavacas-por-el-corredor-oblicuo-y/16931) | Roberto Gil Alonso · 13-05-2019 | 13,3 km · 1561 m | – | Los tres Curavacas, con bajada por el Callejo Grande |
| Espigüete cara sur (Cardaño de Abajo) | [M 6152](https://www.mendikat.net/track/espiguete-cardano-de-abajo-pista-pedrera-cara-sur-espiguete-inicio/6152) | Rafael Bartolomé Resano · 20-09-2012 | 11,2 km · 1183 m | 1.121 vis / 9 desc | Pista, luego la pedrera sur |
| ″ | [W 11896919 "Espigüete cara sur"](https://www.wikiloc.com/hiking-trails/espiguete-cara-sur-11896919) | – · 2014 | – | ~25.800 vis | Salida de Cardaño de Abajo (1315 m) por la Dehesa de Cardaño; base de la montaña a unos 4 km; la Pedrera sur es la vía más frecuentada. Unas 5 h 9 min |
| ″ | [W 148786413](https://www.wikiloc.com/hiking-trails/subida-al-espiguete-por-su-cara-sur-148786413) | – | – | – | Otra ficha de la cara sur |
| Espigüete norte / invernal | [M 25741](https://www.mendikat.net/track/espiguete-parking-cascada-mazobre-cresta-e-pd-inf-espiguete-canales-norte-f/25741) | Rafael Bartolomé Resano · 14-07-2023 | 10,2 km · 1128 m | 1.107 vis / 12 desc | Parking cascada Mazobre, Cresta E (PD inf.), cumbre y bajada por las canales norte |
| ″ | [W 9110380 corredor norte](https://es.wikiloc.com/rutas-alpinismo/espiguete-invernal-por-el-corredor-norte-9110380) | – · 2015 | 13,66 km · ~1130 m | – | "Totalmente desaconsejable tras una nevada por el notable riesgo de aludes. Crampones y piolet imprescindibles" |
| ″ | [W 260648121 Goulotte Norte](https://es.wikiloc.com/rutas-alpinismo/espiguete-goulotte-norte-260648121) | montanhaescalada.com · 03-2026 | 10,2 km · 1090 m | – | Registro reciente: corredor norte de aproximación y paso por la cima Este |
| ″ | [W 29960126 arista E y canal norte](https://www.wikiloc.com/hiking-trails/espiguete-2-451-m-subida-por-arista-este-y-bajada-por-canal-de-la-cara-norte-cascada-de-mazobre-29960126) | – | – | – | Combinación clásica, con bajada hacia Mazobre |
| Peña Prieta / Infierno / Tres Provincias (Cardaño de Arriba) | [M 8280](https://www.mendikat.net/track/pena-prieta-cardano-de-arriba-tres-provincias-pena/8280) | Enrique Fernández Vieites · 29-10-2014 | 20,5 km · 1427 m | 29.510 vis / 1.247 desc | Circular por Tres Provincias, Peña Prieta y Alto del Ves |
| ″ | [M 2698](https://www.mendikat.net/track/pena-prieta-cardano-de-arriba-pozo-lomas-pena/2698) | Julio · 21-07-2009 | 8,4 km · 1440 m | 29.749 vis / 4.922 desc | Cardaño de Arriba, Pozo Lomas y Peña Prieta. Es el track más descargado de Mendikat en la zona |
| ″ | [M 16487](https://www.mendikat.net/track/pena-prieta-cardano-de-arriba-alto-del-tio-celestino/16487) | Ivan Gil Esteban · 10-04-2019 | 19,3 km · 1282 m | – | Por el Tío Celestino, el Alto de Fuentes Carrionas y Tres Provincias |
| ″ | [W 143075784](https://www.wikiloc.com/hiking-trails/techo-de-palencia-pico-infierno-mojon-de-las-3-provincias-y-pena-prieta-desde-cardano-de-arriba-143075784) / [W 220720071 por Canalagujas](https://es.wikiloc.com/rutas-senderismo/techo-de-palencia-pico-del-infierno2537m-por-canalagujas-de-cardanocon-pena-prieta2539m-y-tres-prov-220720071) | – | – | – | Ya citados en cumbres_alta_montana.md |
| Pico Murcia (Cardaño de Arriba) | [M 28231](https://www.mendikat.net/track/murcia-pico-cardano-de-arriba-pico-murcia-valcabe-las-cerezuelas-cardano-de-arriba-2023-07-16/28231) | Rafael Bartolomé Resano · 16-07-2023 | 15,4 km · 1014 m | 867 vis | Circular por Valcabe y Las Cerezuelas |
| Pozo de las Lomas + Laguna de Fuentes Carrionas (+ Pozo Curavacas) | [W 175034497](https://es.wikiloc.com/rutas-senderismo/circular-cardano-de-arriba-pozo-de-las-lomas-laguna-de-fuentes-carrionas-pozo-del-curavacas-collado-175034497) · [W 82945106](https://www.wikiloc.com/mountaineering-trails/pozo-las-lomas-laguna-de-fuentes-carrionas-pozo-curavacas-pozos-del-ves-circular-montana-palentina-82945106) · [W 6759091](https://www.wikiloc.com/mountaineering-trails/pozo-de-las-lomas-alto-de-fuentes-carrionas-desde-cardano-de-arriba-6759091) | – | – | – | Ya citados en otras notas del proyecto. No se pudo leer ningún comentario nuevo |
| Pozo Curavacas (Vidrieros, valle de Pineda) | [W 19631676](https://es.wikiloc.com/rutas-senderismo/vidrieros-pozo-curavacas-19631676) | – · 2017 | ~20,9 km (solo ida) | – | Sube el valle de Pineda junto al Carrión; prevé pernoctar en un refugio |
| ″ | [W 2778852](https://www.wikiloc.com/hiking-trails/vidrieros-pozo-curavacas-2778852) | – · 2012 | ~37 km i/v · ~490 m | – | "Difícil", unas 8 h; a pie o en bici |
| ″ | [W 133781826 (MTB)](https://es.wikiloc.com/rutas-mountain-bike/pozo-curavacas-desde-vidrieros-valle-de-pineda-montana-palentina-133781826) | – · 2023 | ~39,9 km circular | – | 5 h 20 min; BTT por pista |
| ″ | [W 51963484 (MTB)](https://es.wikiloc.com/rutas-mountain-bike/pozo-curavacas-51963484) | – · 2020 | ~43 km | – | Rodea el Curavacas hasta la Vega de los Cantos y termina a pie |
| Valle de Pineda | [W 77588245](https://es.wikiloc.com/rutas-senderismo/vidrieros-rio-carrion-valle-de-pineda-77588245) · [W 7433651 (MTB desde Triollo)](https://www.wikiloc.com/mountain-biking-trails/pozo-curavacas-por-el-valle-de-pineda-7433651) | – | ~43 km (MTB) | – | Según la ficha MTB, pasada la Vega de Cantos el camino es demasiado empinado y pedregoso para la bici |
| Cascada de Mazobre | [W 150311857](https://www.wikiloc.com/hiking-trails/cascada-de-mazobre-cardano-de-arriba-150311857) · [W 177185185 (cascada y refugio)](https://es.wikiloc.com/rutas-senderismo/cascada-y-refugio-de-mazobre-177185185) · [W 6384045](https://es.wikiloc.com/rutas-senderismo/cascada-de-mazobre-6384045) | – | 5,9 km i/v · ~257 m (corta); 8,6 km · 379 m (circular desde Pino Llano, con 2ª cascada y refugio) | – | Fácil, menos de 2 h. En invierno la nieve dificulta la subida |
| Integral de Fuentes Carrionas | [W 1782833 (2 noches)](https://www.wikiloc.com/hiking-trails/integral-fuentes-carrionas-circular-2-noches-1782833) · [W 141106061 (5 pozas + Peña Prieta, trail)](https://www.wikiloc.com/trail-running-trails/recorrido-a-las-5-pozas-de-fuentes-carrionas-con-cima-en-pena-prieta-141106061) | – | – | – | Ya citados en otras notas |
| Lezna | [M 20006](https://www.mendikat.net/track/lezna-cucayo-pico-pumar-lezna-pena/20006) | Ivan Gil Esteban · 12-09-2020 | 21,6 km · 1550 m | 17.188 vis / 2.192 desc | Desde Cucayo (Cantabria) por el Pumar |
| ″ | [W 5376595 Lores–Lezna–Cucayo](https://es.wikiloc.com/rutas-senderismo/lores-pico-lezna-2208-m-cucayo-5376595) | – · 2013 | 21,43 km (ida) · 1138 m | – | "Difícil"; la vertiente palentina sale de Lores |
| ″ | [W 95293455 Lezna y Pumar desde Cucayo](https://es.wikiloc.com/rutas-senderismo/pico-lezna-y-pico-pumar-desde-cucayo-95293455) | – · 2022 | 19,12 km · 1326 m | – | Casi todo por pista, pero exigente por el desnivel |
| ″ | [W 12093110 semicircular desde Lores](https://www.wikiloc.com/hiking-trails/ruta-semicircular-desde-lores-hasta-el-pico-lezna-y-el-pumar-12093110) | – · 2016 | ~22 km | – | Un usuario avisa: "al menos 8 h y 22 km" (registro de 8 h 51 min) |

#### Pisuerga, Brañosera, Peña Labra

| Ruta | Track | Autor · fecha | Dist · D+ | Popularidad | Notas |
|---|---|---|---|---|---|
| Valdecebollas desde Brañosera | [M 9607](https://www.mendikat.net/track/valdecebollas-valdecebollas-y-sestil-desde-branosera/9607) | Enrique Fernández Vieites · 10-10-2015 | 16,9 km · 1015 m | 16.526 vis / 2.192 desc | Circular por el Sestil Alto. Altitud de 1191 a 2142 m |
| ″ | [M 16481](https://www.mendikat.net/track/valdecebollas-branosera-sestil-alto-valdecebollas-cueto/16481) | Ivan Gil Esteban · 10-04-2019 | 18,9 km · 1105 m | – | Vuelta por el Cueto de Comunales |
| ″ | [W 15696656](https://es.wikiloc.com/rutas-senderismo/valdecebollas-desde-branosera-15696656) | – | 16,78 km · 977 m | – | "Difícil", unas 6 h 8 min. Sigue el libro *Ascensiones en la Montaña Palentina* (Villegas y Rioja) |
| ″ | [W 52397436 (julio 2020)](https://www.wikiloc.com/hiking-trails/pico-valdecebollas-desde-branosera-circular-julio-2020-52397436) | – · 07-2020 | – | – | Salida junto al cementerio de Brañosera y bajada por el valle del Rubagón |
| ″ (corta) | [W 15111234 desde el refugio del Golobar](https://es.wikiloc.com/rutas-alpinismo/pico-valdecebollas-desde-el-refugio-del-golobar-15111234) | – | 6,23 km · 394 m | – | Fácil. Se llega en coche desde Brañosera o Salcedillo por la PP-2204 |
| Peña Tremaya | [M 10936](https://www.mendikat.net/track/pena-tremaya-branosera-pena-tremaya-tremaya/10936) | Javier Tezanos Díaz · 20-11-2016 | 22,7 km · 908 m | 29.799 vis / 1.222 desc | Travesía Brañosera–Tremaya |
| ″ | [W 108980041](https://www.wikiloc.com/hiking-trails/pena-tremaya-108980041) | – · 2022 | ~5 km · ~269 m | – | Circular corta y fácil desde Tremaya, unos 78 min en movimiento |
| ″ | [W 4596617](https://es.wikiloc.com/rutas-senderismo/pena-tremaya-montana-palentina-4596617) | – | 4,78 km · 263 m | – | Casi todo por pista forestal |
| ″ | [W 150328856 desde San Salvador de Cantamuda](https://es.wikiloc.com/rutas-senderismo/pena-tremaya-desde-san-salvador-de-cantamuda-150328856) | – | 8,88 km circular | – | – |
| Peña Labra / Tres Mares (Piedrasluengas) | [M 9610](https://www.mendikat.net/track/penalabra-mirador-de-piedrasluengas-penalabra-tres-mares/9610) | Enrique Fernández Vieites · 10-10-2015 | 13,1 km · 1019 m | 18.617 vis / 2.450 desc | Mirador de Piedrasluengas, Peñalabra, Tres Mares y vuelta |
| ″ | [M 25488](https://www.mendikat.net/track/penalabra-mirador-pidedrasluengas-penalabra-tres-mares-sta-maria-de-redondo-travesia-jon-hueso-) (URL truncada; buscar ID 25488) | Jon Hueso · 26-04-2023 | 15,3 km · 998 m | – | Travesía de Piedrasluengas a Santa María de Redondo |
| Tres Mares desde Santa María de Redondo (incluye Fuente Cobre) | [M 14232](https://www.mendikat.net/track/tres-mares-santa-maria-de-redondo-pico-tres-mares-cuchillon-santa-maria-de/14232) | Roberto Gil Alonso · 16-07-2018 | 18,8 km · 1224 m | 22.754 vis / 85 desc | Circular por el Cuchillón |
| Pico Cordel / Mirador de Piedrasluengas | [W 2884830 Piedrasluengas–Bistruey–Cucayo](https://www.wikiloc.com/hiking-trails/mirador-de-piedrasluengas-pena-bistruey-o-astruya-cucayo-2884830) · [W 76749509 Pico Cordel](https://www.wikiloc.com/hiking-trails/pico-cordel-76749509) · [W 3285945 desde Brañavieja](https://www.wikiloc.com/hiking-trails/ascension-al-pico-cordel-2061-m-desde-branavieja-ida-3285945) | – | ~5,1 km (ida) · ~469 m desde Brañavieja | – | No hay una ruta "Pico Cordel desde Piedrasluengas" como tal: el Cordel está en Cantabria (Alto Campoo) y se sube más fácil desde Brañavieja o Palombera |
| Fuente Cobre (nacimiento del Pisuerga) | [W 110546072](https://www.wikiloc.com/hiking-trails/cueva-de-fuente-del-cobre-nacimiento-del-rio-pisuerga-110546072) · [W 257716188](https://es.wikiloc.com/rutas-senderismo/cueva-del-cobre-desde-santa-maria-de-redondo-257716188) · [W 17946364 PR-P 8](https://www.wikiloc.com/hiking-trails/senda-de-fuente-cobrepr-p-8-17946364) | – | – | – | Ya citados en otras notas. Sin comentarios nuevos legibles |

#### Sierra del Brezo, Tosande, Velilla

| Ruta | Track | Autor · fecha | Dist · D+ | Popularidad | Notas |
|---|---|---|---|---|---|
| Peña Redonda | [M 14227](https://www.mendikat.net/track/pena-redonda-traspena-pena-redonda-burrian-barranco-de-santa-eulalia-traspena/14227) | Roberto Gil Alonso · 15-07-2018 | 12,7 km · 1011 m | 22.596 vis / 48 desc | Circular desde Traspeña por el Burrián y el barranco de Santa Eulalia |
| ″ | [M 2696 por el valle de Tosande](https://www.mendikat.net/track/pena-redonda-ascension-a-la-pena-redonda-por-el-valle/2696) | Julio · 20-07-2009 | 10,1 km · 1118 m | 17.815 vis / 1.497 desc | Sube desde el parking de Tosande |
| ″ | [W 27328345 desde Villanueva de la Peña por el Burrián](https://www.wikiloc.com/hiking-trails/pena-redonda-1-995-m-circular-por-el-cdo-de-burrian-desde-villanueva-de-la-pena-palencia-27328345) | – | ~12 km · ~904 m | – | Dificultad técnica moderada |
| ″ | [W 78127949 circular por el barranco](https://es.wikiloc.com/rutas-senderismo/importantes-cimas-de-la-sierra-del-brezo-circular-a-la-pena-redonda-y-pico-rebanal-por-el-barranco-78127949) | – | ~15,7 km · 1028 m | – | Subida por sendas poco marcadas, fácil perderse; bajada calurosa. En la cima hay una cruz metálica de unos 14 m; romería el primer domingo de agosto |
| Pico del Fraile | [M 28948](https://www.mendikat.net/track/fraile-pena-del-cristo-sierra-pena-del-fraile-cueto-cristo-sierra/28948) | Rafael Bartolomé Resano · 19-07-2025 | 7,9 km · 572 m | 741 vis | El más reciente de Mendikat: Cristo Sierra, Peña del Fraile, Cueto y vuelta |
| ″ | [M 14677 desde el Santuario del Brezo](https://www.mendikat.net/track/fraile-pena-del-santuario-del-brezo-pico-del-fraile-pena-cueto-cueto-herrera-santuar) (URL truncada; buscar ID 14677) | Roberto Gil Alonso · 09-09-2018 | 11,5 km · 940 m | – | – |
| ″ | [W 36224517](https://www.wikiloc.com/hiking-trails/pico-del-fraile-36224517) | – | – | – | Ya citado en otras notas |
| Peña Mayor | [M 14584](https://www.mendikat.net/track/mayor-pena-campos-de-la-pena-pena-mayor-pico-del-fraile-campos-de/14584) | Roberto Gil Alonso · 22-08-2018 | 18,9 km · 1271 m | 14.769 vis / 2.459 desc | Circular desde Campos de la Peña con el Pico del Fraile |
| ″ | [W 71294743 desde el poblado de Compuerto](https://www.wikiloc.com/hiking-trails/pena-mayor-1-836-m-desde-poblado-de-compuerto-sierra-del-brezo-xi-71294743) | – · 04-2021 | ~9,7 km | – | Pinar de Velilla, con Peña Mayor de Velilla (1869) y de Guardo (1839) |
| ″ | [W 55441243 cordal Peñas Mayores–Fraile](https://www.wikiloc.com/hiking-trails/cordal-de-la-sierra-del-brezo-penas-mayores-y-pena-del-fraile-velilla-del-rio-carrion-palencia-55441243) | – | ~22,2 km · ~1457 m | – | Se puede acortar volviendo por el asfalto en vez de por el pinar |
| Peña Lampa | [M 16265](https://www.mendikat.net/track/pena-lampa-velilla-del-rio-carrion-monte-valdehaya/16265) | Ivan Gil Esteban · 19-03-2019 | 9,9 km · 748 m | 14.160 vis / 2.063 desc | Desde Velilla por el Monte Valdehaya y el Collado Verdugo |
| ″ | [W 14213545 ASC15](https://es.wikiloc.com/rutas-senderismo/asc15-pena-lampa-14213545) | – | 9,68 km · 657 m | – | Moderada; cresta afilada y bajada por Valdehaya |
| ″ | [W 140549177 con Torre Magalana y Roblón](https://es.wikiloc.com/rutas-senderismo/pena-lampa-torre-magalana-roblon-el-monasterio-y-sabinar-de-pena-lampa-140549177) | – | – | – | Aviso: aparcamiento en la carretera de Besande; la pista tiene tráfico de camiones de una mina cercana |
| ″ | [W 176630925 por la arista SE](https://es.wikiloc.com/rutas-senderismo/subida-a-pena-lampa-176630925) | – | 15,5 km circular | – | Moderada |
| Tejeda de Tosande | [W 141704149 desde el parking](https://es.wikiloc.com/rutas-senderismo/tejeda-de-tosande-desde-el-parking-141704149) · [W 22093550](https://www.wikiloc.com/hiking-trails/senda-de-la-tejeda-de-tosande-p-n-fuentes-carrionas-22093550) · [W 58921442](https://www.wikiloc.com/hiking-trails/senda-de-la-tejeda-de-tosande-58921442) · [W 24657668 (lasrutasdejulio)](https://es.wikiloc.com/rutas-senderismo/montana-palentina-tejeda-de-tosande-parque-natural-de-fuentes-carrionas-y-fuente-cobre-24657668) | – | – | – | Ver comentarios en la sección 4 |
| Senda de los Pescadores (Velilla) | [W 172187903](https://es.wikiloc.com/rutas-senderismo/maravilloso-paseo-por-la-senda-de-los-pescadores-de-velilla-del-rio-carrion-172187903) · [W 108316180](https://es.wikiloc.com/rutas-senderismo/senda-de-los-pescadores-en-velilla-del-rio-carrion-108316180) · [W 28162002](https://es.wikiloc.com/rutas-senderismo/senda-de-los-pescadores-velilla-del-rio-carrion-28162002) | – | – | – | Ya citados en otras notas. Sin datos nuevos |
| Bosque Fósil de Verdeña | [W 33425902](https://es.wikiloc.com/rutas-senderismo/senda-del-bosque-fosil-verdena-33425902) | – | – | – | Ya citado. Sin datos nuevos |
| Cascadas de Lebanza | No se encontró en Wikiloc ninguna ruta con "cascada" en Lebanza. Alternativas desde la abadía: [W 51590770 Peña Carazo y Horca de Lores, circular](https://es.wikiloc.com/rutas-senderismo/pena-carazo-y-horca-de-lores-desde-el-monasterio-de-sta-maria-de-lebanza-circular-51590770) · [W 147075263 Abadía–Refugio de Linares–Hoyo de la Braguilla](https://www.wikiloc.com/hiking-trails/abadia-de-lebanza-refugio-de-linares-hoyo-de-la-braguilla-147075263) | – | ~16 km · ~975 m (Carazo); 11,6 km · ~446 m (Linares) | – | – |

#### Aguilar, La Lora, Valdivia

| Ruta | Track | Autor · fecha | Dist · D+ | Popularidad | Notas |
|---|---|---|---|---|---|
| Covalagua | [M 12349](https://www.mendikat.net/track/valcabado-cueva-de-los-franceses-canto-hito-valcabado-covalagua-cueva-de-los-franceses/12349) | Roberto Gil Alonso · 08-10-2017 | 14,6 km · 369 m | 10.642 vis / 1.633 desc | Cueva de los Franceses, Canto Hito, Valcabado, Covalagua. La caja envolvente del track en Mendikat es errónea |
| ″ | [W 163522451 desde Revilla de Pomar](https://www.wikiloc.com/walking-trails/cascada-de-covalagua-desde-revilla-de-pomar-163522451) | – | – | – | Sigue un PR; la cascada está a unos 2 km |
| ″ | [W 40787618 Pomar–Menhir–Valcabado–Cueva de los Franceses–Covalagua](https://www.wikiloc.com/hiking-trails/pomar-de-valdivia-menhir-canto-hito-mirador-de-valcabado-cueva-de-los-franceses-cascadas-de-covalag-40787618) | – · 2019 | ~27 km circular | – | – |
| ″ | [W 16686613 Pomar–Peña Corvera–Menhir–Covalagua](https://www.wikiloc.com/hiking-trails/pomar-de-valdivia-pena-corvera-menhir-cueva-de-los-franceses-cascada-de-covalagua-16686613) | – · 2017 | ~20,8 km · ~435 m | – | Moderada |
| Hayedo de Monte Ahedo / Pozo de los Lobos | [W 24446341 Valcabado–Hayedo–Pozo de los Lobos](https://es.wikiloc.com/rutas-senderismo/valcabado-hayedo-monte-aedo-pozo-de-los-lobos-valcabado-24446341) | – | 3,51 km · 151 m | 4,7★ (1 voto) | Fácil; baja entre calizas a un hayedo denso |
| ″ | [W 120952868 Revilla de Pomar–Covalagua–Alto de Ahedo–Pozo de los Lobos](https://www.wikiloc.com/hiking-trails/revilla-de-pomar-cascada-de-covalagua-alto-de-ahedo-pozo-de-los-lobos-bosque-ahedo-120952868) | – | ~16 km | – | Fácil. Baja por el único paso practicable y bien marcado al hayedo y a la trampa lobera |
| ″ | [W 178356481 Revelillas–Pozo de los Lobos](https://www.wikiloc.com/hiking-trails/revelillas-pozo-de-los-lobos-178356481) | – | ~10,5 km | – | Moderada; sube por robledal y baja por hayedo. Revelillas está en Cantabria |
| Monte Bernorio | [M 20178](https://www.mendikat.net/track/bernorio-villaren-de-valdibia-bernorio/20178) | Julián Cobo Gutiérrez · 18-09-2020 | 8,1 km · 242 m | 17.373 vis / 1.421 desc | Ida y vuelta desde Villarén de Valdivia |
| ″ | [W 23841391 Vueltiviri, Covalagua y Bernorio](https://es.wikiloc.com/rutas-senderismo/vueltiviri-covalagua-y-monte-bernorio-27-3-18-23841391) | – · 03-2018 | ~27,9 km | – | Circular desde Revilla de Pomar, con altitud máxima de 1221 m |
| Las Tuerces / Monte Cildá | [M 25561](https://www.mendikat.net/track/monte-cilda-monte-cilda-las-tuerces/25561) | Juanan Galán · 13-05-2023 | 10,0 km · 373 m | 928 vis | Circular Monte Cildá–Las Tuerces |
| ″ | [W 133377939 Las Tuerces desde Aguilar](https://es.wikiloc.com/rutas-senderismo/las-tuerces-desde-aguilar-de-campoo-133377939) | – | – | – | Ya citado en otras notas |

### Inferences
- Para "tracks de referencia" en la app conviene enlazar **Mendikat** cuando haga falta un dato fiable (autor, fecha, D+, descargas) y **Wikiloc** como alternativa popular, con los números recomprobados a mano.
- Los tracks de Mendikat con más descargas en la zona son: Peña Prieta por el Pozo Lomas (4.922), Peña Mayor–Fraile (2.459), Piedrasluengas–Peñalabra–Tres Mares (2.450), Curavacas desde Vidrieros (2.300) y Valdecebollas desde Brañosera (2.192). Son un buen indicador de las rutas "estrella".

### Gaps
- Faltan autor, nº de descargas, valoración y fecha exacta de casi todos los tracks de Wikiloc, por el bloqueo de Cloudflare. Hay que revisarlos manualmente en un navegador o pedir acceso con navegador.
- No hay tracks nuevos verificados para Senda de los Pescadores, Verdeña, Fuente Cobre, Las Tuerces (Wikiloc) ni para el Pozo de las Lomas: solo URLs ya conocidas.

## 4. Comentarios recientes de usuarios (condiciones, dificultad, avisos)

### Takeaway
Casi no hay comentarios recientes accesibles. Los tracks de Mendikat de la selección no tienen comentarios de usuarios (`posts` vacío, salvo un aviso de moderación en el 9607), y los comentarios de Wikiloc solo llegan como fragmentos del buscador. Los más útiles son los de **Tosande (2024)** y los avisos invernales del **Espigüete norte** y la **Canal Sur del Curavacas**.

### Cited Findings
- **Tejeda de Tosande (2024).** Un usuario señala el 31-05-2024 que el cartel pone "Tejal" y no "Tejeda", y el autor (lasrutasdejulio) contesta que lo cambiará; otro usuario defiende "Tejeda" ("bosque de tejos"). Junio de 2024: "Una de las rutas más bonitas e interesantes de la Montaña Palentina". Octubre de 2024 (alcafe99): "Espectaculares los tejos y el hayedo. Y además es fácil". Un comentario de 2024 lamenta que "la masificación hace perder su encanto", y otro avisa del calor en julio — [Wikiloc 24657668](https://es.wikiloc.com/rutas-senderismo/montana-palentina-tejeda-de-tosande-parque-natural-de-fuentes-carrionas-y-fuente-cobre-24657668); [Wikiloc 141704149](https://es.wikiloc.com/rutas-senderismo/tejeda-de-tosande-desde-el-parking-141704149). Desde Cervera, noviembre de 2024: recomendada en otoño por los tejos, robles y hayas — [Wikiloc 18537267](https://www.wikiloc.com/hiking-trails/cervera-de-pisuerga-tejeda-de-tosande-18537267). (El buscador no dejó claro qué comentario corresponde a qué ficha de Tosande.)
- **Curavacas normal:** no hay señalización, solo algún hito ocasional; la pedrera del Callejo Grande es lo más duro y la trepada final no es para principiantes — [Wikiloc 11774659](https://www.wikiloc.com/hiking-trails/pico-curavacas-montana-palentina-11774659); [Wikiloc 133695529](https://es.wikiloc.com/rutas-senderismo/curavacas-desde-vidrieros-por-callejo-grande-133695529).
- **Curavacas Canal Sur:** 38° de media con tramos de 60°; piolet y crampones imprescindibles; "solo expertos" (2021) — [Wikiloc 99549660](https://es.wikiloc.com/rutas-alpinismo/canal-sur-del-curavacas-desde-vidrieros-99549660); [Wikiloc 68926959](https://es.wikiloc.com/rutas-alpinismo/invernal-al-curavacas-por-canal-sur-directo-y-vuelta-por-callejo-grande-68926959).
- **Espigüete norte:** desaconsejado tras una nevada por riesgo de aludes; crampones y piolet imprescindibles (2015). Un registro de 2017 la describe como "muy exigente, con mucha pedrera y trepadas", peligrosa en invierno; otro de diciembre de 2017 cuenta que un montañero les desaconsejó subir por la norte y la usaron solo para bajar — [Wikiloc 9110380](https://es.wikiloc.com/rutas-alpinismo/espiguete-invernal-por-el-corredor-norte-9110380); [Wikiloc 19857255](https://es.wikiloc.com/rutas-alpinismo/espiguete-cara-norte-19857255).
- **Cascada de Mazobre:** en invierno la nieve dificulta la subida — [Wikiloc 150311857](https://www.wikiloc.com/hiking-trails/cascada-de-mazobre-cardano-de-arriba-150311857).
- **Covalagua:** la cascada puede ir casi seca; hay informes de octubre de 2018 y de un invierno seco de 2017 — [Wikiloc 16686613](https://www.wikiloc.com/hiking-trails/pomar-de-valdivia-pena-corvera-menhir-cueva-de-los-franceses-cascada-de-covalagua-16686613).
- **Peña Redonda:** las sendas de subida por el barranco están poco marcadas y es fácil perderse; la bajada es calurosa. En la variante desde Rebanal, el tramo final está mal marcado en el track — [Wikiloc 78127949](https://es.wikiloc.com/rutas-senderismo/importantes-cimas-de-la-sierra-del-brezo-circular-a-la-pena-redonda-y-pico-rebanal-por-el-barranco-78127949); [Wikiloc 91646014](https://www.wikiloc.com/hiking-trails/penarredonda-1-993-m-desde-rebanal-de-las-llantas-sierra-del-brezo-xiii-91646014).
- **Peña Lampa:** pista con tráfico de camiones de mina; aparcar en la carretera de Besande — [Wikiloc 140549177](https://es.wikiloc.com/rutas-senderismo/pena-lampa-torre-magalana-roblon-el-monasterio-y-sabinar-de-pena-lampa-140549177).
- **Lezna desde Lores:** "al menos 8 h y 22 km" — [Wikiloc 12093110](https://www.wikiloc.com/hiking-trails/ruta-semicircular-desde-lores-hasta-el-pico-lezna-y-el-pumar-12093110).
- **Valle de Pineda en BTT:** pasada la Vega de Cantos el camino es demasiado empinado y pedregoso para la bici — [Wikiloc 7433651](https://www.wikiloc.com/mountain-biking-trails/pozo-curavacas-por-el-valle-de-pineda-7433651).
- **Mendikat:** los 20 tracks revisados no tienen comentarios de usuarios. El track [9607](https://www.mendikat.net/track/valdecebollas-valdecebollas-y-sestil-desde-branosera/9607) solo tiene una nota de moderación (2018).

### Inferences
- Avisos recurrentes que merecen icono en la app: pedrera o trepada (Curavacas, Espigüete sur), riesgo de aludes y material invernal (Espigüete N, Canal Sur), sendas mal marcadas (Peña Redonda), masificación y calor (Tosande en verano), cascadas secas en estiaje (Covalagua).

### Gaps
- Faltan comentarios de 2025–2026 de casi todas las rutas (Peña Prieta, Pozo Lomas, Valdecebollas, Bernorio, Tuerces, Verdeña, Pescadores, Fuente Cobre). Wikiloc no se pudo leer y Mendikat no tiene comentarios.
- No hay ningún dato sobre las "Cascadas de Lebanza" en Wikiloc. Puede que el nombre no se use allí, o que la ruta se llame por la abadía o el arroyo.
