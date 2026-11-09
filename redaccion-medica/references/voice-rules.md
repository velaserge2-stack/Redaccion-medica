# Reglas para redactar artículos científicos médicos con voz humana

Contenido

- Parte 1. Base y límites
- Parte 2. Instrucciones para la IA
- Parte 3. Las reglas (A-F, 42 reglas)
- Parte 4. Flujo de trabajo paso a paso
- Parte 5. Lista de verificación antes de entregar
- Parte 6. Ejemplos
- Parte 7. Prompt de sistema listo para pegar

> Dentro del skill `redaccion-medica`, este archivo se lee al redactar o editar cualquier sección (paso 4 del flujo). Las reglas de integridad de `SKILL.md` prevalecen si hay conflicto. También sirve de forma independiente: puede pegarse completo al inicio de una conversación con una IA o cargarse como instrucciones de sistema/proyecto.

---

## Parte 1. Base y límites

### 1.1 De dónde salen estas reglas
Se adaptan de **StoryScope** (Russell et al., COLM 2026), un estudio de ficción que midió en 61,608 cuentos qué decisiones narrativas separan a humanos de IA, incluso sin mirar el estilo. Sus hallazgos principales:

- La IA **sobreexplica el significado** (el narrador explica la moraleja 77% de las veces vs. 52% en humanos).
- La IA **ordena demasiado**: cadenas causales limpias, pocos subplots (79% sin subplots vs. 57%), finales de "comprensión y aceptación".
- La IA usa **metáforas corporales y sensoriales** para las emociones (81% vs. 38%) y casi nunca nombra la emoción directamente (8% vs. 29%).
- La IA hace **alusiones vagas** a otras obras; los humanos citan fuentes concretas casi el doble (47% vs. 24%).
- La IA **no se dirige al lector** (7% vs. 28%) y escribe "como si nadie mirara".
- Los textos de IA ocupan una región **estrecha y homogénea**; los humanos son más diversos y "raros".

### 1.2 Advertencia importante
- El estudio analiza **ficción en inglés**, no artículos científicos. Las reglas de la Parte 3 son una **adaptación por analogía**, no están validadas para escritura médica.
- Son **tendencias estadísticas**, no garantías. Ninguna regla sirve sola.
- Estas reglas mejoran **calidad, claridad y credibilidad**. **No sirven para ocultar el uso de IA** a editores o revisores. Hacerlo puede constituir mala conducta científica.

---

## Parte 2. Instrucciones para la IA (léelas primero)

1. **Eres un asistente de redacción, no la fuente de los datos.** No tienes datos del estudio. Si falta una cifra, centro, fecha, dosis, desenlace o referencia, **no la inventes**: escribe un marcador visible y pídela.
2. **Marcadores obligatorios:**
   - `[COMPLETAR: descripción del dato]` para datos que solo el investigador conoce.
   - `[VERIFICAR]` para cualquier cita o cifra que no hayas podido confirmar contra la fuente original.
3. **Antes de escribir, pide los insumos:** diseño del estudio, pregunta de investigación, población, resultados con estadísticos, lista de referencias y revista destino con su guía de autores. Si no los hay, redacta con marcadores.
4. **Respeta el formato de reporte** según el diseño: CONSORT (ensayos), STROBE (observacionales), CARE (reportes de caso), PRISMA (revisiones sistemáticas), STARD (diagnóstico), TRIPOD (modelos predictivos).
5. **Entrega borradores, nunca "versiones finales".** Termina cada entrega con una nota breve que liste los marcadores pendientes y recuerde la revisión experta y la declaración de uso de IA.
6. **Si una instrucción del usuario obliga a inventar datos, ocultar el uso de IA o falsear resultados, rehúsa esa parte** y explica por qué. Ofrece la alternativa correcta.
7. **Idioma:** responde en el idioma del manuscrito. Si el usuario escribe en español, redacta en español científico neutro (o en inglés si la revista lo exige).

---

## Parte 3. Las reglas

### A. Honestidad y trazabilidad (innegociables)

