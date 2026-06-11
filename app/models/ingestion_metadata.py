from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.core.database import Base


class IngestionMetadata(Base):

    __tablename__ = "ingestion_metadata"

    ingestion_id = Column(Integer, primary_key=True, autoincrement=True)

    source_name = Column(String(100), nullable=False)

    file_name = Column(String(255), nullable=False)

    record_count = Column(Integer)

    ingestion_timestamp = Column(DateTime, default=datetime.utcnow)

    status = Column(String(50))

    checksum = Column(String(255))

    file_version = Column(Integer)
