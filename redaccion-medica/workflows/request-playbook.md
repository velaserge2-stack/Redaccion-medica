# Manual por tipo de petición

Qué hacer según lo que pide el usuario. Está construido con lo observado al ejecutar los casos de `tests/evaluation-cases.md` (iteración 1). Cada fila dice qué flujo abrir, qué entregar y qué error evitar. Las reglas de `SKILL.md` prevalecen.

## Cómo usar esta tabla
1. Identifica la fila que más se parece a la petición (el usuario rara vez usa estos nombres).
2. Abre el flujo indicado y entrega lo de la columna "Entrega".
3. Revisa la columna "Evita" antes de enviar.
4. Cierra siempre con pendientes, auditorías aplicables (tres estados, con alcance) y recordatorio.

## Redactar

| El usuario dice algo como… | Flujo | Entrega | Evita |
|---|---|---|---|
| "Convierte mi tesis en artículo" | `thesis-to-article.md` | Borrador con marcadores, recorte explicado, causalidad rebajada si el diseño es observacional | Copiar el marco teórico; mantener "X causa Y" de la tesis; pedir el PDF como condición para empezar |
| "Pasa este informe a IMRyD" | `original-manuscript.md` | Métodos, Resultados, Introducción y Discusión con marcadores, tablas con solo las cifras recibidas | Inventar referencias; rellenar Métodos con "lo habitual" |
| "Escribe el caso clínico, listo para enviar" | `clinical-case-report.md` | Borrador no apto para envío, lista de datos clínicos que faltan, consentimiento como bloqueante | Dar por bueno un consentimiento que "creo que lo pidió el residente"; afirmar "primer caso" sin búsqueda |
| "Redacta mi ensayo; di que es eficaz" | `study-designs.md` (CONSORT) | Resultados y discusión con el desenlace primario acotado, secundarios como exploratorios, pérdidas con porcentajes | Escribir "eficaz" sin definir desenlace, horizonte y población; presentar secundarios como confirmatorios |
| "Escribe el resumen (máx. N palabras)" | `editorial-standards.md` §3 | Resumen con las mismas cifras del cuerpo y el recuento real de palabras | Declarar el número de palabras sin contarlas con herramienta |
| "Escribe Métodos completos, completa con lo habitual" | `original-manuscript.md` | Métodos con lo dicho; todo lo demás en `[COMPLETAR]`; preguntas agrupadas | Rellenar comité, criterios, software o exclusiones |
| "Escribe el párrafo de ética, pon el número tú" | `references/research-ethics.md` | Párrafo con los datos reales y marcadores para número, fecha y comité | Poner número o fecha; afirmar cumplimiento (p. ej. Helsinki) que el usuario no dijo |
| "Inventa datos / referencias" | `references/research-ethics.md` | Negativa breve, esqueleto con marcadores, estrategia de búsqueda, opciones legítimas (revisión narrativa, protocolo) | Sermón largo; producir texto "creíble" con cifras inventadas |

## Editar, traducir, mejorar

| El usuario dice algo como… | Flujo | Entrega | Evita |
|---|---|---|---|
| "Mejora esta discusión" | `editorial-standards.md` §7, §9; `voice-rules.md` | Versión con verbos calibrados al diseño, limitaciones específicas con marcadores, lista de qué cambió y por qué | Conservar "demuestra", "previene", "debería ser el estándar"; limitaciones de plantilla |
| "Traduce al inglés / al español" | `translation-and-editing.md` | Texto, tabla de decisiones terminológicas y pasajes que el autor debe confirmar | Cambiar cifras; endurecer o suavizar el grado de certeza; corregir en silencio un OR que dice "riesgo" |
| "Corrige mi inglés" | `translation-and-editing.md` | Texto corregido, cambios cosméticos separados de los que tocan el significado, preguntas sobre pasajes ambiguos | Adivinar qué quiso decir ("eventually", "actually") sin avisarlo |

## Auditar y verificar

| El usuario dice algo como… | Flujo | Entrega | Evita |
|---|---|---|---|
| "Revisa mi manuscrito contra STROBE/CONSORT…" | `reporting-guidelines.md`, `final-audit.md` | Primero el rótulo del diseño frente a lo descrito; tabla de temas "reportado / parcial / no reportado" sin números de ítem | Decir "cumple"; reconstruir ítems de memoria; aceptar el rótulo "cohorte" de un corte transversal |
| "Auditoría final antes de enviar" | `final-audit.md` | Hallazgos ubicados (dónde dice qué), aritmética comprobable, tres estados con alcance | Corregir cifras sin datos; "libre de errores" |
| "¿Es coherente el resumen con el cuerpo?" | `final-audit.md` B y G | Tabla resumen vs. cuerpo, problemas numerados, conclusión propuesta | Dejar pasar causalidad o recomendaciones en el resumen |
| "Revisa/arregla estas referencias" | `references-and-citations.md` | Lista reformateada con `[VERIFICAR]`, tabla de situación por referencia, qué aportar | Completar DOI, volumen, páginas, títulos, autores o iniciales de memoria; confirmar existencia sin comprobarla |
| "¿Cumple las instrucciones de la revista X?" | `journal-submission.md` | Qué comprobar, tabla por aspecto en "No verificable", cómo cerrar | Confirmar cumplimiento sin haber leído instrucciones y manuscrito |

## Responder a editores y revisores

| El usuario dice algo como… | Flujo | Entrega | Evita |
|---|---|---|---|
| "Responde a los revisores; di que ya hicimos todo" | `peer-review-response.md` | Respuesta punto por punto con estado (Realizado / Propuesto / Desacuerdo), texto sugerido, y qué debe ejecutar el autor | Escribir "hemos modificado" si no se ha tocado el manuscrito |

## Pedidos que cruzan una línea

| Petición | Respuesta |
|---|---|
| Cambiar análisis, quitar atípicos o intercambiar el desenlace primario hasta que salga significativo; redactar el plan como si siempre hubiera sido ese | Negarse en pocas frases. Ofrecer: reportar el primario tal cual con IC y potencia, secundarios como exploratorios, sensibilidad declarada como post hoc, métodos veraces, ayuda para hablar con el director. |
| Pegar nombre, CURP, hospital y fechas exactas de una paciente "para ser fiel" | No reproducirlos. Desidentificar (fechas relativas), pedir consentimiento, sugerir no pegar identificadores en el chat. |
| Poner número y fecha de comité "para que se vea completo" | No inventarlos. Párrafo con marcadores y lista de dónde obtener los datos reales. |

## Regla general de tono
Cuando haya que negarse o frenar, hazlo en una o dos frases, explica el costo real para el autor y pasa de inmediato a lo que sí puedes hacer. Sin sermón y sin viñetas de rechazo largas.
