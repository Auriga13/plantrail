# Infraestructura de montaña y POI — Montaña Palentina (PN Montaña Palentina + Geoparque Las Loras, lado palentino)

Fecha de la investigación: 21/11/2026. Ámbito: bbox lat 42.75–43.05, lon -4.85 a -4.05.

**Limitaciones de método (importante para el redactor):**
- En esta sesión **no se pudo acceder a la API Overpass** (overpass-api.de y sus espejos rechazados por el proxy de red) ni a refugioslibres.com. **No hay extracción OSM**. Se ha dejado la consulta lista para ejecutar en `overpass_query_poi.overpassql` (misma carpeta). Para usarla hay que permitir `overpass-api.de` en la configuración de red de la sesión, o ejecutarla en local: `curl --data-urlencode data@overpass_query_poi.overpassql https://overpass-api.de/api/interpreter -o osm_poi.json`.
- La información procede solo de resultados de búsqueda web (no se pudieron abrir páginas completas). Las coordenadas marcadas como **"aprox. (no verificado)"** son orientativas, de conocimiento general, y deben sustituirse por las de OSM/IGN antes de publicarse en la app.

---

## 1. ¿Qué refugios existen y se pueden usar hoy?

### Takeaway
En la vertiente palentina **no hay ningún refugio guardado**; solo hay refugios libres y chozos de pastor, la mayoría en estado regular o malo, y casi todos los datos tienen años. Los más citados como utilizables son el Refugio de Mazobre (Espigüete, ~10 plazas) y el Refugio de los Pescadores (Vidrieros, 6 plazas, chimenea). El refugio del club Espigüete en Cardaño de Arriba y el chozo de Valcaliente se hundieron. Sobre los nombres propuestos "Refugio de Vidrieros", "del Ves", "de Pineda" y "Collado de Fuentes Carrionas" no encontré ninguna fuente que confirme que existan como refugios.

### Cited Findings
**Inventario (sin guarda en todos los casos):**

