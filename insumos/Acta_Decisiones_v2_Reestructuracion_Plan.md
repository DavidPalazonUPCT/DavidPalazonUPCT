# Acta de decisiones v2 — Reestructuración del Plan de Investigación
### (reforzada y corregida con revisión bibliográfica)

> Documento de trabajo. Fuente de verdad para reescribir el plan.
> v2 incorpora: 5 correcciones derivadas de la revisión bibliográfica, respaldo
> citable por hipótesis y por WP, y sección nueva de posicionamiento frente a
> trabajos solapados. Cambios respecto a v1 marcados con **[v2]**.

---

## 0. Cambios sustantivos introducidos por la investigación **[v2]**

1. **Terminología corregida:** "fuga de la verdad de referencia / threshold leakage"
   → **"selección de umbral con oráculo sobre el conjunto de prueba"**
   (*best-F1 / oracle thresholding*). Es el término de la literatura revisada por
   pares (Kim et al. 2022; Lamberts et al. 2023). Aplicar en TODO el plan.
2. **Causalidad:** NO es una hipótesis de la tesis (nunca lo fue; revisión de los 21
   puntos lo confirma). El punto 9 (explicar ≠ explicar un proxy) queda REFORZADO por
   Fung et al. (NDSS 2024), que demuestran empíricamente que la atribución de features
   falla justo donde se la creía robusta (actuadores categóricos). Entra como soporte
   del punto 9, no como afirmación causal.
3. **Posicionamiento frente a solapamientos (NUEVO):** tres trabajos ya cubren piezas
   sueltas (Heydari & Nyarko 2026 = evaluación alarm-budget; Cai et al. SA² 2024 =
   sensor/actuador espaciotemporal; Han et al. OWAD 2023 = normality shift). La
   contribución NO son las piezas: es la **integración** + el dominio (series OT de
   proceso de agua, niveles 0-2 Purdue). Ver §8.
4. **Gap confirmado:** NO existe protocolo canónico de transferencia
   SWaT→WADI→planta real con métricas deployment-realistas. Justifica WP1/WP2.
5. **Correcciones factuales a propagar:** (a) "24/36 ataques, cero FP" es de AICrit
   (Raman & Mathur), NO de Koutroulis (cuyo dato es F1≈0,941, cero FP, 4 ataques no
   detectados que tampoco cumplían su objetivo físico). (b) La evidencia de concept
   drift / normality shift proviene mayormente de NIDS/logs SCADA: trasladable a OT de
   proceso, pero declararlo explícitamente, no presentarlo como demostrado en agua.

---

## 1. Giro de fondo del objeto de la tesis

**NO es** "contribuir a la detección de anomalías en ICS hídricos".
**ES** el estudio de por qué los detectores que rinden en banco de pruebas fracasan al
desplegarse en sistemas ciberfísicos reales, y qué reduce esa brecha.

- Testbeds (SWaT, WADI, BATADAL, HAI) = **objeto de estudio crítico**, no campo de aplicación.
- Datos de planta sin etiquetar = **evidencia descriptiva del problema** (prueba de
  concepto / trabajo futuro, NO métricas de detección).
- Contribución **medible**: caída de rendimiento entre condiciones, efecto de cada factor
  dentro del diseño, degradación bajo deriva.

*(Puntos 2, 3, 14.)* **[v2]** Respaldo del gap de transferencia: no hay estudio canónico
SWaT→WADI→planta real con protocolo común (revisión, Foco 1c).

---

## 2. Pregunta raíz (punto 20)

> ¿Por qué los modelos de detección de anomalías, pese a su alto rendimiento en entornos
> experimentales, fracasan al desplegarse en sistemas ciberfísicos reales, y cómo puede
> reducirse esa brecha?

Robustez, interpretabilidad y transferencia = ejes de investigación, NO la pregunta.
Pueden surgir contribuciones en ellos, pero no se prometen como objetivo central.

---

## 3. Núcleo de hipótesis (puntos 1, 21)

### Hipótesis central (explicativa — nivel tesis)

> La discrepancia entre el rendimiento en banco de pruebas y el esperable en despliegue
> real no es un artefacto aleatorio, sino el efecto de un conjunto identificable de
> factores: (a) metodológicos de la evaluación —selección de umbral con oráculo sobre el
> conjunto de prueba, y ajuste por puntos (point adjustment)—; (b) propios de la
> naturaleza del sistema —no estacionariedad y dependencia del régimen operativo—. El
> efecto observado de cada factor sobre el rendimiento puede aislarse y estimarse dentro
> de un diseño experimental controlado.

