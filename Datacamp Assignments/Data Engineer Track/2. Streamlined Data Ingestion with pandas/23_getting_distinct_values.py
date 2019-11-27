# Create query for unique combinations of borough and complaint_type
query = """
SELECT DISTINCT borough, complaint_type
  FROM hpd311calls;
"""

# Load results of query to a data frame
issues_and_boros = pd.read_sql(query, engine)

# Check assumption about issues and boroughs
print(issues_and_boros)

'''
<script.py> output:
              borough          complaint_type
    0           BRONX          HEAT/HOT WATER
    1       MANHATTAN                PLUMBING
    2       MANHATTAN          HEAT/HOT WATER
                ...                 ...
    61      MANHATTAN                ELEVATOR
    62       BROOKLYN        OUTSIDE BUILDING
    63  STATEN ISLAND                  SAFETY
    64  STATEN ISLAND        OUTSIDE BUILDING
    
    [65 rows x 2 columns]
    

'''