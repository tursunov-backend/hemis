from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.message import Message


def create_message(
    db: Session, sender_id: int, receiver_id: int, subject: str, body: str
) -> Message:

    if sender_id == receiver_id:
        raise HTTPException(status_code=400, detail="Cannot send message to yourself")

    if not subject.strip():
        raise HTTPException(status_code=400, detail="Subject cannot be empty")

    if not body.strip():
        raise HTTPException(status_code=400, detail="Message body cannot be empty")

    message = Message(
        sender_id=sender_id, receiver_id=receiver_id, subject=subject, body=body
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    return message
