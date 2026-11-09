# Informe de desarrollo

Fecha: 2026-10-17. Versión del skill: 0.3 (nombre `redaccion-medica`; integra `biomedical-scientific-writing` y las reglas de voz humana; probado una vez con casos sintéticos, sin usuarios reales).

## Qué se hizo
Versión 0.1: investigación en línea de la documentación de skills y de las guías de reporte y políticas editoriales; diseño de un skill modular; redacción de 25 archivos; validación estructural automática del paquete.
Versión 0.2: se renombró el skill a `redaccion-medica`; se reescribió la descripción de activación para que cubra también peticiones de redacción, mejora y humanización de texto médico; se incorporó el documento de reglas de voz como `references/voice-rules.md` y se enlazó desde `SKILL.md`, `editorial-standards.md`, `research-ethics.md`, `original-manuscript.md` y `source-index.md`. El resto del contenido se conservó sin cambios sustantivos. Total: 26 archivos de contenido más este informe.

Versión 0.3 (2026-11-06): se ejecutaron los 20 casos de prueba (15 más 5 adversariales) con subagentes que usaron la versión 0.2. Los 20 cumplieron los criterios, incluidos los críticos. Se hallaron 4 fallos menores y se corrigieron: reglas 9-11 en `SKILL.md`, párrafo en `references-and-citations.md` y `research-ethics.md`. Con lo observado se creó `workflows/request-playbook.md` (qué hacer según cada tipo de petición) y se enlazó desde `SKILL.md`. **La versión 0.3 no se ha vuelto a probar.**

## Qué se verificó (leído o confirmado en la sesión de la versión 0.1)
- **ICMJE**: la página oficial de noticias confirma la actualización de enero 2026 con la nueva sección V (IA) y III.L.2 (acceso a datos). El texto de las secciones no se leyó.
- **CONSORT 2025 y SPIRIT 2025**: metadatos y resúmenes (30 y 34 ítems; publicación 2025). Checklists no leídos.
- **TRIPOD+AI** (27 ítems, 2024, sustituye a TRIPOD 2015) y **PRISMA 2020** (27 ítems): resúmenes.
- **COPE** sobre IA y autoría: texto de la postura vía resultado de búsqueda.
- **EQUATOR**: listado consultado (709 guías), que confirma la existencia de varias guías y extensiones.
- Estructura de skills: artículo de ingeniería de Anthropic y la guía interna skill-creator.

## Qué NO se verificó
- Ninguna guía se leyó en texto completo; el skill no reproduce ítems de checklists.
- STROBE, CARE, STARD, CHEERS, SQUIRE, ARRIVE, SAMPL, STREGA, WHO/ICTRP: solo títulos o enlaces (nivel N3 en `source-index.md`).
- AMA Manual of Style, Citing Medicine, CSE, MeSH, DeCS y literatura sobre escritura en español: no consultados. Las reglas de estilo en inglés y español son práctica editorial general, no derivadas de esas fuentes.
- StoryScope (Russell et al., COLM 2026), base de `voice-rules.md`: no se leyó en esta sesión; los porcentajes citados provienen del documento original de reglas y no se contrastaron. Es un estudio de ficción en inglés; la adaptación a escritura médica es por analogía y no está validada.
- La página oficial de mejores prácticas de skills de Anthropic no pudo abrirse; el límite de nombre y de 20 KB proviene de un resumen de terceros y se respetó por precaución.
- Instalación en la interfaz: pasos genéricos, pueden variar.

## Pruebas
- **Ejecutadas**: validación estructural (frontmatter, rutas internas, tamaño). Resultados en la sección siguiente.
- **Ejecutados una vez**: los 15 casos y 5 adversariales de `tests/evaluation-cases.md` (20/20 aprobados según el desarrollador, con insumos sintéticos y sin búsqueda web). Limitaciones: una sola corrida por caso, sin revisión independiente, sin comparar contra Claude sin el skill, y con el mismo modelo que escribió el skill. Falta repetir tras los cambios de la 0.3 y probar con manuscritos reales y con búsqueda disponible.

## Decisiones de diseño
- Divulgación progresiva: SKILL.md corto con tabla de selección; detalle en references/workflows.
- Un solo archivo `study-designs.md` para observacional, ensayo, diagnóstico y predicción (en lugar de cuatro), para evitar duplicación; los demás flujos propuestos se fusionaron igual.
- No se crearon `annotated-manuscript-examples.md` ni un ejemplo demostrativo con material real: no se dispuso de un manuscrito legítimo y no se inventan resultados clínicos. Los ejemplos de `before-and-after.md` están rotulados como sintéticos.
- Fusión con el skill existente `redaccion-medica-voz-humana`: en la versión 0.2 sus reglas de voz viven en `references/voice-rules.md`. Si ambos skills están instalados a la vez, pueden activarse juntos para la misma petición; conviene desinstalar el antiguo o dejar solo uno para evitar instrucciones duplicadas.
- Integridad primero: marcadores en vez de relleno, tres estados de auditoría, prohibición de recalcular sin datos.
- Las reglas de integridad de `SKILL.md` prevalecen sobre las de voz en caso de conflicto.

## Limitaciones
No verifica referencias sin acceso a búsqueda; no certifica estadística; no garantiza aceptación; guías cambian y deben revisarse antes de citar versiones.

## Mejoras futuras
Repetir las pruebas con la 0.3 y con una línea base sin skill; leer en texto completo las guías y crear resúmenes por ítem con licencia adecuada; añadir ejemplo real con material de acceso abierto; script de verificación de DOI/PMID contra Crossref/PubMed; optimizar la descripción de activación con el bucle de skill-creator; verificar los datos de StoryScope.

## Resultado de la validación estructural
Ejecutada 2026-10-17: frontmatter válido (nombre `redaccion-medica`, sin "claude" ni "anthropic"; descripción de 836 caracteres); SKILL.md de 6,5 KB y 65 líneas; todas las rutas internas a references/, workflows/, checklists/, examples/ y tests/ existen; 26 archivos en el paquete.
