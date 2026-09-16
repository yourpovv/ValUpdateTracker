import requests

from src.core.models import VersionInfo
from src.errors import ValorantAPIError

VERSION_URL = "https://valorant-api.com/v1/version"


def fetch_version(timeout_seconds: int) -> VersionInfo:
    try:
        response = requests.get(VERSION_URL, timeout=timeout_seconds)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise ValorantAPIError(f"Can't reach valorant-api.com: {exc}") from exc

    try:
        payload = response.json()
    except ValueError as exc:
        raise ValorantAPIError(f"valorant-api.com sent back something unexpected: {exc}") from exc

    version_data = payload.get("data")
    if not isinstance(version_data, dict):
        raise ValorantAPIError("valorant-api.com sent back something unexpected")

    try:
        return VersionInfo(
            version=version_data["version"],
            branch=version_data["branch"],
            riot_client_version=version_data["riotClientVersion"],
            riot_client_build=version_data["riotClientBuild"],
            build_date=version_data["buildDate"],
        )
    except KeyError as exc:
        raise ValorantAPIError(f"valorant-api.com response is missing {exc}") from exc
