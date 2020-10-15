from pyhive import hive
from airflow.hooks.base_hook import BaseHook


def get_conn(hive_host, hive_port, hive_user, hive_password, hive_database):
    return hive.Connection(
        host=hive_host,
        port=hive_port,
        username=hive_user,
        password=hive_password,
        database=hive_database,
        auth='LDAP'
    )


def execute_hql(conn_id, sql_text, db_name='default'):
    try:
        db = BaseHook.get_connection(conn_id)
        conn = get_conn(db.host, db.port, db.login, db.password, db_name)
        with conn.cursor() as cursor:
            cursor.execute(sql_text)
    finally:
        conn.close()


def get_list(conn_id, sql_text):
    res = None
    try:
        db = BaseHook.get_connection(conn_id)
        conn = get_conn(db.host, db.port, db.login, db.password, db.schema)
        with conn.cursor() as cursor:
            cursor.execute(sql_text)
            res = cursor.fetchall()
    finally:
        conn.close()
    return res
