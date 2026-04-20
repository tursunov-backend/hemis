from datetime import datetime
from typing import Optional
from sqlalchemy import Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class Grade(Base):
    __tablename__ = "grades"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="CASCADE")
    )
    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subjects.id", ondelete="CASCADE")
    )
    semester: Mapped[int] = mapped_column(Integer)
    midterm1: Mapped[int] = mapped_column(Integer)  # 0-30  (1-oraliq ma'ruza)
    midterm2: Mapped[int] = mapped_column(Integer)  # 0-20  (1-oraliq amaliy)
    final_score: Mapped[int] = mapped_column(Integer)  # 0-50  (yakuniy)
    total: Mapped[int] = mapped_column(Integer)
    grade_point: Mapped[Optional[int]] = mapped_column(
        Integer, nullable=True
    )  # 2, 3, 4, 5
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    student: Mapped["Student"] = relationship("Student", back_populates="grades")
    subject: Mapped["Subject"] = relationship("Subject", back_populates="grades")
