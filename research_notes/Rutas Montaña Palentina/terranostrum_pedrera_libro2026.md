# Montaña Palentina: relleno de huecos con Terranostrum, palenciaturismo (libro 2026) y La Pedrera Pindia

Fecha de consulta: 21-11-2026. Notas de investigación para completar las fichas del informe `reports/Rutas Montaña Palentina.md` (§1 y §16). El informe no se ha tocado.

**Confianza**: ✅ dato leído directamente en la fuente (página o GPX descargado) · ⚠️ dato de una sola fuente no oficial, inferido o con discrepancia · ❓ no verificado.

**Convenciones de este fichero**

- Las fichas usan los mismos campos que el §16 del informe. El slug `mp-…` reutiliza el existente cuando la ruta ya está en el informe. Las rutas nuevas llevan slug nuevo y la marca **[NUEVA]**.
- **"GPX calc."** = cifras calculadas por mí a partir del GPX descargado de Terranostrum: inicio y fin (primer y último punto del track), longitud (haversine) y D+ (suma de subidas con umbral de histéresis de 5 m). Sirven para contrastar, no son cifras oficiales. Si el track tiene altitudes ruidosas, el D+ sale inflado; lo marco cuando pasa.
- "Pág." = cifra que publica la propia página. Si "Pág." y "GPX calc." difieren mucho, se dan las dos.
- **Licencias.** Terranostrum (© de sus autores; cada ficha cita también a la entidad que aporta la información) y La Pedrera Pindia: **solo hechos** (cifras, coordenadas, topónimos). No se copian textos ni se redistribuyen sus GPX. Los itinerarios que siguen están **resumidos con mis palabras**. Palenciaturismo (Diputación de Palencia): mismo criterio, salvo los datos fácticos de sus fichas.
- Ficheros descargados (datos no fiables, solo para análisis) en el scratchpad de la sesión: libro y mapa en `/tmp/claude-0/-home-user-plantrail/96c9fb8a-15bd-5ae4-9d15-17b3fbd50d9f/scratchpad/dl_pt/`, páginas y GPX de Terranostrum en `/tmp/claude-0/-home-user-plantrail/96c9fb8a-15bd-5ae4-9d15-17b3fbd50d9f/scratchpad/dl_tn/`, y estadísticas de los GPX en `/tmp/claude-0/-home-user-plantrail/96c9fb8a-15bd-5ae4-9d15-17b3fbd50d9f/scratchpad/gpxstat.json`.

---

## 0. Resumen: qué huecos del informe se cierran

| Pendiente del informe | Resultado |
|---|---|
| 4 y 8. GPX y 24 rutas de lapedrerapindia.com | ❌ **Host inaccesible**: conexión reiniciada en HTTPS (`lapedrerapindia.com` y `www.`), dos reintentos con más de 30 s de separación. Sin datos nuevos (ver §1). |
| 11. Senda de La Pedrosa sin ficha | ✅ Resuelto: Barruelo de Santullán → Brañosera (ermita de San Roque), por el río Rubagón. Palenciaturismo: 9 km i/v, +150 m, 3 h 30, fácil. Terranostrum: 7,2 km i/v, 2 h, con GPX. Coordenadas de inicio en §3.1. |
| 14. Libro Montaña Palentina 2026 sin leer | ✅ Leído. Es un **catálogo fotográfico de 40 enclaves**, no una guía de rutas: no trae tracks, cifras ni horarios. Lo acompaña un mapa interactivo con un enlace de Google Maps por enclave (§2.1). |
| 15. GR-1: cifras oficiales por etapa y E6 | ✅ Palenciaturismo publica cifras por etapa (E1–E6, total 85,38 km, +2.652 / −2.094 m, "homologado: sí") y coordenadas de inicio y fin. E6 termina en el collado de la Cruz Armada (~1.621 m según el GPX). Ver §2.4. |
| 16. Cifras por etapa del Camino Natural del Románico; Camino Olvidado E5; Lebaniego | ✅ Terranostrum tiene el **Camino Natural del Románico Palentino** (bajo el slug engañoso "ruta-del-carbon-de-cok") en E1–E3 más la variante 2; el **Camino Olvidado E5–E7**; y el **Lebaniego Castellano E6–E11** con GPX. Ver §3.3–3.5. |
| 17. Rutas sin fuente | Parcial. **Quejigar de Hérmedes está en el Cerrato, no en la Montaña** (Hérmedes de Cerrato, 41,82 N): hay que sacarlo del dominio. Terranostrum **no tiene** Cascadas de Lebanza, Monte Bernorio a pie, Peña Redonda ni el Hayedo de Monte Ahedo (de Bernorio solo hay una vuelta BTT). Sí aparece la ruta minera de Barruelo (Calero de Brañosera, Ujapero–Cocoto). |
| 18. Discrepancias (Mazobre, Fuente Cobre, Pescadores, Tosande, Tuerces Amarilla y Azul) | ✅ Mazobre 6,6 km i/v (palenciaturismo, Terranostrum y plano coinciden; GPX 5,9). Fuente Cobre: palenciaturismo 13 km circular / +400; Terranostrum 11,6 km / +400 con vuelta alternativa (GPX cerrado = circular). Pescadores: palenciaturismo 6 km circular / +39; GPX 6,35. Tosande: palenciaturismo 10,5 km circular / +300; Terranostrum 10 km / +400; GPX 9,45 / ~430. **Tuerces Amarilla 8,3 km / 3 h 30 y Azul 9,2 km / 3 h 30**: confirmado en Terranostrum y en sus GPX (8,26 y 9,22 km). Las cinco rutas de colores son **lineales y terminan en Peña Mesa**. |
| 20. Coordenadas de trailheads | ✅ Nuevas: Triollo, Santa María de Redondo, Cervera, Aguilar, Barruelo, Revilla de Pomar, San Salvador de Cantamuda, Camporredondo, Salcedillo, Valberzoso, Mave, Gama, Villaescusa, Polentinos, Lores, Tremaya, Casavegas, Guardo, Muñeca… (por ficha). |
| 21. Refugios | Parcial. El GPX y la ficha de Terranostrum sitúan el **Refugio del Golobar en 42.96718, −4.33678**, a 1.775 m según la página ⚠️. Mazobre: la página cita un desvío al refugio hacia la mitad del camino, sin coordenada. |
| Otros avisos nuevos | **Cueva de los Franceses "cerrada temporalmente por obras"** según palenciaturismo (21-11-2026) ✅. |

---

## 1. La Pedrera Pindia (lapedrerapindia.com): inaccesible

- Intentos: `https://lapedrerapindia.com/rutas-montana-palentina/ascensiones/`, `…/Espiguete`, `https://www.lapedrerapindia.com/…` y la portada. Todos devolvieron *Connection reset by peer*. El proxy lo registró como `ws_closed_mid_exchange`: el túnel se cerró a mitad del intercambio. Primer intento hacia las 15:18; reintento pasados más de 60 s y un tercero (HTTP/1.1) más tarde, con el mismo resultado. Por HTTP plano no resuelve DNS: el proxy solo admite HTTPS. **Marcado como bloqueado o caído; no se insistió más.**
- Consecuencias:
  - No se pudo comprobar si las 16 URL de los QR de la guía siguen vivas.
  - No se listaron las 40 páginas.
  - No hay datos de las 24 rutas no libres (02, 04, 05, 07, 08, 10, 11, 13, 15, 17, 19–22, 25, 27, 28, 30, 32–35, 38 y 39).
  - Tampoco se revisó la sección BTT.
- Suplencia parcial desde Terranostrum, para cumbres de esas 24 rutas o próximas:
  - **Pico Lezna (ruta 27)**: Terranostrum "Lores – Pico Lezna" (ver `mp-lezna`).
  - **Monte Coriscao**, en la zona de la ruta 13 "Monte de Las Huelgas"? ❓ No consta que sea la misma cumbre.
  - **Peña Lampa (ruta 15)**: el Sabinar de Peña Lampa sube al cordal.
  - **Peña Abismo (ruta 30)**: solo como foto 33 del libro 2026.
  - **La Verdiana (ruta 33)**: solo fotos 6 y 34 del libro.
  - Del resto no hay nada.
- Cómo cerrarlo: revisión manual en navegador o contacto con la editorial, que sigue siendo titular del © de la guía.

---

## 2. Palenciaturismo.es (Diputación de Palencia)

### 2.1 Libro "Montaña Palentina. Coordenadas de Luz de un Territorio" (2026)