- "Efecto observado dentro de un diseño controlado", NUNCA "contribución causal" (punto 18).
- No promete resolver; promete demostrar y medir. No se cae nunca.

**[v2] Respaldo bibliográfico (SÓLIDO):**
- Point adjustment infla el rendimiento (ruido aleatorio supera al SOTA; F1_PA correlaciona
  pobremente con F1): **Kim et al., AAAI 2022, 36(7):7194-7201** (PCC/KRC −0,59/0,07 SWaT;
  0,41/0,43 WADI).
- Benchmarks defectuosos / "progreso ilusorio": **Wu & Keogh, IEEE TKDE 35(3):2421-2429**.
- Métricas alternativas: **Paparrizos et al. (VUS/VUS-PR), VLDB 2022, 15(11):2774-2787**;
  **Huet et al. (affiliation), KDD 2022**; **Garg et al. (composite Fc1), TNNLS 2021,
  33(6):2508-2517**.
- Evaluación deployment-realista (alarm budget, event-level): **Heydari & Nyarko, IEEE
  Access 2026, 14:17585-17609** (rankings se invierten bajo restricción de carga del
  operador); **Lamberts et al., SoK, J. Systems Research 2023** (~1,3 datasets/paper).
- Concept drift / normality shift: **Gama et al., ACM CSUR 2014, 46(4):44**; **Lu et al.,
  IEEE TKDE 2019, 31(12):2346-2363**; **Han et al. (OWAD), NDSS 2023**; **Bayram et al.,
  KBS 2022, 245:108632**.
- Evidencia empírica de la brecha (fragmentada): **Fung et al., ESORICS 2022**
  (inconsistencia entre datasets); **Erba et al., ACSAC 2020** (recall WADI 0,68→0,12
  manipulando 4/82 sensores).

### Hipótesis de trabajo (mecanismo — nivel paper, dos componentes unificados)

> El estado operativo de la planta es latente y se manifiesta en asociaciones estables
> entre las variables medidas.
> (a) *Contexto:* esas asociaciones dependen del régimen operativo; el criterio de
>     normalidad debe condicionarse al régimen, no aplicarse de forma global.
> (b) *Mecanismo:* bajo las mismas condiciones exógenas y el mismo régimen, la evolución
>     de las variables endógenas preserva esas asociaciones; su ruptura es un indicador de
>     anomalía más robusto frente a la deriva que el valor individual de cada variable o
>     que una puntuación agregada umbralizada globalmente.

**[v2] Respaldo bibliográfico (SÓLIDO en invariantes/state-aware/grafos; MODERADO en agua):**
- Invariantes / relaciones físicas: **Feng et al., NDSS 2019** (9.006 reglas SWaT, 10.490
  WADI; superan invariantes manuales); **Adepu & Mathur, IEEE TDSC 2021, 18(1):86-99**;
  **Umer et al., IJCIP 2020, 28:100341** (design+data-centric, ninguno basta solo);
  **Pal et al., HASE 2017** (association rule mining).
- Detección condicionada al estado: **Ghaeini et al., SAC 2018** (umbrales state-dependent,
  CUSUM state-aware); **Li et al., IEEE TKDE, DOI 10.1109/TKDE.2022.3171562** (espacio de
  estados profundo robusto a contaminación).
- Grafos inter-sensor: **Deng & Hooi (GDN), AAAI 2021, 35(5):4027-4035** (precisión 0,99
  SWaT / 0,98 WADI; +54% F en WADI).
- **[v2] CAVEAT (techo conocido):** las invariantes tienen techo frente a ataques sigilosos
  — AICrit (**Raman & Mathur, JISA 2022, 64:103046**) logra cero FP pero detecta solo
  24/36 escenarios en SWaT. Reconocerlo en el plan.

### Interpretabilidad — consecuencia, NO hipótesis

> Si la detección opera por ruptura de asociaciones condicionada al régimen, la alarma
> identifica qué asociación y en qué régimen se ha roto: explicación nativa del disparo.
> Describe el evento detectado, sin afirmación causal sobre el origen físico.

