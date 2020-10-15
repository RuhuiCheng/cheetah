from src.module import data_init

def test_hql_exec():
    data_init.hql_exec("/home/crh/ws2020/repo/cheetah_etl/src/stg/init/[db].hql")
    print('ok')