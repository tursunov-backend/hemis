from sqlalchemy import URL
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings


url = URL.create(
    drivername="postgresql+psycopg2",
    username=settings.DB_USER,
    password=settings.DB_PASS,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME,
)


class Base(DeclarativeBase):
    pass
