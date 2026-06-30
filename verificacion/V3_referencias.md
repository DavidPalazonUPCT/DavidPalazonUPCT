# V3 — Verificación de referencias (rigor bibliográfico)

> Subagente V3. Tarea READ-ONLY sobre `trabajo/plan_actual.md`. No se ha editado el plan.
> Fuente de verdad: `insumos/Acta_Decisiones_v2_Reestructuracion_Plan.md`.
> Fecha: 2026-06-30. Verificación con WebSearch sobre IEEE Xplore / ACM / MDPI / arXiv / dblp / NDSS.

---

## Resumen ejecutivo

- **Las dos correcciones factuales del acta §0.5 quedan CONFIRMADAS** y son introducciones nuevas (no correcciones de una frase ya errónea): el plan **no** atribuye hoy "24/36" a nadie, y la frase de normality shift (P090) **no** declara que la evidencia proceda de NIDS/SCADA.
  - (a) "24/36 ataques, cero FP, sin detectar ataques sigilosos" = **AICrit (Raman & Mathur, JISA 2022, 64:103046)**. **Confirmado textualmente.** Koutroulis (Sensors 2023, 23(1):257): **F1=0,941, cero falsas alarmas, 4 ataques no detectados.** **Confirmado.**
  - (b) Han et al. OWAD (NDSS 2023) trabaja sobre **aplicaciones de seguridad NIDS/log** (Tsinghua), no agua. Trasladable, pero debe declararse. P090 debe matizarse.
- **Referencias dudosas (2024/2025/preprints): TODAS existen.** SSAD, Barakat/DEVS, Malarkkan, Cai/Wei/Luo, SSAD-Wei, Alnegheimish M2AD, Alves 2026, Li MLAD, Franco ShaTS: confirmadas como trabajos reales.
- **Pero hay 3 errores de metadatos serios en el plan** que marco abajo:
  1. **P146 (M2AD): lista de autores INCORRECTA.** El plan pone "Alnegheimish, Liu, Sala, Berti-Equille, Veeramachaneni"; los autores reales son **Alnegheimish, He, Reimherr, Chandrayan, Pradhan, D'Angelo** (AISTATS 2025, PMLR 258:4384-4392).
  2. **P145 (Adepu & Mathur): año/volumen.** El plan cita "2018" sin volumen; la versión publicada es **2021, IEEE TDSC 18(1):86-99** (el acta tiene razón).
  3. **P190 (Li MLAD): incompleta.** Faltan autores reales (Kunqi Li, Tang, Liang, Li, Liang) y locus **Sensors 2025, 25(13):4115**.
- **Refs NUEVAS que faltan en P145–P228 (confirmadas):** **Erba et al. ACSAC 2020**, **Raman & Mathur / AICrit JISA 2022**, **Fung et al. ESORICS 2022**. APA listo abajo.
- **Purgar (off-domain, confirmado):** Marquardt/OntoCape (P199) y Hendriks (P177). Ambas solo se citan en P095; purga sin huérfanas globales, pero P095 requiere reescritura local menor (sobre todo la frase de Hendriks).

---

## Correcciones factuales

### (a) AICrit (24/36) vs Koutroulis (F1≈0,941)

**Hallazgo de verificación.** Búsqueda en el texto del plan: las cifras "24", "36", "19/22", "0,941" **no aparecen en ningún párrafo del plan**. Por tanto NO existe hoy una frase que atribuya erróneamente "24/36" a Koutroulis: la corrección consiste en **introducir** los datos correctos donde el plan habla de invariantes/híbridos y de su techo, citando a quien corresponde.

Datos verificados:

| Afirmación | Fuente correcta | Verificación |
|---|---|---|
| "Cero falsos positivos, pero solo **24 de 36** escenarios de ataque detectados en SWaT; no detecta ataques sigilosos por su baja tasa de manipulación" | **Raman & Mathur, AICrit, JISA 2022, 64:103046** (*"AICrit: A unified framework for real-time anomaly detection in water treatment plants"*) | Confirmado vía ScienceDirect/ResearchGate: "zero false positive rate; however, only 24 out of 36 attack scenarios… are detected… did not detect any stealthy attacks due to their low manipulation rate". (Cuidado: la cifra "95,83 % de 27 ataques" corresponde a OTRO paper, AICrit *Applied Sciences* 2023, 13(24):13124 — NO confundir.) |
| "F1 ≈ **0,941**, cero falsas alarmas, **4 ataques no detectados** (que tampoco cumplían su objetivo físico)" | **Koutroulis, Mutlu & Kern, Sensors 2023, 23(1):257** | Confirmado: "F1-score of 0.941… highest F1 score with zero false alarms… not able to detect four attacks". (El matiz "esos 4 no cumplían su objetivo físico" es coherente con el paper pero conviene atribuirlo con cautela: "según los autores".) |

