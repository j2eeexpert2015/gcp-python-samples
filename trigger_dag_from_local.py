import requests
import google.auth
import google.auth.transport.requests


def trigger_dag(dag_id, composer_environment, location, client_id):
    # Use the Application Default Credentials to authenticate
    credentials, project_id = google.auth.default()
    authed_session = google.auth.transport.requests.AuthorizedSession(credentials)

    # Use the client ID provided for the web server
    webserver_id = 'https://{}.appspot.com'.format(composer_environment)

    # The URL to trigger the DAG
    dag_url = '{}/api/experimental/dags/{}/dag_runs'.format(webserver_id, dag_id)

    # The JSON data to specify the execution
    json_data = {
        'conf': {}  # You can include any necessary configuration here
    }

    response = authed_session.post(dag_url, json=json_data, headers={'Referer': webserver_id, 'X-Client-Id': client_id})

    # Check the response
    if response.status_code == 200:
        print('Successfully triggered DAG:', dag_id)
    else:
        print('Failed to trigger DAG:', dag_id)
        print('Response:', response.text)


if __name__ == '__main__':
    # Specify your DAG ID, Cloud Composer environment name, and location
    dag_id = 'hello_world_dag'
    composer_environment = 'example-environment'
    location = 'us-east1'  # e.g., us-central1
    client_id = 'o490e237929f61cbcp'  # You can get this from the Cloud Console -> Composer -> Environment -> Web server

    trigger_dag(dag_id, composer_environment, location, client_id)
