from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.crud.announcement import (
    create_announcement,
    get_all_announcements,
    get_announcement_by_id,
    delete_announcement,
)
from app.schemas.announcement import (
    AnnouncementCreate,
    AnnouncementResponse,
)

router = APIRouter(prefix="/announcements", tags=["E'lonlar"])


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AnnouncementResponse)
def create_new_announcement(
    announcement_data: AnnouncementCreate, db: Session = Depends(get_db)
):
    return create_announcement(
        db=db, title=announcement_data.title, content=announcement_data.content
    )


@router.get("/", response_model=list[AnnouncementResponse])
def read_announcements(db: Session = Depends(get_db)):
    return get_all_announcements(db)


@router.get("/{announcement_id}", response_model=AnnouncementResponse)
def read_announcement(announcement_id: int, db: Session = Depends(get_db)):
    return get_announcement_by_id(db, announcement_id)


@router.delete("/{announcement_id}")
def remove_announcement(announcement_id: int, db: Session = Depends(get_db)):
    delete_announcement(db, announcement_id)

    return {"message": "Announcement deleted successfully"}
