from airflow import DAG
from airflow.operators.python import PythonOperator
import time
from App.weather_app import *
# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'retries': 0,
    'start_date': '2025-06-10'
}

# Define the DAG
with DAG(
    dag_id='weather_app',
    default_args=default_args,
    description='A DAG for getting the Daily Weather data and populate in Database',
    schedule_interval='*/30 * * * *',  
    catchup=False,
) as dag:

    def start_task():
        print("Starting the DAG!")

    def process_data():
        print("Processing data...")
        start = Start_Weather_App()

    def end_task():
        print("DAG has completed.")

    # Define tasks
    start = PythonOperator(
        task_id='start',
        python_callable=start_task
    )

    process = PythonOperator(
        task_id='process_data',
        python_callable=process_data
    )

    end = PythonOperator(
        task_id='end',
        python_callable=end_task
    )

    # Set task dependencies
    start >> process >> end
