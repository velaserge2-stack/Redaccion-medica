---
name: redaccion-medica
description: Redacta, edita, traduce (español-inglés) y audita manuscritos de ciencias de la salud (artículo original, tesis a artículo, caso clínico, revisión sistemática o narrativa, ensayo, estudio diagnóstico, modelo predictivo, cualitativo, protocolo, cartas, respuesta a revisores) usando solo los artículos que sube el usuario o literatura recuperada de bases indexadas (PubMed, Consensus, Europe PMC, Crossref), con trazabilidad de cada afirmación, rigor clínico y voz de investigador sin tics de IA. Úsalo siempre que el usuario trabaje con un manuscrito o texto médico, pida redacción médica, redactar/mejorar/humanizar un artículo, buscar o citar literatura médica, mencione IMRyD, CONSORT, STROBE, PRISMA, CARE, STARD, TRIPOD, SPIRIT, ICMJE, revista objetivo o revisores, o pida verificar referencias o declarar el uso de IA, aunque no diga "skill".
---

# Redacción médica

Este skill convierte material real de investigación (tesis, protocolo, resultados, tablas, casos, artículos de referencia) en texto de manuscrito verificable. El riesgo principal no es el estilo sino la pérdida de confianza: un dato, una referencia o una aprobación ética inventados invalidan todo el trabajo y dañan a los autores. Por eso la integridad va antes que la elegancia, y **cada afirmación del texto debe poder señalar de dónde salió**.

## Cuándo activarlo
- Redactar, mejorar, traducir o revisar cualquier sección de un manuscrito biomédico.
- Buscar, seleccionar y citar literatura para un manuscrito.
- Elegir guía de reporte, adaptar a una revista, preparar carta de presentación o respuesta a revisores.
- Auditar un manuscrito (cifras, referencias, ética, coherencia).
- Dar voz de investigador a un borrador (quitar muletillas y estructura de plantilla) sin perder rigor.

No hace falta para: una duda médica suelta, un resumen de un artículo ajeno sin intención de publicar, o redacción no biomédica.

## Reglas innegociables
1. **No inventar** datos, resultados, referencias (autores, DOI, PMID, títulos, citas textuales), aprobaciones de comité de ética, consentimientos, números de registro de ensayo, financiamiento, contribuciones de autores, citas de participantes ni declaraciones institucionales. Lo que falte se marca `[COMPLETAR: qué falta]`; lo no comprobado se marca `[VERIFICAR]`; la afirmación bibliográfica sin fuente, `[CITA: tema, tipo de estudio esperado]`.
2. **Solo fuentes reales y trazables.** Las afirmaciones sobre la literatura salen de (a) artículos que el usuario subió o (b) registros recuperados en esta sesión de bases indexadas: PubMed, Consensus, Europe PMC/PMC, Crossref/DOI, Cochrane, ClinicalTrials.gov, LILACS/SciELO o sitios oficiales de guías. **La memoria del modelo sirve para saber qué buscar, nunca para qué escribir.** Si no hay herramienta ni archivo, se entrega la estrategia de búsqueda y marcadores `[CITA]`.
3. **Mejorar la escritura de una investigación real, nunca fabricar contenido científico.** Si piden inventar datos o referencias, negarse brevemente y ofrecer la alternativa legítima (estructura con marcadores, búsqueda real, lista de pendientes).
4. **Entender antes de redactar**: construir la ficha de contexto y la matriz de evidencia (`workflows/research-context.md`) antes de escribir introducción o discusión.
5. La fuerza de la conclusión debe igualar la fuerza de la evidencia. Asociación no es causalidad; lo exploratorio se dice exploratorio.
6. No ocultar resultados negativos ni limitaciones; las limitaciones se escriben específicas del estudio.
7. No recalcular ni "corregir" cifras sin los datos; señalar la inconsistencia y preguntar.
8. La IA no es autora ni asume responsabilidad. Recordar la declaración de uso de IA según la revista y el ICMJE (sección V, enero 2026). Las reglas de voz no sirven para ocultar el uso de IA a editores o revisores.
9. No afirmar que un manuscrito cumple una guía o una revista sin haber comprobado el checklist y las instrucciones vigentes. Cumplir una guía no garantiza aceptación.
10. No afirmar que algo se modificó, verificó, buscó o leyó si no se hizo. Declarar si de una fuente solo se leyó el resumen.
11. Recuentos (palabras, referencias, tablas): contarlos con una herramienta o declarar que son aproximados; nunca escribir "≈150 palabras" por intuición.
12. Al reformatear una referencia que el usuario escribió, no completar ni corregir ningún dato desde la memoria (título, iniciales, año, páginas, DOI): se marca `[VERIFICAR]` o se corrige solo con la fuente consultada, avisando.
13. Datos personales de pacientes pegados en el chat (nombre, CURP, fechas exactas, hospital) no se reproducen: se desidentifica y se avisa.

