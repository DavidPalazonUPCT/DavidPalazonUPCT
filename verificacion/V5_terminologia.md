# V5 — Verificación de Terminología

> Subagente de verificación V5. READ-ONLY. Fuente de verdad: `insumos/Acta_Decisiones_v2_Reestructuracion_Plan.md` (§0.1 terminología [v2]; §5 puntos 6/15/16/17). Texto auditado: `trabajo/plan_actual.md` (P000–P228).
> Objetivo: localizar CADA aparición de un término/uso que el acta corrige y dar el reemplazo exacto. El acta ordena "aplicar en TODO el plan".

---

## Resumen ejecutivo

Recuento de incidencias por categoría:

| Cat. | Tema | Nº incidencias | Párrafos afectados |
|------|------|----------------|--------------------|
| **1** | Selección de umbral con oráculo (best-F1 / oracle thresholding) | **9** | P065 (×4), P084 (×2), P113, P114, P117 |
| **2** | Endógeno/exógeno mal usados (actuador vs sensor; o difuminado) | **3** | P067 (crítico), P038, P075/P088 (uso colateral correcto, ver nota) |
| **3** | "Reproducible por diseño" / "casi determinista" → asociaciones estables | **3** | P038, P067 (×2: "reproducible por diseño" + "casi determinista") |
| **4** | Modelo de información vs ontología (roles distintos, punto 17) | **2** | P095 (3.7) — confusión/fusión; P066 y P095 falta diferenciación |
| **5** | Información vs decisión (punto 15) — colapso | **2** | P037, P047/P139 (operacionalización tratada como "información/contribución" sin marcar que es gobierno de la alarma) |

**Totales aproximados:** Cat. 1 = 9 · Cat. 2 = 3 · Cat. 3 = 3 · Cat. 4 = 2 · Cat. 5 = 2. **Total ≈ 19 reemplazos/ajustes.**

Las dos incidencias **más críticas** (rompen la doctrina del acta, no solo el léxico):
- **P067** — "las entradas de control (los actuadores, como bombas y válvulas) y las perturbaciones exógenas (no controladas…)": equipara *exógeno* con *no-actuador* y mete los actuadores como categoría contrapuesta a lo exógeno. El acta (punto 6) prohíbe explícitamente el eje actuador/sensor. Además contiene "evolucionan de forma reproducible por diseño" y "la respuesta es casi determinista" (punto 16, ambos a corregir).
- **P065** — concentra 4 variantes prohibidas del término de umbral ("filtración de datos de prueba", "umbral óptimo a posteriori", "sin la verdad de referencia", "fijar el umbral con las etiquetas del propio conjunto de prueba") en un solo párrafo.

---

## Tabla de reemplazos

### Categoría 1 — Selección de umbral con oráculo sobre el conjunto de prueba

Término canónico del acta (§0.1 punto 1): **"selección de umbral con oráculo sobre el conjunto de prueba"**, con *best-F1 / oracle thresholding* entre paréntesis la **primera vez** que aparezca en el documento. Respaldo: Kim et al. 2022; Lamberts et al. 2023. (El "ajuste por puntos / point adjustment" es un fenómeno hermano pero **distinto**; no se renombra, solo se mantiene junto al término de oráculo.)

