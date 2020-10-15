import os
from jinja2 import Template
from airflow.models import variable
from src.utils import common, datax
from src.utils.enum import prj_path, conn_id
from src.module.common import mysql_ops, jdbc_ops


class DataxOperation:

    def __init__(self, sql_path, current_date, start_item, end_item, server_id, db_table):
        self.sql_path = sql_path
        self.current_date = current_date
        self.start_item = start_item
        self.end_item = end_item
        self.server_id = server_id
        self.db_table = db_table

    def run(self):
        # 1. create datax json config
        datax_path = self.__generate_datax_json()
        # 2. refresh hive table PARTITION
        sql_text = "ALTER TABLE stg.{0} DROP IF EXISTS PARTITION (dt='{1}');ALTER TABLE stg.{0} ADD PARTITION (dt='{1}')".format(
            self.db_table, self.current_date)
        jdbc_ops.execute_hql(conn_id.conn_hive_jdbc.name, sql_text, False)
        # 3. execute datax
        datax.run(datax_path)

    def __generate_datax_json(self):
        # 1 get mysql query string
        sql_txt = self.__get_mysql_text()

        # 2 get hive stg columns
        hive_columns = self.__get_hive_columns()

        # 3 create datax string and save to path
        tmp_txt = variable.get_variable(self.server_id)
        template = Template(tmp_txt)
        # 4 hdfs path
        hdfs_path = '/user/hive/warehouse/stg.db/{0}/dt={1}'
        tb_path = hdfs_path.format(self.db_table, self.current_date)
        # 5 get datax config
        res = template.render(hive_table_columns=hive_columns,
                              sql_query=sql_txt, hdfs_path=tb_path, fileName=self.db_table)
        # 6 save to etl project
        datax_path = self.__save_to_stg_tmp(res)
        return datax_path

    def __get_mysql_text(self):
        tmp_txt = common.read_txt(self.sql_path)
        template = Template(tmp_txt)
        return template.render(start_item=self.start_item, end_item=self.end_item)

    def __get_hive_columns(self):
        etl_path = variable.get_variable(prj_path.etl_path.name)
        sql_path = '{0}/src/stg/hive_meta.sql'.format(etl_path)
        tmp_txt = common.read_txt(sql_path)
        template = Template(tmp_txt)
        sql_txt = template.render(db_name='stg', tb_name=self.db_table)
        ls_columns = mysql_ops.get_list(
            conn_id.conn_hive_metadata.name, sql_txt)
        str_template = ''
        for item in ls_columns:
            str_template += '{ "name": "'+item[0]+'","type": "'+item[1]+'" },'
        str_template = str_template.rstrip(',')
        return str_template

    def __save_to_stg_tmp(self, content):
        datax_home = variable.get_variable(prj_path.datax_home.name)
        datax_dir = "{0}/tmp/json/{1}".format(datax_home, self.current_date)
        if not os.path.exists(datax_dir):
            os.makedirs(datax_dir,exist_ok=True)
        datax_path = "{0}/{1}.json".format(datax_dir, self.db_table)
        common.write_txt(datax_path, content)
        return datax_path
