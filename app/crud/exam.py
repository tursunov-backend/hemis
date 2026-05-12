from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.exam import Exam, ExamResult
from app.models.enums import ExamType


# CREATE
def create_exam(
    db: Session,
    subject_id: int,
    semester: int,
    exam_type: ExamType,
    exam_date,
    room: str | None,
    duration_minutes: int,
) -> Exam:

    exam = Exam(
        subject_id=subject_id,
        semester=semester,
        exam_type=exam_type,
        exam_date=exam_date,
        room=room,
        duration_minutes=duration_minutes,
    )

    db.add(exam)
    db.commit()
    db.refresh(exam)

    return exam


# READ
def get_exam_by_id(db: Session, exam_id: int) -> Exam | None:
    return db.query(Exam).filter(Exam.id == exam_id).first()


def get_exams_by_subject(db: Session, subject_id: int):
    return db.query(Exam).filter(Exam.subject_id == subject_id).all()


def get_exams_by_semester(db: Session, semester: int):
    return db.query(Exam).filter(Exam.semester == semester).all()


def get_all_exams(db: Session, skip: int = 0, limit: int = 20):
    return db.query(Exam).offset(skip).limit(limit).all()


# UPDATE
def update_exam(
    db: Session, exam_id: int, exam_date=None, room=None, duration_minutes=None
) -> Exam:

    exam = db.query(Exam).filter(Exam.id == exam_id).first()

    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")

    if exam_date:
        exam.exam_date = exam_date
    if room is not None:
        exam.room = room
    if duration_minutes:
        exam.duration_minutes = duration_minutes

    db.commit()
    db.refresh(exam)

    return exam


# DELETE
def delete_exam(db: Session, exam_id: int):
    exam = db.query(Exam).filter(Exam.id == exam_id).first()

    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")

    db.delete(exam)
    db.commit()


# CREATE
def create_exam_result(
    db: Session, student_id: int, exam_id: int, score: int
) -> ExamResult:

    # duplicate check
    existing = (
        db.query(ExamResult)
        .filter(ExamResult.student_id == student_id, ExamResult.exam_id == exam_id)
        .first()
    )

    if existing:
        raise HTTPException(status_code=400, detail="Result already exists")

    # score validation
    if score < 0 or score > 100:
        raise HTTPException(status_code=400, detail="Score must be between 0 and 100")

    is_passed = score >= 60

    exam_result = ExamResult(
        student_id=student_id, exam_id=exam_id, score=score, is_passed=is_passed
    )

    db.add(exam_result)
    db.commit()
    db.refresh(exam_result)

    return exam_result


# READ
def get_results_by_exam(db: Session, exam_id: int):
    return db.query(ExamResult).filter(ExamResult.exam_id == exam_id).all()


def get_student_results(db: Session, student_id: int):
    return db.query(ExamResult).filter(ExamResult.student_id == student_id).all()


def get_result_by_id(db: Session, result_id: int) -> ExamResult | None:
    return db.query(ExamResult).filter(ExamResult.id == result_id).first()


# UPDATE
def update_exam_result(db: Session, result_id: int, score: int) -> ExamResult:

    exam_result = db.query(ExamResult).filter(ExamResult.id == result_id).first()

    if not exam_result:
        raise HTTPException(status_code=404, detail="Exam result not found")

    if score < 0 or score > 100:
        raise HTTPException(status_code=400, detail="Score must be between 0 and 100")

    exam_result.score = score
    exam_result.is_passed = score >= 60

    db.commit()
    db.refresh(exam_result)

    return exam_result


# DELETE
def delete_exam_result(db: Session, result_id: int):
    exam_result = db.query(ExamResult).filter(ExamResult.id == result_id).first()

    if not exam_result:
        raise HTTPException(status_code=404, detail="Exam result not found")

    db.delete(exam_result)
    db.commit()
