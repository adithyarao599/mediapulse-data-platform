class ReferentialIntegrity:

    @staticmethod
    def validate(dataframe, key_column):

        return dataframe[key_column].notnull().all()
