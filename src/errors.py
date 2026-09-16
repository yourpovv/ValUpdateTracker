class ValorantAPIError(Exception):
    """valorant-api.com didn't respond how we expected"""


class WebhookError(Exception):
    """The Discord webhook didn't go through"""


class StateError(Exception):
    """The saved version couldn't be read or written"""
