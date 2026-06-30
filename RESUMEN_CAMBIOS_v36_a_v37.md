# Resumen de cambios v36 → v37

> Reescritura orquestada del Plan de Investigación según el **Acta de Decisiones v2**.
> Entregables: `Plan_Investigacion_v37.docx` (autoritativo) · `Plan_Investigacion_v37_preview.pdf` (vista) ·
> este resumen · `PREGUNTAS_PENDIENTES.md`. Texto de trabajo en `trabajo/plan_v37.md`.

## Cómo se hizo (trazabilidad)
- **FASE 0–1:** extracción del v36, checklist del acta (`CHECKLIST_ACTA.md`), y verificación con 5 subagentes en paralelo (`verificacion/V1…V5.md` → `INFORME_CONSOLIDADO.md`).
- **FASE 2:** redacción secuencial sección por sección (`trabajo/plan_v37.md`).
- **FASE 3:** control de calidad (`verificacion/FASE3_VERIFICACION.md`): 0 términos prohibidos, 84/84 citas con entrada en bibliografía (sin huérfanas), checklist del acta aplicada.
- **FASE 4:** generación del `.docx` editando el v36 (estilos, portada, encabezados, sangría francesa preservados).

---

## Cambios por sección

### Título (portada)
- **Antes:** «Contribuciones a la detección de anomalías en sistemas de control industrial de infraestructuras hídricas mediante técnicas de Inteligencia Artificial».
- **Ahora (infinitivo, centrado en la brecha):** «Caracterizar y reducir la brecha entre el rendimiento en banco de pruebas y el despliegue operativo de la detección de anomalías en sistemas de control industrial de agua: un estudio sobre series temporales de la capa OT». *(Propuesta — ver Q2.)*

### 1. Resumen
- Reescrito desde cero. Objeto = **la brecha** (testbeds = objeto de estudio; datos de planta = evidencia/PoC, no métricas). Eliminado el esquema de «tres hipótesis competidoras H0/H1/H2». Acotado a **series OT / Purdue 0-2**. Corregido «estado endógeno reproducible por diseño» → **asociaciones estables**. Operacionalización = gobierno de la alarma (no «información»).

### 2. Objetivos e hipótesis
- **Objetivos:** general ≈ título; específicos = **WP0–WP3** + hilo teórico. Eliminado el encuadre **IIoT** (P043 v36). Eliminado el objetivo 5 de «despliegue en hardware de borde» como objetivo (demotado a consecuencia operativa — ver Q1).
- **Hipótesis (reemplazo total de P051–P056 v36):** **central (explicativa)** [factores metodológicos de evaluación + factores del sistema] + **de trabajo (mecanismo)** [ruptura de asociaciones condicionada al régimen] + **interpretabilidad como consecuencia** (Fung 2024) + **delimitación explícita** + **criterio de decisión** (acta §10). Dos planos (central→WP1-2, trabajo→WP3), excluyentes en lo que afirman.

### 3. Introducción y estado del tema
- **3.1:** acotación OT/Purdue; terminología de **oráculo de umbral**; sustrato conceptual corregido (endógeno/exógeno, asociaciones); tono calibrado (NIS2 «vuelve exigible» en vez de «cumplir»; «uno de los primeros» en vez de «primer intento masivo»).
- **3.2:** **inserción de la pila de Purdue (niveles 0-2)** y declaración de que el objeto son las series del proceso físico, no IT/tráfico/protocolos.
- **3.3:** retitulada «…en series OT»; **caveat del techo de invariantes** (AICrit: cero FP, 24/36 ataques); evidencia adversarial de Erba et al. (2020); atribución tratada como descripción, no causa.
- **3.4:** terminología de oráculo de umbral; tono no-denuncia («documenta» en vez de «denuncia»); **panel obligatorio** (VUS-PR + afiliación + Fc1 + presupuesto de alarmas + baselines triviales); construido **sobre** Heydari & Nyarko, no como novedad.
- **3.5:** **normality shift declarado de origen NIDS/logs**, trasladable a verificar (no demostrado en agua).
- **3.6:** **interpretabilidad = consecuencia** (no hipótesis); Fung 2024 (proxy ≠ causa); LLM demotado a una frase de trabajo futuro (ver Q6).
- **3.7:** **separación de roles** modelo de información (operativo, ISA-95) vs ontología (transferencia/interoperabilidad, SSN/SOSA); respaldo en agua reconocido como débil; **purga de OntoCape y condition monitoring**.

