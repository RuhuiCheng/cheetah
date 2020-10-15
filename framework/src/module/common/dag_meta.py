from src.module.common import mysql_ops
from src.utils.enum import conn_id


def get_node_list(dag_name):
    sql_text = "select n.id, n.layer , n.flow_tag \
        from cheetah.node as n \
        inner join cheetah.dag as d\
        on n.dag_id  = d.id \
        where n.is_enabled = 1 \
        and d.is_enabled = 1 \
        and d.name ='{0}'".format(dag_name)
    ls_node = mysql_ops.get_list(conn_id.conn_cheetah.name, sql_text)
    return ls_node


def get_relation_list(dag_name):
    sql_text = "select \
                	f.flow_tag as from_tag \
                	,t.flow_tag as to_tag \
                from cheetah.relation as r \
                inner join cheetah.node as f \
                on r.node_from_id = f.id \
                inner join cheetah.dag as tg \
                on f.dag_id = tg.id \
                inner join cheetah.node as t \
                on r.node_to_id = t.id \
                where r.is_enabled = 1 \
                and f.is_enabled = 1 \
                and tg.is_enabled = 1 \
                and t.is_enabled = 1  \
                and tg.name ='{0}'".format(dag_name)
    ls_relation = mysql_ops.get_list(conn_id.conn_cheetah.name, sql_text)
    return ls_relation
