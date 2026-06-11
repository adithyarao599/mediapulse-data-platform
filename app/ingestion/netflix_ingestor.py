import pandas as pd

from app.ingestion.base_ingestor import BaseIngestor


class NetflixIngestor(BaseIngestor):

    def __init__(self, file_path):

        self.file_path = file_path

    def extract(self):

        return pd.read_csv(self.file_path)

    def validate(self, df):

        return not df.empty

    def load(self, df):

        df.to_csv("data/raw/netflix/" "netflix_raw.csv", index=False)