- **URL vigente**: el enlace del encargo (`/system/files/2026-05/…`) devuelve **403 "Acceso denegado"**. El fichero se ha movido a [2026-06, versión en español](https://palenciaturismo.es/system/files/2026-06/LIBRO%20MONTA%C3%91A%20PALENTINA%20%28versi%C3%B3n%20espa%C3%B1ol%29%20%281%29.pdf). También hay [versión en inglés](https://palenciaturismo.es/system/files/2026-06/LIBRO%20MONTAN%CC%83A%20PALENTINA%20%28versio%CC%81n%20Ingle%CC%81s%29.%20%281%29.pdf), [mapa interactivo](https://palenciaturismo.es/system/files/2026-06/MAPA%20MONTA%C3%91A%20PALENTINA%20%28formato%20interactivo%20digital%29%20INTERNET_0.pdf) y [nota de prensa](https://palenciaturismo.es/system/files/2026-06/NP_GUIA%20MONTA%C3%91A%20PALENTINA.pdf). La página que los agrupa es [Guía Exposición Fotográfica Montaña Palentina](https://palenciaturismo.es/visitar/lugares-interes/guia-exposicion-fotografica-montana-palentina), y también están en la [zona de descargas](https://palenciaturismo.es/guia-practica/zona-decargas) ✅.
- **Ficha técnica**:
  - Edita la Diputación de Palencia (Servicio de Turismo). Fotografías de Juan García Lucas ("Juan PIXELECTA").
  - Depósito legal P 30-2026. PDF de 31 páginas en pliegos dobles (56 páginas impresas).
  - Financiado por el Plan de Sostenibilidad Turística en Destino de la Montaña Palentina (NextGenerationEU) ✅.
  - Acompaña a una exposición que estuvo en el Auditorio de Guardo del 18-6 al 15-7-2026 (nota de prensa) ✅.
- **Contenido** (resumen propio):
  - Introducción, nota del autor y 40 fotografías con un pie de una o dos frases.
  - El propio libro aclara que **no es una guía técnica**: no hay tracks, análisis topográfico, horarios ni itinerarios completos, y las coordenadas y accesos "solo orientan".
  - Recuerda que el Parque Natural cumple 25 años y cita a la fotógrafa Piedad Isla.
  - **No aporta cifras de rutas.** Su valor para la app está en los nombres de enclaves fotogénicos, que pueden ser POI o miradores, y en algunos datos sueltos.
- **Datos de naturaleza y patrimonio que trae** (con confianza ⚠️ por ser texto divulgativo):
  - **Árbol rey de Tosande**: el tejo principal de la Tejeda supera los 1.200 años.
  - La Tejeda se presenta como una de las mejores concentraciones de tejos milenarios.
  - **Fuente del Cobre**: se presenta como nacimiento "oficial" del Pisuerga.
  - **Ojo de la Lastra**: arco natural de piedra al pie de Peña Santa Lucía. Coincide con el WP8 "El Ojo de la Lastra" de la ruta 14 de la Diputación.
  - **Ojo de Caloca o "el Bocarón"**: arco de roca desde el que se ve abajo el pueblo cántabro de Caloca. Es el destino de la ruta Terranostrum "Bocarón de Casavegas" (§3.2).
  - **Pozo Merino**: poza natural en la desembocadura del río Rubagón.
  - **Puente Rojadillo**: puente romano sobre el río Camesa (en el GR-1 E1).
  - **Ribero Pintado**: pared de estratos coloreados (ver §3.2).
  - **Mina de Carracedo**: brecha minera en un bosque. El libro advierte que no hay que asomarse.
  - **Lagos del Ves**: lagunas en la cara norte, entre el Hoya Contina y el Alto de la Curruquilla, cerca del Pozo Curavacas.
  - **Castros Negros**: roquedo con buitres.
  - **Pino Enroscao**: pino retorcido sobre sí mismo en el Pinar de Velilla.
  - **Roblón de Herreruela**: roble centenario. El libro lo cita junto al Roblón de Estalaya y el de los Jugaderos.
  - **Miradores**: Alto de la Varga (vista del Espigüete, hacia el Alto de la Miranda), Alba de los Cardaños ("posiblemente uno de los rincones más bellos del parque") y Peñalabra (el mejor mirador, a 1 km del pueblo de El Campo).
  - **Senda de los Rojos**: discurre por el límite con Cantabria. Según la ficha del [Mirador de Piedrasluengas](https://palenciaturismo.es/visitar/lugares-interes/mirador-piedrasluengas), sale desde ese mirador (43.04168, −4.45863).
  - **Altitudes que da el libro**: Curavacas 2.524, Espigüete 2.450, Fraile 2.001 y **Peñalabra 2.018** (el informe usa 2.029: discrepancia ⚠️).
- **Mapa interactivo**: un PDF de una sola página con 38 enlaces a `maps.app.goo.gl`, uno por enclave. Emparejé cada enlace con su rótulo por posición. No se pudieron resolver a coordenadas porque goo.gl no está entre los hosts permitidos ❓. Tabla para la app (slug relacionado = ruta del informe o de este fichero que pasa por el enclave):

| Nº | Enclave | Enlace del mapa | Slug relacionado |
|---|---|---|---|
| 1 | Pico Curavacas | https://maps.app.goo.gl/CPchniJD2Tz63XEY8 | mp-curavacas-vidrieros |
| 2 | Pico Espigüete | https://maps.app.goo.gl/tZayfZUGR4LJL81y6 | mp-espiguete-sur |
| 3 | Peña del Fraile | https://maps.app.goo.gl/gRiKc3zSynSsMuKb7 | mp-fraile / mp-dip-18 |
| 4 | Peña Redonda | https://maps.app.goo.gl/j5dX5HUN8ggdU7Ai6 | mp-pena-redonda |
| 5/32 | Peñalabra | https://maps.app.goo.gl/1M1nYGpkhjaPMVxN9 | mp-penalabra-tresmares |
| 6 | Sinclinal de la Verdiana | https://maps.app.goo.gl/EKea3EogTwnxed2S8 | mp-dip-33 |
| 7 | Peña Tremaya | https://maps.app.goo.gl/sZtojx7TTpU49Xjv8 | mp-tremaya |
| 8 | Ojo de la Lastra | sin rótulo emparejado (uno de: https://maps.app.goo.gl/13HADbYCigeJUpmZ9 · https://maps.app.goo.gl/i5oZX4zaqwWKtPDG7) ⚠️ | mp-dip-14 |
| 9 | Río Pisuerga | https://maps.app.goo.gl/qcCoA4SX7aciE7SB6 | — |
| 10 | Río Carrión | https://maps.app.goo.gl/ETiNcwHA8aosnTjW8 | — |
| 11 | Río Rubagón | https://maps.app.goo.gl/rRWcfG8eonYysJ7z9 | mp-of-pedrosa |
| 12 | Río Camesa | https://maps.app.goo.gl/LtrPM4DJdt3akFqk8 | mp-gr1-e1 |
| 13 | Valle de Pineda y Pozo de Fuentes Carrionas | https://maps.app.goo.gl/V7haWCTSddZ3j82G6 | mp-valle-pineda |
| 14 | Pozo de las Lomas | https://maps.app.goo.gl/kMqwgAydBDUzQ7Ln8 | mp-of-lomas |
| 15 | Agujas de Cardaño | https://maps.app.goo.gl/z2Qpdy5RRbV3pWZz9 | mp-of-lomas |
| 16 | Lagos del Ves | https://maps.app.goo.gl/pEqqjKRNFMS6x9377 | mp-circular-lagos |
| 17 | Fuente del Cobre | https://maps.app.goo.gl/vFTTDGNkbVJ3gVia6 | mp-of-fuente-cobre |
| 18 | Alto de la Miranda | https://maps.app.goo.gl/wqoQZiVwSmG55cHM7 | mp-gr1-e5 (valle de Miranda) ⚠️ |
| 19 | Ribero Pintado | https://maps.app.goo.gl/t7cEaD7vHaqVUeeJA | mp-ribero-pintado |
| 20 | Tejeda de Tosande | https://maps.app.goo.gl/Jh15UqWATKiGG3BJA | mp-of-tosande |
| 21 | Senda de los Rojos | https://maps.app.goo.gl/PBSgibjLBJw7a5iN7 | — (sin ficha) |
| 22 | Roblón de Herreruela | https://maps.app.goo.gl/4WtK824GkNSZZFsk7 | mp-gr1-e2 (pasa por Herreruela) ⚠️ |
| 23 | Pozo Merino | https://maps.app.goo.gl/4EABgjsSRrYvQrgG8 | — |
| 24 | Puente Rojadillo | https://maps.app.goo.gl/M5XKwKsiTAR4PiAb6 | mp-valberzoso-rojadillo / mp-gr1-e1 |
| 25 | Cascadas de Mazobre | https://maps.app.goo.gl/dCYpX5ez1bYbtPn68 | mp-of-mazobre |
| 26 | Castros Negros | https://maps.app.goo.gl/asRJidBKnMbUHj52A | ❓ |
| 27 | Camporredondo | https://maps.app.goo.gl/pRXNLxnJhGHh6ogE8 | mp-gr1-e5 |
| 28/40 | Alba de los Cardaños | https://maps.app.goo.gl/iMHGYyW82NDkgzse6 | — |
| 29 | Cara norte del Curavacas | https://maps.app.goo.gl/inUWEdWE8FX9fAgz6 | mp-pozo-curavacas-pineda |
| 30 | Espigüete desde el Alto de la Varga | https://maps.app.goo.gl/yS2sZYAYY4fsyc8w7 | — (mirador de carretera P-210) |
| 31 | Cara sur de Peña Redonda | sin rótulo emparejado (el otro de los dos enlaces del nº 8) ⚠️ | mp-pena-redonda |
| 33 | Peña Abismo | https://maps.app.goo.gl/6uQNtXQY9Fsa42eB7 | mp-dip-30 |
| 34 | La Verdiana | https://maps.app.goo.gl/jLGCSQrUXWRXX2kBA | mp-dip-33 |
| 35 | Pino Enroscao | https://maps.app.goo.gl/mX1YHaiz24EcSM5r9 | mp-of-pinar-velilla |
| 36 | Árbol Rey de Tosande | https://maps.app.goo.gl/s5jh7m4ddZ7Ls1aF9 | mp-of-tosande |
| 37 | Reflejos de Camporredondo | https://maps.app.goo.gl/sXsgRGV4ABjvKBbY7 | — |
| 38 | Ojo de Caloca (Bocarón) | https://maps.app.goo.gl/XqELXxqV36jCAJZVA | mp-bocaron-casavegas |
| 39 | Mina de Carracedo | https://maps.app.goo.gl/jqjsPQzMppWuyMkEA | ❓ |

Licencia: textos y fotos © Diputación de Palencia / Juan PIXELECTA. Para la app, solo los nombres de enclaves y el enlace ✅.

### 2.2 Fichas de rutas de palenciaturismo (Montaña Palentina)

Listado completo en [Rutas naturales](https://palenciaturismo.es/que-hacer/rutas-naturales), revisado en sus páginas 0–3. Las coordenadas son el marcador de inicio de cada ficha (`data-lat/lng`). Unas son de trailhead preciso y otras son centroides de pueblo ⚠️. Las cifras son las de la ficha ✅.

| Ficha | Km | D+ / D− | Tipo | Dific. | Tiempo | Homol. | Inicio (coord.) | Notas | Slug |
|---|---|---|---|---|---|---|---|---|---|
| [Cascada de Mazobre](https://palenciaturismo.es/que-hacer/rutas/cascada-mazobre) | 6,6 | 250/250 | i/v | Fácil | 2 h | Sí | Pino Llano, km 2,5 de la P-217 · 42.95100, −4.76174 | Mirador de madera a poco más de 3 km. Una senda corta baja a la base. Raquetas en invierno. Posible oso | mp-of-mazobre |
| [Senda de la Laguna de las Lomas](https://palenciaturismo.es/que-hacer/rutas/senda-laguna-lomas) | 12 | 640/640 | i/v | Moderada | 5 h | Sí | Cardaño de Arriba · 42.97079, −4.75741 | Desvío al Pico Murcia; puente sobre el arroyo; Majada de las Vacas con chozo en ruinas. Invierno: raquetas, crampones, piolet | mp-of-lomas |
| [Pinar de Velilla](https://palenciaturismo.es/que-hacer/rutas/pinar-velilla) | 3,5 | 150/150 | Circular | Fácil | 2 h | No | Poblado de Compuerto, a 2 km de Velilla por la P-210 · 42.85064, −4.83302 | Dos miradores con vista al Espigüete, Peña Lampa y la presa de Compuerto. Único pinar autóctono | mp-of-pinar-velilla |
| [Roblón de Estalaya](https://palenciaturismo.es/que-hacer/rutas/roblon-estalaya) | 4,6 | 125/125 | Circular | Fácil | 1 h 30 | Sí | Aparcamiento a ~2 km por la PP-2173 tras el puente de Requejada · 42.92422, −4.47202 | Roble albar de 17 m de alto y ~10,6 m de perímetro. Tramo final de fuerte pendiente | mp-of-roblon |
| [Senda del Bosque Fósil](https://palenciaturismo.es/que-hacer/rutas/senda-bosque-fosil) | 3 | 120/120 | (i/v o circular) | Fácil | 1 h | Sí | Aparcamiento a la entrada de Verdeña · 42.94307, −4.46424 | Tres miradores: Peña Celada, Bosque Fósil y La Pernía. Troncos de Sigillaria y Cordaites del Carbonífero. Balizada | mp-of-bosque-fosil |
| [Senda del Escultor Ursi](https://palenciaturismo.es/que-hacer/rutas/senda-escultor-ursi) | 11 | 300/300 | Circular | Moderada | 3 h 40 | Sí | Villabellaco (iglesia de San Pedro) · 42.89109, −4.31070 | Tres accesos: Villabellaco, Valle de Santullán y Santuario del Carmen. Miradores de Rulaya y La Solana. 30 esculturas. Folleto 2025 en PDF | mp-of-ursi |
| [Senda de Fuente Cobre](https://palenciaturismo.es/que-hacer/rutas/senda-fuente-cobre) | 13 | 400/400 | Circular | Moderada | 4 h 30 | Sí | Aparcamiento junto a una antigua mina de carbón, tras el puente del Lombatero · 42.99156, −4.42791 | Vuelta alternativa por el Collado de Pando. Nacimiento real en el Sel de la Fuente (2.139 m) | mp-of-fuente-cobre |
| [Senda del Gigante del Valle Estrecho](https://palenciaturismo.es/que-hacer/rutas/senda-gigante-valle-estrecho) | 4,4 | 113/113 | i/v | Fácil | 1 h | Sí | Ruta de los Pantanos, pasado Santibáñez de Resoba · 42.90541, −4.62797 | **El "Gigante" no es un árbol, es una leyenda.** Miradores de Peñalbilla (a 2 km) y Caldacio (panel con la leyenda). Peña Negra (1.445 m). Fuente Deshondonada | mp-of-gigante |
| [Senda del Oso](https://palenciaturismo.es/que-hacer/rutas/senda-oso) | 12,2 | 270/270 | Circular | Moderada | 4 h | Sí | Puente de San Roque, Cervera · 42.87235, −4.50293 | Arbejal, vallejo de Congosto, antigua cantera en Requejada, cimas de Peñas Negras | mp-of-oso |
| [Senda de los Pescadores](https://palenciaturismo.es/que-hacer/rutas/senda-pescadores) | 6 | 39/39 | Circular | Fácil | 3 h | No (SL) | Centro de Interpretación de la Trucha ("paraje del Soto"), Velilla · 42.82599, −4.84857 | ~3 km río arriba hasta el puente del Ahorcado y vuelta por la otra orilla. Ermita de la Virgen de Areños y **dos refugios de pescadores**. Riberas inundables en crecidas | mp-pescadores-velilla |
| [Tejeda de Tosande](https://palenciaturismo.es/que-hacer/rutas/tejeda-tosande) | 10,5 | 300/300 | Circular | Moderada | 3 h 30 | Sí | C-626, a ~6 km de Cervera hacia Guardo · 42.82557, −4.51688 | Tejos de hasta 1,5 m de diámetro, casi milenarios. Pasarelas y mallas de protección. Vuelta circular opcional | mp-of-tosande |
| [Bosque de La Pedrosa](https://palenciaturismo.es/que-hacer/rutas/bosque-pedrosa) | 9 | 150/150 | i/v | Fácil | 3 h 30 | No (PR) | Parque de La Pedrosa, Barruelo · 42.93411, −4.30461 ⚠️ (el marcador cae en Brañosera, no en Barruelo) | Río Rubagón con saltos de agua; robledal; llega a la ermita de San Roque en Brañosera. Admite BTT. Raquetas en invierno | mp-of-pedrosa |
| [Ruta del Ribero Pintado](https://palenciaturismo.es/que-hacer/rutas/ruta-ribero-pintado) | 6 | 107/11 | i/v | Fácil | — | No (SL) | Parking de Fuente Cobre, Sta. M.ª de Redondo · GPX: 42.99154, −4.42821 | Sin señalizar pero sin dificultad. Antigua explotación a cielo abierto. **GPX descargable** ([gpx](https://palenciaturismo.es/system/files/2020-06/santa-maria-de-redondo-ribero-pintado.gpx)) | mp-ribero-pintado |
| [Senda de las Doncellas del Hoyal](https://palenciaturismo.es/que-hacer/rutas/senda-doncellas-hoyal) | 11,97 | 364/364 | Circular | Fácil | 3 h 30 | No | Plaza de Muñeca (Guardo) · GPX: 42.79202, −4.80148 | Red municipal "Sendas de Leyenda" de Guardo. **GPX descargable** ([gpx](https://palenciaturismo.es/system/files/2022-10/senda-de-las-doncellas-del-hoyal_0.gpx)) | mp-doncellas-hoyal |
| [Monumento Natural de las Tuerces](https://palenciaturismo.es/que-hacer/rutas/monumento-natural-tuerces) | 5 | 200/200 | Circular | Fácil | 2 h | No (SL) | Parking a la entrada de Villaescusa de las Torres · 42.75741, −4.24754 | Subida al páramo hasta Peña Mesa; luego "perderse" por el laberinto y bajar al pueblo. Más de 50 ha. Declarado Monumento Natural "Laberinto de las Tuerces" | mp-tuerces-villaescusa [NUEVA] |
| [GR-1](https://palenciaturismo.es/que-hacer/rutas/gr1) | 85,38 | 2.652/2.094 | Travesía | Moderada | — | Sí | Salcedillo → Alto de la Cruz Armada | Ver §2.4 | mp-gr1-e1…e6 |
| [Ruta de los Pantanos](https://palenciaturismo.es/que-hacer/rutas/ruta-pantanos) | 81 | — | Carretera (coche, moto, bici) | — | — | No | P-210 / CL-626 / CL-627 | Embalses de Aguilar (247 hm³, 1963), Requejada (95 hm³, 1940), Ruesga (el más pequeño, 1923, para el Canal de Castilla), Camporredondo (1930) y Compuerto (95 hm³, 1960). Miradores del Alto de la Varga y Alba de los Cardaños. No señalizada | (ruta escénica, no senderista) |
| [Quejigar de Hérmedes](https://palenciaturismo.es/que-hacer/rutas/quejigar-hermedes) | 2,9 | — | Circuito | Fácil | 1 h | No | Hérmedes de Cerrato · 41.82003, −4.17598 | **Está en el Cerrato, FUERA del dominio** ✅. Ornitológica, con GPX | mp-quejigar-hermedes → 🟪 FUERA |

Otras fichas del listado que no son de la Montaña: Canal de Castilla, Monte Vertavillo, Humedales esteparios y Verde Tren Burra. "Pedaleando por el Románico" ya está en el informe.

**Folletos enlazados** desde las fichas (no se leyeron, excepto el de Barruelo):

- `1-SendaMazobre.pdf`, `2-SendaLagunaLomas.pdf`, `3-PinarVelilla.pdf`, `4-Senda-pescadores_0.pdf`, `5-Senda-Roblón_0.pdf`, `6-SendaDelOso.pdf`, `8-SendaFuenteCobre.pdf`, `9-TejedaTosande.pdf`, `SendaBosqueFósil.pdf`, `Senda del Gigante del valle Estrecho.pdf`, `Relación de esculturas.pdf` (Ursi) y `FOLLETO Senda del escultor Ursi-20250621.pdf`. Todos en `https://palenciaturismo.es/system/files/2019-08/…` o `/2025-12/`.
- [sendas_de_barruelo.pdf](https://palenciaturismo.es/system/files/2019-08/sendas_de_barruelo.pdf) (2,4 MB): **escaneado, sin capa de texto**, y no hay OCR en el entorno ❓.

Lugares de interés con coordenadas útiles ✅:

- [Mirador de Piedrasluengas](https://palenciaturismo.es/visitar/lugares-interes/mirador-piedrasluengas): 43.04168, −4.45863.
- [Casa del Parque](https://palenciaturismo.es/visitar/lugares-interes/casa-parque-natural-montana-palentina) (Cervera): 42.86314, −4.49554. Exposición "Zona Oso"; enlaza el horario 2026 de patrimonionatural.org.
- [Cueva de los Franceses](https://palenciaturismo.es/visitar/lugares-interes/cueva-franceses): 42.77255, −4.11672. **Cerrada temporalmente por obras.** Abierta al turismo desde 1974; acceso por un túnel artificial; la sima original de 6 m está clausurada.
- [Reserva del Bisonte Europeo](https://palenciaturismo.es/visitar/lugares-interes/reserva-bisonte-europeo-bison-bonasus) (San Cebrián de Mudá): 42.89728, −4.38597. Visita siempre guiada, 2 h, a 2 km del centro de interpretación.

### 2.3 Quejigar de Hérmedes

Se cierra el ❓ del informe. Es una ruta ornitológica en Hérmedes de Cerrato (área recreativa del arroyo de San Juan; páramo; monte de quejigos de La Dehesa): 2,9 km, 1 h, fácil, con GPX. **Fuera de la Montaña Palentina** (Cerrato) ✅. Propuesta: retirar `mp-quejigar-hermedes` o marcarla 🟪.

### 2.4 GR-1 por etapas (cifras oficiales de palenciaturismo frente a Terranostrum)

Fuente principal: las [fichas de etapa de palenciaturismo](https://palenciaturismo.es/que-hacer/rutas/gr1) ✅. Las coordenadas son los marcadores de inicio y fin; parecen centroides de pueblo ⚠️.

| Slug | Etapa (palenciaturismo) | Km | D+ / D− | Dific. | Inicio → fin (coord.) | Terranostrum (pág.) | GPX calc. (Terranostrum) |
|---|---|---|---|---|---|---|---|
| mp-gr1-e1 | [E1 Salcedillo – Brañosera](https://palenciaturismo.es/que-hacer/etapas/etapa-1-gr1-salcedillo-branosera) | 8,0 | 430/200 | — | 42.94084, −4.27340 → 42.93680, −4.30836 | [E1 "Cantabria – Brañosera"](https://www.terranostrum.es/senderismo/palencia/montana-palentina/gr-1-palencia-etapa-1-cantabria-branosera): 8,1 km, 2 h 30, +430/−200, media. Salida en Mata de Hoz; los primeros 2,4 km son en Cantabria | 8,1 km / +319 / 1.058–1.375 m; inicio 42.93557, −4.24144 (puente Rojadillo) |
| mp-gr1-e2 | [E2 Brañosera – Estalaya](https://palenciaturismo.es/que-hacer/etapas/etapa-2-gr1-branosera-estalaya) | 23,5 | 660/800 | Moderada | 42.93680, −4.30836 → 42.92768, −4.47515 | 24,3 km, 7 h 30, +660/−800, media | 24,3 km / +710 / máx. 1.619 m |
| mp-gr1-e3 | [E3 Estalaya – Cervera](https://palenciaturismo.es/que-hacer/etapas/etapa-3-gr1-estalaya-cervera-pisuerga) | 11,5 | 170/250 | Moderada | 42.92768, −4.47515 → 42.86689, −4.49929 | 10,6 km, 3 h, +170/−250 | 11,1 km / +139 / máx. 1.161 m |
| mp-gr1-e4 | [E4 Cervera – Triollo](https://palenciaturismo.es/que-hacer/etapas/etapa-4-gr1-cervera-pisuerga-triollo) | 23,0 | 540/300 | Moderada | 42.86689, −4.49929 → 42.92464, −4.68056 | 22,4 km, 6 h 40, +574/−275 | 22,35 km / +577 / máx. 1.432 m |
| mp-gr1-e5 | [E5 Triollo – Camporredondo](https://palenciaturismo.es/que-hacer/etapas/etapa-5-gr1-triollo-camporredondo-alba) | 10,7 | 140/200 | Moderada | 42.92464, −4.68056 → 42.89521, −4.74651 | 10,5 km, 3 h, +140/−200 | 10,5 km / +153 / máx. 1.407 m |
| mp-gr1-e6 | [E6 Camporredondo – Alto de la Cruz Armada](https://palenciaturismo.es/que-hacer/etapas/etapa-6-gr1-camporredondo-alba-alto-cruz-armada) | — (no figura) | — | — | 42.89521, −4.74651 → 42.93095, −4.80978 | 9 km, 2 h 45, +430/−100, media | 9,0 km / +486 / **máx. 1.621 m** (collado); fin 42.92916, −4.81033 |

Notas por etapa (resumen propio):

- **Total** según palenciaturismo: 85,38 km, +2.652 / −2.094 m, moderada, "homologado: sí". La ficha general habla de "unos 85 km". El GPX completo de Terranostrum da 85,2 km / ~2.380 m. El informe decía 87 km ⚠️.
- **Temporada**: de marzo a principios de noviembre. Todo el itinerario admite BTT, con variantes señalizadas para los tramos de sendero. Hay que respetar las restricciones temporales por oso ✅.
- **E1**: remonta el río Camesa desde Mata de Hoz (Valdeolea, Cantabria) y entra en Palencia por una portilla. Pasa el puente romano de Rojadillo, cruza el bosque del Monte Mayor y llega al Alto de los Grullos. Tiene variantes a Valberzoso y a Salcedillo. Baja a Brañosera por pista de solana hasta la capilla de San Miguel.
- **E2**: Senda de La Pedrosa hasta Barruelo (puente de madera en las piscinas, El Helechar). Sube a la mina del Calero y continúa por una ancha pista minera en ascenso largo. Baja a Herreruela de Castillería (ermita de N.ª S.ª del Monte) y a San Felices. Termina en el aparcamiento de la Senda del Roblón, a 500 m de Estalaya.
- **E3**: Vañes; borde del embalse de Requejada; antigua cantera de la presa. Enlaza con la Senda del Oso, pasa el portillo de El Collao y llega a Arbejal (mirador) y a Cervera.
- **E4**: Cervera (iglesia de Santa María del Castillo) → Ruesga → orilla derecha del embalse de Ruesga (playas fluviales, áreas recreativas, pinar) → Ventanilla → antiguo camino a San Martín de los Herreros (puente de piedra de dos ojos) → Rebanal de las Llantas → La Lastra → Triollo.
- **E5**: pista por la vega del Carrión con vistas al embalse de Camporredondo y al Curavacas. Remonta el valle de Miranda, cruza una pasarela de madera y sube una rampa de casi 1 km hasta Camporredondo.
- **E6**: camino de Valdegullas (sale encima del cementerio), con fuerte subida inicial. Deja a un lado el desvío al Coriscao y cruza la pradera de Valdegullas. Recibe el ramal de Cardaño de Abajo y termina con una rampa recta hasta el collado de la Cruz Armada (1.632 m) y la senda hacia Valverde de la Sierra (León).
- Licencia: cifras de la Diputación (hechos) · GPX de Terranostrum (enlazar) · ✅ cifras · ⚠️ coordenadas de pueblo.

---

## 3. Terranostrum.es

- **Listado** "[Senderismo · Montaña Palentina](https://www.terranostrum.es/senderismo/palencia/montana-palentina/1)": 10 páginas paginadas, **115 fichas**. La URL `/senderismo/palencia/montana-palentina` sin número da 404.
- **GPX**: 111 fichas tienen GPX descargable, en `https://www.terranostrum.es/images/Tracks/…`. Algunas fichas de etapa enlazan dos GPX: el de la etapa y el del recorrido completo.
- **Sin GPX**: El Pinar de Peña Mayor, Senda del Pinar de Velilla, La Escalera del Tiempo y la ficha general de Las Tuerces.
- Cada ficha da: distancia, tiempo, a veces desnivel, punto de salida, ciclabilidad, dificultad, época, puntos de mapa (nombre + coordenadas) y la entidad que facilita la información ("Información: …").
- **Licencia**: textos, fotos y GPX © Terranostrum o de la entidad citada. **Enlazar; usar solo hechos.**

**No existen en Terranostrum** (búsqueda en las 115 fichas):

- Cascadas de Lebanza, Monte Bernorio a pie (solo la vuelta BTT), Peña Redonda, Hayedo de Monte Ahedo / Valcabado.
- Cascada de Atría, Senda del Agua, Ruta de los Molinos y Pozo Oscuro (este último solo se menciona en el texto del Pozo Curavacas).
- Tres Mares, Peña Labra, Curavacas, Peña Prieta.

### 3.1 Rutas que ya están en el informe: datos nuevos

#### mp-tuerces-roja · Las Tuerces, Ruta Roja
- **Zona / municipio · Provincia:** Aguilar de Campoo (Mave – Villaescusa de las Torres), Monumento Natural de Las Tuerces · Palencia.
- **Tipo · Distancia · D+ / D− · Alt. · Tiempo · Dificultad:** **lineal**, de Mave a Peña Mesa ✅ · 5,6 km (GPX calc. 5,55) · GPX calc. +248 m · 883–1.062 m · 2 h · baja. No ciclable.
- **Inicio · Fin:** cartel de rutas de Mave, cerca de la carretera a Santa María de Mave, 42.73644, −4.27328 (GPX) ✅ · fin en la explanada de Peña Mesa, 42.75402, −4.25722.
- **Temporada · Riesgos / avisos:** todo el año. Tramo junto al borde del cañón (cuidado con niños). Subir a Peña Mesa con los clavos es posible, pero **bajar es delicado**.
- **Agua · Refugios:** agua en Mave y en el manantial potable junto al cartel de Villaescusa (cruce de las rutas roja, verde y amarilla).
- **Waypoints clave:** Mave 42.73673, −4.27395 · Villaescusa 42.75905, −4.25290 · Peña Mesa 42.75393, −4.25726 (puntos de mapa de Terranostrum).
- **Descripción:** se cruza Mave siguiendo marcas rojas y una pista de chopos hasta la antigua harinera de La Horadada (privada; se rodea por arriba; hay vías de escalada). Una senda tallada en la roca sube al túnel de La Horadada, con vista del cañón del Pisuerga, y sale a la meseta. Se bordea el cañón por arriba, se baja a Villaescusa y se sube fuerte al laberinto de Las Tuerces hasta Peña Mesa.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/las-tuerces-ruta-roja) · [GPX](https://www.terranostrum.es/images/Tracks/TU/ruta-roja-monumento-natural-de-las-tuerces.gpx).
- **Licencia · Confianza · Pendiente:** Terranostrum / Ayto. de Aguilar (enlazar) · ✅ · Pendiente: confirmar si el balizado sigue en buen estado.

#### mp-tuerces-amarilla · Las Tuerces, Ruta Amarilla
- **Tipo · Distancia · D+ · Alt. · Tiempo · Dificultad:** lineal, Mave → Olleros → Villaescusa → Peña Mesa · **8,3 km** (GPX calc. 8,26) ✅ · GPX calc. +336 m · 872–1.062 m · **3 h 30** ✅ · baja. Se confirman las cifras dudosas del informe.
- **Inicio · Fin:** Mave 42.73542, −4.27509 (GPX) · Peña Mesa 42.75402, −4.25725.
- **Riesgos / avisos:** tramo intermedio **sin senda y laberíntico**: atención a las marcas. Senda de pescadores estrecha junto al río, con un paso por una roca pulida que entra en el agua. Paso a nivel con muy poca visibilidad antes de Villaescusa.
- **Waypoints clave:** Olleros (iglesia rupestre de los Santos Justo y Pastor) 42.74454, −4.28612 · Monte Cildá (castro cántabro-romano) 42.75140, −4.27740 · Villaescusa 42.75803, −4.25014.
- **Descripción:** carretera hasta Olleros; sendero incómodo junto al cementerio hasta enlazar con una pista que sube al Monte Cildá. Borde alto del cañón de La Horadada; descenso a la parte superior de los túneles del ferrocarril; chopera (lugar para comer); senda de pescadores junto al río; puente a Villaescusa. Termina con la subida a Peña Mesa.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/las-tuerces-ruta-amarilla).
- **Licencia · Confianza:** enlazar · ✅.

#### mp-tuerces-verde · Las Tuerces, Ruta Verde
- **Tipo · Distancia · D+ · Alt. · Tiempo · Dificultad:** lineal, Aguilar → Villaescusa → Peña Mesa · 7,3 km (GPX 7,24) · GPX calc. +183 m · 883–1.069 m · 2 h · baja. **Ciclable** ✅.
- **Inicio · Fin:** zona deportiva de Aguilar de Campoo (cartel), 42.78994, −4.25874 ✅ · Peña Mesa 42.75398, −4.25719.
- **Avisos:** zona árida entre tierras de labor; mismo paso a nivel peligroso.
- **Descripción:** pasarela peatonal sobre el río y choperas paralelas al Pisuerga; se pasa bajo la nacional. A la altura de la presa de la piscifactoría se separa del río. Puente a Villaescusa. En lugar de subir directo, sigue la pista por la base de las paredes, entra en un cañón y sube a la meseta, donde se une con la ruta rosa hasta Peña Mesa.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/las-tuerces-ruta-verde). **Confianza:** ✅.

#### mp-tuerces-rosa · Las Tuerces, Ruta Rosa
- **Tipo · Distancia · D+ · Alt. · Tiempo · Dificultad:** lineal, Gama → castillo → cortafuegos del pinar → Peña Mesa · 6,9 km (GPX 6,89) · GPX calc. +180 m · 953–1.086 m · 2 h · baja.
- **Inicio · Fin:** cartel de Gama, 42.74776, −4.20809 ✅ · Peña Mesa 42.75399, −4.25717.
- **Agua:** **no hay manantiales en la meseta**; hay que llevar agua.
- **Waypoints:** castillo de Gama (ruinas medievales, gran panorámica) 42.74549, −4.20848.
- **Descripción:** senda en revueltas hasta el castillo; detrás, una pista sube y luego llanea por el cortafuegos del borde sur del pinar de repoblación, con cruces señalizados. A mitad comparte unos cientos de metros con la azul, que permite volver a Gama por el "camino viejo". Al final del pinar se une con la verde.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/las-tuerces-ruta-rosa). **Confianza:** ✅.

#### mp-tuerces-azul · Las Tuerces, Ruta Azul
- **Zona / provincia:** Mave – La Rebolleda (🟪 enclave de Burgos) – Villacibio – Gama. Comarcas Montaña Palentina y Sedano y las Loras.
- **Tipo · Distancia · D+ · Alt. · Tiempo · Dificultad:** lineal, Mave → Gama · **9,2 km** (GPX 9,22) ✅ · GPX calc. +231 m · 887–1.069 m · **3 h 30** ✅ · baja.
- **Inicio · Fin:** Mave 42.73563, −4.27225 · Gama 42.74775, −4.20811.
- **Avisos:** tramos poco definidos (marcas en estacas y árboles); senda que a veces se pierde; subida final a la meseta por una quebrada sin trepada. **Sin agua** salvo en los pueblos.
- **Waypoints:** La Rebolleda 42.73184, −4.25667 · ermita rupestre de San Pelayo (Villacibio) · portillo de Villacibio · arroyo de Pradillos (valle de Valseca).
- **Descripción:** pista hacia el este y monte bajo hasta La Rebolleda. Senda hasta las rocas de la ermita rupestre de San Pelayo; carretera unos 400 m; portillo de Villacibio. Bajada al arroyo de Pradillos y subida a la meseta entre encinas. Pistas del pinar y bajada a Gama por un cañón bajo el castillo.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/las-tuerces-ruta-azul). **Confianza:** ✅ (la ficha general dice "de 6 a 10 km, de 2 a 4 h").

#### mp-tuerces-villaescusa · Las Tuerces, circular corta desde Villaescusa (palenciaturismo) [NUEVA]
- 5 km circular · +200/−200 · 2 h · fácil · SL no homologado · todo el año (nieve posible) ✅.
- Inicio: parking a la entrada de Villaescusa de las Torres, 42.75741, −4.24754 ✅. Panel interpretativo al salir del pueblo hacia el páramo.
- Descripción: subida por la ladera al páramo, Peña Mesa ("roca en forma de seta") y libertad para recorrer el laberinto antes de bajar al pueblo por cualquier senda. Requiere algo de orientación.
- Fauna citada: buitre, águila real, halcón peregrino; anfibios en los callejones húmedos; trucha en la Horadada.
- [palenciaturismo](https://palenciaturismo.es/que-hacer/rutas/monumento-natural-tuerces) · Geoparque: "La Escalera del Tiempo" (2 km, 1 h, desde Villaescusa; [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/la-escalera-del-tiempo), sin GPX). Es un itinerario geológico que va del medio fluvial al marino.

#### mp-covalagua-corta · Cascada de Covalagua desde Revilla de Pomar
- **Tipo · Distancia · D+ · Alt. · Tiempo · Dificultad:** **circular** señalizada · 5,2 km (GPX 5,04) · pág. 90 m (GPX calc. 94) · 994–1.084 m · 2 h · baja. No ciclable ✅.
- **Inicio · Fin:** junto a la iglesia de Revilla de Pomar, 42.77071, −4.15124 (GPX, circular cerrado) ✅.
- **Waypoints:** cascada de Covalagua 42.77036, −4.12876 ✅.
- **Descripción:** se baja al fondo del valle, se cruza un puente de madera y se remonta el río Ibia. A unos 2 km se pasa una balsa y se llega a la cascada, una surgencia kárstica. La vuelta sigue la pasarela hasta la cueva de Covalagua y continúa por senda y pista hasta la carretera de Revilla, o se vuelve por el mismo camino.
- **Avisos:** caudal muy variable (ver informe).
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cascada-de-covalagua). **Confianza:** ✅.

#### mp-covalagua-integral · Integral del Espacio Natural de Covalagua
- Circular · 19,7 km (GPX 19,75) · pág. 270 m; **GPX calc. +480 m** ⚠️ · 956–1.226 m · 5 h · media · primavera y otoño.
- Inicio: Revilla de Pomar 42.77094, −4.15180 (GPX, cerrado).
- Waypoints: cascada 42.77039, −4.12870 (salto de 20 m) · menhir de Canto Hito 42.76253, −4.11160 · Pozo de los Lobos 42.77374, −4.09390.
- Descripción: cascada → Cueva de los Franceses (500 m visitables; **ahora cerrada por obras**) → menhir de Canto Hito y vuelta sobre los pasos → Pozo de los Lobos (antigua trampa) → pista de regreso a Revilla.
- [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/integral-espacio-natural-de-covalagua) · ✅ / ⚠️ D+.

#### mp-franceses-lobos · Cueva de los Franceses – Mirador de Valcabado – Pozo de los Lobos
- i/v · 6,2 km (GPX de ida 3,14) · pág. 72 m · 1.125–1.219 m · 2 h · baja · ciclable al 90%.
- Inicio: inmediaciones de la Cueva de los Franceses, 42.77212, −4.11582 (GPX) ✅.
- Waypoints: Cueva de los Franceses 42.77306, −4.11672 · **Mirador de Valcabado 42.78185, −4.10251** · **Pozo de los Lobos 42.77353, −4.09419** ✅. Afina el ⚠️ del informe (42.7737, −4.0939).
- Descripción: pista llana de 1,5 km hasta el mirador. Desde su aparcamiento, senda al sureste paralela al cortado unos 830 m. Escalones calizos y, a unos 400 m, un pequeño cortado que da a la ladera de Valderredible, donde está el pozo. La ficha explica cómo se usaba la trampa: batida con ruido hacia el embudo de muros.
- Información: Agrupación Comarcal de Desarrollo Montaña Palentina · [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cueva-de-los-franceses-pozo-de-los-lobos) · ✅.

#### mp-pozo-curavacas-pineda · El Valle de Pineda y el Pozo Curavacas (también sirve para mp-valle-pineda)
- **Tipo · Distancia · D+ · Alt. · Tiempo · Dificultad:** lineal · **19 km solo ida** (GPX 18,98) · pág. 500 m (GPX calc. +487) · 1.327–1.785 m · 6 h 30 (ida) · **alta por longitud**. No ciclable según la ficha (el informe recoge un uso BTT parcial).
- **Inicio · Fin:** Vidrieros 42.94177, −4.66229 · **Pozo Curavacas 42.99035, −4.68658** (punto de mapa) ✅.
- **Temporada · Riesgos:** todo el año, pero el invierno exige preparación. Dos vados del Carrión. Sin servicios. La ficha sugiere vivac (ojo: el PORN prohíbe acampar, ver informe §11).
- **Agua · Refugios:** Santa Marina, junto a la confluencia con el arroyo de Arauz (el informe tiene allí el refugio de Santa Marina sin coordenadas) ⚠️.
- **Waypoints:** puente Pucherín · Santa Marina · Llanos de la Vega de Correcaballos · El Estrecho (entre el Lezna y el Curavacas) · Vega los Cantos · **Escaleras del Ves** (cascadas del arroyo del Ves) · Pozo Curavacas. Alternativas: Pozo del Ves, Pozo Oscuro, laguna de Fuentes Carrionas.
- **Descripción:** pista por el valle de Pineda junto al Carrión: primero al este; tras el puente Pucherín, al norte hasta Santa Marina; luego al noroeste por llanos despoblados. En Vega los Cantos llega el arroyo del Ves en cascadas; una senda junto a ellas sube al lago glaciar del Pozo Curavacas. También se puede seguir la pista, que cruza el río más arriba.
- **Fauna:** oso, lobo, rebeco, tritón alpino y rana bermeja en el pozo; topillo nival.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/el-valle-de-pineda-y-el-pozo-curavacas). **Confianza:** ✅ cifras / ⚠️ refugio.

#### mp-of-mazobre · Senda de la Cascada de Mazobre (datos complementarios)
- Cifras coincidentes: **6,6 km i/v · +250 · 2 h · baja** (Terranostrum y palenciaturismo) ✅. GPX calc. 5,86 km / +276 / 1.343–1.613 m. Inicio GPX 42.95120, −4.76168 (coincide con la ficha oficial).
- **Cascada (punto de mapa Terranostrum): 42.95927, −4.79282** ⚠️. Ojo: está a ~2,6 km en línea recta del inicio, y el GPX de la senda llega solo a 1.613 m. Puede que el punto marque la cascada superior o la bifurcación hacia el Murcia. Contrastar.
- Hacia la mitad, un desvío a la izquierda lleva al **refugio** (sin coordenadas). El arroyo puede ir seco en tramos por filtración caliza, pero la cascada lleva agua casi todo el año. Siguiendo el arroyo por una senda de ganado hay más cascadas menores (= variante circular del informe).
- Enlaces: [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/senda-de-la-cascada-de-manzobre) (con GPX) · [palenciaturismo](https://palenciaturismo.es/que-hacer/rutas/cascada-mazobre).

#### mp-of-fuente-cobre · Senda de Fuente Cobre (datos complementarios)
- Terranostrum: 11,6 km i/v (o vuelta alternativa) · +400 · 4 h 30 · baja. Palenciaturismo: **13 km circular** · +400 · 4 h 30 · moderada · homologada ✅. GPX calc. 11,61 km / +440 / **1.224–1.604 m**; el track es circular (fin a 3 m del inicio).
- Inicio: 42.99156, −4.42803 (GPX), en la línea de la ficha oficial ✅. **Cueva del Cobre (punto de mapa): 42.98691, −4.37307** ⚠️. Otra ficha la sitúa en 42.98732, −4.37233; diferencia ~80 m.
- Itinerario: puente sobre el Lombatero; pista junto a la escombrera de la mina; puente sobre el Pisuerga; tercer puente; bifurcación con señal de acceso restringido (por la derecha, a la ida). Confluencia con el arroyo de Tejedo; senda por el fondo del valle bajo hayas, acebos y abedules; pequeñas cascadas; la cueva bajo farallones calizos. Vuelta por una senda de ladera con vista de Peña Labra, una majada y un robledal.
- Hidrología: las aguas se sumen en el **Sel de la Fuente o Covarrés** (cara norte del Valdecebollas) y resurgen en la cueva, a ~1 km en línea recta y algo más de 150 m más abajo.
- Avisos: nieve y agua en invierno y al inicio de la primavera.
- Enlaces: [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/la-fuente-del-cobre) · [palenciaturismo](https://palenciaturismo.es/que-hacer/rutas/senda-fuente-cobre). **Pendiente resuelto:** es circular.

#### mp-valdecebollas-branosera · Valdecebollas y El Cueto (Golobar → Valdecebollas → Brañosera)
- Lineal o semicircular · 13 km (GPX 13,15) · desde el Golobar +300 hasta la cima y −940 hasta Brañosera (pág.); GPX calc. +969 recorrido en sentido inverso (Brañosera → Golobar) · 1.183–2.138 m · 4 h 30 · baja o media.
- Inicio: Refugio de El Golobar 42.96736, −4.33682, donde termina la carretera, o Brañosera 42.93659, −4.31027 (GPX).
- Descripción: senda junto al arroyo del Canal hasta el collado entre el Rubagón y el Pisuerga. Cordal al Alto Canalejas (2.096) y al Valdecebollas (2.139; plataforma con hitos y vértice). Bajada al suroeste a El Cueto (2.083) y al collado de Pamporquero. Pista al este por el valle de Pamporquero; a media ladera se elige Barruelo (hayedo-robledal) o Brañosera (siguiendo la línea de alta tensión).
- [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/valdecebollas-y-el-cueto) · ✅.

#### mp-valdecebollas-golobar · y nueva variante mp-golobar-sel-fuente-cobre [NUEVA]: Golobar – Collado de Canaleja – Sel de la Fuente – Fuente Cobre
- Circular · 11,3 km · pág. "+525 m"; **GPX calc. +862 m** ⚠️ · 1.610–2.135 m · 5 h · baja-media.
- Inicio: **Refugio de El Golobar 42.96718, −4.33678**, a 1.775 m (pág.) ✅/⚠️.
- Waypoints: Collado de Canaleja (2.033 m) · Sel de la Fuente (sumidero) · Fuente del Cobre 42.98732, −4.37233.
- Descripción: acceso montañero a la Fuente del Cobre desde la cabecera del Rubagón. Sube al collado de Canaleja, con vistas a La Pernía y los Picos de Europa; cerca queda el Valdecebollas. Baja al circo glaciar del Sel de la Fuente, donde se pierden las aguas, y a la resurgencia. El track también pasa por la cima (2.135 m).
- Notas: piso subalpino (enebro rastrero, arándano); túmulos megalíticos de unos 5.000 años; Valdecebollas = "El Torreón" (vértice de primer orden).
- [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-golobar-valdecebollas-sel-de-la-fuente) · ✅ trazado / ⚠️ D+.

#### mp-tremaya · Peña Tremaya (1.437 m) desde Tremaya
- Semicircular · pág. 4,7 km; GPX calc. 6,87 km / +301 · 1.126–1.424 m · 1 h 30 · baja.
- Inicio: puente sobre el Pisuerga 200 m antes de Tremaya (PP-2176, la carretera de Fuente del Cobre), 42.97937, −4.46532 ✅. Final en el molino de Sopeña, a ~1 km por carretera.
- Waypoints: cumbre 42.97739, −4.47976 (caseta de vigilancia de incendios de la Junta y antenas).
- Descripción: camino hacia el sur con un paso canadiense (portezuela con cadena). Meseta con casa de campo; portilla ganadera; senda que rodea la peña hasta la cumbre. La bajada rodea la peña al revés. Si uno se sale del trazado, hay aulagas.
- Avisos: deja las portillas como las encuentres.
- [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/pena-tremaya) · ✅.

#### mp-of-venganza-conde · Senda de la Venganza del Conde (San Salvador de Cantamuda)
- **Inicio:** junto a la colegiata románica y el puente medieval de San Salvador de Cantamuda, 42.96686, −4.49547 ✅. Cierra el hueco de coordenadas del informe.
- **Cifras:** circular · 7,7 km (GPX "_1" 7,66 km / +323; otro GPX de 9,55 km / +641 incluye la cumbre) · 1.102–1.424 m · 2 h 30 · baja.
- **Waypoints:** robledal de Matacastillo · supuesto emplazamiento del castillo del Conde Munio · **Mirador de la Leyenda** (escultura de doña Elvira, la criada sordomuda y la mula) · cumbre opcional de Peña Tremaya 42.97739, −4.48015 (último tramo más empinado y **sin señalizar**) · Estrecho de San Roque · Collaín de la Corte · calero · embotelladora "Fuentes de Lebanza" · paso subterráneo bajo la carretera.
- **Avisos:** posible hielo y nieve en la ladera norte en invierno y al inicio de la primavera.
- **Descripción:** cruza la CL-627 en Venta Campa, sube entre prados y robledal, bordea las calizas y recorre la cara norte hasta el mirador, con vista de Areños, Los Llazos, el valle de los Redondos y Peña Sagra. Retrocede 450 m y baja entre escobas al Estrecho de San Roque y por pista a San Salvador.
- Información: Ayto. de La Pernía · [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/senda-la-venganza-del-conde) · ✅.

#### mp-of-pedrosa · Senda de La Pedrosa (Barruelo – Brañosera)
- **Inicio · Fin:** barrio de San Pedro, Barruelo de Santullán (cartel), **42.91139, −4.28831** (GPX) ✅ · ermita de San Roque, Brañosera, ~42.9353, −4.3077.
- **Cifras:** Terranostrum 7,2 km i/v, 2 h, baja, ciclable; GPX de ida 3,72 km / +171 / 1.048–1.211 m. Palenciaturismo 9 km i/v, +150, 3 h 30, fácil, PR no homologado ✅.
- **Itinerario:** señalizado, por el bosque de La Pedrosa junto al Rubagón y paralelo a la carretera. Si uno se pierde, río abajo. Acceso alternativo desde la carretera por la senda de la Fuente de la Flor; enlace con la ruta del Calero de Brañosera. Coincide con el GR-1 E2 en sentido inverso.
- **Agua:** varios manantiales y la **Fuente de la Flor**, de agua apreciada (sin control sanitario ⚠️).
- **Temporada:** la nieve cubre La Pedrosa en invierno.
- **Enlaces:** [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/senda-de-la-pedrosa) · [palenciaturismo](https://palenciaturismo.es/que-hacer/rutas/bosque-pedrosa) · **Licencia:** Ayto. de Barruelo / Terranostrum (enlazar) · ✅.

#### mp-triollo-hornamiel · Triollo – La Lastra – Hornamiel
- **Tipo · Distancia · D+ · Alt. · Tiempo · Dificultad:** circular · 9,7 km (GPX 9,7) · pág. 284 m (GPX calc. +375) · 1.274–1.450 m · 2 h 45 · baja. No ciclable ✅.
- **Inicio:** puente del Carrión en Triollo, 42.92303, −4.67943 (GPX) ✅.
- **Waypoints:** La Lastra 42.91534, −4.66880 · Peña del Oso (vista del valle de Miranda) · Alto de Hornamiel (1.478 m) 42.89713, −4.67082 · puente de hormigón sobre el arroyo de Valderrianes.
- **Descripción:** 900 m de pista aguas abajo por la margen izquierda; sube suave a La Lastra; pista al sur; puente de Valderrianes; ladera hasta una pista que sube a la Peña del Oso. Rodea el Alto de Hornamiel y vuelve a La Lastra por el fondo de un valle.
- **Fauna:** zona de berrea; águila real; rastros de lobo.
- Información: Agrupación Comarcal de Desarrollo · [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-triollo-hornamiel) · ✅.

#### mp-lezna · Pico Lezna (2.208 m) desde Lores
- i/v · 21,6 km (GPX de ida 10,83) · pág. 997 m (GPX calc. +1.071) · 1.205–2.202 m · 6 h · media.
- Inicio: Lores 42.99656, −4.53308 (GPX) ✅ · cumbre 43.00672, −4.64687.
- Itinerario: pista del arroyo Gerino; a 1 km no tomar el desvío al molino. Tenadas de Lores y chozo; Majada de Tañuga; chozos de San Salvador (uno antiguo y otro moderno); pista en zigzag con el arroyo del Lezna a la izquierda. **Tramo final campo a través**, sin camino pero cómodo. Vuelta por el mismo camino.
- Información: Ayto. de La Pernía · [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-lores-pico-lezna) · ✅. Refugio: las "Tenadas de Lores" del informe quedan a 1 km o más de Lores, sin coordenada ⚠️.

#### mp-of-lomas · Senda del Pozo de las Lomas (Terranostrum)
- 12 km i/v · 640 m · 5 h · media-alta · GPX de ida 6,19 km / +671 / 1.414–**2.078 m** · inicio 42.97106, −4.75758 (junto a la iglesia) · **Pozo de las Lomas 43.01047, −4.74287** ✅. En invierno y al principio de la primavera la nieve exige técnica.
- [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/el-pozo-de-las-lomas).

#### mp-murcia-valcabe · Pico Murcia desde Cardaño de Arriba (Terranostrum)
- Circular · 11,8 km · pág. 1.144 m (GPX calc. +947) · 1.410–2.345 m · 5 h · media.
- Inicio: aparcamiento 42.97024, −4.75714 · cumbre 42.98045, −4.79450.
- Pasa junto al **refugio Espigüete** a la salida de Cardaño de Arriba y por una **fuente a ~0,8 km** del inicio. Puente sobre el arroyo Valcabe a ~0,9 km.
- Avisos: tramo final entre Peña del Castillo y Cardaño con retamas altas, incómodo.
- [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ascension-al-pico-murcia) · ✅ / ⚠️ D+.

#### mp-espiguete-sur · y mp-espiguete-norte (Terranostrum)
- **Cara sur**: 12,2 km i/v · 1.050 m (GPX calc. +1.137 hasta 2.444 m) · 5 h 45 · alta. Inicio en Cardaño de Abajo, 42.92153, −4.76374. Pedrera de piedra suelta; bajar con mucho cuidado. Información: M. Á. Madrid Gómez. [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ascension-pico-espiguete-por-la-cara-sur).
- **Cara norte**: 9,2 km circular · 1.050 m (GPX calc. +1.197) · 6 h · alta. Inicio en el aparcamiento de Pino Llano, 42.95139, −4.76164. **Con nieve, piolet y crampones**. Cumbre (punto de mapa) 42.94461, −4.79624. Información: Pedro Yubero Rivas. [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ascension-pico-espiguete-por-la-cara-norte).

#### mp-fraile · Peña del Fraile desde Santibáñez de la Peña (Terranostrum)
- Circular · 12 km · 898 m (el GPX tiene altitudes ruidosas: D+ calc. no fiable) · máx. 2.002 m · 5 h · media-alta. En nieve, extremar la precaución.
- Inicio: antiguas escuelas, 42.80945, −4.72989.
- Waypoints: túnel bajo la vía del tren · ruinas de San Román de Entrepeñas (s. X) · Peña Cueto 42.83689, −4.74850 · Peña del Fraile 42.83277, −4.76553.
- [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ascension-pena-fraile).

#### mp-dip-24 · relacionada; nueva variante mp-cruces-almonga-cervera [NUEVA]: Picos Almonga y de las Cruces desde Cervera
- i/v · 9,5 km · pág. 424 m (GPX calc. +634) · 949–1.560 m · 3 h · media-baja.
- Inicio: puesto de Cruz Roja de Cervera, CL-627 dirección Guardo, 42.85709, −4.49949. Cumbre ("Pico de las Cruceras") 42.84470, −4.53206.
- Pista forestal por un robledal y un pastizal cercado.
- Información: Agrupación Comarcal de Desarrollo · [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cervera-de-pisuerga-pico-de-las-cruces) · ⚠️ (descripción leída solo en parte).

#### Sendas oficiales: GPX calc. de Terranostrum frente a la ficha
| Slug | Ficha Terranostrum | GPX calc. | Inicio GPX |
|---|---|---|---|
| mp-of-tosande | [10 km i/v, +400, 3 h 30, baja-media, desde Dehesa de Montejo](https://www.terranostrum.es/senderismo/palencia/montana-palentina/la-tejeda-de-tosande) | 9,45 km, +429, 1.073–1.410 m, circular | 42.82574, −4.51656 |
| mp-of-roblon | [4,5 km, +100, 1 h 30](https://www.terranostrum.es/senderismo/palencia/montana-palentina/el-roblon-de-estalaya) | 4,51 km, +147, 1.079–1.227 m | 42.92417, −4.47207 |
| mp-of-oso | [11,7 km, +300, 4 h, baja; panel junto al puente](https://www.terranostrum.es/senderismo/palencia/montana-palentina/la-senda-pena-del-oso) | 11,7 km, +346, 999–1.267 m | 42.87209, −4.50276 |
| mp-of-bosque-fosil | [3 km, 1 h](https://www.terranostrum.es/senderismo/palencia/montana-palentina/la-senda-del-bosque-fosil) | 3,13 km, +110, 1.183–1.297 m, circular | 42.94297, −4.46199 |
| mp-of-ursi | [11 km circular, +300, 3 h 30, media](https://www.terranostrum.es/senderismo/palencia/montana-palentina/senda-del-escultor-ursi) | 11,28 km, +385, 1.063–1.380 m | 42.89342, −4.31060 (Villabellaco) |
| mp-of-gigante | [4,3 km, 1 h 10](https://www.terranostrum.es/senderismo/palencia/montana-palentina/senda-el-gigante-del-valle-estrecho) | 4,25 km, +157, 1.335–1.444 m | 42.90549, −4.62794; fin (Mirador de Caldacio) 42.89526, −4.61463 |
| mp-of-pinar-velilla | [3,5 km i/v, +150, 2 h; miradores de Compuerto y del Pinar](https://www.terranostrum.es/senderismo/palencia/montana-palentina/senda-del-pinar-de-velilla) | sin GPX | Ciudad del Brezo 42.84970, −4.83507 |
| mp-pescadores-velilla | [6,3 km, 2 h, desde el Centro de la Trucha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/senda-de-los-pescadores-en-la-ribera-del-rio-carrion) | 6,35 km, +17, circular | 42.82602, −4.84857 |

### 3.2 Rutas de Terranostrum que no están en el informe [NUEVAS]

Formato abreviado. Todas las cifras son de la ficha ("pág.") ✅ salvo que se diga GPX calc. Todas tienen GPX en Terranostrum salvo indicación. La descripción es un resumen propio de la parte leída (⚠️ si solo se leyó el inicio).

**Alto Carrión / Fuentes Carrionas / Velilla / Guardo**

#### mp-cardano-cruz-armada · Cardaño de Abajo – Collado de la Cruz Armada (camino de Binesa) [NUEVA]
- Circular · 12 km · pág. 437 m (GPX +512) · 1.252–1.727 m · 3 h 30 · media-baja.
- Inicio: plaza de Cardaño de Abajo, 42.92073, −4.76413 · collado de la Cruz Armada 42.93251, −4.80969.
- Pista al noroeste hacia los Corrales por el "camino de Binesa o Binuesa", entre robledal. Enlaza con el GR-1 E6 ⚠️.
- [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cardano-de-abajo-a-la-cruz-armada) (Agrupación Comarcal).

#### mp-mazobre-sima-anillo · Arroyo de Mazobre y Sima del Anillo, desde Puente Agudín [NUEVA]
- Circular · 13 km (GPX 12,97 / +549) · 1.296–1.794 m · 5 h · media.
- Inicio: aparcamiento de Puente Agudín, 42.92980, −4.75852.
- Waypoints: cascada de Mazobre 42.95926, −4.79281 · **Sima del Anillo 42.95505, −4.79818**.
- Sube 3 km por carretera o por el camino de Lamas hasta Pino Llano (antiguo campamento juvenil abandonado) y sigue el valle de Mazobre bajo la cara norte del Espigüete ⚠️.
- [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/el-arroyo-de-manzobres-y-sima-del-anillo).

#### mp-cueva-dorada · Cueva Dorada desde Camporredondo de Alba [NUEVA]
- i/v · 8 km (GPX de ida 3,98) · 325 m · 1.224–1.567 m · 3 h · media.
- Inicio: Camporredondo 42.89511, −4.74564 · fin 42.89396, −4.71383.
- Monte junto al pueblo con amplias vistas de las cumbres y del embalse ⚠️.
- [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cueva-dorada-fuentes-carrionas).

#### mp-coriscao · Monte Coriscao (1.569 m) desde Camporredondo de Alba [NUEVA]
- Circular · 10 km · 320 m (GPX +440) · 1.234–1.554 m · 3 h 30 · media.
- Inicio: 42.89467, −4.74735 · cerro 42.90374, −4.74454.
- Recorrido por bosques hasta la cima. El GR-1 E6 pasa por su desvío ⚠️.
- [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/subida-al-monte-coriscao-fuentes-carrionas).

#### mp-valsurbio-lobo · Proyecto Lobo: Camporredondo – Valsurbio – Corral de la Valleja [NUEVA]
- Circular · 11,3 km (GPX +469) · 1.224–1.648 m · 3 h · media-baja · **evitar el invierno**.
- Inicio: Camporredondo 42.89507, −4.74557. Valsurbio (despoblado) 42.86655, −4.73339.
- Ruta del proyecto de cooperación WOLF sobre el lobo y la ganadería ⚠️.
- [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/de-camporredondo-de-alba-a-valsurbio).

#### mp-valsurbio-compuerto · Por el despoblado de Valsurbio (Compuerto – Valcobero – Valsurbio – Camporredondo) [NUEVA]
- Lineal · 15,5 km (GPX +496) · 1.224–1.690 m · 5 h · media.
- Inicio: plataforma del embalse de Compuerto antes del túnel (km 52 de la carretera), 42.85679, −4.80806. Fin en Camporredondo.
- Waypoints: Valcobero 42.85692, −4.78308.
- [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/por-el-despoblado-de-valsurbio).

#### mp-collado-pinar · Collado del Pinar (Pinar de Velilla) desde Ciudad del Brezo [NUEVA]
- Circular · 10,7 km · 400 m (GPX +703, máx. 1.611 m) · 4 h · media.
- Inicio: aparcamiento de Ciudad del Brezo, 42.84860, −4.83557.
- Recorre el pinar autóctono de la ladera noroeste de Peña Mayor, desde 1.200 m de altitud ⚠️.
- [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-collado-del-pinar-fuentes-carrionas).
- Relacionada, **sin GPX**: "El Pinar de Peña Mayor" desde Compuerto: 4 km, 2 h 30; +400 m hasta el collado y +700 hasta Peña Mayor. Senda pedregosa junto al arroyo tras una escombrera. [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/el-pinar-de-pena-mayor).

#### mp-sabinar-pena-lampa · El Sabinar de Peña Lampa (Velilla) [NUEVA]
- Circular · 10,2 km · 554 m (GPX +688) · 1.140–**1.803 m** · 3 h 30 · media.
- Inicio: 42.84085, −4.85707.
- Peña Lampa (1.804 m, tres cotas escalonadas) está repartida entre León (Besande) y Palencia (Velilla) 🟧. Enlaza con `mp-pena-lampa`.
- [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-el-sabinar-de-pena-lampa).

#### mp-roblon-monasterio · Sendero del Roblón del Monasterio (PRC-P 12) [NUEVA]
- Circular · 11,8 km · 310 m (GPX +394) · 1.139–1.452 m · 3 h 30 · baja · **señalizado** (PRC-P 12).
- Inicio: campo de tiro al noroeste de Velilla, 42.83371, −4.84872. Roblón 42.85580, −4.89065.
- Sigue el antiguo camino carretero a Besande.
- Información: CIT Montaña Palentina · [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-roblon-del-monasterio-prc-p-12). **Es un PRC homologado municipal que el informe no recoge** ⚠️ (comprobar en FDMESCYL).

#### mp-valdelobos · Sendero de Valdelobos (PRC-P 14), Fresno del Río [NUEVA, periferia]
- Circular · 11,8 km · 78 m · 1.011–1.089 m · 2 h 45 · baja.
- Inicio: área recreativa de Fresno del Río, 42.68089, −4.82386.
- 🟨 Al sur de Guardo, en el límite del ámbito de la app.
- Información: Ayto. de Fresno del Río · [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-de-valdelobos-prc-p-14).

#### Guardo: red "Senderos de Leyenda" y rutas de J. A. Bardasco [NUEVAS]
Todas salen de Guardo (≈ 42.790, −4.844) salvo Doncellas.

| Slug | Ruta | Km | D+ (pág. / GPX) | Tiempo | Dific. | Inicio (GPX) | Notas | Enlace |
|---|---|---|---|---|---|---|---|---|
| mp-guardo-brujas | Valle de las Brujas | 6,2 circ. | 147 / 212 | 1 h 30 | Baja | 42.78995, −4.84311 | Robledal de Monte Castro, Fuentefría; senda de las brujas y de los toboganes. Leyenda de las brujas de Cansoles | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-al-valle-de-las-brujas) |
| mp-guardo-balcon-judas | De los Lobos al Balcón de Judas | 15 circ. | 396 / 628 | 4 h 30 | Media | 42.78991, −4.84312 | Restos de minas de carbón; Monte Castro; **Fuente de la Salud** | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-de-los-lobos-al-balcon-de-judas) |
| mp-doncellas-hoyal | Senda de las Doncellas del Hoyal (desde Muñeca) | 12 circ. (pt 11,97) | 242 / 391 (pt 364) | 3 h (pt 3 h 30) | Media (pt fácil) | 42.79202, −4.80148 | Robledal; camino forestal "casi mágico" | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/senda-de-las-doncellas-del-hoyal) · [pt](https://palenciaturismo.es/que-hacer/rutas/senda-doncellas-hoyal) |
| mp-guardo-merendillas | Ruta de las Merendillas | 9,8 circ. | 187 / 256 | 2 h 30 | Baja | 42.78956, −4.84324 | Mina de Valdecastro, escombreras, **Fuente Ferruginosa**, Cueva del Hoyal 42.80927, −4.81780 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-de-las-merendillas-guardo) |
| mp-guardo-corcos | Monte Corcos y Ermita del Cristo del Amparo | 12 (GPX 10,8; semicircular) | 220 / 222 | 3 h | Baja | 42.79048, −4.84548 | Corrales del Sestil 42.80524, −4.88800; ermita 42.78030, −4.86632 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-monte-corcos-y-ermita-del-cristo) |
| mp-guardo-san-quirce | Valles de San Quirce y Corcos | 14,3 circ. | 340 / 344 | 4 h | Baja | 42.79054, −4.84581 | Corcos 42.81521, −4.88809 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-valles-san-quirce-y-corcos) |
| mp-guardo-circular | Circular de los alrededores de Guardo | 22 | 212 / 487 | 6 h | Media | 42.79040, −4.84468 | Por Velilla, Muñeca e Intorcisa; también en bici; necrópolis de Guardo 42.78513, −4.83970 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-circular-alrededores-de-guardo) |

**La Pernía / Alto Pisuerga**

#### mp-ribero-pintado · El Ribero Pintado (Santa María de Redondo) [NUEVA]
- Terranostrum: circular · 6,2 km · 157 m · 1 h 30 · baja · máx. 1.373 m (GPX 6,26 / +174). Palenciaturismo: 6 km i/v · +107 · fácil · SL sin señalizar · con GPX ✅.
- Inicio: parking de Fuente Cobre, 42.99148, −4.42837 · **Ribero Pintado 43.01087, −4.41972** ✅.
- A ~3 km, por el camino hacia el Tres Mares y junto al arroyo Lombatero: antigua explotación a cielo abierto con estratos de areniscas (rojizas por óxidos de hierro) y lutitas negras ricas en materia orgánica. Los colores cambian con la luz y la lluvia. Foto 19 del libro 2026.
- Avisos: sin dificultad; evitar épocas de mucha nieve.
- [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-del-ribero-pintado) · [palenciaturismo](https://palenciaturismo.es/que-hacer/rutas/ruta-ribero-pintado) (Ayto. de La Pernía).

#### mp-bocaron-casavegas · Bocarón de Casavegas / Ojo de Caloca (Mirador de Cerradillo) [NUEVA]
- i/v · 8,4 km (GPX de ida 4,23) · 308 m (GPX +334) · 1.221–1.529 m · 3 h 30 · baja.
- Inicio: fuente, lavadero y pilón de Casavegas, 43.02222, −4.51268 · **Bocarón 43.03104, −4.54301** ✅.
- Pista con vistas de Peñalabra; bosquete de hayas y robles; collado; bifurcación (a la derecha se baja a Caloca, Cantabria) ⚠️.
- = Foto 38 del libro 2026 ("Ojo de Caloca"). Información: Casavegas.es · [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/bocaron-de-casavegas).

#### mp-redondo-bismo · San Juan de Redondo – Corrala de Bismo [NUEVA]
- Circular · 9,5 km · 371 m (GPX +373) · 1.197–1.444 m · 3 h · baja.
- Inicio: iglesia de San Juan de Redondo, 42.98999, −4.44842 · Corrala de Bismo 43.02358, −4.44320.
- Pista al norte; a 420 m, bifurcación a la izquierda; subida suave de ~700 m ⚠️. La ficha pone por error "San Román de Redondo" como salida.
- [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-san-juan-de-redondo-corrala-de-bismo) (Agrupación Comarcal).

#### mp-polentinos-lebanza · Polentinos – Abadía de Lebanza [NUEVA]
- i/v · 8,9 km (GPX +384) · pág. 211 m · 1.186–1.406 m · 2 h 10 · baja · ciclable.
- Inicio: plaza del Ayuntamiento de Polentinos, 42.93841, −4.52466 · Abadía 42.96283, −4.55313.
- Pista ganadera al noroeste; alto con abrevadero; collado Mojoncillo; bajada a la abadía, edificio neoclásico del s. XVIII y antiguo seminario menor, hoy con uso marginal en verano. Vistas al Curavacas. Zona de oso y lobo.
- [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-polentinos-abadia-de-lebanza). (No son las "Cascadas de Lebanza", que siguen sin fuente.)

#### mp-vidrieros-pie-curavacas · De Vidrieros a los pies del Curavacas [NUEVA]
- Lineal · 4,8 km · 346 m (GPX +393) · 1.282–1.671 m · 1 h 20 · baja.
- Inicio: plaza de Vidrieros, 42.94283, −4.66461 · campa final 42.95493, −4.67389.
- Sale al norte dejando la iglesia a la derecha. El último tramo, el de más pendiente, va por pista ancha. Útil como aproximación familiar o como primer tramo hacia el Curavacas ⚠️.
- [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-vidrieros-pie-del-curavacas).

**La Braña / Brañosera / Barruelo / Mudá**

| Slug | Ruta | Tipo · Km | D+ (pág. / GPX) | Alt. GPX | Tiempo · Dific. | Inicio (GPX) | Notas | Enlace |
|---|---|---|---|---|---|---|---|---|
| mp-salcedillo-rojadillo | Salcedillo – Puente de Rojadillo – Brañosera | Lineal 12,5 | — / 395 | 1.059–1.451 | 4 h 30 · baja | 42.94085, −4.27437 | Iglesia románica del s. XII con pinturas del s. XV; puente romano de Rojadillo 42.93549, −4.24146 entre hayas y robles | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-salcedillo-rojadillo-y-branosera) |
| mp-valberzoso-rojadillo | Valberzoso – Puente Romano El Rojadillo | Circ. 6,6 | 125 / 149 | 1.062–1.168 | 1 h 45 · baja | 42.92382, −4.23767 (a 1 km del pueblo) | En el límite con Cantabria; collado en U entre Peña Ensillada y Peña Castrillo | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-valberzoso-puente-rojadillo) |
| mp-valberzoso-somahoz | Valberzoso – Collado de Somahoz | i/v 10,5 | 140 / 199 (ida) | 1.055–1.216 | 4 h · baja | 42.92384, −4.23766 | Por la PP-2041 hacia Mata de Hoz; collado 42.96030, −4.23556 (🟦 límite con Cantabria) | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/valberzoso-collado-de-somahoz) |
| mp-calero-branosera | La Mata del Fraile y el Calero de Brañosera | Circ. 10,5 | — / 342 | 1.047–1.330 | 3 h · baja | 42.91143, −4.28835 (Barruelo, puente de Peñacorva) | Pista de ~4 km entre robles centenarios hasta el calero | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-la-mata-del-fraile-y-el-calero-de-branosera) |
| mp-ujapero-cocoto | Ujapero y Cocoto (parque eólico El Pical) | Circ. 19 | 466 / 505 | 1.027–1.492 | 4 h · media | 42.90879, −4.28813 (Barruelo) | Brañosera, carretera de Salcedillo; Peña El Cocoto 42.90407, −4.25846 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-de-ujapero-y-cocoto) |
| mp-monte-ciruelo | Monte Ciruelo (Perapertú – San Cebrián de Mudá – San Martín de Perapertú) | Circ. 11,2 | — / 303 | 1.035–1.335 | 3 h · fácil · ciclable | 42.91746, −4.36875 | ~3,5 km por carretera entre San Cebrián y Perapertú | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/monte-ciruelo-desde-la-muneca) |
| mp-minas-san-cebrian | Las minas de San Cebrián de Mudá (Tierras del Bisonte) | Circ. 5 | 118 / 120 | 1.058–1.181 | 1 h 15 · baja | 42.89711, −4.38622 (C. I. Bison Bonasus) | Retorno en 42.91424, −4.38864 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-las-minas-de-san-cebrian-de-muda) |
| mp-muda-monasterio | Mudá – Monasterio | i/v 6,5 | 109 / 128 | 990–1.107 | 1 h 30 · baja | 42.87619, −4.39526 (puente del arroyo de la Pradera) | Monasterio (pueblo) 42.87610, −4.36326 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-de-muda-a-monasterio) |

**Valle del Pisuerga / Valdivia / Aguilar (Las Loras)**

| Slug | Ruta | Tipo · Km | D+ (pág. / GPX) | Tiempo · Dific. | Inicio (GPX) | Notas | Enlace |
|---|---|---|---|---|---|---|---|
| mp-liguerzana-mariposas | Ligüérzana – Vega de Quintanaluengos (mariposa hormiguera oscura) | Circ. 8,7 | 86 / 83 | 2 h · baja | 42.85677, −4.45841 (puente del Pisuerga, panel) | **Microrreserva de mariposas** 42.84447, −4.42769 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-ligueerzana-a-la-vega-de-quintanaluengos) |
| mp-cillamayor-matabuena | Cillamayor – Matabuena (Valle de Santullán) | Circ. 8,7 | 203 / 250 | 2 h · baja | 42.86254, −4.27877 (teleclub) | Campos, praderías, rebollar | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-cillamayor-montes-de-matabuena) |
| mp-canduela-valdelobera | Canduela – Villanueva de Henares (necrópolis de Valdelobera) | Circ. 8,5 (o i/v de 5,6–5,7) | 87 / 269 | 2 h 15 · baja | 42.83439, −4.18623 | Necrópolis 42.83648, −4.16537 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-canduela-villanueva-de-henares) |
| mp-menaza | Campos de Menaza | Circ. 6 | 77 / 87 | 2 h · baja | 42.83134, −4.21617 | Robledal y cultivos; la ficha escribe "Mezana" por error | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/sendero-campos-de-menaza) |
| mp-blendios-e1 | Calzada de los Blendios (GR-73) E1: Herrera de Pisuerga – Santa María de Mave | Lineal 21,3 | — / 187 | 6 h · baja | 42.59624, −4.32911 | Sobre la calzada romana Pisoraca–Portus Blendium. 🟨 La mayor parte queda al sur del ámbito (Herrera, Alar) | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/calzada-de-los-blendios-etapa-1) |
| mp-blendios-e2 | Calzada de los Blendios (GR-73) E2: Santa María de Mave – Aguilar | Lineal 11 | — / 141 | 3 h · baja | 42.72281, −4.27515 | Mave, Olleros, Valoria | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/calzada-de-los-blendios-etapa-2) |

### 3.3 Camino Olvidado: etapas palentinas

#### mp-co-e5 · Camino Olvidado E5: Olea (Cantabria) – Aguilar de Campoo
- Lineal · 24,3 km (GPX 24,61) · desnivel acumulado 452 m (GPX calc. +715) · 719–1.025 m · 6 h · baja · ciclable · todo el año.
- Inicio: Olea 42.93862, −4.17917 · fin en Aguilar, 42.79282, −4.25910.
- Paso por pueblos (puntos de mapa): Casasola 42.91065, −4.19142 · La Cuadra · Las Quintanillas · La Quintana · Las Henestrosas · Bercedo · Cuena (último pueblo cántabro) · **Néstar** (entrada en Palencia por el puente romano de Puenteperdiz) 42.84195, −4.23770 · Grijera 42.81400, −4.24577 · Aguilar.
- Patrimonio: puente romano de la calzada Pisoraca–Portus Blendium; menhires de La Matorra I y II (8 conocidos en el valle); castro cántabro de Grijera; iglesia de Santa María la Real en Las Henestrosas.
- 🟦 Casi toda la etapa va por Cantabria (Valdeolea y Valderredible); en Palencia solo el tramo Néstar–Aguilar.
- [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-olvidado-en-palencia-etapa-5) · ✅.

#### mp-co-e6 · Camino Olvidado E6: Aguilar de Campoo – Cervera de Pisuerga
- Lineal · 28,7 km · acumulado 427 m (GPX +369) · 884–1.007 m · 7 h · baja · ciclable.
- Inicio 42.79282, −4.25910 → fin 42.86210, −4.49855.
- Pueblos: Corvio 42.82207, −4.27981 (necrópolis rupestre con una veintena de tumbas antropomorfas, s. X ⚠️) · Matamorisca · Salinas de Pisuerga · Barcenilla · Quintanaluengos · Ligüérzana · Vado · eremitorio rupestre de San Vicente o Cueva de los Moros · Cervera.
- Sale por el monasterio de Santa María la Real, el paseo de los Cinco Caños y el camino sobre la presa, con vistas del embalse de Aguilar. El Camino Lebaniego lo cruza en Cervera.
- [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-olvidado-en-palencia-etapa-6) · ✅.

#### mp-co-e7 · Camino Olvidado E7: Cervera de Pisuerga – Guardo
- Lineal · 39,3 km (GPX 38,88) · acumulado 851 m (GPX +626) · 990–1.199 m · 8–9 h · baja · ciclable, aunque el primer tramo hasta Tosande puede complicarse en bici.
- Inicio 42.86202, −4.49835 → fin en Guardo, 42.78388, −4.85674.
- Pueblos: valle de Tosande (Tejeda) · Cantoral · Cubillo de Castrejón · Traspeña (crucero) · Villanueva de la Peña · Tarilonte · Aviñante · San Román de Entrepeñas (ruinas) · Santibáñez de la Peña (castro de La Loma, asedio romano del 25 a. C.) · Las Heras · Villanueva de Arriba · Muñeca · Guardo (pila bautismal románica en San Juan; Casa Grande barroca).
- [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-olvidado-en-palencia-etapa-7) · ✅.

(E8 Guardo – Puente Almuhey, León: 58,8 km según el GPX, que parece cubrir más de una etapa ⚠️. [Ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-olvidado-en-leon-etapa-8). Lista completa de etapas: E1 Nava de Ordunte … E12B Buiza – La Magdalena.)

### 3.4 mp-cn-romanico · Camino Natural del Románico Palentino: etapas (Terranostrum, slug "ruta-del-carbon-de-cok")

La fuente de la información es "Caminos Naturales" (MAPA). Dificultad media, ciclable al 100%, todo el año. El GPX completo mide 131,6 km / ~2.000 m calc. (el informe da ~103 km ⚠️, quizá sin variantes).

| Tramo | Km (pág.) | Tiempo | GPX calc. (km / D+ / alt.) | Inicio → fin (GPX) | Pueblos | Enlace |
|---|---|---|---|---|---|---|
| E1 Alar del Rey – Cozuelos de Ojeda | 16,9 | 5 h | 16,86 / +333 / 851–1.065 | 42.65863, −4.30906 → 42.75541, −4.39280 | Prádanos de Ojeda, Santibáñez de Ecla, Villaescusa de Ecla | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-del-carbon-de-cok-etapa-1) |
| E2 Cozuelos de Ojeda – Vado | 32,3 | 9 h | 27,8 / +569 / 990–1.229 | 42.75541, −4.39281 → 42.85415, −4.48349 | Vallespinoso de Aguilar, barrios de San Pedro y Santa María, Dehesa de Montejo | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-del-carbon-de-cok-etapa-2) |
| Variante 2 Cozuelos de Ojeda – Dehesa de Montejo | 22,5 | 6 h 30 (baja) | 22,3 / +397 / 978–1.101 | 42.76432, −4.39716 → 42.81855, −4.50581 | Perazancas, Montoto, Pisón y Colmenares de Ojeda | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-del-carbon-de-cok-variante-2) |
| E3 Vado – Herreruela de Castillería | 21,2 | 6 h | 21,0 / +444 / 951–1.330 | 42.85415, −4.48349 → 42.92933, −4.39066 | Barcenilla, Rueda de Pisuerga, Vallespinoso de Cervera, San Cebrián de Mudá. Mirador sobre Vado | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-del-carbon-de-cok-etapa-3) |

Confianza ✅ en cifras de ficha y GPX / ⚠️ en la equivalencia de nombres. La ficha de la variante la llama "la última etapa de la Ruta del Carbón de Cok", señal de que el sitio mezcla dos nombres. Pendiente: contrastar con el GPX oficial del MAPA.

### 3.5 mp-cn-lebaniego · Camino Lebaniego Castellano: etapas palentinas (Terranostrum; información: Diputación de Palencia)

| Etapa | Km (pág.) | Tiempo | Dific. | GPX calc. (km / D+ / alt.) | Inicio → fin (GPX) | Pueblos | Enlace |
|---|---|---|---|---|---|---|---|
| E6 Alar del Rey – Perazancas de Ojeda | 24,8 | 5 h 30 | Baja | 24,76 / +483 / 847–1.066 | 42.65864, −4.30915 → ~42.785, −4.421 | Prádanos, Santibáñez de Ecla, San Andrés de Arroyo, Villaescusa de Ecla, Cozuelos | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-lebaniego-castellano-etapa-6-alar-del-rey-perazancas-de-ojeda) |
| E7 Perazancas – Cervera | 18,2 | 4 h 30 | Baja | 18,26 / +352 / 987–1.163 | 42.78522, −4.42115 → 42.86389, −4.49794 | Dehesa de Montejo, Vado | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-lebaniego-castellano-etapa-7-perazancas-de-ojeda-cervera-de-pisuerga) |
| E8 Cervera – San Salvador de Cantamuda | 18 | 4 h 30 | Baja | 18,07 / +459 / 995–1.297 | 42.86391, −4.49793 → 42.96494, −4.49840 | Arbejal, Vañes, Estalaya | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-lebaniego-castellano-etapa-8-cervera-de-pisuerga-san-salvador-de-cantamuda) |
| E9 San Salvador – Camasobres | 12,4 | 3 h 30 | Baja | 12,42 / +524 / 1.106–1.401 | 42.96493, −4.49790 → 43.01521, −4.48818 | El Campo, Lores, Casavegas | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-lebaniego-castellano-etapa-9-san-salvador-de-cantamuda-camasobres) |
| E10–11 Camasobres – Pesaguero – Santo Toribio 🟦 | 17,4 + 24 | 4 h 30 + 7 h | Baja | 41,84 / +1.076 / 287–1.454 | 43.01507, −4.48749 → 43.14995, −4.65439 | Entra en Liébana (Cantabria). La ficha numera las etapas como 11 y 12 de forma incoherente ⚠️ | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/camino-lebaniego-castellano-etapas-10-11-camasobres-monasterio-santo-toribio) |

El "Camino Natural Lebaniego de Pineda" no aparece en Terranostrum ❓.

### 3.6 BTT en Terranostrum (Montaña Palentina)

Casi todas proceden de la Agrupación Comarcal de Desarrollo Montaña Palentina. Las cuatro marcadas "TCyL" proceden de Turismo Castilla y León. Todas con GPX. Las cifras son de la ficha; la columna GPX da la longitud calculada. Varias coinciden con títulos de la guía BTT de la Diputación (por ejemplo, "Los Hayedos del Valle Estrecho") ⚠️.

| Slug propuesto | Ruta | Km (pág. / GPX) | D+ (pág.) | Tiempo | Dific. | Salida (coord. GPX) | Enlace |
|---|---|---|---|---|---|---|---|
| mp-btt-alto-muda | Alto Valle de Mudá | 12,2 / 12,15 | 266 | 1 h 20 | Baja | San Cebrián de Mudá 42.89712, −4.38624 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-alto-valle-de-muda) |
| mp-btt-barruelo-cervera | Barruelo – Cervera (TCyL) | 29,3 / 30,6 | 153 | — | Media | 42.90167, −4.28789 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-barruelo-de-santullan-cervera-de-pisuerga) |
| mp-btt-cervera-triollo | Cervera – Triollo (TCyL) | 24,3 / 23,7 | 440 | — | Alta | 42.86211, −4.49870 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-cervera-de-pisuerga-triollo) |
| mp-btt-carbon | Del Carbón | 19 / 19,1 | 255 | 1 h 55 | Baja | Salinas de Pisuerga 42.84850, −4.37923 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-del-carbon) |
| mp-btt-robla | El Ferrocarril de La Robla | 34 / 34,0 | 669 | 3 h 30 | Alta | Las Heras de la Peña 42.80015, −4.73802 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-el-ferrocarril-de-la-robla) |
| mp-btt-gotico-pena | Gótico y Románico en La Peña | 17,5 / 17,6 | 156 | 1 h 40 | Baja | Castrejón de la Peña 42.80801, −4.59890 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-gotico-y-romanico-en-la-pena) |
| mp-btt-guardo-almuhey | Guardo – Puente Almuhey (TCyL) 🟧 | 21,3 / 21,4 | 230 | — | Media-alta | 42.79768, −4.84809 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-guardo-puente-almuhey) |
| mp-btt-despensa-abad | La Despensa del Abad | 25,4 / 25,4 | 450 | 2 h 30 | Baja | Cillamayor 42.86263, −4.27773 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-la-despensa-del-abad) |
| mp-btt-horca-ojeda | La Horca de la Ojeda 🟨 | 22 / 22,0 | 375 | 2 h 15 | Baja | San Andrés de Arroyo 42.70195, −4.38255 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-la-horca-de-la-ojeda) |
| mp-btt-ermitas-aguilar | Las Ermitas del Embalse de Aguilar | 21,6 / 21,4 | 419 | 2 h 15 | Baja | Vallespinoso de Aguilar 42.77399, −4.36764 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-las-ermitas-del-embalse-de-aguilar) |
| mp-btt-tamaricas | Las Fuentes Tamáricas | 13,5 / 13,5 | 198 | 1 h 20 | Baja | Velilla 42.82771, −4.84400 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-las-fuentes-tamaricas) |
| mp-btt-valdavia | Las Ranas del Río Valdavia 🟨 | 20 / 19,9 | 325 | 2 h | Baja | Respenda de la Peña 42.76368, −4.68649 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-las-ranas-del-rio-valdavia) |
| mp-btt-burejo | Los Valles de Burejo | 20 / 20,1 | 317 | 2 h | Baja | Dehesa de Montejo 42.81944, −4.50994 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-los-valles-de-burejo) |
| mp-btt-karsticos | Monumentos Kársticos | 17,7 / 17,7 | 371 | 1 h 50 | Baja | Villaescusa de las Torres 42.75905, −4.25095 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-monumentos-karsticos) |
| mp-btt-pedaleando-romanico | Pedaleando por el Románico Palentino (Diputación) | 59,7 / 56,2 | 1.069 | 3 h 30 | Alta | Aguilar 42.79632, −4.27297 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-pedaleando-por-el-romanico-palentino) |
| mp-btt-vega-carrion | Por la Vega del Carrión | 20 / 20,0 | 254 | 2 h | Baja | Guardo 42.79109, −4.84814 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-por-la-vega-del-carrion) |
| mp-btt-ventas-pernia | Por las Ventas de La Pernía | 9,2 / 9,3 | 160 | 55 min | Baja | San Salvador de Cantamuda 42.96864, −4.49503 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-por-las-ventas-de-la-pernia) |
| mp-btt-valle-estrecho | Por Valle Estrecho | 17,3 / **8,55** ⚠️ (GPX incompleto o solo ida) | 295 | 1 h 45 | Baja | Ruesga 42.86402, −4.52766 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-por-valle-estrecho) |
| mp-btt-santullan | Románico en Tierras de Santullán | 17 / 16,9 | 350 | 1 h 45 | Baja | Barruelo 42.89790, −4.28264 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-romanico-en-tierras-de-santullan) |
| mp-btt-senda-pisuerga | Senda del Pisuerga | 19 / 19,2 | 184 | 1 h 55 | Baja | Cervera 42.86289, −4.49639 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-senda-del-pisuerga) |
| mp-btt-jano | Tras las Huellas de Jano | 27,3 / 27,3 | 264 (GPX +799 ⚠️) | 3 h | Alta | Guardo 42.79640, −4.84771 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-tras-las-huellas-de-jano) |
| mp-btt-triollo-guardo | Triollo – Guardo (TCyL) | 30 / 29,9 | 570 | — | Alta | Triollo 42.92486, −4.68090 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-triollo-guardo) |
| mp-btt-bernorio-gama (informe) | Vuelta al Monte Bernorio | 20,4 / 20,6 | 280 | 2 h | Baja | Pomar de Valdivia 42.77484, −4.16699 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt-vuelta-al-monte-bernorio) |
| mp-btt-aguilar | "Ruta BTT" (Aguilar de Campoo) | 13,4 / 13,4 | 104 | 1 h 20 | Baja | 42.79577, −4.27137 | [ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ruta-btt) |

