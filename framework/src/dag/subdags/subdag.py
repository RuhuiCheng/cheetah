"""Helper function to generate a DAG and operators given some arguments."""

# [START subdag]
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago


def subdag(parent_dag_name, child_dag_name, args):
    """
    Generate a DAG to be used as a subdag.

    :param str parent_dag_name: Id of the parent DAG
    :param str child_dag_name: Id of the child DAG
    :param dict args: Default arguments to provide to the subdag
    :return: DAG to use as a subdag
    :rtype: airflow.models.DAG
    """
    dag_subdag = DAG(
        dag_id='%s.%s' % (parent_dag_name, child_dag_name),
        default_args=args,
        start_date=days_ago(2),
        schedule_interval="@daily",
    )

    dag_stg_layer = DummyOperator(
        task_id="stg",
        dag=dag_subdag)

    for i in range(5):
        item = {'task_id':'%s-task-%s' % (child_dag_name, i + 1)} 
        ops_task = PythonOperator(
            task_id='%s-task-%s' % (child_dag_name, i + 1),
            python_callable=ops_call_back,
            op_kwargs=item,
            provide_context=True,
            dag=dag_subdag
        )
        # dag_stg_layer >> dm
        ops_task >> dag_stg_layer
    return dag_subdag

def ops_call_back(ds, tomorrow_ds, **kwargs):
    print("hello sub dag")
    sql_path = kwargs["task_id"]
    print(sql_path)
# [END subdag]
