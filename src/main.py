import logging

from src.clients.discord_client import Webhook, notify
from src.clients.valorant_client import fetch_version
from src.core.diff import diff
from src.settings import settings
from src.storage.state import load, save

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("update_tracker")


def run() -> None:
    previous = load(settings.state_file)
    current = fetch_version(settings.request_timeout_seconds)
    event = diff(previous, current)

    if event is None:
        logger.info("No update. version=%s", current.version)
    else:
        webhook = Webhook(settings.discord_webhook_url, settings.request_timeout_seconds)
        notify(webhook, event, current)
        logger.info("Notified: %s %s -> %s", event.type, event.previous, event.current)

    save(settings.state_file, current)


if __name__ == "__main__":
    run()
