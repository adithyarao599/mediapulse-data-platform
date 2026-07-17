from logging.config import fileConfig

import sqlalchemy as sa
from alembic import context
from sqlalchemy import engine_from_config, pool

import app.models  # noqa: F401 - registers every model on Base.metadata
from app.config.settings import settings
from app.core.database import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Build the connection URL from the app's own Settings instead of a second,
# hardcoded copy in alembic.ini - one source of truth for how we connect to
# Postgres, whether that's this script or app/core/database.py.
config.set_main_option(
    "sqlalchemy.url",
    f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
    f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}",
)

# Point Alembic at our ORM models so `alembic revision --autogenerate` can
# diff the live database against what the code says the schema should be.
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        # Our tables live in the streaming_dw schema, not Postgres's
        # default "public" schema (see app/core/database.py). Without
        # these two options Alembic only looks at "public" and would
        # think every one of our tables needs to be created from scratch
        # on every run.
        include_schemas=True,
        version_table_schema=target_metadata.schema,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        # Alembic's own bookkeeping table (alembic_version) is configured
        # to live inside streaming_dw too (version_table_schema below), so
        # it can't be created until that schema exists - but on a brand
        # new database, no migration has run yet to create it. Ensure the
        # schema exists before Alembic tries to write to it; every actual
        # table still comes from the versioned migrations, this line only
        # unblocks Alembic's internal state tracking.
        connection.execute(sa.text("CREATE SCHEMA IF NOT EXISTS streaming_dw"))

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_schemas=True,
            version_table_schema=target_metadata.schema,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
