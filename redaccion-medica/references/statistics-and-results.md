# Revisión metodológica y estadística

Alcance: detectar inconsistencias y señalar análisis potencialmente inadecuados. **No certificar validez estadística** y **no recalcular** sin los datos. Lo que no se pueda comprobar se declara "No verificable".

## Qué comprobar
1. **Pregunta, diseño y análisis**: ¿el análisis responde a la pregunta y respeta el diseño (datos pareados, medidas repetidas, clústeres, tiempo a evento)?
2. **Desenlaces y variables**: definidos antes del análisis; desenlace primario identificado; distinguir exploratorios y post hoc.
3. **Tamaño de muestra**: ¿hay justificación? Si el estudio es exploratorio, decirlo.
4. **Pruebas estadísticas**: coherentes con el tipo de variable y distribución; software y versión declarados.
5. **Estimaciones con incertidumbre**: medida de efecto con intervalo de confianza, no solo valor p.
6. **Valores p**: precisión razonable (no "p=0,000"; usar p<0,001); sin dicotomizar mecánicamente.
7. **Significación estadística vs relevancia clínica**: mencionar magnitud y umbral clínicamente importante cuando se conozca.
8. **Datos faltantes y exclusiones**: cuántos, por qué, cómo se manejaron.
9. **Comparaciones múltiples**: declarar manejo o tratar los hallazgos como exploratorios.
10. **Sesgo y confusión**: ¿se ajustó por confusores? ¿Cuáles y por qué? Describir sesgos plausibles.
11. **Modelos predictivos**: separación desarrollo/validación, validación interna y externa, calibración además de discriminación, sobreajuste, eventos por predictor, manejo de desbalance (ver TRIPOD+AI).
12. **Coherencia numérica**: N total = suma de grupos; porcentajes consistentes con numeradores y denominadores; texto = tablas = figuras = resumen.

## Chequeos aritméticos sin datos originales
Permitidos porque no requieren los datos crudos: sumas de grupos, que los porcentajes coincidan con n/N, que un IC contenga la estimación puntual, que un valor p sea coherente en signo con el IC (si el IC del OR excluye 1, p<0,05). Si algo no cuadra, se señala con la ubicación y se pregunta; no se corrige.

## Redacción de resultados
- Presentar n (%) con denominador; media (DE) o mediana (RIC) según distribución.
- Unidades en el encabezado de la tabla; decimales consistentes.
- Resultados negativos se informan con el mismo detalle que los positivos.
- Marcar análisis post hoc o por subgrupos como tales.

## Reglas de seguridad
- Si el usuario pide "que salga significativo", "elimina los valores atípicos" o "ajusta hasta que cuadre": no. Explicar que cambiar análisis o datos para mejorar la narrativa es mala práctica; ofrecer reportar lo observado con transparencia.
- Si faltan datos para evaluar un punto: "No verificable: se requiere [dato]".