**Frase exacta a INSERTAR (recomendada) en P076 o, mejor, como CAVEAT al final de P089 / dentro de P076** (donde el plan menciona los híbridos "Umer et al., 2020; Raman & Mathur, 2022"):

> "Estos enfoques basados en invariantes tienen, no obstante, un techo conocido frente a ataques sigilosos: AICrit alcanza cero falsos positivos pero solo detecta 24 de los 36 escenarios de ataque de SWaT, al no disparar ante manipulaciones de baja magnitud (Raman & Mathur, 2022b)."

**Importante (riesgo de colisión de citas):** el plan ya cita "Raman & Mathur, 2022" en P076, P089 y P115, pero esa referencia es la de **TSMC 2022, 52(9):6003-6014** (P207, marco híbrido física-datos). **AICrit (JISA 2022, 64:103046) es un artículo DISTINTO del mismo par de autores y el mismo año** → al añadirlo habrá que desambiguar con sufijo de año (p. ej. `Raman & Mathur, 2022a` = TSMC; `2022b` = AICrit/JISA) en TODAS las citas en el texto, no solo en la nueva.

**Sobre Koutroulis:** el plan lo cita en P080 (grafos con estructura causal) sin sus métricas. Si se quiere usar el dato F1=0,941 / 4 no detectados (p. ej. en P080 o en §8 al posicionar frente a Koutroulis), insertar:

> "…aunque su detección causal-estructural alcanza un F1 de 0,941 con cero falsas alarmas en SWaT, deja sin detectar cuatro ataques (Koutroulis et al., 2023)."

**Nota de metadato sobre Koutroulis (P187):** el plan lo fecha **2022**; el volumen citado, **Sensors 23(1):257**, corresponde al **número de enero de 2023** (recibido nov-2022, publicado 2023). APA usa el año de publicación → debería ser **(2023)**, no (2022). Coherente además con que el acta §0.5/§8 lo cita como "Koutroulis et al. 2023". **Recomendación: cambiar el año a 2023 en P187 y en la cita de P080.**

### (b) Concept drift / normality shift = evidencia NIDS/SCADA, trasladable pero a declarar

**Hallazgo.** La frase afectada es **P090**:

> "[P090] … En los detectores semisupervisados, entrenados solo sobre operación normal, la deriva determinante es la de la propia normalidad (del inglés *normality shift*), una vertiente señalada como poco explorada frente a la deriva de los patrones anómalos (Han et al., 2023); su efecto es una degradación progresiva del rendimiento que ha motivado detectores de deriva sensibles al propio rendimiento del modelo (Bayram et al., 2022)."

**Verificación.** OWAD (Han et al., NDSS 2023) se evalúa sobre **"three security-related anomaly detection applications"** de tipo **NIDS / detección de intrusiones / logs** (autores de Tsinghua + State Grid), **no sobre series OT de proceso de agua**. La afirmación del plan es correcta en el fondo, pero **presenta la evidencia como si fuera del dominio** sin aclarar su procedencia.

**Frase exacta a INSERTAR** (añadir cláusula al final de la cita de Han en P090):

> "…una vertiente señalada como poco explorada frente a la deriva de los patrones anómalos (Han et al., 2023); esta evidencia procede mayoritariamente de la detección de intrusiones en red y del análisis de registros, y se asume aquí como **trasladable** a las series OT de proceso de agua, extrapolación que esta investigación se propone verificar y no da por demostrada en el dominio hídrico."

(El mismo matiz vale para Gama et al. 2014 y Lu et al. 2019, que son surveys de concept drift genéricos, no de agua; el plan ya los usa correctamente como marco general en P090.)

---

## Referencias [VERIFICAR MANUALMENTE]

Tras la verificación, **ninguna de las referencias dudosas resultó inexistente**. Las que mantengo en watch son por **metadatos no confirmables al 100 % desde snippets** (IEEE Xplore bloquea WebFetch directo: HTTP 403). Recomiendo una comprobación manual final en IEEE Xplore / la página del editor para los campos marcados.

