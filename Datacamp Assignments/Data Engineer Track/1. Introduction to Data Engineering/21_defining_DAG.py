''' 
The etl() function extracts raw course and ratings data from relevant databases, 
cleans corrupt data and fills in missing value, computes average rating per 
course and creates recommendations based on the decision rules for producing 
recommendations, and finally loads the recommendations into a database.
 '''

 # Define the DAG so it runs on a daily basis
dag = DAG(dag_id="recommendations",
          schedule_interval="0 0 * * *") # runs daily at 00:00.

# Make sure `etl()` is called in the operator. Pass the correct kwargs.
task_recommendations = PythonOperator(
    task_id="recommendations_task",
    python_callable=etl,
    op_kwargs={"db_engines": db_engines}, # will be filled in as kwargs in the fucntion callable
)