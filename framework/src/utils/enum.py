from enum import IntEnum, unique


@unique
class exec_status(IntEnum):
    failed = 0
    success = 1
    processing = 2


@unique
class conn_id(IntEnum):
    conn_hive_jdbc = 0
    conn_hive_metadata = 1
    conn_cheetah = 2


@unique
class prj_path(IntEnum):
    datax_home = 1
    etl_path = 0
    framework_path = 2


@unique
class etl_layer(IntEnum):
    ads = 0
    dm = 1
    dws = 2
    dwd = 3
    ods = 4
    odh = 5
    stg = 6
    tmp = 7
