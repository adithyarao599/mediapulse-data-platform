from app.ml.prediction_service import PredictionService


class BatchInference:

    @staticmethod
    def run(model_path, dataframe):

        predictions = PredictionService.predict(model_path, dataframe)

        dataframe["prediction"] = predictions

        return dataframe
