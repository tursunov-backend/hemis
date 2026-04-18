# 🎓 HEMIS Backend API

O'zbekiston universitetlarining **HEMIS Student tizimi** uchun backend API.  
Talabalar o'z profili, baholar, davomat, jadval va moliyaviy ma'lumotlarini ko'ra oladi.
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
| **JWT** | Token orqali foydalanuvchini tanish |
| **bcrypt** | Parolni xavfsiz saqlash |
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
    ├── models/                  ← Baza jadvallari
    │   │
    │   │  💡 Har bir fayl = bitta jadval
    │   │     Barcha modellarda bor:
    │   │       created_at — qachon yaratilgan
    │   │       updated_at — qachon o'zgartirilgan
    │   │       is_deleted — o'chirilganmi? (haqiqatda o'chmaydi)
    │   │
    │   ├── __init__.py
    │   ├── user.py              ← Tizim foydalanuvchisi
    │   ├── role.py              ← Rollar: student, teacher, admin
    │   ├── faculty.py           ← Fakultetlar
    │   ├── department.py        ← Kafedralar
    │   ├── group.py             ← Guruhlar
    │   ├── teacher.py           ← O'qituvchilar
    │   ├── student.py           ← Talabalar ⭐
    │   ├── subject.py           ← Fanlar
    │   ├── schedule.py          ← Dars jadvali
    │   ├── attendance.py        ← Davomat
    │   ├── grade.py             ← Baholar
    │   ├── exam.py              ← Imtihonlar
    │   ├── financial.py         ← Kontrakt va stipendiya
    │   ├── message.py           ← Xabarlar
    │   ├── announcement.py      ← E'lonlar
    │   ├── audit_log.py         ← Kim nima o'zgartirdi?
    │   ├── login_history.py     ← Kirish tarixi
    │   └── certificate.py       ← Sertifikatlar
    │
    ├── schemas/                 ← API ma'lumot formatlari
    │   │
    │   │  ⚠️ model ≠ schema farqi:
    │   │     model  = bazadagi jadval ko'rinishi
    │   │     schema = API orqali keladigan/ketadigan ma'lumot
    │   │
    │   ├── __init__.py
    │   ├── common.py            ← Umumiy formatlar (pagination, xato)
    │   ├── auth.py              ← Login so'rovi va javob
    │   ├── student.py           ← Profil formati
    │   ├── curriculum.py        ← Jadval va fanlar
    │   ├── attendance.py        ← Davomat
    │   ├── grade.py             ← Baholar
    │   ├── exam.py              ← Imtihonlar
    │   ├── financial.py         ← Kontrakt, stipendiya
    │   ├── message.py           ← Xabarlar
    │   └── announcement.py      ← E'lonlar
    │
    ├── crud/                    ← Baza bilan ishlash logikasi
    │   │
    │   │  💡 Nima uchun alohida?
    │   │     Router  → HTTP so'rovlarni qabul qiladi
    │   │     CRUD    → faqat baza bilan ishlaydi
    │   │     Shunday bo'lsa kod toza va tushunarli bo'ladi
    │   │
    │   ├── __init__.py
    │   ├── auth.py              ← Login, logout, parol o'zgartirish
    │   ├── student.py           ← Profil olish, yangilash
    │   ├── attendance.py        ← Davomat
    │   ├── grade.py             ← Baholar, GPA
    │   ├── exam.py              ← Imtihonlar
    │   ├── financial.py         ← Kontrakt, stipendiya
    │   └── message.py           ← Xabarlar
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
    │           ├── auth.py      ← /api/v1/auth/...
    │           ├── student.py   ← /api/v1/student/...
    │           ├── curriculum.py← /api/v1/curriculum/...
    │           ├── attendance.py← /api/v1/attendance/...
    │           ├── grades.py    ← /api/v1/grades/...
    │           ├── exams.py     ← /api/v1/exams/...
    │           ├── financial.py ← /api/v1/financial/...
    │           ├── messages.py  ← /api/v1/messages/...
    │           └── announcements.py
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
linux
sudo -u postgres psql

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
DB_HOST=
DB_PORT=
DB_USER=
DB_PASS=
DB_NAME=

