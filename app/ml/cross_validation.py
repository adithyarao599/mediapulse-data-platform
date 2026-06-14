from sklearn.model_selection import cross_val_score


class CrossValidator:

    @staticmethod
    def evaluate(model, features, target):

        scores = cross_val_score(model, features, target, cv=5, scoring="r2")

        return {"mean_score": scores.mean(), "std_score": scores.std()}
