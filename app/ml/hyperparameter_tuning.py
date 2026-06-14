from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV


class HyperparameterTuning:

    @staticmethod
    def tune(features, target):

        parameters = {"n_estimators": [100, 200], "max_depth": [5, 10]}

        model = RandomForestRegressor(random_state=42)

        grid = GridSearchCV(model, parameters, cv=3)

        grid.fit(features, target)

        return grid.best_estimator_
