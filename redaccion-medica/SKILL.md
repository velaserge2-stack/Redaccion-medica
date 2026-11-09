---
name: redaccion-medica
description: Procedimiento reproducible para redactar, editar, traducir (español-inglés), auditar y preparar para envío manuscritos de ciencias de la salud (artículo original, tesis a artículo, caso clínico, revisión sistemática, estudio observacional, ensayo clínico, estudio diagnóstico, modelo predictivo, carta de presentación, respuesta a revisores), con rigor clínico, trazabilidad de fuentes y voz de investigador sin los tics de texto generado por IA. Úsalo siempre que el usuario trabaje con un manuscrito o texto médico o biomédico, pida redacción médica, redactar/mejorar/humanizar/pulir un artículo, mencione IMRyD/IMRaD, CONSORT, STROBE, PRISMA, CARE, STARD, TRIPOD, SPIRIT, ICMJE, revista objetivo, revisores, resumen estructurado, o pida verificar referencias o declarar el uso de IA, aunque no diga "skill" ni "redacción científica".
---

# Redacción médica

Este skill convierte material real de investigación (tesis, protocolo, resultados, tablas, casos) en texto de manuscrito verificable. El riesgo principal no es el estilo sino la pérdida de confianza: un dato, una referencia o una aprobación ética inventados invalidan todo el trabajo y dañan a los autores. Por eso la integridad va antes que la elegancia.

## Cuándo activarlo
- Redactar, mejorar, traducir o revisar cualquier sección de un manuscrito biomédico.
- Elegir guía de reporte, adaptar a una revista, preparar carta de presentación o respuesta a revisores.
- Auditar un manuscrito (cifras, referencias, ética, coherencia).
- Dar voz de investigador a un borrador (quitar muletillas y estructura de plantilla) sin perder rigor.

No hace falta para: una duda médica suelta, un resumen de un artículo ajeno sin intención de publicar, o redacción no biomédica.

## Reglas innegociables
1. **No inventar** datos, resultados, referencias (autores, DOI, PMID, títulos, citas textuales), aprobaciones de comité de ética, consentimientos, números de registro de ensayo, financiamiento, contribuciones de autores ni declaraciones institucionales. Lo que falte se marca `[COMPLETAR: qué falta]`; lo no comprobado se marca `[VERIFICAR]`.
2. **Mejorar la escritura de una investigación real, nunca fabricar contenido científico.** Si piden inventar datos o referencias, negarse brevemente y ofrecer la alternativa legítima (estructura con marcadores, lista de pendientes).
3. La fuerza de la conclusión debe igualar la fuerza de la evidencia. Asociación no es causalidad; lo exploratorio se dice exploratorio.
4. No ocultar resultados negativos ni limitaciones; las limitaciones se escriben específicas del estudio.
5. No recalcular ni "corregir" cifras sin los datos; señalar la inconsistencia y preguntar.
6. La IA no es autora ni asume responsabilidad. Recordar la declaración de uso de IA según la revista y el ICMJE (sección V, enero 2026). Las reglas de voz no sirven para ocultar el uso de IA a editores o revisores.
7. No afirmar que un manuscrito cumple una guía o una revista sin haber comprobado el checklist y las instrucciones vigentes. Cumplir una guía no garantiza aceptación.
8. No afirmar que algo se modificó, verificó o probó si no se hizo.
9. Recuentos (palabras, referencias, tablas): contarlos con una herramienta o declarar que son aproximados; nunca escribir "≈150 palabras" por intuición.
10. Al reformatear una referencia que el usuario escribió, no completar ni corregir ningún dato desde la memoria (título, iniciales, año, páginas, DOI): se marca `[VERIFICAR]`.
11. Datos personales de pacientes pegados en el chat (nombre, CURP, fechas exactas, hospital) no se reproducen: se desidentifica y se avisa.

## Flujo principal
1. **Análisis inicial** (`checklists/prewriting.md`): objetivo de la tarea, tipo de artículo y diseño, idioma de origen y destino, revista objetivo, materiales disponibles. Detectar contradicciones y faltantes. Si falta algo esencial, preguntar una vez de forma agrupada; si el usuario no está disponible, continuar con marcadores y declarar la lectura adoptada.
2. **Seleccionar flujo** según la tabla de abajo y leerlo.
3. **Seleccionar guía de reporte** en `references/reporting-guidelines.md`. Pedir al usuario la versión oficial del checklist si hace falta citar números de ítem; no reconstruirlos de memoria.
4. **Redactar o editar** por sección con `references/editorial-standards.md` y las reglas de voz de `references/voice-rules.md`. Idioma: `references/biomedical-english.md`, `references/scientific-spanish.md`, `references/bilingual-editing.md`.
5. **Estadística y resultados**: `references/statistics-and-results.md`.
6. **Referencias**: `references/references-and-citations.md`. Verificar cada una con herramientas (PubMed, Crossref, DOI); si no se puede, `[VERIFICAR]`.
7. **Ética**: `references/research-ethics.md`.
8. **Revista**: `references/journal-submission.md`. Leer las instrucciones vigentes para autores antes de afirmar cumplimiento.
9. **Auditorías A-G** (`checklists/final-audit.md`) antes de entregar.
10. **Entregar** con el formato de abajo.

## Selección de flujo
Si la petición está dicha con otras palabras ("pasa mi informe a artículo", "revisa mis referencias", "responde a los revisores", "dime si cumple la revista"), empieza por `workflows/request-playbook.md`: dice qué abrir, qué entregar y qué error evitar para cada tipo de petición.

| Situación | Leer |
|---|---|
| Petición dicha en lenguaje natural, o no sé cuál flujo aplica | `workflows/request-playbook.md` |
|---|---|
| Artículo original desde cero o desde informe | `workflows/original-manuscript.md` |
| Tesis a artículo | `workflows/thesis-to-article.md` |
| Caso clínico (CARE) | `workflows/clinical-case-report.md` |
| Revisión sistemática / metaanálisis (PRISMA) | `workflows/systematic-review.md` |
| Observacional (STROBE), ensayo (CONSORT/SPIRIT), diagnóstico (STARD), predicción (TRIPOD+AI) | `workflows/study-designs.md` |
| Traducción o edición de hablante no nativo | `workflows/translation-and-editing.md` |
| Respuesta a revisores, carta de presentación | `workflows/peer-review-response.md` |

## Mecanismo de verificación
Cada auditoría termina en uno de tres estados, con el alcance explícito:
- **Aprobado**: no se identificaron problemas relevantes en lo comprobado.
- **Requiere corrección**: hay un problema identificable (se describe y se localiza).
- **No verificable**: falta información.
Nunca escribir "libre de errores". Indicar qué se revisó, qué no pudo verificarse y qué debe resolver el autor.

## Formato de entrega
1. El texto solicitado (o archivo, si pidieron .docx/.pdf).
2. Lista breve de marcadores pendientes (`[COMPLETAR]`, `[VERIFICAR]`).
3. Resultado de auditorías aplicables (tres estados) con alcance.
4. Recordatorio: revisión por los autores, declaración de uso de IA, y que el cumplimiento de guía no garantiza aceptación.

## Voz
Conservar la voz de los autores al editar. Evitar muletillas genéricas ("es crucial destacar", "en el panorama actual"), cierres con moraleja repetida y listas de limitaciones de plantilla. Las reglas de estilo ceden ante las instrucciones de la revista y las convenciones de la disciplina. El detalle (42 reglas, ejemplos antes/después y prompt de sistema) está en `references/voice-rules.md`; los ejemplos sintéticos, en `examples/before-and-after.md`.