| Pxxx | Cita actual (verbatim) | Uso incorrecto | Reemplazo exacto exigido por el acta | Cat. |
|------|------------------------|----------------|--------------------------------------|------|
| **P065** | "fijar el umbral de detección con las etiquetas del propio conjunto de prueba (una filtración de datos de prueba) y aplicar el ajuste por puntos eleva e iguala de forma artificial los resultados publicados" | "filtración de datos de prueba" como nombre del fenómeno | "…fijar el umbral de detección mediante **selección de umbral con oráculo sobre el conjunto de prueba** (*best-F1 / oracle thresholding*) y aplicar el ajuste por puntos (*point adjustment*)…" (introducir aquí el inglés si es la 1.ª aparición del documento) | 1 |
| **P065** | "este umbral óptimo a posteriori muestra el potencial del modelo, pero no es aplicable en producción" | "umbral óptimo a posteriori" | "esta **selección de umbral con oráculo sobre el conjunto de prueba** muestra el potencial del modelo, pero no es aplicable en producción" | 1 |
| **P065** | "falta un marco válido e iterativo para fijar el umbral sin la verdad de referencia" | "sin la verdad de referencia" (eco del término viejo "fuga de la verdad de referencia") | "…para fijar el umbral **sin recurrir al oráculo del conjunto de prueba** (sin etiquetas de prueba en calibración)" | 1 |
| **P065** | "no se dispone de las etiquetas para calibrarlo" | (correcto en contenido) | Mantener; alinear con el término canónico al describir el problema como ausencia del oráculo de etiquetas en producción | 1 |
| **P084** | "Fijar el umbral con las etiquetas del conjunto de prueba para maximizar la métrica (best-F1), una forma de filtración de datos de prueba (del inglés data leakage) no replicable en producción" | "best-F1" como término principal + "filtración de datos de prueba (data leakage)" como etiqueta del fenómeno | "**La selección de umbral con oráculo sobre el conjunto de prueba** (*best-F1 / oracle thresholding*), no replicable en producción, y el ajuste por puntos (*point adjustment*)…" — usar el canónico como sujeto; *best-F1* solo entre paréntesis | 1 |
| **P084** | "(dar por detectado un intervalo entero porque un único punto cae cerca de la anomalía)" | (definición de point adjustment, correcta) | Mantener; es el ajuste por puntos, NO el oráculo de umbral. No fusionar ambos conceptos | 1 |
| **P113** | "se neutralizan como variables de confusión la filtración del umbral y de la normalización, el ajuste por puntos y el solape de ventana" | "filtración del umbral" | "se neutralizan como variables de confusión la **selección de umbral con oráculo** (y la normalización ajustada sobre prueba), el ajuste por puntos y el solape de ventana" | 1 |
| **P114** | "Toda comparación fija el umbral sin información del conjunto de prueba, prescinde del ajuste por puntos" | Perífrasis correcta pero no usa el término canónico (debilita la trazabilidad) | "Toda comparación fija el umbral **sin recurrir al oráculo del conjunto de prueba** (evitando la selección de umbral con oráculo), prescinde del ajuste por puntos" | 1 |
| **P117** | "La validez interna se protege fijando el umbral y la normalización sin información del conjunto de prueba y prescindiendo del ajuste por puntos" | Perífrasis correcta sin término canónico | "…fijando el umbral y la normalización **sin oráculo del conjunto de prueba** (evitando best-F1 / oracle thresholding) y prescindiendo del ajuste por puntos" | 1 |

Nota de cobertura Cat. 1: el acta menciona explícitamente P065, P084, P114, P117. Esta auditoría añade **P113** ("filtración del umbral") como aparición no listada en el mandato pero que cae bajo la misma regla. La mención §4 del acta ("NUNCA usar best-F1 sobre test como métrica principal") refuerza que *best-F1* solo puede aparecer como sinónimo entre paréntesis, nunca como sujeto.

### Categoría 2 — Endógeno = interno a la dinámica del proceso / Exógeno = externo a la planta (NO actuador vs sensor)

Regla del acta (§5 punto 6): **Exógenas** = externas a la planta (demanda, ambiente, consignas externas). **Endógenas** = internas a la dinámica del proceso (el estado y sus relaciones). **NO** es actuador vs sensor.