### 4. Metodología y plan de trabajo
- **4.1:** DSR conservado y calibrado; el «diseño de atribución factorial» se reorienta a **cuantificar los factores del acta** (oráculo, ajuste por puntos, no estacionariedad, régimen); efectos «condicionales al pipeline, no causales».
- **4.2:** variables con endógeno/exógeno correctos; **panel de evaluación** y confusoras (oráculo, normalización, ajuste por puntos, solape); muestras por conveniencia reconocidas.
- **4.3 (reemplazo de la antigua 4.3):** **WP0–WP3 + hilo teórico**, con salidas (Papers 1-3) y cierres; orden WP1→WP2→WP3 con **WP2/WP3 solapados**.
- **4.4 Cronograma:** tabla reusada del v36 con **etiquetas WP0–WP3** y barras solapadas (WP2/WP3).
- **4.5:** conservado; hardware de borde reducido a comprobación.

### 5. Posicionamiento frente al estado del arte *(sección nueva — acta §8)*
- Tabla de diferenciación (Heydari & Nyarko / Cai SA² / Han OWAD / Umer-Raman-Mathur / Koutroulis) + **tesis = integración** + cuatro huecos.

### 6. Interés científico y aplicabilidad *(antes «Interés científico»)*
- Calibrado: «orientación, no receta»; «principios que el programa busca validar»; eliminado «robusto al resultado» y «directamente accionable / reutilizable más allá del dominio»; beneficiarios (operadores, reguladores), encaje EECTI/NIS2 como motivación, no promesa de despliegue.

### 7. Bibliografía
- 84 entradas, APA 7ª, orden alfabético, sangría francesa. Sin citas huérfanas (verificado).

---

## Referencias: añadidas, corregidas y purgadas

**Añadidas (3):**
- Erba et al. (2020), ACSAC — fragilidad adversarial (recall WADI 0,68→0,12).
- Raman & Mathur (2022b), *AICrit*, JISA 64:103046 — techo de invariantes (24/36, cero FP). Distinta de Raman & Mathur (2022a) TSMC.
- Fung et al. (2022), ESORICS — inconsistencia de resultados entre datasets.

**Corregidas (metadatos):**
- Adepu & Mathur: 2018 → **2021, 18(1):86-99**.
- Koutroulis et al.: 2022 → **2023**.
- Wu & Keogh: 2021 → **2023, 35(3):2421-2429**.
- Alnegheimish (M2AD): autores corregidos → Alnegheimish, He, Reimherr, Chandrayan, Pradhan, D'Angelo (AISTATS 2025, PMLR 258:4384-4392).
- Li (MLAD): completada → Sensors 25(13):4115.
- Raman & Mathur (TSMC): desambiguada como **2022a** (vs 2022b/AICrit).

**Purgadas (dominio ajeno / línea demotada):**
- Marquardt et al. (2010), OntoCape — proceso químico.
- Hendriks et al. (2024) — condition monitoring de activos.
- Antonini et al. (2023), TinyML — vinculada al despliegue en borde (demotado).

---

## [VERIFICAR MANUALMENTE] — comprobar antes de la versión final
Las referencias **existen** (verificadas); solo los campos indicados no se confirmaron al 100 % (IEEE Xplore/MDPI devuelven 403 a la verificación automática):

1. **Wei et al. (2024), SSAD, MSN 2024** — páginas (479-486) y DOI.
2. **Barakat et al. (2025), DEVS, SMARTCOMP 2025** — páginas (474-479) y DOI.
3. **Cai et al. (2024), SA², IEEE TII** — issue 20(8) y DOI.
4. **Erba et al. (2020), ACSAC** — rango de páginas exacto (480-495).
5. **Fung et al. (2022), ESORICS** — rango de páginas LNCS (493-513).
6. **Alves et al. (2026), arXiv 2603.18941** — iniciales del primer autor.
7. **Li et al. (2025), MLAD, Sensors** — confirmar autores y DOI.
8. **Umer et al. (2020), IJCIP** — nº de artículo: el plan tenía **100356**, el acta **100341** (resolver cuál es correcto — ver Q8).

*(Estos marcadores están en `trabajo/plan_v37.md`; se han retirado del `.docx` para no afectar a la presentación.)*

---

## Preguntas para ti → ver `PREGUNTAS_PENDIENTES.md`
Q1 (borde/TinyML: demotado por defecto) · Q2 (título exacto) · Q3 (skills `contraparte-critica`/`sintesis-densa`/`revisar-ia` no estaban en el entorno: emuladas) · Q4 (informe de revisión no estaba en el repo) · Q5 (línea «Multimedia» conservada; IIoT eliminado) · Q6 (LLM como una frase de futuro) · Q7 («gemelos digitales» acotado) · Q8 (Umer 100356 vs 100341) · Q9 (sección 5 nueva + renumeración).

## Nota sobre el PDF
`Plan_Investigacion_v37_preview.pdf` es una **vista fiel renderizada desde el contenido** (HTML→Chromium), porque LibreOffice/Word no están operativos en este entorno de ejecución para convertir el `.docx`. El entregable autoritativo, con los estilos del v36, es **`Plan_Investigacion_v37.docx`**; ábrelo en Word para la maquetación final (la granularidad del cronograma se ajusta al maquetar).
