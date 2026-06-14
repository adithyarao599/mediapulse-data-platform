import joblib


class PredictionService:

    @staticmethod
    def predict(model_path, features):

        model = joblib.load(model_path)

        return model.predict(features)
