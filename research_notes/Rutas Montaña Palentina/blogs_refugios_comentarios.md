# Montaña Palentina: refugios, textos descriptivos y comentarios de usuarios (relleno de huecos)

Fecha de la investigación: 21-11-2026. Completa las secciones 3, 4 y 5 y los puntos 6, 21 y 22 de "Pendientes" del informe `reports/Rutas Montaña Palentina.md`. Todo está resumido con palabras propias. Leyenda: ✅ leído directamente en la fuente · ⚠️ solo fragmento del buscador, o fuente leída con dudas · ❓ sin confirmar o inferencia.

## 0. Cómo se obtuvo y qué quedó bloqueado

| Host | Resultado | Consecuencia |
|---|---|---|
| refugioslibres.com | ✅ Accesible con cortes intermitentes (timeouts; funcionó al reintentar). Se leyeron 13 fichas. | **Las coordenadas públicas son "zona aproximada"** (`approx:1`). Las exactas solo se ven con cuenta, y no se creó ninguna. |
| es.wikipedia.org | ✅ Se leyeron las páginas HTML (la API devolvió "too many requests"; se espaciaron las peticiones). | Uso: datos fácticos reescritos. Licencia CC BY-SA 4.0: **los hechos se pueden usar libremente, pero copiar texto literal obliga a atribuir y compartir igual**. |
| pyrenaica.emf.eus | ✅ El PDF del artículo 5998 se leyó completo. | — |
| www.komoot.com | ✅ Se leyeron las guías y los highlights; los consejos (*tips*) de usuarios salen del JSON incrustado. | Solo enlazar. Los datos fácticos (coordenadas de highlights) son orientativos. |
| www.escapadarural.com | ✅ Blog leído. | — |
| www.summitpost.org | ❌ 403 Cloudflare "Attention Required", también al reintentar pasados 30 s. **No se ha intentado saltar la protección.** | Solo fragmentos del buscador ⚠️ |
| www.guiarepsol.com | ❌ 418 (Akamai), también al reintentar. | Solo fragmentos del buscador ⚠️ |
| Wikiloc | No se ha intentado acceder (Cloudflare, por instrucción). | — |
| Otros blogs | Solo fragmentos de WebSearch ⚠️ | — |

**Aviso importante sobre refugioslibres.com:** casi todas las reseñas del "libro de visitas" parecen **generadas o de relleno**. Las firman cuentas como "Test Meta", "rflgo Scouts", "Oriol Scouts", "Nuria Val" y "Raul Rocallissa", con frases de plantilla ("fregadero pequeño pero funcional", "coger agua del grifo antes de que se llenase la cola", "ambiente entre peregrinos", "literas que crujen") que no cuadran con los servicios descritos en la propia ficha. **No deben usarse como estado real** ❓. Se tratan como fiables las **descripciones** de las fichas (autores Luis Cano y Jon Ander Espés Romero, sin fecha) y una sola reseña con aspecto genuino (Joseba99, Cabaña de Naranco, julio de 2026).

---

## 1. Refugios, chozos y cabañas

### 1.1 Inventario de refugioslibres.com (Palencia y zona de borde)

Se extrajeron las 702 fichas del mapa incrustado en la página de Castilla y León y se filtraron por la caja 42,6–43,25 N / 5,2–3,9 O. En la vertiente palentina **solo hay 5 fichas**. No hay ficha de Postil de Soña, Tenadas de Lores, Golobar, Corral, Tierraconcejo ni de ningún chozo del Ves. "Coord. aprox." es la zona pública, **que no sirve como posición** (en Mazobre falla por ~5 km; ver §1.2).

