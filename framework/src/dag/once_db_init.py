from airflow import DAG
from datetime import datetime

from airflow.models import variable
framework_path = variable.get_variable("framework_path")
import sys
sys.path.append(framework_path)

from src.module import data_init

args = {
    'owner': 'demo',
    'depends_on_past': False,
    'start_date': datetime(2020, 9, 9),
    'email': ['demo.cheng@hotmail.com'],
    'queue': 'cheetah_q1'
}

dag = DAG(
    dag_id='once_db_init',
    default_args=args,
    schedule_interval='@once',
    tags=['default']
)

# init schema
data_init.schema_init(dag)


