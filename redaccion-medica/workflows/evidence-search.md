# Búsqueda y uso de evidencia: solo fuentes reales y trazables

Principio: **todo lo que el manuscrito afirma sobre la literatura sale de un artículo que se tuvo delante** (subido por el usuario o recuperado en esta sesión de una base indexada). Nada sale de la memoria del modelo. La memoria sirve para saber *qué buscar*, no para *qué escribir*.

## 1. Jerarquía de fuentes

| Prioridad | Fuente | Uso |
|---|---|---|
| 1 | **Artículos que subió el usuario** | Base primaria. Se leen antes de buscar. |
| 2 | **PubMed / MEDLINE** (pubmed.ncbi.nlm.nih.gov) | Existencia, PMID, metadatos, resumen, tipo de publicación, retractaciones. |
| 3 | **Consensus** (si la herramienta está conectada) | Búsqueda semántica sobre artículos revisados por pares (Semantic Scholar, OpenAlex, PubMed). Útil para mapear el tema y encontrar estudios; cada resultado se confirma después en PubMed o por DOI. |
| 4 | **Europe PMC / PubMed Central** | Texto completo de acceso abierto. |
| 5 | **Crossref / doi.org** | Confirmar DOI y metadatos. |
| 6 | **Cochrane Library** | Revisiones sistemáticas. |
| 7 | **ClinicalTrials.gov / WHO ICTRP** (si hay herramienta) | Registro de ensayos, desenlaces registrados vs. publicados. |
| 8 | **LILACS / SciELO / BVS** | Literatura latinoamericana en español y portugués. |
| 9 | Sitios oficiales de guías (OMS, sociedades, NICE, CDC, Secretaría de Salud, etc.) | Guías de práctica clínica y datos epidemiológicos oficiales. |

No usar como fuente de afirmaciones: blogs, Wikipedia, notas de prensa, sitios comerciales, revistas predatorias, resúmenes generados por IA (incluido el resumen que devuelve un buscador semántico: se lee el artículo o su resumen original).

## 2. Qué hacer según las herramientas disponibles

| Situación en la sesión | Qué hacer |
|---|---|
| Hay herramienta de Consensus, PubMed o búsqueda web | Buscar, abrir el registro, extraer los datos a la matriz, citar. |
| Solo hay artículos subidos | Usar solo esos. Lo que no cubran → `[CITA: tema, tipo de estudio esperado]` y estrategia de búsqueda para que el autor la ejecute. |
| No hay herramientas ni artículos | No escribir afirmaciones bibliográficas. Entregar la estrategia de búsqueda (términos MeSH/DeCS, cadena booleana) y marcadores `[CITA]`. |
| La herramienta falla o está bloqueada | Decirlo explícitamente ("No pude acceder a PubMed en esta sesión"); no completar con memoria. |

Para verificar en lote DOI y PMID de una lista de referencias, usar `scripts/verificar_referencias.py` cuando la sesión tenga acceso a internet (ver el encabezado del script).

## 3. Procedimiento de búsqueda

1. **Pregunta**: formular en PICO/PECO a partir de la ficha de contexto (`research-context.md`).
2. **Términos**: descriptores MeSH (inglés) y DeCS (español/portugués) más sinónimos en texto libre. Comprobar los descriptores en el MeSH Browser o DeCS si es posible.
3. **Cadena**: ejemplo de estructura (no copiar los términos, adaptarlos):
   `("Termino MeSH"[Mesh] OR sinonimo1[tiab] OR sinonimo2[tiab]) AND ("Desenlace"[Mesh] OR desenlace[tiab]) AND (filtro de diseño)`
4. **Búsqueda semántica (Consensus)**: preguntas en lenguaje natural ("¿Se asocia X con Y en adultos con Z?"). Sin filtros salvo que el usuario los pida. Revisar los primeros resultados y anotar los relevantes.
5. **Registro** de cada búsqueda: fuente, fecha, cadena o pregunta, filtros, número de resultados, cuántos se revisaron.
6. **Selección**: priorizar revisiones sistemáticas recientes, ensayos, cohortes grandes y guías vigentes. Anotar el tipo de estudio. Revisar si hay retractación o corrección.
7. **Lectura**: abrir al menos el resumen original; el texto completo si se va a citar una cifra concreta, un método o una limitación.
8. **Extraer a la matriz** (abajo) antes de redactar.

## 4. Matriz de evidencia (plantilla)

| # | Autor principal, año | Revista | DOI / PMID | Diseño | Población y n | Hallazgo principal (cifra con IC si se citará) | Cómo se obtuvo | Nivel de lectura | ¿Respalda qué frase del manuscrito? |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | Subido / PubMed / Consensus / Europe PMC | Texto completo / Solo resumen | |

Reglas de la matriz:
- Cada celda se llena **con lo que se vio en la fuente**. Si no se vio, queda vacía o `[VERIFICAR]`.
- Si solo se leyó el resumen, no se citan detalles que no estén en el resumen.
- Un estudio que no se pudo confirmar en ninguna base no entra en la matriz.

## 5. De la matriz al texto

- Cada frase con contenido bibliográfico lleva su número de matriz durante la redacción (p. ej., `[M3]`), que luego se convierte en la cita del estilo de la revista.
- Citar con precisión: "En una cohorte de [n] adultos de [país], [Autor] et al. observaron [hallazgo] [cita]". Solo con datos que estén en la matriz.
- Sintetizar, no enumerar: agrupar estudios que coinciden y explicar las discrepancias (diseño, población, definición).
- **Prohibido**: afirmaciones del tipo "numerosos estudios han demostrado" sin las citas concretas; atribuir a un artículo algo que no dice; citar un artículo porque "suele citarse" sin haberlo comprobado.

## 6. Informe de búsqueda que se entrega al usuario

Al final de la entrega, si se buscó literatura:
- Fuentes consultadas y fecha.
- Cadenas o preguntas usadas.
- Estudios incluidos (matriz) y nivel de lectura de cada uno.
- Afirmaciones que quedaron sin fuente (`[CITA: …]`) y sugerencia de búsqueda.
- Advertencia: la búsqueda es de apoyo a la redacción, **no es una búsqueda sistemática** salvo que se haya seguido PRISMA-S con protocolo.

## 7. Errores que este archivo evita

| Error | Ejemplo | Corrección |
|---|---|---|
| Referencia de memoria | Escribir "Smith et al., 2019, NEJM" porque "suena" correcto | Buscar; si no se encuentra, `[CITA]` |
| Cita que no respalda | Citar una revisión sobre adultos para una frase sobre niños | Comprobar población y desenlace en la fuente |
| Cifra mal atribuida | Copiar un OR del resumen de Consensus en vez del artículo | Ir al resumen original o al texto completo |
| Fuente retractada | Citar un artículo retirado | Revisar tipo de publicación en PubMed ("Retracted Publication") |
| Brecha inventada | "No existen estudios en Latinoamérica" sin buscar en LILACS/SciELO | Buscar o formular con cautela y fecha de búsqueda |
