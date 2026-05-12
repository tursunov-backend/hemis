from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import date

from app.models.financial import Contract, Scholarship


# CREATE CONTRACT
def create_contract(
    db: Session,
    student_id: int,
    contract_number: str,
    academic_year: str,
    amount: float,
    due_date: date,
) -> Contract:

    # unique contract number
    existing = (
        db.query(Contract).filter(Contract.contract_number == contract_number).first()
    )

    if existing:
        raise HTTPException(status_code=400, detail="Contract already exists")

    contract = Contract(
        student_id=student_id,
        contract_number=contract_number,
        academic_year=academic_year,
        amount=amount,
        paid_amount=0,
        due_date=due_date,
        is_paid=False,
    )

    db.add(contract)
    db.commit()
    db.refresh(contract)

    return contract


# READ
def get_contract_by_id(db: Session, contract_id: int) -> Contract | None:
    return db.query(Contract).filter(Contract.id == contract_id).first()


def get_student_contracts(db: Session, student_id: int):
    return db.query(Contract).filter(Contract.student_id == student_id).all()


def get_all_contracts(db: Session, skip: int = 0, limit: int = 20):
    return db.query(Contract).offset(skip).limit(limit).all()


# PAYMENT
def pay_contract(db: Session, contract_id: int, amount: float) -> Contract:

    contract = db.query(Contract).filter(Contract.id == contract_id).first()

    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")

    if amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid payment amount")

    # ortiqcha to‘lovni tekshirish
    if contract.paid_amount + amount > contract.amount:
        raise HTTPException(status_code=400, detail="Payment exceeds contract amount")

    contract.paid_amount += amount

    # avtomatik yopiladi
    if contract.paid_amount >= contract.amount:
        contract.is_paid = True

    db.commit()
    db.refresh(contract)

    return contract


# CREATE SCHOLARSHIP
def create_scholarship(
    db: Session, student_id: int, month: date, amount: float
) -> Scholarship:

    # 1 oyda 1 ta stipendiya
    existing = (
        db.query(Scholarship)
        .filter(Scholarship.student_id == student_id, Scholarship.month == month)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400, detail="Scholarship already exists for this month"
        )

    scholarship = Scholarship(
        student_id=student_id, month=month, amount=amount, is_paid=False
    )

    db.add(scholarship)
    db.commit()
    db.refresh(scholarship)

    return scholarship


# READ
def get_student_scholarships(db: Session, student_id: int):
    return db.query(Scholarship).filter(Scholarship.student_id == student_id).all()


# PAY SCHOLARSHIP
def pay_scholarship(db: Session, scholarship_id: int) -> Scholarship:

    scholarship = db.query(Scholarship).filter(Scholarship.id == scholarship_id).first()

    if not scholarship:
        raise HTTPException(status_code=404, detail="Scholarship not found")

    scholarship.is_paid = True
    scholarship.paid_date = date.today()

    db.commit()
    db.refresh(scholarship)

    return scholarship


# DELETE
def delete_contract(db: Session, contract_id: int):
    contract = db.query(Contract).filter(Contract.id == contract_id).first()

    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")

    db.delete(contract)
    db.commit()


def delete_scholarship(db: Session, scholarship_id: int):
    scholarship = db.query(Scholarship).filter(Scholarship.id == scholarship_id).first()

    if not scholarship:
        raise HTTPException(status_code=404, detail="Scholarship not found")

    db.delete(scholarship)
    db.commit()
