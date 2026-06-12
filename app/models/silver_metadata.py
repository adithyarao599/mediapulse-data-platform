from sqlalchemy import Column, Float, Integer, String

from app.core.database import Base


class SilverMetadata(Base):

    __tablename__ = "silver_metadata"

    process_id = Column(Integer, primary_key=True)

    dataset_name = Column(String(100))

    row_count = Column(Integer)

    quality_score = Column(Float)
