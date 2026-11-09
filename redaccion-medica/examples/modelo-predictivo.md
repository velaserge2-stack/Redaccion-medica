# Ejemplo: modelo de predicción (TRIPOD+AI)

> Modelo anotado. Sin datos reales.

## Qué pedir al autor
¿Desarrollo, validación o ambos? Fuente de datos y periodo, desenlace y horizonte, predictores candidatos y cómo se eligieron, número de eventos, datos faltantes, algoritmo, ajuste de hiperparámetros, validación interna (bootstrap, validación cruzada) y externa, discriminación (AUC/C) **y** calibración (gráfico, pendiente, intercepto), análisis por subgrupos de equidad, disponibilidad de código y modelo.

## Esqueleto (orientativo 3500-4500 palabras)
Título (desarrollo y/o validación) · Resumen · Introducción (decisión clínica que apoya el modelo) · Métodos · Resultados (participantes, rendimiento, calibración) · Discusión · Disponibilidad de código y datos.

## Modelo anotado

**Título**
> Desarrollo y validación interna de un modelo para predecir [desenlace] a [horizonte] en [población]

**Métodos**
> Se usaron datos de [fuente] de [fechas]. El desenlace fue [definición] a [horizonte]. Se consideraron [n] predictores candidatos seleccionados por [criterio]. Hubo [n] eventos ([eventos por parámetro]). Los datos faltantes se imputaron con [método]. Se entrenó [algoritmo]; los hiperparámetros se ajustaron con [método]. El rendimiento se evaluó con [validación cruzada de k = x / bootstrap con x réplicas].

**Resultados**
> El modelo mostró un estadístico C de [x] (IC 95 % [x-x]) y una pendiente de calibración de [x] en la validación interna (Figura [x]). El rendimiento en [subgrupo] fue [x].

**Discusión**
- Validación externa pendiente si no se hizo: decirlo como limitación principal.
- No afirmar beneficio clínico sin evaluación de impacto o análisis de curva de decisión.
- Riesgo de sobreajuste con pocos eventos por predictor.

## Errores típicos
- Informar solo AUC sin calibración.
- "El modelo mejora la atención" sin estudio de impacto.
- Llamar "validación" a la partición de la misma base sin aclarar que es interna.
