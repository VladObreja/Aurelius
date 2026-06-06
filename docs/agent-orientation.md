# Aurelius Agent Orientation

Read this first when entering the Aurelius repository as an AI agent.

## What Aurelius Is

Aurelius is a research and self-tracking protocol knowledge base. It is not a software application.

The project stores a phased biohacking/healing protocol as machine-readable protocol objects, generated human-readable guides, preserved source artifacts, and process documentation for ongoing protocol development.

The protocol is currently **energy-first**: restoring usable biological energy is the primary objective because energy is the basis of action. Libido, erectile quality, smell, mood/drive, training response, and HFMP expression matter, but they are downstream or parallel expressions of restored energy and resilience.

Important: this is a research and self-tracking knowledge base, not medical advice.

## Current Purpose

The current project objective is to finalize and optimize the Aurelius protocol spine so it remains:

- simple enough to execute
- supple enough to adapt
- encompassing enough to be effective
- constrained enough to avoid stack bloat

The immediate work is **not** to add more interventions. The immediate work is to clarify the protocol architecture, risk review, evidence thresholds, tracking, rollback logic, and research intake process.

## Core Model

The working terrain hypothesis is that partial ALDH impairment, fungal/gut overgrowth, cholestasis, aldehyde burden, and endotoxin pressure may drive downstream suppression of energy, libido, smell, mood/drive, and sexual function.

This is a working hypothesis, not dogma. The project should seek measurable ways to test the hypothesis itself or downstream effects.

## Main Entry Points

Start here:

- `README.md` - repo-level overview
- `AGENTS.md` - Codex-specific guidance and local skill usage
- `docs/index.md` - documentation index
- `docs/protocol-brief.md` - energy-first protocol brief
- `docs/protocol-spine.md` - frozen current protocol spine
- `docs/bmad-protocol-workflow.md` - BMAD adaptation for protocol development

For operator-facing questions:

- `skills/aurelius-protocol-operator/SKILL.md`
- `tools/aurelius_operator.py`

For data layout:

- `docs/data-layout.md`
- `data/protocol/`
- `data/research/`

For validation:

- `docs/validation-report.md`
- `data/validation_report.json`

## Repository Layout

```text
data/protocol/       canonical structured protocol data
data/research/       research source metadata and text chunks
docs/                human-readable guides, indexes, and planning artifacts
archive/original/    preserved source workbook, PDFs, and text research files
tools/               extraction and operator helper scripts
skills/              repo-local skills, including the protocol operator
```

Local BMAD tooling may exist under `.agents/`, `.agent/`, `.claude/`, `_bmad/`, and `_bmad-output/`. These are intentionally ignored by Git.

## Protocol Object Types

- `CAS-*` - compounds, agents, foods, supplements, drugs, or other inputs
- `COP-*` - operator practices
- `CFS-*` - functional systems
- `HFMP-*` - target phenotype axes
- `CLAB-*` - lab markers, derived where possible
- `PROD-*` - products mapped to CAS objects

Stable IDs are sacred. Do not reuse an ID for a different meaning.

## Development Principles

- Energy first.
- Terrain before force.
- Phase gates over enthusiasm.
- CORE means structurally necessary, not merely good.
- Every intervention is a hypothesis.
- Every intervention needs an exit.
- Practices are first-class interventions.
- Signal quality precedes novelty.
- Research does not directly change the protocol.
- Safety must be encoded, not remembered.
- Complexity must be budgeted even when pill tolerance is high.
- Rollback is a feature, not failure.
- Mature success means a quieter protocol.

## Change Discipline

Do not mutate `data/protocol/*.json` casually.

Before changing canonical protocol data, prefer creating or updating planning artifacts. Any intervention promoted to CORE should have:

- purpose
- phase
- tier
- entry condition
- exit/taper/stop rule
- safety note
- evidence rationale
- tracking signal

Run `tools/extract_aurelius.py` only when intentionally regenerating extracted data from the original workbook.

## BMAD Adaptation

Use BMAD concepts in their protocol-adapted form:

- product -> protocol
- feature -> protocol module or intervention
- implementation -> canonical data and generated docs
- QA -> safety, coherence, evidence, and reference validation
- architecture -> phase model, dependency graph, progression gates, and safety model

Recommended artifact sequence:

1. Protocol Brief
2. Protocol PRD
3. Protocol Architecture
4. Protocol Stories
5. Canonical data updates
6. Generated docs
7. Validation and safety review
8. Commit

## Operator Skill

For practical protocol execution questions, use:

```text
skills/aurelius-protocol-operator/SKILL.md
```

Examples:

- "It is Saturday evening; where do I start Sunday morning?"
- "I am shopping for Phase 1.0 CORE/SUPPORT items. What should I get?"
- "What do I track today?"

The helper script can ground common answers:

```powershell
& 'C:\Users\Vlad\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' tools\aurelius_operator.py morning --phase 1.0
& 'C:\Users\Vlad\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' tools\aurelius_operator.py shopping --phase 1.0 --tiers CORE SUPPORT
& 'C:\Users\Vlad\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' tools\aurelius_operator.py phase --phase 1.0
```

## Safety Posture

Energy crash is a top-tier adverse signal.

The project intends to use HIRA risk analysis for interventions rather than fixed category-level bans. HIRA should evaluate hazard severity, likelihood, reversibility, interaction risk, monitoring availability, evidence quality, operator-specific vulnerability, medical-supervision requirement, and rollback clarity.

If the user reports severe or medically concerning symptoms, do not continue protocol escalation. Recommend stopping escalation and seeking qualified medical help.

## Current Known Data Issue

`CAS-GUT-05` is referenced by `CFS-05` and `HFMP-8`, but no corresponding compound exists in the extracted CAS table.

See:

- `docs/validation-report.md`

## Suggested First Move For A New Agent

1. Read this file.
2. Read `docs/protocol-brief.md`.
3. Read `docs/protocol-spine.md`.
4. If answering execution questions, load `skills/aurelius-protocol-operator/SKILL.md`.
5. If planning protocol changes, use `docs/bmad-protocol-workflow.md` and create planning artifacts before editing canonical data.

