from sqlalchemy.orm import Session
from app.models.attendance import Attendance
from app.models.enums import AttendanceStatus


# CREATE (teacher ishlatadi)
def create_attendance(
    db: Session, student_id: int, schedule_id: int, date, status: AttendanceStatus
) -> Attendance:

    attendance = Attendance(
        student_id=student_id, schedule_id=schedule_id, date=date, status=status
    )

    db.add(attendance)
    db.commit()
    db.refresh(attendance)

    return attendance


#  READ (student o‘zini ko‘radi)
def get_student_attendance(
    db: Session, student_id: int, skip: int = 0, limit: int = 20
):
    return (
        db.query(Attendance)
        .filter(Attendance.student_id == student_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


#  SUMMARY (foiz hisoblash)
def get_attendance_summary(db: Session, student_id: int):
    records = db.query(Attendance).filter(Attendance.student_id == student_id).all()

    total = len(records)
    present = len([r for r in records if r.status == AttendanceStatus.PRESENT])

    percent = (present / total * 100) if total > 0 else 0

    return {"total": total, "present": present, "percentage": round(percent, 2)}


#  UPDATE (teacher o‘zgartiradi)
def update_attendance(db: Session, attendance_id: int, status: AttendanceStatus):
    attendance = db.query(Attendance).get(attendance_id)

    if not attendance:
        return None

    attendance.status = status

    db.commit()
    db.refresh(attendance)

    return attendance
