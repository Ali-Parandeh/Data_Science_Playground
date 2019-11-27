# Create query to get temperature and precipitation by month
query = """
SELECT month, 
        MAX(tmax), 
        MIN(tmin),
        SUM(prcp)
  FROM weather 
 GROUP BY month;
"""

# Get data frame of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)


'''
<script.py> output:
          month  MAX(tmax)  MIN(tmin)  SUM(prcp)
    0  December         61          9       2.21
    1  February         78         16       5.83
    2   January         61          5       2.18
    3     March         62         27       5.17

Aggregate functions can be a useful way to summarize large datasets. 
Different database management systems even have SQL functions for statistics 
like standard deviation and percentiles, though these are non-standard and vendor-specific.
'''