| Nombre | Ubicación / acceso | Coordenadas | Estado / capacidad / servicios | Fuente | Verificación |
|---|---|---|---|---|---|
| Refugio de los Pescadores | Unos 2 km por encima de Vidrieros, junto a la pista que sube el río Carrión; se llega en coche por 2 km de pista en buen estado | 42.9384, -4.64265 | Libre, 6 plazas, chimenea, mesa y bancos. La ficha da una **altitud de 2.528 m, que es un error evidente** (Vidrieros está a unos 1.250 m; la cota real debe rondar los 1.300 m) | [walkaholic.me (datos de refugioslibres.com)](https://www.walkaholic.me/shelter/spain/castile-and-leon/palencia/306-refugio-de-los-pescadores) | Agregador, sin fecha de estado |
| Refugio de Mazobre | Majada de Espigüete, base de la cara NE del Espigüete, unos 30 min desde el aparcamiento de Pino Llano | Sin coordenadas en las fuentes | Dos plantas; en la superior duermen unas 10 personas; descrito como "refugio abierto en aceptable estado" en una entrada de hace unos 13 años | [walkaholic.me](https://www.walkaholic.me/es/refugio/espana/castilla-y-leon/palencia/234-refugio-mazobre); [casiaventurilla.com](http://www.casiaventurilla.com/fuentes-carrionas-montana-palentina-cascada-de-mazobre) | Datos antiguos |
| Chozo / Refugio de la Majada de Fuentes Carrionas | Majada de Fuentes Carrionas, a 1.878 m (PeakVisor) | Ver PeakVisor | Según una página de 2026, "el estado actual del chozo es deficiente": solo vale como vivac de fortuna o resguardo temporal | [wikitrekk.com](https://wikitrekk.com/palencia/chozo-de-la-majada-de-fuentes-carrionas); [peakvisor.com](https://peakvisor.com/mountain-hut/refugio-de-majadas-de-fuentes-carrionas.html) | 2026, agregador |
| Chozo de las Tenadas de Lores | Lores (valle de Lores / Pineda) | — | En agosto de 2017 estaba "muy bueno", con 8 a 10 plazas para dormir | [subiendodosmilesenpalencia.blogspot.com](http://subiendodosmilesenpalencia.blogspot.com/p/los-chozos-de-la-montana-palentina.html) | Blog, 2017 |
| Chozo de Valcaliente | — | — | **Hundido.** Cayó el mismo invierno que se llevó el refugio del club Espigüete de Cardaño de Arriba | [mismo blog](http://subiendodosmilesenpalencia.blogspot.com/p/los-chozos-de-la-montana-palentina.html) | Blog |
| Refugio del club Espigüete (Cardaño de Arriba) | Cardaño de Arriba | — | **Destruido** (ver fila anterior) | [mismo blog](http://subiendodosmilesenpalencia.blogspot.com/p/los-chozos-de-la-montana-palentina.html) | Blog |
| Refugio del Postil de Soña | 1.526 m, Palencia | Ver ficha | Libre, sin guarda ni comidas, sin reserva; "solo sirve de abrigo con mal tiempo" | [refuge.camp](https://refuge.camp/es/refuge/refugio-del-postil-de-sona) | Agregador |
| Vivac de las Agujas de Cardaño | Agujas de Cardaño (macizo de Fuentes Carrionas) | — | Vivac de alta montaña, para montañeros experimentados; no es una construcción | [komoot guide 366047](https://www.komoot.com/el-gr/guide/366047) | Guía de usuarios |
| "Casa Hobbit" / Casa Enterrada | Alba de los Cardaños | — | Citada como abrigo libre para senderistas | [komoot guide 366047](https://www.komoot.com/el-gr/guide/366047) | Guía de usuarios |
| Refugio Cubil del Can | Lado leonés/cántabro, cerca de Peña Prieta | — | PeakVisor lo da como el refugio más cercano a Peña Prieta | [peakvisor Peña Prieta](https://peakvisor.com/peak/pena-prieta.html) | **Probablemente fuera de Palencia (Cantabria/León)** |

- Una relación de alojamientos del parque de hacia 2010 incluye el "Hostal Pineda" en Cervera de Pisuerga y la "Casa Cardiel" en Cardaño de Arriba. Son alojamientos, no refugios, lo que podría explicar de dónde salen "Refugio de Pineda" y "refugio de Cardaño" — [komoot / patrimonionatural (resumen de búsqueda)](https://patrimonionatural.org/ficheros/fuentescarrionasapdf221010_132617.pdf)
- Dirección y gestión del parque: Casa del Parque de Cervera de Pisuerga (ver §3). Para consultar el estado actual de los refugios: tel. 979 13 94 01 / 676 210 231 — [patrimonionatural.org Horario 2026](https://patrimonionatural.org/ficheros/Horario%202026.pdf)

### Inferences
- Para la app conviene **no presentar ningún refugio como "operativo" o "garantizado"**. Mejor usar la categoría "abrigo libre / estado no verificado" con la fecha del último dato, y separar los chozos (abrigo de emergencia) de los refugios con litera (Mazobre, Pescadores).
- El Refugio de los Pescadores es accesible en coche, así que en la práctica funciona más como abrigo o área de pesca que como refugio de alta montaña.
- Los nombres "Refugio de Vidrieros", "Refugio del Ves", "Refugio de Pineda" y "refugio Collado de Fuentes Carrionas" no aparecen en ninguna fuente encontrada. Lo más probable es que sean confusiones con alojamientos o con los chozos de majada.

### Gaps
- No hay coordenadas verificadas de Mazobre, Tenadas de Lores, Postil de Soña ni chozo de Fuentes Carrionas, porque no se pudo consultar OSM ni refugioslibres.com. La consulta Overpass guardada (`amenity=shelter`, `tourism=wilderness_hut|alpine_hut`) debería resolverlo.
- No hay datos de 2025-2026 sobre Mazobre ni Lores. Tampoco hay inventario oficial de la Junta de refugios o chozos del parque.
- Queda por confirmar si alguno tiene fuente al lado o chimenea (salvo Pescadores).

---

## 2. Puntos de agua: ¿qué fuentes son fiables?

### Takeaway
No encontré ningún inventario fiable de fuentes con datos de caudal estacional ni de potabilidad para el parque. "Fuente del Cobre" no es un manantial de agua para beber: es la cueva-surgencia del Pisuerga (Cueva del Cobre, Santa María de Redondo). La fiabilidad de las fuentes de ruta tendrá que salir de OSM (`natural=spring`, `amenity=drinking_water`) y de comprobaciones de campo.

### Cited Findings
- El nacimiento tradicional del Pisuerga es la Cueva del Cobre. Una guía docente matiza que el Pisuerga solo usa la Fuente del Cobre como zona de paso (sumidero/surgencia kárstica). Ruta de acceso: Santa María de Redondo → nacimiento del Pisuerga; también la "Senda del Escultor Ursi" (11 km, unas 3,5 h) — [fmdva.org guía docente Fuente del Cobre](https://www.fmdva.org/media/oi1nwveq/07-docente-fuente-del-cobre.pdf); [spain.info](https://www.spain.info/es/naturaleza/parque-natural-fuentes-carrionas-fuente-cobre-montana-palentina/)
- La Majada de Fuentes Carrionas (1.878 m) está en las fuentes del río Carrión, al pie de Peña Prieta y el Alto del Tío Celestino — [peakvisor](https://peakvisor.com/mountain-hut/refugio-de-majadas-de-fuentes-carrionas.html)
- La ganadería extensiva (vacuno, equino y ovino en los puertos de verano) es parte estructural del parque — [palenciaturismo Casa del Parque](https://www.palenciaturismo.es/system/files/2019-08/Casa%20parque%201.pdf)
- La guía oficial del GR 1 en Palencia (Patrimonio Natural) recorre el parque y es la mejor fuente documental para buscar las fuentes que hay en ruta — [Libro GR1 en Palencia (PDF)](https://patrimonionatural.org/ficheros/58dce5a62bd0a_Libro-GR1-en-PALENCIA.pdf)
- La guía "Libro Montaña Palentina" de la Diputación (mayo de 2026) es una fuente reciente que puede detallar fuentes y servicios — [palenciaturismo.es PDF 2026](https://palenciaturismo.es/system/files/2026-05/LIBRO%20MONTA%C3%91A%20PALENTINA%20%28versi%C3%B3n%20espa%C3%B1ol%29.pdf)

### Inferences
- Aviso recomendado en la app: ninguna fuente o manantial de montaña cuenta con control sanitario. Con presencia de ganado en los puertos (junio a octubre), hay que **tratar o filtrar el agua siempre**. Los manantiales de cota alta suelen ir menguando a finales del verano, en agosto y septiembre (inferencia general, sin fuente local).
- No hay que ofrecer la "Fuente del Cobre" como punto de agua: en la app debe aparecer como POI de interés geológico.

### Gaps
- No se encontró ninguna fuente sobre "Fuente de las Ánimas" ni sobre "Fuente Carrionas" como manantial con nombre y coordenadas.
- No hay datos de fiabilidad estacional ni análisis de potabilidad. Faltan las coordenadas de las fuentes, que hay que sacar de OSM.

---

## 3. Casas del Parque y centros de interpretación

### Takeaway
La Casa del Parque de Cervera de Pisuerga tiene horario oficial de 2026: de jueves a domingo casi todo el año y de martes a domingo en julio y agosto. Cierra del 14 de diciembre al 11 de febrero. El Centro de Interpretación de la Minería de Barruelo abre de miércoles a domingo y cierra en invierno. No conseguí verificar horarios del ROM (Aguilar) ni de los centros del Geoparque Las Loras.

### Cited Findings
- **Casa del Parque Natural Montaña Palentina (Cervera de Pisuerga).** Horario 2026:
  - del 12 de febrero al 30 de junio, de jueves a domingo (jueves, viernes y sábado de 10 a 14 h y de 17 a 20 h; domingo de 10 a 14 h);
  - del 1 de julio al 31 de agosto, de martes a domingo (mismo horario de martes a sábado);
  - del 1 de septiembre al 13 de diciembre, otra vez de jueves a domingo.

  Grupos: 979 13 94 01 / 676 210 231 — [patrimonionatural.org Horario 2026 (PDF)](https://patrimonionatural.org/ficheros/Horario%202026.pdf); [turismocastillayleon.com](https://www.turismocastillayleon.com/es/naturaleza/casa-parque-natural-montana-palentina). Otra ficha de Turismo CyL da el tel. 979 870 688 (discrepancia) — [Oficina comarcal turismo Cervera](https://www.turismocastillayleon.com/es/servicios/oficinas-turismo-4ec3/oficina-comarcal-turismo-cervera-pisuerga)
- **Cierres de senderos (aviso del 16/04/2026):** la Senda del Oso, tramo Cervera de Pisuerga - Arbejal, está cerrada por obras con cortes intermitentes y sin fecha de reapertura — [patrimonionatural.org PDF cierres](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural_2026_4_16-20260417-104844.pdf). En la app conviene enlazar este PDF o la página de cierres como fuente de estado de senderos.
- **Centro de Interpretación de la Minería (Barruelo de Santullán).** C/ Cerrada s/n, 34820, tel. 979 607 294. Unos 600 m² de exposición y mina visitable — [turismocastillayleon.com](https://www.turismocastillayleon.com/es/patrimonio-cultura/centro-interpretacion-mineria); [turismobarruelo.com](https://turismobarruelo.com/cim/mina-visitable-en.php). Según un agregador, cierra lunes y martes; de miércoles a viernes abre de 10:00 a 13:30 y de 16:00 a 19:30; cierre invernal del 12 de diciembre al 28 de febrero — [whichmuseum.com](https://whichmuseum.com/museum/centro-de-interpretacion-de-la-mineria-barruelo-de-santullan-34726/opening-hours) (no oficial). Hay una licitación de obras de rehabilitación energética (subvención de 681.000 €) que podría alterar la apertura — [barruelo.com](https://barruelo.com/descargas_breves/licitacion-cim.pdf)
- Oficina de turismo de Barruelo: Av. Constitución 20, tel. 979 606 045 — [turismocastillayleon.com](https://www.turismocastillayleon.com/es/patrimonio-cultura/centro-interpretacion-mineria)

### Inferences
- En diciembre y enero la Casa del Parque está cerrada. La app debería mostrar el estado "cerrado (temporada)" según la fecha.

### Gaps
- Faltan horarios verificados del Centro Expositivo ROM (Románico, Aguilar de Campoo), de los centros de visitantes del Geoparque Las Loras (sede en Aguilar / Olleros de Pisuerga) y de cualquier "Museo/Casa del Oso" (p. ej. el centro de la Fundación Oso Pardo en Verdeña); no se buscaron por falta de presupuesto de búsqueda.
- Faltan las coordenadas exactas de los centros.

---

## 4. Aparcamientos, trailheads, miradores, campings y albergues

### Takeaway
Las coordenadas verificadas (de fuente) que tengo son pocas: Mirador de Piedrasluengas, Mirador del Alto de la Varga y Refugio de los Pescadores (Vidrieros). Las demás salidas solo tienen coordenadas aproximadas de los pueblos y hay que cruzarlas con OSM (`amenity=parking`, `tourism=viewpoint`, `tourism=camp_site`).

### Cited Findings
| POI | Tipo | Coordenadas | Notas | Fuente |
|---|---|---|---|---|
| Mirador de Piedrasluengas | Mirador + aparcamiento | 43.0416715, -4.459259 | Puerto a más de 1.300 m, en el PN; hay aparcamiento propio | [soyecoturista.com (equipamientos de uso público)](https://soyecoturista.com/en/actividad/equipamientos-de-uso-publico); [trip.com](https://ca.trip.com/travel-guide/attraction/la-pernia/mirador-de-piedrasluengas-55808233) |
| Mirador del Alto de la Varga | Mirador + aparcamiento | 42.9085021, -4.7276461 | Sobre la carretera Velilla–Cardaño, vistas al Espigüete | [soyecoturista.com](https://soyecoturista.com/en/actividad/equipamientos-de-uso-publico); [komoot](https://www.komoot.com/highlight/5786112) |
| Aparcamiento Senda de Tosande (tejeda) | Trailhead | Sin coordenadas en la fuente | Equipamiento de uso público oficial | [soyecoturista.com](https://soyecoturista.com/en/actividad/equipamientos-de-uso-publico) |
| Aparcamiento de Pino Llano | Trailhead del Espigüete (cara N) y de Mazobre | — | A unos 30 min de Mazobre | [walkaholic Mazobre](https://www.walkaholic.me/es/refugio/espana/castilla-y-leon/palencia/234-refugio-mazobre) |
| Vidrieros (salida al Curavacas por Callejo Grande, pista del Carrión) | Trailhead | Aprox. 42.93, -4.64 (no verificado; según la posición del Ref. Pescadores) | | [loc.wiki ruta Curavacas desde Vidrieros](https://www.loc.wiki/hiking-trails/ascension-al-pico-curavacas-por-callejo-grande-desde-vidrieros-54764360) |

Cumbres de referencia para el 3D: Curavacas 42.976403, -4.67392 (Triollo) — [peakvisor](https://peakvisor.com/peak/curavacas.html); Peña Prieta 43.023843, -4.730018 — [peakvisor](https://peakvisor.com/peak/pena-prieta.html); Espigüete 42.94472, -4.79611 — [Wikipedia](https://en.wikipedia.org/wiki/Espig%C3%BCete).

Coordenadas aproximadas de los núcleos de salida (**no verificadas**, solo como semilla para cruzar con OSM): Cardaño de Arriba ~42.96, -4.76; Triollo ~42.93, -4.68; Lebanza ~42.95, -4.54; San Salvador de Cantamuda ~42.96, -4.50; Brañosera ~42.94, -4.31; Barruelo ~42.91, -4.28; Cervera ~42.87, -4.50; Aguilar ~42.79, -4.26; Velilla ~42.83, -4.85; Guardo ~42.79, -4.85 (**límite oeste del bbox**). El puerto de San Glorio (~43.07, -4.76) queda **fuera del bbox (lat > 43.05) y en León/Cantabria**.

### Inferences
- La capa de "Equipamientos de uso público" de la Junta (soyecoturista / IDECyL) parece la fuente oficial georreferenciada de aparcamientos, miradores y áreas recreativas. Es preferible a los agregadores.

### Gaps
- Sin datos de campings ni albergues verificados (Lebanza, Cervera, Aguilar, Velilla), ni de áreas recreativas, ni de la pernocta en autocaravana en los aparcamientos del parque.
- No hay datos sobre un "Mirador de Ojeda".

---

## 5. Emergencias: protocolo, cobertura y GREIM

### Takeaway
El protocolo es llamar al **112 Castilla y León**. En Palencia **no hay GREIM**: los rescates en Curavacas y Espigüete los hacen el **GREIM de Sabero (León)** y el **Grupo de Rescate y Salvamento de la Junta / Protección Civil de CyL** (con helicóptero), además de los bomberos de la Diputación de Palencia. No hay datos públicos de cobertura móvil en las cumbres.

### Cited Findings
- En la lista oficial de unidades de montaña de la Guardia Civil no figura ningún GREIM en Palencia. En el caso del Espigüete de mayo de 2024 se activó el GREIM de Sabero (León), que trabajó con el grupo de rescate de la Junta — [nuevecuatrouno.com 2024](https://nuevecuatrouno.com/2024/05/26/sucesos-muere-montanero-riojano-57-anos-espiguete-palencia/); [Guardia Civil Especialidad Montaña PDF](https://web.guardiacivil.es/pdflink/es/fb46b663-4062-11eb-8bde-6d0b3e4c7555/Especialidad-Montana.pdf)
- El GREIM de Sabero intervino en 23 rescates con 38 personas en 2025 (ámbito leonés y limítrofe) — [Diario de León](https://www.diariodeleon.es/leon/provincia/250805/2056076/greim-sabero-leon-interviene-23-rescates-montana-38-personas-2025.html)
- Curavacas: en febrero de 2023 tres especialistas de montaña de la Guardia Civil rescataron el cuerpo de un escalador — [The Objective](https://theobjective.com/actualidad/2023-02-27/rescate-cadaver-montanero-palencia/). En otro caso, el aviso al 112 CyL movilizó al Grupo de Rescate y Salvamento de Protección Civil (Triollo) — [El Mirón de Soria](https://elmirondesoria.es/soria/sucesos/fallece-montanero-en-monte-curavacas/amp); también se alertó a los bomberos de la Diputación — [Vozpópuli](https://www.vozpopuli.com/sucesos/muere-un-escalador-de-30-anos-tras-sufrir-una-indisposicion-mientras-ascendia-el-pico-curavacas-en-palencia.html)
- Espigüete, cara norte: aviso al 112 CyL y rescate por Protección Civil — [El Mirón de Soria](https://elmirondesoria.es/soria/sucesos/rescatados-dos-montaneros-enriscados-en-pico-espigueete/amp)
- El 112 se puede marcar con la cobertura de cualquier operadora, pero hace falta alguna. Sin cobertura, las alternativas son un teléfono o mensajero satelital, o un aviso diferido con las coordenadas a una persona de confianza — [FEMECV opciones de comunicación](https://www.femecv.com/sites/default/files/uploads/files/Opciones%20comunicacion%20montana.pdf); [senditur.com](https://www.senditur.com/es/blog/como-comunicar-una-emergencia-cuando-hacemos-senderismo-o-montana/)
- Centros de salud:
  - **Cervera de Pisuerga:** C/ Felipe Calvo s/n, tel. 979 870 291 (otro directorio da 979 870 494) — [saludcastillayleon ZBS Cervera](https://www.saludcastillayleon.es/CAPalencia/en/area-influencia/z-b-s-cervera-pisuerga)
  - **Aguilar de Campoo:** Av. Ciudad Deportiva s/n, tel. 979 122 088 (otro: 979 125 440) — [saludcastillayleon ZBS Aguilar](https://www.saludcastillayleon.es/CAPalencia/es/area-influencia/z-b-s-aguilar-campoo)
  - **Guardo:** tel. 979 851 505. Velilla del Río Carrión es un consultorio local de la ZBS de Guardo — [saludcastillayleon cita previa Palencia](https://www.saludcastillayleon.es/es/citaprevia/centros-adscritos-sistema-cita-previa/palencia)
  - **Hospital de referencia:** Complejo Asistencial Universitario de Palencia (Hospital Río Carrión) — [saludcastillayleon urgencias](https://www.saludcastillayleon.es/CAPalencia/fr/cartera-servicios/urgencias)

### Inferences
- Protocolo recomendado para la app: 1) llamar al 112 (indicar las coordenadas WGS84 que muestre la app); 2) si no hay cobertura, subir a una cresta o collado y probar por SMS; 3) usar el SOS satelital del móvil o de un mensajero. Que el GREIM más cercano esté en Sabero (a más de 1 h por carretera) hace que el helicóptero de la Junta sea el medio más rápido, aunque esto es una inferencia.
- Los valles encajados (Vidrieros, Lebanza, Pineda, Cardaño) probablemente tienen mala cobertura. No hay fuente que lo confirme.

### Gaps
- No hay mapa de zonas de sombra verificado: habría que consultar los mapas de cobertura de las operadoras o el estudio del Ministerio de Transformación Digital.
- Sin datos de helipuertos ni de puntos de toma de helicóptero (la consulta Overpass incluye `aeroway=helipad`).
- No se confirmaron las Urgencias PAC (atención continuada) de Cervera, Guardo y Aguilar.

---

## 6. Transporte: autobús, tren y puertos

### Takeaway
El norte de Palencia tiene concesiones regionales de autobús desde Palencia (VACL-111 Cervera–Palencia y VACL-079 Guardo–Palencia). La línea Palencia–Guardo la opera Autocares Abagón, según un agregador. Hay un servicio Guardo–Velilla con horario municipal, y la estación de Renfe de Aguilar de Campoo está en la línea Palencia–Santander. Para los puertos hay que consultar la DGT en tiempo real: San Glorio (N-621) exige cadenas a menudo y prohíbe camiones.

### Cited Findings
- Concesiones regionales VACL-111 (Cervera de Pisuerga–Palencia) y VACL-079 (Guardo–Palencia) en el ámbito Aguilar, Cervera, Guardo, Herrera y Saldaña — [BOCCL (sirdoc.ccyl.es)](https://sirdoc.ccyl.es/SIRDOC/PDF/PUBLOFI/BO/CCL/11L/BOCCL1100248/BOCCL-11-008044.pdf)
- Palencia–Guardo: directo, operado por Autocares Abagón (horarios en abagon.es), unos 5 días por semana — [rome2rio](https://www.rome2rio.com/es/Autob%C3%BAs/Palencia/Guardo) (agregador, confirmar)
- Guardo–Velilla del Río Carrión: horario municipal con horario de verano del 1/07 al 30/09 y sin servicio en festivos — [velilladelriocarrion.es/municipio/autobuses](https://velilladelriocarrion.es/municipio/autobuses/). Horario antiguo del Ayuntamiento de Guardo (salidas a las 11:15, 12:30, 13:45, 15:15 y 19:45 en días laborables), probablemente desactualizado — [guardo.org](https://guardo.org/conoce-guardo/como-llegar-horarios-de-transporte/)
- Alsa opera Bilbao–Cervera de Pisuerga según Omio. También aparecen Linecar y Autocares Abel Gómez en la zona de Palencia (sin confirmar en estas rutas) — [omio.es](https://www.omio.es/autobuses/bilbao/cervera-de-pisuerga); [Alsa estación Palencia](https://www.alsa.com/pt/estacoes/estacao-palencia)
- San Glorio (N-621): prohibido a camiones y articulados, y con cadenas obligatorias en episodios de nieve — [Diario de León](https://www.diariodeleon.es/leon/provincia/210109/736160/diecisiete-carreteras-provincia-afectadas-nieve-siete-cadenas-intransitable.html). Pando entre los puertos con cadenas; P-210 y P-217 (Cervera y Velilla) afectadas — [publico.es](https://www.publico.es/sociedad/nieve-obliga-cerrar-al-trafico.html). Aviso DGT de enero de 2026 sobre la CL-627 en Palencia — [DGT nota de prensa](https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/nota_prensa/20251119-Imprescindible-consultar-el-estado-de-vialidad-de-las-carreteras-antes-de-realizar-desplazamientos/NP-AVISO-DGT-NIEVE.pdf)
- Hay discrepancias en las fuentes sobre la denominación de San Glorio (N-621 / LE-621 / N-625) — [Wikipedia San Glorio](https://Www.Wikipedia.org/wiki/San_Glorio)

### Inferences
- Carreteras clave (inferencia sobre la red): CL-627 Aguilar–Cervera–Piedrasluengas (hacia Potes); P-210 Cervera–Guardo por la Pernía/Triollo; N-621 por San Glorio, ya en León, fuera del bbox. Estado en tiempo real: infocar.dgt.es / nap.dgt.es.
- Tren: estación de Aguilar de Campoo (Renfe, línea Palencia–Santander). Es conocimiento general y no se verificó en esta sesión.

### Gaps
- Faltan los horarios 2026 verificados de VACL-111, Aguilar–Palencia y Palencia–Guardo, el nombre del operador de Cervera–Palencia y la existencia de transporte a la demanda de la Junta en la Pernía o el Alto Carrión.
- No hay datos de cierres invernales de Piedrasluengas (no aparece en los resultados).

---

## 7. Fuentes de meteorología y estado de la nieve

### Takeaway
AEMET da predicción de montaña para "Picos de Europa" (zona más cercana) y avisos para la "Cordillera Cantábrica de León". El boletín de peligro de aludes existe para Picos de Europa y para las **sierras del Cordel y Peña Labra**, que lindan con la Montaña Palentina oriental (Peña Labra / Valdecebollas). **No hay boletín específico de Fuentes Carrionas** (Curavacas–Espigüete).

### Cited Findings
- Predicción de montaña AEMET para Picos de Europa: hoy más 4 días — [aemet.es predicción montaña peu1](https://www.aemet.es/es/eltiempo/prediccion/montana?p=peu1&w=1)
- Boletín de peligro de aludes (temporada aproximada de diciembre a mayo; lo elabora AEMET Zaragoza a escala regional) para Pirineos, Picos de Europa, sierras del Cordel y Peña Labra y Guadarrama. Fuera de estas zonas se emiten avisos específicos — [aemet.es servicios de montaña](https://www.aemet.es/es/conocermas/montana/detalles/serv_meteo); [aemetblog](https://aemetblog.es/2018/02/03/prediccion-meteorologica-para-zonas-de-montana-en-espana/). Página del boletín: aemet.es/es/eltiempo/prediccion/montana/boletin_peligro_aludes (URL indicada en los resultados; no abierta).

### Inferences
- Para la app: enlazar AEMET Picos de Europa y el boletín de aludes de Cordel–Peña Labra, más un pronóstico por punto (meteoblue o mountain-forecast) en las coordenadas de Curavacas y Espigüete de §4.

### Gaps
- No se verificaron las URLs de meteoblue ni de mountain-forecast, ni webcams (p. ej. Piedrasluengas o Aguilar), ni fuentes de espesor de nieve (estaciones automáticas de AEMET o CHDuero). Tampoco se comprobó si existe una zona AEMET "Cordillera Cantábrica" que cubra Palencia.

---

## 8. Datos geográficos abiertos para 3D (MDT, ortofoto, OSM)

### Takeaway
La mejor base de terreno es el **MDT02 (2ª cobertura LiDAR PNOA) o el MDT05 del CNIG**, con licencia **CC BY 4.0** (atribución "© Instituto Geográfico Nacional / scne.es"). Se completa con la ortofoto PNOA (WMTS del IGN) y con OSM (ODbL) para los POI. La Junta (IDECyL) publica un MDT propio y la capa de equipamientos de uso público.

### Cited Findings
- MDT05: malla de 5 m obtenida del LiDAR PNOA (1ª cobertura), con la restricción de uso "MDT05 CC BY 4.0 SCNE" — [INSPIRE Geoportal spaignMDT05](https://inspire-geoportal.ec.europa.eu/srv/api/records/spaignMDT05)
- MDT02 (2ª cobertura): https://centrodedescargas.cnig.es/CentroDescargas/modelo-digital-terreno-mdt02-segunda-cobertura — [EEA data](https://cis2.eea.europa.eu/data/912). Una presentación de 2019 hablaba de CC BY 3.0 ES ([IDEE JIIDE2019](https://idee.es/resources/presentaciones/JIIDE19/dia_24/AUDITORIO_PRINCIPAL/1.Sesion_1_Nuevos_Desarrollos/2_MapaLidar_JIIDE2019.pdf)). Hay una discrepancia de versión, aunque la licencia actual del Centro de Descargas es CC BY 4.0 — [datos.gob.es Centro de Descargas](https://datos.gob.es/es/aplicaciones/centro-de-descargas)
- MDS05 (modelo de superficie, útil para vegetación y edificios) — [IDEE spaignMDS](https://idee.es/csw-inspire-idee/static/api/records/spaignMDS); Mapa LiDAR 2,5 m — [datos.gob.es](https://datos.gob.es/es/catalogo/e00125901-spaign-mapa-lidar); WCS MDT — [INSPIRE spaignwcs_mdt](https://inspire-geoportal.ec.europa.eu/srv/api/records/spaignwcs_mdt)
- Nubes de puntos PNOA-LiDAR (procesado y distribución) — [pnoa.ign.es PDF](https://pnoa.ign.es/resources/archivos/pdf/Procesado_distribucion_nubes_puntos_proyecto_PNOA-LiDAR.pdf)
- MDT de Castilla y León (IDECyL) — [idecyl.jcyl.es metadato](https://idecyl.jcyl.es/geonetwork/srv/api/records/SPAGOBCYLCITDTSELMDT0811)
- Consulta OSM preparada (`amenity=shelter`, `tourism=alpine_hut|wilderness_hut|viewpoint|camp_site|hostel|information|museum|picnic_site`, `natural=spring`, `amenity=drinking_water|parking|doctors|clinic|hospital|pharmacy|bus_station`, `aeroway=helipad`, `emergency=landing_site`, `railway=station`; bbox 42.75,-4.85,43.05,-4.05): archivo `overpass_query_poi.overpassql`. Licencia OSM: ODbL 1.0, con atribución "© OpenStreetMap contributors" (conocimiento general; no se abrió la página de licencia en esta sesión).

### Inferences
- Para la app 3D: MDT02 (2 m) en la zona de cumbres (Curavacas, Espigüete, Peña Prieta) y MDT05 o MDT25 para el resto; textura con la ortofoto PNOA (WMTS `https://www.ign.es/wmts/pnoa-ma`, conocimiento general, no verificado). Hojas MTN50 que cubren la zona (inferencia): 0081, 0082, 0106, 0107, 0132, 0133. **Verificar.**
- Si el producto final mezcla datos IGN y OSM, hay que cumplir las dos licencias: atribución IGN (CC BY 4.0) y ODbL "share-alike" si se redistribuye una base de datos derivada de OSM.

### Gaps
- No hay extracción OSM (red bloqueada). No se confirmó la fecha del vuelo LiDAR de 2ª o 3ª cobertura en Palencia norte, ni la URL exacta del servicio de "equipamientos de uso público" de IDECyL.