**[v2] Refuerzo del punto 9 (explicar ≠ explicar un proxy):** **Fung et al., NDSS 2024**
demuestran que la atribución de features NO rinde tan bien como se afirmaba —es inexacta
en el punto de detección y falla con actuadores categóricos—. Esto CONFIRMA la cautela del
punto 9: la explicación describe qué asociación se rompió, no por qué (causa). NO se
introduce causalidad como afirmación; se cita esta tensión de forma explícita.

### Delimitación explícita (lo que NO se afirma)

> No se afirma reducir la brecha en una planta real concreta: los datos de planta carecen
> de verdad de referencia de ataques y no permiten métricas de detección (prueba de
> concepto / trabajo futuro). La operacionalización de la decisión (reglas, restricciones,
> costes, utilidad) NO es información observacional, sino gobierno de la alarma; se
> distingue de la representación del contexto, que sí es estado inferido de los datos
> (punto 15).

### Dos planos
- Central → gobierna **WP1-WP2** (diagnóstico).
- Trabajo → gobierna **WP3** (propuesta).
- Visualmente separados: diagnóstico vs. solución.

*(Hipótesis excluyentes entre sí en lo que afirman: caracterizar ≠ contexto/mecanismo.
Cada una puede ser cierta o falsa sin que las otras la determinen. Resuelve punto 1.)*

---

## 4. Estructura en Work Packages (punto 19) **[v2 con respaldo y posicionamiento]**

| WP | Tipo | Objetivo | Hipótesis | Salida | Cierre |
|----|------|----------|-----------|--------|--------|
| **WP0** | Transversal | Marco conceptual (estado latente, asociaciones, endógeno/exógeno, modelo info vs ontología, alcance OT/series, Purdue) | — | Plan + marco teórico | Sustrato fijado |
| **WP1** | Diagnóstico | Revisión acotada del SOTA + **tipificar** los factores de la brecha | Central (teórica) | **Paper 1 — revisión acotada a la brecha** | Taxonomía de la brecha + huecos |
| **WP2** | Diagnóstico | Cuantificar el **efecto observado** de cada factor en diseño controlado sobre testbeds | Central (empírica) | **Paper 2 — caracterización experimental** | Magnitud de cada efecto + protocolo realista derivado |
| **WP3** | Propuesta | Detector por ruptura de asociaciones condicionado al régimen + protocolo de WP2 | De trabajo | **Paper 3 — propuesta metodológica** | Robustez vs deriva vs baselines, sin oráculo de umbral; interpretabilidad emergente |
| **Hilo teórico transversal** | Teórico (punto 8) | Marco de condiciones de transferibilidad testbed→planta + **contexto operativo explícito (modelo de información + rol de la ontología para plantas heterogéneas)** | — | Sección de tesis o paper de posición ligero | Diferencia de una tesis puramente experimental |

**Decisiones de dimensionado:**
- WP1 = revisión propia ACOTADA a la brecha (no PRISMA exhaustiva). Usa revisiones
  existentes + aporta taxonomía propia. Publicable y rápida.
- 3 papers + marco teórico transversal ligero. No se compromete más.
- Orden WP1→WP2→WP3, con WP2 y WP3 **solapados** (el protocolo de WP2 alimenta WP3).
  Cronograma con barras solapadas.

**[v2] Panel de evaluación obligatorio (transversal a WP2-WP3):** reportar SIEMPRE
VUS-PR + affiliation + composite Fc1 + evaluación alarm-budget event-level. NUNCA usar
best-F1 sobre test como métrica principal. Incluir baselines triviales (detector
aleatorio, all-positive) como prueba de cordura (Garg et al.; Kim et al.).

**[v2] Contexto operativo explícito → vive en el HILO DE TRANSFERIBILIDAD** (decisión
tomada). Es el *cómo* de la transferencia (modelo de información estructura la telemetría;
ontología media entre plantas heterogéneas), NO un cuarto WP ni el corazón de la
contribución. La revisión halló respaldo DÉBIL/indirecto en agua para esta vía: es a la
vez hueco real y terreno poco asentado → tratarlo con prudencia, como aportación del hilo
teórico, no como pieza con grandes promesas.

---

## 5. Correcciones conceptuales (puntos 6, 15, 16, 17)

### Estado latente y variables (puntos 6, 16)
- Planta = sistema dinámico multivariante cuyo **estado operativo no se observa
  directamente**; la telemetría es **observación de ese estado latente**.
- **Exógenas** = externas a la planta (demanda, ambiente, consignas externas).
  **Endógenas** = internas a la dinámica del proceso. (NO actuador vs sensor.)
