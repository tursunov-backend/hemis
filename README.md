# 🎓 HEMIS Backend API

O'zbekiston universitetlarining **HEMIS Student tizimi** uchun backend API.  
Talabalar o'z profili, baholar, davomat, jadval va moliyaviy ma'lumotlarini ko'ra oladi.

> 💡 **Backend nima?** — Foydalanuvchi ko'rmaydigan "orqa" qism. Telefon yoki veb-sayt shu backend bilan gaplashib ma'lumot oladi.

---

## 🛠️ Texnologiyalar

| Texnologiya | Bu nima? |
|---|---|
| **Python 3.11+** | Dasturlash tili |
| **FastAPI** | API yaratish uchun framework |
| **PostgreSQL** | Ma'lumotlar bazasi |
| **SQLAlchemy 2.0** | Python orqali bazaga murojaat (SQL yozmasdan) |
| **Alembic** | Baza o'zgarishlarini boshqarish |
| **Pydantic v2** | Kelgan ma'lumotlarni tekshirish |
| **python-jose** | JWT token yaratish va tekshirish |
| **bcrypt (passlib)** | Parolni xavfsiz saqlash |
| **Uvicorn** | Serverni ishga tushirish |

---

## 📁 Loyiha strukturasi

> 💡 Har bir papka va fayl nima uchun ekanini tushuntirdik.

