# Load pandas as pd
import pandas as pd

# Load the daily report to a data frame
pop_in_shelters = pd.read_json('dhs_daily_report.json')

# View summary stats about pop_in_shelters
print(pop_in_shelters.describe())


'''
<script.py> output:
           adult_families_in_shelter  adults_in_families_with_children_in_shelter  children_in_families_with_children_in_shelter  families_with_children_in_shelter  \
    count                1000.000000                                  1000.000000                                    1000.000000                         1000.00000   
    mean                 2074.955000                                 16487.932000                                   23273.873000                        11588.83500   
    std                   148.020238                                   848.363772                                     926.243984                          626.41371   
    min                  1796.000000                                 14607.000000                                   21291.000000                        10261.00000   
    25%                  1906.000000                                 15831.500000                                   22666.000000                        11060.00000   
    50%                  2129.000000                                 16836.000000                                   23285.500000                        11743.00000   
    75%                  2172.250000                                 17118.250000                                   23610.000000                        12146.00000   
    max                  2356.000000                                 17733.000000                                   25490.000000                        12413.00000   
    
           individuals_in_adult_families_in_shelter  ...  total_adults_in_shelter  total_children_in_shelter  total_individuals_in_families_with_children_in_shelter_  total_individuals_in_shelter  \
    count                                1000.00000  ...              1000.000000                1000.000000                                        1000.000000                         1000.000000   
    mean                                 4368.05400  ...             32328.857000               23273.882000                                       39761.805000                        55602.739000   
    std                                   299.05424  ...              2150.583637                 926.247187                                        1677.972788                         2745.294235   
    min                                  3811.00000  ...             28127.000000               21291.000000                                       35902.000000                        49462.000000   
    25%                                  4026.00000  ...             30184.250000               22666.000000                                       38775.500000                        53196.500000   
    50%                                  4473.00000  ...             33142.000000               23285.500000                                       40026.000000                        56713.500000   
    75%                                  4567.00000  ...             33940.750000               23610.000000                                       40529.500000                        57872.250000   
    max                                  4944.00000  ...             35294.000000               25490.000000                                       43208.000000                        59068.000000   
    
           total_single_adults_in_shelter  
    count                      1000.00000  
    mean                      11472.88000  
    std                        1113.66412  
    min                        9610.00000  
    25%                       10381.75000  
    50%                       11633.50000  
    75%                       12437.50000  
    max                       13270.00000  
    
    [8 rows x 12 columns]

When getting data from a URL, like with open data portals, 
be mindful of how much data is being pulled and how often you do it. Requesting lots of data can strain shared resources.

'''