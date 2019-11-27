# Define the ETL function
def etl():
    
    # Returns the extracted film table as a pandas DataFrame
    film_df = extract_film_to_pandas() 
    
    # Takes a pandas DataFrame and returns the transformed DataFrame
    film_df = transform_rental_rate(film_df) 
    
    # Takes a pandas DataFrame and loads it into the film table in the data warehouse
    load_dataframe_to_film(film_df)

# Define the ETL task using PythonOperator
etl_task = PythonOperator(task_id='etl_heart_disease',
                          python_callable=etl,
                          dag=dag)

# Set the upstream to wait_for_table and sample run etl()
etl_task.set_upstream(wait_for_table)
etl()

# Experimenting with a few queries once the data pipeline has run:
pd.read_sql('SELECT age, AVG(chol) FROM heart GROUP BY age ORDER BY age' db_engine)