SECRET_KEY=bu-yerga-kamida-32-belgi-yozing
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
```

> 🔑 Xavfsiz kalit yasash:
> ```bash
> # Linux / Mac
> openssl rand -hex 32
>
> # Windows (PowerShell)
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

---

## 🗄️ Schema Overview

> 💡 Barcha jadvallar, ustunlar va ma'lumot turlari.
> `PK` = asosiy kalit, `FK` = boshqa jadvalga havola, `nullable` = bo'sh bo'lishi mumkin

```
faculty
  id          INTEGER   PK
  name        VARCHAR(100)
  code        VARCHAR(20)    UNIQUE
  created_at  TIMESTAMP

department
  id          INTEGER   PK
  name        VARCHAR(100)
  code        VARCHAR(20)    UNIQUE
  faculty_id  INTEGER   FK → faculty.id

group
  id              INTEGER   PK
  name            VARCHAR(50)
  department_id   INTEGER   FK → department.id
  course          INTEGER                      (1-4 yil)
  education_form  VARCHAR(20)                  (kunduzgi, sirtqi)
  education_lang  VARCHAR(20)                  (uzbek, rus)

teacher
  id              INTEGER   PK
  first_name      VARCHAR(100)
  last_name       VARCHAR(100)
  middle_name     VARCHAR(100)   (nullable)
  email           VARCHAR(255)   UNIQUE (nullable)
  phone           VARCHAR(20)    (nullable)
  department_id   INTEGER   FK → department.id

student  ⭐
  id              INTEGER   PK
  student_id      VARCHAR(20)    UNIQUE        (login: 20210001)
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
  group_id        INTEGER   FK → group.id
  semester        INTEGER                      (1-8)
  status          VARCHAR(20)                  (active, academic, expelled)
  payment_type    VARCHAR(20)                  (grant, contract)
  admission_year  INTEGER
  gpa             FLOAT          (nullable)
  is_active       BOOLEAN        default=True
  last_login      TIMESTAMP      (nullable)
  created_at      TIMESTAMP
  updated_at      TIMESTAMP
  is_deleted      BOOLEAN        default=False

subject
  id            INTEGER   PK
  name          VARCHAR(200)
  code          VARCHAR(20)    UNIQUE
  credits       INTEGER
  semester      INTEGER
  department_id INTEGER   FK → department.id

schedule
  id             INTEGER   PK
  subject_id     INTEGER   FK → subject.id
  teacher_id     INTEGER   FK → teacher.id
  group_id       INTEGER   FK → group.id
  semester       INTEGER
  day_of_week    INTEGER                       (1=Dushanba, 7=Yakshanba)
  lesson_number  INTEGER                       (1-6)
  start_time     TIME
  end_time       TIME
  room           VARCHAR(50)    (nullable)
  lesson_type    VARCHAR(20)                   (lecture, practice, lab)

attendance
  id           INTEGER   PK
  student_id   INTEGER   FK → student.id
  schedule_id  INTEGER   FK → schedule.id
  date         DATE
  status       VARCHAR(20)                     (present, absent, late, excused)
  created_at   TIMESTAMP

grade
  id           INTEGER   PK
  student_id   INTEGER   FK → student.id
  subject_id   INTEGER   FK → subject.id
  semester     INTEGER
  midterm1     INTEGER                         (0-30)
  midterm2     INTEGER                         (0-30)
  final_score  INTEGER                         (0-40)
  total        INTEGER                         (0-100)
  letter_grade VARCHAR(5)     (nullable)       (A, A-, B+...)
  gpa_point    FLOAT          (nullable)       (0.0-4.0)
  created_at   TIMESTAMP
  updated_at   TIMESTAMP

exam
  id               INTEGER   PK
  subject_id       INTEGER   FK → subject.id
  semester         INTEGER
  exam_type        VARCHAR(20)                 (midterm, final)
  exam_date        DATETIME
  room             VARCHAR(50)   (nullable)
  duration_minutes INTEGER

exam_result
  id         INTEGER   PK
  exam_id    INTEGER   FK → exam.id
  student_id INTEGER   FK → student.id
  score      INTEGER
  is_passed  BOOLEAN

contract
  id              INTEGER   PK
  student_id      INTEGER   FK → student.id
  contract_number VARCHAR(50)    UNIQUE
  academic_year   VARCHAR(20)                  (2024-2025)
  amount          DECIMAL(12,2)
  paid_amount     DECIMAL(12,2)  default=0
  due_date        DATE
  is_paid         BOOLEAN        default=False
  created_at      TIMESTAMP

scholarship
  id         INTEGER   PK
  student_id INTEGER   FK → student.id
  month      DATE
  amount     DECIMAL(10,2)
  is_paid    BOOLEAN        default=False
  paid_date  DATE           (nullable)
  created_at TIMESTAMP

message
  id          INTEGER   PK
  sender_id   INTEGER   FK → student.id
  receiver_id INTEGER   FK → student.id
  subject     VARCHAR(255)
  body        TEXT
  status      VARCHAR(20)                      (sent, read)
  created_at  TIMESTAMP

announcement
  id           INTEGER   PK
  title        VARCHAR(255)
  content      TEXT
  target_group VARCHAR(50)    (nullable)        (all, cs-21, ...)
  is_active    BOOLEAN        default=True
  expires_at   TIMESTAMP      (nullable)
  created_at   TIMESTAMP

login_history
  id         INTEGER   PK
  student_id INTEGER   FK → student.id
  ip_address VARCHAR(50)    (nullable)
  user_agent TEXT           (nullable)
  login_at   TIMESTAMP
  is_success BOOLEAN

certificate
  id          INTEGER   PK
  student_id  INTEGER   FK → student.id
  name        VARCHAR(255)
  issued_by   VARCHAR(255)
  issued_date DATE
  file_url    VARCHAR(500)   (nullable)
  created_at  TIMESTAMP

audit_log
  id         INTEGER   PK
  user_id    INTEGER   FK → student.id
  action     VARCHAR(100)                      (profile_updated, grade_viewed...)
  old_value  TEXT      (nullable)              (JSON ko'rinishida)
  new_value  TEXT      (nullable)              (JSON ko'rinishida)
  created_at TIMESTAMP
```

