from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, Boolean, DateTime, func, text

from app.db.base import Base
from app.models.enums import AnnouncementTarget


class Announcement(Base):
    __tablename__ = "announcements"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(Text)

    target_group: Mapped[str] = mapped_column(
        String(50),
        server_default=AnnouncementTarget.ALL,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        server_default=text("true"),
    )

    expires_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )