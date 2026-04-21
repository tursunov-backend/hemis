from datetime import datetime

from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import DateTime, ForeignKey, func, Enum, JSON

from app.db.base import Base
from app.models.enums import AuditAction


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(primary_key=True)

    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="CASCADE")
    )

    action: Mapped[AuditAction] = mapped_column(
        Enum(AuditAction, name="audit_action")
    )

    old_value: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    new_value: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    student: Mapped["Student"] = relationship(
        "Student", back_populates="audit_logs"
    )