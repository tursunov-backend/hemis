from datetime import datetime, timezone

from sqlalchemy import String, Text, ForeignKey, DateTime, Enum, INTEGER
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import MessageStatus


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    sender_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="CASCADE")
    )
    receiver_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="CASCADE")
    )
    subject: Mapped[str] = mapped_column(String(255))
    body: Mapped[str] = mapped_column(Text)
    status: Mapped[MessageStatus] = mapped_column(
        Enum(MessageStatus), default=MessageStatus.sent
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    sender: Mapped["Student"] = relationship(
        "Student", foreign_keys=[sender_id], back_populates="messages"
    )

    receiver: Mapped["Student"] = relationship(
        "Student", foreign_keys=[receiver_id], back_populates="messages"
    )
