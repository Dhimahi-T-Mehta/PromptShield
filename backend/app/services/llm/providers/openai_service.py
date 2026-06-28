from app.services.llm.base import BaseLLMProvider


class OpenAIService(BaseLLMProvider):
    """
    OpenAI LLM Provider.
    """

    async def generate_response(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> str:

        raise NotImplementedError(
            "OpenAI integration not implemented yet."
        )