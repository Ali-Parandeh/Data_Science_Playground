# Create query for records with max temps <= 32 or snow >= 1
query = """
SELECT *
  FROM weather
  WHERE tmax <= 32
  OR snow >= 1;
"""

# Query database and assign result to wintry_days
wintry_days = pd.read_sql(query, engine)

# View summary stats about the temperatures
print(wintry_days.describe())

'''
<script.py> output:
               latitude     longitude     elevation       awnd      prcp       snow       tmax       tmin
    count  2.500000e+01  2.500000e+01  2.500000e+01  25.000000  25.00000  25.000000  25.000000  25.000000
    mean   4.077898e+01 -7.396925e+01  4.270000e+01   7.739600   0.17600   1.332000  27.320000  17.160000
    std    7.251946e-15  1.450389e-14  7.251946e-15   2.621778   0.36947   2.685256   7.122266   7.673982
    min    4.077898e+01 -7.396925e+01  4.270000e+01   3.130000   0.00000   0.000000  13.000000   5.000000
    25%    4.077898e+01 -7.396925e+01  4.270000e+01   5.820000   0.00000   0.000000  22.000000  11.000000
    50%    4.077898e+01 -7.396925e+01  4.270000e+01   7.830000   0.00000   0.000000  28.000000  17.000000
    75%    4.077898e+01 -7.396925e+01  4.270000e+01   9.170000   0.09000   1.200000  31.000000  20.000000
    max    4.077898e+01 -7.396925e+01  4.270000e+01  12.970000   1.41000   9.800000  40.000000  33.000000
'''