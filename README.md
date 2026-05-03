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
examples/
└── streams/
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
- Lead the catalog with standing-relationship sources: macOS Calendar, Reminders, Notes, Mail, Messages, local files, local repos, and personal SaaS APIs.
- Use `catalog_tier` to guide presentation:
  - `1`: macOS-native demo-maker streams.
  - `2`: local files and developer context.
  - `3`: bearer-token APIs that require Keychain-backed credentials.
  - `4`: flexible long-tail public templates.
- Use `catalog_order` for explicit ordering inside each tier.

## macOS TCC Permissions

Mac-native templates should never silently work around privacy prompts. If a required TCC permission has not been granted, the fetch should fail with a known error and the skill should tell the user which System Settings panel to visit and why.

Permission mapping:

- Calendar adapters require Calendar permission for the terminal or host process.
- Reminders adapters require Reminders permission.
- Notes adapters require Automation permission for Notes.app.
- Mail adapters require Automation permission for Mail.app.
- iMessage adapters require Full Disk Access for read-only access to `~/Library/Messages/chat.db`.
- Safari Reading List reads `~/Library/Safari/Bookmarks.plist` and does not require a TCC prompt.
- Recent Downloads reads `~/Downloads` and does not require a TCC prompt.
