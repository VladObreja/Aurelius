# BMAD Adaptation for Aurelius

BMAD is a software-development method, but its architecture is useful here because Aurelius has the same failure modes as a complex software project: drift, hidden assumptions, overgrown scope, unclear ownership, weak QA, and poor change control.

This document adapts BMAD into a protocol-development method.

## Working Name

PMAD: Protocol Method of Agentic Development.

## Objective

Develop the Aurelius protocol through specialized roles and durable artifacts instead of ad hoc chat decisions.

The goal is not bureaucracy. The goal is to keep the protocol simple, supple, and effective while preserving mechanistic depth.

## Role Mapping

### Analyst

Purpose: understand the research and extract claims.

Outputs:

- research briefs
- claim tables
- mechanism maps
- contradiction lists
- evidence grades

### Protocol Manager

Purpose: define goals, constraints, priorities, and success metrics.

Outputs:

- protocol brief
- phase objectives
- operator constraints
- symptom priorities
- success and stop criteria

### Protocol Architect

Purpose: design the protocol structure.

Outputs:

- phase architecture
- module boundaries
- dependency graph
- escalation and taper rules
- safety architecture

### Protocol Developer

Purpose: implement approved changes in the canonical data.

Outputs:

- updates to `data/protocol/*.json`
- regenerated docs
- version notes
- migration scripts when needed

### Safety / QA Reviewer

Purpose: check coherence, references, contraindications, overload, and monitoring.

Outputs:

- validation reports
- safety reviews
- missing evidence lists
- interaction and adverse-event checks

### Operator Planner

Purpose: turn the architecture into usable daily execution.

Outputs:

- daily guide
- phase guide
- MVP spine
- weekly checklist
- tracking instructions

### Technical Writer

Purpose: keep human-readable materials clear and current.

Outputs:

- protocol guides
- quick-start docs
- rationale summaries
- research indexes

## Artifact Sequence

1. Freeze current spine.
2. Create protocol brief.
3. Create protocol PRD.
4. Create protocol architecture.
5. Convert improvements into protocol stories.
6. Implement stories in canonical data.
7. Regenerate human-readable docs.
8. Run validation and safety review.
9. Commit changes with clear version notes.

## Change Pipeline

Every proposed protocol change should move through this path:

```text
research or observation
-> claim extraction
-> relevance assessment
-> protocol change proposal
-> safety and evidence review
-> canonical data update
-> generated human guide
-> validation report
-> commit
```

## Protocol Story Template

Each protocol story should answer:

- What problem does this solve?
- Which phase or module does it affect?
- Which existing object IDs are involved?
- Is this CORE, SUPPORT, EXPERIMENT, PRN, or archive-only?
- What is the entry condition?
- What is the exit, taper, or stop condition?
- What should be tracked?
- What safety issues or interactions exist?
- What evidence supports it?
- What generated docs must change?

## First BMAD Pass on Existing Protocol

The first pass should not add new interventions. It should clarify what already exists.

Recommended order:

1. Analyst: summarize the current research corpus and identify core claims.
2. Protocol Manager: define current objectives and operator constraints.
3. Architect: formalize the phase model and dependency graph.
4. Safety / QA: identify overload, missing references, weak stop rules, and risky combinations.
5. Operator Planner: produce a minimal executable spine per phase.
6. Developer: update structured data and regenerate docs.
7. Technical Writer: polish human guides.

## Non-Goals

- Do not turn the protocol into a software project for its own sake.
- Do not promote speculative tools just because they have an interesting mechanism.
- Do not optimize the data model before the protocol spine is clear.
- Do not create a RAG database until source documents, claims, and protocol object links are cleaner.

