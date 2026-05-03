# Agent Feeds Catalog

Built-in provider definitions and schemas for Agent Feeds.

This repo hosts the public catalog consumed by the Agent Feeds core CLI. Providers are YAML stream definitions under `catalog/streams/`; schemas live under `catalog/schemas/`.

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

## Provider Guidelines

- Prefer providers that require no authentication.
- Keep provider descriptions short and operator-facing.
- Use stable `category/name` provider IDs.
- Add or reuse an event schema for every stream definition.
- Mark new providers `quality_tier: experimental` until they have real usage.
- Do not include user-specific secrets, tokens, paths, or account IDs.
