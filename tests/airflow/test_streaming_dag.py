from airflow.models import DagBag


def test_streaming_dag():

    dagbag = DagBag()

    dag = dagbag.get_dag("streaming_platform")

    assert dag is not None
