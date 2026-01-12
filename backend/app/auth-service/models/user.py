from datetime import datetime
from sqlalchemy import String, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from core.database import Base
from core.roles import Role


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(String(200), nullable=False)
    employee_id: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
        unique=True,
    )

    role: Mapped[int] = mapped_column(
        Integer,
        default=Role.MANAGER,
        nullable=False,
    )  # manager = 1 , waiter = 2 , cashier = 3

    status: Mapped[int] = mapped_column(Integer, default=1)  # 1=active, 0=inactive

    email: Mapped[str] = mapped_column(
        String(120), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
