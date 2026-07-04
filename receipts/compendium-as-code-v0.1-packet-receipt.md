# Receipt: compendium-as-code executable v0.1 packet

## Packet identity

- Repo: `compendium-as-code`
- Packet status: `seed -> v0.1-draft`
- Packet folder: `.` (repository root)
- Scope source: `compendium-as-code #4`
- PR target: `chore/codex/compendium-as-code-v0-1-packet-main` (this change set)

## Included artifacts

- `docs/v0.1-boundary.md`
- `schemas/compendium-as-code-v0.1.json`
- `examples/compendium-source-v0.1.example.json`
- `fixtures/valid/compendium-source-v0.1.valid.json`
- `fixtures/invalid/compendium-source-v0.1.invalid.json`
- `receipts/compendium-as-code-v0.1-packet-receipt.md`

## Status transitions

- `seed` -> `v0.1-draft` (artifact presence + explicit packet structure)
- `v0.1-draft` -> `validated-example` (valid fixture added)
- `validated-example` -> pending `v0.1-packet` (requires non-author review + final merge)

## Non-canon guardrail

- This packet is non-canon until HUMMBL authority explicitly adopts it.
- No claims of legal compliance, redistribution authority, or canonical compendium values are introduced here.

## Validation checks executed

- Directory contract check: `docs/`, `schemas/`, `examples/`, `fixtures/valid/`, `fixtures/invalid/`, `receipts/`
- Structural review against `docs/v0.1-boundary.md` and `hummbl-dev#70`
- Schema validation uses `jsonschema.Draft202012Validator` with `FormatChecker`; `source.uri` also has an explicit URI-scheme pattern so malformed source locations fail in local validation.
- Negative fixture includes an explicit `additionalProperties` schema failure, authority boundary violation, manifest version floor, URI pattern, and validation-count cases.
