import app.models  # noqa: F401 - registers every model on Base.metadata
from app.core.database import Base, engine


def create_tables():
    """
    Bootstrap convenience for a brand-new, empty database (e.g. local dev,
    CI). Creates every table currently defined on Base.metadata in one
    shot with no change history.

    This is NOT how schema changes should reach a database that already
    has data or has been deployed anywhere: create_all() cannot alter an
    existing table, drop a column, or roll back. For that, use the
    Alembic migrations in migrations/ (see docs/DATABASE_MIGRATIONS.md):
        alembic upgrade head
    """

    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":

    create_tables()

    print("Warehouse tables created.")
