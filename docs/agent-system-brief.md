---
title: "Aurelius Agent System Brief"
status: draft
created: 2026-06-06
updated: 2026-06-06
---

# Aurelius Agent System Brief

## Executive Summary

The Aurelius Agent System is the protocol-facing agent and tooling layer around the Aurelius knowledge base.

Its purpose is to make a mature, complex healing and optimization protocol usable in ordinary life while preserving disciplined development. It should let an agent answer practical execution questions, help the operator follow the protocol, process new research, run safety and HIRA reviews, and turn approved protocol changes into durable artifacts instead of chat drift.

The system begins with repo-local skills, scripts, orientation docs, and BMAD-adapted workflows. It may later grow into a richer local-first assistant, RAG-backed research interface, tracker, or app, but version 1 should remain small, inspectable, and grounded in the existing repository.

## Product Thesis

Aurelius does not only need better protocol content. It needs an operating layer.

The protocol has become mature enough that the limiting factor is no longer raw ideation. The limiting factors are execution clarity, change control, safety review, research triage, and continuity between AI sessions.

The agent system should become the bridge between:

- canonical protocol data
- human-readable protocol guidance
- research and claim extraction
- practical daily operation
- BMAD / PMAD protocol development
- HIRA and validation review
- future tracking and feedback loops

## Problem

The protocol is high-dimensional. It includes phased terrain work, gut-liver strategy, suspected aldehyde and endotoxin burden, antifungal and bile-flow logic, energy restoration, sexual and neurovascular recovery, sensory targets, HFMP optimization, and long-term maintenance.

That maturity creates several operational risks:

- a new session may not know where to start
- the operator may need a concrete answer in a time-constrained context
- research novelty can become execution pressure
- protocol changes can bypass safety review
- simultaneous changes can destroy signal quality
- BMAD artifacts can exist but not guide actual use
- local skills and scripts can become invisible to future agents
- the protocol can grow more impressive while becoming harder to follow

The highest practical risk remains changing too many things at once.

## User And Stakeholders

Primary user:

- Vlad, the protocol operator, researcher, and final decision-maker.

Secondary users:

- future Codex sessions entering the repository
- protocol-development agents using BMAD / PMAD roles
- future reviewers who need to inspect rationale, safety, and evidence

Possible future users:

- clinicians, coaches, or technically literate reviewers invited to inspect the protocol
- an externalized version of the operator assistant if the system later becomes shareable

## Jobs To Be Done

### Follow The Protocol

When the operator asks "where do I start tomorrow?" or "what should I buy?", the system should produce a grounded, phase-aware, actionable answer.

The answer should distinguish CORE, SUPPORT, EXPERIMENT, PRN, RESET, and archive-only material. It should also name what to defer and what to track.

### Develop The Protocol

When new research, observations, or ideas appear, the system should route them through analysis, HIRA, architecture, story creation, canonical data updates, generated docs, and validation.

It should not casually mutate executable protocol content.

### Preserve Continuity

When a new agent enters the repository, the system should provide a clear orientation: purpose, safety posture, current hypothesis, entry points, stable IDs, and the correct next workflow.

### Control Risk

When an intervention is proposed or an adverse signal appears, the system should apply energy-first logic, HIRA review, rollback rules, and stop/escalation criteria.

### Support Maintenance

When the protocol succeeds, the system should help reduce it toward maintenance interventions and targeted HFMP optimization rather than endlessly adding mechanisms.

## Solution Shape

Version 1 should be a local-first agent infrastructure made of:

- repo-local skills for protocol operation and future specialized roles
- helper scripts that query canonical JSON data
- orientation and entry-point documentation
- BMAD / PMAD workflow documents
- validation reports and known-data-issue tracking
- structured templates for HIRA, research intake, protocol stories, and operator answers

The current `aurelius-protocol-operator` skill is the first slice: it answers practical execution questions grounded in local protocol data and routes redesign questions back to BMAD/HIRA.

## Proposed Agent Roles

### Protocol Operator

Turns canonical data into daily instructions, shopping lists, phase summaries, tracking prompts, and mild drift recovery guidance.

### Research Analyst

