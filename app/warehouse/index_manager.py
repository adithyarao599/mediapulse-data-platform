from sqlalchemy import Index


def create_indexes():

    Index("idx_fact_date", "date_key")

    Index("idx_fact_artist", "artist_key")

    Index("idx_fact_content", "content_key")
