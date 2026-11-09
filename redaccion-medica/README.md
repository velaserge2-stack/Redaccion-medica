# Manual de uso

## Qué es
Un skill (carpeta con `SKILL.md`) llamado `redaccion-medica` que enseña a Claude un procedimiento para redactar, verificar, traducir y auditar manuscritos biomédicos, con voz de investigador y sin inventar datos ni referencias. Desde la versión 0.4 trabaja **solo con los artículos que subas o con literatura que recupere de bases indexadas** (PubMed, Consensus, Europe PMC, Crossref), construye primero una ficha del contexto de tu investigación y trae un ejemplo anotado para cada tipo de artículo.

## Instalar
- **Claude (app web/escritorio)**: comprime la carpeta `redaccion-medica/` en un ZIP y súbelo en Configuración → Capacidades/Skills, según lo permita tu plan y organización. Los pasos exactos de la interfaz pueden cambiar; consulta https://support.claude.com.
- **Claude Code**: copia la carpeta a `~/.claude/skills/` (personal) o `.claude/skills/` (proyecto).
- Para que busque literatura por su cuenta, conecta en Claude el conector de **Consensus** y/o habilita la búsqueda web. Sin esas herramientas, solo usará los artículos que subas y te dará la estrategia de búsqueda para el resto.

## Activar
Se activa por la descripción cuando pides algo de un manuscrito médico o biomédico. También puedes decir: "Usa el skill de redacción médica".

## Cómo usarlo
1. Sube el material real (tesis, resultados, tablas) **y los artículos de referencia que ya tengas** (PDF), y di la revista objetivo.
2. Indica la tarea (redactar, buscar literatura, traducir, auditar, responder revisores).
3. Claude te mostrará la ficha de contexto y la matriz de evidencia (qué artículo respalda cada afirmación). Revísalas.
4. Responde a la lista de pendientes. Los `[COMPLETAR]`, `[VERIFICAR]` y `[CITA]` son para ti: no los dejes en el envío final.
5. Pide la auditoría final (A-G) antes de enviar.

## Ejemplos por tipo de artículo
`examples/README.md`: original observacional, ensayo clínico, caso clínico, revisión sistemática, revisión narrativa, estudio diagnóstico, modelo predictivo, estudio cualitativo, protocolo, tesis a artículo, carta al editor, carta de presentación y respuesta a revisores. Son modelos anotados con marcadores, sin datos reales.

## Verificar referencias en lote
```
python3 scripts/verificar_referencias.py mis_referencias.txt
```
Extrae DOI y PMID, los consulta en Crossref y PubMed y avisa si un artículo está retractado. Necesita internet; sin red marca todo como "No verificable".

## Qué no hace
No certifica validez estadística, no garantiza aceptación, no sustituye tu revisión ni la de tus coautores, no crea comité de ética ni registro, no hace búsquedas sistemáticas formales (salvo que tú definas el protocolo). Verifica referencias solo si la sesión tiene acceso a búsqueda; si no, las marca.

## Estructura
`SKILL.md` (puerta de entrada) · `workflows/` (contexto, búsqueda de evidencia, un flujo por tipo de artículo y `request-playbook.md`) · `examples/` (un modelo por tipo de artículo) · `references/` (normas, fuentes y `voice-rules.md`) · `checklists/` · `scripts/` (verificador de DOI/PMID) · `tests/` · `DEVELOPMENT-REPORT.md`.
