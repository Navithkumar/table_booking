from datetime import datetime
from sqlalchemy import Integer, String, DateTime, func
from core.database import Base
from core.status import Status
from sqlalchemy.orm import Mapped, mapped_column


class Table(Base):
    __tablename__ = "tables"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    seating_capacity: Mapped[int] = mapped_column(String(200), nullable=False)
    table_no: Mapped[str] = mapped_column(String(200), nullable=False)
    status: Mapped[int] = mapped_column(
        Integer,
        default=Status.AVAILABLE,
        nullable=False,
    )  # AVAILABLE = 1 ,OCCUPIED = 2,BILL_REQUESTED = 3,CLOSED = 4
    managed_staff: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
