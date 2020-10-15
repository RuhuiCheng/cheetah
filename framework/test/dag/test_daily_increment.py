import os

def test_args():
   file_path = '/home/crh/ws2020/repo/cheetah_etl/src/stg/init/table/demo.hql'
   fs = os.path.split(file_path)
   file_name = os.path.splitext(fs[1])[0]
   print(file_name)