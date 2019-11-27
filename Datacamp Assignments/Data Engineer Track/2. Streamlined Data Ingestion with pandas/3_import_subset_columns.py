import pandas as pd

''' 
There is a saying that rows are cheap, but columns are expensive. 
Limiting datasets to only variables of interest makes them more 
manageable and streamlines pipelines, but make sure you aren't losing 
confounding data in the process.

 '''

# Create list of columns to use
cols = ['zipcode', 'agi_stub', 'mars1', 'MARS2', 'NUMDEP']

# Create data frame from csv using only selected columns
data = pd.read_csv("vt_tax_data_2016.csv", usecols = cols)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())

''' 
<script.py> output:
              zipcode   mars1  MARS2  NUMDEP
    agi_stub                                
    1         1439444  170320  28480   52490
    2         1439444  104000  37690   64660
    3         1439444   39160  45390   47330
    4         1439444   11670  44410   37760
    5         1439444    7820  67750   60730
    6         1439444    1210  16340   16300
 '''