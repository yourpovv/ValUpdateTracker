from dataclasses import dataclass

import requests

from src.core.models import GAME, UpdateEvent, VersionInfo
from src.errors import WebhookError

GAME_UPDATE_COLOR = 0xFF4655
VANGUARD_UPDATE_COLOR = 0x00C2FF


@dataclass(frozen=True)
class Webhook:
    url: str
    timeout_seconds: int


def notify(webhook: Webhook, event: UpdateEvent, current: VersionInfo) -> None:
    payload = {
        "username": "Valorant Update Tracker",
        "embeds": [_embed(event, current)],
    }
    try:
        response = requests.post(webhook.url, json=payload, timeout=webhook.timeout_seconds)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise WebhookError(f"Discord didn't accept the notification: {exc}") from exc


def _embed(event: UpdateEvent, current: VersionInfo) -> dict:
    if event.type == GAME:
        title = "VALORANT Updated"
        color = GAME_UPDATE_COLOR
    else:
        title = "Vanguard Updated"
        color = VANGUARD_UPDATE_COLOR

    return {
        "title": title,
        "color": color,
        "fields": [
            {"name": "Previous Version", "value": event.previous, "inline": True},
            {"name": "Latest Version", "value": event.current, "inline": True},
            {"name": "Branch", "value": current.branch, "inline": False},
        ],
        "timestamp": event.detected_at.isoformat(),
    }
