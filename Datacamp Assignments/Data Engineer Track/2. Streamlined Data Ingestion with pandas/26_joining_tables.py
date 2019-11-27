# Query to join weather to call records by date columns
query = """
SELECT * 
  FROM hpd311calls
  JOIN weather 
  ON hpd311calls.created_date = weather.date;
"""

# Create data frame of joined tables
calls_with_weather = pd.read_sql(query, engine)

# View the data frame to make sure all columns were joined
print(calls_with_weather.head())


'''
<script.py> output:
      unique_key created_date agency  complaint_type incident_zip  ... prcp snow tavg tmax tmin
    0   38070822   01/01/2018    HPD  HEAT/HOT WATER        10468  ...  0.0  0.0        19    7
    1   38065299   01/01/2018    HPD        PLUMBING        10003  ...  0.0  0.0        19    7
    2   38066653   01/01/2018    HPD  HEAT/HOT WATER        10452  ...  0.0  0.0        19    7
    3   38070264   01/01/2018    HPD  HEAT/HOT WATER        10032  ...  0.0  0.0        19    7
    4   38072466   01/01/2018    HPD  HEAT/HOT WATER        11213  ...  0.0  0.0        19    7
    
    [5 rows x 21 columns]


The joins you perform only return records whose key values appear in both tables, 
which is why the resulting data frames have values for all columns. 
But there are other kinds of joins that can return records that don't have a match.
'''