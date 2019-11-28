# Load other business attributes and set meta prefix
from pandas.io.json import json_normalize


flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories",
                    		meta=['name', 
                                  'alias',  
                                  'rating',
                          		  ['coordinates', 'latitude'], 
                          		  ['coordinates', 'longitude']],
                    		meta_prefix='biz_')


# View the data
print(flat_cafes.head())


'''
<script.py> output:
                  alias              title           biz_name                   biz_alias  biz_rating  biz_coordinates_latitude  biz_coordinates_longitude
    0            coffee       Coffee & Tea        White Noise      white-noise-brooklyn-2         4.5                 40.689358                 -73.988415
    1            coffee       Coffee & Tea           Devocion         devocion-brooklyn-3         4.0                 40.688570                 -73.983340
    2  coffeeroasteries  Coffee Roasteries           Devocion         devocion-brooklyn-3         4.0                 40.688570                 -73.983340
    3             cafes              Cafes           Devocion         devocion-brooklyn-3         4.0                 40.688570                 -73.983340
    4            coffee       Coffee & Tea  Coffee Project NY  coffee-project-ny-new-york         4.5                 40.726990                 -73.989220

Naming meta columns can get tedious for datasets with many attributes, 
and code is susceptible to breaking if column names or nesting levels change. 
In such cases, you may have to write a custom function and 
employ techniques like recursion to handle the data.

'''