from sqlalchemy import URL, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings


url = URL.create(
    drivername="postgresql+psycopg2",
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    username=settings.DB_USER,
    password=settings.DB_PASS,
    database=settings.DB_NAME,
    secret_key=settings.SECRET_KEY,
    algorithm=settings.ALGORITHM,
    acces_token_expire_minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
)
engine = create_engine(url)
SessionLocal = sessionmaker(engine)


class Base(DeclarativeBase):
    pass
