# Data Directory

This directory is intentionally cacheless.

Do not commit upstream Compendium spreadsheets, full tables, exports, or derived local cache files unless a future review explicitly authorizes redistribution.

Local importers may read user-provided source files from this directory during development.

## Test Fixtures

Validation uses synthetic fixtures in `tests/fixtures/` instead of committing upstream
Compendium source rows. Each fixture is minimal, synthetic, and contains only the fields
needed to validate importer contracts.
