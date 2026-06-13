class ForeignKeyMapper:

    @staticmethod
    def map_column(dataframe, source_column, target_column, lookup):

        dataframe[target_column] = dataframe[source_column].map(lookup)

        return dataframe
