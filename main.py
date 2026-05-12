from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router
from app.core.config import settings

# ✅ Shu qatorlarni qo'shing

app = FastAPI(
    title="HEMIS Backend API",
    description="O'zbekiston universitetlarining HEMIS Student tizimi uchun backend API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS sozlamasi
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Barcha routerlarni ulash
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {
        "message": "HEMIS Backend API ishlayapti ✅",
        "docs": "/docs",
        "version": "1.0.0",
    }


@app.get("/health")
async def health_check():
    return {"status": "ok"}
