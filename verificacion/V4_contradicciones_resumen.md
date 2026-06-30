# V4 — Contradicciones y coherencia del resumen e introducción

> Informe de verificación READ-ONLY. No reescribe el plan; diagnostica.
> Fuente de verdad: `insumos/Acta_Decisiones_v2_Reestructuracion_Plan.md`.
> Texto auditado: `trabajo/plan_actual.md` — resumen (P036–P040), objetivos/hipótesis
> (P042–P056), introducción (P057–P069). Título en P006.

## Resumen ejecutivo

El resumen y la introducción actuales pertenecen al **plan v36 anterior** y chocan
frontalmente con el giro del acta en cuatro frentes graves:

1. **Estructura de hipótesis (P037, P051–P056).** El texto sostiene el esquema
   "**tres hipótesis competidoras H0/H1/H2 + ablación factorial**" que el acta §3
   sustituye explícitamente por **hipótesis central (explicativa) + hipótesis de
   trabajo (mecanismo) + interpretabilidad como consecuencia + delimitación**. Es la
   contradicción estructural mayor: el plan promete contrastar una H0 nula y estimar
   contribuciones marginales factoriales de "representación del contexto" y
   "operacionalización de la decisión", factores que el acta reordena por completo.

2. **"Reproducible por diseño" (P038, P067).** Ambos párrafos afirman que el estado
   endógeno **"evoluciona de forma reproducible por diseño"**. El acta (punto 16,
   §5) lo corrige expresamente: lo reproducible es la **lógica de relación
   (asociaciones entre variables endógenas)**, NO la trayectoria física. Contradicción
   literal con una corrección que el acta marca como "✔ resuelto".

3. **Confusión exógenas / actuadores (P067).** P067 define "las entradas de control
   (los actuadores, como bombas y válvulas) y las perturbaciones exógenas". El acta
   (§5, punto 6) prohíbe esa lectura: **exógenas = externas a la planta; endógenas =
   internas a la dinámica; NO actuador vs sensor**. Los actuadores son internos al
   lazo de control, no exógenos.

4. **Objeto y delimitación (P036, P038, P039, P044, P050).** El resumen aún trata los
   testbeds como banco de validación de un detector ("se demuestra eficacia"), arrastra
   marco IIoT/edge (P040, P043, P050) que el acta manda purgar, y promete viabilidad de
   despliegue en hardware de borde como objetivo específico, todo ello en tensión con el
   giro "testbed = objeto de estudio crítico, no campo de aplicación".