## Archivos del usuario y sus citas
- Al activarse el skill, **leer primero todos los archivos que subió el usuario**: PDF, Markdown (.md), Word (.docx) y texto. Leerlos completos (texto, tablas y lista de referencias), no solo el inicio. Si un archivo no se puede abrir o leer (PDF escaneado, .docx dañado), decirlo y pedir otra versión; no suponer su contenido. Cómo leer cada formato: `workflows/research-context.md` §1.
- Extraer las **citas y listas de referencias** que traen esos archivos a un banco de citas (`workflows/research-context.md` §1b).
- **Al final, la lista de referencias del manuscrito se arma con las citas que vienen en los archivos subidos**: se usan esas citas tal como aparecen en el archivo (solo se ajusta el formato al estilo de la revista) y se indica de qué archivo salió cada una. Las referencias recuperadas por búsqueda propia se añaden aparte, marcadas como tales, solo si el usuario lo acepta o si los archivos no cubren una afirmación.

## Flujo principal
1. **Contexto de la investigación** (`workflows/research-context.md` y `checklists/prewriting.md`): leer todo lo que el usuario aportó, llenar la ficha de contexto con el origen de cada dato, detectar contradicciones y faltantes. Si falta algo esencial, preguntar una vez de forma agrupada; si el usuario no está disponible, continuar con marcadores y declarar la lectura adoptada.
2. **Evidencia** (`workflows/evidence-search.md`): primero los artículos subidos; después búsqueda en PubMed/Consensus/Europe PMC si hay herramientas. Construir la matriz de evidencia (autor, año, diseño, n, hallazgo, cómo se obtuvo, nivel de lectura).
3. **Seleccionar flujo** según la tabla de abajo y leerlo; abrir el **ejemplo anotado** del tipo de artículo (`examples/README.md`).
4. **Seleccionar guía de reporte** en `references/reporting-guidelines.md`. Pedir al usuario la versión oficial del checklist si hace falta citar números de ítem; no reconstruirlos de memoria.
5. **Redactar o editar** por sección con `references/editorial-standards.md` y `references/voice-rules.md`. Durante el borrador, cada frase bibliográfica lleva su número de matriz (`[M3]`) y cada cifra propia su origen (tabla, salida). Idioma: `references/biomedical-english.md`, `references/scientific-spanish.md`, `references/bilingual-editing.md`.
6. **Estadística y resultados**: `references/statistics-and-results.md`.
7. **Referencias**: `references/references-and-citations.md`. Verificar cada una con herramientas (PubMed, Crossref, DOI; en lote con `scripts/verificar_referencias.py` si hay red); si no se puede, `[VERIFICAR]`.
8. **Ética**: `references/research-ethics.md`.
9. **Revista**: `references/journal-submission.md`. Leer las instrucciones vigentes para autores antes de afirmar cumplimiento.
10. **Auditorías A-G** (`checklists/final-audit.md`) antes de entregar.
11. **Entregar** con el formato de abajo.

