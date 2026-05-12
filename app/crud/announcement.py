from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.announcement import Announcement


def create_announcement(
    db: Session,
    title: str,
    content: str
) -> Announcement:

    if not title.strip():
        raise HTTPException(status_code=400, detail="Title is required")

    if not content.strip():
        raise HTTPException(status_code=400, detail="Content is required")

    announcement = Announcement(
        title=title.strip(),
        content=content.strip()
    )

    db.add(announcement)
    db.commit()
    db.refresh(announcement)

    return announcement


def get_all_announcements(db: Session):
    return db.query(Announcement).all()

def get_announcement_by_id(
    db: Session,
    announcement_id: int
) -> Announcement:

    announcement = db.query(Announcement).filter(
        Announcement.id == announcement_id
    ).first()

    if not announcement:
        raise HTTPException(
            status_code=404,
            detail="Announcement not found"
        )

    return announcement


def delete_announcement(
    db: Session,
    announcement_id: int
):

    announcement = db.query(Announcement).filter(
        Announcement.id == announcement_id
    ).first()

    if not announcement:
        raise HTTPException(
            status_code=404,
            detail="Announcement not found"
        )

    db.delete(announcement)
    db.commit()