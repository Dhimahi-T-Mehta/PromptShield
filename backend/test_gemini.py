import asyncio

from app.services.llm.llm_service import LLMService


async def main():

    llm = LLMService()

    response = await llm.generate_response(
        "What is Prompt Injection?"
    )

    print(response)


asyncio.run(main())