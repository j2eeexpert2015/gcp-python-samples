from airflow import models
from airflow.providers.google.cloud.sensors.pubsub import PubSubPullSensor
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

with models.DAG(
    "pull_from_pubsub",
    schedule_interval=None,  # This DAG is manually triggered
    start_date=days_ago(1),
    tags=["example"],
) as dag:

    wait_for_message = PubSubPullSensor(
        task_id="wait_for_message",
        project_id="your-gcp-project-id",
        subscription="your-subscription-name",
        ack_messages=True,
        max_messages=1,
    )

    next_task = DummyOperator(
        task_id="next_task",
    )

    wait_for_message >> next_task
