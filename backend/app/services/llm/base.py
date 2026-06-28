from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    """
    Abstract base class for all LLM providers.

    Every provider (Gemini, OpenAI, Ollama, etc.)
    must implement this interface.
    """

    @abstractmethod
    async def generate_response(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> str:
        """
        Generate a response from the LLM.

        Args:
            prompt: User prompt.
            system_prompt: Optional system instruction.

        Returns:
            LLM response text.
        """
        pass