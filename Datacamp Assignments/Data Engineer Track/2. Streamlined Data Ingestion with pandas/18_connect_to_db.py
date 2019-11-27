# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine

# Create the database engine
engine = create_engine('sqlite:///data.db')

# View the tables in the database
print(engine.table_names())

'''
<script.py> output:
    ['boro_census', 'hpd311calls', 'weather']

sqlalchemy is a powerful library that can be used with pandas to both query databases for analysis and write results back to database tables.
'''