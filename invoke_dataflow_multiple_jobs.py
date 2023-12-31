import datetime
from airflow import models
from airflow.contrib.operators.dataflow_operator import DataFlowJavaOperator
from airflow.utils.dates import days_ago

bucket_path = "gs:/dataflow-base-bucket/jars/gcp-dataflow-java-bundled-1.0-SNAPSHOT.jar"
gcp_project_id = "healthy-reason-396205"

default_args = {
    'start_date': days_ago(1),
    'dataflow_default_options': {
        'project': gcp_project_id,
        'region': gcp_project_id,
        'tempLocation': 'gs://dataflow_compser_run/temp'
    }
}

with models.DAG(
        'composermultipletasks',
        schedule_interval=datetime.timedelta(days=1),
        default_args=default_args) as dag:

    t1 = DataFlowJavaOperator(
        task_id='rundataflowjobfirst',
        jar=bucket_path,
        job_class='dataflowsample.SamplePipeline'
    )

    t1
