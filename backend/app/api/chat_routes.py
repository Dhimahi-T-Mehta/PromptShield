from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.services.llm.llm_service import LLMService
from app.services.security_pipeline import SecurityPipeline
from app.services.response_guard import ResponseGuard
router = APIRouter()

pipeline = SecurityPipeline()
llm = LLMService()
response_guard = ResponseGuard()


@router.post("/chat")
async def chat(request: ChatRequest):

    analysis = pipeline.analyze_prompt(request.prompt)

    if analysis.action == "BLOCK":
        return {
            **analysis.model_dump(),
            "response": None,
        }

    llm_response = await llm.generate_response(
        prompt=request.prompt,
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