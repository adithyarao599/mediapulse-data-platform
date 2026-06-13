from datetime import datetime

from airflow.operators.python import PythonOperator

from airflow import DAG
from airflow.dags.config import DEFAULT_ARGS


def run_quality_check():

    print("Running data quality checks")


with DAG(
    dag_id="data_quality",
    default_args=DEFAULT_ARGS,
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    quality_check = PythonOperator(
        task_id="quality_check", python_callable=run_quality_check
    )