La frase de delimitación de P038 ("eficacia bajo condiciones operativas simuladas, no
efectividad en operación real") es **direccionalmente correcta** y compatible con el
acta, pero queda **aislada y contradicha** por el resto del resumen/objetivos, que sí
prometen lo que esa frase niega (cerrar/medir la brecha vía factores accionables,
despliegue, atribución como artefacto central).

---

## Contradicciones

| Pxxx | Cita (literal) | Tipo | Choca con (decisión acta) | Criterio de resolución |
|------|----------------|------|---------------------------|------------------------|
| **P037** | "Se contrastan **tres hipótesis competidoras**. La **hipótesis nula** sostiene que aumentar la capacidad predictiva del modelo basta para cerrar la brecha." | Estructura de hipótesis incompatible | §3: el acta sustituye H0/H1/H2 por **central (explicativa) + trabajo (mecanismo) + interpretabilidad consecuencia + delimitación**. Punto 21 "✔ resuelto". | Reescribir el resumen con la pareja central/trabajo. Eliminar la noción de "hipótesis nula que combatir". La central "no se cae nunca; promete demostrar y medir, no resolver" (§3). |
| **P037** | "estimar la **contribución marginal de cada factor**, y su interacción, mediante un protocolo de **ablación factorial** declarado y condicional al pipeline fijado." | Método declarado obsoleto | §3 e implícito: la ablación factorial de v36 sobre los factores "contexto/operacionalización" se sustituye por **aislar y estimar el efecto observado** de los factores del acta (oráculo de umbral, point adjustment, no estacionariedad, régimen) dentro de un diseño controlado. WP2. | Mantener "diseño experimental controlado" y "efecto observado", pero referido a los factores del acta §3 (metodológicos + de naturaleza del sistema), no a "contexto vs operacionalización". Calibrar: "efecto observado", nunca "contribución" (riesgo causal, punto 18). |
| **P037** | "la representación explícita del **contexto operativo** y la **operacionalización de la decisión** aportan información adicional." | Mezcla de planos información/decisión | Punto 15 (§5): la **operacionalización de la decisión NO aporta información observacional**; aporta reglas/costes/utilidad (gobierno de la alarma). Solo la representación del contexto aporta información (estado inferido). | No presentar la operacionalización como factor que "aporta información". Distinguir: contexto = información (estado inferido); decisión = gobierno de la alarma, distinto de la representación. |
| **P038** | "su estado endógeno **evoluciona de forma reproducible por diseño**, gobernado por la física y por la lógica de control" | Afirmación factual corregida por el acta | Punto 16 (§5): ANTES "estado endógeno evoluciona de forma reproducible por diseño" → DESPUÉS "las **asociaciones entre variables endógenas se mantienen**; lo reproducible es la **lógica de relación, no la trayectoria** física". | Sustituir por: bajo mismas condiciones exógenas, mismo proceso y régimen, **se preservan las asociaciones** entre endógenas; lo reproducible es la lógica de relación. No afirmar trayectoria determinista. |
| **P038** | "su estado endógeno evoluciona... mientras que sus **variables exógenas** (no controladas, como la demanda o la calidad del agua de entrada) introducen la estocasticidad" | Parcial: definición de exógenas correcta aquí, pero marco "estocasticidad vs reproducible" hereda el error de trayectoria | Punto 6 / punto 16. La dicotomía correcta no es "exógena=estocástica vs endógena=trayectoria reproducible", sino exógena=externa / endógena=interna, con **asociaciones estables** dado el contexto. | Conservar la lista de exógenas (demanda, calidad de entrada = correctas), pero reencuadrar: la regularidad está en las asociaciones, no en una evolución determinista del estado. |
| **P038** | "se demuestra **eficacia bajo condiciones operativas simuladas, no efectividad en operación real**, que se reconoce como trabajo futuro." | Coherente con el acta **pero contradicha por el entorno** | §1 y §3 (delimitación): correcto que los testbeds no dan efectividad real y que planta real = trabajo futuro. PERO el resto del resumen/objetivos prometen lo contrario (medir/cerrar brecha, despliegue, atribución central). | Conservar y **reforzar** esta frase; alinear el resto del resumen para que no prometa lo que ella delimita. Precisar además que "condiciones operativas simuladas" es el testbed como **objeto de estudio**, no validación de un producto. |
| **P038 / P039** | "se demuestra eficacia" / "una **metodología de atribución** y un conjunto de **principios de diseño** para acercar la detección a la operación." | Objeto de la tesis mal enfocado | §1: el testbed es **objeto de estudio crítico**, no campo de aplicación; la contribución medible es la **caída de rendimiento entre condiciones / efecto de cada factor / degradación bajo deriva**, no "acercar la detección a la operación" como verbo de producto. | Reescribir el objeto como diagnóstico de la brecha (por qué fracasan los detectores de banco al desplegarse, qué la reduce). La atribución/principios se subordinan a ese diagnóstico, no son la promesa central. |
| **P067** | "las **entradas de control (los actuadores, como bombas y válvulas)** y las **perturbaciones exógenas** (no controladas...) gobiernan la evolución de un estado interno latente" | Categoría errónea: actuadores tratados como entradas junto a exógenas | Punto 6 (§5): **exógenas = externas a la planta** (demanda, ambiente, consignas externas); **endógenas = internas a la dinámica**; **NO actuador vs sensor**. Los actuadores son internos al lazo de control. | Separar claramente: exógenas = externas (demanda, calidad de entrada, ambiente). Los actuadores NO son exógenos: son parte de la dinámica interna gobernada por la lógica de control. No equiparar "entradas de control" con "perturbaciones exógenas". |
| **P067** | "las endógenas (el estado y sus relaciones físicas), que **evolucionan de forma reproducible por diseño**: ... la respuesta es **casi determinista**" | Repetición de la afirmación corregida (segunda instancia) | Punto 16 (§5), igual que P038. | Igual criterio que P038: lo reproducible es la **lógica de relación / las asociaciones**, no la respuesta casi determinista del estado. Reescribir en línea con la corrección del punto 16. |
| **P036** | "infraestructuras hídricas entendidas como sistemas de control industrial (ICS)... o, más en general, como sistemas ciberfísicos (CPS)" | Alcance demasiado amplio | Puntos 10, 12, 13 (§6): trabajar con **series temporales del proceso físico (OT, niveles 0-2 Purdue)**, NO "ICS" en sentido amplio (IT+OT, redes, protocolos). | Acotar el resumen a series temporales multivariantes de la capa OT del proceso de agua. Evitar el salto "más en general a CPS" si no se delimita el plano OT. |
| **P040 / P043 / P050** | P040 kw "despliegue en hardware de borde"; P043 "ámbito del Internet Industrial de las Cosas (IIoT)"; P050 obj. 5 "viabilidad de despliegue en hardware de borde" | Literatura/marco a purgar | Puntos 10, 12 (§6): **PURGAR IIoT, manufactura, visión, IA general**. §1: despliegue/edge no es el objeto. | Quitar IIoT como encuadre. Rebajar "viabilidad de despliegue" de objetivo a, como mucho, consecuencia operativa menor o trabajo futuro; no como objetivo específico del diagnóstico de la brecha. |
| **P051 / P052** | "Hipótesis general... **dos factores habitualmente implícitos: la representación del contexto... y la operacionalización de la decisión**." / "se contrastan **tres hipótesis competidoras**, mediante un protocolo de **ablación factorial**" | Hipótesis general del v36, no la del acta | §3: la hipótesis central del acta identifica **factores metodológicos (oráculo de umbral, point adjustment) + de naturaleza del sistema (no estacionariedad, régimen)**, no "representación vs operacionalización". | Sustituir la hipótesis general por la central del acta (texto §3, sin redactar aquí). Los dos ejes "contexto/decisión" del v36 no son el núcleo. |
| **P053** | "**H0 (nula).** Fijada la capacidad del modelo, ni la representación del contexto ni la operacionalización producen una mejora marginal estadísticamente significativa..." | Hipótesis nula que el acta elimina | §3: no hay H0/H1/H2; hay central + trabajo. La central "no se cae nunca". | Eliminar H0/H1/H2 como tales. Si se conserva contraste estadístico, es para **estimar el efecto observado de cada factor** del acta, no para refutar una nula sobre "contexto/operacionalización". |
| **P054 / P055** | "**H1.** La representación explícita del contexto... aporta una contribución marginal significativa..." / "**H2.** La operacionalización consciente del tipo de señal... aporta una contribución marginal significativa..." | Hipótesis alternativas del v36 | §3 y punto 15: ni el desdoblamiento H1/H2 ni el marco "operacionalización aporta contribución" sobreviven al acta. | Reconvertir el contenido útil (régimen/contexto) a la **hipótesis de trabajo (mecanismo)** del acta: ruptura de asociaciones condicionada al régimen. Sacar la "operacionalización" del plano de hipótesis con aporte de información. |
| **P056** | "El **diseño factorial** estima además si el efecto conjunto de H1 y H2 supera la suma de sus efectos aislados. Cada hipótesis se da por corroborada si... no se rechaza H0 para ese factor." | Aparato H0/H1/H2 + factorial completo | §3 (estructura) + punto 18 (causalidad). | Eliminar el lenguaje "no se rechaza H0". Reemplazar por estimación del efecto observado de los factores del acta dentro del diseño controlado, sin marco de hipótesis competidoras. |
| **P044** | Objetivo general: "determinar qué factores explican la brecha... y **estimar la contribución marginal de cada uno, condicional al pipeline, mediante un protocolo de ablación factorial**." | Objetivo formulado sobre el método obsoleto | §3 + §4 (WP1/WP2): el objetivo es **tipificar** los factores (WP1) y **cuantificar el efecto observado** de cada uno en diseño controlado (WP2). | Mantener "qué factores explican la brecha" (correcto, alineado con la pregunta raíz), pero reformular el método como diseño controlado sobre los factores del acta; "efecto observado", no "contribución marginal causal". |
| **P057–P069 (intro) vs P070+ (cuerpo)** | La intro presenta "dos candidatos no excluyentes: representación del contexto y operacionalización de la decisión" (P068), mientras el cuerpo (3.4–3.7) ya describe oráculo de umbral, point adjustment, deriva y normality shift como ejes. | Incoherencia interna intro ↔ cuerpo | §3: los factores reales del acta (metodológicos + naturaleza del sistema) ya aparecen en el cuerpo (P065, P084, P090), pero la intro los subordina al binomio v36 "contexto/operacionalización". | Alinear P068 con la hipótesis central del acta: los factores que organizan el estudio son los del acta. El binomio "contexto/operacionalización" deja de ser el organizador de la pregunta. |

---

## Promesas que la delimitación niega

El acta §3 (Delimitación explícita) y §1 fijan lo que **NO se afirma**. El texto actual
promete varias de esas cosas:

1. **Reducir/medir la brecha como utilidad operativa real (P036, P044, P051).**
   El resumen dice investigar "qué factores explican la brecha entre el rendimiento...
   y su **utilidad en condiciones operativas**" y "estimar la contribución marginal de
   cada uno". El acta: la contribución medible es **caída de rendimiento entre
   condiciones / efecto de cada factor / degradación bajo deriva** sobre testbeds, NO
   utilidad en operación real ni reducción de la brecha en una planta concreta.

2. **Efectividad / acercamiento a la operación como entregable (P038, P039, P050).**
   "Acercar la detección a la operación" (P039) y "caracterizar la **viabilidad de
   despliegue en hardware de borde**" (P050) como objetivo específico. El acta delimita
   el despliegue/operación real como **prueba de concepto / trabajo futuro**, no como
   métrica ni objetivo. P038 ya lo reconoce ("trabajo futuro") pero P039/P050 lo
   reintroducen como promesa.

3. **Operacionalización de la decisión como fuente de información/contribución
   (P037, P047, P051, P055).** El plan la trata como factor que "aporta información
   adicional" (P037) y cuya "contribución" se cuantifica (obj. 2, H2). El acta
   (punto 15, y delimitación §3): la operacionalización **NO es información
   observacional**, es gobierno de la alarma (reglas, restricciones, costes, utilidad);
   se distingue de la representación del contexto.

4. **Atribución/explicación con riesgo de deriva causal (P039, P049, intro P067).**
   "Metodología de atribución" (P039) y obj. 4 "método de atribución que estime la
   contribución marginal de cada factor". El acta (puntos 9, 18; §3 interpretabilidad):
   la interpretabilidad es **consecuencia, no hipótesis**, y describe **qué asociación
   se rompió, no por qué (causa)**; nunca "contribución causal". El término
   "contribución" en contexto de atribución debe calibrarse a "efecto observado".

5. **Marco IIoT / CPS amplio (P036, P040, P043).** Encuadrar la tesis en IIoT (P043)
   y CPS general (P036) y listar "despliegue en hardware de borde" como palabra clave
   (P040). El acta (puntos 10–13): purgar IIoT/manufactura/IA general; trabajar solo
   con **series OT del proceso (niveles 0-2 Purdue)**.

6. **Métricas de detección implícitamente extensibles a planta (P133, contexto del
   resumen).** Aunque P133 (fuera del rango pedido) lo reconoce, el resumen no aclara
   que los datos de planta real **no permiten métricas de detección** (sin verdad de
   referencia). El acta §1 lo exige: planta sin etiquetar = **evidencia descriptiva**,
   no fuente de métricas.

---

## Incoherencias título / resumen / objetivos / hipótesis

Coherencia evaluada **tal como está hoy** (lo que la reescritura deberá resolver):

1. **Título (P006) ↔ giro del acta.**
   Título: *"**Contribuciones a la detección de anomalías** en sistemas de control
   industrial de infraestructuras hídricas mediante técnicas de Inteligencia
   Artificial"*. El acta §1 dice explícitamente que el objeto **NO es** "contribuir a
   la detección de anomalías en ICS hídricos", sino **explicar por qué los detectores
   de banco fracasan al desplegarse y qué reduce la brecha**. El título promete
   justamente lo que el acta descarta como enunciado del objeto. → La reescritura tendrá
   que reorientar el título hacia la brecha banco↔despliegue / transferibilidad, o al
   menos hacia "evaluación rigurosa y factores de la brecha", no "contribuciones a la
   detección". (Además "sistemas de control industrial" debería acotarse a series OT,
   niveles 0-2 — puntos 11, 13.)

