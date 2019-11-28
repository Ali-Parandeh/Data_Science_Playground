import pandas as pd
import requests

api_url = "https://api.yelp.com/v3/businesses/search"

headers = {'Authorization': 'Bearer {}'.format('api_key')}
params = {'location': 'NYC', 'term': 'cafe'}

# Get data about NYC cafes from the Yelp API
response = requests.get(api_url, 
                headers=headers, 
                params=params)

# Extract JSON data from the response
data = response.json()

'''
In [14]: data.keys()
Out[14]: dict_keys(['businesses', 'total', 'region'])
'''

# Load data to a data frame
cafes = pd.DataFrame(data['businesses'])

# View the data's dtypes
print(cafes.dtypes)

'''
<script.py> output:
    alias             object
    categories        object
    coordinates       object
    display_phone     object
    distance         float64
    id                object
    image_url         object
    is_closed           bool
    location          object
    name              object
    phone             object
    price             object
    rating           float64
    review_count       int64
    transactions      object
    url               object
    dtype: object

Check the response format whenever you work with a new API -- 
chances are the data you need is nested under a dictionary key, like here.
One important note: to avoid problems like hitting usage limits or
potential connection issues, this course mimics API requests in the background, 
and, if you set up the code right, returns the corresponding response object. 
The code you'll write looks exactly like what you would use to interact with the actual API
'''