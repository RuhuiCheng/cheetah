from src.module import stg_task

def test_get_ops_tasks():
    dt = stg_task.get_ops_tasks()
    assert len(dt)>0