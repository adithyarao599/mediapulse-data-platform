import pandas as pd

from app.silver.standardizer import Standardizer


def test_column_standardization():

    dataframe = pd.DataFrame({"Artist Name": ["Taylor"]})

    result = Standardizer.standardize_columns(dataframe)

    assert "artist_name" in result.columns