| Ref (Pxxx) | Qué se pudo confirmar | Qué NO se pudo confirmar / riesgo | Recomendación |
|---|---|---|---|
| **SSAD — Wei et al. (2024), MSN 2024** (P222) | EXISTE: IEEE Xplore doc **11036473**, título *"SSAD: State Space-Based Anomaly Detection in Industrial Control Systems"*, conferencia MSN 2024, ICS/FDI, espacio de estados. | Páginas exactas (plan: 479-486) y DOI (`10.1109/MSN63567.2024.00072`) y lista completa de autores **no verificados desde snippet**. | Existe → **mantener**. Verificar manualmente páginas+DOI+autores en IEEE Xplore (doc 11036473). |
| **Barakat/DEVS — Barakat et al. (2025), SMARTCOMP 2025** (P151) | EXISTE: *"State-Based Modeling and Anomaly Detection in Industrial Systems Using DEVS"*, autores Ghena Barakat, Harshit Gupta, Luca D'Agati, G. Tricomi, F. Longo, G. Merlino, A. Puliafito; SMARTCOMP 2025 (Cork, jun-2025). Lista de autores del plan = correcta. | Páginas (plan: 474-479) y DOI (`10.1109/SMARTCOMP65954.2025.00108`) no verificados desde snippet. | **Mantener.** Verificar páginas+DOI en IEEE Xplore. |
| **Malarkkan et al. (2025), arXiv 2507.08177** (P197) | CONFIRMADO al 100 %: ID, título, autores (Malarkkan, Bai, X. Wang, Kaushik, D. Wang, Fu) coinciden con el plan. Vision paper, SIGSPATIAL 2025. | — | **Correcta. Sin acción** (es preprint/vision paper; OK como tal). |
| **Cai, J., Wei, Z., & Luo, J. (2024), IEEE TII** (P154) | CONFIRMADO: *"ICS Anomaly Detection Based on Sensor Patterns and Actuator Rules in Spatiotemporal Dependency"*, IEEE TII **20:10647-10656 (2024)**, IEEE Xplore doc **10530861**. Método = "SA²" (sensor-actuator separated) → coincide con "Cai et al. SA² 2024" del acta §8. | Issue exacto (plan: 20(8)) y DOI (`10.1109/TII.2024.3393528`) no verificados desde snippet; iniciales de autores plausibles. | **Mantener.** Verificar issue+DOI. |
| **Autoría "Wei"** (P222 SSAD = Wei, Z. 1er autor; P154 = Cai, J., **Wei, Z.**, Luo, J. 2º autor) | CONFIRMADO que son **dos trabajos distintos y reales** con un autor común (Z. Wei): SSAD (MSN 2024) y SA² (TII 2024). No es duplicado ni autor inventado. | — | **Ambas correctas como trabajos distintos.** |
| **Alnegheimish M2AD (2025)** (P146) | EXISTE: arXiv **2504.15225** + **AISTATS 2025, PMLR 258:4384-4392**. Título correcto. | **AUTORES DEL PLAN INCORRECTOS** (ver sección de erratas abajo). | **CORREGIR autores.** No es "verificar": es error confirmado. |
| **Alves et al. (2026), arXiv 2603.18941** (P147) | CONFIRMADO: ID y título correctos; autores reales Bruna Alves, Armando J. Pinho, Sónia Gouveia. | Las iniciales "B. C. F." del primer autor en el plan no se pudieron confirmar (la fuente lista "Bruna Alves"); 2º/3er autor OK. | **Mantener**; verificar iniciales del 1er autor. Es preprint → OK como tal. |
| **Li et al. (2025) MLAD** (P190) | CONFIRMADO: *"MLAD: A Multi-Task Learning Framework for Anomaly Detection"*, **Sensors 2025, 25(13):4115**, autores Kunqi Li, Zhiqin Tang, Shuming Liang, Zhidong Li, Bin Liang (UTS). | El plan está **incompleto** ("Li, K., et al. … Sensors." sin vol/núm/art/DOI). | **COMPLETAR** (ver erratas). |
| **Franco de la Peña ShaTS (2025), arXiv 2506.01450** (P165) | CONFIRMADO al 100 %: ID, título, autores (Franco de la Peña, Perales Gómez, Fernández Maimó) coinciden con el plan. | — | **Correcta. Sin acción.** |

### Erratas de metadatos confirmadas (no "dudosas": verificadas como erróneas)

