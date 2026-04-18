# 🎓 HEMIS Backend API

Bu loyiha O'zbekiston universitetlarining **HEMIS Student tizimi** uchun yozilgan backend API.  
Talabalar o'z profili, baholar, davomat, jadval va moliyaviy ma'lumotlarini ko'ra oladi.

> 💡 **Backend nima?** — Bu foydalanuvchi ko'rmaydigan "orqa" qism. Frontend (telefon yoki veb-sayt) shu backend bilan gaplashadi va ma'lumot oladi.

---

## 🛠️ Qanday texnologiyalar ishlatilgan?

| Texnologiya | Bu nima? |
|---|---|
| **Python** | Dasturlash tili |
| **FastAPI** | Python uchun web framework — API yaratish uchun |
| **PostgreSQL** | Ma'lumotlar bazasi (Excel kabi, lekin kuchliroq) |
| **SQLAlchemy** | Python orqali bazaga murojaat qilish uchun (SQL yozmasdan) |
| **Alembic** | Baza strukturasini o'zgartirish uchun (migratsiya) |
| **Pydantic** | Kelayotgan ma'lumotlarni tekshirish uchun |
| **JWT** | Foydalanuvchi kimligini tekshirish (token orqali) |
| **Uvicorn** | Serverni ishga tushiruvchi dastur |

---

## 📁 Loyiha strukturasi

> 💡 Har bir papka va fayl nima uchun ekanini tushuntirdik.

```
hemis_backend/               ← Loyihaning asosiy papkasi
│
├── main.py                  ← Ilova shu yerdan boshlanadi (entry point)
├── requirements.txt         ← O'rnatilishi kerak bo'lgan barcha kutubxonalar
├── .env                     ← Maxfiy sozlamalar (parol, kalit) — GitHubga chiqarma!
├── .env.example             ← .env uchun namuna (bu faylni GitHubga qo'ysa bo'ladi)
├── alembic.ini              ← Alembic (migratsiya) uchun sozlama
├── README.md                ← Siz o'qiyotgan shu fayl 😄
│
├── alembic/                 ← Baza o'zgarishlari tarixi saqlanadigan joy
│   └── versions/            ← Har bir o'zgarish alohida fayl bo'ladi
│
├── tests/                   ← Kodimiz to'g'ri ishlayaptimi? Shu yerda tekshiramiz
│   ├── test_auth.py
│   └── test_student.py
│
└── app/                     ← Asosiy kod shu papkada
    │
    ├── core/                ← Ilova "yuragi" — eng asosiy sozlamalar
    │   ├── config.py        ← .env fayldan sozlamalarni o'qiydi
    │   ├── security.py      ← Parolni xeshlash, JWT token yaratish
    │   └── dependencies.py  ← "Hozir kim login qilgan?" — shu yerda aniqlanadi
    │
    ├── db/                  ← Database bilan bog'liq hamma narsa
    │   ├── base.py          ← Barcha modellar meros oladigan asosiy class
    │   ├── session.py       ← Bazaga ulanish va get_db() funksiyasi
    │   └── init_db.py       ← Boshlang'ich (test) ma'lumotlar qo'shish
    │
    ├── models/              ← Baza jadvallari (har bir fayl = bir jadval)
    │   ├── __init__.py
    │   ├── faculty.py       ← Fakultetlar jadvali
    │   ├── department.py    ← Kafedralar jadvali
    │   ├── group.py         ← Guruhlar jadvali
    │   ├── teacher.py       ← O'qituvchilar jadvali
    │   ├── student.py       ← Talabalar jadvali ⭐ (eng asosiy)
    │   ├── subject.py       ← Fanlar jadvali
    │   ├── schedule.py      ← Dars jadvali
    │   ├── attendance.py    ← Davomat jadvali
    │   ├── grade.py         ← Baholar jadvali
    │   ├── exam.py          ← Imtihonlar jadvali
    │   ├── financial.py     ← Kontrakt va stipendiya
    │   ├── message.py       ← Xabarlar jadvali
    │   ├── announcement.py  ← E'lonlar jadvali
    │   ├── login_history.py ← Kim, qachon, qayerdan kirgan
    │   └── certificate.py   ← Fan sertifikatlari
    │
    ├── schemas/             ← API dan kelgan/ketgan ma'lumot formati
    │   │
    │   │  ⚠️ model ≠ schema!
    │   │     model  = bazadagi jadval ko'rinishi
    │   │     schema = API orqali keladigan/ketadigan ma'lumot ko'rinishi
    │   │
    │   ├── auth.py          ← Login so'rovi va javob formati
    │   ├── student.py       ← Profil ma'lumotlari formati
    │   ├── curriculum.py    ← Jadval va fanlar formati
    │   ├── attendance.py    ← Davomat formati
    │   ├── grade.py         ← Baho formati
    │   ├── exam.py          ← Imtihon formati
    │   ├── financial.py     ← Kontrakt va stipendiya formati
    │   ├── message.py       ← Xabar formati
    │   └── announcement.py  ← E'lon formati
    │
    ├── crud/                ← CRUD = Create, Read, Update, Delete
    │   │
    │   │  💡 Nima uchun alohida papka?
    │   │     Router  → faqat HTTP so'rovlarni qabul qiladi
    │   │     CRUD    → faqat baza bilan ishlaydi
    │   │     Shunday bo'lsa kod toza va tushunarli bo'ladi
    │   │
    │   ├── auth.py          ← Login, logout, parol o'zgartirish logikasi
    │   ├── student.py       ← Profil olish, yangilash logikasi
    │   ├── attendance.py    ← Davomat ma'lumotlari logikasi
    │   ├── grade.py         ← Baho va GPA logikasi
    │   ├── exam.py          ← Imtihon logikasi
    │   ├── financial.py     ← Kontrakt va stipendiya logikasi
    │   └── message.py       ← Xabar yuborish/olish logikasi
    │
    ├── api/                 ← HTTP so'rovlarni qabul qiluvchi qatlam
    │   └── routes/          ← Har bir fayl = bir guruh endpoint
    │       ├── auth.py      ← /api/auth/...
    │       ├── student.py   ← /api/student/...
    │       ├── curriculum.py← /api/curriculum/...
    │       ├── attendance.py← /api/attendance/...
    │       ├── grades.py    ← /api/grades/...
    │       ├── exams.py     ← /api/exams/...
    │       ├── financial.py ← /api/financial/...
    │       ├── messages.py  ← /api/messages/...
    │       └── announcements.py ← /api/announcements/...
    │
    └── utils/               ← Qayta ishlatiluvchi yordamchi funksiyalar
        ├── enums.py         ← Barcha ro'yxatlar: status, tur, shakl...
        ├── pagination.py    ← Sahifalash (1-20, 21-40...)
        └── grade_utils.py   ← 87 ball → "A-" va 3.7 GPA hisobi
```