| Nombre (ficha) | Coord. aprox. pública | Alt. | Plazas | Estado según la ficha | Servicios / agua | Último dato | URL | Conf. |
|---|---|---|---|---|---|---|---|---|
| **Refugio Mazobre** | 42.9607, −4.7347 (aprox., errónea) | 1.559 m | 10 | "Buenas condiciones"; dos plantas: abajo chimenea, mesas y bancos; arriba altillo para dormir. Al pie del Espigüete | Chimenea, mesa, señalizado con carteles, pista asfaltada a <500 m. Sin dato de agua | Ficha sin fecha; 1 reseña "hace 1 año" (sospechosa) | [ficha](https://www.refugioslibres.com/refugios/refugio-mazobre) | ✅ descripción / ❓ fecha |
| **Refugio de Pescadores Campoluengo** | 42.9602, −4.5982 (aprox.) | 1.357 m | 6 | "Buen estado"; junto al río Carrión, a pocos km de Vidrieros. Chimenea, mesa con bancos. **"Al ser fácilmente accesible no es difícil encontrarlo ocupado"**. Propiedad: "Ayto Vidrieros" (sic; Vidrieros es pedanía de Triollo) | Leña escasa, **río a <100 m**, pista sin asfaltar a <100 m | Ficha sin fecha; 2 reseñas "hace 2 años" (sospechosas) | [ficha](https://www.refugioslibres.com/refugios/refugio-de-pescadores-campoluengo) | ✅/❓ |
| **Refugio de Santa Marina** | 42.9640, −4.5565 (aprox.) | 1.455 m | "0" (dato vacío en la ficha) | Refugio de pescadores en el Valle de Pineda, cerca de la confluencia del arroyo de Arauz con el Carrión. Dos niveles: abajo chimenea, mesa y sillas; arriba, por trampilla, **sitio para ~8 personas** | Leña escasa, **río a <100 m**, pista sin asfaltar a <2 km | Ficha sin fecha; 1 reseña "hace 1 año" (sospechosa) | [ficha](https://www.refugioslibres.com/refugios/refugio-de-santa-marina) | ✅/❓ |
| **Cabaña de Mollorente (o del Pano)** 🆕 | 42.9399, −4.6367 (aprox.) | 1.829 m | 3 | Ladera sur del Pico Pando, en las estribaciones del Curavacas. Se sube desde Vidrieros por una pista que sale de la iglesia, **en mal estado y no apta para vehículos** | Chimenea, mesa, cama, leña escasa, **fuente a <100 m**, pueblo a <5 km | Sin fecha; sin reseñas | [ficha](https://www.refugioslibres.com/refugios/cabana-de-mollorente) | ✅ / ❓ estado actual |
| **Refugio de Cristo Sierra** 🆕 | 42.8276, −4.7681 (aprox.) | 1.635 m | 6 | En un cruce de pistas entre Valcobero y Valsurbio. Dos estancias: una amplia con chimenea y mesa, y una **capilla** pequeña | Chimenea, mesa, leña, **fuente a <1 km**, pista sin asfaltar a <100 m | Sin fecha; sin reseñas | [ficha](https://www.refugioslibres.com/refugios/refugio-de-cristo-sierra) | ✅ / ❓ |

Fichas de la zona de borde, León y Cantabria 🟧🟦 (útiles para Peña Prieta desde Llánaves, Lechada y Barniedo):

| Nombre | Ubicación según la ficha | Alt. | Plazas | Estado | URL |
|---|---|---|---|---|---|
| Cabaña de Naranco 🟧 | Vega del Naranco, ~3 km al E de Llánaves de la Reina | 1.534 m | 6 | Buen estado, dos estancias, mesas, sillas y chimenea. **Reseña genuina (~jul-2026):** algo de polvo; la puerta se cerró calzándola con una piedra; pequeño pero suficiente para pasar la noche | [ficha](https://www.refugioslibres.com/refugios/cabana-de-naranco) ✅ |
| Cabaña Linarucas 🟧 | Arroyo Culebrejas, desde Llánaves | 1.522 m | 5 | Pequeño refugio de piedra, vacío ("no tiene nada") | [ficha](https://www.refugioslibres.com/refugios/cabana-linarucas) ✅ |
| Refugio Majada de los Cantos 🟧 | Arroyo Culebrejas, pasada Linarucas | 1.558 m | 5 | Buen estado, chimenea | [ficha](https://www.refugioslibres.com/refugios/refugio-majada-de-los-cantos) ✅ |
| Refugio del Pico del Calar 🟧 | Valle de Lechada, ~5 km desde el área recreativa de Portilla de la Reina | 1.422 m | 5 | Chimenea y mesa; **litera en mal estado** | [ficha](https://www.refugioslibres.com/refugios/refugio-del-pico-del-calar) ✅ |
| Cabaña Machorril 🟧 | 4 km al E de Barniedo de la Reina (camino de Valponguero) | 1.292 m | 5 | Mesa, sillas, chimenea, cama | [ficha](https://www.refugioslibres.com/refugios/cabana-machorril) ✅ |
| Refugio Rozalacalle 🟧 | ~7 km al E de Barniedo; se llega en coche por pista de tierra | 1.398 m | 6 | Buen estado; chimenea, mesas, sillas | [ficha](https://www.refugioslibres.com/refugios/refugio-rozalacalle) ✅ |
| Refugio Braña de los Tejos 🟦 | ~5 km al S de Cicera (Peñarrubia), al N del collado de Pasaneu | 1.273 m | 5 | **Mal estado**, pero sirve para pernoctar | [ficha](https://www.refugioslibres.com/refugios/refugio-brana-de-los-tejos) ✅ |
| Refugio del Murón 🟦 | ~4 km de Cicera | 924 m | 5 | Chimenea y banco de piedra; puertas y ventanas cierran bien | [ficha](https://www.refugioslibres.com/refugios/refugio-del-muron) ✅ |

### 1.2 Refugios y abrigos en komoot (highlights con coordenadas y consejos de usuarios)

Las coordenadas son el punto del highlight en komoot, verificado en su página ✅. Son orientativas para cruzarlas con OSM.

| Highlight komoot | Coordenadas · alt. | Comentarios de usuarios (fecha) | Interpretación | URL |
|---|---|---|---|---|
| "Refugio Libre en el Parque Natural Montaña Palentina" | 42.96051, −4.60581 · 1.424 m | "No es un hotel de 5 estrellas, pero te ayudará a pasar la noche; buen sitio para resguardarse de la lluvia; chimenea pequeña" (20-06-2023) | ❓ Probablemente el **Refugio de los Pescadores / Campoluengo** (cuadra con la zona aproximada de refugioslibres, 42.9602, −4.5982, junto al Carrión aguas arriba de Vidrieros) | [5837344](https://www.komoot.com/highlight/5837344) |
| "Pequeño refugio libre" | 42.96098, −4.60563 · 1.490 m | "Plataforma elevada y chimenea; la chimenea tira mal pero se puede hacer fuego; jabalíes y corzos en las laderas del Curavacas; quizá algún oso" (31-05-2021) | ❓ Mismo edificio que el anterior (a 50 m). El "altillo" encaja | [3306171](https://www.komoot.com/highlight/3306171) |
| "Refugio libre" (el título en griego de la guía dice "Καταφύγιο") | **43.02377, −4.55316 · 1.614 m** | "Otro refugio libre de la montaña palentina; chimenea, leña y mesa; déjalo limpio" (09-09-2022). Pregunta sin respuesta sobre plazas (05-09-2024) | ❓ Al norte de Lores, en la cabecera del valle de Lores: **candidato a "Chozo de las Tenadas de Lores"** | [4976372](https://www.komoot.com/highlight/4976372) |
| Refugio de Golobar | 42.96744, −4.33746 · 1.791 m | "Abandonado, pero con vistas maravillosas; carretera asfaltada con poco tráfico" (29-12-2022). "Era parte de un proyecto de Parador y estación de esquí; hoy solo lo usan pastores y ganado" (25-04-2023) | **No es un refugio útil**: es un edificio abandonado que se usa como corral (ver Wikipedia, §2) | [3394566](https://www.komoot.com/highlight/3394566) |
| Vivac Agujas de Cardaño | 43.01573, −4.74466 | Texto promocional (27-06-2025) | Vivac sin construcción. **Acampar está prohibido y el vivac solo es autorizable** (informe §11) | [3943784](https://www.komoot.com/highlight/3943784) |
| Chozo Tonino (cueva) | 42.92741, −4.25569 · 1.288 m | "Está junto al camino, pero se pasa de largo si no lo buscas; es una pequeña cueva donde se escondió un barruelano en la posguerra" (08-06-2023) | POI histórico (Barruelo), no es abrigo | [4444414](https://www.komoot.com/highlight/4444414) |
| Chozo del Prau del Toru | 42.93861, −4.33156 · 1.417 m | "Construcción típica apoyada en una gran roca; algunas se siguen usando como refugio" (29-12-2022) | Chozo de pastores, zona de Brañosera / Valdecebollas | [4444419](https://www.komoot.com/highlight/4444419) |
| Refugio de Covalagua | 42.76982, −4.13132 · 1.081 m | "Lugar tranquilo para descansar o pasar el día en familia en las mesas que rodean el refugio" (01-09-2022; 26-05-2024) | Abrigo con merendero. Para `mp-covalagua-*` | [6659058](https://www.komoot.com/highlight/6659058) |

Guías komoot de origen: [Refugios en Palencia (366047)](https://www.komoot.com/el-gr/guide/366047) · [Refugios en el PN (415492)](https://www.komoot.com/guide/415492).

### 1.3 Resolución de las contradicciones del informe

| Caso | Lo que había | Lo que se encontró | Veredicto |
|---|---|---|---|
| **Refugio de los Pescadores: ¿abierto o cerrado con llave?** | Walkaholic: libre, 6 plazas. Guía alpina 2018: cerrado, llaves en Vidrieros, 10 plazas | Refugioslibres (que walkaholic cita como fuente original): **libre**, 6 plazas, buen estado, a menudo ocupado por lo fácil del acceso, río a <100 m. komoot: dos usuarios lo describen como abrigo libre utilizable (may-2021 y jun-2023). La búsqueda no encontró ninguna mención de llave posterior a 2018 | ⚠️ **Lo más probable es que esté abierto** (evidencia de usuarios 2021–2023). La "llave" de la guía de 2018 puede referirse a otro edificio o a una situación ya cambiada. La posición tampoco está resuelta: walkaholic da 42.9384, −4.64265 (a 1,6 km de Vidrieros), mientras refugioslibres y komoot apuntan a ~42.9605, −4.6058, a ~5 km por la pista del Carrión. Etiqueta para la app: "abrigo libre, estado no verificado (2023)". Hay que confirmarlo en la Casa del Parque o con OSM |
| **Mazobre** | Guía alpina: 20 plazas. Walkaholic: ~10 durmiendo | Refugioslibres: **10 plazas**, dos plantas, "buenas condiciones", señalizado con carteles. Por los fragmentos de las fichas de la Junta y Terranostrum: a mitad del camino Pino Llano–cascada sale un desvío a la izquierda hacia el refugio, a ~30 min del aparcamiento, al pie de la cara NE del Espigüete ⚠️ | ✅ Existe y está en uso. **Capacidad real para dormir ≈ 10** (las 20 plazas de la guía son probablemente de abrigo). Coordenada todavía ❓: la zona de refugioslibres no vale. Estimación: entre Pino Llano (km 2,5 de la carretera Cardaño de Abajo–Cardaño de Arriba) y la cascada (highlight 42.95929, −4.79297) |
| **Refugio del club Espigüete (Cardaño de Arriba)** | Destruido por un alud en febrero de 2015 | Un estudio académico ([UVa, nieve y aludes](https://uvadoc.uva.es/bitstream/handle/10324/40660/Nieve-aludes-Monta%c3%b1a-Cant%c3%a1brica.pdf.pdf?sequence=1)) sitúa el alud entre el 9 y el 13-02-2015, con más de 2 m de nieve. Fue el daño principal; también afectó al camino, al tejado de la iglesia y al tendido eléctrico ⚠️. En un [foro meteorológico](https://foro.tiempo.com/nevadon-en-la-montana-palentina-febrero-2015-t145640.60.html) el presidente del club lo confirma a la SER y lo ubica al norte del pueblo, entre el camino al Pico Murcia y el arroyo que baja del Pozo de las Lomas ⚠️. No hay rastro de reconstrucción | ✅ Destruido (2015). **No mostrarlo como refugio.** Como mucho, POI "ruinas / zona de aludes" en la salida de `mp-pena-prieta-cardano` y `mp-murcia-valcabe` |
| **Tenada(s) de Lores** | Blog 2017: "muy bueno", 8–10 plazas | No hay ficha en refugioslibres. El buscador solo devuelve "Tenadas de Resoba / de Santibáñez / Tenadas Viejas" en PeakVisor ⚠️. Candidato en komoot: refugio libre en 43.02377, −4.55316 (1.614 m), con chimenea, leña y mesa (2022) ❓ | ❓ Probablemente existe y estaba en uso en 2022. La identidad no está confirmada |
| **Postil de Soña** | Libre, 20 plazas (2018) | No hay ficha en refugioslibres ni comentarios recientes. Mountain-forecast lo pone como "refugio de pago, 20 plazas, chimenea" (clasificación poco creíble) ⚠️; PeakVisor solo lo lista ⚠️ | ❓ Sin datos posteriores a 2018. Nota de toponimia: Postil de Soña es también una cumbre del cordal Curruquilla–Postil de Soña–Hoya Contina, al E del Curavacas (Wikipedia), y el collado de Soña (2.217 m) queda sobre el Pozo del Ves (Pyrenaica). El refugio de 1.526 m estaría al pie |
| **Santa Marina** | Libre, 20 plazas (2018) | Refugioslibres: refugio de pescadores de dos niveles en el Valle de Pineda (confluencia Arauz–Carrión), con sitio para dormir ~8 y río a <100 m ✅ | ✅ Existe; **capacidad para dormir ≈ 8**. Fecha del estado ❓ |
| **Golobar** | "En ruinas" (2016) | Wikipedia: edificio del Parador abandonado en 1973, usado primero como refugio y hoy como **corral de ganado**; propiedad de la Diputación. komoot 2022–2023: abandonado, con ganado | ✅ **No apto como refugio.** Sí es trailhead (aparcamiento al final de la PP-2203, 1.840 m) |

---

## 2. Textos descriptivos (datos de es.wikipedia.org, resumidos)

Licencia: Wikipedia CC BY-SA 4.0. Los datos de abajo están reformulados. Si se reutiliza texto literal, hay que citar "Wikipedia, CC BY-SA 4.0" y compartir igual. Todas las fichas están ✅ (leídas el 21-11-2026). Entre corchetes, el slug del informe.

### Curavacas (2.524 m) [mp-curavacas-vidrieros, mp-curavacas-canal-sur, mp-dip-12] · [artículo](https://es.wikipedia.org/wiki/Curavacas)
- Es la **cumbre más alta situada íntegramente en Palencia**. El Pico del Infierno (2.537 m) es más alto, pero muchos lo consideran una prolongación de Peña Prieta. Término de Triollo, junto a Vidrieros. Prominencia ~472 m.
- **Roca:** conglomerado oscuro (el "conglomerado de Curavacas") cubierto de líquenes que le dan un tono verdinegro. Contrasta con las calizas y granitos de alrededor.
- **Tres cumbres:** Este (la más alta), Medio y Oeste. La cara S, que es la fácil, baja hacia Vidrieros; la N cae al Valle de Pineda. La **cara NE** es una de las paredes más difíciles de la Cordillera Cantábrica.
- **Glaciarismo:** al pie de la cara N y del cordal Curruquilla–Postil de Soña–Hoya Contina están el **Pozo Curavacas** y los **Pozos del Ves**, lagunas glaciares que alimentan el Carrión. El río rodea el macizo desde su nacimiento hasta Vidrieros, donde recibe el arroyo Valdenievas.
- **Historia:** la primera ascensión deportiva conocida es de **agosto de 1947**, por el notario de Cervera Luis García Guinea; de ahí el nombre de la **"senda del notario"**. El **16-04-1957**, la "Cordada de los Faquires" quedó atrapada por una nevada y **murieron tres montañeros**; el rescate de los cuerpos duró más de un mes (hay un documental de 2006). En **enero de 2010** un alud mató a dos escaladores.
- **Espeleología:** desde el 2000 se explora una sima de −322 m en el Alto del Ves.
- **Flora:** piso alpino con siempreviva (*Sempervivum*) y, en las faldas, brezo y arándano. Junto al Pozo Curavacas hay tormentilla, brezo de turbera y *Pedicularis*.

### Espigüete (2.450 m) [mp-espiguete-sur, mp-espiguete-norte, mp-dip-01] · [artículo](https://es.wikipedia.org/wiki/Espig%C3%BCete)
- Es una **pirámide caliza aislada**, la silueta más reconocible del parque. Término de Velilla del Río Carrión, junto a Cardaño de Abajo; la vertiente oeste es de Valverde de la Sierra (León). Prominencia ~474 m.
- La cara S tiene relieve suave (la pedrera) y la N, paredes verticales. Pasa buena parte del invierno nevado.
- **Límites geológicos:** al N, el cabalgamiento que encauza el arroyo de Mazobres; al E, el sinclinorio del arroyo de las Lomas; al O, laderas metamórficas; al S, las pizarras y areniscas de la Formación Cervera. Por dentro es **muy kárstico**, con simas, cuevas y ríos subterráneos.
- **Endemismo:** *Sempervivum giuseppii*, que solo crece en este pico. Lo descubrió Paul Leon Giuseppi en 1935.
- **Historia:** la primera ascensión documentada es del geólogo **Casiano de Prado en 1854**; Aymar de Saint-Saud subió en 1892. Pyrenaica atribuye a **Juan Díaz-Caneja** la primera ascensión de la **cara E en 1915** ✅ ([PDF](https://pyrenaica.emf.eus/wp-content/uploads/aldizkariak/286/artikulua_5998.pdf)). SummitPost dice que la **arista E se escaló por primera vez en 1946** ⚠️ ([ruta](https://www.summitpost.org/route/474243/north-face-classic-eastern-ridge.html)).

### Peña Prieta (2.540,5 m) y Pico del Infierno (2.537 m) [mp-pena-prieta-cardano, mp-pena-prieta-llanaves, mp-pena-prieta-san-glorio, mp-dip-06] · [artículo](https://es.wikipedia.org/wiki/Pe%C3%B1a_Prieta)
- Es la **cumbre más alta del macizo de Fuentes Carrionas** y la más alta de la Cordillera Cantábrica fuera de los Picos de Europa. La cima es cántabra (Vega de Liébana). El vértice geodésico marca 2.539,10 m en la base del pilar. Prominencia de 929 m (el artículo del macizo da 1.088 m).
- **Toponimia:** "prieta" significa oscura, por el conglomerado de la formación Curavacas, que se ennegrece con la intemperie.
- **Glaciarismo:** del pico arrancan el **circo de Riofrío** (al N, con los puertos de Riofrío) y el circo de la **laguna de Fuentes Carrionas** (al S), donde nace el Carrión.
- **El Pico del Infierno** está a 171 m al S de la cima y tiene 2.537 m (43.02218, −4.73184). Es el **punto más alto de Palencia de facto**. El **Mojón de Tres Provincias** (2.497–2.499 m) es el punto donde se unen León, Cantabria y Palencia. Por la ruta de Llánaves se pasa por el Cubil del Can (2.419 m).
- Las cotas no coinciden del todo entre artículos de Wikipedia (2.538 / 2.539 / 2.540,5 m). Conviene seguir usando Mendikat, como en el informe.

### Macizo de Fuentes Carrionas [mp-integral-fuentes-carrionas, mp-circular-lagos, mp-of-lomas] · [artículo](https://es.wikipedia.org/wiki/Fuentes_Carrionas)
- Tiene **52 cumbres de más de 2.000 m** con al menos 30 m de prominencia (15 con 100 m o más; 5 con 300 m o más: Peña Prieta, Curavacas, Espigüete, Lezna y Horca de Lores). **11 cumbres superan los 2.400 m.**
- Es una zona tectónicamente muy compleja, con muchas fallas y calizas muy diaclasadas (mucho karst). El **glaciarismo cuaternario** dejó circos, valles en artesa y sistemas de morrenas.
- **Lagos glaciares:** laguna de Fuentes Carrionas (~2.220 m), Pozo de las Lomas (~2.080 m), lago del Ves (~2.050 m) y Pozo Curavacas (~1.800 m).
- **Toponimia:** Plinio el Viejo habla de un "campo carrinense" con dos fuentes juntas, una que expulsa lo que recibe y otra que lo absorbe. Se cree que se refería a las lagunas donde nace el Carrión. Es la primera mención del nombre, que sustituyó al más antiguo de "Nubis".
- Es **Reserva Nacional de Caza desde 1966**. Las especies emblemáticas son el oso pardo y el urogallo.

### Parque Natural Montaña Palentina · [artículo](https://es.wikipedia.org/wiki/Parque_natural_Monta%C3%B1a_Palentina)
- Antes se llamaba "Fuentes Carrionas y Fuente Cobre–Montaña Palentina", por los nacimientos del Carrión y del Pisuerga. El PORN se aprobó por **Decreto 140/1998** y el parque se **declaró en 2000** (publicado el 5 de julio de 2000).
- Lo que justificó la declaración: el **sabinar albar más septentrional** (Peña Lampa), los endemismos *Artemisia cantabrica* y *Echium cantabricum*, y el oso pardo.
- El relieve contrasta entre la cuenca del Carrión (pendientes fuertes con poca vegetación) y la del Pisuerga (más arbolada y suave). Los inviernos son fríos y los veranos suaves: según el artículo, unos 3,5 °C de media en invierno y 19,5 °C en verano.
- **Bosques singulares:** la Tejeda de Tosande, el **Pinar de Velilla** (uno de los pocos pinares naturales de la Cordillera) y el sabinar de Peña Lampa.
- **Fauna:** oso, urogallo, lobo, rebeco, ciervo, nutria, desmán, perdiz pardilla, treparriscos y víbora de Seoane, entre otras.

### Tejeda de Tosande [mp-of-tosande, mp-dip-24] · [artículo](https://es.wikipedia.org/wiki/Tejeda_de_Tosande)
- Es una de las mayores concentraciones de tejo de la Península. Está en la ladera N de **Peña Oracada (1.818 m)**, en la sierra de la Peña (Dehesa de Montejo), en el valle de Tosande (o "Tosante").
- Los tejos crecen entre **1.300 y 1.500 m**, dentro de un hayedo, sobre sustrato paleozoico. Son **bosques relictos del Terciario**: tejos maduros y huecos donde anidan aves y viven martas.
- Tres ejemplares están en el **Catálogo de especímenes vegetales de singular relevancia** de Castilla y León. El tejo tiene protección de "atención preferente" (Decreto 63/2007).
- El aparcamiento está en la C-626, ~6 km de Cervera hacia Guardo. El sendero está acondicionado con pasarelas y puentes, y acaba en un mirador. **Está prohibido salirse del sendero** y coger ramas o frutos.

### Fuente Cobre / Cueva del Cobre [mp-of-fuente-cobre, mp-valdecebollas-*] · [artículo](https://es.wikipedia.org/wiki/Fuente_Cobre)
- Se tuvo durante mucho tiempo por el nacimiento del Pisuerga, pero el río **nace en el circo glaciar de Covarrés**, al pie del Valdecebollas. Se sume en el **sumidero del Sel de la Fuente** y reaparece **~3 km más abajo** en la cueva.
- La cueva está en el Valle de los Redondos (La Pernía); se deja el coche en Santa María de Redondo, a 22 km de Cervera. Madoz la cita en 1849.
- En **septiembre de 1980**, cinco vecinos del valle guiados por un espeleólogo de Avilés cruzaron a nado el sifón (8 °C), que una sequía excepcional había convertido en laguna. En 1982 se confirmó el origen en Covarrés.
- Las exploraciones (1987–2011) superan los **7,5 km** de galerías, con un desnivel de +202 m. Hay conexiones parciales con el Torcón Mosquitero y la cueva del Humo.
- Para la app: **POI geológico, no fuente de agua potable** (coincide con el informe §5).

### Valdecebollas (2.144 m; el vértice marca 2.139 m) y El Golobar [mp-valdecebollas-branosera, mp-valdecebollas-golobar, mp-dip-37] · [artículo](https://es.wikipedia.org/wiki/Valdecebollas) · [El Golobar](https://es.wikipedia.org/wiki/El_Golobar)
- Es el macizo de La Cebollera, un contrafuerte S de la sierra de Híjar, y marca el límite E de la Montaña Palentina. En la cima está el **"Torreón"**, una torre cilíndrica escalonada con placa, buzón y vértice. **Desde 1965 se celebra allí una misa el primer domingo de agosto** (vecinos de Barruelo y Brañosera): ese día habrá gente en la cumbre.
- Su vertiente N cierra el **circo glaciar de Covarrés**, nacimiento del Pisuerga. En invierno nieva mucho y se forman **cascadas de hielo** en las faldas.
- **El Golobar:** la carretera PP-2203 (6,5 km desde el desvío de Salcedillo) es **la más alta de la provincia (1.840 m)**. No tiene mantenimiento y **ha sufrido desprendimientos**. El edificio de la cima es el Parador inacabado de 1973, hoy corral de ganado. La estación de esquí proyectada en los años 60 nunca se terminó.

### Peña Labra (2.018 m; el vértice marca 2.028,7 m) y Tres Mares (2.171–2.172,6 m) [mp-penalabra-tresmares, mp-tres-mares-redondo] · [Peña Labra](https://es.wikipedia.org/wiki/Pe%C3%B1a_Labra) · [Tres Mares](https://es.wikipedia.org/wiki/Pico_Tres_Mares)
- Peña Labra aparece como "Peña Luenga" en el Libro de la Montería. La cima está en Palencia y la cresta hace de límite con Cantabria. Tiene una cruz junto al vértice.
- **Toponimia en disputa:** el IGN llama "sierra de Peña Labra" a lo que tradicionalmente es la **sierra de Híjar**. Autores como Hernández-Pacheco y la cartografía del siglo XIX defienden "Híjar".
- **Tres Mares** es la **única cumbre peninsular que vierte a tres mares**: el Nansa (Cantábrico), el Híjar–Ebro (Mediterráneo) y el Pisuerga–Duero (Atlántico). Antes se llamaba "Pico Negro", "Cueto Negro" o "Pico de los Asnos". La cresta es de conglomerado cuarcítico triásico. Una pista de la estación de Alto Campoo llega a la cima. Es LIC y ZEPA.
- **Glaciarismo en la sierra de Híjar:** más de diez cuencas glaciares de tipo alpino, de entre 70.000 y 18.000 años. En la vertiente S está el complejo Covarrés–Sel de la Fuente–Valdecebollas–Canalejas–Honcamesa ([sierra de Híjar](https://es.wikipedia.org/wiki/Sierra_de_H%C3%ADjar)).

### Pico Murcia (2.352 m) [mp-murcia-valcabe, mp-dip-03] · [artículo](https://es.wikipedia.org/wiki/Pico_Murcia)
- El vértice está en el **límite entre León y Palencia**, en el cordal Murcia–Cuartas–Las Lomas. Desde Cardaño de Arriba son ~6 km y casi 1.000 m de desnivel. Tiene buzón.
- La dificultad se considera media-baja, **pero ha habido varios accidentes, sobre todo en invierno**.

### Pico Lezna (2.208 m) [mp-lezna] · [artículo](https://es.wikipedia.org/wiki/Pico_Lezna)
- Separa La Pernía (E) de Cervera (O) y está junto a los puertos de Pineda. Al S, el Carrión riega la vega de Correcaballos. El Pumar (2.066 m) está a 1,2 km. Las rutas directas salen de **Cucayo (Cantabria) y de Lores**.

### Peña Redonda (1.993 m) y Sierra del Brezo [mp-pena-redonda, mp-dip-23, mp-fraile, mp-of-gigante] · [Peña Redonda](https://es.wikipedia.org/wiki/Pe%C3%B1a_Redonda) · [Sierra del Brezo](https://es.wikipedia.org/wiki/Sierra_del_Brezo)
- Es caliza, entre Castrejón de la Peña y Cervera. La cruz metálica de la cima la hace "superar" los 2.000 m. Tiene vértice y una caseta con una Virgen. **Por la mañana suele estar cubierta de niebla** (aviso de orientación: coincide con los comentarios de Wikiloc del informe).
- **Acceso habitual:** desde Traspeña por pista hasta una cantera abandonada, y después senda con **hitos** por la cara S hasta el hombro E. Hay vías menos marcadas por el N, el O y desde Villanueva de la Peña.
- **Romería el primer domingo de agosto** a la Virgen de las Cumbres, con misa del obispo.
- **Leyenda del Gigante:** un gigante de San Martín de los Herreros (Valle Estrecho) se fugó a la sierra tras perder a su hija, que huyó con su amado. Murió tendido en la cumbre, y el perfil de la sierra es su cuerpo, con Peña Redonda como la barriga. Sus lágrimas brotarían en la Fuente de la Sondonada. Es el **trasfondo de la senda oficial `mp-of-gigante`**.
- La Sierra del Brezo mide ~30 km (Guardo–Cervera). Es caliza y sin arbolado (gayuba y brezo), y su techo es el **Pico del Fraile (2.025 m)**. Allí nacen el Valdavia, el Boedo y el Burejo.

### Las Tuerces [mp-tuerces-*, mp-cilda-tuerces] · [artículo](https://es.wikipedia.org/wiki/Las_Tuerces)
- Es un laberinto kárstico en calizas del **Cretácico Superior**, en el borde occidental de los páramos de La Lora, donde la Cordillera Cantábrica se encuentra con la Cuenca del Duero. El **Cañón de la Horadada** (Pisuerga) se ve entero desde el Monte Cildá.
- El PORN se inició en 1992. Según Wikipedia (texto antiguo) seguía sin declarar. El Turismo de Castilla y León lo presenta como "Paisaje Protegido y Monumento Natural", y un medio lo fecha como Monumento Natural en 2019 ⚠️. **Hay que confirmar la figura de protección vigente** ([turismocastillayleon](https://www.turismocastillayleon.com/douro/es/espacios-naturales/paisaje-protegido-monumento-natural-tuerces) ⚠️).

### Covalagua [mp-covalagua-corta, mp-covalagua-integral, mp-franceses-lobos] · [artículo](https://es.wikipedia.org/wiki/Covalagua)
- Es un espacio kárstico de Pomar de Valdivia (Revilla de Pomar, Pomar de Valdivia y Respenda de Aguilar). La cueva-surgencia del **río Ivia** deposita **toba** en gradas semicirculares que forman pequeñas cascadas hasta una balsa.
- En el mismo espacio están la **Cueva de los Franceses** (según el artículo, la única cueva visitable de Palencia), el **Pozo de los Lobos** y el **menhir del Canto Hito**.
- El bosque mezcla hayas en umbría y quejigos en solana, con tejo, acebo y avellano. El PORN se inició en 1992. Turismo CyL lo llama "Paisaje Protegido y Monumento Natural" ⚠️.

### Monte Bernorio (1.170 m; la guía da 1.178 m) [mp-bernorio] · [artículo](https://es.wikipedia.org/wiki/Monte_Bernorio)
- Es un **oppidum** cántabro de más de 120 ha (la cima plana mide ~28 ha), junto a Villarén de Valdivia, a 7 km de Aguilar. Estuvo ocupado de forma continua del **siglo VIII al I a. C.**, con indicios del Calcolítico y el Bronce.
- A 2 km, en El Castillejo (Pomar de Valdivia), hay un **campamento romano de más de 18 ha**, probablemente de dos legiones (se cita la IIII Macedonica). Se han hallado proyectiles de asedio. Tras la conquista se convirtió en *castellum* romano.
- Es **BIC (zona arqueológica) desde 1992**. Algunos autores lo identifican con la *Bergida* de las guerras cántabras. Hay **parapetos de la Guerra Civil** (octubre de 1936).
- Está en la **Lista Roja de Hispania Nostra** por un proyecto de parque eólico de 24 aerogeneradores.

### Geoparque Mundial UNESCO Las Loras · [artículo](https://es.wikipedia.org/wiki/Geoparque_Las_Loras)
- Entró en la red el **5-05-2017** (11.º geoparque español). Ocupa **95.076 ha** en **16 municipios: 5 palentinos y 11 burgaleses**.
- **Geología:** páramos calizos separados por cañones, karst (La Valdivia, Las Tuerces, La Lora), relieves estructurales (las "loras"), diapiros (Nestar), fallas y el campo petrolífero de Ayoluengo (1964).
- **Lugares en Palencia:** Covalagua, Las Tuerces, Cañón de la Horadada, Cueva de los Franceses, Monte Bernorio, Monte Cildá y el románico.

---

## 3. Descripciones de rutas, notas técnicas y consejos (por slug)

### mp-integral-fuentes-carrionas · Integral de Fuentes Carrionas — Pyrenaica n.º 286 ✅
Fuente: Iván Ruiz Rotaeche, "Integral de Fuentes Carrionas. El gran reto de la Montaña Palentina", *Pyrenaica* n.º 286 (fecha del número no verificada ❓) · [PDF](https://pyrenaica.emf.eus/wp-content/uploads/aldizkariak/286/artikulua_5998.pdf)
- **Ficha técnica:** 35 km · **+3.400 m** · 14 h 30 min en total · **PD+** · más de 20 cotas de más de 2.000 m. Lineal de Pino Llano (1.350 m) a Vidrieros (1.326 m), así que **hace falta mover el coche** o tener un segundo vehículo.
- **Itinerario:** Pino Llano → arista E del Espigüete (de noche, con frontal) → cima E (2.443 m, trepada sencilla) → Espigüete (2.451 m, unas 2 h). Bajada: no vieron clara la cabecera del canal SO y siguieron las **viras de la cara O, con un destrepe de ~6 m** de buenos agarres pero algo comprometido. Hitos hasta la arista NO, collado de Arra (1.999 m) → Pico de la Arra (2.034 m) → Cutulillos (2.041 m), con terreno roto y escobas incómodas → Hoya de Martín Vaquero (2.112 m) → Peña del Águila (2.136 m), rodeada por el E y subida por un canal con algo de ambiente → Valcabe (2.204 m) → **Pico Murcia (2.351 m): ~200 m de desnivel en 350 m** → collado de Peñas Caburdas (2.127 m) → Zamurdias (2.171 m) → Peñas Malas (2.282 m) → Frontino (2.197 m) → Guadañas (2.248 m) → Cuartas (2.451 m, buzón con forma de esquís) → Pico de las Lomas (2.444 m) → lago sobre el **Pozo de las Lomas** (mitad de la ruta) → canal empinado al collado Agujas de Cardaño / Alto del Concejo → Tres Provincias (2.499 m) → Monte Infierno (2.537 m) → Peña Prieta (2.539 m) → Alto del Concejo (2.432 m) → Tío Celestino (2.396 m) → Calderón (2.274 m) → Alto del Ves (2.192 m) → collado del Ves (2.067 m) → **Hoya Contina (2.395 m)** → *tramo más técnico*: destrepe al collado de Soña (2.217 m, sobre el Pozo del Ves), y después terrazas y canales de conglomerado (PD) → Curruquilla (2.416 m) → brecha Curruquilla → **Curavacas Oeste (2.502 m), "la más vertiginosa"**. Al bajar hay un **destrepe expuesto**: colgarse de la repisa con las dos manos y bajar los pies en adherencia hasta una terraza; después, un canal → Pico Medio (2.494 m, se puede rodear por una senda de la cara N) → Curavacas (2.524 m) → brecha y destrepe sencillo a la Torre del Callejo Grande → zigzags por el Callejo Grande → pedrera incómoda hasta el arroyo de Cabriles → **fuente junto al arroyo** → Vidrieros.
- **Agua:** el único punto de recarga fue el **Pozo de las Lomas**. No encontraron el manantial que buscaban bajo las Agujas de Cardaño. El autor llevaba consumidos 3,5 L a mitad de ruta y cogieron agua de un arroyuelo del lago, filtrada con una tela y con **pastillas potabilizadoras**. Con calor se les acabaron las reservas antes del Pico Cuartas. Al final, fuente junto al arroyo de Cabriles, ya cerca de Vidrieros.
- **Consejos:** el verano puede ser caluroso; terreno de sube y baja constante, con pedregales calizos y trepadas por conglomerado; exige buena preparación física y mental. Durmieron en furgoneta en Pino Llano, con otras campers. **Ojo: pernoctar en vehículo o vivaquear en el parque está regulado** (informe §11). La foto de un "vivac cerca de la cima del Espigüete" no se debe presentar en la app como práctica recomendada.
- Rebecos a 20 m en el Callejo Grande.

### mp-curavacas-vidrieros · Curavacas por la vía normal (Callejo Grande)
- **komoot** ✅ ([tour](https://www.komoot.com/smarttour/e1068189616/curavacas-desde-vidrieros-parque-natural-montana-palentina)): 10,17 km · +1.064 m · ~5 h 39 min · "difícil", muy buena forma física y paso seguro. El inicio (42.94161, −4.66191; 1.335 m) está **junto a un aparcamiento**. Es la ruta de senderismo más popular en torno a Triollo ([guía Triollo](https://www.komoot.com/guide/1659696/hiking-around-triollo)). Consejos de usuarios: "**ascensión muy dura por la pedrera; se requiere alguna trepada**" (21-09-2022); vistas del Pozo Curavacas y de la Curruquilla (15-05-2023). Hay variantes de **Callejo Grande** y **Senda del Notario** (texto generado, 20-02-2025).
- **komoot "Curavacas Normal Route via Callejo Grande"** ⚠️ ([fragmento](https://blog.komoot.de/smarttour/e1118937486/curavacas-normal-route-via-callejo-grande)): 10,3 km, +1.090 m. Lo más característico son las pedreras y el Callejo Grande, empinado y con piedra suelta.
- **Gulliver.it** ⚠️ ([fragmento](https://www.gulliver.it/?p=351935)): +1.204 m, dificultad alta. Al final del Callejo Grande hay una trepada corta, poco arriesgada con precaución.
- **HikingIberia** ⚠️ ([PDF](https://www.hikingiberia.com/resources/routes/es/fuentes-carrionas-curavacas.pdf)): el último tramo es muy empinado y difícil, factible para excursionistas con experiencia **solo sin nieve**. Se **cruza varias veces el arroyo de Cabriles** pisando piedras (con deshielo puede complicarse ❓).
- **viajaporlibre** ⚠️ ([fragmento](https://www.viajaporlibre.com/senderismo/ruta-curavacas-vidrieros)): sin conocimientos de alpinismo, **solo sin nieve, de junio a octubre**.
- **SummitPost** ⚠️ (solo buscador): 2.525 m, posición interior y aislada, gran mirador. Forma con Espigüete y Peña Prieta una "trilogía" que rivaliza con los Picos ([página](https://www.summitpost.org/curavacas/153553)).
- **Accidentes:** un escalador de 30 años murió por una indisposición en la **cara N** ([Vozpópuli](https://www.vozpopuli.com/sucesos/muere-un-escalador-de-30-anos-tras-sufrir-una-indisposicion-mientras-ascendia-el-pico-curavacas-en-palencia.html), fecha no verificada ⚠️). Dos escaladores heridos fueron evacuados con apoyo del grupo de rescate de Asturias ([El Mirón de Soria](https://elmirondesoria.es/soria/sucesos/evacuados-dos-escaladores-heridos-en-curavacas/amp), fecha no verificada ⚠️).

### mp-curavacas-canal-sur · Curavacas Canal Sur (invernal)
- No hay datos nuevos. Wikipedia recuerda el alud mortal de **enero de 2010** y la tragedia de 1957 con nevada repentina: refuerzan el icono "material invernal / aludes".

### mp-espiguete-sur · Espigüete por la cara sur (pedrera), desde Cardaño de Abajo
- **Guía Repsol "Espigüete con perro"** ⚠️ (bloqueada, 418; [URL](https://www.guiarepsol.com/es/viajar/con-mi-mascota/ruta-con-perro-espiguete-palencia/); el buscador la fecha "hace unos dos años", ~2024): salida de Cardaño de Abajo (P-210). Pista de hormigón desde la plaza; a ~500 m, desvío a la izquierda por pista forestal hasta la base. **Agua: llenar en la gran fuente del pueblo; no hay más en todo el recorrido.** Aproximación fácil (~200 m de desnivel por pista). La **pedrera mide menos de 1 km pero sube más de 400 m**: conviene ir por el **lado derecho del canal**, con roca más firme. Cumbre: ~5,5 km y 3 h 30 min a la ida, con un último tramo de cresta ancha de ~100 m. Bajada por el mismo sitio, ~2 h. **Perro atado** en el parque y en el collado, que en hora punta está concurrido. **Las aristas E y N no son para mascotas.** En invierno, solo para expertos; el verano y el principio del otoño son más amables (salida del autor en octubre).
- **Terranostrum** ⚠️ ([ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/ascension-pico-espiguete-por-la-cara-sur)): 12,2 km ida y vuelta, 5 h 45 min, +1.050 m, dificultad alta. **Error de orientación habitual:** el valle de un arroyuelo que baja de la montaña *no* es el camino; hay que seguir la pista principal hasta la pedrera. Bajar la pedrera con mucho cuidado.
- **Montaña Pegaso (club), salida invernal de marzo de 2026** ⚠️ ([info](https://www.montanapegaso.es/carteles/2026/Espiguete2026_info.pdf) · [memoria](https://montanapegaso.es/carteles/2026/Espiguete2026_memo.pdf)): vía normal S por un corredor ancho, ~12 km ida y vuelta, ~5 h. Subieron dos grupos, uno por cada cara. **Huella aceptable en la cara N; la Pala Sur hubo que abrirla, y en la bajada estaba "bastante penosa"** (nieve de primavera).
- **Diario de Valderrueda (jun-2025)** ⚠️ ([artículo](https://www.diariodevalderrueda.es/texto-diario/mostrar/5259975/grandes-cumbres-descubrir-montana-palentina)): ~6 km (ida) y casi 1.000 m de desnivel por la vertiente palentina.

### mp-espiguete-norte · Espigüete por la arista E y la cara N, desde Pino Llano / Mazobre
- **escapadarural** ✅ ([blog](https://www.escapadarural.com/blog/rutas-por-la-montana-palentina)): dificultad muy alta y +1.050 m, solo con buena forma física. Sale de un aparcamiento de la carretera Cardaño de Abajo–Cardaño de Arriba (Pino Llano) y sigue la pista del valle del arroyo Mazobres.
- **komoot** ⚠️: las rutas de la arista E son técnicas y peligrosas y requieren experiencia. Hay una circular de 10,1 km desde el aparcamiento de Pino Llano ([fragmento](https://blog.komoot.nl/smarttour/e1068198404/espigueete-by-the-east-ridge-circular-in-the-parque-natural-montana-palentina)).
- **SummitPost** ⚠️: más de 20 vías descritas; la arista E cae ~1.100 m al valle; ruta clásica Pino Llano–cara N–arista E ([ruta](https://www.summitpost.org/route/474243/north-face-classic-eastern-ridge.html)). **Pino Llano tiene aparcamiento con fuente** ⚠️ (según el fragmento; confirmar que funciona).
- **Pyrenaica 286** ✅: la arista E de noche es "agradable"; la caliza tiene muy buena adherencia; hay un resalte con trepada sencilla antes de la cima E y un destrepe corto en un corte de la arista.
- **Rescates sin fecha verificable** ⚠️: dos montañeros accidentados en la cara N, uno de 58 años con una pierna fracturada, evacuado en helicóptero a Riaño ([El Mirón de Soria](https://elmirondesoria.es/soria/sucesos/dos-montaneros-heridos-rescatados-por-proteccion-civil/amp)); dos montañeros enriscados ([El Mirón](https://elmirondesoria.es/soria/sucesos/rescatados-dos-montaneros-enriscados-en-pico-espigueete/amp)); una montañera herida por una roca ([El Congresista](https://elcongresista.mx/rescate-montanera-herida-espiguete)). Se suman a los del informe (mayo de 2024 y 16-05-2025).

### mp-of-mazobre / mp-mazobre-circular · Cascada y Refugio de Mazobre
- **komoot** ✅ ([guía de cascadas](https://www.komoot.com/guide/3519921)): es el **mayor salto de agua del parque y de Palencia**; sendero fácil y cómodo; **mejor después de lluvias** (04-04-2023). Desde el mirador sale una senda corta hasta la **base de la cascada** (02-10-2023). Pino Llano–cascada: **3 km de buena pista**, también ciclable (05-10-2022). Agua fresca para refrescarse (02-08-2024). Highlight de la cascada: 42.95929, −4.79297 (1.613 m) ([3487275](https://www.komoot.com/highlight/3487275)).
- **Ficha Junta / Terranostrum** ⚠️: inicio en Pino Llano, **km 2,5** de la carretera Cardaño de Abajo–Cardaño de Arriba. **Aparcamiento pequeño: madrugar.** 6,6 km ida y vuelta, +320 m, dificultad baja. Mejor época, la primavera (deshielo). Desvío a la izquierda hacia el refugio a mitad de camino (~30 min).
- Refugio: ver §1.1 y §1.3 (10 plazas, en uso).

### mp-pena-prieta-cardano / mp-cordal-lomas-murcia / mp-of-lomas · Peña Prieta y Pozo de las Lomas desde Cardaño de Arriba
- **escapadarural** ✅: Pozo de las Lomas, dificultad media-alta, **12 km ida y vuelta, +640 m**. Sale de la **iglesia** de Cardaño de Arriba; praderas junto al río, varios arroyos que cruzar, Alto de La Lomba con vista al circo; Celestino, Agujas de Cardaño y Alto de las Lomas alrededor.
- **komoot** ✅ (Pozo de las Lomas, highlight 43.01029, −4.74284, 2.115 m, [1651543](https://www.komoot.com/highlight/1651543)): "precioso lago glaciar bajo las Agujas de Cardaño" (26-06-2026). "**Espectacular verlo helado y poder caminar sobre él**" (14-02-2025): ⚠️ **hay que avisar en la app de que no se camine sobre el hielo del lago**. En invierno y a principios de primavera la nieve complica la subida (15-05-2023).
- **komoot** ⚠️: circular Peña Prieta–Infierno–Tres Provincias, ~16,5–17 km y más de 7 h ([fragmento](https://blog.komoot.de/smarttour/e1068265978/pena-prieta-pena-del-infierno-y-mojon-de-tres-provincias-circular-por-el-parque-natural-montana-palentina)).
- **SummitPost** ⚠️ (Cardaño de Arriba): remontar el río de las Lomas, cruzar un puente, subir a las praderas de la Campiza, dejar la laguna a la izquierda y llegar al collado bajo la cara S ([página](https://summitpost.org/carda-o-de-arriba/188808)).
- **Turismo CyL** ⚠️: se sale del aparcamiento de Cardaño de Arriba; laguna a ~2.080 m ([P3](https://www.turismocastillayleon.com/es/naturaleza/p3-senda-lagunas-lomas)). Los vehículos de visitantes solo pueden ir por tramos asfaltados (Terranostrum ⚠️).
- **Blogs** ⚠️: viajaporlibre, ~18 km, +1.600 m y 8 h ida y vuelta por la cara S ([fragmento](https://www.viajaporlibre.com/senderismo/rutas-montana-palentina)); Península Blog (31-07-2020), senda ancha y bien marcada ([entrada](https://peninsulablog.com/2020/07/31/pena-prieta-2-539-m-montana-palentina/)).
- **Aviso histórico de zona:** el refugio del club Espigüete, al N del pueblo junto al arroyo del Pozo de las Lomas, lo destruyó un alud en 2015 (§1.3).

### mp-murcia-valcabe · Pico Murcia
- Wikipedia ✅: dificultad media-baja, pero con accidentes en invierno. Pyrenaica ✅: desde el collado de Valcabe, ~200 m de desnivel en 350 m de distancia hasta una cima rocosa.

### mp-valdecebollas-golobar / mp-valdecebollas-branosera · Valdecebollas
- **komoot** ⚠️: desde el Golobar son ~5,25 km y +380 m, unas 2 h; es la ruta más popular de Brañosera (actualizada 26-02-2026 y mayo de 2026). Variante larga de ~20 km y +980 m, difícil ([fragmento](https://blog.komoot.nl/smarttour/e1093102700/pico-valdecebollas-from-golobar-trail)). komoot ✅: la cima tiene el Torreón con vértice y cruz; vistas espectaculares (25-04-2023).
- **Terranostrum** ⚠️: circular de 12–13 km y ~4 h 30 min. Desde el Golobar se suben 300 m hasta la cima y desde la cima se bajan 940 m hasta Brañosera. El Golobar está donde muere la carretera ([ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/branosera/valdecebollas-y-el-cueto)). Variante Golobar–Valdecebollas–Sel de la Fuente: 11,3 km, 5 h ([ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/branosera/ruta-golobar-valdecebollas-sel-de-la-fuente)).
- **Wikipedia** ✅: carretera sin mantenimiento y con desprendimientos; nieve abundante y cascadas de hielo en invierno; misa en la cima el primer domingo de agosto.

### mp-penalabra-tresmares · Peña Labra y Tres Mares
- komoot ✅: el mirador de Piedrasluengas (>1.300 m) ofrece vistas de los Picos, Peña Labra, Tres Mares, Cuchillón y Liébana (2023; "espectacular mirador, gran recompensa tras una larga subida", 13-09-2026). Desde la cima de Tres Mares se ve el arranque del camino a Peña Labra (28-09-2026). La cumbre de Tres Mares está muy cerca de la estación de Alto Campoo (2022).

### mp-pena-redonda · Peña Redonda
- Wikipedia ✅: niebla matinal frecuente; acceso por la cantera de Traspeña y hitos; romería el primer domingo de agosto (ver §2).
- komoot ⚠️: ascenso de ~13,8 km y +820 m, difícil ([fragmento](https://blog.komoot.nl/smarttour/e1068363176/pena-redonda-ascent-trail)).
- No se encontró ninguna crónica de 2024–2026.

### mp-of-tosande · Tejeda de Tosande
- **escapadarural** ✅: dificultad media, +400 m, ~10 km en buena parte de ida y vuelta, ~3 h 30 min; tejos de hasta 1,5 m de diámetro.
- **Cierres por caza** ✅/⚠️: el PDF de cierres de senderos de la Fundación (actualizado el 13-11-2025) incluía **cierres de la Senda de Tosande por cacería el 13-12-2025 y el 22-02-2026** ([PDF](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural_2025_11_14-20251113-155300.pdf), fragmento del buscador). Esto respalda que el corte de agosto de 2025 del informe pudo tener otra causa, porque la caza se concentra entre octubre y febrero ❓.
- Wikipedia ✅: prohibido salirse del sendero; aparcamiento en la C-626.

### mp-of-roblon · Roblón de Estalaya
- escapadarural ✅: circular, ~100 m de desnivel, ≤1 h 30 min. Árbol "El Abuelo": **17 m de altura, 10,6 m de perímetro, más de 500 años**. Hayedo y robledal, muy bonito en otoño.
- komoot ✅: "impresionante roble de más de 600 años, paseo fácil y bien señalizado" (03-04-2026). **La edad no coincide (500 frente a 600 años)** ❓.

### mp-of-fuente-cobre · Senda de Fuente Cobre (PR-P 8)
- Turismo CyL ⚠️: circular de 11 km, ~4 h, dificultad media. Terranostrum ⚠️: 11,6 km, 4 h 30 min, +400 m, dificultad "baja"; **en invierno y principios de primavera, la nieve y el agua pueden dificultar el acceso**. komoot ⚠️: 11,7 km, +410 m. Aparcamiento a ~800 m de Santa María de Redondo ([Turismo CyL](https://www.turismocastillayleon.com/en/countryside-nature/nature-routes/pathway-fuente-cobre-birth-pisuerga-river-672e) · [Terranostrum](https://www.terranostrum.es/senderismo/palencia/montana-palentina/santa-maria-de-redondo/la-fuente-del-cobre)).
- No se encontraron avisos de oso recientes (el del informe sigue siendo un testimonio único).

### mp-covalagua-corta / mp-covalagua-integral
- komoot ⚠️: desde Revilla de Pomar son 5,8 km, ~2 h, moderada. Terranostrum ⚠️: 5,2 km, 2 h, dificultad baja, todo el año; la balsa y la cascada están a ~2 km del inicio ([ficha](https://www.terranostrum.es/senderismo/palencia/montana-palentina/revilla-de-pomar/sendero-cascada-de-covalagua)).
- **El caudal depende del deshielo y de las lluvias** (Turismo CyL ⚠️). No hay informes de caudal de 2025–2026. El estiaje de 2017–2018 del informe sigue siendo el único dato concreto.
- Abrigo con merendero "Refugio de Covalagua" (§1.2).

### mp-tuerces-* · Las Tuerces
- Fragmentos de guías ⚠️ (Terranostrum, esdiario, Los Pueblos más Bonitos): laberinto de más de 50 ha; acceso por senda señalizada desde Villaescusa de las Torres. Ruta Roja desde Mave, ~5,6 km y ~2 h; Verde desde Aguilar por el Pisuerga, ~7,3 km; Amarilla por Olleros y Monte Cildá, ~8,3 km y ~3 h. **Llevar agua (cargar en Mave o Villaescusa)**; **cuidado con el borde del cañón, sobre todo con niños**.
- No se encontró ninguna crónica de 2024–2026.

### mp-bernorio · Monte Bernorio
- komoot ✅: cima plana con yacimiento prerromano (20-06-2023). Ver §2 para el texto descriptivo. Hay otro highlight ✅ con "restos de parapetos y trincheras de la Guerra Civil; se sube cómodamente desde el páramo sin camino establecido" (07-11-2021), pero corresponde a una cumbre con vistas a Valderredible y **no consta que sea el Bernorio** ❓.

### mp-of-gigante · Senda del Gigante del Valle Estrecho
- komoot ✅: 4,3 km (~1 h 16 min caminando), una de las favoritas de la zona de Triollo. Trasfondo: la leyenda del Gigante de San Martín de los Herreros (§2, Peña Redonda).

### mp-valle-pineda / mp-pozo-curavacas-pineda
- komoot ✅: hay un highlight en la ruta del Valle de Pineda junto al Carrión (02-10-2022). En la vega están los refugios de **Pescadores** (~1.357–1.490 m) y **Santa Marina** (~1.455 m), los dos con río a <100 m (§1.1).

### Otros (komoot ✅)
- Senda del Oso (Cervera–Arbejal): circular de ~11 km desde el puente de San Roque por la margen derecha del Pisuerga, hasta el embalse de Requejada (texto de 20-02-2025).
- Embalse de Ruesga: está permitido el baño; zona de arena y alquiler de patines (07-10-2022). Pista agradable por la orilla (20-06-2026).

---

## 4. Crónicas y comentarios recientes (2024–2026)

**No se encontraron crónicas de blog de 2024–2026 accesibles para Curavacas, Peña Prieta, Peña Redonda, Las Tuerces, Covalagua ni Fuente Cobre.** Los buscadores devuelven sobre todo fichas (Terranostrum, Turismo CyL, komoot). Lo que sí hay con fecha en ese periodo:

| Fecha | Ruta / slug | Comentario resumido | Fuente | Conf. |
|---|---|---|---|---|
| 13-09-2026 y 28-09-2026 | mp-penalabra-tresmares | Mirador de Piedrasluengas, "gran recompensa tras una larga subida". Desde Tres Mares se ve el camino a Peña Labra | [komoot guía cumbres PN](https://www.komoot.com/guide/415494) | ✅ |
| ~jul-2026 | 🟧 Cabaña de Naranco (Llánaves) | Estado aceptable, algo de polvo; la puerta se cierra con una piedra; cabe un grupo pequeño | [refugioslibres](https://www.refugioslibres.com/refugios/cabana-de-naranco) | ✅ |
| 26-06-2026 | mp-of-lomas | Lago glaciar bajo las Agujas de Cardaño, precioso | [komoot 1651543](https://www.komoot.com/highlight/1651543) | ✅ |
| 20-06-2026 | mp-of-ruesga / mp-ruesga-berrea | Camino bonito alrededor del embalse de Ruesga | [komoot lagos PN](https://www.komoot.com/guide/3798621) | ✅ |
| 03-04-2026 | mp-of-roblon | Roble "de más de 600 años"; paseo fácil y bien señalizado | [komoot Palencia](https://www.komoot.com/es-es/guide/50235/rutas-de-senderismo-en-palencia) | ✅ |
| mar-2026 | mp-espiguete-sur / norte | Invernal del club Montaña Pegaso: huella aceptable en la N; la Pala Sur hubo que abrirla y la bajada fue penosa | [memoria](https://montanapegaso.es/carteles/2026/Espiguete2026_memo.pdf) | ⚠️ |
| 13-12-2025 / 22-02-2026 | mp-of-tosande | Cierres por cacería programados | [PDF cierres](https://patrimonionatural.org/ficheros/Cierres%20de%20Senderos%20Parque%20Natural_2025_11_14-20251113-155300.pdf) | ⚠️ |
| 08-11-2025 | mp-valdecebollas-golobar | Track de Wikiloc Peña Rubia–Sestil–Cueva del Cobre–Valdecebollas desde La Collada (Golobar) (solo fragmento; Wikiloc sin abrir) | buscador | ⚠️ |
| jun-2025 | general | Artículo de prensa: el Pico del Infierno (2.537 m) es de facto el techo de la Montaña Palentina; Espigüete ~6 km y ~1.000 m | [Diario de Valderrueda](https://www.diariodevalderrueda.es/texto-diario/mostrar/5259975/grandes-cumbres-descubrir-montana-palentina) | ⚠️ |
| 14-02-2025 | mp-of-lomas | Lago helado, "se puede caminar sobre él" → **aviso de seguridad: no pisar el hielo** | [komoot 1651543](https://www.komoot.com/highlight/1651543) | ✅ |
| 02-08-2024 | mp-of-mazobre | Cascada tras una caminata corta y bastante fácil; agua fresca | [komoot 3487275](https://www.komoot.com/highlight/3487275) | ✅ |
| 2024 (aprox.) | mp-espiguete-sur | Guía Repsol con perro: agua solo en Cardaño; ir por el lado derecho de la pedrera; perro atado | [Guía Repsol](https://www.guiarepsol.com/es/viajar/con-mi-mascota/ruta-con-perro-espiguete-palencia/) | ⚠️ |
| 26-05-2024 | mp-covalagua-* | Refugio con mesas, sitio tranquilo para comer | [komoot 6659058](https://www.komoot.com/highlight/6659058) | ✅ |

Blogs con contenido de la zona que se podrían revisar a mano (solo vistos en el buscador, sin fecha confirmada) ⚠️: [atrochando.com](https://atrochando.com/rutas-de-senderismo-en-montana/montana-palentina/) · [rutinasvarias.com](https://www.rutinasvarias.com/category/montana-palentina/) · [elcorrelimos.com](https://elcorrelimos.com/montana-palentina/) · [sendasycumbres.com](https://sendasycumbres.com/montana-palentina/) · [mountainguidespain.com (trilogía)](https://www.mountainguidespain.com/trilogia-de-la-montana-palentina/) · [viajaporlibre.com](https://www.viajaporlibre.com/senderismo/ruta-curavacas-vidrieros) · [peninsulablog.com (2020)](https://peninsulablog.com/2020/07/31/pena-prieta-2-539-m-montana-palentina/).

---

## 5. Puntos de agua mencionados explícitamente

Ninguno tiene control sanitario. **Tratar o filtrar siempre** (informe §5). La fiabilidad es la que cuenta la fuente.

| Punto | Ruta / slug | Ubicación | Fiabilidad según la fuente | Fuente | Conf. |
|---|---|---|---|---|---|
| **Gran fuente de Cardaño de Abajo** | mp-espiguete-sur | Plaza o entrada del pueblo | Recomendada para llenar; **no hay más agua en la ruta** | Guía Repsol (fragmento) | ⚠️ |
| Fuente del aparcamiento de **Pino Llano** | mp-espiguete-norte, mp-of-mazobre, mp-integral | Aparcamiento, km 2,5 de la carretera de los Cardaños | Citada por SummitPost; funcionamiento actual sin confirmar | SummitPost (fragmento) | ⚠️ |
| **Pozo de las Lomas** (y el arroyuelo del lago) | mp-integral, mp-of-lomas, mp-cordal-lomas-murcia | ~2.080–2.115 m (43.01029, −4.74284) | **Único punto de agua de la Integral**; agua de lago, la tomaron con pastillas | Pyrenaica 286 | ✅ |
| Manantial bajo las Agujas de Cardaño | mp-integral | Encima del Pozo de las Lomas | **No lo encontraron** (verano) | Pyrenaica 286 | ✅ (negativo) |
| "Manantial Las Lomas" | mp-of-lomas | Waypoint de Wikiloc (sin abrir) | ❓ | [Wikiloc (solo buscador)](https://es.wikiloc.com/waypoints/fAgab3/manantial-las-lomas) | ⚠️ |
| Fuente junto al **arroyo de Cabriles** | mp-curavacas-vidrieros, mp-integral | Al bajar del Callejo Grande, cerca de Vidrieros | Existía cuando pasó el autor | Pyrenaica 286 | ✅ |
| Arroyo de Cabriles (vados) | mp-curavacas-vidrieros | Subida desde Vidrieros | Arroyo, se cruza varias veces | HikingIberia (fragmento) | ⚠️ |
| Fuente a <100 m de la **Cabaña de Mollorente** | — (Pico Pando, desde Vidrieros) | ~1.829 m | Según la ficha, sin fecha | refugioslibres | ✅/❓ |
| Río a <100 m de los refugios de **Pescadores** y **Santa Marina** | mp-valle-pineda, mp-pozo-curavacas-pineda | Río Carrión / Arauz | Río permanente (no potable sin tratar) | refugioslibres | ✅ |
| Fuente a <1 km del **refugio de Cristo Sierra** | mp-fraile (variante Cristo Sierra) | Entre Valcobero y Valsurbio | Según la ficha | refugioslibres | ✅/❓ |
| Cascada de Mazobre | mp-of-mazobre | 42.95929, −4.79297 | Corriente superficial, más caudal tras lluvias y en deshielo. **En el valle del Mazobre hay tramos de arroyo secos** porque la caliza filtra el agua | komoot · fragmento | ✅/⚠️ |
| Fuentes de Las Tuerces | mp-tuerces-* | — | **No hay agua en la ruta**: cargar en Mave o Villaescusa | guías (fragmento) | ⚠️ |
| Fuente de la Flor y manantiales | mp-of-pedrosa (Senda de La Pedrosa, Barruelo–Brañosera) | — | "Famosa por la calidad de su agua" | Terranostrum (fragmento) | ⚠️ |
| Fuente de la Sondonada | mp-pena-redonda / mp-of-gigante | Bajo la sierra de la Peña | Solo aparece en la leyenda; sin dato de caudal | Wikipedia | ❓ |

Lo que cambia respecto al informe: se confirma la **escasez de agua en las crestas** (Pyrenaica, de primera mano). Se añaden puntos concretos en Cardaño de Abajo, Pino Llano, Cabriles y Mollorente. Covalagua y Mazobre dependen de las lluvias.

---

## 6. Huecos que siguen abiertos

1. **Coordenadas exactas de los refugios.** Refugioslibres solo las enseña con cuenta (no se creó). Hay que cruzar con OSM (la consulta Overpass ya preparada) la ubicación de Pescadores (¿42.9384, −4.6427 o ~42.9605, −4.6058?), Mazobre, Santa Marina, Mollorente, Cristo Sierra y el candidato a Tenadas de Lores (43.0238, −4.5532).
2. **Postil de Soña:** no hay ningún dato posterior a 2018. Llamar a la Casa del Parque (979 13 94 01).
3. **SummitPost y Guía Repsol** solo se conocen por el buscador (Cloudflare 403 y Akamai 418). Para leerlos haría falta revisarlos a mano en un navegador.
4. **Crónicas 2024–2026:** apenas hay en abierto. Las que existen estarán en Wikiloc (bloqueado) o en redes sociales. Faltan sobre todo Peña Redonda, Las Tuerces, Covalagua y Fuente Cobre.
5. Fechas exactas de los rescates del Curavacas y del Espigüete citados por El Mirón de Soria y Vozpópuli.
6. Figura de protección vigente de Las Tuerces y de Covalagua (¿Monumento Natural / Paisaje Protegido?).
7. Fecha del número 286 de Pyrenaica.
