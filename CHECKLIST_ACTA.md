# CHECKLIST_ACTA.md — Criterio de "hecho" para la reescritura v36 → v37

> Cada decisión del acta v2 con: **id** · qué exige · sección(es) del plan afectada(s) · estado.
> Estado se marca en FASE 3. Ref. acta entre paréntesis.

## A. Giro de fondo del objeto (acta §1, §2; puntos 2,3,14,20)

| id | Qué exige | Afecta | Estado |
|----|-----------|--------|--------|
| A1 | Objeto = estudio de **por qué los detectores que rinden en banco fracasan al desplegarse** y qué reduce la brecha. NO "contribuir a la detección de anomalías en ICS hídricos". | Título, Resumen, Objetivos, Intro, Interés | ⏳ |
| A2 | Testbeds (SWaT, WADI, BATADAL, HAI) = **objeto de estudio crítico**, no campo de aplicación. | Resumen, Metodología, Diseño exp. | ⏳ |
| A3 | Datos de planta sin etiquetar = **evidencia descriptiva / PoC / trabajo futuro**, NO métricas de detección. | Resumen, Metodología, Delimitación, Aplicabilidad | ⏳ |
| A4 | Contribución medible = caída de rendimiento entre condiciones, efecto de cada factor dentro del diseño, degradación bajo deriva. | Objetivos, Interés | ⏳ |
| A5 | Pregunta raíz **explicativa** (verbatim acta §2): "¿Por qué… fracasan… y cómo puede reducirse esa brecha?". Robustez/interpretabilidad/transferencia = ejes, NO la pregunta. | Resumen, Objetivos, Intro | ⏳ |
| A6 | Gap confirmado: NO existe protocolo canónico SWaT→WADI→planta real con métricas deployment-realistas. Justifica WP1/WP2. | Intro, Huecos, WP | ⏳ |

## B. Núcleo de hipótesis (acta §3; puntos 1,21)

| id | Qué exige | Afecta | Estado |
|----|-----------|--------|--------|
| B1 | **Hipótesis central (explicativa, nivel tesis)** verbatim acta §3: la brecha = efecto de factores identificables: (a) metodológicos de evaluación [selección de umbral con oráculo sobre test + ajuste por puntos]; (b) propios del sistema [no estacionariedad + dependencia del régimen]. El efecto de cada factor puede aislarse y estimarse en diseño controlado. | Hipótesis, Objetivos, Metodología | ⏳ |
| B2 | Central: "efecto observado dentro de un diseño controlado", NUNCA "contribución causal". No promete resolver; promete demostrar y medir. No se cae nunca. | Hipótesis, Metodología, tono global | ⏳ |
| B3 | **Hipótesis de trabajo (mecanismo, nivel paper)** verbatim acta §3: estado operativo latente → asociaciones estables. (a) Contexto: asociaciones dependen del régimen; normalidad condicionada al régimen, no global. (b) Mecanismo: bajo mismas exógenas y régimen, evolución de endógenas preserva asociaciones; su ruptura = indicador más robusto frente a deriva que el valor individual o una puntuación agregada umbralizada globalmente. | Hipótesis, Metodología, WP3 | ⏳ |
| B4 | **Interpretabilidad = consecuencia, NO hipótesis**: si detecta por ruptura de asociaciones condicionada al régimen, la alarma identifica qué asociación y en qué régimen se rompió. Describe el evento, sin afirmación causal sobre origen físico. | Hipótesis, Intro 3.6, WP3 | ⏳ |
| B5 | **Delimitación explícita (lo NO afirmado)**: no se afirma reducir la brecha en una planta real concreta; datos de planta sin verdad de referencia → no métricas (PoC/futuro). Operacionalización de la decisión (reglas, costes, utilidad) ≠ información observacional = gobierno de la alarma; se distingue de la representación del contexto (estado inferido). | Resumen, Hipótesis, Metodología | ⏳ |
| B6 | **Dos planos**: Central → WP1-WP2 (diagnóstico); Trabajo → WP3 (propuesta). Visualmente separados diagnóstico vs solución. | Hipótesis, WP | ⏳ |
| B7 | Hipótesis **excluyentes en lo que afirman**: caracterizar (central) ≠ contexto/mecanismo (trabajo). Cada una puede ser cierta o falsa sin que las otras la determinen. | Hipótesis | ⏳ |
| B8 | Refuerzo punto 9 (explicar ≠ explicar un proxy) con **Fung et al. NDSS 2024**: la atribución de features falla con actuadores categóricos → cautela; explicar qué asociación se rompió, no por qué. Sin introducir causalidad como afirmación. | Hipótesis B4, Intro 3.6, Huecos | ⏳ |

