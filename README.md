# 🎓 HEMIS Backend API

O'zbekiston universitetlarining **HEMIS Student tizimi** uchun to'liq RESTful backend API.  
`student.samtuit.uz` platformasiga mos keluvchi server tomoni.

> 💡 **Backend nima?** — Foydalanuvchi ko'rmaydigan "orqa" qism. Telefon yoki veb-sayt shu backend bilan gaplashib ma'lumot oladi.

---

## 📋 Mundarija

- [Texnologiyalar](#-texnologiyalar)
- [Loyiha strukturasi](#-loyiha-strukturasi)
- [O'rnatish](#-ornatish)
- [Ishga tushirish](#-ishga-tushirish)
- [Rollar va ruxsatlar](#-rollar-va-ruxsatlar-rbac)
- [API Endpointlar](#-api-endpointlar)
- [Xavfsizlik](#-xavfsizlik)
- [Muhit o'zgaruvchilari](#-muhit-ozgaruvchilari)
- [Docker](#-docker)
- [Testlar](#-testlar)
- [Migratsiya](#-migratsiya)
- [Tez-tez uchraydigan xatolar](#-tez-tez-uchraydigan-xatolar)

---

## 🛠️ Texnologiyalar

| Texnologiya | Bu nima? |
|---|---|
| **Python 3.11+** | Dasturlash tili |
| **FastAPI** | Web framework — API yaratish uchun |
| **PostgreSQL** | Ma'lumotlar bazasi |
| **SQLAlchemy 2.0** | Python orqali bazaga murojaat (SQL yozmasdan) |
| **Alembic** | Baza o'zgarishlarini boshqarish (migratsiya) |
| **Pydantic v2** | Kelayotgan ma'lumotlarni tekshirish |
| **JWT (python-jose)** | Foydalanuvchi kimligini tekshirish |
| **bcrypt (passlib)** | Parolni xavfsiz saqlash |
| **Redis** | Tezkor kesh va rate limiting |
| **Celery** | Orqa fon vazifalari (email, notification) |
| **slowapi** | Brute-force hujumlardan himoya |
| **structlog** | Professional log tizimi |
| **Docker** | Loyihani istalgan joyda ishlatish |
| **pytest** | Avtomatik testlar |
| **Uvicorn** | Serverni ishga tushiruvchi dastur |

---

## 📁 Loyiha strukturasi

> 💡 Har bir papka va fayl nima uchun ekanini tushuntirdik. Avval bularni o'qing!

```
hemis_backend/
│
├── main.py                      ← Ilova shu yerdan boshlanadi
├── requirements.txt             ← Barcha kutubxonalar ro'yxati
├── .env                         ← Maxfiy sozlamalar — GitHubga chiqarma! ⚠️
├── .env.example                 ← .env uchun namuna (GitHubga qo'ysa bo'ladi)
├── alembic.ini                  ← Alembic sozlamasi
├── Dockerfile                   ← Docker image yaratish uchun
├── docker-compose.yml           ← Barcha servislarni birga ishga tushirish
├── .github/
│   └── workflows/
│       └── ci.yml               ← GitHub Actions: test + deploy
├── README.md
│
├── alembic/                     ← Baza o'zgarishlari tarixi
│   └── versions/
│
├── tests/                       ← Avtomatik testlar
│   ├── conftest.py              ← Test sozlamalari va umumiy fixtures
│   ├── test_auth.py             ← Login, logout, token testlari
│   ├── test_student.py          ← Profil testlari
│   ├── test_grades.py           ← Baho testlari
│   ├── test_attendance.py       ← Davomat testlari
│   ├── test_financial.py        ← Moliya testlari
│   ├── test_messages.py         ← Xabar testlari
│   ├── test_security.py         ← Xavfsizlik testlari (rate limit, auth)
│   └── test_permissions.py      ← Rol va ruxsat testlari
│
└── app/
    ├── __init__.py
    │
    ├── core/                    ← Ilova "yuragi" — eng asosiy sozlamalar
    │   ├── config.py            ← .env fayldan sozlamalarni o'qiydi
    │   ├── security.py          ← JWT token yaratish va tekshirish, bcrypt
    │   ├── dependencies.py      ← get_current_user, require_role va boshqalar
    │   ├── permissions.py       ← Kim nimaga ruxsati bor? (RBAC)
    │   ├── rate_limiter.py      ← Brute-force himoyasi (slowapi + Redis)
    │   ├── logging.py           ← structlog sozlamasi
    │   └── exceptions.py        ← Global exception handler (markazlashgan)
    │
    ├── db/                      ← Database bilan bog'liq hamma narsa
    │   ├── base.py              ← Barcha modellar meros oladigan asosiy class
    │   ├── session.py           ← Bazaga ulanish va get_db() funksiyasi
    │   ├── redis.py             ← Redis ulanishi (cache + rate limit)
    │   └── init_db.py           ← Boshlang'ich ma'lumotlar (seed data)
    │
    ├── models/                  ← Baza jadvallari (har bir fayl = bir jadval)
    │   │
    │   │  💡 Barcha modellarda quyidagilar bor:
    │   │     created_at  — qachon yaratilgan
    │   │     updated_at  — qachon o'zgartirilgan
    │   │     is_deleted  — o'chirilganmi? (soft delete)
    │   │
    │   ├── __init__.py
    │   ├── user.py              ← Tizim foydalanuvchisi (student/teacher/admin)
    │   ├── role.py              ← Rollar: student, teacher, admin, superadmin
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
    │   ├── audit_log.py         ← Kim nima o'zgartirdi? (audit)
    │   ├── login_history.py     ← Kirish tarixi
    │   └── certificate.py       ← Sertifikatlar
    │
    ├── schemas/                 ← API ma'lumot formatlari (Pydantic v2)
    │   │
    │   │  ⚠️ model ≠ schema!
    │   │     model  = bazadagi jadval
    │   │     schema = API orqali keladigan/ketadigan ma'lumot
    │   │
    │   ├── __init__.py
    │   ├── common.py            ← PaginatedResponse, ErrorResponse (umumiy)
    │   ├── auth.py              ← LoginRequest, TokenResponse
    │   ├── user.py              ← UserOut, RoleOut
    │   ├── student.py           ← StudentProfile, StudentUpdate
    │   ├── curriculum.py        ← ScheduleItem, SubjectOut
    │   ├── attendance.py        ← AttendanceOut, AttendanceSummary
    │   ├── grade.py             ← GradeOut, GPASummary
    │   ├── exam.py              ← ExamOut, ExamResultOut
    │   ├── financial.py         ← ContractOut, ScholarshipOut
    │   ├── message.py           ← MessageOut, MessageCreate
    │   └── announcement.py      ← AnnouncementOut
    │
    ├── crud/                    ← Baza bilan ishlash logikasi
    │   │
    │   │  💡 Nima uchun alohida papka?
    │   │     Router  → faqat HTTP so'rovlarni qabul qiladi
    │   │     CRUD    → faqat baza bilan ishlaydi
    │   │     Bu "Separation of Concerns" deyiladi — har narsa o'z joyida
    │   │
    │   ├── __init__.py
    │   ├── base.py              ← Umumiy CRUD operatsiyalar (get, create, update)
    │   ├── auth.py              ← Login, logout, parol o'zgartirish
    │   ├── student.py           ← Profil olish, yangilash
    │   ├── attendance.py        ← Davomat ma'lumotlari
    │   ├── grade.py             ← Baho va GPA
    │   ├── exam.py              ← Imtihon
    │   ├── financial.py         ← Kontrakt va stipendiya
    │   └── message.py           ← Xabar yuborish/olish
    │
    ├── api/                     ← HTTP so'rovlarni qabul qiluvchi qatlam
    │   ├── __init__.py
    │   └── v1/                  ← API versiya 1 (/api/v1/...)
    │       ├── __init__.py
    │       ├── router.py        ← Barcha routerlarni birlashtiradi
    │       └── routes/
    │           ├── __init__.py
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
    ├── tasks/                   ← Orqa fon vazifalari (Celery)
    │   ├── __init__.py
    │   ├── celery_app.py        ← Celery sozlamasi
    │   ├── email_tasks.py       ← Email yuborish (async)
    │   └── notification_tasks.py← Push notification
    │
    └── utils/                   ← Yordamchi funksiyalar
        ├── __init__.py
        ├── enums.py             ← Barcha Enum'lar (status, tur, shakl...)
        ├── pagination.py        ← limit/offset pagination
        ├── grade_utils.py       ← 87 ball → "A-" va 3.7 GPA
        ├── validators.py        ← Parol kuchi, telefon, email tekshiruvi
        └── cache.py             ← Redis cache yordamchi funksiyalar
```

---

## 💻 O'rnatish

### 1. Repozitoriyani yuklab oling

```bash
git clone https://github.com/username/hemis-backend.git
cd hemis-backend
```

### 2. Virtual muhit yarating

> 💡 Har bir loyiha uchun alohida "xona" — kutubxonalar aralashmaydi.

```bash
python -m venv venv

# Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate

# (venv) belgisi chiqsa — muvaffaqiyatli
```

### 3. Kutubxonalarni o'rnating

```bash
pip install -r requirements.txt
```

### 4. PostgreSQL bazasini yarating

```bash
psql -U postgres

CREATE DATABASE hemis_db;
CREATE USER hemis_user WITH PASSWORD 'parol123';
GRANT ALL PRIVILEGES ON DATABASE hemis_db TO hemis_user;
\q
```

### 5. Redis o'rnating

> 💡 Redis — tezkor xotira. Rate limiting va cache uchun kerak.

```bash
# Ubuntu / Debian
sudo apt install redis-server
sudo systemctl start redis

# Mac
brew install redis
brew services start redis

# Ishlayaptimi?
redis-cli ping   # → PONG
```

### 6. .env faylini sozlang

```bash
cp .env.example .env
```

`.env` ichida:

```env
# Database
DATABASE_URL=postgresql://hemis_user:parol123@localhost:5432/hemis_db

# JWT
SECRET_KEY=bu-yerga-kamida-32-ta-belgi-yozing
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Redis
REDIS_URL=redis://localhost:6379/0

# Rate limiting
LOGIN_RATE_LIMIT=5/minute

# Celery
CELERY_BROKER_URL=redis://localhost:6379/1

# Email (ixtiyoriy)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=sizning@email.com
SMTP_PASSWORD=emailparol

# Muhit (development yoki production)
APP_ENV=development
DEBUG=True
```

> 🔑 Xavfsiz kalit yaratish:
> ```bash
> openssl rand -hex 32
> ```

---

## ▶️ Ishga tushirish

### Oddiy usul

```bash
# Jadvallarni bazada yaratish (birinchi marta)
alembic upgrade head

# Serverni ishga tushirish
uvicorn main:app --reload

# Swagger UI:
# http://localhost:8000/docs
```

### Docker bilan (tavsiya etiladi)

```bash
# Barcha servislarni birga ishga tushirish
# (PostgreSQL + Redis + API + Celery)
docker-compose up --build

# Orqa fonda ishlatish
docker-compose up -d

# To'xtatish
docker-compose down
```

---

## 👥 Rollar va ruxsatlar (RBAC)

> 💡 **RBAC nima?** — Role-Based Access Control. Kim nimaga kira olishini rol orqali boshqarish.

### Rollar

| Rol | Kimlar? | Nimalarga kirishi mumkin? |
|-----|---------|--------------------------|
| `student` | Talabalar | Faqat o'z ma'lumotlari |
| `teacher` | O'qituvchilar | O'z guruhi, davomat belgilash |
| `admin` | Dekanat xodimlari | Barcha talabalar, hisobotlar |
| `superadmin` | Tizim boshqaruvchisi | Hamma narsa |

### Ruxsatlar qanday ishlaydi?

```
Talaba /api/v1/grades/ ga so'rov yuboradi
              ↓
JWT token tekshiriladi (kim bu?)
              ↓
Rol tekshiriladi (student/teacher/admin?)
              ↓
ID tekshiriladi (o'z ma'lumotimi?)
              ↓
Ma'lumot qaytariladi yoki 403 xato
```

### Muhim qoidalar

- Talaba **faqat o'z** ma'lumotlarini ko'ra oladi
- Boshqa talabaning profili, bahosi, xabarlari — **403 Forbidden**
- Teacher faqat **o'z fanidagi** talabalarni ko'radi
- Admin hamma narsani ko'radi, lekin o'zgartira olmaydi
- Superadmin to'liq nazorat

---

## 🌐 API Endpointlar

> 🔒 — JWT token talab qilinadi
> 👑 — faqat admin/superadmin

Barcha endpointlar `/api/v1/` bilan boshlanadi.

Token headerga shunday qo'shiladi:
```
Authorization: Bearer <tokeningiz>
```

---

### 🔐 Autentifikatsiya `/api/v1/auth`

#### `POST /api/v1/auth/login` — Kirish

So'rov:
```json
{
  "student_id": "20210001",
  "password": "parolingiz"
}
```

Javob:
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

> ⚠️ **Rate limit:** 1 daqiqada 5 ta urinish. Ortiq bo'lsa `429 Too Many Requests`.

#### `POST /api/v1/auth/logout` 🔒

#### `POST /api/v1/auth/change-password` 🔒

```json
{
  "old_password": "eskiparol",
  "new_password": "Yangi@Parol123"
}
```

> Parol kuchi tekshiriladi: kamida 8 belgi, 1 ta katta harf, 1 ta raqam.

---

### 👤 Talaba profili `/api/v1/student`

| So'rov | URL | 🔒 | Tavsif |
|--------|-----|----|--------|
| `GET` | `/profile` | ✅ | O'z profilini ko'rish |
| `PUT` | `/profile` | ✅ | Telefon/email/manzil o'zgartirish |
| `GET` | `/gpa` | ✅ | GPA ball (keshlanadi) |
| `GET` | `/login-history` | ✅ | Oxirgi 20 ta kirish |
| `GET` | `/certificates` | ✅ | Sertifikatlar |

> 🔒 Boshqa talabaning profiliga kirmoqchi bo'lsangiz → `403 Forbidden`

---

### 📚 Dars jadvali `/api/v1/curriculum`

```
GET /api/v1/curriculum/schedule?semester=6&day=1   🔒
GET /api/v1/curriculum/subjects                    🔒
```

Jadval javobi (keshlanadi — Redis da 10 daqiqa saqlanadi):
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

### 📅 Davomat `/api/v1/attendance`

```
GET /api/v1/attendance/?page=1&limit=20   🔒   ← Sahifalash bilan
GET /api/v1/attendance/summary            🔒
```

> 💡 **Sahifalash nima?** — 500 ta yozuv birdaniga emas, 20 tadan bo'lib yuboriladi. Sayt sekinlashmaydi.

Summary javobi:
```json
[
  {
    "subject": "Matematika",
    "total": 30,
    "present": 26,
    "absent": 2,
    "late": 1,
    "excused": 1,
    "attendance_percent": 86.7
  }
]
```

---

### 📊 Baholar `/api/v1/grades`

```
GET /api/v1/grades/?semester=6   🔒
GET /api/v1/grades/gpa-summary   🔒
```

Baho javobi:
```json
{
  "subject": "Dasturlash asoslari",
  "midterm1": 28,
  "midterm2": 25,
  "final": 36,
  "total": 89,
  "letter_grade": "A-",
  "gpa_point": 3.7
}
```

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

### 📝 Imtihonlar `/api/v1/exams`

```
GET /api/v1/exams/?semester=6   🔒
```

---

### 💰 Moliya `/api/v1/financial`

```
GET /api/v1/financial/contracts      🔒
GET /api/v1/financial/scholarships   🔒   ← faqat grant talabalar
GET /api/v1/financial/summary        🔒
```

---

### ✉️ Xabarlar `/api/v1/messages`

```
GET   /api/v1/messages/?page=1&limit=20   🔒
POST  /api/v1/messages/                   🔒
PATCH /api/v1/messages/{id}/read          🔒
```

So'rov:
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

### 📢 E'lonlar `/api/v1/announcements`

```
GET /api/v1/announcements/   🔒
```

---

## 🛡️ Xavfsizlik

### 1. Rate Limiting (brute-force himoyasi)

```
/login endpointi:  1 daqiqada maksimal 5 urinish
                   Ortiq bo'lsa → 429 Too Many Requests
                   10 daqiqa bloklanadi
```

### 2. JWT Token

```
Token muddati: 24 soat
Algorithm:     HS256
Payload:       {"sub": "user_id", "role": "student", "exp": ...}
```

### 3. Parol xavfsizligi

- bcrypt bilan xeshlanadi (oddiy matn saqlanmaydi)
- Parol kuchi: kamida 8 belgi, 1 katta harf, 1 raqam
- Eski parol tekshirilmasdan o'zgartirib bo'lmaydi

### 4. Ma'lumot himoyasi

- Har bir so'rovda `current_user.id == requested_id` tekshiriladi
- Boshqa foydalanuvchi ma'lumotiga kirish → `403 Forbidden`
- Soft delete: ma'lumot o'chirilmaydi, `is_deleted=True` bo'ladi

### 5. Audit Log

Kim nima o'zgartirdi — hammasi yozib boriladi:
```json
{
  "user_id": "20210001",
  "action": "grade_updated",
  "old_value": {"total": 85},
  "new_value": {"total": 89},
  "timestamp": "2024-03-15T10:30:00",
  "ip_address": "192.168.1.1"
}
```

---

## ⚙️ Muhit o'zgaruvchilari

```env
# ═══════════════════════════
# DATABASE
# ═══════════════════════════
DATABASE_URL=postgresql://hemis_user:parol@localhost:5432/hemis_db

# ═══════════════════════════
# JWT
# ═══════════════════════════
SECRET_KEY=kamida-32-belgi-bu-yerda          # openssl rand -hex 32
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440             # 24 soat

# ═══════════════════════════
# REDIS
# ═══════════════════════════
REDIS_URL=redis://localhost:6379/0
CACHE_EXPIRE_SECONDS=600                     # 10 daqiqa

# ═══════════════════════════
# RATE LIMITING
# ═══════════════════════════
LOGIN_RATE_LIMIT=5/minute
API_RATE_LIMIT=100/minute

# ═══════════════════════════
# CELERY (orqa fon vazifalari)
# ═══════════════════════════
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/2

# ═══════════════════════════
# EMAIL
# ═══════════════════════════
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=sizning@email.com
SMTP_PASSWORD=emailparol

# ═══════════════════════════
# ILOVA
# ═══════════════════════════
APP_ENV=development          # development | production
DEBUG=True                   # Productionda False bo'lsin!
ALLOWED_ORIGINS=*            # Productionda aniq domain yozing
```

---

## 🐳 Docker

> 💡 **Docker nima?** — Loyihani "qutiga" solib, istalgan kompyuterda bir xil ishlatish. "Menda ishlaydi, senda ishlamaydi" muammosi yo'qoladi.

```bash
# Qurishni va ishga tushirishni birga bajarish
docker-compose up --build

# Orqa fonda ishlatish
docker-compose up -d

# Loglarni ko'rish
docker-compose logs -f api

# To'xtatish
docker-compose down

# Bazani ham o'chirish bilan to'xtatish
docker-compose down -v
```

`docker-compose.yml` ichida quyidagilar ishga tushadi:
- `api` — FastAPI server (port 8000)
- `db` — PostgreSQL (port 5432)
- `redis` — Redis (port 6379)
- `celery` — Orqa fon vazifalari
- `celery-beat` — Rejalashtirilgan vazifalar (har kuni, har soat...)

---

## 🧪 Testlar

> 💡 **Test nima uchun?** — Kodingiz to'g'ri ishlayaptimi? Har safar qo'lda tekshirmasdan, kod o'zi tekshirsin.

```bash
# Barcha testlar
pytest

# Batafsil chiqish
pytest -v

# Bitta fayl
pytest tests/test_auth.py

# Bitta test funksiya
pytest tests/test_auth.py::test_login_success

# Test qamrovi (coverage) — qancha kod test qilingan?
pytest --cov=app tests/ --cov-report=html

# Hisobot: htmlcov/index.html da ochiladi
```

### Test turlari

| Fayl | Nima tekshiriladi? |
|------|-------------------|
| `test_auth.py` | Login, logout, noto'g'ri parol, token muddati |
| `test_student.py` | Profil ko'rish, yangilash, boshqa profil bloklash |
| `test_grades.py` | Baholar, GPA hisob, letter grade |
| `test_attendance.py` | Davomat, foiz hisob, sahifalash |
| `test_financial.py` | Kontrakt, stipendiya, grant talabalar |
| `test_messages.py` | Yuborish, o'qish, o'ziga yubora olmaslik |
| `test_security.py` | Rate limit, brute-force, token tekshirish |
| `test_permissions.py` | Rol tekshirish, boshqa data bloklash |

---

## 🗃️ Migratsiya

> 💡 **Alembic nima?** — Baza jadvallari o'zgarganda, o'zgarishlarni faylda saqlaydi va avtomatik qo'llaydi. Git kabi — tarix saqlanadi.

```bash
# Model o'zgarganda yangi migratsiya yaratish
alembic revision --autogenerate -m "student ga email qoshildi"

# O'zgarishlarni bazaga qo'llash
alembic upgrade head

# Bir qadam orqaga (xato bo'lsa)
alembic downgrade -1

# Tarixni ko'rish
alembic history
```

---

## 🐞 Tez-tez uchraydigan xatolar

**`ModuleNotFoundError`** — kutubxona yo'q:
```bash
pip install -r requirements.txt
```

**`could not connect to server`** — PostgreSQL ishlamayapti:
```bash
sudo systemctl start postgresql    # Linux
brew services start postgresql     # Mac
```

**`Connection refused` (Redis)** — Redis ishlamayapti:
```bash
sudo systemctl start redis         # Linux
brew services start redis          # Mac
redis-cli ping                     # → PONG bo'lishi kerak
```

**`alembic: command not found`** — virtual muhit yoqilmagan:
```bash
source venv/bin/activate           # Linux/Mac
venv\Scripts\activate              # Windows
```

**`401 Unauthorized`** — token yo'q yoki muddati o'tgan. Qayta login qiling.

**`403 Forbidden`** — ruxsatingiz yo'q. Boshqa foydalanuvchi ma'lumotiga kirishga uringan bo'lishingiz mumkin.

**`422 Unprocessable Entity`** — yuborilgan ma'lumot formati noto'g'ri. `/docs` da namunani tekshiring.

**`429 Too Many Requests`** — rate limit ishladi. 1 daqiqa kuting.

---

## 📊 Log tizimi

Loyihada 3 xil log yoziladi:

```
logs/
├── app.log        ← Umumiy so'rovlar logi
├── error.log      ← Xatolar logi
└── security.log   ← Xavfsizlik logi (login urinishlar, bloklash)
```

Log ko'rish:
```bash
# Barcha loglar
tail -f logs/app.log

# Faqat xatolar
tail -f logs/error.log

# Xavfsizlik
tail -f logs/security.log
```

---

## 🔄 CI/CD (GitHub Actions)

Har safar kod `main` branchga push qilinganda avtomatik:

```
1. Testlar ishga tushadi
2. Testlar o'tsa → servega deploy qilinadi
3. Testlar o'tmasa → deploy to'xtatiladi, xabar yuboriladi
```

---

## 📄 Litsenziya

MIT — xohlaganingizcha foydalaning.

---

<div align="center">
  <sub>Birinchi loyiha qiyin tuyuladi — lekin siz uddalaysiz! 💪</sub>
</div>
