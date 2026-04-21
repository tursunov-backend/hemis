from datetime import datetime, timezone

from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(200))
    code: Mapped[str] = mapped_column(String(20), unique=True)
    credits: Mapped[int] = mapped_column(Integer)
    semester: Mapped[int] = mapped_column(Integer)

    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id", ondelete="CASCADE")
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )

    department: Mapped["Department"] = relationship(
        "Department", back_populates="subjects"
    )

    schedules: Mapped[list["Schedule"]] = relationship(
        "Schedule", back_populates="subjects", cascade="all, delete-orphan"
    )

    grades: Mapped[list["Grade"]] = relationship(
        "Grade", back_populates="subjects", cascade="all, delete-orphan"
    )

    exam_results: Mapped[list["ExamResult"]] = relationship(
        "ExamResult", back_populates="subjects", cascade="all, delete-orphan"
    )