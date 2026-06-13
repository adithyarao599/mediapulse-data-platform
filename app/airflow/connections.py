from airflow.hooks.base import BaseHook


class DatabaseConnection:

    @staticmethod
    def get_postgres():

        return BaseHook.get_connection("postgres_default")
