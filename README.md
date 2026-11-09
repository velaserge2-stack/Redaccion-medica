# Redacción médica — skill para Claude

Skill `redaccion-medica` (v0.4): redacta, edita, traduce y audita manuscritos de ciencias de la salud sin inventar datos ni referencias. Se basa solo en los artículos que sube el usuario o en literatura recuperada de bases indexadas (PubMed, Consensus, Europe PMC, Crossref), entiende primero el contexto de la investigación y trae ejemplos anotados de cada tipo de artículo.

- Skill: [`redaccion-medica/`](redaccion-medica/) — empieza por [`SKILL.md`](redaccion-medica/SKILL.md).
- Manual de uso e instalación: [`redaccion-medica/README.md`](redaccion-medica/README.md).
- Ejemplos por tipo de artículo: [`redaccion-medica/examples/`](redaccion-medica/examples/README.md).
- Cambios y limitaciones: [`redaccion-medica/DEVELOPMENT-REPORT.md`](redaccion-medica/DEVELOPMENT-REPORT.md).

## Instalar en Claude
Comprime la carpeta `redaccion-medica/` en un ZIP y súbela en Configuración → Capacidades → Skills. En Claude Code, cópiala a `~/.claude/skills/`.
