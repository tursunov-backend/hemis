from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.student import Student
from app.core.security import hash_password, verify_password, create_access_token


# REGISTER
def register_user(
    db: Session,
    student_id: str,
    password: str,
    first_name: str,
    last_name: str,
) -> Student:

    #  oldin bor-yo‘qligini tekshiramiz
    existing_user = db.query(Student).filter(Student.student_id == student_id).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    user = Student(
        student_id=student_id,
        password_hash=hash_password(password),
        first_name=first_name,
        last_name=last_name,
        admission_year=2024,
        group_id=1,
        semester=1,
        status="active",
        payment_type="contract",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# LOGIN
def login_user(
    db: Session,
    student_id: str,
    password: str,
) -> dict:

    user = db.query(Student).filter(Student.student_id == student_id).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user.id)})

    return {
        "access_token": token,
        "token_type": "bearer",
        "full_name": f"{user.first_name} {user.last_name}",
    }


# CHANGE PASSWORD
def change_password(db: Session, user: Student, old_password: str, new_password: str):

    if not verify_password(old_password, user.password_hash):
        raise HTTPException(status_code=400, detail="Wrong password")

    user.password_hash = hash_password(new_password)

    db.commit()

    return {"message": "Password updated"}
