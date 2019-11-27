repl:~$ cat dag.py

# from airflow.models import DAG
# dag = DAG(dag_id="sample", schedule_interval="0 0 * * *")


repl:~/airflow$ head airflow.cfg

# [core]
# The home folder for airflow, default is ~/airflow
# airflow_home = /home/repl/airflow

# The folder where your airflow pipelines live, most likely a
# subfolder in a code repository
# This path must be absolute
# dags_folder = /home/repl/airflow/dags

# The folder where airflow should store its log files

repl:~$ cat airflow/dags/dag_recommendations.py

# from airflow.models import DAG
# from airflow.operators.python_operator import PythonOperator
# def etl(): pass
# db_engines = {}
# dag = DAG(dag_id="recommendations",
#           schedule_interval="0 0 * * *")
# task_recommendations = PythonOperator(
#     task_id="recommendations_task",
#     python_callable=etl,
#     op_kwargs={"db_engines":db_engines},
# )
