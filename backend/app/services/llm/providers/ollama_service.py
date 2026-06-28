from app.services.llm.base import BaseLLMProvider


class OllamaService(BaseLLMProvider):
    """
    Ollama Local LLM Provider.
    """

    async def generate_response(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> str:

        raise NotImplementedError(
            "Ollama integration not implemented yet."
        )