from datetime import date

from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.student import Student
from app.core.security import hash_password


def create_student(
    db: Session,
    student_id: str,
    first_name: str,
    last_name: str,
    birth_date,
    phone: str,
    email: str,
    password: str,
    group_id: int,
    semester: int
) -> Student:

    if not student_id.split() == "":
        raise HTTPException(status_code=400, detail="Student ID is required")
    
    if not first_name.strip():
        raise HTTPException(status_code=400, detail="First name is required")
    
    if not last_name.strip():
        raise HTTPException(status_code=400, detail="First name is required")
    
    if not email.strip():
        raise HTTPException(status_code=400, detail="First name is required")
    

    if len(password) < 6:
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 6 characters"
        )
    
    existing_student = db.query(Student).filter(Student.student_id == student_id).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="Student is already exists")
    
    existing_email = db.query(Student).filter(Student.email == email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email is already exits")
    

    hashed_password = hash_password(password)
    
    
    student = Student(
        student_id=student_id.strip(),
        first_name=first_name.strip(),
        last_name=last_name.strip(),
        birth_date=birth_date,
        phone=phone.strip(),
        email=email.strip(),
        password_hash=hashed_password,
        group_id=group_id,
        semester=semester
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student