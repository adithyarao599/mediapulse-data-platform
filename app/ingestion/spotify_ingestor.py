import pandas as pd

from app.ingestion.base_ingestor import BaseIngestor
from app.ingestion.metadata_service import record_ingestion
from app.utils.logger import get_logger

logger = get_logger()


class SpotifyIngestor(BaseIngestor):

    def __init__(self, file_path):

        self.file_path = file_path

    def extract(self):

        logger.info("Reading Spotify dataset")

        return pd.read_csv(self.file_path)

    def validate(self, df):

        if df.empty:

            raise ValueError("Spotify file empty")

        return True

    def load(self, df):

        output_path = "data/raw/spotify/" "spotify_raw.csv"

        try:

            df.to_csv(output_path, index=False)

            record_ingestion(
                source_name="spotify",
                file_name="spotify_raw.csv",
                record_count=len(df),
                status="SUCCESS",
            )

            logger.info("Spotify Bronze Load Complete")

        except Exception:

            record_ingestion(
                source_name="spotify",
                file_name="spotify_raw.csv",
                record_count=0,
                status="FAILED",
            )

            raise