| Pxxx | Cita actual (verbatim) | Uso incorrecto | Reemplazo exacto exigido por el acta | Cat. |
|------|------------------------|----------------|--------------------------------------|------|
| **P067** | "las entradas de control (los actuadores, como bombas y válvulas) y las perturbaciones exógenas (no controladas, como la demanda o la calidad del agua de entrada) gobiernan la evolución de un estado interno latente" | Construye el eje **actuador vs perturbación exógena**, contraponiendo "actuadores" a "exógenas"; sugiere que lo exógeno = lo no-actuador. Viola el punto 6 | Reformular sin oponer actuadores a exógenas: "las **variables exógenas** —externas a la planta (consignas, demanda, calidad del agua de entrada)— gobiernan, junto con la **dinámica endógena** del proceso (estado y relaciones físicas, materializada en el lazo de control y sus actuadores), la evolución de un estado interno latente del que los sensores captan una proyección ruidosa". Los actuadores son parte de la dinámica endógena, NO el contrapunto de lo exógeno | 2 |
| **P067** | "Conviene distinguir las variables exógenas, que se determinan fuera del proceso y aportan la estocasticidad, de las endógenas (el estado y sus relaciones físicas)" | Definición en sí **correcta** (exógeno=fuera del proceso; endógeno=estado y relaciones). Conservar, pero queda contaminada por la frase previa que las ata a actuador/no-actuador | Mantener esta definición como ancla y eliminar de P067 toda asociación actuador↔(no)exógeno introducida antes | 2 |
| **P038** | "Sus variables exógenas (no controladas, como la demanda o la calidad del agua de entrada) introducen la estocasticidad, mientras que su estado endógeno evoluciona…" | "exógenas = no controladas" es **impreciso**: el acta define exógeno como *externo a la planta*, no como *no controlado* (una consigna externa es controlada y exógena). Riesgo de difuminar el eje | "Sus variables exógenas (**externas a la planta**: demanda, ambiente, consignas externas, calidad del agua de entrada) introducen la estocasticidad, mientras que las **asociaciones entre sus variables endógenas se mantienen…**" (ver Cat. 3) | 2 |

Nota de cobertura Cat. 2: en **P075** ("modelar por separado los patrones de los sensores y las reglas de los actuadores") y **P088** ("qué sensores o actuadores manipular") el par sensor/actuador se usa en su sentido **legítimo de ingeniería** (tipo de señal / superficie de ataque), NO como definición de endógeno/exógeno → **no requieren cambio**, pero el redactor debe evitar que el lector los confunda con el eje endógeno/exógeno. Lo mismo en P101 ("variables continuas y los actuadores discretos"): correcto, es tipo de señal.

### Categoría 3 — "Asociaciones estables" en lugar de "evolución reproducible por diseño / casi determinista"

Corrección del acta (§5 punto 16): sustituir "su estado endógeno evoluciona de forma reproducible por diseño" por: **bajo las mismas condiciones exógenas, mismo proceso y mismo contexto, las asociaciones entre variables endógenas se mantienen**; lo reproducible es la **lógica de relación**, no la trayectoria física completa. Normalidad = **asociaciones estables entre variables** dado el contexto; anomalía = ruptura de asociaciones.

| Pxxx | Cita actual (verbatim) | Uso incorrecto | Reemplazo exacto exigido por el acta | Cat. |
|------|------------------------|----------------|--------------------------------------|------|
| **P038** | "mientras que su estado endógeno evoluciona de forma reproducible por diseño, gobernado por la física y por la lógica de control" | Frase exacta que el punto 16 manda sustituir ("reproducible por diseño") | "…mientras que, **bajo las mismas condiciones exógenas, el mismo proceso y el mismo contexto, las asociaciones entre sus variables endógenas se mantienen**, gobernadas por la física y por la lógica de control; lo reproducible es la **lógica de relación**, no la trayectoria física completa" | 3 |
| **P067** | "de las endógenas (el estado y sus relaciones físicas), que evolucionan de forma reproducible por diseño" | "reproducible por diseño" (segunda aparición de la frase prohibida) | "…de las endógenas (el estado y sus relaciones físicas), **cuyas asociaciones se mantienen estables bajo las mismas condiciones exógenas y el mismo régimen** (es la lógica de relación lo reproducible, no la trayectoria)" | 3 |
| **P067** | "bajo operación normal, dados el estado y la consigna, la respuesta es casi determinista, gobernada por la física y por la lógica de control, no por grados de libertad arbitrarios" | "casi determinista" + idea de trayectoria reproducible (lo que el punto 16 rechaza: lo reproducible es la relación, no la trayectoria/respuesta) | "bajo operación normal, dados el contexto y el régimen, **las asociaciones entre variables se mantienen** (la lógica de relación es estable), gobernadas por la física y por la lógica de control; la normalidad es esa **estabilidad de asociaciones**, no la repetición de una trayectoria" | 3 |

