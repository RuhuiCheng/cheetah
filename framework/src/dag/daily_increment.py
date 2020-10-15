from airflow import DAG
from datetime import datetime

from airflow.models import variable
framework_path = variable.get_variable("framework_path")
import sys
sys.path.append(framework_path)
from src.module import ods_task, dwd_task, dws_task, dm_task
from src.module.common import dag_meta

args = {
    'owner': 'demo',
    'depends_on_past': False,
    'start_date': datetime(2020, 9, 9),
    'email': ['demo.cheng@hotmail.com'],
    'queue': 'cheetah_q1'
}

dag = DAG(
    dag_id='daily_increment',
    default_args=args,
    schedule_interval='0 18 * * *'
)

# get node list
ls_node = dag_meta.get_node_list(dag.dag_id)
# flow node init
ls_ods_task = ods_task.node_init(dag, ls_node)
ls_dwd_node = dwd_task.node_init(dag, ls_node)
ls_dws_node = dws_task.node_init(dag, ls_node)
ls_dm_node = dm_task.node_init(dag, ls_node)

# get relation list
ls_relation = dag_meta.get_relation_list(dag.dag_id)
# flow relation init
ods_task.relation_init(ls_relation, ls_ods_task, ls_dwd_node, ls_dws_node, ls_dm_node)
dwd_task.relation_init(ls_relation, ls_dwd_node, ls_dws_node, ls_dm_node)
dws_task.relation_init(ls_relation, ls_dws_node, ls_dm_node)