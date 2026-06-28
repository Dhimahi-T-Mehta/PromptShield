from google import genai

from app.core.config import settings
from app.services.llm.base import BaseLLMProvider


class GeminiService(BaseLLMProvider):
    """
    Google Gemini Provider using the new google-genai SDK.
    """

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    async def generate_response(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> str:

        try:

            final_prompt = prompt

            if system_prompt:
                final_prompt = (
                    f"{system_prompt}\n\n{prompt}"
                )

            response = self.client.models.generate_content(
                model=settings.GEMINI_MODEL,
                contents=final_prompt,
            )

            return response.text

        except Exception as e:
            raise RuntimeError(
                f"Gemini API Error: {e}"
            )