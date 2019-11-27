# Create database engine for data.db
engine = create_engine('sqlite:///data.db')

# Write query to get date, tmax, and tmin from weather
query = """
SELECT date, 
       tmax, 
       tmin
  FROM weather;
"""

# Make a data frame by passing query and engine to read_sql()
temperatures = pd.read_sql(query, engine)

# View the resulting data frame
print(temperatures)

'''
script.py> output:
               date  tmax  tmin
    0    12/01/2017    52    42
    1    12/02/2017    48    39
    2    12/03/2017    48    42
    3    12/04/2017    51    40
            ...
    119  03/30/2018    62    44
    120  03/31/2018    58    39
    
    [121 rows x 3 columns]


Selecting columns is useful when you only want a few columns from a table. 
If you want most of the columns, it may be easier to load them all and then use pandas to drop unwanted columns.

'''