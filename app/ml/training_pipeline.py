from sklearn.model_selection import train_test_split

from app.ml.hyperparameter_tuning import HyperparameterTuning
from app.ml.model_registry import ModelRegistry


class TrainingPipeline:

    def train_popularity_model(self, features, target):

        x_train, x_test, y_train, y_test = train_test_split(
            features, target, test_size=0.2, random_state=42
        )

        model = HyperparameterTuning.tune(x_train, y_train)

        ModelRegistry.save_model(model, "popularity_model")

        return model