- **P145 — Adepu & Mathur:** plan dice "(2018)… IEEE TDSC" sin volumen ni páginas. **Correcto: (2021), IEEE TDSC, 18(1), 86-99**, DOI 10.1109/TDSC.2018.2875008 (dblp: `AdepuM21`). El DOI con "2018" es el del online-first; la **versión publicada es 2021 18(1):86-99**. El acta §3 tiene razón. → **Cambiar año a 2021 y añadir 18(1), 86-99.** (Afecta a las citas en texto P076 y P115, que pasarían a "Adepu & Mathur, 2021".)
- **P146 — M2AD:** **autores erróneos.** Plan: "Alnegheimish, S., Liu, L., Sala, A., Berti-Equille, L., & Veeramachaneni, K." → **Reales: Alnegheimish, S., He, Z., Reimherr, M., Chandrayan, A., Pradhan, A., & D'Angelo, L.** (los autores que el plan lista, Berti-Equille y Veeramachaneni, son colaboradores habituales de Alnegheimish en OTROS papers — error de copiado). Además, ya no es solo preprint: **publicado en AISTATS 2025 (PMLR 258:4384-4392)** → conviene citar la versión de conferencia.
- **P190 — MLAD:** incompleta (ver tabla). Completar a Sensors 2025, 25(13):4115.
- **P187 — Koutroulis:** año 2022 → **2023** (Sensors 23(1):257 es número de enero 2023; el acta lo cita como 2023).

---

## Referencias NUEVAS a añadir

APA 7ª, sangría francesa, listas para pegar en §6 (orden alfabético). Indico para qué afirmación/sección sirve cada una.

**FALTAN en P145–P228 (confirmadas como ausentes) — añadir:**

```
Erba, A., Taormina, R., Galelli, S., Pogliani, M., Carminati, M., Zanero, S., &
    Tippenhauer, N. O. (2020). Constrained concealment attacks against
    reconstruction-based anomaly detectors in industrial control systems. En
    Proceedings of the 36th Annual Computer Security Applications Conference
    (ACSAC '20) (pp. 480-495). Association for Computing Machinery.
    https://doi.org/10.1145/3427228.3427660
```
→ **Para:** evidencia empírica de la fragilidad/brecha (hipótesis central, §3.1/§3.4 y P084/P088). Dato citable: el recall en WADI cae de 0,68 a 0,12 manipulando 4 de 82 sensores. (Verificar nº de páginas exacto del DOI ACM; 480-495 es el rango habitualmente indexado.)

```
Raman, M. R. G., & Mathur, A. P. (2022). AICrit: A unified framework for
    real-time anomaly detection in water treatment plants. Journal of
    Information Security and Applications, 64, 103046.
    https://doi.org/10.1016/j.jisa.2021.103046
```
→ **Para:** el CAVEAT del techo de las invariantes (P076/P089 y acta §3): cero FP pero 24/36 ataques, no detecta sigilosos. **DISTINTA de P207** (Raman & Mathur, TSMC 2022, marco híbrido). **Requiere desambiguar año con sufijos a/b** en P076, P089, P115 y P207.

```
Fung, C., Srinarasi, S., Lucas, K., Phee, H. B., & Bauer, L. (2022).
    Perspectives from a comprehensive evaluation of reconstruction-based
    anomaly detection in industrial control systems. En V. Atluri, R. Di Pietro,
    C. D. Jensen, & W. Meng (Eds.), Computer Security – ESORICS 2022 (LNCS
    13556, pp. 493-513). Springer. https://doi.org/10.1007/978-3-031-17143-7_24
```
→ **Para:** inconsistencia de resultados entre datasets / falta de reproducibilidad (hipótesis central, §3.4). **DISTINTA de Fung et al. NDSS 2024 (P166)**, que es la de atribución/actuadores categóricos. (Verificar rango de páginas LNCS; capítulo _24.)

**Verificar iniciales/páginas antes de fijar:** Erba (páginas ACM), Fung ESORICS (páginas LNCS).

---

**YA PRESENTES en el plan (acta §7 [v2] / §3) — NO duplicar, solo confirmadas y, en su caso, completar pages:**