Nota Cat. 3: la frase de P067 "Esta regularidad de baja entropía es la que habilita una detección entrenada solo sobre operación normal" debe re-anclarse: la regularidad que habilita la detección es la **estabilidad de las asociaciones** dado el contexto, no la baja entropía de la trayectoria. Recomendable reescribir "regularidad de baja entropía" → "estabilidad de las asociaciones entre variables".

### Categoría 4 — Modelo de información (operativo, WP3) vs Ontología (transferencia/interoperabilidad, hilo teórico)

Roles distintos (§5 punto 17): **Modelo de información** = sustrato OPERATIVO (estructura telemetría, asocia variable→proceso/subsistema, define régimen; ligero, fuera de línea; ISA-95/IEC 62264). **Ontología** = horizonte de TRANSFERENCIA/interoperabilidad; independencia de nomenclatura/tags; mapear semántica SWaT↔planta real; NO razonador en el lazo. No compiten.

| Pxxx | Cita actual (verbatim) | Uso incorrecto | Reemplazo exacto exigido por el acta | Cat. |
|------|------------------------|----------------|--------------------------------------|------|
| **P095** | "La robustez y la explicabilidad precisan de un modelo de información que capture la semántica del sistema… Una herramienta habitual para formalizar ese modelo son las ontologías: vocabularios legibles por máquina…" | **Colapsa los dos roles**: presenta la ontología como mera "herramienta para formalizar el modelo de información", borrando la distinción del punto 17 (modelo info = operativo/ahora; ontología = transferencia/generalización). No separa "cómo lo implemento ahora" de "cómo se generaliza" | Diferenciar explícitamente: "(i) un **modelo de información** —sustrato operativo, ligero y fuera de línea (ISA-95/IEC 62264)— que estructura la telemetría, asocia cada variable a su proceso/subsistema y define el régimen, y fija el sesgo inductivo del detector; (ii) separadamente, como **horizonte de transferencia e interoperabilidad**, las **ontologías** (SSN/SOSA) permiten que el método no dependa de la nomenclatura/tags de la planta concreta y mapear la semántica SWaT↔planta real —vía de generalización y posible trabajo futuro, NO razonador en el lazo—" | 4 |
| **P095** | "esta estructura semántica se emplea fuera de línea… y no como un razonador que se ejecute en el lazo de inferencia" | Contenido correcto (no razonador en el lazo) pero atribuido indistintamente a "la estructura semántica" sin separar modelo info / ontología | Mantener la cláusula "no razonador en el lazo", pero **adscribirla al modelo de información operativo** y dejar la ontología en el plano de transferencia (interoperabilidad), conforme al punto 17 y a §5 [v2] ("enmarcar como interoperabilidad, sin atribuirle capacidad de detección") | 4 |
| **P066** | "La cuarta, transversal, es la adquisición y estructuración del contexto operativo (estado del proceso, relaciones físicas y semántica de la planta), sustrato que permite condicionar el criterio de alarma al régimen…" | No distingue el **modelo de información** (operativo, condiciona el detector) del horizonte ontológico (transferencia). Mezcla "semántica de la planta" (transferencia) con "condicionar el criterio de alarma" (operativo) | Precisar que el sustrato operativo que condiciona el criterio de alarma es el **modelo de información** (estado, relaciones físicas, régimen); la "semántica de la planta" en sentido de independencia de nomenclatura pertenece al horizonte de **transferencia/ontología**, no al lazo operativo | 4 |

Nota Cat. 4: el acta sitúa la ontología en el **hilo de transferibilidad** con respaldo DÉBIL en agua → P095 debe rebajar el tono (interoperabilidad / trabajo futuro), nunca presentar la ontología con capacidad de detección. Refs 69/71/72 (SSN/SOSA, revisiones) sostienen el hilo de transferibilidad, no el detector (§7 del acta).