2. **Título ↔ resumen.** El título es de producto ("contribuciones a la detección");
   el resumen (P036) ya gira a "qué factores explican la brecha". Hay desalineación:
   el resumen está más cerca de la pregunta raíz que el título, pero el resumen luego
   recae en aparato de detección/ablación (P037). Coherencia parcial, ambos a corregir.

3. **Resumen ↔ objetivos.** El resumen plantea **tres hipótesis competidoras**
   (P037); los objetivos (P051–P056) las desarrollan como H0/H1/H2 — internamente
   consistentes **entre sí**, pero ambos consistentes con el **marco v36 equivocado**,
   no con el acta. La incoherencia no es resumen-vs-objetivos sino **ambos-vs-acta**.

4. **Resumen/objetivos ↔ hipótesis del acta.** Punto crítico: el acta (§3) define
   central + trabajo + interpretabilidad-consecuencia; el texto define H0/H1/H2 +
   interacción factorial. **No hay correspondencia 1:1**: la "hipótesis de trabajo"
   del acta (ruptura de asociaciones condicionada al régimen) **no figura como tal** en
   resumen ni objetivos; lo más próximo es H1 (P054), pero H1 está formulada como
   "aporta contribución marginal", no como mecanismo de detección por ruptura de
   asociaciones. La reescritura debe **crear** la hipótesis de trabajo y degradar la
   interpretabilidad de objetivo a consecuencia.

