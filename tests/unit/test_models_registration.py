import app.models  # noqa: F401 - importing the package registers every model
from app.core.database import Base

EXPECTED_TABLES = {
    "dim_artist",
    "dim_content",
    "dim_country",
    "dim_date",
    "dim_genre",
    "dim_platform",
    "fact_content_performance",
    "gold_metadata",
    "ingestion_metadata",
    "ml_metadata",
    "silver_metadata",
    "warehouse_load_metadata",
}


def test_all_models_are_registered_on_base_metadata():
    # app/warehouse/create_tables.py used to hand-import 8 of the 12 model
    # modules and silently missed the other 4 (gold_metadata, ml_metadata,
    # silver_metadata, warehouse_load_metadata never got created). This
    # test fails loudly the same way if a future model is ever added
    # without being wired into app/models/__init__.py.
    # Table keys in Base.metadata.tables are schema-qualified
    # ("streaming_dw.dim_artist"), so compare against Table.name instead.
    registered_tables = {table.name for table in Base.metadata.tables.values()}
    assert registered_tables == EXPECTED_TABLES


def test_every_table_is_namespaced_to_streaming_dw_schema():
    for table in Base.metadata.tables.values():
        assert table.schema == "streaming_dw"
