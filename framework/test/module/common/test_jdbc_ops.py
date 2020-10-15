from src.module.common import jdbc_ops
from src.utils import common
from jinja2 import Template


def test_query():
    from airflow.hooks.jdbc_hook import JdbcHook
    hh = JdbcHook(jdbc_conn_id="conn_hive_jdbc")
    # sql = "select * from stg.mdm_hap_prd_hmdm_md limit 100"
    sql = "select * from test_tmp.demo"
    id = hh.get_records(sql=sql)
    print('JDBC done')

def test_execute_hql():
    sql_text = common.read_txt("/home/crh/ws2020/repo/cheetah_etl/src/ods/ops/demo.hql")
    template = Template(sql_text)
    sql_text = template.render(dt='2020-08-01')
    jdbc_ops.execute_hql("conn_hive_jdbc",sql_text)
    print('JDBC done')


def test_get_list():
    sql_text = common.read_txt("/home/crh/ws2020/repo/cheetah_etl/test/stg/test1.sql")
    ls = jdbc_ops.get_list("conn_hive_jdbc",sql_text)
    assert len(ls) > 0