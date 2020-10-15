from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime


default_args = {
    'owner': 'demo',
    'depends_on_past': False,
    'start_date': datetime(2020, 9, 9),
    'email': ['demo.cheng@hotmail.com'],
    'queue': 'cheetah_q1'
}

dag = DAG("daily_maintain", 
        default_args=default_args, 
        schedule_interval='0 8 * * *',
        tags=['default'])

def test(ds, **kwargs):
    print("hello")
    # 1/0

task_table_init = PythonOperator(
        task_id='task_hello',
        python_callable=test,
        provide_context=True,
        dag=dag
    )