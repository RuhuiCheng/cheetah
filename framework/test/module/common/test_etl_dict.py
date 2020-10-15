from src.module.common import etl_dict

def test_init():
    res = etl_dict.get_etl_data()
    assert res is not None