- Normalidad = **asociaciones estables entre variables** dado el contexto, no valores
  individuales. Anomalía = ruptura de asociaciones esperadas.

**Corrección frase punto 16:**
- ANTES: "su estado endógeno evoluciona de forma reproducible por diseño".
- DESPUÉS: bajo las mismas condiciones exógenas, mismo proceso y mismo contexto, las
  **asociaciones entre variables endógenas se mantienen**. Lo reproducible es la **lógica
  de relación**, no la trayectoria física completa.

### Información vs. decisión (punto 15)
- **Representación del contexto** = SÍ aporta información (estado inferido; alimenta el
  criterio de detección).
- **Operacionalización de la decisión** = NO aporta información observacional; aporta
  **reglas, restricciones, costes, utilidad** (gobierno de la alarma).

### Modelo de información vs. ontología (punto 17) — ROLES DISTINTOS
- **Modelo de información** = sustrato OPERATIVO (WP3). Estructura la telemetría, asocia
  variable→proceso/subsistema, define régimen. Ligero, fuera de línea. Ref: ISA-95/IEC 62264.
- **Ontología** = horizonte de TRANSFERENCIA/interoperabilidad (hilo teórico). Mecanismo
  para que el método no dependa de nomenclatura/tags de la planta concreta; mapear
  semántica SWaT ↔ planta real. Posible trabajo futuro. NO razonador en el lazo.
- No compiten: modelo info = "cómo lo implemento ahora"; ontología = "cómo se generaliza".
- **[v2]** Mantener esta sección breve y diferenciada; respaldo en agua DÉBIL → enmarcar
  como interoperabilidad, sin atribuirle capacidad de detección.

---

## 6. Alcance, dominio y rigor (puntos 5, 7, 10, 11, 12, 13)

### Dominio y especificidad (puntos 10, 12, 13)
- Dominio: **ICS de agua**, específicamente **telemetría y series temporales multivariantes
  de la capa OT** (proceso físico).
- NO "ICS" en sentido amplio (IT+OT, redes, protocolos, tráfico). Decir explícitamente:
  trabajamos con **las series temporales del proceso físico**, no con la capa IT ni con
  tráfico de red (punto 13).
- **PURGAR:** IIoT, manufactura, visión por computador, IA general (puntos 10, 12).

### Pila de Purdue (punto 11)
- Situar dónde operamos: **niveles 0-2** (proceso, control, supervisión). NO niveles IT
  superiores. Resuelve el 13 visualmente.

### Tono y rigor (puntos 5, 7, 18)
- Afirmaciones calibradas: "la literatura sugiere", "bajo el diseño considerado", "el
  efecto observado". NUNCA "contribución causal" → "**efecto observado sobre el rendimiento
  dentro del diseño experimental considerado**" (punto 18).
- Reforzar/reescribir toda afirmación débil/etérea (punto 5).
- Discurso centrado en el método riguroso, no en la denuncia (punto 7).

---

## 7. Ajuste de literatura (puntos 12, 17) **[v2 ampliado]**

- **Refs 69 (SSN/SOSA), 71, 72 (revisiones de ontologías):** sostienen el **hilo de
  transferibilidad** (no el detector).
- **Refs 70 (OntoCape — proceso químico), 73 (condition monitoring de activos):** fuera por
  dominio ajeno.
- Purgar literatura de visión/IA general/IIoT/manufactura.
- **[v2] Incorporar al corpus** (de la revisión): Kim et al. (AAAI 2022), Wu & Keogh (TKDE),
  Heydari & Nyarko (IEEE Access 2026), Lamberts et al. (SoK 2023), Han et al. (OWAD, NDSS
  2023), Cai et al. (SA², TII 2024), Fung et al. (NDSS 2024), Erba et al. (ACSAC 2020),
  Raman & Mathur / AICrit (JISA 2022). Verificar varios de 2025/preprints en IEEE Xplore/ACM
  antes de la versión final (SSAD, DEVS, Malarkkan).

---

## 8. Posicionamiento frente a trabajos solapados (NUEVO) **[v2]**

Tres trabajos cubren PIEZAS de lo que la tesis propone. La contribución debe posicionarse
en la INTEGRACIÓN, no en las piezas:

| Trabajo | Qué ya hace | Cómo se diferencia la tesis |
|---------|-------------|------------------------------|
| **Heydari & Nyarko 2026** (IEEE Access) | Evaluación alarm-budget event-level en SWaT/WADI | NO reclamar la evaluación realista como novedad; **construir sobre ella** como parte del panel |
| **Cai et al. SA² 2024** (IEEE TII) | Separa sensor/actuador en dependencia espaciotemporal | Diferenciarse por la **condicionalidad explícita al régimen** + adaptación a drift |
| **Han et al. OWAD 2023** (NDSS) | Detecta/explica/adapta normality shift | Diferenciarse por aplicación a **series OT de proceso de agua** (niveles 0-2 Purdue), no NIDS/logs |
| Umer / Raman / Mathur | Integran design+data-centric | Novedad en condicionalidad al régimen + protocolo de transferencia, no en la fusión |
| Koutroulis et al. 2023 | Detección causal-estructural en SWaT | Posicionar lo causal como extensión/exploración, no como primicia |

**Tesis = INTEGRACIÓN de:** (i) detección por asociaciones condicionada al régimen +
(ii) protocolo de transferencia inter-planta + (iii) evaluación deployment-realista,
aplicada específicamente a series OT de proceso de agua. El **contexto operativo explícito**
(modelo de información / ontología) es el hilo que conecta detección y transferencia, y es
donde el SOTA está más vacío (hueco real, respaldo débil → aportación del hilo teórico).

---

## 9. Huecos que la tesis puede llenar (de la revisión) **[v2]**
1. Protocolo canónico de transferencia SWaT→WADI→planta real con métricas
   deployment-realistas reportadas conjuntamente. **No existe hoy.**
2. Descomposición experimental: cuánto del rendimiento publicado se debe a artefactos de
   evaluación vs. capacidad real bajo régimen cambiante (separar efecto PA/oráculo del
   efecto drift).
3. Arquitectura régimen-condicionada unificada (invariantes + estado latente + adaptación a
   normality shift) evaluada en series OT de proceso de agua.
4. Distinción operativa proxy vs causa: validación de atribución a nivel de ventana de
   ataque en datasets de agua, extendiendo Fung et al. (2024).

---

## 10. Umbral de decisión que cambia el rumbo (de la revisión) **[v2]**
Si al re-evaluar el método propio con métricas deployment-realistas la mejora sobre
baselines triviales desaparece o no se sostiene tras un cambio de régimen/dataset →
reorientar hacia robustez ante drift y transferibilidad, en lugar de exactitud puntual.
Recíprocamente, si la ventaja persiste bajo presupuesto de alarmas y transferencia, ese es
el resultado publicable central.

---

## Estado de los 21 puntos

| # | Punto | Estado |
|---|-------|--------|
| 1 | Hipótesis excluyentes | ✔ resuelto |
| 2 | Contribución medible | ✔ resuelto + respaldo gap |
| 3 | Contradicción testbed/planta | ✔ resuelto + gap confirmado |
| 4 | Contradicciones en el resumen | ⏳ pendiente de redacción |
| 5 | Afirmaciones débiles/etéreas | ✔ criterio + respaldo citable |
| 6 | Endógeno/exógeno, estado latente | ✔ resuelto |
| 7 | Approach científico riguroso | ✔ criterio fijado |
| 8 | Contribución teórica | ✔ resuelto (hilo + contexto explícito) |
| 9 | Explicar vs proxy | ✔ resuelto + reforzado (Fung 2024) |
| 10 | No confundir ICS/IIoT/manufactura | ✔ criterio fijado |
| 11 | Pila de Purdue | ✔ resuelto (niveles 0-2) |
| 12 | No mezclar literatura ajena | ✔ criterio + corpus depurado |
| 13 | ICS = IT+OT o solo OT | ✔ resuelto (solo OT, series del proceso) |
| 14 | Objeto real = robustez + brecha | ✔ resuelto |
| 15 | Información vs reglas/decisión | ✔ resuelto |
| 16 | "reproducible por diseño" | ✔ resuelto (asociaciones, no trayectoria) |
| 17 | Ontología vs modelo de información | ✔ resuelto (roles distintos) |
| 18 | Causalidad → efecto observado | ✔ resuelto |
| 19 | Work packages | ✔ resuelto + panel de métricas |
| 20 | Pregunta raíz | ✔ resuelto (explicativa) |
| 21 | Hipótesis central | ✔ resuelto (central + trabajo + respaldo) |

Todo lo estructural cerrado y respaldado. Queda **redactar** (punto 4 y aplicación de 5/7
a todo el texto), con las referencias de §3 y §8 ya disponibles para citar.
