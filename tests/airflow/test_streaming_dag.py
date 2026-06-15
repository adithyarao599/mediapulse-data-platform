from airflow.models import DagBag


def test_streaming_dag():
    dagbag = DagBag(include_examples=False)

    assert len(dagbag.import_errors) == 0
    assert "streaming_platform" in dagbag.dags
