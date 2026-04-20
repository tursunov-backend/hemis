from enum import Enum


# announcement.py
# target_group uchun (ixtiyoriy, hozircha String ishlatsa ham bo'ladi)
class TargetGroup(str, Enum):
    ALL = "all"


# attendance.py
class AttendanceStatus(str, Enum):
    PRESENT = "present"  # keldi
    ABSENT = "absent"  # kelmadi
    LATE = "late"  # kech keldi
    EXCUSED = "excused"  # sababli


# exam.py
class ExamType(str, Enum):
    MIDTERM = "midterm"  # oraliq
    FINAL = "final"  # yakuniy


# grade.py
class GradePoint(int, Enum):
    EXCELLENT = 5  # a'lo       (90-100)
    GOOD = 4  # yaxshi     (70-89)
    SATISFACTORY = 3  # qoniqarli  (60-69)
    FAILED = 2  # qoniqarsiz (0-59)


# group.py
class EducationForm(str, Enum):
    KUNDUZGI = "kunduzgi"
    SIRTQI = "sirtqi"
    MASOFAVIY = "masofaviy"


class EducationLang(str, Enum):
    UZBEK = "uzbek"
    RUS = "rus"
    INGLIZ = "ingliz"


# message.py
class MessageStatus(str, Enum):
    SENT = "sent"  # yuborildi
    READ = "read"  # o'qildi


# schedule.py
class LessonType(str, Enum):
    LECTURE = "lecture"  # ma'ruza
    PRACTICE = "practice"  # amaliy
    LAB = "lab"  # laboratoriya


class DayOfWeek(int, Enum):
    MONDAY = 1  # Dushanba
    TUESDAY = 2  # Seshanba
    WEDNESDAY = 3  # Chorshanba
    THURSDAY = 4  # Payshanba
    FRIDAY = 5  # Juma
    SATURDAY = 6  # Shanba


class LessonNumber(int, Enum):
    FIRST = 1  # 1-dars
    SECOND = 2  # 2-dars
    THIRD = 3  # 3-dars
    FOURTH = 4  # 4-dars
    FIFTH = 5  # 5-dars
    SIXTH = 6  # 6-dars


# student.py
class StudentStatus(str, Enum):
    ACTIVE = "active"  # o'qiyapti
    ACADEMIC = "academic"  # akademik ta'tilda
    EXPELLED = "expelled"  # chiqarib yuborilgan


class PaymentType(str, Enum):
    GRANT = "grant"
    CONTRACT = "contract"


class Semester(int, Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7
    EIGHTH = 8