### Categoría 5 — Información (estado inferido) vs Decisión (reglas/costes/utilidad = gobierno de la alarma)

Regla del acta (§5 punto 15): **Representación del contexto** = SÍ información (estado inferido; alimenta el criterio). **Operacionalización de la decisión** = NO información observacional; aporta **reglas, restricciones, costes, utilidad** (gobierno de la alarma). No colapsar ambos.

| Pxxx | Cita actual (verbatim) | Uso incorrecto | Reemplazo exacto exigido por el acta | Cat. |
|------|------------------------|----------------|--------------------------------------|------|
| **P037** | "Las alternativas plantean que la representación explícita del contexto operativo y la operacionalización de la decisión **aportan información adicional**." | Colapsa los dos planos: atribuye "aportar información" también a la operacionalización de la decisión, que según el punto 15 **NO es información observacional** sino gobierno de la alarma | "…la representación explícita del contexto operativo (que **aporta información**: estado inferido) y la operacionalización de la decisión (que **no aporta información observacional, sino reglas, restricciones, costes y utilidad** —gobierno de la alarma—) **contribuyen marginalmente al rendimiento operativo**" — sustituir "aportan información adicional" por una formulación que separe los dos roles | 5 |
| **P047 / P139** | P047: "Cuantificar la contribución de la operacionalización de la detección (criterio de decisión, puntuación… y umbral) al rendimiento operativo." · P139: "estima la contribución marginal de la capacidad del modelo, de la representación del contexto y de la operacionalización de la decisión" | Trata la operacionalización en pie de igualdad con la "información" del contexto sin marcar que es **gobierno de la alarma** (reglas/costes/utilidad), no estado observacional | Mantener "contribución al rendimiento", pero aclarar al menos una vez (preferible en P037 o P051) que la operacionalización **no es información observacional sino la operacionalización de la decisión**: criterio, costes y utilidad que gobiernan la alarma (punto 15) | 5 |

Nota Cat. 5: el acta ya formula el patrón correcto en §3 (Delimitación): "La operacionalización de la decisión (reglas, restricciones, costes, utilidad) NO es información observacional, sino gobierno de la alarma; se distingue de la representación del contexto, que sí es estado inferido". El plan debe importar esa distinción explícita; hoy la difumina en P037 (y la deja implícita en P047/P051/P139).

---

## Notas de uso (para el redactor de FASE 2 — aplicación uniforme)

1. **Umbral con oráculo (Cat. 1).** Término único en TODO el documento: **"selección de umbral con oráculo sobre el conjunto de prueba"**. Glosar el inglés *best-F1 / oracle thresholding* **una sola vez**, en su primera aparición (será P065 según el orden del texto; si se reordena, en la primera que quede). *best-F1* y *data leakage* nunca como sujeto ni como nombre del fenómeno: solo como sinónimo entre paréntesis. Prohibido en el resto del plan: "filtración de datos de prueba", "filtración del umbral", "umbral óptimo a posteriori", "fuga/sin la verdad de referencia", "threshold leakage". Respaldo citable: Kim et al. 2022; Lamberts et al. 2023 (+ Garg et al. 2021, Wu & Keogh 2021 ya presentes).

2. **Oráculo ≠ ajuste por puntos.** Son dos artefactos distintos que suelen ir juntos; mantenerlos **nombrados por separado** ("selección de umbral con oráculo" y "ajuste por puntos / *point adjustment*"). No fundirlos en una sola etiqueta.

3. **Endógeno/exógeno (Cat. 2).** Eje único válido: **exógeno = externo a la planta** (demanda, ambiente, consignas externas); **endógeno = interno a la dinámica del proceso** (estado y relaciones físicas). Prohibido el eje **actuador/sensor** como definición de endógeno/exógeno (los actuadores son parte de la dinámica endógena/lazo de control). Evitar también "exógeno = no controlado" (impreciso: una consigna externa es controlada y exógena). El par sensor/actuador puede seguir usándose para *tipo de señal* y *superficie de ataque* (P075, P088, P101), pero nunca cerca de la definición de endógeno/exógeno sin desambiguar.