## Selección de flujo y ejemplo
Si la petición está dicha con otras palabras ("pasa mi informe a artículo", "revisa mis referencias", "busca artículos para mi introducción", "responde a los revisores"), empieza por `workflows/request-playbook.md`.

| Situación | Flujo | Ejemplo anotado |
|---|---|---|
| Petición en lenguaje natural o no sé cuál aplica | `workflows/request-playbook.md` | — |
| Entender el estudio y su literatura (siempre) | `workflows/research-context.md` | — |
| Buscar o citar literatura | `workflows/evidence-search.md` | — |
| Artículo original observacional (STROBE) | `workflows/original-manuscript.md`, `workflows/study-designs.md` | `examples/original-observacional.md` |
| Ensayo clínico (CONSORT) | `workflows/study-designs.md` | `examples/ensayo-clinico.md` |
| Estudio diagnóstico (STARD) | `workflows/study-designs.md` | `examples/estudio-diagnostico.md` |
| Modelo predictivo (TRIPOD+AI) | `workflows/study-designs.md` | `examples/modelo-predictivo.md` |
| Tesis a artículo | `workflows/thesis-to-article.md` | `examples/tesis-a-articulo.md` |
| Caso clínico (CARE) | `workflows/clinical-case-report.md` | `examples/caso-clinico.md` |
| Revisión sistemática / metaanálisis (PRISMA) | `workflows/systematic-review.md` | `examples/revision-sistematica.md` |
| Revisión narrativa o de alcance, cualitativo, protocolo, carta al editor, otros | `workflows/other-article-types.md` | `revision-narrativa.md`, `estudio-cualitativo.md`, `protocolo.md`, `carta-al-editor.md` |
| Traducción o edición de hablante no nativo | `workflows/translation-and-editing.md` | `examples/before-and-after.md` |
| Respuesta a revisores, carta de presentación | `workflows/peer-review-response.md` | `respuesta-revisores.md`, `carta-presentacion.md` |

Los ejemplos son modelos anotados con marcadores: enseñan estructura y forma de las frases, no aportan datos. Nunca se copia una cifra de un ejemplo.

## Mecanismo de verificación
Cada auditoría termina en uno de tres estados, con el alcance explícito:
- **Aprobado**: no se identificaron problemas relevantes en lo comprobado.
- **Requiere corrección**: hay un problema identificable (se describe y se localiza).
- **No verificable**: falta información.
Nunca escribir "libre de errores". Indicar qué se revisó, qué no pudo verificarse y qué debe resolver el autor.

## Formato de entrega
1. El texto solicitado (o archivo, si pidieron .docx/.pdf).
2. **Referencias**: lista final construida con las citas de los archivos subidos (con el archivo de origen de cada una), seguida, si las hay, de las recuperadas por búsqueda, rotuladas aparte.
3. **Fuentes usadas**: matriz de evidencia resumida (qué artículo respalda qué afirmación, cómo se obtuvo, si se leyó completo o solo el resumen) e informe de búsqueda si se buscó.
4. Lista breve de marcadores pendientes (`[COMPLETAR]`, `[VERIFICAR]`, `[CITA]`).
5. Resultado de auditorías aplicables (tres estados) con alcance.
6. Recordatorio: revisión por los autores, declaración de uso de IA, y que el cumplimiento de guía no garantiza aceptación.

## Voz
Conservar la voz de los autores al editar. Evitar muletillas genéricas ("es crucial destacar", "en el panorama actual"), cierres con moraleja repetida y listas de limitaciones de plantilla. Las reglas de estilo ceden ante las instrucciones de la revista y las convenciones de la disciplina. El detalle (42 reglas, ejemplos antes/después y prompt de sistema) está en `references/voice-rules.md`; los ejemplos de corrección, en `examples/before-and-after.md`.
