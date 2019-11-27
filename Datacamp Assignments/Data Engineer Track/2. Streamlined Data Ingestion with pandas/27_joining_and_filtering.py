# Query to get water leak calls and daily precipitation
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
    ON hpd311calls.created_date = weather.date
  WHERE hpd311calls.complaint_type = 'WATER LEAK';
"""

# Load query results into the leak_calls data frame
leak_calls = pd.read_sql(query, engine)

# View the data frame
print(leak_calls.head())

'''
<script.py> output:
      unique_key created_date agency complaint_type incident_zip         incident_address community_board   borough  prcp
    0   38074305   01/01/2018    HPD     WATER LEAK        11212     1026 WILLMOHR STREET     17 BROOKLYN  BROOKLYN   0.0
    1   38078748   01/01/2018    HPD     WATER LEAK        10458       2700 MARION AVENUE        07 BRONX     BRONX   0.0
    2   38081097   01/01/2018    HPD     WATER LEAK        11221  192 MALCOLM X BOULEVARD     03 BROOKLYN  BROOKLYN   0.0
    3   38077874   01/01/2018    HPD     WATER LEAK        11418    129-11 JAMAICA AVENUE       09 QUEENS    QUEENS   0.0
    4   38081110   01/01/2018    HPD     WATER LEAK        11420        111-17 133 STREET       10 QUEENS    QUEENS   0.0

How you go about constructing a complicated SQL query can depend on what operators you need and how big the tables you're working with are. 
If your tables are very big, you may decide to filter or aggregate the data first before attempting a join.

'''