## C. Work packages (acta §4; punto 19)

| id | Qué exige | Afecta | Estado |
|----|-----------|--------|--------|
| C1 | **WP0** transversal: marco conceptual (estado latente, asociaciones, endógeno/exógeno, modelo info vs ontología, alcance OT/series, Purdue). Salida: plan + marco teórico. | Objetivos, WP, Intro | ⏳ |
| C2 | **WP1** diagnóstico (hipótesis central teórica): revisión acotada del SOTA + **tipificar** factores de la brecha. Salida: **Paper 1 — revisión acotada**. Cierre: taxonomía de la brecha + huecos. | Objetivos, WP | ⏳ |
| C3 | **WP2** diagnóstico (central empírica): cuantificar el **efecto observado** de cada factor en diseño controlado sobre testbeds. Salida: **Paper 2 — caracterización experimental**. Cierre: magnitud de cada efecto + protocolo realista derivado. | Objetivos, WP, Metodología | ⏳ |
| C4 | **WP3** propuesta (de trabajo): detector por ruptura de asociaciones condicionado al régimen + protocolo de WP2. Salida: **Paper 3 — propuesta metodológica**. Cierre: robustez vs deriva vs baselines, **sin oráculo de umbral**; interpretabilidad emergente. | Objetivos, WP, Metodología | ⏳ |
| C5 | **Hilo teórico transversal**: condiciones de transferibilidad testbed→planta + **contexto operativo explícito (modelo de información + rol de la ontología para plantas heterogéneas)**. Salida: sección de tesis / paper de posición ligero. | WP, Posicionamiento | ⏳ |
| C6 | WP1 = revisión propia **ACOTADA** a la brecha (no PRISMA exhaustiva); usa revisiones existentes + taxonomía propia. | WP1, Metodología | ⏳ |
| C7 | 3 papers + marco teórico transversal ligero. No comprometer más. | WP, Cronograma | ⏳ |
| C8 | Orden WP1→WP2→WP3 con **WP2 y WP3 solapados** (protocolo de WP2 alimenta WP3). Cronograma con barras solapadas. | WP, Cronograma | ⏳ |
| C9 | Contexto operativo explícito **vive en el hilo de transferibilidad**, NO es un 4º WP ni el corazón. Respaldo DÉBIL/indirecto en agua → prudencia, sin grandes promesas. | WP, Posicionamiento, 3.7 | ⏳ |

## D. Panel de evaluación obligatorio (acta §4 [v2])

| id | Qué exige | Afecta | Estado |
|----|-----------|--------|--------|
| D1 | Reportar SIEMPRE: **VUS-PR + affiliation + composite Fc1 + evaluación alarm-budget event-level**. | Metodología 4.2, WP2/WP3 | ⏳ |
| D2 | **NUNCA** usar best-F1 sobre test como métrica principal (= selección de umbral con oráculo). | Metodología, tono | ⏳ |
| D3 | Incluir **baselines triviales** (detector aleatorio, all-positive) como prueba de cordura (Garg; Kim). | Metodología, WP2 | ⏳ |
| D4 | Composite Fc1 = Garg et al. TNNLS 2021. VUS-PR = Paparrizos VLDB 2022. Affiliation = Huet KDD 2022. Alarm-budget = Heydari & Nyarko 2026. | Metodología, Bibliografía | ⏳ |

## E. Correcciones conceptuales (acta §5; puntos 6,15,16,17)

