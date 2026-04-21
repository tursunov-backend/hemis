from enum import Enum, IntEnum


class AnnouncementTarget(str, Enum):
    """E'lon manzili — announcement.target_group ustuni uchun"""

    ALL = "all"  # Barcha talabalar
    GROUP = "group"  # Muayyan guruh (CS-21-01 kabi)
    FACULTY = "faculty"  # Muayyan fakultet


class AttendanceStatus(str, Enum):
    """Davomat holati — attendance.status ustuni uchun"""

    PRESENT = "present"  # Keldi
    ABSENT = "absent"  # Kelmadi
    LATE = "late"  # Kech keldi
    EXCUSED = "excused"  # Sababli


class AuditAction(str, Enum):
    """
    Audit log harakati — audit_log.action ustuni uchun
    Kim, nima qilganini aniq yozib borish uchun
    """

    # Talaba profili
    PROFILE_VIEWED = "profile_viewed"  # Profil ko'rildi
    PROFILE_UPDATED = "profile_updated"  # Profil yangilandi

    # Baholar
    GRADE_VIEWED = "grade_viewed"  # Baho ko'rildi
    GRADE_UPDATED = "grade_updated"  # Baho o'zgartirildi (admin/teacher)

    # Davomat
    ATTENDANCE_VIEWED = "attendance_viewed"  # Davomat ko'rildi
    ATTENDANCE_MARKED = "attendance_marked"  # Davomat belgilandi (teacher)

    # Parol
    PASSWORD_CHANGED = "password_changed"  # Parol o'zgartirildi
    PASSWORD_RESET = "password_reset"  # Parol tiklandi (admin)

    # Kirish
    LOGIN_SUCCESS = "login_success"  # Muvaffaqiyatli kirdi
    LOGIN_FAILED = "login_failed"  # Kirish muvaffaqiyatsiz
    LOGOUT = "logout"  # Chiqdi

    # Xabar
    MESSAGE_SENT = "message_sent"  # Xabar yuborildi
    MESSAGE_READ = "message_read"  # Xabar o'qildi
    MESSAGE_DELETED = "message_deleted"  # Xabar o'chirildi

    # Moliya
    CONTRACT_VIEWED = "contract_viewed"  # Kontrakt ko'rildi
    SCHOLARSHIP_VIEWED = "scholarship_viewed"  # Stipendiya ko'rildi

    # Sertifikat
    CERTIFICATE_ADDED = "certificate_added"  # Sertifikat qo'shildi
    CERTIFICATE_DELETED = "certificate_deleted"  # Sertifikat o'chirildi


class DayOfWeek(IntEnum):
    """
    Hafta kuni — schedule.day_of_week ustuni uchun
    IntEnum ishlatiladi — raqam bilan taqqoslash oson bo'ladi
    """

    MONDAY = 1  # Dushanba
    TUESDAY = 2  # Seshanba
    WEDNESDAY = 3  # Chorshanba
    THURSDAY = 4  # Payshanba
    FRIDAY = 5  # Juma
    SATURDAY = 6  # Shanba
    SUNDAY = 7  # Yakshanba


class EducationForm(str, Enum):
    """Ta'lim shakli — group.education_form ustuni uchun"""

    KUNDUZGI = "kunduzgi"  # Kunduzgi
    KECHKI = "kechki"  # Kechki


class EducationLang(str, Enum):
    """Ta'lim tili — group.education_lang ustuni uchun"""

    UZBEK = "uzbek"  # O'zbek tilida
    RUS = "rus"  # Rus tilida


class ExamType(str, Enum):
    """Imtihon turi — exam.exam_type ustuni uchun"""

    MIDTERM = "midterm"  # Oraliq nazorat
    FINAL = "final"  # Yakuniy imtihon


class Gender(str, Enum):
    """Jins — student.gender ustuni uchun"""

    MALE = "male"  # Erkak
    FEMALE = "female"  # Ayol


class LessonType(str, Enum):
    """Dars turi — schedule.lesson_type ustuni uchun"""

    LECTURE = "lecture"  # Ma'ruza
    PRACTICE = "practice"  # Amaliy mashg'ulot
    LAB = "lab"  # Laboratoriya ishi
    SEMINAR = "seminar"  # Seminar


class LessonNumber(IntEnum):
    """Dars raqami — schedule.lesson_number ustuni uchun"""

    FIRST = 1  # 1-dars
    SECOND = 2  # 2-dars
    THIRD = 3  # 3-dars
    FOURTH = 4  # 4-dars
    FIFTH = 5  # 5-dars
    SIXTH = 6  # 6-dars


class LetterGrade(str, Enum):
    """
    Harf baho tizimi — grade.letter_grade ustuni uchun
    100 ballik tizim asosida
    """

    A = "A"  # 90-100 ball → GPA 4.0
    A_MINUS = "A-"  # 85-89  ball → GPA 3.7
    B_PLUS = "B+"  # 80-84  ball → GPA 3.3
    B = "B"  # 75-79  ball → GPA 3.0
    B_MINUS = "B-"  # 70-74  ball → GPA 2.7
    C_PLUS = "C+"  # 65-69  ball → GPA 2.3
    C = "C"  # 60-64  ball → GPA 2.0
    C_MINUS = "C-"  # 55-59  ball → GPA 1.7
    D = "D"  # 50-54  ball → GPA 1.0
    F = "F"  # 0-49   ball → GPA 0.0


class MessageStatus(str, Enum):
    """Xabar holati — message.status ustuni uchun"""

    SENT = "sent"  # Yuborildi, hali o'qilmadi
    READ = "read"  # O'qildi
    DELETED = "deleted"  # O'chirildi (soft delete)


class PaymentType(str, Enum):
    """To'lov turi — student.payment_type ustuni uchun"""

    GRANT = "grant"  # Davlat granti (bepul)
    CONTRACT = "contract"  # Kontrakt (pullik)


class Semester(str, Enum):
    """Semestr — student.semester ustuni uchun"""

    FIRST = "first"  # 1-semestr
    SECOND = "second"  # 2-semestr
    THIRD = "third"  # 3-semestr
    FOURTH = "fourth"  # 4-semestr
    FIFTH = "fifth"  # 5-semestr
    SIXTH = "sixth"  # 6-semestr
    SEVENTH = "seventh"  # 7-semestr
    EIGHTH = "eighth"  # 8-semestr


class StudentStatus(str, Enum):
    """Talaba holati — student.status ustuni uchun"""

    ACTIVE = "active"  # Faol o'qiyapti
    ACADEMIC = "academic"  # Akademik ta'tilda
    EXPELLED = "expelled"  # Haydangan


class UserRole(str, Enum):
    """Foydalanuvchi roli — rollar tizimi uchun"""

    STUDENT = "student"  # Talaba — faqat o'z ma'lumotlari
    TEACHER = "teacher"  # O'qituvchi — o'z fani va guruhi
    ADMIN = "admin"  # Dekanat — barcha talabalar
    SUPERADMIN = "superadmin"  # Tizim boshqaruvchisi — hamma narsa
