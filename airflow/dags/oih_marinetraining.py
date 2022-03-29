import datetime as dt
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

DAG_NAME = "oih_marinetraining"
CONFIG_VAR = "{}.yaml".format(DAG_NAME)
GLEANER_CMD = "/home/fils/src/Projects/gleaner.io/scheduler/airflow/airflow/bin/gleaner -cfg /home/fils/src/Projects/gleaner.io/scheduler/airflow/airflow/configs/{}".format(CONFIG_VAR)

def run_info():
    print('DAG: {} with config file: {}'.format(DAG_NAME, CONFIG_VAR))

default_args = {
    'owner': 'oih',
    'start_date': dt.datetime(2022, 3, 23),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=60),
}

with DAG(DAG_NAME, default_args=default_args,
         schedule_interval='0 11 * * *',   # ref: https://crontab.guru/#0_20_*_*_3  |  minute, hour, day (month), month, day (week)
         ) as dag:

    # The Main command we want to run
    run_gleaner = BashOperator(task_id='run_gleaner', bash_command=GLEANER_CMD )

    # A simple post run command to do X
    sleep = BashOperator(task_id='sleep', bash_command='sleep 5')

    # Place holder for some post run metadata from the object store, perhaps a quick SHACL run
    print_info = PythonOperator(task_id='print_info', python_callable=run_info)

# print_hello >> sleep >> print_world
run_gleaner >> sleep >> print_info

