import os
from src.module.common import etl_dict, jdbc_ops
from src.utils.enum import etl_layer
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from src.utils.enum import conn_id
from src.utils import common


def schema_init(dag):
    all_dt = etl_dict.get_etl_data()
    for item in etl_layer:
        db_ops = PythonOperator(
        task_id=item.name,
        python_callable=callback_db_init,
        provide_context=True,
        op_kwargs={"db_name":item.name},
        dag=dag)

        tbs = all_dt[item.name]['init']['table']
        for tb_item in tbs:
            fs = os.path.split(tb_item)
            file_name = os.path.splitext(fs[1])[0]
            table_ops = PythonOperator(
            task_id='{0}_{1}'.format(item.name,file_name),
            python_callable=callback_table_init,
            provide_context=True,
            op_kwargs={"hql_file":tb_item},
            dag=dag)
            db_ops >> table_ops


def callback_db_init(ds, **kwargs):
    db_name = kwargs['db_name']
    all_dt = etl_dict.get_etl_data()
    hql_file = all_dt[db_name]['init']['db']
    sql_text = common.read_txt(hql_file)
    jdbc_ops.execute_hql(conn_id.conn_hive_jdbc.name, sql_text)


def callback_table_init(ds, **kwargs):
    hql_file = kwargs['hql_file']
    sql_text = common.read_txt(hql_file)
    jdbc_ops.execute_hql(conn_id.conn_hive_jdbc.name, sql_text)
