from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
    Enum,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import EducationForm, EducationLang


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(50))

    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id", ondelete="CASCADE"),
    )

    course: Mapped[int] = mapped_column(Integer)  # 1, 2, 3, 4

    education_form: Mapped[EducationForm] = mapped_column(
        Enum(EducationForm, name="education_form")
    )

    education_lang: Mapped[EducationLang] = mapped_column(
        Enum(EducationLang, name="education_lang")
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    department: Mapped["Department"] = relationship(
        "Department", back_populates="groups"
    )

    students: Mapped[list["Student"]] = relationship("Student", back_populates="group")

    schedules: Mapped[list["Schedule"]] = relationship(
        "Schedule", back_populates="group"
    )