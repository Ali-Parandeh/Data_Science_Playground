# Query to get heat/hot water call counts by created_date
query = """
SELECT hpd311calls.created_date, 
       COUNT(*)
  FROM hpd311calls 
  WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER'
  GROUP BY hpd311calls.created_date;"""

# Query database and save results as df
df = pd.read_sql(query, engine)

# View first 5 records
print(df.head())


'''
<script.py> output:
      created_date  COUNT(*)
    0   01/01/2018      4597
    1   01/02/2018      4362
    2   01/03/2018      3045
    3   01/04/2018      3374
    4   01/05/2018      4333
'''


# Modify query to join tmax and tmin from weather by date
query = """
SELECT hpd311calls.created_date, 
	   COUNT(*), 
       weather.tmax,
       weather.tmin
  FROM hpd311calls 
       JOIN weather
       ON hpd311calls.created_date = weather.date
 WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER' 
 GROUP BY hpd311calls.created_date;"""

# Query database and save results as df
df = pd.read_sql(query, engine)

# View first 5 records
print(df.head())


'''
<script.py> output:
      created_date  COUNT(*)  tmax  tmin
    0   01/01/2018      4597    19     7
    1   01/02/2018      4362    26    13
    2   01/03/2018      3045    30    16
    3   01/04/2018      3374    29    19
    4   01/05/2018      4333    19     9

 You've just written a pretty complicated query to wrangle data. 
 While SQL joins can only be used in databases, there are analagous pandas operations to combine datasets
'''