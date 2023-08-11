import google.auth
import google.auth.transport.requests
import requests
import os


def trigger_dag(data, context):
    # Set the environment, location, and DAG name
    composer_environment = 'composer1'
    composer_location = 'us-east1'
    dag_name = 'airflow_monitoring'
    project_id ='sanguine-anthem-393416'

    # Use the default identity provided by GCF instance metadata
    credentials, project_id = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )

    # Create a request to trigger the DAG
    url = (f"https://composer.googleapis.com/v1beta1/projects/{project_id}/"
           f"locations/{composer_location}/environments/{composer_environment}"
           f"/dags/{dag_name}/triggerDag")

    auth_req = google.auth.transport.requests.Request()
    credentials.refresh(auth_req)

    response = requests.post(
        url,
        headers={'Authorization': f'Bearer {credentials.token}'},
        json={}
    )

    if response.status_code == 200:
        print(f'Successfully triggered {dag_name}')
    else:
        print(f'Failed to trigger {dag_name}. Response: {response.text}')
