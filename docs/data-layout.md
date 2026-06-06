# Data Layout

The extracted protocol data is split by object type so it can be versioned, validated, searched, and regenerated into human-readable formats.

## Protocol Data

- `data/protocol/compounds.json` - CAS agents, foods, supplements, drugs, and other protocol inputs
- `data/protocol/practices.json` - COP practices and operations
- `data/protocol/systems.json` - CFS modules
- `data/protocol/axes.json` - HFMP axes
- `data/protocol/labs.json` - CLAB markers and interpretations
- `data/protocol/cpo_entries.json` - phase-specific protocol entries
- `data/protocol/daily_schedule.json` - full daily schedule by phase and time block
- `data/protocol/daily_mvp.json` - reduced daily spine
- `data/protocol/products.json` - product mappings to CAS IDs
- `data/protocol/version_history.json` - migrated workbook version history
- `data/protocol/metadata.json` - workbook extraction metadata and text sections

## Research Data

- `data/research/sources.json` - source file metadata, hashes, inferred topics, and excerpts
- `data/research/chunks.json` - chunked text corpus suitable for search or later embedding

## Generated Docs

- `docs/protocol-index.md` - object counts and module/axis overview
- `docs/compound-index.md` - compound table
- `docs/practice-index.md` - practice table
- `docs/daily-guide.md` - generated daily protocol guide
- `docs/research-index.md` - research source index
- `docs/validation-report.md` - missing cross-reference report
