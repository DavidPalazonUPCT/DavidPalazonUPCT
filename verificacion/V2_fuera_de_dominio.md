# V2 — Caza de literatura fuera de dominio (informe de verificación)

> Subagente V2. Tarea READ-ONLY. No se edita el plan; este documento es solo un informe.
> Fuente de verdad: `insumos/Acta_Decisiones_v2_Reestructuracion_Plan.md` (§6 puntos 10/11/12/13; §7).
> Plan auditado: `trabajo/plan_actual.md` (párrafos `[PNNN]`).
> Dominio estricto exigido: ICS de **agua**, **telemetría y series temporales multivariantes de la capa OT (proceso físico)**, **Purdue niveles 0-2**. NO "ICS" amplio (IT+OT, redes, protocolos, tráfico).

---

## Resumen ejecutivo

Recuento por categoría de acción:

| Categoría de acción | Nº apariciones | Pxxx implicados |
|---|---:|---|
| **ELIMINAR** (fuera de dominio, sin función) | 2 | P043 (IIoT como encuadre); P043 framing "Multimedia/IIoT" |
| **RECONVERTIR a contraste / acotar** | 6 | P060, P071, P072, P088, P093, P095 |
| **DUDOSA (preguntar)** | 4 | P040, P050, P096, P119/P126 (TinyML/borde) + P043 (línea Multimedia, ya en Q5) |

Recuento por **fuente del problema** (qué dominio ajeno se cuela):

- **IIoT genérico:** 3 apariciones (P043 encuadre central; P093 "ShaTS … en el IIoT"; P165 ref ShaTS — IIoT por título). Acta manda purgar (§6 p.10/12, §7).
- **IT + OT / redes / protocolos / tráfico / NIDS / perímetro:** 4 apariciones (P060, P071, P072, P088 "anomalía adversarial"; P188 Lamberts = *intrusion detection*). El acta exige acotar a **solo OT, series del proceso** (§6 p.13).
- **IA general / NLP / LLM como objeto:** 1 aparición (P093, LLM como capa de explicación — ya marcada "fuera del alcance central" por el autor).
- **Manufactura discreta / visión por computador:** **0 apariciones de contenido** (no hay imagen, píxel, visión, línea de montaje, robótica). Solo persiste el rótulo "Tecnologías **Multimedia**" en P043 (encuadre administrativo del programa, no contenido técnico). Nada que purgar por contenido aquí.
- **Detección por condition monitoring / activos / dominio ajeno (química, energía):** refs P177 (Hendriks, condition monitoring), P199 (OntoCape, química), SAREF (energía) y DEXPI/BFO dentro de P095; y P163 (Dong, *hydraulic condition monitoring*).

**Dos hallazgos estructurales de alcance (críticos):**
1. **Purdue NO aparece en NINGÚN punto del plan** (búsqueda exhaustiva: 0 coincidencias de "Purdue"/"niveles 0-2"/"capa OT"). El acta §6 p.11 lo exige explícito (niveles 0-2). Hay que **insertarlo** (ancla natural: 3.2 / P071, y marco WP0).
2. El plan **difumina el alcance hacia "ICS amplio / IT+OT"** justo donde debería acotarlo: P071 (lista PLC+SCADA+RTU+HMI+protocolos) y P072/P060 (convergencia IT-OT). Hay que **declarar explícitamente** que se trabaja con **las series temporales del proceso físico (OT), no con la capa IT ni con tráfico de red** (acta §6 p.13).

---

## Apariciones a depurar

