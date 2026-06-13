class WarehouseMonitor:

    @staticmethod
    def calculate_metrics(rows_loaded, load_time_seconds):

        return {
            "rows_loaded": rows_loaded,
            "load_time": load_time_seconds,
            "rows_per_second": rows_loaded / load_time_seconds,
        }
