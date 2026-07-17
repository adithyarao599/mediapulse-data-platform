"""
Importing this package registers every ORM model on Base.metadata.

SQLAlchemy only knows about a table once its model class has been
imported somewhere in the process - Base.metadata itself stays empty
otherwise. Centralizing the imports here (instead of requiring every
caller, like create_tables.py or Alembic's env.py, to import each model
file individually) means "give me the full warehouse schema" is always
just `import app.models`.
"""

from app.models.dim_artist import DimArtist
from app.models.dim_content import DimContent
from app.models.dim_country import DimCountry
from app.models.dim_date import DimDate
from app.models.dim_genre import DimGenre
from app.models.dim_platform import DimPlatform
from app.models.fact_content_performance import FactContentPerformance
from app.models.gold_metadata import GoldMetadata
from app.models.ingestion_metadata import IngestionMetadata
from app.models.ml_metadata import MLMetadata
from app.models.silver_metadata import SilverMetadata
from app.models.warehouse_load_metadata import WarehouseLoadMetadata

__all__ = [
    "DimArtist",
    "DimContent",
    "DimCountry",
    "DimDate",
    "DimGenre",
    "DimPlatform",
    "FactContentPerformance",
    "GoldMetadata",
    "IngestionMetadata",
    "MLMetadata",
    "SilverMetadata",
    "WarehouseLoadMetadata",
]
