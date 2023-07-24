import datetime

from airflow import models
from airflow.contrib.operators.dataflow_operator import DataFlowPythonOperator
from airflow.utils.dates import days_ago

args = {
    'start_date': days_ago(1),
    'dataflow_default_options': {
        'project': 'sanguine-anthem-393416',
        'region': 'us-central1',
        'stagingLocation': 'gs://gcpsampleall/gcp_python/staging',
        'tempLocation': 'gs://gcpsampleall/gcp_python/temp',
        'runner': 'DataflowRunner',
    },
}

with models.DAG(
    'composer_dataflow_dag',
    schedule_interval=datetime.timedelta(days=1),
    default_args=args) as dag:

    start_python_dataflow_job = DataFlowPythonOperator(
        task_id='start-python-dataflow-job',
        py_file='gs://gcpsampleall/gcp_python/dataflow/jobs/dataflow_sample.py',
        py_requirements='gs://gcpsampleall/gcp_python/dataflow/jobs/requirements.txt',
        py_interpreter='python3',
    )
