# MAPA_SECCIONES.md — Estructura actual del Plan v36 (índice con nº de párrafo)

> Párrafos identificados como `[PNNN]` en `trabajo/plan_actual.md`. 229 párrafos totales + 1 tabla (cronograma).
> Estilos en uso: `Heading 1` (7), `Heading 2` (12), `Normal` (210).

## Portada (P000–P014)
- P003 ESCUELA INTERNACIONAL DE DOCTORADO · P004 Programa de Doctorado
- P006 **Título** actual: "Contribuciones a la detección de anomalías en sistemas de control industrial de infraestructuras hídricas mediante técnicas de Inteligencia Artificial"
- P009 Autor: David Palazón Palau · P011–P012 Directores: Dr. Juan Miguel Navarro Ruiz, Dr. Antonio Pita Lozano · P014 Murcia, Junio de 2026

## Índice de contenidos (P015 H1; P016–P033)

## 1. Resumen del proyecto de tesis (P035 H1; P036–P040)
- P036 brecha banco↔operación · P037 **tres hipótesis competidoras (H0/H1/H2)** · P038 sustrato (estado endógeno "reproducible por diseño" ⚠E4) · P039 TrueData/GRITA/UCAM · P040 **Palabras clave**

## 2. Objetivos científicos (P042 H1; P043–P056)
- P043 encuadre (⚠**IIoT** F3) · P044 objetivo general · P045–P050 5 objetivos específicos (P050 = viabilidad despliegue borde ⚠) · P051 hipótesis general · P052–P056 **H0/H1/H2 + interacción** (⚠ se reemplaza por central+trabajo)

## 3. Introducción y estado del tema (P057 H1)
- **3.1 Justificación** (P058 H2; P059–P069): P059–P063 regulación/amenazas · P065 dificultades (⚠ best-F1/filtración G1) · P066 deriva/explicabilidad/contexto · P067 sustrato espacio de estados (⚠ "reproducible por diseño" E4, mezcla actuadores en exógenas E2) · P068 brecha como objeto · P069 hoja de ruta 6 bloques
- **3.2 Infraestructuras hídricas y ciberseguridad** (P070 H2; P071–P073): ⚠ falta Purdue explícito F4; P071 lista IT+OT (RTU/HMI/protocolos) revisar F2
- **3.3 Técnicas de IA para detección en ICS** (P074 H2; P075–P082): familias (invariantes, predicción, reconstrucción, regresión transversal, grafos, fusión); ⚠ I1/I3 caveat AICrit
- **3.4 Detección fiable y evaluación rigurosa** (P083 H2; P084–P085): ⚠ G1 terminología best-F1; D1 panel métricas
- **3.5 Deriva, contexto operativo y robustez** (P086 H2; P087–P090): P089 state-aware; P090 normality shift (⚠ I2 NIDS/logs)
- **3.6 Explicabilidad de las alarmas** (P091 H2; P092–P093): ⚠ B4/B8 interpretabilidad=consecuencia, Fung 2024
- **3.7 Estructuración del contexto y viabilidad de despliegue** (P094 H2; P095–P096): P095 modelo info/ontología (⚠ E6/E7/E8 roles distintos, H1/H2 lit); P096 edge/TinyML (⚠ demotar)

## 4. Metodología y plan de trabajo (P097 H1)
- **4.1 Marco metodológico** (P098 H2; P099–P110): DSR, Gregor&Hevner exaptación, bucle experimental, **atribución factorial** (⚠ reestructurar a central+trabajo/WP), FEDS
- **4.2 Diseño experimental** (P111 H2; P112–P117): datasets, variables (⚠ E2 endo/exo), **protocolo insesgado** (G1/D1/D2), familias, reproducibilidad, amenazas a la validez
- **4.3 Organización del trabajo** (P118 H2; P119–P127): corrientes/rampa/suelo-sonda-sonda (⚠ reemplazar por WP0–WP3 + hilo)
- **4.4 Cronograma** (P128 H2; P129–P131 + TABLA 12×17): ⚠ C8 barras solapadas WP2/WP3
- **4.5 Instalaciones, instrumentos y técnicas** (P132 H2; P133–P136): GPU/edge HW, datasets, software, ThingsBoard/Zotero

## 5. Interés científico del proyecto (P137 H1; P138–P143)
- P139 método de atribución · P140 principios de diseño · P141 robustez al resultado · P142 revistas · P143 transferencia/aplicabilidad (⚠ A1/J2 integración; sin sobreventa)

## 6. Bibliografía consultada (P144 H1; P145–P228)
- ~80 referencias APA 7ª, orden alfabético, sangría francesa. Añadir nuevas (H4), corregir factual (I1), [VERIFICAR MANUALMENTE] (H5), purgar ajenas (H2/H3).

---
## Correspondencia v36 → estructura v37 (acta)
| v37 (acta) | Origen en v36 |
|---|---|
| Título (infinitivo, brecha) | reescribe P006 |
| Resumen | reescribe 1 (P036–P040) |
| Palabras clave | reescribe P040 |
| Objetivos (general ≈ título; específicos = WP0–WP3) | reescribe 2 (P043–P050) |
| Hipótesis (central + trabajo + interpretabilidad + delimitación) | **reemplaza** H0/H1/H2 (P051–P056) |
| Introducción / estado del tema | reordena/purga 3.1–3.7 |
| Metodología (DSR, cuasi-exp, variables, panel métricas, sesgos, reproducibilidad) | reescribe 4.1–4.2 |
| Work packages y plan | **reemplaza** 4.3 por WP0–WP3 + hilo; conserva 4.4 cronograma + 4.5 |
| Posicionamiento / SOTA (tabla §8) | **sección nueva** (de Interés + acta §8) |
| Aplicabilidad | reescribe 5 (P138–P143) |
| Bibliografía | actualiza 6 |
