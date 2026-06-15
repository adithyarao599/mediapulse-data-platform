from sqlalchemy import create_engine

from app.config.settings import settings

DATABASE_URL = (
    f"postgresql://"
    f"{settings.POSTGRES_USER}:"
    f"{settings.POSTGRES_PASSWORD}@"
    f"{settings.POSTGRES_HOST}:"
    f"{settings.POSTGRES_PORT}/"
    f"{settings.POSTGRES_DB}"
)

engine = create_engine(DATABASE_URL)

if __name__ == "__main__":
    with engine.connect() as connection:
        print("Database Connected Successfully")
