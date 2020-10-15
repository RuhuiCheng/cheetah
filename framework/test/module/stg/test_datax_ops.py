import time
from src.module.stg_datax import DataxOperation

def test_datax_ops_run():
    sql_path = '/home/crh/ws2020/repo/cheetah_etl/src/stg/ops/demo.sql'
    current_date = time.strftime("%Y-%m-%d", time.localtime())
    dt_start = None #'2020-07-26 09:00:00'
    dt_end = None #'2020-07-26 10:00:00'
    server_id = 'S1'
    stg_table_name = 'airflow_log'
    _ops = DataxOperation(sql_path,current_date,dt_start,dt_end,server_id,stg_table_name)
    bl =_ops.run()
    assert bl
    