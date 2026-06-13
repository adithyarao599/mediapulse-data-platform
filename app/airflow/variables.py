from airflow.models import Variable


class PipelineVariables:

    @staticmethod
    def get_environment():

        return Variable.get("environment", default_var="dev")
