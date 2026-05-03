# Agent Feeds Template Catalog

Built-in template definitions and schemas for Agent Feeds.

This repo hosts the public catalog consumed by the Agent Feeds skill runtime. Templates are YAML stream definitions under `catalog/streams/`; schemas live under `catalog/schemas/`.

The Agent Feeds skill bundle ships a frozen snapshot of this catalog for offline first-run discovery. Runtime installs can still refresh `~/.agentfeeds/catalog-cache/` from this repo or from a local checkout with `AGENTFEEDS_CATALOG_DIR`.

## Layout

```text
catalog/
├── INDEX.json
├── streams/
└── schemas/
    └── event-types/
scripts/
├── build-index.py
└── validate-stream.py
tests/
└── test_catalog.py
```

## Validate

```bash
uv run pytest
```

Regenerate the catalog index after changing streams:

```bash
uv run python scripts/build-index.py
```

## Template Guidelines

- Prefer templates that require no authentication.
- Keep template descriptions short and operator-facing.
- Use stable `category/name` template IDs.
- Add or reuse an event schema for every stream definition.
- Mark new templates `quality_tier: experimental` until they have real usage.
- Do not include user-specific secrets, tokens, paths, or account IDs.
- Do not add `local_command` templates to the public catalog. Command templates are operator-local, require explicit approval in the runtime, and belong under `~/.agentfeeds/templates/`.
