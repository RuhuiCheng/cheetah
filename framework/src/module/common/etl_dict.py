import os
from src.utils.enum import prj_path,etl_layer
from airflow.models import variable
from src.utils import common
etl_dict = None


def get_etl_data():
    global etl_dict
    if etl_dict is not None:
        return etl_dict
    etl_dict = {
        'ads': {
            'init': {
                'db': '',
                'table': []
            },
            'ops': []
        },
        'dm': {
            'init': {
                'db': '',
                'table': []
            },
            'ops': []
        },
        'dws': {
            'init': {
                'db': '',
                'table': []
            },
            'ops': []
        },
        'dwd': {
            'init': {
                'db': '',
                'table': []
            },
            'ops': []
        },
        'ods': {
            'init': {
                'db': '',
                'table': []
            },
            'ops': []
        },
        'odh': {
            'init': {
                'db': '',
                'table': []
            },
            'ops': []
        },
        'stg': {
            'init': {
                'db': '',
                'table': []
            },
            'ops': []
        },
        'tmp': {
            'init': {
                'db': '',
                'table': []
            },
            'ops': []
        }
    }
    etl_dict = fill_etl_dict(etl_dict)
    return etl_dict

def fill_etl_dict(etl_dict):
    etl_path = variable.get_variable(prj_path.etl_path.name)
    root_path = "{0}/src".format(etl_path)
    print('etl_path:{0}'.format(root_path))
    current_folder = ''
    for maindir, subdir, file_name_list in os.walk(root_path):
        tmp_dir = get_current_dir(maindir)
        if tmp_dir is not None:
            current_folder = tmp_dir
        if maindir.endswith('init'):
            etl_dict[current_folder]['init']['db'] = '{0}/{1}'.format(maindir,file_name_list[0])
        if maindir.endswith('init/table'):
            for item in file_name_list:
                etl_dict[current_folder]['init']['table'].append('{0}/{1}'.format(maindir,item))
        if maindir.endswith('ops'):
            for item in file_name_list:
                file_path = '{0}/{1}'.format(maindir,item)
                ops_item = common.read_sqlheader(file_path)
                etl_dict[current_folder]['ops'].append(ops_item)
    return etl_dict


def get_current_dir(maindir):
    current_folder = None
    if maindir.endswith(etl_layer.stg.name):
        current_folder = etl_layer.stg.name
    elif maindir.endswith(etl_layer.odh.name):
        current_folder = etl_layer.odh.name
    elif maindir.endswith(etl_layer.ods.name):
        current_folder = etl_layer.ods.name
    elif maindir.endswith(etl_layer.dwd.name):
        current_folder = etl_layer.dwd.name
    elif maindir.endswith(etl_layer.dws.name):
        current_folder = etl_layer.dws.name
    elif maindir.endswith(etl_layer.dm.name):
        current_folder = etl_layer.dm.name
    elif maindir.endswith(etl_layer.ads.name):
        current_folder = etl_layer.ads.name
    elif maindir.endswith(etl_layer.tmp.name):
        current_folder = etl_layer.tmp.name
    return current_folder