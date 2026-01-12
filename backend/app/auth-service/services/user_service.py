from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.user import User
from core.security import hash_password, verify_password
from schemas.user import RegisterSchema
from core.roles import ROLE_MAP


async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


async def create_user(db: AsyncSession, data: RegisterSchema):
    user = User(
        role=data.role,
        email=data.email,
        name=data.name,
        hashed_password=hash_password(data.password),
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)

    user.employee_id = f"{ROLE_MAP.get(user.role, 'UNKNOWN')}_{user.id}"

    await db.commit()
    await db.refresh(user)
    return user


async def authenticate_user(db: AsyncSession, email: str, password: str):
    user = await get_user_by_email(db, email)
    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user
