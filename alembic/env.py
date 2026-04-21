import sys
import os

# 🔥 app ni tanitish
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logging.config import fileConfig
from sqlalchemy import create_engine
from alembic import context

from app.core.config import settings
from app.db.base import Base

# 🔥 barcha modellarni import qilish
from app.models import (
    faculty,
    department,
    group,
    teacher,
    student,
    subject,
    schedule,
    attendance,
    grade,
    exam,
    financial,
    message,
    announcement,
    audit_log,
    login_history,
    certificate,
)

config = context.config

# 🔥 .env dan DB olish
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 🔥 metadata
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    context.configure(
        url=settings.DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = create_engine(settings.DATABASE_URL)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
