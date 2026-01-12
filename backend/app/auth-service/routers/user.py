from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from schemas.user import RegisterSchema, LoginSchema, TokenSchema
from services.user_service import (
    create_user,
    authenticate_user,
    get_user_by_email,
)
from core.security import create_access_token
from core.dependencies import get_current_user
from core.roles import Role
from core.permissions import require_role
from core.response import success_response, error_response

router = APIRouter(tags=["Auth"])


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    # dependencies=[Depends(require_role(Role.MANAGER))],
)
async def register(
    data: RegisterSchema,
    db: AsyncSession = Depends(get_db),
):
    existing = await get_user_by_email(db, data.email)
    if existing:
        return error_response(
            message="Email already registered",
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    user = await create_user(db, data)

    return success_response(
        data={
            "id": user.id,
            "email": user.email,
            "role": user.role,
        },
        message="User registered successfully",
        status_code=status.HTTP_201_CREATED,
    )


@router.post("/login", response_model=TokenSchema)
async def login(
    data: LoginSchema,
    db: AsyncSession = Depends(get_db),
):
    user = await authenticate_user(db, data.email, data.password)
    if not user:
        return error_response(
            message="Invalid email or password",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    token = create_access_token(
        {
            "sub": str(user.id),
            "role": int(user.role),
        }
    )

    return success_response(
        data={
            "access_token": token,
            "token_type": "bearer",
        },
        message="Login successful",
    )


@router.get("/profile")
async def profile(
    user=Depends(get_current_user),
):
    return success_response(
        data={
            "user_id": user["user_id"],
            "role": user["role"],
        },
        message="Profile fetched successfully",
    )
