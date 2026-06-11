from app.ingestion.spotify_ingestor import SpotifyIngestor


def run_spotify_ingestion():

    ingestor = SpotifyIngestor("datasets/spotify.csv")

    df = ingestor.extract()

    ingestor.validate(df)

    ingestor.load(df)


if __name__ == "__main__":

    run_spotify_ingestion()