| Pxxx | Cita textual (fragmento) | Categoría | Acción | Nota |
|---|---|---|---|---|
| **P043** | "La investigación se encuadra en la línea de Tecnologías Multimedia … **en el ámbito del Internet Industrial de las Cosas (IIoT, del inglés Industrial Internet of Things)**, la Inteligencia Artificial y la protección de infraestructuras críticas." | IIoT genérico | **ELIMINAR** el sintagma IIoT | El acta (§6 p.10/12, §7) ordena purgar IIoT como encuadre. Sustituir por encuadre en **ICS de agua / series OT del proceso físico, Purdue 0-2**. La "línea de Tecnologías Multimedia" es decisión administrativa → ver Q5 (DUDOSA, conservar salvo indicación). |
| **P060** | "La proliferación de sensores del Internet de las Cosas (IoT…), la adopción de sistemas … SCADA … y **la convergencia de las redes de tecnología de operación (OT…) con las de tecnología de la información (IT…)** han mejorado la eficiencia, pero también han ampliado la superficie de ataque…" | IT+OT / IoT genérico | **RECONVERTIR / acotar** | Vale como motivación (por qué hay amenaza), pero debe cerrarse con la acotación: "esta tesis se ocupa **solo de la capa OT — las series del proceso físico —, no del tráfico IT ni del perímetro de red**". Mantener IoT/IT como contexto, no como objeto. |
| **P071** | "Dependen de sistemas de control industrial compuestos por los PLC, sistemas SCADA, unidades terminales remotas (RTU…), interfaces hombre-máquina (HMI…), redes de sensores y actuadores, y **protocolos industriales como OPC-UA, Modbus o Profinet**, que supervisan y controlan el proceso físico en tiempo real." | ICS amplio / protocolos / redes | **RECONVERTIR / acotar** | Es la frase que más difumina el alcance hacia "ICS = IT+OT + redes + protocolos". Acotar: el listado sirve para **situar la pila**, pero el objeto de estudio son **las series temporales del proceso físico (niveles 0-1) y su supervisión (nivel 2)**, NO los protocolos ni el tráfico. Punto natural para **insertar Purdue 0-2** (ver sección 4). |
| **P072** | "La **convergencia de las redes OT con las de IT** ha ampliado la superficie de ataque de unos sistemas concebidos para operar aislados (Giraldo et al., 2018)." | IT+OT | **RECONVERTIR / acotar** | Igual que P060: aceptable como contexto de amenaza, pero añadir la frase de alcance OT-series. No eliminar (justifica la criticidad), sí delimitar. |
| **P088** | "…los ciberataques introducen una **anomalía adversarial**, provocada por una inteligencia que elige qué sensores o actuadores manipular… SSSP, SSMP, MSSP y MSMP…" | Adversarial / vectores | **RECONVERTIR (mantener)** | DENTRO de dominio: los vectores SWaT son sobre sensores/actuadores del proceso (OT), no sobre tráfico de red. **No purgar.** Solo verificar que no derive hacia "detección por tráfico/NIDS". Anotada por completitud. |
| **P093** | "…como ShaTS (Franco de la Peña et al., 2025), lleva esta idea a la detección de anomalías **en el IIoT**. … se abre además el uso de **modelos de lenguaje (LLM…) como capa de explicación en lenguaje natural, una extensión que queda fuera del alcance central de la tesis**." | IIoT + LLM/NLP | **RECONVERTIR a contraste** | (a) ShaTS: reconvertir el "en el IIoT" → presentarlo como método de atribución Shapley en series temporales **a contraste** ("a diferencia de su aplicación en IIoT genérico, aquí sobre series OT de proceso de agua"). (b) LLM: el autor YA lo acota como fuera de alcance; mantener como una sola frase de cierre o demotarlo a trabajo futuro. No expandir. |
| **P095** | "Sobre esta base existen familias especializadas (**SAREF para eficiencia energética**, **OntoCape para procesos químicos (Marquardt et al., 2010)**, **DEXPI** para el intercambio de instrumentación, o la **ontología de fundamento BFO**)… **Hendriks et al. (2024)** aportan uno de los pocos casos aplicados." | Ontologías de dominio ajeno (energía/química) + condition monitoring | **RECONVERTIR / RETIRAR** (ver sección 3) | El acta §7 marca OntoCape (química) y Hendriks (condition monitoring de activos) **fuera por dominio ajeno**. SAREF (energía), DEXPI y BFO son ejemplos de "fragmentación" ajenos al agua/OT-series. Reducir el inventario a SSN/SOSA + revisiones (Karabulut, Jarwar) **como soporte del hilo de transferibilidad**, no del detector. |
| **P040** | "Palabras clave: … explicabilidad; **despliegue en hardware de borde**." | TinyML / borde | **DUDOSA** | El acta no incluye el borde en su estructura WP. Si se demota (ver Q1), esta palabra clave debe caer o suavizarse. |
| **P050** | "5. **Caracterizar la viabilidad de despliegue en hardware de borde** de las configuraciones resultantes, como consecuencia operativa del trabajo." | TinyML / borde (objetivo 5) | **DUDOSA** | El objetivo específico 5 NO tiene correspondencia en la estructura WP0-WP3 del acta. Candidato a demotar a "consecuencia operativa / trabajo futuro" o retirar (Q1). No decidir aquí. |
| **P096** | "…las técnicas de compresión (cuantización y poda) y los motores de inferencia (ONNX Runtime, TensorRT)… (**Zhou et al., 2024**; …). … (TinyML) … incluido el monitorizado … de equipos como bombas (**Antonini et al., 2023**)…" | TinyML / NAS hardware | **DUDOSA** | Refs Antonini 2023 (TinyML) y Zhou 2024 (HGNAS) sostienen una sección (3.7) que el acta no estructura. Si se demota el borde, retirar/reducir estas refs. Anotar, no decidir (Q1). |
| **P119 / P126** | P126: "La **viabilidad de despliegue en hardware de planta** acompaña a estas líneas como comprobación operativa…, no como objeto central." (+ barra de cronograma P129/P174) | TinyML / borde | **DUDOSA** | Coherente con "consecuencia operativa", pero sigue ocupando objetivo + sección + barra de cronograma. Decisión de demotar/retirar pendiente de David (Q1). |