4. **Asociaciones estables (Cat. 3).** Erradicar "reproducible por diseño" y "casi determinista" en todo el texto. Fórmula canónica: bajo las mismas **condiciones exógenas, mismo proceso y mismo contexto/régimen**, **las asociaciones entre variables endógenas se mantienen**; lo reproducible es la **lógica de relación**, no la trayectoria física completa. Normalidad = **asociaciones estables entre variables** dado el contexto; anomalía = **ruptura de asociaciones**. Sustituir "regularidad de baja entropía" (P067) por "estabilidad de las asociaciones".

5. **Modelo de información ≠ ontología (Cat. 4).** Dos roles, nunca intercambiables:
   - **Modelo de información** = sustrato **operativo** (WP3): estructura la telemetría, asocia variable→proceso/subsistema, define régimen; ligero, **fuera de línea**; **NO razonador en el lazo**; ISA-95/IEC 62264. Es el "cómo lo implemento ahora".
   - **Ontología** = horizonte de **transferencia/interoperabilidad** (hilo teórico): independencia de nomenclatura/tags, mapear semántica SWaT↔planta real; trabajo futuro; **sin capacidad de detección**. Es el "cómo se generaliza".
   En P095 no presentar la ontología como "herramienta para formalizar el modelo de información" (eso los colapsa). Tono prudente en agua (respaldo débil). Refs SSN/SOSA (P175) y revisiones (P183, P185) sostienen el hilo de transferibilidad, no el detector.

6. **Información ≠ decisión (Cat. 5).** **Representación del contexto** = SÍ información (estado inferido; alimenta el criterio de detección). **Operacionalización de la decisión** = NO información observacional; son **reglas, restricciones, costes, utilidad** = **gobierno de la alarma**. No escribir que la operacionalización "aporta información" (corregir P037). Importar la frase ya redactada en §3 del acta como formulación de referencia.

7. **Tono calibrado (transversal, refuerza 1–6).** Coherente con §6 del acta: "efecto observado sobre el rendimiento dentro del diseño experimental considerado", nunca "contribución causal". Aplica al describir las contribuciones marginales de los factores (P037, P049, P051, P109, P139).

---

### Resumen final (recuentos y apariciones críticas)

- **Cat. 1 (umbral con oráculo): 9 incidencias** en P065 (×4), P084 (×2), P113, P114, P117. El acta solo nombraba P065/P084/P114/P117; esta auditoría añade **P113** ("filtración del umbral"). Término único obligatorio: "selección de umbral con oráculo sobre el conjunto de prueba" (best-F1 / oracle thresholding glosado una sola vez). Prohibido usar best-F1/"filtración de datos de prueba" como sujeto.
- **Cat. 2 (endógeno/exógeno): 3.** Crítico **P067**, que opone "actuadores" a "perturbaciones exógenas" (eje actuador/sensor vetado por el punto 6). P038 usa "exógeno = no controlado" (impreciso). P075/P088/P101 usan sensor/actuador legítimamente (tipo de señal) → no se tocan.
- **Cat. 3 (asociaciones estables): 3.** "reproducible por diseño" aparece en **P038 y P067**; "casi determinista" en **P067**. Las tres se sustituyen por la fórmula de asociaciones estables del punto 16.
- **Cat. 4 (modelo info vs ontología): 2–3.** **P095** colapsa ambos roles (ontología como "herramienta del modelo de información"); P066 mezcla sustrato operativo con semántica de transferencia. Separar operativo (ISA-95, fuera de línea, no razonador) de transferencia (SSN/SOSA, interoperabilidad, trabajo futuro).
- **Cat. 5 (información vs decisión): 2.** **P037** dice que la operacionalización "aporta información adicional" → viola el punto 15 (es gobierno de la alarma: reglas/costes/utilidad, no información observacional). P047/P139 lo dejan implícito; conviene marcarlo una vez.
- **Apariciones más críticas: P067** (concentra Cat. 2 + Cat. 3, dos correcciones doctrinales) y **P065** (concentra 4 variantes prohibidas del término de umbral). Ambos párrafos son de obligada reescritura en FASE 2.
