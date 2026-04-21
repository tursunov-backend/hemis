from datetime import datetime, timezone

from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    middle_name: Mapped[str | None] = mapped_column(String(100), nullable=True)

    email: Mapped[str | None] = mapped_column(String(255), unique=True, nullable=True)
    phone: Mapped[str | None] = mapped_column(String(20), nullable=True)

    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id", ondelete="CASCADE")
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )

    department: Mapped["Department"] = relationship(
        "Department", back_populates="teachers"
    )

    schedules: Mapped[list["Schedule"]] = relationship(
        "Schedule", back_populates="teachers", cascade="all, delete-orphan"
    )