Extracts claims from research, maps mechanisms, grades evidence, identifies contradictions, and prepares candidate protocol-change notes.

### HIRA Reviewer

Scores intervention risk by hazard severity, likelihood, reversibility, interaction burden, monitoring availability, evidence quality, operator-specific vulnerability, medical-supervision requirement, and rollback clarity.

### Protocol Manager

Maintains objectives, constraints, success criteria, phase priorities, and intervention classification rules.

### Protocol Architect

Maintains phase architecture, dependency graphs, progression gates, rollback paths, and safety architecture.

### Protocol Developer

Implements approved changes in canonical data and regenerates human-readable docs.

### Protocol QA

Checks references, missing IDs, unsafe combinations, unclear stop rules, evidence gaps, and generated-doc consistency.

### Technical Writer

Keeps orientation, guides, summaries, and operator-facing docs clear enough to use.

## Differentiators

The system is not a generic wellness chatbot.

It is:

- grounded in local canonical protocol data
- energy-first by design
- phase-aware
- safety-aware
- change-controlled through BMAD / PMAD
- explicit about evidence, uncertainty, and rollback
- designed to reduce protocol complexity over time
- versioned in Git so reasoning and artifacts can be inspected

## Version 1 Scope

In scope:

- maintain the existing operator skill
- define the agent-system brief
- create PRD-level requirements for agent roles and workflows
- add HIRA and protocol-story templates
- improve helper scripts for common operator questions
- document how new agents should enter and choose a workflow
- keep all executable answers grounded in local data

Out of scope for version 1:

- a full app UI
- autonomous protocol mutation
- medical diagnosis or medical decision automation
- unsupervised supplement or drug recommendations
- a production RAG database
- automatic syncing to external services
- making the protocol public-facing or generalized for other people

## Success Criteria

The agent system is working when:

- a new Codex session can enter the repo and understand the project within minutes
- the operator can ask a practical question and receive a grounded, executable answer
- shopping and morning-start answers are generated from canonical data
- proposed protocol changes are routed through BMAD/HIRA instead of being casually added
- research can be archived without becoming immediate execution pressure
- known data issues are visible and not silently ignored
- the system can produce a protocol story ready for implementation
- the operator can tell what is CORE, optional, experimental, gated, or deferred
- adverse signals, especially energy crashes, trigger review or rollback logic
- long-term success means simplification toward maintenance rather than stack growth

## Key Product Principles

1. Ground answers in local data first.
2. Make the next action obvious.
3. Keep protocol development separate from protocol operation.
4. Treat research intake as a filter, not a shopping list.
5. Encode safety rather than relying on memory.
6. Preserve stable IDs and auditability.
7. Prefer small scripts and clear skills before complex infrastructure.
8. Keep the system useful in a normal, time-constrained moment.
9. Reduce complexity when the protocol is working.
10. Never let agent confidence outrun evidence, safety, or operator consent.

## Risks

- The agent layer could become another source of complexity.
- Skills may drift from canonical data unless validation is routine.
- RAG could retrieve convincing but low-quality claims.
- Operator answers could overfit incomplete protocol data.
- A future agent may treat planning artifacts as executable instructions.
- Safety review can become performative unless thresholds are explicit.
- Too many specialized agents could fragment responsibility.

## Open Questions

1. Should repo-local skills remain the main interface, or should selected skills be installed into native Codex skill locations?
2. Where should operator tracking data live: Markdown logs, JSON, spreadsheet export, or a future local database?
3. What exact HIRA scoring scale and approval thresholds should Aurelius use?
4. Which agent roles need separate skills first, and which can remain documented workflows?
5. When is RAG justified, and what source-cleaning must happen before it is safe enough to rely on?
6. Should there be a lightweight UI or command palette for operator questions?
7. How should the system represent uncertainty in daily operator answers?
8. What minimum evidence is required before an agent may suggest an intervention as a candidate trial?

## Recommended Next BMAD Step

Run `bmad-prd` for the Aurelius Agent System.

The PRD should turn this brief into requirements for:

- agent roles
- user workflows
- grounding rules
- HIRA workflow
- research intake workflow
- tracking workflow
- helper scripts and data contracts
- validation and acceptance criteria

