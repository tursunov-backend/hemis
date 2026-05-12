from fastapi import APIRouter

from app.api.v1.routers.announcements import router as announcements_router

api_router = APIRouter()

api_router.include_router(announcements_router)
