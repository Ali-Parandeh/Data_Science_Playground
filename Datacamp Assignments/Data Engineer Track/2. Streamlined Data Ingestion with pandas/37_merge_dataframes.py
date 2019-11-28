'''
In [1]: crosswalk.head(1)
Out[1]: 
  zipcode        ziptype postalcity  zcta5  bcode note   puma                                      pumaname
0   10001  ZIP Code area   New York  10001  36061  NaN  03807  Chelsea, Clinton & Midtown Business District
'''

'''
In [2]: pop_data.head(1)
Out[2]: 
   geo_type                                          geog_name   puma borough  total_pop_estimate  total_pop_moe
0  PUMA2010  NYC-Bronx Community District 8--Riverdale, Fie...  03701   Bronx              109810           2134
'''

'''
In [5]: cafes.head(1)
Out[5]: 
                        alias                                      categories  coordinates_latitude  coordinates_longitude   display_phone  ...  price rating review_count  transactions  \
0  coffee-project-ny-new-york  [{'alias': 'coffee', 'title': 'Coffee & Tea'}]              40.72699              -73.98922  (212) 228-7888  ...     $$    4.5          615            []   
                                                 url  
0  https://www.yelp.com/biz/coffee-project-ny-new...  

[1 rows x 24 columns]
'''


print(pd.merge(cafes, crosswalk, left_on= 'location_zip_code', right_on='zipcode').head(1))

'''
                        alias                                      categories  coordinates_latitude  coordinates_longitude   display_phone  ...  zcta5  bcode note   puma                     pumaname
0  coffee-project-ny-new-york  [{'alias': 'coffee', 'title': 'Coffee & Tea'}]              40.72699              -73.98922  (212) 228-7888  ...  10003  36061  NaN  03809  Chinatown & Lower East Side

[1 rows x 32 columns]
'''

print(pd.merge(crosswalk, pop_data, on='puma').head(1))

'''
  zipcode        ziptype postalcity  zcta5  bcode  ...  geo_type                                          geog_name    borough total_pop_estimate total_pop_moe
0   10001  ZIP Code area   New York  10001  36061  ...  PUMA2010  NYC-Manhattan Community District 4 & 5--Chelse...  Manhattan             149309          3412

[1 rows x 13 columns]
'''

# Merge crosswalk into cafes on their zip code fields
cafes_with_pumas = cafes.merge(crosswalk, left_on ='location_zip_code', right_on='zipcode')


# Merge pop_data into cafes_with_pumas on puma field
cafes_with_pop = cafes_with_pumas.merge(pop_data, on='puma')

# View the data
print(cafes_with_pop.head())

'''
<script.py> output:
                            alias                                         categories  coordinates_latitude  coordinates_longitude   display_phone  ...  geo_type  \
    0  coffee-project-ny-new-york     [{'alias': 'coffee', 'title': 'Coffee & Tea'}]             40.726990             -73.989220  (212) 228-7888  ...  PUMA2010   
    1   saltwater-coffee-new-york     [{'alias': 'coffee', 'title': 'Coffee & Tea'}]             40.730458             -73.983918  (917) 881-2245  ...  PUMA2010   
    2   daily-provisions-new-york  [{'alias': 'cafes', 'title': 'Cafes'}, {'alias...             40.737680             -73.987668  (212) 488-1505  ...  PUMA2010   
    3              mud-new-york-3  [{'alias': 'coffee', 'title': 'Coffee & Tea'},...             40.729050             -73.986680  (212) 228-9074  ...  PUMA2010   
    4  coffee-project-ny-new-york     [{'alias': 'coffee', 'title': 'Coffee & Tea'}]             40.726990             -73.989220  (212) 228-7888  ...  PUMA2010   
    
                                               geog_name    borough  total_pop_estimate total_pop_moe  
    0  NYC-Manhattan Community District 3--Chinatown ...  Manhattan              160709          3289  
    1  NYC-Manhattan Community District 3--Chinatown ...  Manhattan              160709          3289  
    2  NYC-Manhattan Community District 3--Chinatown ...  Manhattan              160709          3289  
    3  NYC-Manhattan Community District 3--Chinatown ...  Manhattan              160709          3289  
    4  NYC-Manhattan Community District 3--Chinatown ...  Manhattan              160709          3289  
    
    [5 rows x 37 columns]

You've built a pretty sophisticated pipeline that translates geographies to link data 
from multiple sources. While postal codes are a commonly used areal unit, 
there are often more meaningful ways to group spatial data, such as by neighborhood here.
'''