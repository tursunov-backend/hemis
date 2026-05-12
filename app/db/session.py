from .base import url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(url)
SessionLocal = sessionmaker(engine)