---

## Referencias fuera de dominio a retirar/reconvertir

Comprobación directa contra acta §7 (las que marca fuera por dominio ajeno) + barrido propio.

| Ref (Pxxx bibliografía) | Cita | Dónde se usa | Veredicto acta | Recomendación |
|---|---|---|---|---|
| **P199 — Marquardt et al. 2010 (OntoCape)** | "OntoCape: A re-usable ontology for chemical process engineering." | P095 ("OntoCape para procesos químicos") | **FUERA — proceso químico** (§7) | **RETIRAR** del corpus, o dejar una sola mención **a contraste** ("ontologías de proceso químico como OntoCape, ajenas al dominio hídrico"). No usar como soporte. |
| **P177 — Hendriks et al. 2024** | "Structured data ontology for AI in industrial **asset condition monitoring**." | P095 ("uno de los pocos casos aplicados") | **FUERA — condition monitoring de activos** (§7) | **RETIRAR**. El cierre ontología→IA debe apoyarse, si acaso, en revisiones del hilo de transferibilidad, no en un caso de monitorizado de activos. |
| **SAREF** (en texto P095, sin entrada propia) | "SAREF para **eficiencia energética**" | P095 | Fuera por dominio ajeno (energía) | **RETIRAR** la mención o dejarla solo como ejemplo de fragmentación a contraste. |
| **DEXPI** (en texto P095, sin entrada propia) | "DEXPI para el intercambio de instrumentación" | P095 | Periférico (intercambio de datos de instrumentación, no detección OT-series) | Reducir a contraste o retirar; no es soporte del detector ni del hilo. |
| **BFO** (en texto P095, sin entrada propia) | "la ontología de fundamento BFO" | P095 | IA/ontología general, fuera de dominio | **RETIRAR** o dejar como mero ejemplo de fragmentación. |
| **P185 — Karabulut et al. 2023** | "Ontologies in **digital twins**: A systematic literature review." | P095 (fragmentación) | **SE QUEDA** (revisión de ontologías) | **MANTENER**, pero **solo como soporte del hilo de transferibilidad/interoperabilidad**, no del detector. Acotar el "gemelos digitales" para que no abra un frente de digital twins. |
| **P183 — Jarwar et al. 2025** | "Modeling **industrial IoT security** using ontologies: A systematic review." | P095 (ontologías de seguridad industrial; señala escasa cobertura hídrica) | **SE QUEDA** (revisión de ontologías) | **MANTENER** como soporte del hilo de transferibilidad. El "industrial IoT" del título es admisible aquí porque se usa para señalar el **hueco** (escasa cobertura del agua), no como encuadre del detector. |
| **P175 — Haller et al. 2019 (SSN/SOSA)** | "The modular SSN ontology… sensors, observations, sampling, and actuation." | P095 (vocabulario común) | **SE QUEDA** (§7: ref 69 SSN/SOSA) | **MANTENER**, solo como soporte del **hilo de transferibilidad** (mapear semántica SWaT↔planta), NO como componente del detector. |
| **P165 — Franco de la Peña et al. 2025 (ShaTS)** | "…anomaly detection in **Industrial Internet of Things**." | P093 | IIoT por título | **RECONVERTIR a contraste**: usar el método (atribución Shapley en series) reconociendo que su banco es IIoT genérico, a diferencia de las series OT de agua de la tesis. No es soporte de dominio. |
| **P188 — Lamberts et al. 2023 (SoK)** | "SoK: Evaluations in **industrial intrusion detection** research." | P137 (FEDS, "más de un dataset/métrica") | El acta lo INCORPORA al corpus (§7) por la evidencia de evaluación (~1,3 datasets/paper) | **MANTENER** pero **acotar el uso**: citarlo por su lección metodológica de evaluación, NO por "intrusion detection" (que es IT/NIDS). Asegurar que no arrastre el marco de detección por tráfico. |
| **P163 — Dong et al. 2023** | "…anomaly detection in **hydraulic condition monitoring** system." | P112, P133 (escasez de etiquetas / generalización entre plantas) | Limítrofe (condition monitoring hidráulico) | **DUDOSA-leve**: se usa por la lección de "falta de etiquetas / generalización entre plantas", que sí aplica. Mantener solo por esa función; vigilar que no se lea como traslado de "condition monitoring de activos". |
| **P149 — Antonini et al. 2023 (TinyML)** | "An adaptable and unsupervised **TinyML** anomaly detection system…" | P096 | Vinculada a borde (no estructurado por el acta) | **DUDOSA** → retirar si se demota el borde (Q1). |
| **P228 — Zhou et al. 2024 (HGNAS)** | "**HGNAS**: Hardware-aware graph neural architecture search for **edge devices**." | P080, P096 | Vinculada a borde + NAS hardware | **DUDOSA** → retirar/reducir si se demota el borde (Q1). En P080 se usa solo para "mayor coste de inferencia en hardware embebido": esa mención puede sobrevivir como nota, pero la ref es prescindible fuera del hilo de borde. |

