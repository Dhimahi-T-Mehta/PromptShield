from dataclasses import dataclass


@dataclass
class PromptShieldConfig:
    """
    SDK configuration.
    """

    base_url: str = "http://127.0.0.1:8000/api/v1"
    provider: str = "gemini"
    timeout: int = 60