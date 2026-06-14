from datetime import datetime


class ModelVersioning:

    @staticmethod
    def generate_version():

        return datetime.now().strftime("%Y%m%d%H%M%S")