5. **Objetivo 1 (P046) ↔ resto.** El obj. 1 (protocolo de evaluación riguroso e
   insesgado, "suelo metodológico") **sí** es coherente con el acta (WP1/WP2, panel de
   métricas, §4). Es el componente más rescatable. Pero queda subordinado a un objetivo
   general (P044) y a hipótesis (P051–P056) formulados sobre el marco obsoleto, lo que
   crea fricción: una pieza alineada dentro de un andamiaje desalineado.

6. **Objetivo 4 (P049) ↔ artefacto nuclear.** Obj. 4 hace del "método de atribución"
   el destilado central; el acta subordina la atribución/interpretabilidad a
   consecuencia (no hipótesis) y al diagnóstico de la brecha. El "método de atribución"
   como artefacto de primera clase es coherente con el cuerpo metodológico (P101) pero
   **no** con la jerarquía del acta, donde la contribución es la **integración**
   (detección condicionada al régimen + protocolo de transferencia + evaluación
   realista, §8), no un método de atribución factorial.

7. **Palabras clave (P040) ↔ alcance del acta.** Incluyen "aprendizaje profundo",
   "explicabilidad", "despliegue en hardware de borde" como ejes destacados; el acta
   (punto 1, §2) advierte que robustez, interpretabilidad y transferencia son **ejes,
   no la pregunta**, y purga el énfasis edge/IIoT. Las kw sobre-prometen líneas que el
   acta degrada a consecuencia o trabajo futuro.

---

### Nota de cobertura
Todas las citas provienen de `trabajo/plan_actual.md` (P006, P036–P040, P042–P056,
P057–P069) y se contrastan contra `insumos/Acta_Decisiones_v2_Reestructuracion_Plan.md`
(§§1–6, puntos 6, 9, 10–13, 15, 16, 18, 21). No se ha redactado texto sustitutivo: solo
criterios de resolución, conforme al mandato READ-ONLY.
