from datetime import datetime, timezone
from typing import Optional

from src.core.models import GAME, VANGUARD, UpdateEvent, VersionInfo


def diff(previous: Optional[VersionInfo], current: VersionInfo) -> Optional[UpdateEvent]:
    if previous is None:
        return None

    now = datetime.now(timezone.utc)

    if previous.version != current.version:
        return UpdateEvent(
            type=GAME, previous=previous.version, current=current.version, detected_at=now
        )

    if previous.riot_client_build != current.riot_client_build:
        return UpdateEvent(
            type=VANGUARD,
            previous=previous.riot_client_build,
            current=current.riot_client_build,
            detected_at=now,
        )

    return None
