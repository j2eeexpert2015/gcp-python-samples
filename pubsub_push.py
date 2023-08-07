from airflow import models, utils
from airflow.providers.google.cloud.operators.pubsub import PubSubPublishMessageOperator

with models.DAG(
    "publish_to_pubsub",
    schedule_interval="@daily",
    start_date=utils.dates.days_ago(1),
    tags=["example"],
) as dag:

    publish_message = PubSubPublishMessageOperator(
        task_id="publish_message",
        project_id="your-gcp-project-id",
        topic="your-topic-name",
        messages=[{"data": "Your message payload"}],
    )
