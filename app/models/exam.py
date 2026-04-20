from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey, func
from sqlalchemy import Enum as SAEnum
from app.db.base import Base

from app.models.enums import ExamType


class Exam(Base):
    __tablename__ = "exams"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subjects.id", ondelete="CASCADE")
    )
    semester: Mapped[int] = mapped_column(Integer)
    exam_type: Mapped[ExamType] = mapped_column(SAEnum(ExamType))
    exam_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    room: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    duration_minutes: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    subject: Mapped["Subject"] = relationship("Subject", back_populates="exams")
    results: Mapped[list["ExamResult"]] = relationship(
        "ExamResult", back_populates="exams"
    )
