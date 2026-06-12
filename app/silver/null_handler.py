import pandas as pd


class NullHandler:

    @staticmethod
    def fill_string_nulls(df):

        string_columns = df.select_dtypes(include=["object"]).columns

        df[string_columns] = df[string_columns].fillna("UNKNOWN")

        return df

    @staticmethod
    def fill_numeric_nulls(df):

        numeric_columns = df.select_dtypes(include=["number"]).columns

        df[numeric_columns] = df[numeric_columns].fillna(0)

        return df
