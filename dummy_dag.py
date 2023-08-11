import datetime
from airflow import models
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def hello_world():
    print("Hello, World!")

# Default DAG arguments.
default_args = {
    'start_date': datetime.datetime(2023, 8, 11),
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
}

with models.DAG(
    'hello_world_dag',
    schedule_interval=None,  # Override to None to make it run manually only
    default_args=default_args) as dag:

    start = DummyOperator(
        task_id='start',
    )

    hello_world_task = PythonOperator(
        task_id='hello_world_task',
        python_callable=hello_world,
    )

    end = DummyOperator(
        task_id='end',
    )

    start >> hello_world_task >> end
