from fastapi import APIRouter, HTTPException

from app.auth.jwt_handler import create_access_token
from app.auth.password import verify_password
from app.database.users import get_user_by_username
from app.models.user_models import UserLogin

from app.models.user_models import (
    UserLogin,
    TokenResponse,
)

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(credentials: UserLogin):

    user = get_user_by_username(
        credentials.username
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password.",
        )

    if not verify_password(
        credentials.password,
        user[4],      # password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password.",
        )

    access_token = create_access_token(
        {
            "sub": user[1],     # username
            "role": user[5],    # role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": 1800,
    }