# Entender el contexto de la investigación

Antes de escribir una sola frase del manuscrito hay que entender **qué investigación es, qué encontró y qué ya se sabe del tema**. La mayoría de los errores graves de un borrador (conclusión causal en un transversal, introducción que no lleva a la pregunta, discusión que compara con estudios que no existen) nacen de redactar sin este paso.

Este archivo se usa en el paso 1 del flujo principal y siempre que el usuario suba material nuevo.

## 1. Leer todo lo que el usuario aportó

Orden de lectura recomendado:
1. **Material propio del estudio**: protocolo, tesis, base de resultados, salidas estadísticas, tablas, figuras, manuscrito previo, dictamen del comité.
2. **Artículos que el usuario subió** (PDF, texto o enlaces): son la base bibliográfica primaria. Leerlos completos si es posible, no solo el resumen.
3. **Instrucciones de la revista** si las adjuntó.
4. Comentarios de revisores, si existen.

Si un archivo no se puede abrir o está incompleto (PDF escaneado, tabla cortada), decirlo de inmediato; no suponer su contenido.

### Cómo leer cada formato
| Formato | Cómo leerlo |
|---|---|
| PDF | Leer el texto completo con la lectura de PDF disponible (skill o herramienta de PDF, o `pdftotext -layout`). En PDF largos, leer por páginas hasta el final, incluidas tablas y referencias. Si es escaneado (sin texto), avisar o usar OCR si está disponible. |
| Word (.docx) | Usar el skill o herramienta de .docx disponible (o `pandoc archivo.docx -t markdown`). Revisar también tablas, notas al pie, comentarios y control de cambios: pueden contener datos o referencias. |
| Markdown (.md) / texto | Leer directamente, completo. |
| Hojas de cálculo (.xlsx, .csv) | Leer con la herramienta de hojas de cálculo; las cifras se toman de ahí, sin redondear de nuevo. |

Al terminar, decir qué archivos se leyeron y si alguno se leyó solo en parte.

## 1b. Banco de citas de los archivos subidos

Mientras se leen los archivos, extraer **todas las citas y listas de referencias** que contienen (de la tesis, del manuscrito previo, de los artículos de referencia) a una tabla:

| # | Cita tal como aparece en el archivo | Archivo de origen (y página o sección) | DOI / PMID si aparece | ¿Se usa en el manuscrito? ¿Para qué frase? | Estado (verificada / `[VERIFICAR]`) |
|---|---|---|---|---|---|

Reglas:
- La cita se copia **tal como viene en el archivo**; solo se cambia el formato al estilo de la revista. No se completan datos faltantes de memoria (regla 12 de `SKILL.md`).
- Al final, **la lista de referencias del manuscrito se construye con este banco**. Cada afirmación bibliográfica del texto se respalda primero con una cita del banco.
- Si una cita del banco no respalda la frase donde se quiere usar (otra población, otro desenlace), no se usa ahí.
- Si los archivos no cubren una afirmación, se marca `[CITA]` o se propone una referencia de búsqueda propia, rotulada aparte como "recuperada por búsqueda", para que el autor decida.
- Si hay herramientas, comprobar existencia y metadatos de las citas del banco (`scripts/verificar_referencias.py`, PubMed, Crossref); las no comprobadas quedan `[VERIFICAR]`.

## 2. Ficha de contexto (se construye, no se inventa)

Llenar cada campo **solo con lo que consta en el material**, indicando de dónde salió. Lo que no consta queda como `[COMPLETAR]`.

| Campo | Contenido | Origen (archivo, página, tabla) |
|---|---|---|
| Pregunta de investigación | | |
| PICO / PECO (población, intervención o exposición, comparador, desenlace) | | |
| Diseño **real** (no el rótulo del autor) | | |
| Escenario, país, periodo | | |
| N y flujo de participantes | | |
| Desenlace primario y cómo se midió | | |
| Análisis principal (modelo, ajuste, software) | | |
| Hallazgo principal con su medida de efecto e IC | | |
| Hallazgos secundarios / exploratorios | | |
| Limitaciones que el propio material reconoce | | |
| Ética, consentimiento, registro, financiamiento | | |
| Revista objetivo y tipo de artículo | | |
| Lo que el autor quiere afirmar | | |
| ¿Lo que quiere afirmar cabe en el diseño y los datos? | Sí / Parcialmente / No (explicar) | |

La última fila es la más importante: si el autor quiere afirmar algo que el diseño no permite, se avisa **antes** de redactar.

## 3. Mapa del conocimiento previo

Para escribir la introducción y la discusión hace falta saber qué hay publicado. Se construye con:
- los artículos que subió el usuario, y
- una búsqueda propia en bases indexadas (ver `workflows/evidence-search.md`) cuando las herramientas estén disponibles en la sesión.

Resultado: una **matriz de evidencia** (plantilla en `evidence-search.md`) con cada estudio relevante: autor, año, diseño, población, n, hallazgo principal, cómo se obtuvo (subido / PubMed / Consensus) y nivel de lectura (texto completo / solo resumen).

Con la matriz se responden tres preguntas:
1. ¿Qué se sabe con solidez? (revisiones sistemáticas, ensayos, cohortes grandes)
2. ¿Dónde está la brecha que este estudio cubre? Debe ser una brecha **real y verificable** en la matriz, no "existen pocos estudios" por intuición.
3. ¿Con qué estudios concretos se comparan los resultados en la discusión? ¿Coinciden o discrepan, y por qué podría ser (población, diseño, definición del desenlace)?

## 4. Detectar contradicciones y faltantes

Revisar antes de redactar:
- Cifras que no coinciden entre tesis, tablas y texto.
- Diseño rotulado distinto del descrito (p. ej., "cohorte" sin seguimiento).
- Objetivo que no corresponde con el análisis realizado.
- Desenlace primario cambiado respecto al protocolo o al registro.
- Referencias del usuario que no respaldan la frase donde están citadas.

Se listan con ubicación y se pregunta. No se resuelven "eligiendo la cifra que parece correcta".

## 5. Preguntar una vez, de forma agrupada

Si faltan datos esenciales, hacer **una sola** ronda de preguntas, numeradas y agrupadas (datos del estudio / ética / revista / referencias). Si el usuario no está disponible o pide avanzar, continuar con marcadores y declarar la lectura adoptada ("Asumí que el diseño es transversal porque no hay seguimiento; confírmalo").

## 6. Señales de que se está perdiendo el contexto (detenerse)

- Se está escribiendo una frase de la introducción sin una fuente concreta detrás.
- La discusión menciona "estudios previos" que no están en la matriz.
- Aparece una cifra en el texto que no está en ningún archivo del usuario.
- El borrador "suena bien" pero no se puede señalar de dónde salió cada afirmación.

En cualquiera de estos casos: volver a la ficha y a la matriz, o marcar `[CITA: …]` / `[COMPLETAR: …]`.
