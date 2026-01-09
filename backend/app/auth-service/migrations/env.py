import asyncio

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context
from core.database import Base
from core.config import settings
from models.user import User


# Alembic Config object
config = context.config

# Inject DB URL dynamically
config.set_main_option(
    "sqlalchemy.url",
    settings.DATABASE_URL,
)

# Target metadata for autogenerate
target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in offline mode (no DB connection)."""
    context.configure(
        url=settings.DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in online mode using async engine."""

    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    # IMPORTANT: this must be a NORMAL function (not async)
    def do_run_migrations(connection: Connection):
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

    async def run():
        async with connectable.connect() as connection:
            await connection.run_sync(do_run_migrations)

        await connectable.dispose()

    asyncio.run(run())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
