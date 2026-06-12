from app.silver.deduplicator import Deduplicator
from app.silver.null_handler import NullHandler
from app.silver.standardizer import Standardizer


class SilverEngine:

    def process(self, dataframe):

        dataframe = Standardizer.standardize_columns(dataframe)

        dataframe = NullHandler.fill_string_nulls(dataframe)

        dataframe = NullHandler.fill_numeric_nulls(dataframe)

        dataframe = Deduplicator.remove_duplicates(dataframe)

        return dataframe
