class MLMonitor:

    @staticmethod
    def calculate_metrics(total_predictions, failed_predictions):

        success_rate = (
            (total_predictions - failed_predictions) / total_predictions
        ) * 100

        return {"success_rate": success_rate}
