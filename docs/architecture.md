# Aurelius Architecture

**Date:** 2026-06-06

## Architecture Summary

Aurelius uses a source-preserving knowledge-base architecture:

```text
original artifacts
-> extraction script
-> structured protocol/research JSON
-> generated Markdown guides
-> validation reports
-> Git/GitHub version history
```

The architecture exists to prevent protocol drift. Stable protocol IDs and canonical data should outlast any individual chat, workbook, or generated guide.

## Layers

### 1. Source Archive

Location: `archive/original/`

This layer preserves the original workbook, text research files, and PDFs. It provides provenance and an escape hatch if extraction mistakes are found.

### 2. Canonical Protocol Data

Location: `data/protocol/`

This is the machine-readable protocol substrate. Major collections include:

- `compounds.json`: CAS agents and inputs
- `practices.json`: COP operator practices
- `systems.json`: CFS functional systems
- `axes.json`: HFMP phenotype axes
- `labs.json`: CLAB markers
- `cpo_entries.json`: phase-specific canonical protocol entries
- `daily_schedule.json`: daily phase schedule
- `version_history.json`: migrated workbook version history

### 3. Research Corpus

Location: `data/research/`

This layer indexes research source files and text chunks. It is prepared for later search, claim extraction, and RAG work.

### 4. Human Documentation

Location: `docs/`

This layer makes the protocol usable. It includes daily guides, indexes, protocol spine, data layout, validation report, and BMAD workflow adaptation.

### 5. Local Workflow Tooling

Locations: `.agents/`, `.agent/`, `.claude/`, `_bmad/`, `_bmad-output/`

These are local-only BMAD tools and artifacts. They are intentionally ignored by Git.

## Data Flow

1. Original workbook and research files are preserved.
2. `tools/extract_aurelius.py` extracts workbook sheets and research source metadata.
3. Structured JSON files are written under `data/`.
4. Markdown docs are generated under `docs/`.
5. Cross-reference validation is written to `data/validation_report.json` and `docs/validation-report.md`.
6. Meaningful changes are committed to GitHub.

## Protocol Object Model

The protocol is organized around stable IDs:

- `CAS-*`: compounds, agents, foods, drugs, supplements, or other inputs
- `COP-*`: operator practices
- `CFS-*`: functional systems
- `HFMP-*`: target phenotype axes
- `CLAB-*`: lab markers, derived where possible
- `PROD-*`: mapped products

The key design rule is that stable IDs should not be reused for a different meaning.

## Safety and Change Control

Protocol edits should not be casual text edits. A safe change should identify:

- object ID affected
- phase affected
- tier: CORE, SUPPORT, EXPERIMENT, PRN, or archive-only
- entry condition
- exit/taper/stop condition
- safety note
- evidence rationale
- generated docs affected

## Known Architecture Gap

The current extraction is JSON-based, but not yet schema-enforced. Future work should add explicit schemas and validators for required fields, cross-reference integrity, evidence grades, safety flags, and phase gates.

---

_Generated using BMAD Method `document-project` workflow, adapted for Aurelius._
