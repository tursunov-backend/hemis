from datetime import date, datetime
from typing import Optional
from decimal import Decimal

from sqlalchemy import String, Date, Boolean, Numeric, DateTime, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Contract(Base):
    __tablename__ = "contracts"

    id: Mapped[int] = mapped_column(primary_key=True)

    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="CASCADE"),
    )

    contract_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
    )

    academic_year: Mapped[str] = mapped_column(String(20))  # "2024-2025"

    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2))

    paid_amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2), server_default=text("0")
    )

    due_date: Mapped[date] = mapped_column(Date)

    is_paid: Mapped[bool] = mapped_column(Boolean, server_default=text("false"))

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    student: Mapped["Student"] = relationship("Student", back_populates="contracts")


class Scholarship(Base):
    __tablename__ = "scholarships"

    id: Mapped[int] = mapped_column(primary_key=True)

    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="CASCADE"),
    )

    month: Mapped[date] = mapped_column(
        Date,
    )

    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    is_paid: Mapped[bool] = mapped_column(Boolean, server_default=text("false"))

    paid_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    student: Mapped["Student"] = relationship("Student", back_populates="scholarships")