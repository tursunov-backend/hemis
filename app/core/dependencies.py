from typing import Generator, Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db.base import SessionLocal
from app.core.security import verify_token
from app.models.student import Student
from app.models.enums import UserRole


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


# DB
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CURRENT USER
def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[Session, Depends(get_db)],
) -> Student:

    payload = verify_token(token)

    student_id = payload.get("sub")
    if student_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
        )

    user = db.query(Student).filter(Student.id == int(student_id)).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return user


# ROLE CHECK
def require_role(required_role: UserRole):
    def role_checker(user: Annotated[Student, Depends(get_current_user)]) -> Student:
        if user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied",
            )
        return user

    return role_checker


# Shortcutlar
get_admin = require_role(UserRole.ADMIN)
get_teacher = require_role(UserRole.TEACHER)
get_student = require_role(UserRole.STUDENT)
