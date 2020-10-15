import os
import socket
import logging
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from jinja2 import Template
from src.module.common import etl_dict, jdbc_ops
from src.utils.enum import etl_layer, conn_id
from src.utils import common
logger = logging.getLogger(__name__)


def node_init(dag, ls_node):
    ls_dm_node = []
    ls_node = [item for item in ls_node if item[1] == etl_layer.dm.name]
    for item in ls_node:
        flow_tag = item[2]
        dm_node = per_node_init(dag,flow_tag)
        ls_dm_node.append(dm_node)
    return ls_dm_node


def per_node_init(dag, flow_tag):
    all_data = etl_dict.get_etl_data()
    ops_data = all_data[etl_layer.dm.name]['ops']
    for item in ops_data:
        if item['flow_tag'] == flow_tag:
            file_path = item['sql_path']
            fs = os.path.split(file_path)
            file_name = os.path.splitext(fs[1])
            task_item = {'sql_path': file_path, 
                         'incr_type':item['incr_type'],
                         'task_name': file_name[0]}
            dm_node = PythonOperator(
            task_id='{0}_{1}'.format(etl_layer.dm.name, task_item['task_name']),
            python_callable=ops_call_back,
            op_kwargs=task_item,
            pool='comm_task_pool',
            provide_context=True,
            dag=dag)
            return {'flow_tag':flow_tag,'node':dm_node}


def ops_call_back(ds, **kwargs):
    host_name = socket.gethostname()
    sql_path = kwargs['sql_path']
    tmp_txt = common.read_txt(sql_path)
    template = Template(tmp_txt)
    sql_text = template.render(dt=ds)
    msg = 'hostname:{0}, sqlpath:{1}, dt:{2}'.format(
        host_name, sql_path, ds)
    logger.info("dm task start -->{0}".format(msg))
    jdbc_ops.execute_hql(conn_id.conn_hive_jdbc.name, sql_text)
    logger.info("dm task done -->{0}".format(msg))
