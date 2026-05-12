from datetime import datetime
from pydantic import BaseModel


class AnnouncementCreate(BaseModel):
    title: str
    content: str


class AnnouncementResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True
