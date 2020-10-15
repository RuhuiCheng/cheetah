from airflow.hooks.jdbc_hook import JdbcHook
import re

def execute_hql(conn_id, sql_text, transfer=True):
    jh = JdbcHook(jdbc_conn_id=conn_id)
    if(transfer) :
        sql_text_without_comment = re.sub(r'--[\w\s].*?\n', ' ', sql_text)
        sql_text_replace_semicolon_in_comment = re.sub(r';(?=.*\')', ',', sql_text_without_comment)
        sql_text_without_enter = re.sub('\\n+', ' ', sql_text_replace_semicolon_in_comment)
        sql_text_without_comment_segment = re.sub(r'/[*].*?[*]/', ' ', sql_text_without_enter)
        sql_text_without_space = re.sub(r'\s+', ' ', sql_text_without_comment_segment)
        ls_sql_statement = sql_text_without_space.split(';')
        ls_sql_statement_final = list(map(lambda sql_item: re.sub(r'^\s+', '', sql_item) ,filter(lambda sql: sql and sql.strip(), ls_sql_statement)))
    else:
        ls_sql_statement_final = sql_text.split(';')
    jh.run(ls_sql_statement_final)

def get_list(conn_id, sql_text):
    jh = JdbcHook(jdbc_conn_id=conn_id)
    ls = jh.get_records(sql_text)
    return ls