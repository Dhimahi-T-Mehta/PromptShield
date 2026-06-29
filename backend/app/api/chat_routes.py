from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.services.llm.llm_service import LLMService
from app.services.security_pipeline import SecurityPipeline
from app.services.response_guard import ResponseGuard
from app.services.prompt_sanitizer import PromptSanitizer

router = APIRouter()

pipeline = SecurityPipeline()
llm = LLMService()
response_guard = ResponseGuard()
sanitizer = PromptSanitizer()

@router.post("/chat")
async def chat(request: ChatRequest):

    analysis = pipeline.analyze_prompt(request.prompt)

    prompt_to_send = request.prompt

    sanitization = None

    # Only attempt recovery for blocked prompts
    if analysis.action == "BLOCK":

        sanitization = sanitizer.sanitize(request.prompt)

        if (
            sanitization is not None
            and sanitization.modified
            and sanitization.sanitized_prompt.strip()
        ):

            prompt_to_send = sanitization.sanitized_prompt

            analysis = pipeline.analyze_prompt(prompt_to_send)     
       
    if analysis.action == "BLOCK":

        return {
            **analysis.model_dump(),
            "sanitization": (
                sanitization.model_dump()
                if sanitization
                else None
            ),
            "response": None,
        }

    print("=" * 60)
    print("Original Prompt:")
    print(request.prompt)

    print("-" * 60)

    print("Sanitized Prompt:")
    print(prompt_to_send)

    print("-" * 60)

    print("Final Analysis:")
    print(analysis)

    print("=" * 60)


    llm_response = await llm.generate_response(
        prompt=prompt_to_send,
        system_prompt=request.system_prompt,
    )

    response_analysis = response_guard.analyze_response(
        llm_response
    )

    if response_analysis.action == "BLOCK":
        return {
            **analysis.model_dump(),
            "response": None,
            "response_analysis": response_analysis.model_dump(),
        }

    return {
        **analysis.model_dump(),
        "response": response_analysis.sanitized_response,
        "response_analysis": response_analysis.model_dump(),
    }