- Kim et al. **AAAI 2022, 36(7):7194-7201** → **presente y correcta** en P186. ✔
- Wu & Keogh, **IEEE TKDE 35(3):2421-2429 (2023)** → presente en P223 **pero sin vol/núm/páginas** (solo DOI). **Completar** a `IEEE Transactions on Knowledge and Data Engineering, 35(3), 2421-2429.` (mantener DOI; el plan la fecha 2021 por el online-first — la versión impresa es 2023; aceptable conservar 2021 si se prefiere coherencia con la cita en texto "Wu & Keogh, 2021", pero entonces NO mezclar con vol 35(3) de 2023; lo más limpio: año **2023**, 35(3):2421-2429).
- Heydari & Nyarko, **IEEE Access 2026, 14:17585-17609** → **presente y correcta** en P180. ✔
- Lamberts et al., **SoK, J. Systems Research 2023** → **presente y correcta** en P188. ✔
- Han et al. (OWAD), **NDSS 2023** → presente en P176 como "Han, D., et al. (2023)". ✔ (Opcional: APA admite "et al." con ≥21 autores listando los 19 primeros + … + último; con su autoría enorme, "Han, D., et al." es aceptable. Primer autor = Dongqi Han, confirmado.)
- Cai et al. (SA²), **IEEE TII 2024** → presente en P154. ✔ (verificar issue+DOI).
- Fung et al., **NDSS 2024** → **presente y correcta** en P166. ✔

**Refs del acta §3 comprobadas y ya presentes (correctas salvo nota):**
Paparrizos VLDB 2022 (P204 ✔), Huet KDD 2022 (P181 ✔), Garg TNNLS 2021 (P169 ✔), Gama CSUR 2014 (P167 ✔), Lu TKDE 2019 (P193 ✔), Bayram KBS 2022 (P152 ✔), Feng NDSS 2019 (P164 ✔), Deng & Hooi AAAI 2021 (P161 ✔), Ghaeini SAC 2018 (P170 ✔), Li et al. TKDE (P191: el plan lo da como **2023, 35(6):6058-6072**, DOI 10.1109/TKDE.2022.3171562 — el "2022/2023" del acta se resuelve como **2023** impreso / online 2022; correcto). **Adepu & Mathur: ver erratas (P145, año 2021).**

---

## Referencias a purgar

Confirmado por dominio ajeno (acta §6/§7):

| Ref | Pxxx | Verificación de dominio ajeno | ¿Deja huérfanas? |
|---|---|---|---|
| **Marquardt et al. (2010), OntoCape** | P199 (entrada) + **citada solo en P095** | CONFIRMADO: *"OntoCAPE: A Re-Usable Ontology for **Chemical Process Engineering**"*, Springer 2010. Proceso químico, no agua/OT. | **Sin huérfanas globales** (solo aparece en P095). Retirada limpia: borrar el inciso "OntoCape para procesos químicos (Marquardt et al., 2010)" de la lista de familias de ontologías; SAREF/DEXPI/BFO ya figuran sin cita, así que la frase sigue siendo gramatical. |
| **Hendriks et al. (2024), condition monitoring de activos** | P177 (entrada) + **citada solo en P095** | CONFIRMADO: *"Structured data ontology for AI in industrial **asset condition monitoring**"*, J. Sensor and Actuator Networks 13(2):23. Monitorización de estado de activos, no detección en OT hídrico. | **Riesgo de huérfana LOCAL en P095.** La frase *"El cierre del ciclo de la ontología a la IA es aún incipiente; Hendriks et al. (2024) aportan uno de los pocos casos aplicados."* quedaría coja. **Acción:** reescribir a *"El cierre del ciclo de la ontología a la IA es aún incipiente, con escasos casos aplicados en el dominio industrial."* (sin cita), o sustituir por una referencia del sector hídrico si se desea respaldo. |

**Nota:** ambas se citan exclusivamente en P095; ninguna aparece en abstract, objetivos, metodología ni en otras secciones (grep confirmado). Por tanto la purga **no** crea citas huérfanas fuera de P095; solo exige los dos retoques locales de redacción indicados.

(Dato adicional sobre coherencia de §7 del acta: el acta habla de "Refs 69 (SSN/SOSA), 71, 72" como a conservar para el hilo de transferibilidad; en el plan reescrito esas funciones las cubren **Haller et al. 2019 (P175, SSN/SOSA)**, **Karabulut et al. 2023 (P185)** y **Jarwar et al. 2025 (P183)** — todas presentes y de dominio pertinente (gemelos digitales / ontologías de seguridad industrial con nota de escasa cobertura hídrica). No requieren purga.)

---

## Inventario (acta vs plan)

**Leyenda:** ✔ presente y correcta · ⚠ presente con errata · ＋ falta (añadir) · ✖ purgar

