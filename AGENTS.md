# Codex Guidance for Aurelius

This repository is a research/protocol knowledge base, not a software application. Treat protocol content with care: preserve provenance, avoid casual medical claims, and keep the protocol simple enough to execute.

## BMAD Skills

BMAD has been installed under:

- `.agents/skills/`
- `_bmad/`

OpenAI Codex may not auto-load these as native session skills. When the user invokes a BMAD skill or agent by name, manually load the relevant `.agents/skills/<skill-name>/SKILL.md` file and follow it as repo-local workflow guidance.

For BMAD customization resolution, prefer the bundled Codex Python runtime if system `python` fails:

```powershell
& 'C:\Users\Vlad\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' _bmad\scripts\resolve_customization.py --skill .agents\skills\<skill-name> --key agent
```

Use `--key workflow` for workflow skills.

BMAD config lives at:

- `_bmad/bmm/config.yaml`
- `_bmad/config.toml`
- `_bmad/config.user.toml`
- `_bmad/custom/`

## Protocol-Specific Adaptation

Before applying software-oriented BMAD instructions literally, translate them into the Aurelius protocol domain:

- product -> protocol
- feature -> protocol module or intervention
- implementation -> canonical data and generated docs
- QA -> safety, coherence, evidence, and reference validation
- architecture -> phase model, dependency graph, progression gates, and safety model

The current project-specific adaptation is documented in:

- `docs/protocol-spine.md`
- `docs/bmad-protocol-workflow.md`

## Aurelius Protocol Operator

For practical execution questions such as "where do I start Sunday morning?" or "what should I buy while shopping?", use the repo-local skill:

- `skills/aurelius-protocol-operator/SKILL.md`

Use its helper script for grounded phase plans and shopping lists:

```powershell
& 'C:\Users\Vlad\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' tools\aurelius_operator.py morning --phase 1.0
& 'C:\Users\Vlad\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' tools\aurelius_operator.py shopping --phase 1.0 --tiers CORE SUPPORT
```

## Change Discipline

- Do not mutate `data/protocol/*.json` casually.
- Prefer creating or updating planning artifacts before protocol data changes.
- Any protocol intervention promoted to CORE should have purpose, phase, entry condition, exit/taper rule, safety note, and evidence rationale.
- Run `tools/extract_aurelius.py` only when intentionally regenerating extracted data from the original workbook.
- After meaningful repo changes, validate JSON files and check `docs/validation-report.md`.
