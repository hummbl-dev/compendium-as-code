# Canonical Boundaries

`compendium-as-code` is not the Compendium of Physical Activities.

It is a governed adapter layer for:

- preserving source references;
- validating activity-code and MET semantics;
- distinguishing upstream values from HUMMBL annotations;
- documenting release lineage;
- supporting import from user-provided local files.

## Invariants

- Do not change upstream MET values.
- Do not merge distinct activities with different MET levels.
- Preserve original activity code.
- Preserve original activity description.
- Mark all derived fields.
- Mark HUMMBL mappings as non-upstream annotations.
- Validate fixture-backed import semantics before promoting adapter maturity.
