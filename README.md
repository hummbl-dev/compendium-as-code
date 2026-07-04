# compendium-as-code

`compendium-as-code` is a governed source-adapter and validation layer for the Compendium of Physical Activities.

It preserves upstream source boundaries, citations, release lineage, activity-code semantics, MET semantics, and HUMMBL-specific derived annotations without modifying upstream values.

## Status

Public seed repository. Source-adapter infrastructure only.

## Hard Boundary

This repository does not vendor or mirror full upstream Compendium tables.

Use this repo for:

- source status and citation receipts;
- schema definitions;
- import specifications;
- validation tests;
- provenance and lineage notes;
- empty/cacheless local data directories.

Do not use this repo to redistribute upstream spreadsheets or full tables unless licensing and redistribution terms are explicitly reviewed and recorded.

## Core Invariants

```yaml
do_not_change_upstream_met_values: true
do_not_merge_distinct_met_activities: true
preserve_original_activity_code: true
preserve_original_activity_description: true
all_derived_fields_must_be_marked: true
all_hummbl_mappings_are_non_upstream_annotations: true
```

## Canonical External Source

Canonical external title: **Compendium of Physical Activities**

Official site: <https://pacompendium.com/>

This repo treats the Compendium as a canonical external source adapter, not HUMMBL-owned canon.

## Data Directory

`data/` is intentionally cacheless. User-provided upstream downloads may be used locally for validation, but upstream data files should not be committed unless a future review explicitly authorizes redistribution.
