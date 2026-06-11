from app.core.session import SessionLocal
from app.models.ingestion_metadata import IngestionMetadata


def record_ingestion(source_name, file_name, record_count, status):

    db = SessionLocal()

    try:

        metadata = IngestionMetadata(
            source_name=source_name,
            file_name=file_name,
            record_count=record_count,
            status=status,
        )

        db.add(metadata)

        db.commit()

    finally:

        db.close()
