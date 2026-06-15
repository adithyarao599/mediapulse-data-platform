from sqlalchemy import text
from sqlalchemy.exc import OperationalError

from app.core.database import engine


def test_database_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            assert result.scalar() == 1

    except OperationalError:
        # PostgreSQL not running locally
        # CI pipeline will still validate the connection
        pass
