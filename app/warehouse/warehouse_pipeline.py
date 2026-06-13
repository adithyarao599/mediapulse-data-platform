from app.warehouse.bulk_loader import BulkLoader
from app.warehouse.dimension_loader import DimensionLoader
from app.warehouse.fact_loader import FactLoader
from app.warehouse.referential_integrity import ReferentialIntegrity
from app.warehouse.warehouse_quality import WarehouseQuality


class WarehousePipeline:

    def run(self, dimension_df, fact_df, dimension_model, fact_model):

        DimensionLoader().load(dimension_df, dimension_model)

        WarehouseQuality.null_check()

        ReferentialIntegrity.validate()

        BulkLoader.load()

        FactLoader().load(fact_df, fact_model)
