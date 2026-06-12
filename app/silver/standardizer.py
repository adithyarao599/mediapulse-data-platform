import pandas as pd


class Standardizer:

    @staticmethod
    def standardize_columns(df):

        df.columns = [column.strip().lower().replace(" ", "_") for column in df.columns]

        return df