```
hemis_backend/
│
├── main.py                      ← Ilova shu yerdan boshlanadi
├── requirements.txt             ← Barcha kutubxonalar ro'yxati
├── .env                         ← Maxfiy sozlamalar — GitHubga chiqarma! ⚠️
├── .env.example                 ← .env uchun namuna (GitHubga qo'ysa bo'ladi)
├── alembic.ini                  ← Alembic sozlamasi
├── README.md                    ← Siz o'qiyotgan fayl 😄
│
├── alembic/                     ← Baza o'zgarishlari tarixi
│   └── versions/                ← Har bir o'zgarish alohida fayl
│
└── app/
    ├── __init__.py
    │
    ├── core/                    ← Eng asosiy sozlamalar
    │   ├── config.py            ← .env dan sozlamalarni o'qiydi
    │   ├── security.py          ← JWT token va bcrypt
    │   └── dependencies.py      ← "Hozir kim login qilgan?" shu yerda
    │
    ├── db/                      ← Database bilan bog'liq hamma narsa
    │   ├── base.py              ← Barcha modellar meros oladigan class
    │   ├── session.py           ← Bazaga ulanish, get_db() funksiyasi
    │   └── init_db.py           ← Boshlang'ich test ma'lumotlar
    │
    ├── models/                  ← Baza jadvallari (har bir fayl = bitta jadval)
    │   │
    │   │  💡 Barcha modellarda avtomatik mavjud:
    │   │       created_at — qachon yaratilgan
    │   │       updated_at — qachon o'zgartirilgan
    │   │       is_deleted — o'chirilganmi? (haqiqatda o'chmaydi)
    │   │
    │   ├── __init__.py          ← Barcha modellarni bir yerda import qiladi
    │   ├── faculty.py           ← Fakultet jadvali
    │   ├── department.py        ← Kafedra jadvali
    │   ├── group.py             ← Guruh jadvali
    │   ├── teacher.py           ← O'qituvchi jadvali
    │   ├── student.py           ← Talaba jadvali ⭐ (login ham shu yerda)
    │   ├── subject.py           ← Fan jadvali
    │   ├── schedule.py          ← Dars jadvali
    │   ├── attendance.py        ← Davomat jadvali
    │   ├── grade.py             ← Baho jadvali
    │   ├── exam.py              ← Imtihon jadvali
    │   ├── financial.py         ← Kontrakt va stipendiya jadvallari
    │   ├── message.py           ← Xabar jadvali
    │   ├── announcement.py      ← E'lon jadvali
    │   ├── audit_log.py         ← Kim nima o'zgartirdi?
    │   ├── login_history.py     ← Kirish tarixi jadvali
    │   └── certificate.py       ← Sertifikat jadvali
    │
    ├── schemas/                 ← API ma'lumot formatlari (Pydantic v2)
    │   │
    │   │  ⚠️ model ≠ schema farqi:
    │   │     model  = bazadagi jadval ko'rinishi
    │   │     schema = API orqali keladigan/ketadigan ma'lumot
    │   │
    │   ├── __init__.py
    │   ├── common.py            ← Umumiy formatlar (pagination, xato)
    │   ├── auth.py              ← Login so'rovi va javob formati
    │   ├── student.py           ← Profil ko'rish va yangilash formati
    │   ├── curriculum.py        ← Jadval va fanlar formati
    │   ├── attendance.py        ← Davomat formati
    │   ├── grade.py             ← Baho va GPA formati
    │   ├── exam.py              ← Imtihon va natija formati
    │   ├── financial.py         ← Kontrakt va stipendiya formati
    │   ├── message.py           ← Xabar formati
    │   └── announcement.py      ← E'lon formati
    │
    ├── crud/                    ← Baza bilan ishlash logikasi
    │   │
    │   │  💡 Nima uchun alohida?
    │   │     Router → HTTP so'rovlarni qabul qiladi
    │   │     CRUD   → faqat baza bilan ishlaydi
    │   │     Shunday bo'lsa kod toza va tushunarli bo'ladi
    │   │
    │   ├── __init__.py
    │   ├── auth.py              ← Login, logout, parol o'zgartirish
    │   ├── student.py           ← Profil olish, yangilash
    │   ├── attendance.py        ← Davomat ma'lumotlari
    │   ├── grade.py             ← Baholar va GPA hisoblash
    │   ├── exam.py              ← Imtihon va natijalar
    │   ├── financial.py         ← Kontrakt va stipendiya
    │   └── message.py           ← Xabar yuborish va olish
    │
    ├── api/                     ← HTTP endpointlar
    │   └── v1/                  ← Versiya 1
    │       │
    │       │  💡 Nima uchun v1?
    │       │     Kelajakda tizim o'zgarse /v2 qo'shiladi
    │       │     Eski /v1 ishlab turadi — hech narsa buzilamaydi
    │       │
    │       ├── router.py        ← Barcha routerlarni birlashtiradi
    │       └── routes/
    │           ├── auth.py          ← /api/v1/auth/...
    │           ├── student.py       ← /api/v1/student/...
    │           ├── curriculum.py    ← /api/v1/curriculum/...
    │           ├── attendance.py    ← /api/v1/attendance/...
    │           ├── grades.py        ← /api/v1/grades/...
    │           ├── exams.py         ← /api/v1/exams/...
    │           ├── financial.py     ← /api/v1/financial/...
    │           ├── messages.py      ← /api/v1/messages/...
    │           └── announcements.py ← /api/v1/announcements/...
    │
    └── utils/                   ← Yordamchi funksiyalar
        ├── enums.py             ← Barcha ro'yxatlar (status, tur...)
        ├── pagination.py        ← Sahifalash (20 tadan bo'lib yuborish)
        ├── grade_utils.py       ← 87 ball → "A-", 3.7 GPA hisoblash
        └── validators.py        ← Parol kuchi, telefon, email tekshiruvi
```

---

## 💻 O'rnatish (qadam-baqadam)

### 1-qadam: Yuklab oling

```bash
git clone https://github.com/username/hemis-backend.git
cd hemis-backend
```

### 2-qadam: Virtual muhit yarating

> 💡 **Virtual muhit nima?** — Har bir loyiha uchun alohida "xona". Kutubxonalar bir-biriga aralashmaydi.

```bash
python -m venv venv

# Linux / Mac:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# Muvaffaqiyatli bo'lsa terminalda (venv) chiqadi
```

### 3-qadam: Kutubxonalarni o'rnating

```bash
pip install -r requirements.txt
```

### 4-qadam: PostgreSQL bazasini yarating

> 💡 PostgreSQL o'rnatilmagan bo'lsa: https://www.postgresql.org/download/

```bash
psql -U postgres

CREATE DATABASE hemis_db;
CREATE USER hemis_user WITH PASSWORD 'parol123';
GRANT ALL PRIVILEGES ON DATABASE hemis_db TO hemis_user;
\q
```

### 5-qadam: .env faylini sozlang

```bash
cp .env.example .env
```

`.env` ichida:

```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=hemis_user
DB_PASS=parol123
DB_NAME=hemis_db

SECRET_KEY=bu-yerga-kamida-32-belgi-yozing
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
```

