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
    ls_dwd_node = []
    ls_node = [item for item in ls_node if item[1] == etl_layer.dwd.name]
    for item in ls_node:
        flow_tag = item[2]
        dwd_node = per_node_init(dag,flow_tag)
        ls_dwd_node.append(dwd_node)
    return ls_dwd_node


def per_node_init(dag, flow_tag):
    all_data = etl_dict.get_etl_data()
    ops_data = all_data[etl_layer.dwd.name]['ops']
    for item in ops_data:
        if item['flow_tag'] == flow_tag:
            file_path = item['sql_path']
            fs = os.path.split(file_path)
            file_name = os.path.splitext(fs[1])
            task_item = {'sql_path': file_path, 
                         'incr_type':item['incr_type'],
                         'task_name': file_name[0]}
            dwd_node = PythonOperator(
            task_id='{0}_{1}'.format(etl_layer.dwd.name, task_item['task_name']),
            python_callable=ops_call_back,
            op_kwargs=task_item,
            pool='comm_task_pool',
            provide_context=True,
            dag=dag)
            return {'flow_tag':flow_tag,'node':dwd_node}


def relation_init(ls_relation ,ls_dwd_node ,ls_dws_node ,ls_dm_node):
    for dwd_item in ls_dwd_node:
        dwd_node = dwd_item['node']
        dwd_node_tag = dwd_item['flow_tag']
        for dws_item in ls_dws_node:
            dws_node = dws_item['node']
            dws_node_tag = dws_item['flow_tag']
            rel_dws = [item for item in ls_relation if item[0] == dwd_node_tag and item[1] == dws_node_tag]
            if len(rel_dws) == 1:
                dwd_node >> dws_node

        for dm_item in ls_dm_node:
            dm_node = dm_item['node']
            dm_node_tag = dm_item['flow_tag']
            rel_dm = [item for item in ls_relation if item[0] == dwd_node_tag and item[1] == dm_node_tag]
            if len(rel_dm) == 1:
                dwd_node >> dm_node


def ops_call_back(ds, **kwargs):
    host_name = socket.gethostname()
    sql_path = kwargs['sql_path']
    tmp_txt = common.read_txt(sql_path)
    template = Template(tmp_txt)
    sql_text = template.render(dt=ds)
    msg = 'hostname:{0}, sqlpath:{1}, dt:{2}'.format(
        host_name, sql_path, ds)
    logger.info("dwd task start -->{0}".format(msg))
    jdbc_ops.execute_hql(conn_id.conn_hive_jdbc.name, sql_text)
    logger.info("dwd task done -->{0}".format(msg))