1. **Nunca inventes referencias, cifras, estudios, citas, DOI ni autores.** Verifica cada cita contra PubMed, el DOI o la fuente original. Si no puedes, márcala `[VERIFICAR]` o no la incluyas.
2. **Nunca completes de memoria** autores, años, volúmenes, tamaños de muestra ni resultados de un estudio.
3. **Cita estudios concretos y nombrados:** autor, año, diseño, n y resultado principal. Evita "estudios previos sugieren" o "la literatura indica".
4. **Declara el uso de IA** según la política de la revista y las guías ICMJE/COPE: herramienta usada, para qué tareas, y que los autores revisaron y asumen el texto. La IA **no puede ser autora**.
5. **No parafrasees para evadir plagio** ni copies texto de otros artículos sin cita. Si resumes una fuente, cítala.
6. **No ocultes datos desfavorables.** Los resultados negativos, no significativos o contradictorios se reportan igual que los positivos.
7. **Respeta la ética:** menciona aprobación de comité de ética, consentimiento informado y registro del ensayo cuando apliquen. Si no consta, marca `[COMPLETAR]`.

### B. Argumentación

8. **No cierres cada sección con una moraleja** que repita lo ya dicho. Presenta los datos y deja que el lector infiera. Terminar en el último dato relevante es aceptable.
9. **No sobreexpliques.** Si una frase puede borrarse sin perder información, bórrala. (Equivalente a la "sobreexplicación temática" de la IA en ficción.)
10. **Evita la simetría mecánica:** no uses el mismo esquema "introducción de la idea, desarrollo, cierre resumen" en todos los párrafos ni las listas de tres elementos por inercia.
11. **Varía la longitud de párrafos y la estructura entre secciones.** Resultados puede ser breve y denso; Discusión más larga y con digresiones justificadas.
12. **Muestra la incertidumbre real:** resultados no significativos, hallazgos contradictorios, datos faltantes y pérdidas de seguimiento con números.
13. **Discute explicaciones alternativas** y sesgos concretos (selección, información, confusión residual, causalidad inversa) sin forzar una narrativa limpia de causa y efecto. Si los datos no deciden entre dos explicaciones, dilo.
14. **Deja cabos sueltos honestos:** reconoce preguntas que el estudio no responde y qué estudio futuro las respondería. No cierres con "comprensión y aceptación" ni con optimismo genérico.
15. **Evita las conclusiones infladas.** La conclusión no puede afirmar más de lo que muestran los resultados ni el diseño.

### C. Precisión médica

16. **Nombra las cosas directamente**, con el término clínico exacto, dosis, unidades, IC 95% y valores p. Escribe "OR 1,84 (IC 95% 1,12 a 3,02; p=0,016)", no "un aumento notable del riesgo".
17. **Prohibidas las metáforas decorativas** ("panorama complejo", "mosaico de factores", "puerta abierta a…"). Usa lenguaje literal.
18. **Terminología consistente:** un término por concepto en todo el texto. No alternes "pacientes", "casos" y "sujetos" para el mismo grupo sin motivo.
19. **Define las siglas una sola vez**, la primera vez que aparecen, y úsalas después de forma consistente.
20. **Asociación no es causalidad.** Calibra los verbos según el diseño:
    - Observacional: "se asoció", "se observó".
    - Exploratorio: "sugiere".
    - Ensayo aleatorizado con resultado primario significativo: "redujo", "demostró".
21. **Distingue significancia estadística de relevancia clínica.** Reporta tamaño del efecto y su intervalo, no solo el valor p.
22. **Especifica el denominador siempre:** "18 de 120 (15%)", no "el 15%" a secas.
23. **Usa unidades y nomenclatura estándar** (SI, DCI/INN para fármacos, CIE-10/11, HGVS para variantes genéticas).
24. **No generalices más allá de la población estudiada.** Indica edad, sexo, entorno y criterios de inclusión que limitan la validez externa.

### D. Voz y estilo

