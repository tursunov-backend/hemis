from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, func
from sqlalchemy import Enum as SAEnum

from app.db.base import Base
from app.models.enums import ExamType


class Exam(Base):
    __tablename__ = "exams"

    id: Mapped[int] = mapped_column(primary_key=True)

    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subjects.id", ondelete="CASCADE"),
    )

    semester: Mapped[int] = mapped_column(Integer)

    exam_type: Mapped[ExamType] = mapped_column(SAEnum(ExamType, name="exam_type"))

    exam_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    room: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
    )

    duration_minutes: Mapped[int] = mapped_column(Integer)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    subject: Mapped["Subject"] = relationship("Subject", back_populates="exams")

    results: Mapped[list["ExamResult"]] = relationship(
        "ExamResult", back_populates="exam"
    )


class ExamResult(Base):
    __tablename__ = "exam_results"

    id: Mapped[int] = mapped_column(primary_key=True)

    exam_id: Mapped[int] = mapped_column(
        ForeignKey("exams.id", ondelete="CASCADE"),
    )

    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="CASCADE"),
    )

    score: Mapped[int] = mapped_column(Integer)

    is_passed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    exam: Mapped["Exam"] = relationship("Exam", back_populates="results")

    student: Mapped["Student"] = relationship("Student", back_populates="exam_results")
