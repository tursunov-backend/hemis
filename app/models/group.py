from datetime import datetime
from app.db.base import Base

from sqlalchemy import DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id", ondelete="CASCADE")
    )
    course: Mapped[int] = mapped_column(Integer)  # 1, 2, 3, 4
    education_form: Mapped[str] = mapped_column(String(20))  # kunduzgi, masofaviy
    education_lang: Mapped[str] = mapped_column(String(20))  # uzbek, rus
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    department: Mapped["Department"] = relationship(
        "Department", back_populates="groups"
    )
    students: Mapped[list["Student"]] = relationship("Student", back_populates="groups")
    schedules: Mapped[list["Schedule"]] = relationship(
        "Schedule", back_populates="groups"
    )
