# Function to extract table to a pandas DataFrame
def extract_table_to_pandas(tablename, db_engine):
    query = "SELECT * FROM {}".format(tablename)
    return pd.read_sql(query, db_engine)

# Connect to the database using the connection URI
# The connection URI can also be a link to an external database. 
# Pulling in full tables can result in loads of network traffic.
connection_uri = "postgresql://repl:password@localhost:5432/pagila" 
db_engine = sqlalchemy.create_engine(connection_uri)

# Extract the film table into a pandas DataFrame
extract_table_to_pandas('film', db_engine)

'''       film_id                 title                                        description  release_year  language_id  ... replacement_cost  rating                      last_update  \
# 0          1      ACADEMY DINOSAUR  A Epic Drama of a Feminist And a Mad Scientist...          2006            1  ...            20.99      PG 2017-09-10 17:46:03.905795+00:00    '''


# Extract the customer table into a pandas DataFrame
extract_table_to_pandas('customer', db_engine)

'''      customer_id  store_id first_name  last_name                                  email  address_id  activebool create_date               last_update  active
0              1         1       MARY      SMITH          MARY.SMITH@sakilacustomer.org           5        True  2017-02-14 2017-02-15 09:57:20+00:00       1 '''