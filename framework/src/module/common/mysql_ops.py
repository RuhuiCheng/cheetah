import pymysql
import logging
from airflow.hooks.base_hook import BaseHook
logger = logging.getLogger(__name__)


def get_conn(mysql_host, mysql_port, mysql_user, mysql_password, mysql_database, timeout=None):
    return pymysql.connect(
        host=mysql_host,
        port=mysql_port,
        user=mysql_user,
        password=mysql_password,
        database=mysql_database,
        read_timeout=timeout,
        charset='utf8mb4'
        # cursorclass=pymysql.cursors.DictCursor
    )


def get_list(conn_id, sql_text):
    logger.info(sql_text)
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


def get_one(conn_id, sql_text):
    logger.info(sql_text)
    res = None
    try:
        db = BaseHook.get_connection(conn_id)
        conn = get_conn(db.host, db.port, db.login, db.password, db.schema)
        with conn.cursor() as cursor:
            cursor.execute(sql_text)
            res = cursor.fetchone()
    finally:
        conn.close()
    return res


# insert or update one
def execute_one(conn_id, sql_text):
    res = None
    try:
        db = BaseHook.get_connection(conn_id)
        conn = get_conn(db.host, db.port, db.login, db.password, db.schema)
        with conn.cursor() as cursor:
            cursor.execute(sql_text)
            res = cursor.lastrowid
            conn.commit()
    finally:
        conn.close()
    return res