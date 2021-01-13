import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator

from airflow.hooks.postgres_hook import PostgresHook


from pandahouse.core import to_clickhouse, read_clickhouse
dag = DAG(
    dag_id="demo_200_postgres_clickhouse",
    start_date=airflow.utils.dates.days_ago(3),
    # schedule_interval="@hourly",
    # max_active_runs=1,
    # default_args={"depends_on_past": True},
    # template_searchpath="/tmp",
)


def load():
    #create  a PostgresHook option using the 'example' connection
    db_hook = PostgresHook('my_postgres_conn')
    df = db_hook.get_pandas_df('SELECT * FROM pageview_counts')
    print(df.head())

    connection = {'host': 'http://clh:8123',
                'database': 'tutorial'}
    affected_rows = to_clickhouse(df, table='pageview_counts', connection=connection)     
    print(affected_rows)
    
    
load_task = PythonOperator(task_id='load',
                           python_callable=load,
                            dag=dag,
                           
                           )
