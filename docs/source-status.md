# Source Status

Status: `canonical_external_source_adapter`

The Compendium of Physical Activities is the canonical external source. This repository provides HUMMBL adapter infrastructure for source boundaries, schemas, validation, and provenance.

Official source checked on 2026-07-04:

- <https://pacompendium.com/>

The official site states that Adult, Older Adult, and Wheelchair Compendia are free to use for commercial purposes and asks users not to change MET values or combine activities with different MET levels. This repository preserves that boundary by default.

## Repository Boundary

This repo may include:

- source and citation metadata;
- import specifications;
- schemas;
- validation logic;
- test fixtures that do not reproduce full upstream tables;
- provenance receipts.

This repo should not include:

- full upstream Compendium tables;
- user-downloaded spreadsheets;
- modified upstream MET values;
- medical advice or user-specific protocols.
