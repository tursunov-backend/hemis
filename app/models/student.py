from datetime import datetime, date, timezone
from sqlalchemy import Date, DateTime, ForeignKey, Integer, String, Float, Boolean, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.models.enums import StudentStatus, PaymentType, Semester


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student_id: Mapped[str] = mapped_column(String(20), unique=True)  # login: 20210001
    password_hash: Mapped[str] = mapped_column(String(255))
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    middle_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    birth_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    gender: Mapped[str | None] = mapped_column(String(10), nullable=True)
    passport_number: Mapped[str | None] = mapped_column(String(20), nullable=True)
    address: Mapped[str | None] = mapped_column(String, nullable=True)
    phone: Mapped[str | None] = mapped_column(String(20), nullable=True)
    email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    photo_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id", ondelete="CASCADE"))
    semester: Mapped[Semester] = mapped_column(Enum(Semester))
    status: Mapped[StudentStatus] = mapped_column(Enum(StudentStatus))
    payment_type: Mapped[PaymentType] = mapped_column(Enum(PaymentType))
    admission_year: Mapped[int] = mapped_column(Integer)
    gpa: Mapped[float | None] = mapped_column(Float, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    last_login: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)

    group = relationship(
        "Group",
        back_populates="students"
    )
    attendances: Mapped[list["Attendance"]] = relationship(
        "Attendance", back_populates="student", cascade="all, delete-orphan"
    )
    grades = relationship(
        "Grade",
        back_populates="student",
        cascade="all, delete-orphan"
    )

    exam_results = relationship(
        "ExamResult",
        back_populates="student",
        cascade="all, delete-orphan"
    )
    contracts: Mapped[list["Contract"]] = relationship(
        "Contract", back_populates="student", cascade="all, delete-orphan"
    )
    scholarships: Mapped[list["Scholarship"]] = relationship(
        "Scholarship", back_populates="student", cascade="all, delete-orphan"
    )
    certificates: Mapped[list["Certificate"]] = relationship(
        "Certificate", back_populates="student", cascade="all, delete-orphan"
    )
    audit_logs: Mapped[list["AuditLog"]] = relationship(
        "AuditLog", back_populates="student", cascade="all, delete-orphan"
    )
    login_history: Mapped[list["LoginHistory"]] = relationship(
        "LoginHistory", back_populates="student", cascade="all, delete-orphan"
    )
    messages: Mapped[list["Message"]] = relationship(
        "Message", foreign_keys="Message.sender_id", back_populates="sender"
    )
    messages: Mapped[list["Message"]] = relationship(
        "Message", foreign_keys="Message.receiver_id", back_populates="receiver"
    )
