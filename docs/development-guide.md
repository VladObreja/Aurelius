# Aurelius Development Guide

**Date:** 2026-06-06

## Purpose

This guide explains how to work safely in the Aurelius repository. "Development" here means protocol knowledge-base development: data edits, documentation updates, validation, BMAD planning artifacts, and Git versioning.

## Prerequisites

- Git configured for the repository
- Python runtime capable of running `tools/extract_aurelius.py`
- Local BMAD install if using BMAD skills
- Awareness that protocol content is health-related and should be handled conservatively

## Core Workflow

1. Read the relevant current docs.
2. Decide whether the change is planning-only, documentation-only, data-changing, or source-regeneration.
3. For protocol logic changes, create or update a planning artifact first.
4. Edit canonical data only when the change is approved.
5. Regenerate derived docs if needed.
6. Validate JSON and references.
7. Commit with a clear message.

## Working With BMAD

BMAD files are local tooling and ignored by Git:

- `.agents/skills/`
- `.agent/`
- `.claude/`
- `_bmad/`
- `_bmad-output/`

OpenAI Codex can read the local BMAD skill files when present. See `AGENTS.md`.

For protocol work, translate BMAD concepts:

- product -> protocol
- feature -> module/intervention
- implementation -> canonical data and generated docs
- QA -> safety, coherence, evidence, and reference validation
- architecture -> phase model, dependency graph, gates, taper logic, and safety model

## Running Extraction

The extractor rebuilds data from the original workbook and research files:

```powershell
& 'C:\Users\Vlad\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' tools\extract_aurelius.py
```

Run it only when intentionally regenerating extracted data from the workbook/source artifacts.

## Validation

Minimum validation after JSON/data changes:

```powershell
& 'C:\Users\Vlad\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -c "import json,pathlib; [json.loads(p.read_text(encoding='utf-8')) for p in pathlib.Path('data').glob('**/*.json')]; print('json ok')"
```

Then inspect:

- `data/validation_report.json`
- `docs/validation-report.md`

## Git Workflow

Check status:

```powershell
git status --short
```

Commit only meaningful repository artifacts. Do not commit ignored local BMAD tooling folders.

## Safety Rules

- Do not promote an intervention to CORE without rationale, phase, entry condition, exit/taper rule, safety note, and evidence basis.
- Do not use the research library as a shopping list.
- Preserve stable IDs.
- Keep human-readable guides aligned with canonical data.
- Treat adverse response, unstable sleep, unstable digestion, worsening bile symptoms, anxiety, and overtraining as protocol-significant.

---

_Generated using BMAD Method `document-project` workflow, adapted for Aurelius._