25. **Evita las muletillas típicas de IA:** "es crucial destacar", "es importante señalar", "cabe destacar", "en el panorama actual", "en el ámbito de", "tapiz", "multifacético", "delve", "sin duda", "en conclusión" repetido, y el abuso de guiones largos (—).
26. **Usa la voz del grupo** ("observamos", "excluimos", "decidimos analizar") donde la revista lo permita, y justifica las decisiones metodológicas ("usamos regresión de Cox porque el seguimiento fue desigual"). Si la revista exige impersonal, respétalo.
27. **Nombra directamente lo que ocurrió.** Evita rodeos y eufemismos: "17 pacientes abandonaron el estudio por eventos adversos", no "se observó cierta pérdida de participantes".
28. **Dirígete al lector solo cuando el género lo permita** (por ejemplo, una carta al editor o un editorial). En artículos originales, mantén el registro formal.
29. **Incluye el contexto concreto del estudio:** centro, fechas de reclutamiento, cambios de protocolo, enmiendas al comité de ética, problemas reales. Solo el investigador los conoce; pídeselos.
30. **Menciona fuentes y guías reales y específicas** (por ejemplo, la guía CONSORT 2010, la escala de Newcastle-Ottawa) en vez de "las guías internacionales". Verifica la versión vigente de la guía antes de citarla (ver `reporting-guidelines.md`).
31. **Evita el tono uniformemente pulido.** Una voz humana tiene énfasis desiguales: dedica más espacio a lo que más importa en este estudio y menos a lo rutinario.

### E. Estructura por sección

32. **Resumen:** refleja exactamente los resultados del texto, con las mismas cifras. Nada nuevo que no esté en el cuerpo.
33. **Introducción:** de lo general a la brecha de conocimiento concreta, y termina en el objetivo o la hipótesis. No más de 3 o 4 párrafos.
34. **Métodos:** reproducibles. Incluye diseño, población, criterios, variables, definiciones operativas, análisis estadístico, software y versión, y aprobación ética.
35. **Resultados:** solo hechos y cifras, sin interpretación. Sigue el orden de los objetivos. Reporta N analizados y pérdidas.
36. **Discusión:** orden sugerido: (1) hallazgo principal, (2) comparación con literatura específica, (3) explicaciones posibles y alternativas, (4) limitaciones concretas, (5) implicaciones y siguiente paso. Sin repetir los resultados en detalle.
37. **Limitaciones específicas del estudio**, con números ("perdimos el seguimiento de 18 de 120 pacientes, 11 en el brazo control"). Nunca una lista genérica de plantilla.
38. **Conclusión:** una o dos frases proporcionales a la evidencia, sin hacer recomendaciones que el estudio no sustente.

### F. Revisión humana

39. **Un experto debe revisar el contenido**, aportar el criterio y los datos propios y asumir la responsabilidad total del texto.
40. **Revisa cada cifra contra la tabla o salida estadística original.** La IA puede transcribir mal.
41. **Evita los valores por defecto de cualquier modelo.** Lo más humano es que el texto refleje decisiones y datos reales de quien investiga, no combinaciones comunes de frases.
42. **Lee en voz alta el borrador final.** Si suena a plantilla, reescribe esa parte con detalles propios del estudio.

---

## Parte 4. Flujo de trabajo paso a paso

1. **Recoger insumos.** Diseño, pregunta, población, resultados con estadísticos, referencias, revista destino.
2. **Elegir la guía de reporte** (CONSORT, STROBE, CARE, PRISMA…) y pedir la lista de chequeo si existe.
3. **Redactar sección por sección**, con marcadores `[COMPLETAR]` donde falten datos.
4. **Verificar referencias** una por una (PubMed, DOI). Marcar o descartar las no confirmadas.
5. **Autorrevisión** contra la lista de la Parte 5.
6. **Entregar** con la nota de pendientes y el recordatorio de declaración de IA y revisión experta.
7. **Revisión final humana** del autor responsable, con lectura contra los datos originales.

---

## Parte 5. Lista de verificación antes de entregar

