from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.auth.jwt_handler import decode_access_token

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    """
    Validate the JWT and return the token payload.
    """

    payload = decode_access_token(
        credentials.credentials
    )

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token.",
        )

    return payload

def require_admin(
    current_user: dict = Depends(get_current_user),
):
    """
    Allow access only to administrators.
    """

    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Administrator access required.",
        )

    return current_user


def require_user(
    current_user: dict = Depends(get_current_user),
):
    """
    Any authenticated user.
    """

    allowed_roles = [
        "admin",
        "analyst",
        "user",
    ]

    if current_user.get("role") not in allowed_roles:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User access required.",
        )

    return current_user

def require_analyst(
    current_user: dict = Depends(get_current_user),
):
    """
    Analyst or Administrator.
    """

    allowed_roles = [
        "admin",
        "analyst",
    ]

    if current_user.get("role") not in allowed_roles:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Analyst access required.",
        )

    return current_user