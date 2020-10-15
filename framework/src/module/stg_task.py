import os
import socket
import logging
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from src.module.common import etl_dict
from src.module.stg_datax import DataxOperation
from src.utils.enum import etl_layer
logger = logging.getLogger(__name__)


def per_node_init(dag, flow_tag):
    all_data = etl_dict.get_etl_data()
    ops_data = all_data[etl_layer.stg.name]['ops']
    for item in ops_data:
        # logger.info('stg per_node_init-->{0}'.format(item))
        if item['flow_tag'] == flow_tag:
            file_path = item['sql_path']
            fs = os.path.split(file_path)
            file_name = os.path.splitext(fs[1])
            tmp = file_name[0].strip('[').strip(']').split('].[')
            db_table = '{0}_{1}_{2}'.format(tmp[0], tmp[1], tmp[2])
            task_item = {'sql_path': file_path,
                     'incr_type': item['incr_type'],
                     'server_id': tmp[0] + '_' + tmp[1],
                     'db_table': db_table}
            stg_node = PythonOperator(
            task_id='{0}_{1}'.format(etl_layer.stg.name, task_item['db_table']),
            python_callable=ops_call_back,
            op_kwargs=task_item,
            pool='stg_task_pool',
            provide_context=True,
            dag=dag)
            return stg_node


def ops_call_back(ds, tomorrow_ds, **kwargs):
    host_name = socket.gethostname()
    sql_path = kwargs["sql_path"]
    current_date = ds
    start_item = ds
    end_item = tomorrow_ds
    server_id = kwargs["server_id"]
    db_table = kwargs["db_table"]
    msg = 'hostname:{0}, sqlpath:{1}, dt_start:{2}, dt_end:{3}'.format(
        host_name, sql_path, start_item, end_item)
    logger.info("stg task start -->{0}".format(msg))
    _ops = DataxOperation(sql_path, current_date,
                          start_item, end_item, server_id, db_table)
    _ops.run()
    logger.info("stg task done -->{0}".format(msg))
