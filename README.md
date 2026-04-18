# 🎓 HEMIS Backend API

O'zbekiston universitetlarining **HEMIS Student tizimi** uchun backend API.  
Talabalar o'z profili, baholar, davomat, jadval va moliyaviy ma'lumotlarini ko'ra oladi.


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
psql -U postgres

CREATE DATABASE hemis_db;
CREATE USER hemis_user WITH PASSWORD 'parol123';
GRANT ALL PRIVILEGES ON DATABASE hemis_db TO hemis_user;
\q
```

### 5-qadam: .env faylini sozlang

```bash
cp .env.example .env
# Keyin .env faylini oching va to'ldiring
```

`.env` ichida:

```env
DATABASE_URL=postgresql://hemis_user:parol123@localhost:5432/hemis_db

SECRET_KEY=bu-yerga-kamida-32-belgi-yozing-hech-kimga-bermang
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
```

> 🔑 Xavfsiz kalit yasash:
> ```bash
> openssl rand -hex 32
> ```

---

## ▶️ Ishga tushirish

```bash
# 1. Jadvallarni bazada yaratish (faqat birinchi marta)
alembic upgrade head

# 2. Serverni ishga tushirish
uvicorn main:app --reload

# Server ishlaydi:
# http://localhost:8000
```

### Swagger UI — API ni brauzerda sinab ko'ring

```
http://localhost:8000/docs
```

> 💡 Bu sahifada barcha endpointlarni ko'rib, to'g'ridan-to'g'ri sinab ko'rsa bo'ladi. Postman kerak emas!

---

## 👥 Rollar tizimi

> 💡 Har bir foydalanuvchi ma'lum bir "rol" ga ega. Rol uning nimalarga kira olishini belgilaydi.

| Rol | Kimlar? | Nimalarga kirishi mumkin? |
|-----|---------|--------------------------|
| `student` | Talabalar | Faqat **o'z** ma'lumotlari |
| `teacher` | O'qituvchilar | O'z fani va guruhi |
| `admin` | Dekanat | Barcha talabalar ma'lumotlari |
| `superadmin` | Tizim boshqaruvchisi | Hamma narsa |

### Muhim qoidalar

```
✅ Talaba o'z profilini ko'ra oladi
✅ Talaba o'z baholarini ko'ra oladi

❌ Talaba boshqa talabaning profilini ko'ra olmaydi  → 403 Forbidden
❌ Talaba baholarni o'zgartira olmaydi               → 403 Forbidden
❌ Teacher boshqa guruh ma'lumotlarini ko'ra olmaydi → 403 Forbidden
```

---

## 🌐 API Endpointlar

> 🔒 — bu belgili endpointlar uchun token kerak (avval `/login` dan oling)

Token headerga shunday qo'shiladi:
```
Authorization: Bearer <tokeningiz>
```

---

### 🔐 Kirish — `/api/v1/auth`

#### `POST /api/v1/auth/login` — Tizimga kirish

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

> Bu `access_token` ni saqlab qoling — keyingi barcha so'rovlarda kerak!

#### `POST /api/v1/auth/logout` 🔒 — Chiqish

#### `POST /api/v1/auth/change-password` 🔒 — Parol o'zgartirish

```json
{
  "old_password": "eskiparol",
  "new_password": "YangiParol123"
}
```

> Parol kuchi tekshiriladi: kamida 8 belgi, 1 katta harf, 1 raqam

---

### 👤 Talaba profili — `/api/v1/student`

| So'rov | URL | Tavsif |
|--------|-----|--------|
| `GET` | `/api/v1/student/profile` | 🔒 O'z profilini ko'rish |
| `PUT` | `/api/v1/student/profile` | 🔒 Telefon/email/manzil o'zgartirish |
| `GET` | `/api/v1/student/gpa` | 🔒 GPA ballini ko'rish |
| `GET` | `/api/v1/student/login-history` | 🔒 Oxirgi 20 ta kirish |
| `GET` | `/api/v1/student/certificates` | 🔒 Sertifikatlar |

---

### 📚 Dars jadvali — `/api/v1/curriculum`

```
GET /api/v1/curriculum/schedule?semester=6&day=1   🔒
GET /api/v1/curriculum/subjects                    🔒
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

---

### 📅 Davomat — `/api/v1/attendance`

```
GET /api/v1/attendance/?page=1&limit=20   🔒
GET /api/v1/attendance/summary            🔒
```