Fuera de interés: "Cyclope Palencia Road Bike" es una ruta de carretera de 489 km por toda la provincia (Diputación).

**Monte Bernorio** (pendiente 17): solo existe esta vuelta BTT. Desde Pomar de Valdivia rodea el monte, con interés arqueológico; pasa por Quintanilla y el río Camesa y llega a Porquera de los Infantes (necrópolis) ⚠️. No hay ficha a pie.

---

## 4. Lo que sigue pendiente después de esta pasada

1. **lapedrerapindia.com**: 24 rutas de la Diputación, estado de los QR, GPX y BTT. Host caído o bloqueado.
2. **Coordenadas reales del mapa del libro 2026**: 38 enlaces `maps.app.goo.gl` sin resolver (host no permitido). Bastaría con abrirlos en un navegador.
3. **OCR de `sendas_de_barruelo.pdf`** (escaneado) y de los folletos 2019 de la Junta que enlaza palenciaturismo.
4. **Mazobre**: el punto "Cascada" de Terranostrum (42.95927, −4.79282) no encaja con el final del GPX de la senda (máx. 1.613 m). Hay que contrastar la ubicación del mirador.
5. **D+ de Terranostrum**: varias fichas dan menos desnivel que el GPX (Covalagua integral 270 frente a 480; Golobar 525 frente a 862; Cervera–Cruces 424 frente a 634). Usar rangos.
6. **PRC-P 12 (Roblón del Monasterio) y PRC-P 14 (Valdelobos)**: senderos homologados municipales que no estaban en el informe. Falta confirmar su homologación en FDMESCYL (host no probado en esta pasada).
7. **Sin fuente todavía**: Cascadas de Lebanza, Cascada de Atría, Senda del Agua, Ruta de los Molinos, Hayedo de Monte Ahedo en Terranostrum, Peña Redonda en Terranostrum, Monte Bernorio a pie con ficha oficial y Senda de los Rojos (solo foto y mención en el mirador de Piedrasluengas).