| id | Qué exige | Afecta | Estado |
|----|-----------|--------|--------|
| E1 | Planta = sistema dinámico multivariante con **estado operativo no observado directamente**; telemetría = observación del estado latente. | Resumen, Intro 3.1/3.3 | ⏳ |
| E2 | **Exógenas** = externas a la planta (demanda, ambiente, consignas externas). **Endógenas** = internas a la dinámica del proceso. **NO actuador vs sensor.** | Resumen, Intro, Metodología (tabla variables) | ⏳ |
| E3 | Normalidad = **asociaciones estables entre variables** dado el contexto, no valores individuales. Anomalía = ruptura de asociaciones esperadas. | Resumen, Intro, Hipótesis | ⏳ |
| E4 | **Corrección frase punto 16**: ANTES "su estado endógeno evoluciona de forma reproducible por diseño" → DESPUÉS "bajo mismas condiciones exógenas, mismo proceso y mismo contexto, las **asociaciones entre variables endógenas se mantienen**; lo reproducible es la **lógica de relación**, no la trayectoria física completa". | Resumen (P038), Intro (P067) | ⏳ |
| E5 | **Información vs decisión (punto 15)**: representación del contexto = SÍ información (estado inferido, alimenta el criterio); operacionalización de la decisión = NO información observacional, sino reglas/restricciones/costes/utilidad (gobierno de la alarma). | Hipótesis B5, Metodología | ⏳ |
| E6 | **Modelo de información** = sustrato OPERATIVO (WP3): estructura telemetría, variable→proceso/subsistema, define régimen. Ligero, fuera de línea. ISA-95/IEC 62264. | WP3, 3.7, Metodología | ⏳ |
| E7 | **Ontología** = horizonte de TRANSFERENCIA/interoperabilidad (hilo teórico): independencia de nomenclatura/tags; mapear semántica SWaT↔planta real; posible futuro. NO razonador en el lazo. | Hilo teórico, 3.7, Posicionamiento | ⏳ |
| E8 | Modelo info y ontología NO compiten: info = "cómo lo implemento ahora"; ontología = "cómo se generaliza". Sección breve, diferenciada; respaldo en agua DÉBIL → enmarcar como interoperabilidad, sin capacidad de detección. | 3.7, hilo teórico | ⏳ |

## F. Alcance, dominio y rigor (acta §6; puntos 5,7,10,11,12,13,18)

| id | Qué exige | Afecta | Estado |
|----|-----------|--------|--------|
| F1 | Dominio = **ICS de agua**, específicamente **telemetría y series temporales multivariantes de la capa OT (proceso físico)**. | Título, Resumen, Palabras clave, Intro | ⏳ |
| F2 | NO "ICS" amplio (IT+OT, redes, protocolos, tráfico). Decir explícito: trabajamos con **series temporales del proceso físico**, no capa IT ni tráfico de red (punto 13). | Resumen, Intro 3.2/3.3, Metodología | ⏳ |
| F3 | **PURGAR**: IIoT, manufactura, visión por computador, IA general (puntos 10,12). | Objetivos (P043 IIoT), Intro, Palabras clave, Bibliografía | ⏳ |
| F4 | **Purdue niveles 0-2** (proceso, control, supervisión). NO niveles IT superiores. | Intro 3.2, Metodología, Resumen | ⏳ |
| F5 | Afirmaciones calibradas: "la literatura sugiere", "bajo el diseño considerado", "el efecto observado". | Todo el texto | ⏳ |
| F6 | "contribución causal" → "**efecto observado sobre el rendimiento dentro del diseño experimental considerado**" (punto 18). | Hipótesis, Metodología, Interés | ⏳ |
| F7 | Reforzar/reescribir toda afirmación débil/etérea (punto 5, V1). | Todo el texto | ⏳ |
| F8 | Discurso centrado en el **método riguroso**, no en la denuncia (punto 7). | Intro 3.4, Interés | ⏳ |

## G. Terminología corregida (acta §0.1 [v2]; V5)

| id | Qué exige | Afecta | Estado |
|----|-----------|--------|--------|
| G1 | "fuga de la verdad de referencia / threshold leakage / filtración de datos de prueba / best-F1" → **"selección de umbral con oráculo sobre el conjunto de prueba"** (*best-F1 / oracle thresholding*). Aplicar en TODO el plan. (Kim 2022; Lamberts 2023). | Intro 3.4 (P065,P084), Metodología (P114,P117), Objetivos | ⏳ |
| G2 | Usar "asociaciones estables" (no "evolución reproducible por diseño"). | Resumen, Intro, Hipótesis | ⏳ |

## H. Ajuste de literatura y referencias nuevas (acta §7; V3)

| id | Qué exige | Afecta | Estado |
|----|-----------|--------|--------|
| H1 | Refs SSN/SOSA (Haller), revisiones de ontologías (Karabulut, Jarwar) → sostienen **hilo de transferibilidad**, no el detector. | 3.7, hilo teórico | ⏳ |
| H2 | OntoCape (Marquardt — proceso químico) y condition monitoring de activos (Hendriks) → **fuera por dominio ajeno**. | 3.7, Bibliografía | ⏳ |
| H3 | Purgar literatura de visión/IA general/IIoT/manufactura del corpus. | Bibliografía, Intro | ⏳ |
| H4 | **Incorporar al corpus** (ya en v36 la mayoría): Kim 2022✓, Wu&Keogh✓, Heydari&Nyarko 2026✓, Lamberts 2023✓, Han OWAD 2023✓, Cai SA² 2024✓, Fung NDSS 2024✓. **NUEVAS a añadir**: Erba et al. ACSAC 2020; Raman & Mathur/AICrit JISA 2022; Fung et al. ESORICS 2022. | Bibliografía, Intro, Hipótesis | ⏳ |
| H5 | Verificar en IEEE Xplore/ACM antes de versión final: **SSAD (Wei et al. 2024), DEVS (Barakat 2025), Malarkkan 2025**. Marcar no confirmables como **[VERIFICAR MANUALMENTE]**. | Bibliografía | ⏳ |

