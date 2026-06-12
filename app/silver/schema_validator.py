class SchemaValidator:

    @staticmethod
    def validate(dataframe, expected_columns):

        missing_columns = [
            column for column in expected_columns if column not in dataframe.columns
        ]

        if missing_columns:

            raise ValueError(f"Missing columns: " f"{missing_columns}")

        return True