| Referencia (acta §3/§7/§8/§0.5) | Estado en plan | Detalle |
|---|---|---|
| Kim et al., AAAI 2022, 36(7):7194-7201 | ✔ P186 | Correcta |
| Wu & Keogh, IEEE TKDE 35(3):2421-2429 | ⚠ P223 | Falta vol/núm/páginas (solo DOI); año online 2021 / impreso 2023 |
| Heydari & Nyarko, IEEE Access 2026, 14:17585-17609 | ✔ P180 | Correcta |
| Lamberts et al., SoK, J. Systems Research 2023 | ✔ P188 | Correcta |
| Han et al. (OWAD), NDSS 2023 | ✔ P176 | Correcta (et al.; 1er autor Dongqi Han). Dominio NIDS → declarar en P090 |
| Cai et al. (SA²), IEEE TII 2024 | ✔/⚠ P154 | Correcta; verificar issue 20(8)+DOI |
| Fung et al., NDSS 2024 | ✔ P166 | Correcta |
| **Erba et al., ACSAC 2020** | ＋ FALTA | Añadir (APA arriba). Dato recall WADI 0,68→0,12 |
| **Raman & Mathur / AICrit, JISA 2022, 64:103046** | ＋ FALTA | Añadir (APA arriba). Distinta de P207 (TSMC). Desambiguar 2022a/b |
| **Fung et al., ESORICS 2022** | ＋ FALTA | Añadir (APA arriba). Distinta de P166 (NDSS 2024) |
| Paparrizos, VLDB 2022 | ✔ P204 | Correcta |
| Huet, KDD 2022 | ✔ P181 | Correcta |
| Garg, TNNLS 2021 | ✔ P169 | Correcta (pero ojo: plan pone IJCIP **100356**; acta no lo discute — ver nota*) |
| Gama, CSUR 2014 | ✔ P167 | Correcta |
| Lu, TKDE 2019 | ✔ P193 | Correcta |
| Bayram, KBS 2022 | ✔ P152 | Correcta |
| Feng, NDSS 2019 | ✔ P164 | Correcta |
| **Adepu & Mathur, TDSC** | ⚠ P145 | Plan: 2018 sin vol; **correcto 2021, 18(1):86-99** |
| Deng & Hooi, AAAI 2021 | ✔ P161 | Correcta |
| Ghaeini, SAC 2018 | ✔ P170 | Correcta |
| Li et al., TKDE 2022/2023 | ✔ P191 | Correcta (2023, 35(6):6058-6072) |
| Koutroulis et al. | ⚠ P187/P080 | Año 2022 → **2023**; métricas F1=0,941/4 no detect. disponibles para citar |
| Malarkkan, arXiv 2507.08177 | ✔ P197 | Correcta |
| SSAD (Wei et al.), MSN 2024 | ✔/⚠ P222 | Existe (doc 11036473); verificar pág+DOI |
| Barakat/DEVS, SMARTCOMP 2025 | ✔/⚠ P151 | Existe; verificar pág+DOI |
| Alnegheimish M2AD | ⚠ P146 | **Autores incorrectos**; añadir AISTATS 2025 PMLR 258:4384-4392 |
| Alves et al. 2026, arXiv 2603.18941 | ✔/⚠ P147 | Correcta; verificar iniciales 1er autor |
| Li et al. MLAD 2025 | ⚠ P190 | Incompleta → Sensors 25(13):4115, autores Kunqi Li et al. |
| Franco de la Peña ShaTS, arXiv 2506.01450 | ✔ P165 | Correcta |
| Marquardt/OntoCape 2010 | ✖ P199 | Purgar (proceso químico). Retoque en P095 |
| Hendriks 2024 | ✖ P177 | Purgar (condition monitoring). Reescribir frase en P095 |

\* **Nota colateral (fuera del mandato, pero detectada):** P218 cita Umer et al. 2020 como **IJCIP 28, 100356**, mientras el acta §3 lo lista como **28:100341**. Discrepancia de número de artículo entre acta y plan → **verificar manualmente** (no resuelto aquí; uno de los dos está mal). No afecta a las correcciones del mandato.

---

### Cierre

Verificación cerrada. Bloqueo técnico: IEEE Xplore/MDPI/PMC devuelven 403 a WebFetch directo, por lo que páginas/DOI de actas IEEE (SSAD, Barakat, Cai) se confirmaron por existencia (doc-id) pero no campo a campo → marcados [VERIFICAR MANUALMENTE] solo en esos campos. Ninguna referencia resultó inexistente.
