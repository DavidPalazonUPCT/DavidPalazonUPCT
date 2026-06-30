# INFORME CONSOLIDADO — Entrada de la FASE 2 (redacción)

> Fusión de V1–V5 + mandatos estructurales del acta v2, ordenado por **sección del plan v37**.
> Para cada sección: (A) **mandato estructural** (acta, decidido) · (B) **calibración/terminología/refs** (V1–V5).
> Resueltos los solapamientos: cada hallazgo aparece UNA vez en su sección de aplicación primaria.
> Leyenda de fuentes: V1=afirmaciones débiles · V2=fuera de dominio · V3=referencias · V4=resumen · V5=terminología.

---

## REGLAS TRANSVERSALES (aplican a TODO el texto)

- **R1 · Registro causal (V1 C1; V5 nota 7; acta p.18).** Erradicar "contribución marginal", "aislar el efecto", "atribuir a su origen". Fórmula única: **"el efecto observado sobre el rendimiento dentro del diseño experimental considerado, condicional al pipeline fijado"**. Plantilla de oro ya presente en el plan: P109.
- **R2 · Umbral con oráculo (V5 Cat 1; V1 H08; acta §0.1).** Término único: **"selección de umbral con oráculo sobre el conjunto de prueba"** (glosar *best-F1 / oracle thresholding* SOLO la 1.ª vez). Prohibidos como sujeto/nombre del fenómeno: "filtración de datos de prueba", "filtración del umbral", "umbral óptimo a posteriori", "best-F1", "data leakage", "fuga/sin la verdad de referencia". Mantener "ajuste por puntos / *point adjustment*" como concepto **separado**.
- **R3 · "Insesgado" → "que controla los sesgos documentados" (V1 H08/C3).** Ningún protocolo es insesgado. Sustituir en TODAS las apariciones (P046, P101, P114, P116, P134).
- **R4 · Asociaciones estables (V5 Cat 3; V1 H03/H17; V4; acta p.16).** Erradicar "reproducible por diseño" y "casi determinista". Fórmula: bajo las mismas condiciones exógenas, mismo proceso y mismo régimen, **las asociaciones entre variables endógenas se mantienen**; lo reproducible es la **lógica de relación**, no la trayectoria. "regularidad de baja entropía" → "estabilidad de las asociaciones".
- **R5 · Endógeno/exógeno (V5 Cat 2; acta p.6).** Exógeno = **externo a la planta** (demanda, ambiente, consignas externas). Endógeno = **interno a la dinámica del proceso** (estado y relaciones; los actuadores son parte del lazo endógeno). NUNCA actuador/sensor como definición. Evitar "exógeno = no controlado". Sensor/actuador permitido solo como *tipo de señal*/*superficie de ataque* (P075, P088, P101).
- **R6 · Tono no-denuncia (V1 H16/H19/H23/H24; acta p.7).** "denuncia/reclama/el campo descuida/prioriza" → "documenta / señala / ha recibido menos atención que". Discurso de método, no de denuncia.
- **R7 · Planta real = PoC, no métricas (V1 C7/H06/H14/H34; V4; acta §1, delimitación).** Todo verbo de utilidad operativa/transferencia a planta real → condicional + "orientación", reservando validación naturalista a trabajo futuro.
- **R8 · Alcance OT-series + Purdue 0-2 (V2; acta p.11/13).** Insertar explícito en Resumen, Objetivos, Intro 3.1/3.2, marco WP0. Declarar: objeto = **series temporales multivariantes de la capa OT (proceso físico), niveles 0-2 de Purdue**; NO capa IT, NO tráfico de red, NO protocolos.
- **R9 · Proxy ≠ causa (V1 C5/H25; acta p.9 + Fung 2024).** La explicación describe **qué** asociación se rompió (proxy), no **por qué** (causa). Sin causalidad como afirmación.

---

## 0. TÍTULO
- **(A)** Infinitivo, centrado en la **brecha** banco→despliegue (acta §1/§2). NO "Contribuciones a la detección de anomalías" (V4: el título actual enuncia lo que el acta descarta como objeto). Ver Q2.
- Propuesta de trabajo: *"Caracterizar y reducir la brecha entre el rendimiento en banco de pruebas y el despliegue operativo de la detección de anomalías en sistemas de control industrial de agua: un estudio sobre series temporales OT"*.

## 1. RESUMEN
- **(A1)** Objeto = la brecha; testbeds = objeto de estudio; planta real = evidencia/PoC (acta §1; A1–A3). 
- **(A2)** Reemplazar "tres hipótesis competidoras H0/H1/H2" (P037) por **central (explicativa) + trabajo (mecanismo) + interpretabilidad consecuencia + delimitación** (B1/B3/B4/B5).
- **(A3)** Integración (J2): detección por asociaciones condicionada al régimen + protocolo de transferencia + evaluación deployment-realista, en series OT de agua.
- **(B) V4:** resolver contradicciones P036–P040. **V1:** H01 (observación "contrastada"→fragmentada, citar Erba/Fung 2022/Lamberts), H04 ("simuladas"→testbeds etiquetados), H05 ("ampliamente aceptada"→citar Zamanzadeh/Alves), H06 ("acercar a la operación"→caracterizar la brecha). **V5:** R4 en P038, R5 en P038, Cat 5 en P037 (operacionalización = gobierno de la alarma, no "información"). **V2:** R8 (acotar "ICS…o CPS" → series OT agua, Purdue 0-2).

## 2. PALABRAS CLAVE (P040)
- **(B)** Alinear con dominio OT-agua + brecha. Añadir "series temporales OT", "niveles 0-2 de Purdue", "evaluación deployment-realista", "deriva/normality shift", "transferibilidad testbed-planta". Retirar "despliegue en hardware de borde" si se demota (Q1). Sin IIoT.

## 3. OBJETIVOS
- **(A)** Objetivo general ≈ título en infinitivo (brecha). Específicos = **WP0–WP3 operacionalizados** (C1–C4):
  - OE0/WP0 marco conceptual; OE1/WP1 revisión acotada + tipificar factores (Paper 1); OE2/WP2 cuantificar efecto observado de cada factor (Paper 2); OE3/WP3 detector por ruptura de asociaciones condicionado al régimen + protocolo (Paper 3); hilo teórico = transferibilidad + contexto operativo.
- **(B) V2:** ELIMINAR encuadre IIoT (P043); insertar encuadre OT-series/Purdue (R8). **V1:** H07 (R1), H08 (R3), H09 (efecto puede ser nulo, no se rechaza H0), H10 (transferibilidad "se discute", no "lograda"). Retirar objetivo 5 (borde) o demotarlo (Q1). **V5 Cat 5** en P047.

## 4. HIPÓTESIS  *(reemplaza P051–P056 completas)*
- **(A) Volcado EXACTO del acta §3 (B1–B8):**
  - **Central (explicativa, tesis):** brecha = efecto de factores identificables: (a) metodológicos [selección de umbral con oráculo + ajuste por puntos]; (b) del sistema [no estacionariedad + dependencia del régimen]. Efecto de cada factor aislable/estimable en diseño controlado. "Efecto observado", nunca causal; no se cae nunca; promete demostrar y medir.
  - **Trabajo (mecanismo, paper):** estado latente → asociaciones estables; (a) contexto = condicionar al régimen; (b) mecanismo = ruptura de asociaciones más robusta frente a deriva que valor individual o puntuación agregada umbralizada globalmente.
  - **Interpretabilidad = consecuencia** (no hipótesis): identifica qué asociación y en qué régimen se rompió; describe el evento, sin causa (R9 + Fung 2024, B8).
  - **Delimitación explícita (lo NO afirmado):** no reducir la brecha en planta real concreta; datos de planta = PoC; operacionalización = gobierno de la alarma ≠ información (E5/V5 Cat 5).
  - **Dos planos (B6):** central→WP1-WP2 (diagnóstico); trabajo→WP3 (propuesta). **Excluyentes en lo que afirman (B7).**
- **(B) V1:** H11 (P051 "fracción sustancial"→sin cuantificador, hipótesis falsable), H12 (corroboración = efecto observado significativo). R1 en todo.

## 5. INTRODUCCIÓN / ESTADO DEL TEMA (3.1–3.7)
- **3.1 Justificación (P059–P069):**
  - **V2:** R8 — cerrar P060/P072 con acotación OT-series/Purdue; insertar Purdue. **V1:** H13 (P061 "primer intento masivo"→"uno de los primeros"), H14 (P063 cumplimiento NIS2→"vuelve exigible"), H15 (P065 hueco con prudencia). **V5:** R2 en P065 (×4), R4+R5 en P067, Cat 4 en P066 (modelo info vs ontología). **V1 H18** (P067 "baja entropía"→estabilidad asociaciones). Reescribir P067/P068 como sustrato (estado latente, asociaciones, endógeno/exógeno) = base de WP0 (C1, E1–E4).
- **3.2 Infraestructuras hídricas y ciberseguridad (P070–P073):** **V2:** P071 = ancla principal de Purdue 0-2; declarar objeto = series del proceso físico, NO IT/tráfico/protocolos (R8). 
- **3.3 Técnicas de IA (P074–P082):** **V3:** insertar CAVEAT techo de invariantes — AICrit cero FP pero 24/36 (Raman & Mathur, 2022b/AICrit), desambiguar 2022a(TSMC)/2022b(AICrit) en P076/P089/P115/P207 (I1/I3). **V1 H22** (P089 "fuerte localidad"/"competitivas"→calibrar). 
- **3.4 Evaluación rigurosa (P083–P085):** **V5:** R2 en P084 (×2), P113. **V1:** H19 (P084 "denuncia"→documenta, R6), H20 ("hoy consolidada"→"cada vez más aceptada"; Lamberts ~1,3 datasets/paper), H21 (P085 "interés de revistas"→citar marcos). **(A) D1:** panel obligatorio VUS-PR + affiliation + composite Fc1 + alarm-budget; baselines triviales (D3). Posicionar el panel **sobre** Heydari & Nyarko (V1 C3, acta §8).
- **3.5 Deriva, contexto, robustez (P086–P090):** **V3:** P090 — declarar que normality shift proviene de NIDS/logs (Han 2023), trasladable pero a verificar, no demostrado en agua (I2). **V5:** Cat 4 (modelo info). **V1 H25** (P093 nexo causal→proxy, R9).
- **3.6 Explicabilidad (P091–P093):** **(A) B4:** interpretabilidad = consecuencia; Fung 2024 (B8/R9). **V1:** H23 (P092 "el campo descuida"→R6), H24 ("requisito de diseño"→atenuar). **V2:** P093 ShaTS a contraste (no "en el IIoT"); LLM = una frase de cierre/trabajo futuro (Q3).
- **3.7 Estructuración del contexto y despliegue (P094–P096):** **(A) E6/E7/E8:** separar **modelo de información** (operativo, WP3, ISA-95, fuera de línea, no razonador) de **ontología** (transferencia/interoperabilidad, hilo teórico, SSN/SOSA, trabajo futuro, sin capacidad de detección). **V5 Cat 4** (P095 colapsa roles). **V2/V3:** purgar OntoCape (Marquardt P199) y Hendriks (P177); reducir SAREF/DEXPI/BFO a contraste; mantener SSN/SOSA, Karabulut, Jarwar solo como soporte del hilo (H1/H2). **Borde/TinyML (P096):** demotar a consecuencia operativa/trabajo futuro (Q1); retirar Antonini/HGNAS del corpus central.

## 6. METODOLOGÍA (4.1–4.2)
- **(A)** Marco DSR (conservar, está bien: P099–P101 con calibración). Diseño **cuasi-experimental** (P113). **Variables (tabla):** independientes = factores del acta (oráculo, point adjustment, no estacionariedad, régimen) + activación de representación del contexto / operacionalización; dependientes = panel de métricas (D1). Endógeno/exógeno correctos (R5). Control, confusoras (oráculo, PA, normalización, solape), muestreo por conveniencia reconocido. **Panel obligatorio (D1/D2/D3).** Reproducibilidad. Sesgos/amenazas a la validez (conservar P117, calibrado).
- **(B) V1:** H26 (P100 "generan conocimiento"→"se espera derivar"), H27 (P101 R3+"primera clase"), H28/H29 (P109 unificar registro R1), H30 (P112 "garantiza reproducibilidad total"→"favorece"), H31 (P114 R3 + errata "la eje"→"el eje"), H32 ("precede a cualquier"→"a las afirmaciones de este trabajo"). **V5:** R2 (P114, P117), R5. **(A) K2:** umbral de decisión (§10) explícito.

## 7. WORK PACKAGES Y PLAN (reemplaza 4.3; conserva 4.4 cronograma + 4.5)
- **(A) C1–C9:** WP0 (marco) + WP1 (revisión acotada, Paper 1) + WP2 (cuantificación, Paper 2) + WP3 (detector + protocolo, Paper 3) + **hilo teórico transversal** (transferibilidad + contexto operativo: modelo info + ontología). Orden WP1→WP2→WP3 con **WP2/WP3 solapados** (C8). 3 papers + marco ligero (C7). Responsables: doctorando + directores + GRITA/TrueData.
- **Cronograma (4.4, P128–P131 + TABLA):** actualizar etiquetas de filas a WP0–WP3 + hilo; barras solapadas WP2/WP3 (C8). 
- **4.5 Instalaciones (P132–P136):** conservar; retirar/atenuar hardware de borde si se demota (Q1); conservar GPU, datasets SWaT/WADI, software, ThingsBoard/Zotero.

## 8. POSICIONAMIENTO / SOTA  *(sección nueva — acta §8)*
- **(A) J1/J2/J3:** tabla — Heydari & Nyarko (construir sobre alarm-budget, no reclamar novedad); Cai/SA² (diferenciarse por condicionalidad explícita al régimen + drift); Han/OWAD (aplicación a series OT de agua, no NIDS/logs); Umer/Raman/Mathur (novedad en condicionalidad + protocolo, no en la fusión); Koutroulis (causal = extensión, no primicia). Tesis = INTEGRACIÓN, no las piezas. Contexto operativo explícito = hilo que conecta detección y transferencia, donde el SOTA está más vacío.

## 9. APLICABILIDAD / INTERÉS (reescribe 5, P138–P143)
- **(A)** Quién se beneficia (operadores hídricos, reguladores), cómo, plazo; encaje EECTI/transición digital/infraestructura crítica. Sin sobreventa.
- **(B) V1:** H34 (P139 "accionable/reutilizable"→orientación+hipótesis, R7), H35 (R1), H36 (P140 "validados"→"busca validar"), H37 (P141 "robusto al resultado"→interés metodológico + umbral §10/K2), H38 (P142 "intereses de revistas"→encaje temático), H33 (P133 Dong "obstáculos centrales"→calibrar; dominio limítrofe).

## 10. BIBLIOGRAFÍA (actualiza 6)
- **(A/B) V3 — acciones concretas:**
  - **AÑADIR (APA listo en V3):** Erba et al. ACSAC 2020; Raman & Mathur/AICrit JISA 2022 (=2022b); Fung et al. ESORICS 2022.
  - **CORREGIR metadatos:** Adepu & Mathur → **2021, 18(1):86-99** (P145; afecta citas P076/P115); M2AD autores → Alnegheimish, He, Reimherr, Chandrayan, Pradhan, D'Angelo (AISTATS 2025, PMLR 258:4384-4392) (P146); MLAD → completar Sensors 2025, 25(13):4115 (P190); Koutroulis → **2023** (P187/P080); Wu & Keogh → completar 35(3):2421-2429 (P223, año 2023).
  - **DESAMBIGUAR:** Raman & Mathur 2022a (TSMC, P207) vs 2022b (AICrit/JISA) en texto y bibliografía.
  - **PURGAR:** Marquardt/OntoCape (P199), Hendriks (P177) — solo citadas en P095; reescribir P095 local.
  - **[VERIFICAR MANUALMENTE]** (existen; páginas/DOI/issue no confirmables por bloqueo 403): SSAD/Wei MSN 2024 (P222), Barakat/DEVS SMARTCOMP 2025 (P151), Cai/SA² TII 2024 issue+DOI (P154), Erba páginas ACM, Fung ESORICS páginas LNCS, Alves iniciales 1er autor (P147). 
  - **Discrepancia a resolver:** Umer IJCIP 100356 (P218) vs acta 100341.
- **(B) Formato:** APA 7ª, orden alfabético, sangría francesa (left=567 hanging=567, 10pt). Toda cita en texto ↔ bib.

---

## PREGUNTAS PENDIENTES detectadas (→ PREGUNTAS_PENDIENTES.md)
- Q1 (borde/TinyML, confirmado por V2): demotar/retirar.
- Q2 (título exacto).
- Q3 (LLM como capa explicación: una frase o eliminar — V2 nuevo).
- Q4 (gemelos digitales vía Karabulut: acotar — V2 nuevo).
- Q5 (encuadre "Multimedia" + IIoT: IIoT fuera; Multimedia se conserva salvo indicación).
- Nuevo: Umer IJCIP 100356 vs 100341 (verificar manual).
