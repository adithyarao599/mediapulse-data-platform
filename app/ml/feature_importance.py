import pandas as pd


class FeatureImportance:

    @staticmethod
    def generate(model, feature_names):

        return pd.DataFrame(
            {"feature": feature_names, "importance": model.feature_importances_}
        )
