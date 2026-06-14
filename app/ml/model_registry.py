import joblib

from app.ml.model_versioning import ModelVersioning


class ModelRegistry:

    @staticmethod
    def save_model(model, model_name):

        version = ModelVersioning.generate_version()

        file_path = f"artifacts/models/" f"{model_name}_" f"{version}.pkl"

        joblib.dump(model, file_path)

        return file_path
