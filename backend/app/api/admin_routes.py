from fastapi import APIRouter, Depends

from app.auth.dependencies import require_admin

router = APIRouter(
    prefix="/admin",
    tags=["Administration"],
)


@router.get("/status")
def admin_status(
    current_user: dict = Depends(require_admin),
):
    """
    Test endpoint for administrator access.
    """

    return {
        "message": "Administrator access granted.",
        "user": current_user["sub"],
        "role": current_user["role"],
    }