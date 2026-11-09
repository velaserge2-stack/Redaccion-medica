# Manual de uso

## Qué es
Un skill (carpeta con `SKILL.md`) llamado `redaccion-medica` que enseña a Claude un procedimiento para redactar, verificar, traducir y auditar manuscritos biomédicos, con voz de investigador y sin inventar datos ni referencias. Integra dos fuentes: el procedimiento de redacción científica biomédica (guías de reporte, auditorías, traducción, revistas) y las reglas de voz humana para escritura médica.

## Instalar
- **Claude (app web/escritorio)**: comprime la carpeta `redaccion-medica/` en un ZIP (o usa el ZIP entregado) y súbelo en Configuración → Capacidades/Skills, según lo permita tu plan y organización. Los pasos exactos de la interfaz pueden cambiar; consulta https://support.claude.com.
- **Claude Code**: copia la carpeta a `~/.claude/skills/` (personal) o `.claude/skills/` (proyecto).

## Activar
Se activa por la descripción cuando pides algo de un manuscrito médico o biomédico. También puedes decir: "Usa el skill de redacción médica".

## Cómo usarlo
1. Adjunta el material real (tesis, resultados, tablas, referencias) y di la revista objetivo.
2. Indica la tarea (redactar, traducir, auditar, responder revisores).
3. Responde a la lista de pendientes. Los `[COMPLETAR]` y `[VERIFICAR]` son para ti: no los dejes en el envío final.
4. Pide la auditoría final (A-G) antes de enviar.

## Qué no hace
No certifica validez estadística, no garantiza aceptación, no sustituye tu revisión ni la de tus coautores, no crea comité de ética ni registro. Verifica referencias solo si la sesión tiene acceso a búsqueda; si no, las marca.

## Estructura
`SKILL.md` (puerta de entrada) · `workflows/request-playbook.md` (qué hacer según cada petición) · `references/` (normas, fuentes y `voice-rules.md`) · `workflows/` (por tipo de artículo) · `checklists/` · `examples/` · `tests/` · `DEVELOPMENT-REPORT.md`.
