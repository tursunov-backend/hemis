from datetime import datetime
from typing import Optional

from sqlalchemy import (
    Integer,
    DateTime,
    ForeignKey,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Grade(Base):
    __tablename__ = "grades"

    id: Mapped[int] = mapped_column(primary_key=True)

    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="CASCADE"),
    )

    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subjects.id", ondelete="CASCADE")
    )

    semester: Mapped[int] = mapped_column(Integer)

    midterm1: Mapped[int] = mapped_column(Integer)  # 0-30
    midterm2: Mapped[int] = mapped_column(Integer)  # 0-30
    final_score: Mapped[int] = mapped_column(Integer)  # 0-40

    total: Mapped[int] = mapped_column(Integer)  # 0-100

    grade_point: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    student: Mapped["Student"] = relationship("Student", back_populates="grades")
    subject: Mapped["Subject"] = relationship("Subject", back_populates="grades")
