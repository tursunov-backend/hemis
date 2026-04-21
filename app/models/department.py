from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, DateTime, func, UniqueConstraint

from app.db.base import Base


class Department(Base):
    __tablename__ = "departments"

    __table_args__ = (UniqueConstraint("faculty_id", "name"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(100))
    code: Mapped[str] = mapped_column(String(20), unique=True)

    faculty_id: Mapped[int] = mapped_column(
        ForeignKey("faculties.id", ondelete="CASCADE"),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    faculty: Mapped["Faculty"] = relationship("Faculty", back_populates="departments")

    groups: Mapped[list["Group"]] = relationship("Group", back_populates="department")

    teachers: Mapped[list["Teacher"]] = relationship(
        "Teacher", back_populates="department"
    )

    subjects: Mapped[list["Subject"]] = relationship(
        "Subject", back_populates="department"
    )
