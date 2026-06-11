import pandas as pd


def generate_report(df):

    report = {
        "row_count": len(df),
        "columns": len(df.columns),
        "nulls": df.isnull().sum().sum(),
    }

    return report
