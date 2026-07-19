# Physical Task Layer v0.1 — Boundary and Semantic Stack

**Status:** draft, experimental
**Linked issue:** #7
**Date:** 2026-07-19

## Purpose

Establish a bounded, machine-readable foundation for a **compendium of physical tasks**, beginning with keyboard typing as the first hybrid human-machine reference task.

This document defines the scope, non-goals, candidate vocabulary, and relationship to the existing activity-source adapter.

## Scope boundary

The physical-task layer is an **experimental adjacent semantic and observability layer**. It is not a replacement for the Compendium of Physical Activities.

| Layer | Purpose | Source |
|-------|---------|--------|
| Activity-source adapter (existing) | Preserve upstream MET values, activity codes, descriptions, licensing | Compendium of Physical Activities |
| Physical-task layer (this document) | Model functional tasks, execution modalities, protocols, observations, and interpretations | HUMMBL-derived, non-canonical |

The external Compendium of Physical Activities remains authoritative for metabolic intensity. The physical-task layer addresses a different problem: representing the physical realities of modern human-machine work.

## Hard invariants

- Do not alter upstream MET values.
- Do not merge distinct upstream activities.
- Preserve upstream codes and descriptions.
- Keep derived annotations separate from source values.
- Do not vendor unreviewed upstream tables.
- Preserve source licensing, attribution, provenance, and transformation receipts.
- All new terminology remains candidate/non-canon until separately audited.

## Semantic stack

The ordered entities from intent to decision:

```text
Intent / functional goal
  -> task
  -> task variant
  -> execution modality
  -> protocol
  -> instrument
  -> task episode
  -> observation
  -> derived measure
  -> bounded interpretation
  -> agent or human decision
```

### Candidate entities

| Entity | Purpose |
|--------|---------|
| `Task` | Stable definition of an intended embodied outcome |
| `TaskVariant` | A materially distinct execution form of a task |
| `ExecutionModality` | Keyboard, touch, speech, eye gaze, switch input, agent assistance, etc. |
| `Protocol` | Exact procedure used for training, measurement, simulation, or assessment |
| `Instrument` | Keyboard, application, sensor, timer, or other measurement surface |
| `TaskEpisode` | One situated performance of a task by an actor at a time |
| `Observation` | Directly recorded result or context from an episode |
| `DerivedMeasure` | Computed trend, deviation, fatigue slope, activation gain, or similar output |
| `Interpretation` | Revisable, evidence-linked hypothesis with explicit limits and confidence |
| `Decision` | A human or agent action informed by goals, evidence, preferences, risk, and uncertainty |

These names are candidate vocabulary and remain non-canon until separately reviewed and adopted.

## Foundational distinctions

### Movement, action, task, activity, workflow

- A finger flexion is a **movement**.
- Pressing a key is an **action**.
- Entering text is a **task**.
- Drafting a document is an **activity**.
- Publishing an approved document is a **workflow** outcome.

### Goal vs physical realization

The functional goal may be "produce accurate machine-readable text." Valid realizations include bimanual keyboard typing, one-handed typing, touchscreen entry, speech-to-text, eye-gaze entry, switch input, agent-assisted drafting.

Alternative embodiments and assistive modalities are not task failure when they satisfy the intended functional outcome.

### Capability, performance, capacity, readiness, adaptability, resilience

These must not be collapsed into a single score:

- **Capability:** whether the task can be performed under acceptable conditions.
- **Performance:** how well one episode was executed.
- **Capacity:** how much performance can be sustained.
- **Readiness:** current state relative to the individual's expected range.
- **Adaptability:** stability under changed devices, content, or environments.
- **Resilience:** recovery after interruption, error, fatigue, or temporary impairment.

### Task load vs human strain

- **Task load:** external demands (duration, pace, repetition, precision, complexity, force).
- **Human strain:** actor's response (discomfort, effort, fatigue, error increase, recovery time).

## Task-demand fingerprint

A multidimensional fingerprint rather than a single intensity value:

- **physical:** fine/gross motor, force, precision, stability, range of motion, repetition, posture, bilateral coordination
- **perceptual:** visual discrimination, tactile feedback, proprioception, target acquisition, spatial tracking
- **cognitive:** attention, working memory, language, sequencing, inhibition, planning, error detection, procedural recall
- **temporal:** discrete/continuous, self-paced/externally paced, rhythmic/irregular, burst/sustained
- **contextual:** tool dependence, environmental stability, time pressure, consequence of error, reversibility, safety criticality
- **assistance:** manual, guided, augmented, supervised automation, delegated, fully automated

## Task graph relationships

Candidate relations:

```text
contains
requires
is_variant_of
is_prerequisite_for
trains
measures
transfers_to
substitutes_for
is_assisted_by
is_automated_by
is_performed_with
produces
aggravates
interferes_with
```

The first implementation does not need a graph database. It defines stable, machine-readable relations that can later support graph traversal.

## Privacy and governance boundaries

- Do not retain typed content by default.
- Do not treat fine-grained timing traces as low-sensitivity telemetry.
- Separate task definitions, protocols, raw events, aggregate observations, derived models, interpretations, and decisions into distinct data classes.
- Preserve provenance for every derived measure and interpretation.
- Make deletion and export possible for personal task data.
- Do not reuse wellness-oriented observations for productivity ranking without explicit, separate authorization.
- Do not make diagnostic, employment, insurance, or eligibility claims from this layer.
- Keep all HUMMBL, BaseN, and newly introduced terms marked as candidate/non-canon until audited.

## Non-goals

- Diagnosing cognitive, neurological, musculoskeletal, or medical conditions.
- Creating a universal human-performance score.
- Ranking people or creating a public leaderboard.
- Retaining raw typed content.
- Storing biometric-grade keystroke traces by default.
- Automatically changing high-stakes schedules or work assignments.
- Claiming validated transfer from typing tests to general cognition or occupational performance.
- Replacing the Compendium of Physical Activities.
- Declaring new HUMMBL, BaseN, or Ownward canon.

## Success condition

This initiative succeeds when the repository can represent a physical task, its alternative realizations, a versioned protocol, a situated episode, a provenance-preserving observation, and a bounded interpretation without confusing any of those layers — and when keyboard typing proves that the model can support modern human-machine work while preserving accessibility, privacy, uncertainty, and source boundaries.