---

## 💻 O'rnatish (qadam-baqadam)

> 🐣 Hech narsa o'rnatilmagan bo'lsa ham, quyidagi tartibda bajaring.

### 1-qadam: Repozitoriyani yuklab oling

```bash
git clone https://github.com/username/hemis-backend.git
cd hemis-backend
```

### 2-qadam: Virtual muhit yarating

> 💡 **Virtual muhit nima?** — Har bir loyiha uchun alohida "xona". Bir loyihaning kutubxonalari boshqasiga aralashmaydi.

```bash
# Virtual muhit yaratish
python -m venv venv

# Linux yoki Mac bo'lsa:
source venv/bin/activate

# Windows bo'lsa:
venv\Scripts\activate

# Muvaffaqiyatli bo'lsa, terminalda (venv) ko'rinadi:
# (venv) C:\Users\siz>
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
# Keyin .env ni matn muharririda oching va to'ldiring
```

`.env` fayli ichida:

```env
# Ma'lumotlar bazasi manzili
DATABASE_URL=postgresql://hemis_user:parol123@localhost:5432/hemis_db

# JWT uchun maxfiy kalit (kamida 32 ta belgi, hech kimga bermang)
SECRET_KEY=bu-yerga-uzun-va-murakkab-matn-yozing-123abc

# Token algoritmi — o'zgartirmang
ALGORITHM=HS256

# Token necha daqiqa amal qiladi (1440 = 24 soat)
ACCESS_TOKEN_EXPIRE_MINUTES=1440
```

> 🔑 Xavfsiz kalit yasash uchun:
> ```bash
> openssl rand -hex 32
> ```

---

## ▶️ Ishga tushirish

```bash
# Birinchi marta: jadvallarni bazada yaratish
alembic upgrade head

# Serverni ishga tushirish
uvicorn main:app --reload

# Server manzili:
# http://localhost:8000
```

### Swagger UI — API ni brauzerda sinab ko'ring

```
http://localhost:8000/docs
```

> 💡 Bu sahifada barcha endpointlarni ko'rib, to'g'ridan-to'g'ri sinab ko'rish mumkin. Postman o'rnatmasangiz ham bo'ladi!

---

## 🌐 API Endpointlar

> 🔒 — bu belgili endpointlar uchun token kerak (avval `/login` dan oling)

Token headerga shunday qo'shiladi:
```
Authorization: Bearer <tokeningiz>
```

---

### 🔐 Kirish `/api/auth`