---

## 🔗 Relationships

> 💡 **Relationship nima?** — Jadvallar o'rtasidagi bog'liqlik.
> `one-to-many` = bittasi ko'pini; `many-to-many` = ko'pi ko'pini bog'laydi

```
Faculty → Department    : one-to-many  (1 fakultetda ko'p kafedra bor)
Department → Group      : one-to-many  (1 kafedrada ko'p guruh bor)
Department → Teacher    : one-to-many  (1 kafedrada ko'p o'qituvchi bor)
Department → Subject    : one-to-many  (1 kafedra ko'p fan o'qitadi)
Group → Student         : one-to-many  (1 guruhda ko'p talaba bor)

Student → Attendance    : one-to-many  (1 talabaning ko'p davomati bor)
Student → Grade         : one-to-many  (1 talabaning ko'p bahosi bor)
Student → ExamResult    : one-to-many  (1 talabaning ko'p imtihon natijasi bor)
Student → Contract      : one-to-many  (1 talabaning ko'p kontrakti bor)
Student → Scholarship   : one-to-many  (1 talabaning ko'p stipendiyasi bor)
Student → Certificate   : one-to-many  (1 talabaning ko'p sertifikati bor)
Student → LoginHistory  : one-to-many  (1 talabaning ko'p kirish tarixi bor)
Student → AuditLog      : one-to-many  (1 talabaning ko'p o'zgarish tarixi bor)

Student ↔ Student (Message) : many-to-many  (talabalar bir-biriga xabar yubora oladi)
                                             sender_id va receiver_id ikkalasi ham student.id

Subject ↔ Group (Schedule)  : many-to-many  (1 fan ko'p guruhda, 1 guruhda ko'p fan)
                                             Schedule oraliq jadval bo'lib xizmat qiladi

Subject → Exam          : one-to-many  (1 fanning ko'p imtihoni bor)
Subject → Grade         : one-to-many  (1 fanning ko'p talabadagi bahosi bor)
Subject → Schedule      : one-to-many  (1 fan ko'p jadvallarda bor)
Teacher → Schedule      : one-to-many  (1 o'qituvchi ko'p jadvalda bor)
Exam → ExamResult       : one-to-many  (1 imtihonda ko'p talabaning natijasi bor)
Schedule → Attendance   : one-to-many  (1 dars ko'p talabaning davomatini yozadi)
```