> 💡 **`page` va `limit` nima?** — 500 ta yozuv birdaniga emas, 20 tadan bo'lib yuboriladi. Sayt sekinlashmaydi.

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

### 📊 Baholar — `/api/v1/grades`

```
GET /api/v1/grades/?semester=6   🔒
GET /api/v1/grades/gpa-summary   🔒
```

Javob:
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

### 📝 Imtihonlar — `/api/v1/exams`

```
GET /api/v1/exams/?semester=6   🔒
```

---

### 💰 Moliya — `/api/v1/financial`

```
GET /api/v1/financial/contracts      🔒   ← Kontrakt summasi va qoldig'i
GET /api/v1/financial/scholarships   🔒   ← Faqat grant talabalarga
GET /api/v1/financial/summary        🔒   ← Umumiy to'lov holati
```

---

### ✉️ Xabarlar — `/api/v1/messages`

```
GET   /api/v1/messages/?page=1&limit=20   🔒   ← Barcha xabarlar
POST  /api/v1/messages/                   🔒   ← Xabar yuborish
PATCH /api/v1/messages/{id}/read          🔒   ← O'qilgan deb belgilash
```

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

```
GET /api/v1/announcements/   🔒   ← Muddati o'tmagan faol e'lonlar
```

---

## 🔑 JWT Token qanday ishlaydi?

```
1. Talaba  →  student_id + parol yuboradi
                    ↓
2. Server  →  parolni tekshiradi
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
- Parollar bcrypt bilan xeshlanadi — bazada oddiy matn saqlanmaydi
- Kimdir bazani o'g'irlasa ham parollarni bila olmaydi

### Ma'lumot himoyasi
- Har bir so'rovda "bu o'z ma'lumotimi?" tekshiriladi
- Boshqa talabaning ma'lumotiga urinish → `403 Forbidden`

### Soft delete
- Ma'lumot o'chirilganda bazadan butunlay ketmaydi
- `is_deleted = True` bo'ladi — kerak bo'lsa qaytarib olsa bo'ladi

### Audit log
- Kim nima o'zgartirdi — hammasi yozib boriladi
```
[2024-03-15 10:30] student:20210001 → o'z profilini yangiladi
[2024-03-15 11:00] admin:001        → 20210002 bahosini o'zgartirdi
```

---

## ⚙️ Muhit o'zgaruvchilari (`.env`)

```env
# Database ulanish manzili
DATABASE_URL=postgresql://hemis_user:parol123@localhost:5432/hemis_db

# JWT maxfiy kalit (kamida 32 belgi, hech kimga bermang!)
SECRET_KEY=bu-yerga-uzun-matn-yozing

# Token algoritmi — o'zgartirmang
ALGORITHM=HS256

# Token necha daqiqa amal qiladi (1440 = 24 soat)
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# development yoki production
APP_ENV=development
```

---

## 🗃️ Migratsiya (Alembic)

> 💡 Model o'zgarganda (yangi ustun, yangi jadval) Alembic bazani avtomatik yangilaydi.

```bash
# Barcha jadvallarni yaratish (birinchi marta)
alembic upgrade head

# Model o'zgarganda yangi migratsiya fayli yaratish
alembic revision --autogenerate -m "nima o'zgardi"

# O'zgarishlarni bazaga qo'llash
alembic upgrade head

# Xato bo'lsa — bir qadam orqaga
alembic downgrade -1
```

---

## 🐞 Tez-tez uchraydigan xatolar

**`ModuleNotFoundError`** — kutubxona o'rnatilmagan:
```bash
pip install -r requirements.txt
```

**`could not connect to server`** — PostgreSQL ishlamayapti:
```bash
# Linux
sudo systemctl start postgresql

# Mac
brew services start postgresql
```

**`alembic: command not found`** — virtual muhit yoqilmagan:
```bash
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

**`401 Unauthorized`** — token yo'q yoki muddati o'tgan. Qayta login qiling.

**`403 Forbidden`** — bu ma'lumotga ruxsatingiz yo'q.

**`422 Unprocessable Entity`** — yuborilgan ma'lumot formati noto'g'ri. `/docs` da namunani tekshiring.

---

## 📄 Litsenziya

MIT — xohlaganingizcha foydalaning.

---

<div align="center">
  <sub>Birinchi loyiha qiyin tuyuladi — lekin siz uddalaysiz! 💪</sub>
</div>
