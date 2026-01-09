from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from schemas.user import RegisterSchema, LoginSchema, TokenSchema
from services.user_service import create_user, authenticate_user, get_user_by_email
from core.security import create_access_token
from core.dependencies import get_current_user

router = APIRouter(tags=["Auth"])


@router.post("/register", status_code=201)
async def register(data: RegisterSchema, db: AsyncSession = Depends(get_db)):
    existing = await get_user_by_email(db, data.email)
    if existing:
        raise HTTPException(400, "Email already registered")

    user = await create_user(db, data)
    return {"id": user.id, "email": user.email}


@router.post("/login", response_model=TokenSchema)
async def login(data: LoginSchema, db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, data.email, data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token}


@router.get("/profile")
async def profile(user_id: str = Depends(get_current_user)):
    return {"user_id": user_id}
