from app.ingestion.ingestion_config import INGESTION_CONFIG
from app.ingestion.spotify_ingestor import SpotifyIngestor


class IngestionEngine:

    def run(self, source_name):

        config = INGESTION_CONFIG[source_name]

        ingestor = SpotifyIngestor(config["source_file"])

        df = ingestor.extract()

        ingestor.validate(df)

        ingestor.load(df)
