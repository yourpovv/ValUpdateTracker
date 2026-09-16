import os
import sys
import time
from pathlib import Path

WAIT_SECONDS = 900


def _base_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).resolve().parent.parent


def _webhook_set(env_path: Path) -> bool:
    if not env_path.exists():
        return False
    for line in env_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("DISCORD_WEBHOOK_URL=") and line.split("=", 1)[1].strip():
            return True
    return False


def _check_webhook(env_path: Path) -> None:
    if _webhook_set(env_path):
        return

    webhook_url = input("Discord webhook URL: ").strip()
    env_path.write_text(f"DISCORD_WEBHOOK_URL={webhook_url}\n", encoding="utf-8")
    print(f"Saved to {env_path.name}\n")


def main() -> None:
    os.chdir(_base_dir())
    _check_webhook(Path(".env"))

    from src.main import run

    minutes = WAIT_SECONDS // 60
    print(f"Checking every {minutes} min. Ctrl+C to stop.\n")
    while True:
        try:
            run()
        except Exception as exc:
            print(f"Check failed: {exc}")
        time.sleep(WAIT_SECONDS)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped.")