**Refs que el acta confirma DENTRO y que NO deben tocarse por dominio** (verificadas presentes y bien usadas): Kim et al. (P186), Wu & Keogh (P223), Heydari & Nyarko (P180), Han et al. OWAD (P176), Cai et al. SA² (P154), Fung et al. 2024 (P166), Raman & Mathur/AICrit (P207), Garg (P169), Paparrizos (P204), Huet (P181), Gama (P167), Lu (P193), Bayram (P152), Ghaeini (P170), Feng (P164), Deng & Hooi (P161), Umer (P218), Li robust state space (P191). Todas sobre series OT / evaluación / deriva / invariantes en agua. Sin acción.

---

## Dónde explicitar el alcance (OT-series + Purdue 0-2)

El plan **no menciona Purdue en ningún punto** (0 coincidencias) y deja varias frases que difuminan hacia "ICS amplio". Inserciones recomendadas con Pxxx ancla:

1. **P071 (3.2) — ANCLA PRINCIPAL DE PURDUE.** Tras enumerar PLC/SCADA/RTU/HMI/protocolos, insertar una frase que sitúe el trabajo en **Purdue niveles 0-2** (proceso, control, supervisión) y declare que el objeto son **las series temporales del proceso físico (OT)**, no la capa IT, las redes ni el tráfico/protocolos. Es la frase que el acta §6 p.11 y p.13 exige y hoy falta por completo. (Sugerencia: añadir incluso una mención visual del modelo de Purdue.)

2. **P060 (3.1).** Cerrar la frase de convergencia IT-OT con la acotación de alcance: "esta tesis se ocupa de la **capa OT — las series del proceso físico — en los niveles 0-2 de la pila de Purdue**, no del tráfico de red ni de la seguridad perimetral".

3. **P072 (3.2).** Misma acotación que P060: reconvertir "convergencia OT-IT amplía la superficie de ataque" en motivación + delimitación ("…pero el detector que aquí se estudia observa el proceso físico, no la red").

4. **P057-P058 marco / WP0 (sustrato conceptual).** El acta (§4, fila WP0) pide que el marco fije explícitamente "alcance OT/series, Purdue". Hoy P067/P038 hablan de "sistema dinámico parcialmente observado" pero **sin nombrar OT-series ni Purdue**. Insertar en el sustrato conceptual (P067 o un párrafo nuevo en 3.1) la delimitación: telemetría = series temporales multivariantes de la capa OT; niveles 0-2.

