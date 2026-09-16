from dataclasses import dataclass
from datetime import datetime
from typing import Literal

UpdateType = Literal["game", "vanguard"]
GAME: UpdateType = "game"
VANGUARD: UpdateType = "vanguard"


@dataclass(frozen=True)
class VersionInfo:
    version: str
    branch: str
    riot_client_version: str
    riot_client_build: str
    build_date: str


@dataclass(frozen=True)
class UpdateEvent:
    type: UpdateType
    previous: str
    current: str
    detected_at: datetime
