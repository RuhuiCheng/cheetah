from src.module.common import dag_meta


def test_get_node_list():
    ls_node = dag_meta.get_node_list('daily_increment')
    assert len(ls_node) > 0