#### `POST /api/auth/login` — Tizimga kirish

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
  "group": "CS-21-01",
  "semester": 6
}
```

> Olgan `access_token` ni saqlab qoling — keyingi barcha so'rovlarda kerak bo'ladi.

#### `POST /api/auth/logout` 🔒 — Chiqish

#### `POST /api/auth/change-password` 🔒 — Parol o'zgartirish

```json
{
  "old_password": "eskiparol",
  "new_password": "yangiparol"
}
```

---

### 👤 Talaba profili `/api/student`

| So'rov | URL | Nima qiladi? |
|--------|-----|-------------|
| `GET` | `/api/student/profile` | 🔒 Profilni ko'rish |
| `PUT` | `/api/student/profile` | 🔒 Telefon/email/manzil o'zgartirish |
| `GET` | `/api/student/gpa` | 🔒 GPA ballini ko'rish |
| `GET` | `/api/student/login-history` | 🔒 Oxirgi 20 ta kirish |
| `GET` | `/api/student/certificates` | 🔒 Sertifikatlar |

---

### 📚 Dars jadvali `/api/curriculum`

```
GET /api/curriculum/schedule?semester=6&day=1   🔒
```

Javob:
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

```
GET /api/curriculum/subjects   🔒   ← Semestr fanlar ro'yxati
```

---

### 📅 Davomat `/api/attendance`

```
GET /api/attendance/           🔒   ← Sanalar bo'yicha davomat
GET /api/attendance/summary    🔒   ← Fanlar bo'yicha foiz
```

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

### 📊 Baholar `/api/grades`

```
GET /api/grades/?semester=6    🔒   ← Baholar ro'yxati
GET /api/grades/gpa-summary    🔒   ← Barcha semestrlar GPA
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

**Letter grade qanday hisoblanadi?**

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

### 📝 Imtihonlar `/api/exams`

```
GET /api/exams/?semester=6     🔒
```

Har bir imtihon uchun sana, xona va talabaning natijasi qaytadi.

---

### 💰 Moliya `/api/financial`

```
GET /api/financial/contracts      🔒   ← Kontrakt summasi va qoldig'i
GET /api/financial/scholarships   🔒   ← Faqat grant talabalarga ko'rinadi
GET /api/financial/summary        🔒   ← Umumiy to'lov holati
```

---

### ✉️ Xabarlar `/api/messages`

```
GET   /api/messages/           🔒   ← Barcha xabarlar
POST  /api/messages/           🔒   ← Xabar yuborish
PATCH /api/messages/{id}/read  🔒   ← O'qilgan deb belgilash
```

Xabar yuborish:
```json
{
  "receiver_student_id": "20210002",
  "subject": "Laboratoriya haqida",
  "body": "Ertangi labga kelasizmi?"
}
```

> ⚠️ O'zingizga xabar yubormoqchi bo'lsangiz — `400 xato` qaytadi.

---

### 📢 E'lonlar `/api/announcements`

```
GET /api/announcements/        🔒   ← Muddati o'tmagan faol e'lonlar
```

---

## 🔑 JWT Token qanday ishlaydi?

```
1. Talaba  →  student_id + parol yuboradi
                      ↓
2. Server  →  parolni tekshiradi (bcrypt)
                      ↓
3. Server  →  JWT token yaratadi va qaytaradi
                      ↓
4. Talaba  →  keyingi har bir so'rovda tokenni yuboradi
                      ↓
5. Server  →  tokenni tekshiradi, "bu kim?" ni biladi
```

> Token 24 soat amal qiladi. Muddati o'tsa — qayta login qilish kerak.

---

## 🗃️ Migratsiya buyruqlari

> 💡 Modellarda o'zgartirish qilganda (yangi ustun, yangi jadval) — Alembic bazani yangilaydi.

```bash
# Model o'zgarganda yangi migratsiya fayli yaratish
alembic revision --autogenerate -m "nima o'zgardi"

# O'zgarishlarni bazaga qo'llash
alembic upgrade head

# Bir qadam orqaga qaytish (xato bo'lsa)
alembic downgrade -1

# O'zgarishlar tarixini ko'rish
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
sudo service postgresql start   # Linux
brew services start postgresql  # Mac
```

**`alembic: command not found`** — virtual muhit yoqilmagan:
```bash
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

**`401 Unauthorized`** — token yo'q yoki muddati o'tgan. Qayta login qiling.

**`422 Unprocessable Entity`** — yuborilgan ma'lumot formati noto'g'ri. `/docs` da namunani tekshiring.

---

## 📄 Litsenziya

MIT — xohlaganingizcha foydalaning.

---

<div align="center">
  <sub>Birinchi loyiha qiyin tuyuladi — lekin siz uddalaysiz! 💪</sub>
</div>