> 🔑 Xavfsiz kalit yasash:
> ```bash
> # Linux / Mac
> openssl rand -hex 32
>
> # Windows
> python -c "import secrets; print(secrets.token_hex(32))"
> ```
> Chiqgan natijani `SECRET_KEY=` ga qo'ying.

---

## ▶️ Ishga tushirish

```bash
# 1. Jadvallarni bazada yaratish (faqat birinchi marta)
alembic upgrade head

# 2. Serverni ishga tushirish
uvicorn main:app --reload

# Server ishlaydi:
# http://localhost:8000
# Swagger UI: http://localhost:8000/docs
```

> 💡 **Swagger UI** — barcha endpointlarni brauzerda ko'rib, sinab ko'rish mumkin. Postman kerak emas!

---

## 🗄️ Schema Overview

> 💡 Barcha jadvallar, ustunlar va ma'lumot turlari.
> - `PK` = asosiy kalit (har bir yozuvning o'ziga xos raqami)
> - `FK` = boshqa jadvalga havola
> - `nullable` = bo'sh qolishi mumkin
> - `UNIQUE` = ikki xil yozuv bir xil bo'lmasligi kerak

```
faculty
  id          INTEGER    PK
  name        VARCHAR(100)
  code        VARCHAR(20)   UNIQUE
  created_at  TIMESTAMP

department
  id          INTEGER    PK
  name        VARCHAR(100)
  code        VARCHAR(20)   UNIQUE
  faculty_id  INTEGER    FK → faculty.id
  created_at  TIMESTAMP

group
  id              INTEGER    PK
  name            VARCHAR(50)
  department_id   INTEGER    FK → department.id
  course          INTEGER                       (1, 2, 3, 4)
  education_form  VARCHAR(20)                   (kunduzgi, sirtqi)
  education_lang  VARCHAR(20)                   (uzbek, rus)
  created_at      TIMESTAMP

teacher
  id              INTEGER    PK
  first_name      VARCHAR(100)
  last_name       VARCHAR(100)
  middle_name     VARCHAR(100)   (nullable)
  email           VARCHAR(255)   UNIQUE (nullable)
  phone           VARCHAR(20)    (nullable)
  department_id   INTEGER    FK → department.id
  created_at      TIMESTAMP

student  ⭐
  id              INTEGER    PK
  student_id      VARCHAR(20)    UNIQUE         (login: 20210001)
  password_hash   VARCHAR(255)
  first_name      VARCHAR(100)
  last_name       VARCHAR(100)
  middle_name     VARCHAR(100)   (nullable)
  birth_date      DATE           (nullable)
  gender          VARCHAR(10)    (nullable)
  passport_number VARCHAR(20)    (nullable)
  address         TEXT           (nullable)
  phone           VARCHAR(20)    (nullable)
  email           VARCHAR(255)   (nullable)
  photo_url       VARCHAR(500)   (nullable)
  group_id        INTEGER    FK → group.id
  semester        INTEGER                       (1-8)
  status          VARCHAR(20)                   (active, academic, expelled)
  payment_type    VARCHAR(20)                   (grant, contract)
  admission_year  INTEGER
  gpa             FLOAT          (nullable)
  is_active       BOOLEAN        default=True
  last_login      TIMESTAMP      (nullable)
  created_at      TIMESTAMP
  updated_at      TIMESTAMP
  is_deleted      BOOLEAN        default=False

subject
  id            INTEGER    PK
  name          VARCHAR(200)
  code          VARCHAR(20)    UNIQUE
  credits       INTEGER
  semester      INTEGER
  department_id INTEGER    FK → department.id
  created_at    TIMESTAMP

schedule
  id             INTEGER    PK
  subject_id     INTEGER    FK → subject.id
  teacher_id     INTEGER    FK → teacher.id
  group_id       INTEGER    FK → group.id
  semester       INTEGER
  day_of_week    INTEGER                        (1=Dushanba ... 7=Yakshanba)
  lesson_number  INTEGER                        (1-6)
  start_time     TIME
  end_time       TIME
  room           VARCHAR(50)    (nullable)
  lesson_type    VARCHAR(20)                    (lecture, practice, lab)
  created_at     TIMESTAMP

attendance
  id           INTEGER    PK
  student_id   INTEGER    FK → student.id
  schedule_id  INTEGER    FK → schedule.id
  date         DATE
  status       VARCHAR(20)                      (present, absent, late, excused)
  created_at   TIMESTAMP

grade
  id           INTEGER    PK
  student_id   INTEGER    FK → student.id
  subject_id   INTEGER    FK → subject.id
  semester     INTEGER
  midterm1     INTEGER                          (0-30)
  midterm2     INTEGER                          (0-30)
  final_score  INTEGER                          (0-40)
  total        INTEGER                          (0-100)
  letter_grade VARCHAR(5)     (nullable)        (A, A-, B+, ...)
  gpa_point    FLOAT          (nullable)        (0.0 - 4.0)
  created_at   TIMESTAMP
  updated_at   TIMESTAMP

exam
  id               INTEGER    PK
  subject_id       INTEGER    FK → subject.id
  semester         INTEGER
  exam_type        VARCHAR(20)                  (midterm, final)
  exam_date        DATETIME
  room             VARCHAR(50)    (nullable)
  duration_minutes INTEGER
  created_at       TIMESTAMP

exam_result
  id         INTEGER    PK
  exam_id    INTEGER    FK → exam.id
  student_id INTEGER    FK → student.id
  score      INTEGER
  is_passed  BOOLEAN
  created_at TIMESTAMP

contract                       (financial.py ichida)
  id              INTEGER    PK
  student_id      INTEGER    FK → student.id
  contract_number VARCHAR(50)    UNIQUE
  academic_year   VARCHAR(20)                   (2024-2025)
  amount          DECIMAL(12,2)
  paid_amount     DECIMAL(12,2)  default=0
  due_date        DATE
  is_paid         BOOLEAN        default=False
  created_at      TIMESTAMP

scholarship                    (financial.py ichida)
  id         INTEGER    PK
  student_id INTEGER    FK → student.id
  month      DATE
  amount     DECIMAL(10,2)
  is_paid    BOOLEAN        default=False
  paid_date  DATE           (nullable)
  created_at TIMESTAMP

message
  id          INTEGER    PK
  sender_id   INTEGER    FK → student.id   (xabar yuborguvchi)
  receiver_id INTEGER    FK → student.id   (xabar qabul qiluvchi)
  subject     VARCHAR(255)
  body        TEXT
  status      VARCHAR(20)                       (sent, read)
  created_at  TIMESTAMP

announcement
  id           INTEGER    PK
  title        VARCHAR(255)
  content      TEXT
  target_group VARCHAR(50)    (nullable)         (all, cs-21, ...)
  is_active    BOOLEAN        default=True
  expires_at   TIMESTAMP      (nullable)
  created_at   TIMESTAMP

login_history
  id         INTEGER    PK
  student_id INTEGER    FK → student.id
  ip_address VARCHAR(50)    (nullable)
  user_agent TEXT           (nullable)
  login_at   TIMESTAMP
  is_success BOOLEAN

certificate
  id          INTEGER    PK
  student_id  INTEGER    FK → student.id
  name        VARCHAR(255)
  issued_by   VARCHAR(255)
  issued_date DATE
  file_url    VARCHAR(500)   (nullable)
  created_at  TIMESTAMP

audit_log
  id         INTEGER    PK
  user_id    INTEGER    FK → student.id
  action     VARCHAR(100)                       (profile_updated, grade_viewed, ...)
  old_value  TEXT           (nullable)          (JSON ko'rinishida)
  new_value  TEXT           (nullable)          (JSON ko'rinishida)
  created_at TIMESTAMP
```

---

## 📝 Har bir model fayli ichida nima bo'ladi?

> 💡 Har bir `.py` faylni ochmadan turib nima yozishni bilish uchun.

### `faculty.py`
```python
- Faculty klassi (SQLAlchemy Model)
- Ustunlar: id, name, code, created_at
- Relationship: departments → (bu fakultetning kafedralari)
```

### `department.py`
```python
- Department klassi
- Ustunlar: id, name, code, faculty_id, created_at
- Relationship: faculty → (qaysi fakultetga tegishli)
                groups   → (bu kafedraning guruhlari)
                teachers → (bu kafedraning o'qituvchilari)
                subjects → (bu kafedraning fanlari)
```

### `group.py`
```python
- Group klassi
- Ustunlar: id, name, department_id, course,
            education_form, education_lang, created_at
- Relationship: department → (qaysi kafedra)
                students   → (bu guruhning talabalari)
                schedules  → (bu guruhning dars jadvali)
```

### `teacher.py`
```python
- Teacher klassi
- Ustunlar: id, first_name, last_name, middle_name,
            email, phone, department_id, created_at
- Relationship: department → (qaysi kafedra)
                schedules  → (bu o'qituvchining dars jadvali)
```

### `student.py` ⭐
```python
- Student klassi (eng asosiy model — login ham shu yerda)
- Ustunlar: id, student_id, password_hash,
            first_name, last_name, middle_name,
            birth_date, gender, passport_number,
            address, phone, email, photo_url,
            group_id, semester, status, payment_type,
            admission_year, gpa, is_active,
            last_login, created_at, updated_at, is_deleted
- Relationship: group         → (qaysi guruh)
                attendances   → (davomatlari)
                grades        → (baholari)
                exam_results  → (imtihon natijalari)
                contracts     → (kontraktlari)
                scholarships  → (stipendiyalari)
                certificates  → (sertifikatlari)
                login_history → (kirish tarixi)
                sent_messages     → (yuborgan xabarlari)
                received_messages → (olgan xabarlari)
```

### `subject.py`
```python
- Subject klassi
- Ustunlar: id, name, code, credits, semester,
            department_id, created_at
- Relationship: department → (qaysi kafedra)
                schedules  → (bu fanning dars jadvali)
                grades     → (bu fanning baholari)
                exams      → (bu fanning imtihonlari)
```

### `schedule.py`
```python
- Schedule klassi
- Ustunlar: id, subject_id, teacher_id, group_id,
            semester, day_of_week, lesson_number,
            start_time, end_time, room, lesson_type,
            created_at
- Relationship: subject     → (qaysi fan)
                teacher     → (qaysi o'qituvchi)
                group       → (qaysi guruh)
                attendances → (bu darsning davomatlari)
```

### `attendance.py`
```python
- Attendance klassi
- Ustunlar: id, student_id, schedule_id,
            date, status, created_at
- Status qiymatlari: present | absent | late | excused
- Relationship: student  → (qaysi talaba)
                schedule → (qaysi dars)
```

### `grade.py`
```python
- Grade klassi
- Ustunlar: id, student_id, subject_id, semester,
            midterm1, midterm2, final_score, total,
            letter_grade, gpa_point,
            created_at, updated_at
- Relationship: student → (qaysi talaba)
                subject → (qaysi fan)
```

### `exam.py`
```python
- Exam klassi (imtihon jadvali)
- ExamResult klassi (imtihon natijalari)
- Exam ustunlari: id, subject_id, semester, exam_type,
                  exam_date, room, duration_minutes, created_at
- ExamResult ustunlari: id, exam_id, student_id,
                        score, is_passed, created_at
- Relationship (Exam): subject → (qaysi fan)
                        results → (natijalar)
- Relationship (ExamResult): exam    → (qaysi imtihon)
                              student → (qaysi talaba)
```

### `financial.py`
```python
- Contract klassi (to'lov kontrakt)
- Scholarship klassi (stipendiya)
- Contract ustunlari: id, student_id, contract_number,
                      academic_year, amount, paid_amount,
                      due_date, is_paid, created_at
- Scholarship ustunlari: id, student_id, month, amount,
                         is_paid, paid_date, created_at
- Relationship: student → (qaysi talaba)
```

### `message.py`
```python
- Message klassi
- Ustunlar: id, sender_id, receiver_id,
            subject, body, status, created_at
- Status qiymatlari: sent | read
- Relationship: sender   → Student (yuboruvchi)
                receiver → Student (qabul qiluvchi)
```

### `announcement.py`
```python
- Announcement klassi
- Ustunlar: id, title, content, target_group,
            is_active, expires_at, created_at
```

### `login_history.py`
```python
- LoginHistory klassi
- Ustunlar: id, student_id, ip_address,
            user_agent, login_at, is_success
- Relationship: student → (qaysi talaba)
```

### `certificate.py`
```python
- Certificate klassi
- Ustunlar: id, student_id, name, issued_by,
            issued_date, file_url, created_at
- Relationship: student → (qaysi talaba)
```

### `audit_log.py`
```python
- AuditLog klassi
- Ustunlar: id, user_id, action,
            old_value, new_value, created_at
- Relationship: student → (kim o'zgartirdi)
```

---

## 🔗 Relationships

> 💡 **Relationship nima?** — Jadvallar o'rtasidagi bog'liqlik.
> - `one-to-many` = bittasi ko'pini bog'laydi
> - `many-to-many` = ko'pi ko'pini bog'laydi (oraliq jadval kerak)

```
Faculty → Department         : one-to-many  (1 fakultetda ko'p kafedra)
Department → Group           : one-to-many  (1 kafedrada ko'p guruh)
Department → Teacher         : one-to-many  (1 kafedrada ko'p o'qituvchi)
Department → Subject         : one-to-many  (1 kafedra ko'p fan o'qitadi)
Group → Student              : one-to-many  (1 guruhda ko'p talaba)

Student → Attendance         : one-to-many  (1 talabaning ko'p davomati)
Student → Grade              : one-to-many  (1 talabaning ko'p bahosi)
Student → ExamResult         : one-to-many  (1 talabaning ko'p imtihon natijasi)
Student → Contract           : one-to-many  (1 talabaning ko'p kontrakti)
Student → Scholarship        : one-to-many  (1 talabaning ko'p stipendiyasi)
Student → Certificate        : one-to-many  (1 talabaning ko'p sertifikati)
Student → LoginHistory       : one-to-many  (1 talabaning ko'p kirish tarixi)
Student → AuditLog           : one-to-many  (1 talabaning ko'p o'zgarish tarixi)

Student ↔ Student (Message)  : many-to-many (talabalar bir-biriga xabar yubora oladi)
                                              sender_id va receiver_id — ikkalasi ham student.id

Subject ↔ Group (Schedule)   : many-to-many (1 fan ko'p guruhda, 1 guruhda ko'p fan)
                                              Schedule oraliq jadval bo'lib xizmat qiladi

Subject → Exam               : one-to-many  (1 fanning ko'p imtihoni)
Subject → Grade              : one-to-many  (1 fanning ko'p talabadagi bahosi)
Subject → Schedule           : one-to-many  (1 fan ko'p jadvallarda)
Teacher → Schedule           : one-to-many  (1 o'qituvchi ko'p jadvalda)
Exam → ExamResult            : one-to-many  (1 imtihonda ko'p talabaning natijasi)
Schedule → Attendance        : one-to-many  (1 dars ko'p talabaning davomatini yozadi)
```

### Kaskad o'chirish (ON DELETE CASCADE)

> 💡 "Ota" o'chirilsa "bolalari" ham o'chadi. Lekin bizda `is_deleted=True` ishlatamiz — hech narsa haqiqatda o'chmaydi!

```
Faculty     o'chirilsa → Departmentlari ham o'chadi
Department  o'chirilsa → Grouplar, Teacherlar, Subjectlar ham o'chadi
Group       o'chirilsa → Studentlar ham o'chadi
Student     o'chirilsa → Grades, Attendances, Contracts... ham o'chadi
Exam        o'chirilsa → ExamResultlar ham o'chadi
```

---

## 👥 Rollar tizimi

| Rol | Kimlar? | Nimalarga kirishi mumkin? |
|-----|---------|--------------------------|
| `student` | Talabalar | Faqat **o'z** ma'lumotlari |
| `teacher` | O'qituvchilar | O'z fani va guruhi |
| `admin` | Dekanat | Barcha talabalar ma'lumotlari |
| `superadmin` | Tizim boshqaruvchisi | Hamma narsa |

### Har bir rol nima qila oladi?

```
student
  ✅ O'z profilini ko'rish va yangilash (telefon, email, manzil)
  ✅ O'z dars jadvalini ko'rish
  ✅ O'z davomatini ko'rish
  ✅ O'z baholarini ko'rish
  ✅ O'z imtihon jadvalini ko'rish
  ✅ O'z kontrakt va stipendiyasini ko'rish
  ✅ Xabar yuborish va olish
  ✅ E'lonlarni ko'rish
  ❌ Boshqa talabaning ma'lumotlarini ko'rish
  ❌ Hech narsani o'zgartirish (faqat o'z profili)

teacher
  ✅ O'z fanidagi guruhlar jadvalini ko'rish
  ✅ O'z guruhidagi talabalar davomatini belgilash
  ✅ O'z guruhidagi talabalar baholarini ko'rish
  ✅ E'lonlarni ko'rish
  ❌ Boshqa o'qituvchining faniga kirish

admin
  ✅ Barcha talabalar ma'lumotlarini ko'rish
  ✅ Barcha guruhlar va jadvallarni ko'rish
  ✅ E'lon yaratish
  ❌ Tizim sozlamalarini o'zgartirish

superadmin
  ✅ Hamma narsa
  ✅ Foydalanuvchi yaratish va o'chirish
  ✅ Rol berish
  ✅ Tizim sozlamalarini o'zgartirish
```

---

## 🌐 API Endpointlar

> 🔒 — bu belgili endpointlar uchun token kerak (login qilmasdan ishlamaydi)

Token headerga shunday qo'shiladi:
```
Authorization: Bearer <tokeningiz>
```

---

### 🔐 Kirish — `/api/v1/auth`

| Method | URL | Tavsif |
|--------|-----|--------|
| `POST` | `/api/v1/auth/login` | Tizimga kirish — token olish |
| `POST` | `/api/v1/auth/logout` | 🔒 Chiqish |
| `POST` | `/api/v1/auth/change-password` | 🔒 Parol o'zgartirish |

Login so'rovi:
```json
{
  "student_id": "20210001",
  "password": "parolingiz"
}
```

Login javobi:
```json
{
  "access_token": "eyJhbGci...",
  "token_type": "bearer",
  "full_name": "Aliyev Jasur Karimovich",
  "role": "student",
  "group": "CS-21-01",
  "semester": 6
}
```

> Bu `access_token` ni saqlab qoling — keyingi barcha so'rovlarda kerak!

---

### 👤 Talaba profili — `/api/v1/student`

| Method | URL | Tavsif |
|--------|-----|--------|
| `GET` | `/api/v1/student/profile` | 🔒 O'z profilini ko'rish |
| `PUT` | `/api/v1/student/profile` | 🔒 Telefon/email/manzil o'zgartirish |
| `GET` | `/api/v1/student/gpa` | 🔒 GPA ballini ko'rish |
| `GET` | `/api/v1/student/login-history` | 🔒 Oxirgi 20 ta kirish |
| `GET` | `/api/v1/student/certificates` | 🔒 Sertifikatlar |

---

### 📚 Dars jadvali — `/api/v1/curriculum`

| Method | URL | Tavsif |
|--------|-----|--------|
| `GET` | `/api/v1/curriculum/schedule` | 🔒 Dars jadvali (`?semester=6&day=1`) |
| `GET` | `/api/v1/curriculum/subjects` | 🔒 Semestr fanlari ro'yxati |

Jadval javobi:
```json
[
  {
    "subject": "Algoritmlar nazariyasi",
    "teacher_name": "Karimov Behruz Saidovich",
    "day_name": "Dushanba",
    "lesson_number": 2,
    "start_time": "09:30",
    "end_time": "11:00",
    "room": "A-301",
    "lesson_type": "Ma'ruza"
  }
]
```

---

### 📅 Davomat — `/api/v1/attendance`

| Method | URL | Tavsif |
|--------|-----|--------|
| `GET` | `/api/v1/attendance/` | 🔒 Davomat ro'yxati (`?page=1&limit=20`) |
| `GET` | `/api/v1/attendance/summary` | 🔒 Fan bo'yicha foiz |

> 💡 `page` va `limit` — 500 ta yozuv birdaniga emas, 20 tadan bo'lib yuboriladi.

---

### 📊 Baholar — `/api/v1/grades`

| Method | URL | Tavsif |
|--------|-----|--------|
| `GET` | `/api/v1/grades/` | 🔒 Baholar ro'yxati (`?semester=6`) |
| `GET` | `/api/v1/grades/gpa-summary` | 🔒 Barcha semestrlar GPA |

**Letter grade tizimi:**

| Ball | Harf | GPA |
|------|------|-----|
| 90–100 | A | 4.0 |
| 85–89 | A- | 3.7 |
| 80–84 | B+ | 3.3 |
| 75–79 | B | 3.0 |
| 70–74 | B- | 2.7 |
| 65–69 | C+ | 2.3 |
| 60–64 | C | 2.0 |
| 55–59 | C- | 1.7 |
| 50–54 | D | 1.0 |
| 0–49 | F | 0.0 |

---

### 📝 Imtihonlar — `/api/v1/exams`

| Method | URL | Tavsif |
|--------|-----|--------|
| `GET` | `/api/v1/exams/` | 🔒 Imtihon jadvali va natijalar (`?semester=6`) |

---

### 💰 Moliya — `/api/v1/financial`

| Method | URL | Tavsif |
|--------|-----|--------|
| `GET` | `/api/v1/financial/contracts` | 🔒 Kontrakt summasi va qoldig'i |
| `GET` | `/api/v1/financial/scholarships` | 🔒 Stipendiya (faqat grant talabalar) |
| `GET` | `/api/v1/financial/summary` | 🔒 Umumiy to'lov holati |

---

### ✉️ Xabarlar — `/api/v1/messages`

| Method | URL | Tavsif |
|--------|-----|--------|
| `GET` | `/api/v1/messages/` | 🔒 Barcha xabarlar (`?page=1&limit=20`) |
| `POST` | `/api/v1/messages/` | 🔒 Xabar yuborish |
| `PATCH` | `/api/v1/messages/{id}/read` | 🔒 O'qilgan deb belgilash |

Xabar yuborish:
```json
{
  "receiver_student_id": "20210002",
  "subject": "Laboratoriya haqida",
  "body": "Ertangi labga kelasizmi?"
}
```

> ⚠️ O'zingizga xabar yuborish → `400 Bad Request`
> ⚠️ Boshqa birovning xabarini o'qish → `403 Forbidden`

---

### 📢 E'lonlar — `/api/v1/announcements`

| Method | URL | Tavsif |
|--------|-----|--------|
| `GET` | `/api/v1/announcements/` | 🔒 Muddati o'tmagan faol e'lonlar |

---

## 🔑 JWT Token qanday ishlaydi?

```
1. Talaba  →  student_id + parol yuboradi
                    ↓
2. Server  →  parolni tekshiradi (bcrypt)
                    ↓
3. To'g'ri →  python-jose yordamida JWT token yaratadi
                    ↓
4. Talaba  →  har so'rovda tokenni yuboradi
                    ↓
5. Server  →  tokenni tekshiradi, kimligini biladi
```

Token 24 soat amal qiladi. Muddati o'tsa — qayta login qilish kerak.

---

## 🛡️ Xavfsizlik

### Parol xavfsizligi
- bcrypt bilan xeshlanadi — bazada oddiy matn saqlanmaydi
- Kimdir bazani o'g'irlasa ham parollarni bila olmaydi
- Kamida 8 belgi, 1 katta harf, 1 raqam talab qilinadi

### Ma'lumot himoyasi
- Har so'rovda `current_user.id == requested_id` tekshiriladi
- Boshqa talabaning ma'lumotiga urinish → `403 Forbidden`

### Soft delete
- Ma'lumot o'chirilganda bazadan butunlay ketmaydi
- `is_deleted = True` bo'ladi — kerak bo'lsa qaytarib olsa bo'ladi

### Audit log
- Kim nima o'zgartirdi — hammasi yozib boriladi
```
[2024-03-15 10:30] student:20210001 → profilini yangiladi
[2024-03-15 11:00] admin:001        → 20210002 bahosini o'zgartirdi
```

## 🗃️ Migratsiya (Alembic)

> 💡 Model o'zgarganda Alembic bazani avtomatik yangilaydi. Git kabi — tarix saqlanadi.

```bash
# Birinchi marta: barcha jadvallarni yaratish
alembic upgrade head

# Model o'zgarganda yangi migratsiya fayli yaratish
alembic revision --autogenerate -m "nima o'zgardi"

# O'zgarishlarni bazaga qo'llash
alembic upgrade head

# Xato bo'lsa — bir qadam orqaga
alembic downgrade -1

# Tarixni ko'rish
alembic history

## 📄 Litsenziya

MIT — xohlaganingizcha foydalaning.

---
