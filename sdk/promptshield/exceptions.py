class PromptShieldError(Exception):
    """Base PromptShield SDK exception."""


class APIConnectionError(PromptShieldError):
    """Cannot connect to PromptShield server."""


class APIResponseError(PromptShieldError):
    """PromptShield returned an error."""