## I. Correcciones factuales (acta §0.5; V3)

| id | Qué exige | Afecta | Estado |
|----|-----------|--------|--------|
| I1 | "24/36 ataques, cero FP" = **AICrit (Raman & Mathur, JISA 2022)**, NO Koutroulis. (Koutroulis: F1≈0,941, cero FP, 4 ataques no detectados que tampoco cumplían su objetivo físico). | Intro 3.3/3.5, Hipótesis (caveat invariantes) | ⏳ |
| I2 | Concept drift / normality shift proviene mayormente de **NIDS/logs SCADA**: trasladable a OT de proceso, pero declararlo explícitamente, no como demostrado en agua. | Intro 3.5, Hipótesis, Posicionamiento | ⏳ |
| I3 | CAVEAT techo de invariantes frente a ataques sigilosos: AICrit cero FP pero 24/36 en SWaT. Reconocerlo. | Intro 3.3, Hipótesis (caveat) | ⏳ |

## J. Posicionamiento frente a solapamientos (acta §8 NUEVO)

| id | Qué exige | Afecta | Estado |
|----|-----------|--------|--------|
| J1 | Tabla de posicionamiento: Heydari&Nyarko (alarm-budget → construir sobre ella, no reclamar novedad); Cai/SA² (diferenciarse por condicionalidad explícita al régimen + drift); Han/OWAD (diferenciarse por aplicación a series OT de agua, no NIDS/logs); Umer/Raman/Mathur (novedad en condicionalidad + protocolo de transferencia, no en la fusión); Koutroulis (lo causal = extensión/exploración, no primicia). | Posicionamiento (sección nueva) | ⏳ |
| J2 | Tesis = **INTEGRACIÓN** de (i) detección por asociaciones condicionada al régimen + (ii) protocolo de transferencia inter-planta + (iii) evaluación deployment-realista, aplicada a series OT de agua. NO las piezas. | Resumen, Posicionamiento, Interés | ⏳ |
| J3 | Contexto operativo explícito (modelo info/ontología) = hilo que conecta detección y transferencia; donde el SOTA está más vacío (hueco real, respaldo débil → aportación del hilo teórico). | Posicionamiento, hilo teórico | ⏳ |

## K. Huecos y umbral de decisión (acta §9, §10)

| id | Qué exige | Afecta | Estado |
|----|-----------|--------|--------|
| K1 | Huecos: (1) protocolo canónico transferencia con métricas deployment-realistas; (2) descomposición experimental PA/oráculo vs deriva; (3) arquitectura régimen-condicionada en series OT de agua; (4) distinción proxy vs causa a nivel de ventana de ataque (extendiendo Fung 2024). | Intro, Huecos, WP, Interés | ⏳ |
| K2 | Umbral de decisión que cambia el rumbo: si con métricas deployment-realistas la mejora sobre baselines triviales desaparece tras cambio de régimen/dataset → reorientar a robustez ante drift y transferibilidad. Recíprocamente, si persiste bajo presupuesto de alarmas y transferencia = resultado publicable central. | Metodología, Interés | ⏳ |

## L. Formato y entregable (FASE 4)

| id | Qué exige | Afecta | Estado |
|----|-----------|--------|--------|
| L1 | Partir de Plan_Investigacion_v36_APA7.docx; preservar estilos, portada, encabezados, numeración, formato APA, sangría francesa. NO docx desde cero. | docx | ⏳ |
| L2 | Bibliografía APA 7ª, orden alfabético, sangría francesa; toda cita en texto existe en bib y viceversa. | Bibliografía, QC | ⏳ |
| L3 | Validar docx (paquete bien formado, sin duplicados, sin huérfanos); convertir a PDF y revisar visualmente. | docx | ⏳ |
| L4 | Entregar Plan_Investigacion_v37.docx + RESUMEN_CAMBIOS_v36_a_v37.md + lista [VERIFICAR MANUALMENTE] + PREGUNTAS_PENDIENTES.md. | Entregable | ⏳ |
