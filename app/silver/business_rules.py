class BusinessRules:

    @staticmethod
    def validate_positive_metrics(dataframe, metric_columns):

        for column in metric_columns:

            if (dataframe[column] < 0).any():

                raise ValueError(f"Negative values " f"found in {column}")

        return True
