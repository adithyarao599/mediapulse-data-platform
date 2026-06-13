from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup


def create_bronze_group():

    with TaskGroup(group_id="bronze_group") as group:

        ingest_spotify = EmptyOperator(task_id="ingest_spotify")

        ingest_netflix = EmptyOperator(task_id="ingest_netflix")

    return group
