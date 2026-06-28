from app.services.llm.llm_factory import LLMFactory

class LLMService:
    """
    High-level service responsible for
    interacting with the configured LLM.
    """

    def __init__(self):
        self.provider = LLMFactory.get_provider()

    async def generate_response(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ):

        return await self.provider.generate_response(
            prompt,
            system_prompt,
        )