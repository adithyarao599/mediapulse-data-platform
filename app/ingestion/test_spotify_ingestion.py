from app.ingestion.spotify_ingestor import SpotifyIngestor


def test_spotify_ingestor():

    ingestor = SpotifyIngestor("datasets/spotify.csv")

    df = ingestor.extract()

    assert len(df) > 0
