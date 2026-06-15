from airflow.models import DagBag


def test_dag_loaded():
    dagbag = DagBag(include_examples=False)

    assert len(dagbag.import_errors) == 0
    assert "streaming_platform" in dagbag.dags
