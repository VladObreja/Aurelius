# Aurelius - Project Overview

**Date:** 2026-06-06  
**Type:** Protocol knowledge base  
**Architecture:** Canonical structured data with generated human-readable documentation

## Executive Summary

Aurelius is a machine-readable and human-readable knowledge base for a phased biohacking/healing protocol. Its current source material was migrated from an Excel workbook and adjacent research files into structured JSON, generated Markdown guides, and a preserved source archive.

The protocol itself is a terrain-first, phase-gated recovery and optimization system focused on gut-liver flow, endotoxin/aldehyde burden, fungal terrain, mitochondrial output, neurovascular/sexual function, endocrine signaling, pelvic/autonomic mechanics, and sensory recovery.

## Project Classification

- **Repository Type:** Single-part knowledge repository
- **Project Type:** Data/documentation project
- **Primary Languages:** JSON, Markdown, Python
- **Architecture Pattern:** Source archive -> extraction script -> canonical protocol data -> generated docs -> validation reports

## Technology Stack Summary

| Category | Technology | Role |
| --- | --- | --- |
| Structured data | JSON | Canonical protocol and research data |
| Human docs | Markdown | Generated and hand-authored protocol guides |
| Extraction | Python | Workbook/research migration and validation |
| Source workbook | XLSX | Historical source artifact, not canonical going forward |
| Versioning | Git/GitHub | Change history and collaboration |
| Local workflow | BMAD | Ignored local protocol-development tooling |

## Key Features

- Machine-readable protocol objects in `data/protocol/`
- Research source metadata and text chunks in `data/research/`
- Human-readable protocol docs in `docs/`
- Original artifacts preserved in `archive/original/`
- Cross-reference validation report
- BMAD-inspired protocol-development workflow
- Codex guidance for using local BMAD skills

## Architecture Highlights

- The current executable protocol spine is documented separately from the full research library.
- Protocol objects use stable IDs such as `CAS-*`, `COP-*`, `CFS-*`, and `HFMP-*`.
- Human-readable guides are treated as generated or derivative views of structured data.
- BMAD tooling is local-only and ignored by Git; repo guidance explains how Codex should use it when present.
- The current validation report identifies a missing `CAS-GUT-05` reference.

## Development Overview

### Prerequisites

- Git
- Python with `openpyxl` available, or Codex bundled Python runtime
- Local BMAD install is optional and ignored by Git

### Getting Started

Read `README.md`, then `docs/index.md`, `docs/protocol-spine.md`, and `docs/bmad-protocol-workflow.md`.

### Key Commands

- **Extract/regenerate from workbook:** `python tools/extract_aurelius.py`
- **Check Git status:** `git status --short`
- **Validate JSON manually:** load all `data/**/*.json` with Python

## Repository Structure

The repository is organized around canonical data, generated docs, source archive, and workflow tooling. See [Source Tree Analysis](./source-tree-analysis.md).

## Documentation Map

- [index.md](./index.md) - Master BMAD documentation index
- [architecture.md](./architecture.md) - Knowledge-base architecture
- [source-tree-analysis.md](./source-tree-analysis.md) - Directory structure
- [development-guide.md](./development-guide.md) - Repository workflow
- [component-inventory.md](./component-inventory.md) - Protocol/data component map

---

_Generated using BMAD Method `document-project` workflow, adapted for Aurelius._
