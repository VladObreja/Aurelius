# Aurelius - Source Tree Analysis

**Date:** 2026-06-06

## Overview

Aurelius is organized as a single knowledge-base repository. It separates original source artifacts, canonical structured data, generated documentation, scripts, and local workflow tooling.

## Complete Directory Structure

```text
Aurelius/
|-- AGENTS.md
|-- README.md
|-- archive/
|   `-- original/
|       |-- AURELIUS_CXO_v1.30.xlsx
|       |-- *.pdf
|       `-- *.txt
|-- data/
|   |-- protocol/
|   |   |-- axes.json
|   |   |-- compounds.json
|   |   |-- cpo_entries.json
|   |   |-- daily_mvp.json
|   |   |-- daily_schedule.json
|   |   |-- labs.json
|   |   |-- metadata.json
|   |   |-- practices.json
|   |   |-- systems.json
|   |   `-- version_history.json
|   |-- research/
|   |   |-- chunks.json
|   |   `-- sources.json
|   `-- validation_report.json
|-- docs/
|   |-- index.md
|   |-- protocol-spine.md
|   |-- bmad-protocol-workflow.md
|   |-- daily-guide.md
|   |-- compound-index.md
|   |-- practice-index.md
|   |-- protocol-index.md
|   |-- research-index.md
|   `-- validation-report.md
|-- tools/
|   `-- extract_aurelius.py
|-- .agent/          # ignored local BMAD tooling
|-- .agents/         # ignored local BMAD skills
|-- .claude/         # ignored local BMAD/Claude tooling
|-- _bmad/           # ignored local BMAD framework
`-- _bmad-output/    # ignored local BMAD output
```

## Critical Directories

### `data/protocol/`

Machine-readable protocol objects extracted from the original workbook.

**Purpose:** Canonical protocol substrate.  
**Contains:** agents/compounds, practices, functional systems, phenotype axes, labs, schedules, products, trackers, print views, and version history.  
**Entry Points:** `metadata.json`, `cpo_entries.json`, `daily_schedule.json`, `compounds.json`.

### `data/research/`

Research source metadata and retrieval-ready text chunks.

**Purpose:** Search/RAG substrate for later research workflows.  
**Contains:** `sources.json` and `chunks.json`.  
**Integration:** Future claim extraction and evidence grading should link chunks to protocol object IDs.

### `docs/`

Human-readable protocol and project documentation.

**Purpose:** Operator and AI-facing documentation.  
**Contains:** generated guides, indexes, protocol spine, BMAD workflow adaptation, and validation report.  
**Entry Points:** `index.md`, `protocol-spine.md`, `daily-guide.md`.

### `archive/original/`

Preserved source artifacts.

**Purpose:** Provenance and migration safety.  
**Contains:** Original workbook, PDFs, and text research files.  
**Integration:** This is source archive, not the preferred editing location.

### `tools/`

Utility scripts.

**Purpose:** Reproducible extraction and regeneration.  
**Contains:** `extract_aurelius.py`.

### `.agents/skills/` and `_bmad/`

Local BMAD tooling.

**Purpose:** Local workflow guidance and skill definitions.  
**Contains:** BMAD skills, configuration, customization resolver, and framework files.  
**Integration:** Ignored by Git; Codex can read these locally when present.

## Entry Points

- **Human project entry:** `README.md`
- **AI/BMAD project entry:** `docs/index.md`
- **Codex instructions:** `AGENTS.md`
- **Protocol spine:** `docs/protocol-spine.md`
- **Data layout:** `docs/data-layout.md`
- **Extraction script:** `tools/extract_aurelius.py`

## File Organization Patterns

- `data/protocol/*.json`: canonical structured protocol data
- `data/research/*.json`: research corpus metadata and chunks
- `docs/*.md`: human-readable protocol/project docs
- `archive/original/*`: historical source files
- `tools/*.py`: repo utility scripts

## Configuration Files

- `.gitignore`: ignores loose root artifacts and local BMAD tooling
- `.gitattributes`: text/binary handling for Git
- `AGENTS.md`: Codex guidance for Aurelius and local BMAD usage
- `_bmad/bmm/config.yaml`: local BMAD config, ignored by Git

## Notes for Development

Treat the repository as a knowledge system. Canonical protocol changes should flow through planning artifacts, structured data updates, generated docs, validation, and commits.

---

_Generated using BMAD Method `document-project` workflow, adapted for Aurelius._
