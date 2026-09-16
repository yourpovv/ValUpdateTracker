import json
from pathlib import Path
from typing import Optional

from src.core.models import VersionInfo
from src.errors import StateError


def load(path: Path) -> Optional[VersionInfo]:
    if not path.exists():
        return None

    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        if not raw:
            return None
        return VersionInfo(
            version=raw["version"],
            branch=raw["branch"],
            riot_client_version=raw["riot_client_version"],
            riot_client_build=raw["riot_client_build"],
            build_date=raw["build_date"],
        )
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        raise StateError(f"Can't read {path}: {exc}") from exc


def save(path: Path, version: VersionInfo) -> None:
    payload = {
        "version": version.version,
        "branch": version.branch,
        "riot_client_version": version.riot_client_version,
        "riot_client_build": version.riot_client_build,
        "build_date": version.build_date,
    }
    try:
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    except OSError as exc:
        raise StateError(f"Can't write to {path}: {exc}") from exc