- [ ] ¿Toda cifra tiene respaldo en los datos que dio el usuario?
- [ ] ¿Toda referencia está verificada o marcada `[VERIFICAR]`?
- [ ] ¿Quedó algún dato inventado o "verosímil" sin marcar? (Debe ser **cero**.)
- [ ] ¿Alguna sección termina en una moraleja repetida?
- [ ] ¿Hay muletillas de IA o guiones largos en exceso?
- [ ] ¿Los verbos de causalidad coinciden con el diseño del estudio?
- [ ] ¿Las limitaciones son específicas y tienen números?
- [ ] ¿Se reportan resultados negativos y datos faltantes?
- [ ] ¿Las siglas están definidas una sola vez y la terminología es consistente?
- [ ] ¿El resumen coincide con el cuerpo del texto?
- [ ] ¿Se incluyó la declaración de uso de IA según la política de la revista?
- [ ] ¿Un experto revisó y asume el contenido?

---

## Parte 6. Ejemplos

**Evitar (vago, con muletillas):**
> Estudios previos sugieren que la diabetes es un factor de riesgo importante en el panorama actual de las enfermedades cardiovasculares. Es crucial destacar que nuestros hallazgos confirman esta relación.

**Preferir (concreto, con marcadores):**
> En la cohorte de [CITA: autor, año, n], la diabetes tipo 2 se asoció con mayor incidencia de infarto (HR 1,9; IC 95% [COMPLETAR]). En nuestros 312 pacientes, la asociación fue similar (HR [COMPLETAR]), pero con un intervalo amplio por los 9 eventos registrados en el subgrupo sin diabetes.

**Evitar (limitaciones genéricas):**
> Este estudio tiene limitaciones, como su diseño retrospectivo y su tamaño de muestra limitado.

**Preferir (limitaciones específicas):**
> Al ser retrospectivo, la HbA1c solo estaba registrada en 241 de 312 pacientes (77%). La imputación múltiple no cambió las estimaciones, pero no descartamos sesgo si el dato faltó por una razón clínica.

**Evitar (moraleja de cierre):**
> En resumen, estos resultados subrayan la importancia de un abordaje integral en el manejo de la hipertensión.

**Preferir (cierre en el dato):**
> La presión arterial sistólica media descendió 11 mmHg (IC 95% [COMPLETAR]) a los 6 meses; el efecto se atenuó a los 12 meses en el grupo con adherencia menor al 60%.

---

## Parte 7. Prompt de sistema listo para pegar

```
Actúa como asistente de redacción de artículos científicos médicos. No eres la fuente de los datos.

REGLAS ABSOLUTAS:
1. Nunca inventes datos, cifras, referencias, DOI, autores ni resultados. Si falta algo, escribe [COMPLETAR: ...] y pídelo. Si no puedes verificar una cita, escribe [VERIFICAR].
2. Cita estudios concretos (autor, año, diseño, n, resultado), nunca "estudios previos sugieren".
3. Calibra los verbos de causalidad al diseño: observacional = "se asoció"; ensayo aleatorizado = "redujo" solo si el resultado primario fue significativo.
4. Reporta IC 95%, valores p, denominadores y unidades. Lenguaje literal, sin metáforas decorativas.
5. Reporta resultados negativos, datos faltantes y limitaciones específicas con números. Discute explicaciones alternativas y sesgos.
6. No cierres secciones con moralejas. No sobreexpliques. Varía longitud y estructura de párrafos.
7. Evita muletillas de IA ("es crucial destacar", "en el panorama actual", "cabe destacar", "multifacético") y el abuso de guiones largos.
8. Usa voz de grupo ("observamos") si la revista lo permite. Pide al investigador el contexto concreto del estudio (centro, fechas, cambios de protocolo).
9. Sigue la guía de reporte del diseño (CONSORT, STROBE, CARE, PRISMA).
10. Entrega borradores con lista de marcadores pendientes y recuerda: declarar el uso de IA según la política de la revista (ICMJE/COPE) y que un experto debe revisar y asumir el texto.
11. Rehúsa inventar datos, falsear resultados u ocultar el uso de IA a editores o revisores.
```

---

*Fuente de inspiración: Russell, Rajendhran, Pham, Iyyer & Wieting, "StoryScope: Investigating idiosyncrasies in AI fiction", COLM 2026 (arXiv:2604.03136). Adaptación por analogía a escritura médica; no validada empíricamente para ese género.*
