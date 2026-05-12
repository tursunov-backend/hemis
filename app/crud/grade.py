from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.grade import Grade


def create_grade(
    db: Session,
    student_id: int,
    subject_id: int,
    semester: int,
    midterm1: int,
    midterm2: int,
    final_score: int
) -> Grade:

    # ❗ Duplicate check
    existing = db.query(Grade).filter(
        Grade.student_id == student_id,
        Grade.subject_id == subject_id,
        Grade.semester == semester
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Grade already exists")

    # ❗ Validation
    if not (0 <= midterm1 <= 30):
        raise HTTPException(status_code=400, detail="midterm1 must be 0-30")

    if not (0 <= midterm2 <= 20):
        raise HTTPException(status_code=400, detail="midterm2 must be 0-20")

    if not (0 <= final_score <= 50):
        raise HTTPException(status_code=400, detail="final_score must be 0-50")

    #Total hisoblash
    total = midterm1 + midterm2 + final_score

    # Grade point hisoblash (oddiy variant)
    if total >= 90:
        grade_point = 4.0
    elif total >= 85:
        grade_point = 3.7
    elif total >= 80:
        grade_point = 3.3
    elif total >= 75:
        grade_point = 3.0
    elif total >= 70:
        grade_point = 2.7
    elif total >= 65:
        grade_point = 2.3
    elif total >= 60:
        grade_point = 2.0
    else:
        grade_point = 0.0

    # Create
    grade = Grade(
        student_id=student_id,
        subject_id=subject_id,
        semester=semester,
        midterm1=midterm1,
        midterm2=midterm2,
        final_score=final_score,
        total=total,
        grade_point=grade_point
    )

    db.add(grade)
    db.commit()
    db.refresh(grade)

    return grade