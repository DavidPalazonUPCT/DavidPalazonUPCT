# PREGUNTAS_PENDIENTES.md — Para David (decisiones no cubiertas por el acta v2)

> Regla de oro aplicada: lo que el acta no cubre, NO se inventa; se anota aquí.

## Q1 — Viabilidad de despliegue en hardware de borde (edge / TinyML)
El plan v36 trata el despliegue en hardware de borde como **objetivo específico 5** y dedica media sección (3.7) y varias referencias (Antonini et al. 2023 TinyML; Zhou et al. 2024 HGNAS; ONNX/TensorRT) al tema. **El acta v2 NO incluye el despliegue en borde** en su estructura de WP0–WP3 ni en el panel de contribuciones; su foco es la brecha de transferencia, el rigor de evaluación, la deriva/régimen y la transferibilidad inter-planta.
- **Decisión tomada por defecto (reversible):** demoto el borde a una mención breve como *consecuencia operativa / trabajo futuro*, NO como objetivo ni WP, y retiro las referencias de TinyML/NAS hardware del corpus central (visión de "manufactura/IIoT/IA general" purgada).
- **¿Confirmas** que el despliegue en borde deja de ser objetivo/WP, o **quieres conservarlo** como línea operativa menor?

## Q2 — Título exacto
El acta exige un título en **infinitivo**, centrado en la **brecha** (no en "detectar anomalías"). Propongo (FASE 2) algo como: *"Caracterizar y reducir la brecha entre el rendimiento en banco de pruebas y el despliegue operativo de la detección de anomalías en sistemas de control industrial de agua (series temporales OT)"*. Es una propuesta; **dime si prefieres otra formulación o palabra ("explicar/medir/cerrar" en lugar de "caracterizar/reducir")**.

## Q3 — Skills no disponibles en este entorno
Las skills `contraparte-critica`, `sintesis-densa` y `revisar-ia` mencionadas en el prompt **no están instaladas** en este entorno de ejecución. He **emulado su función** (estrés de afirmaciones por revisor hostil; condensación sin relleno; auditoría de huella de IA y existencia de referencias) dentro de los subagentes y del control de calidad. Si tienes definiciones concretas de esas skills, puedo reejecutar esas pasadas con tus criterios.

## Q4 — Informe de revisión bibliográfica
El prompt menciona un informe de revisión bibliográfica "si está en el repo como `.md`". **No existe en el repositorio** (estaba vacío al iniciar). He usado el **respaldo citable que el propio acta consolida** (§3 y §8) como fuente. Si tienes ese informe, adjúntalo para verificación cruzada de metadatos.

## Q5 — Directores y línea del programa
El v36 encuadra la tesis en la "línea de **Tecnologías Multimedia**" (P043). El acta no lo menciona. Lo conservo salvo que indiques lo contrario; solo retiro el marco **IIoT** que el acta manda purgar.

## Q6 — LLM como capa de explicación (P093 v36)
El v36 menciona los LLM como capa de explicación en lenguaje natural, ya acotada como "fuera del alcance central". **Decisión por defecto:** la conservo como **una sola frase de trabajo futuro**, sin introducir NLP/LLM como objeto (el acta no lo contempla). ¿Eliminar del todo o mantener esa frase?

## Q7 — "Gemelos digitales" vía Karabulut et al. (2023)
La referencia se conserva como revisión de ontologías (soporte del hilo de transferibilidad), pero el sintagma "gemelos digitales" podría abrir un frente ajeno. **Decisión por defecto:** acoto la cita a "revisiones de ontologías" sin invocar *digital twins* como línea. ¿De acuerdo?

## Q8 — Discrepancia de metadato: Umer et al. (2020)
El plan v36 cita Umer et al. (2020) como IJCIP **28, 100356**; el acta lo lista como **28:100341**. Uno de los dos está mal. Lo dejo marcado **[VERIFICAR MANUALMENTE]**; no pude resolverlo (IEEE/Elsevier devuelven 403). Confírmame el número de artículo correcto.

## Q9 — Sección nueva de Posicionamiento y renumeración
El acta §8 pide una sección de **posicionamiento frente a trabajos solapados** (tabla) que el v36 no tenía. **Decisión por defecto:** la inserto como **sección 5 "Posicionamiento frente al estado del arte"**, con lo que "Interés científico" pasa a 6 (lo fusiono con "Aplicabilidad") y "Bibliografía" a 7. Las referencias cruzadas internas (3.x, 4.x) no cambian. ¿De acuerdo con esta ubicación?

---
*(Se añadirán entradas conforme surjan en FASE 2.)*