5. **P036 / P040 (Resumen y palabras clave).** El resumen (P036) dice "ICS … o, más en general, … CPS". Acotar a **series OT del proceso de agua** y añadir a palabras clave algo como "series temporales OT" / "niveles 0-2 Purdue", en lugar de (o además de) reforzar "ICS" amplio. Coherente con acta §6 p.13.

6. **P043 (Objetivos).** Al eliminar el encuadre IIoT, sustituirlo por el encuadre correcto: detección sobre **series temporales OT del proceso físico de agua, niveles 0-2 de Purdue**.

7. **P075 (3.3).** Ya dice bien "series temporales multivariantes (MTSAD)" y "proceso físico"; **reforzar** aquí que esas series son la **telemetría OT del proceso** (nivel 0-1) — buen punto para anclar coherencia con la delimitación, sin cambiar el contenido técnico.

8. **P087 (3.5).** Ya trabaja con "contexto operativo" y "régimen"; conviene una nota de que todo ello vive en la **capa de proceso (OT)**, para que la noción de "anomalía contextual" no se confunda con anomalías de tráfico/red.

---

## Para PREGUNTAS_PENDIENTES

Los siguientes puntos son **dudosos** (el acta no los resuelve unívocamente) → no decidir aquí; elevar a David. Algunos **ya están registrados** en `PREGUNTAS_PENDIENTES.md`; se cruzan para evitar duplicado.

1. **[YA = Q1] Despliegue en hardware de borde / TinyML (objetivo 5; 3.7; P040, P050, P096, P119/P126; refs Antonini 2023, Zhou 2024 HGNAS).** El acta NO lo incluye en su estructura WP0-WP3 ni en el panel de contribuciones. **Recomendación V2:** demotar a "consecuencia operativa / trabajo futuro" (mantener a lo sumo P126 como comprobación menor) y retirar las refs Antonini/HGNAS del corpus central; o retirarlo del todo como objetivo. **Decisión de David.** (Confirma alineación con Q1.)

2. **[YA = Q5] Encuadre "línea de Tecnologías Multimedia" + IIoT (P043).** El IIoT debe **eliminarse** (acta §6/§7). La "línea de Tecnologías Multimedia" es administrativa del programa: V2 recomienda **conservarla** salvo indicación, pero señalar la tensión (un encuadre "Multimedia" no casa con series OT de proceso). **Decisión de David** sobre si se reformula el encuadre del programa.

3. **[NUEVO] LLM como capa de explicación (P093).** El autor ya lo marca "fuera del alcance central". ¿Se mantiene como **una frase** de cierre/trabajo futuro, o se **elimina** para no introducir NLP/LLM como objeto? V2 recomienda mantener una sola frase demotada o eliminar; evitar cualquier expansión. **Decisión de David.**

4. **[NUEVO] Mención a "gemelos digitales" vía Karabulut (P095).** La ref se queda (revisión de ontologías), pero el sintagma "gemelos digitales" puede abrir un frente ajeno. ¿Se acota a "revisiones de ontologías" sin invocar digital twins como línea? V2 recomienda acotar. **Decisión de David.**

5. **[NUEVO — leve] Refs limítrofes de condition monitoring que NO están en la lista de purga explícita del acta:** Dong et al. 2023 (P163, *hydraulic condition monitoring*) se usa por la lección de "falta de etiquetas / generalización entre plantas" (función válida). ¿Se conserva por esa función concreta o se sustituye por una fuente de agua/OT-series más alineada? V2 recomienda conservar acotando el uso. **Decisión de David.**

---

### Notas de método
- Búsquedas realizadas sobre `trabajo/plan_actual.md` (texto + bibliografía completos, P000-P228).
- "Purdue", "niveles 0-2", "capa OT": **0 coincidencias** → ausencia confirmada, no inferida.
- Contenido de **visión por computador / manufactura discreta / imágenes**: **0 coincidencias** → no hay nada que purgar por contenido; solo persiste el rótulo administrativo "Multimedia" (P043).
- "variables discretas" (P140, P075) NO es manufactura: es tratamiento del **tipo de señal** dentro del proceso OT (actuadores binarios/multinivel); **dentro de dominio**, sin acción.
- Toda cita es textual del plan; no se ha inventado contenido.