### Kaskad o'chirish (ON DELETE CASCADE)

> 💡 Agar "ota" o'chirilsa, "bolalari" ham avtomatik o'chadi.

```
Faculty o'chirilsa    → uning Departmentlari ham o'chadi
Department o'chirilsa → uning Grouplar, Teacherlar, Subjectlari ham o'chadi
Group o'chirilsa      → uning Studentlari ham o'chadi
Student o'chirilsa    → uning Grades, Attendance, Contracts... ham o'chadi
Exam o'chirilsa       → uning ExamResultlari ham o'chadi
```

> ⚠️ Lekin bizda `is_deleted = True` ishlatamiz — haqiqatda hech narsa o'chmaydi!

---

## 👥 Rollar tizimi

> 💡 Har bir foydalanuvchi ma'lum bir "rol" ga ega. Rol uning nimalarga kira olishini belgilaydi.

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
  ❌ Hech narsani o'zgartirish (faqat profil)

teacher
  ✅ O'z fanidagi guruhlar jadvalini ko'rish
  ✅ O'z guruhidagi talabalar davomatini belgilash
  ✅ O'z guruhidagi talabalar baholarini ko'rish
  ✅ E'lonlarni ko'rish
  ❌ Boshqa o'qituvchining faniga kirish

admin
  ✅ Barcha talabalar ma'lumotlarini ko'rish
  ✅ Barcha guruhlar va jadvallarni ko'rish
  ✅ Hisobotlar olish
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

> 🔒 — bu belgili endpointlar uchun token kerak (login dan oldin ishlamaydi)

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
3. To'g'ri →  JWT token yaratib qaytaradi
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

---

## ⚙️ Muhit o'zgaruvchilari (`.env`)

```env
DB_HOST=
DB_PORT=
DB_USER=
DB_PASS=
DB_NAME=

SECRET_KEY=bu-yerga-kamida-32-belgi-yozing
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
```

---

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
```

---

## 🐞 Tez-tez uchraydigan xatolar

**`ModuleNotFoundError`** — kutubxona o'rnatilmagan:
```bash
pip install -r requirements.txt
```

**`could not connect to server`** — PostgreSQL ishlamayapti:
```bash
sudo systemctl start postgresql    # Linux
brew services start postgresql     # Mac
```

**`alembic: command not found`** — virtual muhit yoqilmagan:
```bash
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

**`401 Unauthorized`** — token yo'q yoki muddati o'tgan. Qayta login qiling.

**`403 Forbidden`** — bu ma'lumotga ruxsatingiz yo'q.

**`422 Unprocessable Entity`** — ma'lumot formati noto'g'ri. `/docs` da namunani tekshiring.

---

## 📄 Litsenziya

MIT — xohlaganingizcha foydalaning.

---
