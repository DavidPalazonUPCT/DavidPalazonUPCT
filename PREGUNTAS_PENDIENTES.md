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

---
*(Se añadirán entradas conforme surjan en FASE 2.)*
