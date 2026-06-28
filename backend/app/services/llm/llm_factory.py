import os

from app.services.llm.providers.gemini_service import GeminiService
from app.services.llm.providers.openai_service import OpenAIService
from app.services.llm.providers.ollama_service import OllamaService
from app.core.config import settings

class LLMFactory:
    """
    Factory responsible for returning
    the configured LLM provider.
    """

    @staticmethod
    def get_provider():

        provider = settings.LLM_PROVIDER.lower()

        if provider == "gemini":
            return GeminiService()

        if provider == "openai":
            return OpenAIService()

        if provider == "ollama":
            return OllamaService()

        raise ValueError(
            f"Unsupported LLM provider: {provider}"
        )