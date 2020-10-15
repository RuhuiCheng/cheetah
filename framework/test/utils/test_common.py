from src.utils import common

sql_file = '/home/crh/ws2020/repo/cheetah_etl/src/stg/ops/demo.sql'

def test_read_txt():
    sql_txt = common.read_txt(sql_file)
    assert len(sql_txt) > 0


def test_read_sqlheader():
    res = common.read_sqlheader(sql_file)
    assert res is not None