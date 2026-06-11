from app.ingestion.checksum import generate_checksum


def test_checksum():

    checksum = generate_checksum("datasets/spotify.csv")

    assert checksum is not None
