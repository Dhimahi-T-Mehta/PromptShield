import requests
from typing import Optional

from .config import PromptShieldConfig
from .exceptions import APIConnectionError, APIResponseError
from .models import (
    Explanation,
    Sanitization,
    ResponseAnalysis,
    ScanResult,
    HealthStatus,
)


# ============================================================
# Low-Level HTTP Client
# ============================================================

class PromptShieldClient:
    """
    Low-level HTTP client used internally by the SDK.
    """

    def __init__(self, config: PromptShieldConfig | None = None):
        self.config = config or PromptShieldConfig()

        self.base_url = self.config.base_url.rstrip("/")
        self.timeout = self.config.timeout
        self.provider = self.config.provider

    # --------------------------------------------------------

    def _get(self, endpoint: str) -> dict:
        try:
            response = requests.get(
                f"{self.base_url}{endpoint}",
                timeout=self.timeout,
            )

            response.raise_for_status()
            return response.json()

        except requests.exceptions.ConnectionError:
            raise APIConnectionError(
                "Unable to connect to PromptShield server."
            )

        except requests.exceptions.HTTPError as e:
            raise APIResponseError(str(e))

    # --------------------------------------------------------

    def _post(self, endpoint: str, payload: dict) -> dict:
        try:
            response = requests.post(
                f"{self.base_url}{endpoint}",
                json=payload,
                timeout=self.timeout,
            )

            response.raise_for_status()
            return response.json()

        except requests.exceptions.ConnectionError:
            raise APIConnectionError(
                "Unable to connect to PromptShield server."
            )

        except requests.exceptions.HTTPError as e:
            raise APIResponseError(str(e))

    # --------------------------------------------------------

    def detect(self, prompt: str):
        return self._post(
            "/detect",
            {
                "prompt": prompt,
            },
        )

    # --------------------------------------------------------

    def chat(
        self,
        prompt: str,
        provider: Optional[str] = None,
    ):
        return self._post(
            "/chat",
            {
                "prompt": prompt,
                "provider": provider or self.provider,
            },
        )

    # --------------------------------------------------------

    def health(self) -> HealthStatus:
        data = self._get("/health")

        return HealthStatus(
            status=data.get("status", "unknown"),
            version=data.get("version", ""),
            provider=data.get("provider"),
        )


# ============================================================
# Public SDK
# ============================================================

class PromptShield:

    def __init__(
        self,
        config: PromptShieldConfig | None = None,
    ):

        self.config = config or PromptShieldConfig()

        self.client = PromptShieldClient(self.config)

    # --------------------------------------------------------

    @staticmethod
    def _build_result(data: dict) -> ScanResult:

        explanation = (
            Explanation(**data["explanation"])
            if data.get("explanation")
            else None
        )

        sanitization = (
            Sanitization(**data["sanitization"])
            if data.get("sanitization")
            else None
        )

        response_analysis = (
            ResponseAnalysis(**data["response_analysis"])
            if data.get("response_analysis")
            else None
        )

        return ScanResult(
            attack_type=data.get("attack_type", ""),
            confidence=data.get("confidence", 0.0),
            risk_score=data.get("risk_score", 0),
            action=data.get("action", ""),
            explanation=explanation,
            pii_entities=data.get("pii_entities"),
            matched_keywords=data.get("matched_keywords"),
            matched_patterns=data.get("matched_patterns"),
            sanitized_text=data.get("sanitized_text"),
            sanitization=sanitization,
            response=data.get("response"),
            response_analysis=response_analysis,
        )

    # --------------------------------------------------------

    def scan(self, prompt: str) -> ScanResult:

        if not isinstance(prompt, str):
            raise TypeError("prompt must be a string.")

        prompt = prompt.strip()

        if not prompt:
            raise ValueError("prompt cannot be empty.")

        result = self.client.detect(prompt)

        return self._build_result(result)

    # --------------------------------------------------------

    def chat(
        self,
        prompt: str,
        provider: Optional[str] = None,
    ) -> ScanResult:

        if not isinstance(prompt, str):
            raise TypeError("prompt must be a string.")

        prompt = prompt.strip()

        if not prompt:
            raise ValueError("prompt cannot be empty.")

        provider = provider or self.config.provider

        if provider not in {
            "gemini",
            "openai",
            "ollama",
        }:
            raise ValueError(
                f"Unsupported provider: {provider}"
            )

        result = self.client.chat(
            prompt=prompt,
            provider=provider,
        )

        return self._build_result(result)

    # --------------------------------------------------------

    def ask(
        self,
        prompt: str,
        provider: Optional[str] = None,
    ) -> str:

        return self.chat(
            prompt,
            provider,
        ).response

    # --------------------------------------------------------

    def secure_chat(
        self,
        prompt: str,
        provider: Optional[str] = None,
    ) -> ScanResult:

        return self.chat(
            prompt,
            provider,
        )

    # --------------------------------------------------------

    def health(self) -> HealthStatus:
        return self.client.health()

    # --------------------------------------------------------

    def is_safe(self, prompt: str) -> bool:
        return self.scan(prompt).action == "ALLOW"

    # --------------------------------------------------------

    def risk_score(self, prompt: str) -> int:
        return self.scan(prompt).risk_score

    # --------------------------------------------------------

    def attack_type(self, prompt: str) -> str:
        return self.scan(prompt).attack_type