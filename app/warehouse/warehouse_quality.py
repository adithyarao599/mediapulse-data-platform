class WarehouseQuality:

    @staticmethod
    def null_check(dataframe):

        return dataframe.isnull().sum().sum()

    @staticmethod
    def duplicate_check(dataframe):

        return dataframe.duplicated().sum()
