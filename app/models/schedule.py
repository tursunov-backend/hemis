from datetime import datetime, timezone, time

from sqlalchemy import Integer, String, Time, DateTime, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import LessonType, DayOfWeek, LessonNumber


class Schedule(Base):
    __tablename__ = "schedules"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subjects.id", ondelete="CASCADE")
    )

    teacher_id: Mapped[int] = mapped_column(
        ForeignKey("teachers.id", ondelete="CASCADE")
    )

    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id", ondelete="CASCADE"))

    semester: Mapped[int] = mapped_column(Integer)

    day_of_week: Mapped[DayOfWeek] = mapped_column(Enum(DayOfWeek))

    lesson_number: Mapped[LessonNumber] = mapped_column(Enum(LessonNumber))

    start_time: Mapped[time] = mapped_column(Time)
    end_time: Mapped[time] = mapped_column(Time)

    room: Mapped[str | None] = mapped_column(String(50), nullable=True)

    lesson_type: Mapped[LessonType] = mapped_column(Enum(LessonType))

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )

    subject: Mapped["Subject"] = relationship("Subject", back_populates="schedules")
    teacher: Mapped["Teacher"] = relationship("Teacher", back_populates="schedules")
    group: Mapped["Group"] = relationship("Group", back_populates="schedules")

    attendances: Mapped[list["Attendance"]] = relationship(
        "Attendance", back_populates="schedules", cascade="all, delete-orphan"
    )
