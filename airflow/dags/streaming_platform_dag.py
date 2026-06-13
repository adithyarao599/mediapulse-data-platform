from datetime import datetime

from airflow.operators.empty import EmptyOperator

from airflow import DAG
from airflow.dags.config import DEFAULT_ARGS
from airflow.dags.task_groups import create_bronze_group

with DAG(
    dag_id="streaming_platform",
    default_args=DEFAULT_ARGS,
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["streaming", "production"],
) as dag:

    start = EmptyOperator(task_id="start")

    bronze_group = create_bronze_group()

    silver = EmptyOperator(task_id="silver")

    gold = EmptyOperator(task_id="gold")

    warehouse = EmptyOperator(task_id="warehouse")

    end = EmptyOperator(task_id="end")

    start >> bronze_group

    bronze_group >> silver

    silver >> gold

    gold >> warehouse

    warehouse >> end
