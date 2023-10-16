import datetime
from airflow import models
from airflow.contrib.operators.dataflow_operator import DataFlowJavaOperator
from airflow.utils.dates import days_ago

bucket_path = "gs://df-new/jars/gcp-dataflow-java.jar"
gcp_project_id = "healthy-reason-396205"
region ="us-east1"

default_args = {
    'start_date': days_ago(1),
    'dataflow_default_options': {
        'project': gcp_project_id,
        'region': region,
        'tempLocation': 'gs://df-new/temp'
    }
}

with models.DAG(
        'dataflowmodelv333',
        schedule_interval=datetime.timedelta(days=1),
        default_args=default_args) as dag:

    t1 = DataFlowJavaOperator(
        task_id='dataflowtaskv333',
        jar=bucket_path,
        job_class='dataflowsample.SamplePipeline'
    )

    t1
