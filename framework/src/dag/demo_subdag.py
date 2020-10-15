# Hourly call third-party api (e.g: GI @ CBEC)
from airflow import DAG
from airflow.operators.subdag_operator import SubDagOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

from airflow.models import variable
framework_path = variable.get_variable("framework_path")
import sys
sys.path.append(framework_path)

from src.dag.subdags.subdag import subdag

DAG_NAME = 'demo_subdag'
args = {
    'owner': 'airflow',
}

dag = DAG(
    dag_id=DAG_NAME,
    default_args=args,
    start_date= datetime(2020, 9, 22),
    schedule_interval="@once",
    tags=['example']
)

start = DummyOperator(
    task_id='start',
    dag=dag,
)

section_1 = SubDagOperator(
    task_id='section-1',
    subdag=subdag(DAG_NAME, 'section-1', args),
    dag=dag,
)

some_other_task = DummyOperator(
    task_id='some-other-task',
    dag=dag,
)

section_2 = SubDagOperator(
    task_id='section-2',
    subdag=subdag(DAG_NAME, 'section-2', args),
    dag=dag,
)

end = DummyOperator(
    task_id='end',
    dag=dag,
)

start >> section_1 >> some_other_task >> section_2 >> end