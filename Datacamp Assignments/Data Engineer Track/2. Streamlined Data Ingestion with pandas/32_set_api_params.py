import pandas as pd
import requests

api_url = "https://api.yelp.com/v3/businesses/search"

headers = {'Authorization': 'Bearer {}'.format('api_key')}

# Create dictionary to query API for cafes in NYC
parameters = {'term': 'cafe',
          	  'location': 'NYC'}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                params = parameters,
                headers = headers)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a data frame and print head
cafes = pd.DataFrame(data['businesses'])
print(cafes.head())


'''
<script.py> output:
                             alias                                         categories                                        coordinates   display_phone     distance  ... price rating  review_count  \
    0       white-noise-brooklyn-2     [{'alias': 'coffee', 'title': 'Coffee & Tea'}]  {'latitude': 40.6893582571548, 'longitude': -7...                  1856.127036  ...   NaN    4.5            15   
    1          devocion-brooklyn-3  [{'alias': 'coffee', 'title': 'Coffee & Tea'},...     {'latitude': 40.68857, 'longitude': -73.98334}  (718) 285-6180  2087.816949  ...    $$    4.0            73   
    2   coffee-project-ny-new-york     [{'alias': 'coffee', 'title': 'Coffee & Tea'}]     {'latitude': 40.72699, 'longitude': -73.98922}  (212) 228-7888  2435.843426  ...    $$    4.5           630   
    3  spreadhouse-cafe-new-york-3  [{'alias': 'cafes', 'title': 'Cafes'}, {'alias...     {'latitude': 40.71891, 'longitude': -73.98585}  (646) 524-6353  1657.232800  ...     $    4.0           380   
    4             usagi-ny-dumbo-7  [{'alias': 'bookstores', 'title': 'Bookstores'...     {'latitude': 40.70383, 'longitude': -73.98691}  (718) 801-8037   635.781863  ...    $$    4.5            57   
    
      transactions                                                url  
    0           []  https://www.yelp.com/biz/white-noise-brooklyn-...  
    1           []  https://www.yelp.com/biz/devocion-brooklyn-3?a...  
    2           []  https://www.yelp.com/biz/coffee-project-ny-new...  
    3           []  https://www.yelp.com/biz/spreadhouse-cafe-new-...  
    4           []  https://www.yelp.com/biz/usagi-ny-dumbo-7?adju...  
    
    [5 rows x 16 columns]

Notice that some of the values are themselves dictionaries, making them hard to analyze
'''