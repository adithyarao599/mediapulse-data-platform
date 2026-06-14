class DriftDetector:

    @staticmethod
    def detect(training_mean, production_mean, threshold=0.2):

        difference = abs(training_mean - production_mean)

        return difference > threshold
