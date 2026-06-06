# Aurelius Component Inventory

**Date:** 2026-06-06

## Overview

This repository's components are protocol/data/documentation components rather than software runtime components.

## Protocol Components

| Component | File | Count / Shape | Purpose |
| --- | --- | --- | --- |
| Compounds / agents | `data/protocol/compounds.json` | 181 items | CAS library for inputs and interventions |
| CPO entries | `data/protocol/cpo_entries.json` | 83 items | Phase-specific canonical protocol objects |
| Daily schedule | `data/protocol/daily_schedule.json` | 313 items | Full operator-facing phase schedule |
| Daily MVP | `data/protocol/daily_mvp.json` | 36 items | Compressed daily spine |
| Practices | `data/protocol/practices.json` | 26 items | COP practice library |
| Functional systems | `data/protocol/systems.json` | 12 items | CFS mechanistic modules |
| HFMP axes | `data/protocol/axes.json` | 11 items | Target phenotype axes |
| Labs | `data/protocol/labs.json` | 21 items | CLAB marker interpretations |
| Products | `data/protocol/products.json` | 3 items | Product-to-CAS mappings |
| Reset track | `data/protocol/reset_track.json` | 5 items | Optional reset interventions |

## Research Components

| Component | File | Count / Shape | Purpose |
| --- | --- | --- | --- |
| Sources | `data/research/sources.json` | 31 sources | Source metadata, hashes, topics, excerpts |
| Chunks | `data/research/chunks.json` | 583 chunks | Retrieval-ready text chunks |

## Documentation Components

| Component | File | Purpose |
| --- | --- | --- |
| Protocol spine | `docs/protocol-spine.md` | Frozen current working spine |
| Daily guide | `docs/daily-guide.md` | Operator execution guide |
| Protocol index | `docs/protocol-index.md` | Module and axis overview |
| Compound index | `docs/compound-index.md` | Compound lookup |
| Practice index | `docs/practice-index.md` | Practice lookup |
| Research index | `docs/research-index.md` | Research source lookup |
| BMAD workflow | `docs/bmad-protocol-workflow.md` | Protocol-specific BMAD adaptation |
| Validation report | `docs/validation-report.md` | Missing cross-reference report |

## Tooling Components

| Component | File / Folder | Purpose |
| --- | --- | --- |
| Extractor | `tools/extract_aurelius.py` | Reproducible workbook/research extraction |
| Codex guidance | `AGENTS.md` | Repo instructions and BMAD bridge |
| BMAD skills | `.agents/skills/` | Local workflow skills, ignored by Git |
| BMAD config | `_bmad/` | Local BMAD framework/config, ignored by Git |

## Current Validation Issue

The extracted protocol has one missing object ID referenced from two places:

- `CFS-05` references missing `CAS-GUT-05`
- `HFMP-8` references missing `CAS-GUT-05`

See `docs/validation-report.md`.

---

_Generated using BMAD Method `document-project` workflow, adapted for Aurelius._
