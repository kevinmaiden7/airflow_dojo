# Python standard modules
from datetime import datetime, timedelta

# Airflow modules
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=30),
    'max_active_runs': 1
}

dag_key = 'dag_key'

dag = DAG(dag_key,
          description = 'DAG description',
          default_args = default_args,
          schedule_interval = None
)

task_1 = BashOperator(
    task_id = 'task_1',
    bash_command = 'pwd',
    dag = dag
)

task_2 = BashOperator(
    task_id = 'task_2',
    bash_command = 'touch /airflow/my_bash_file.txt',
    dag = dag
)

task_3 = BashOperator(
    task_id = 'task_3',
    bash_command = 'cp /airflow/my_bash_file.txt /airflow/my_bash_file_changed.txt',
    dag = dag
)

task_1 >> task_2 >> task_3
