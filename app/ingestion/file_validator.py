from pathlib import Path


class FileValidator:

    @staticmethod
    def file_exists(path):

        return Path(path).exists()

    @staticmethod
    def file_not_empty(path):

        return Path(path).stat().st_size > 0
