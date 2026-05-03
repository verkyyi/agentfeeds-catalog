from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate-stream.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_stream", VALIDATOR)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_all_streams_validate():
    validator = load_validator()
    for path in sorted((ROOT / "catalog" / "streams").glob("**/*.yaml")):
        validator.validate_stream(path)


def test_index_matches_streams():
    index = json.loads((ROOT / "catalog" / "INDEX.json").read_text(encoding="utf-8"))
    streams = sorted((ROOT / "catalog" / "streams").glob("**/*.yaml"))
    assert index["stream_count"] == len(streams)
    assert sorted(stream["path"] for stream in index["streams"]) == [
        str(path.relative_to(ROOT)) for path in streams
    ]


def test_template_ids_are_unique():
    ids = []
    for path in sorted((ROOT / "catalog" / "streams").glob("**/*.yaml")):
        ids.append(yaml.safe_load(path.read_text(encoding="utf-8"))["id"])
    duplicates = sorted({stream_id for stream_id in ids if ids.count(stream_id) > 1})
    assert duplicates == []


def test_public_catalog_does_not_ship_local_command_templates():
    for path in sorted((ROOT / "catalog" / "streams").glob("**/*.yaml")):
        stream = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert stream["adapter"]["kind"] != "local_command", path
