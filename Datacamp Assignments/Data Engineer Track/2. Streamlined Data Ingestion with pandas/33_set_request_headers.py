import pandas as pd
import requests

api_url = "https://api.yelp.com/v3/businesses/search"

# Create dictionary that passes Authorization and key string
headers = {'Authorization': "Bearer {}".format(api_key)}

# Query the Yelp API with headers and params set
response = requests.get(api_url, params = params, headers = headers)



# Extract JSON data from response
data = response.json()

# Load "businesses" values to a data frame and print names
cafes = pd.DataFrame(data['businesses'])
print(cafes.name)

'''
<script.py> output:
    0             Coffee Project NY
    1                Urban Backyard
    2              Saltwater Coffee
    3                 Bird & Branch
    4                  Bibble & Sip
    5             Coffee Project NY
    6                        Burrow
    7                   Cafe Patoro
    8                     Sweatshop
    9                       Round K
    10               Kobrick Coffee
    11            Kaigo Coffee Room
    12              Absolute Coffee
    13                     Devocion
    14                The Uncommons
    15                      Butler 
    16              Cafe Hanamizuki
    17    Brooklyn Roasting Company
    18             Takahachi Bakery
    19              Happy Bones NYC
    Name: name, dtype: object

Great work! API keys are employed to track and moderate API usage. 
Be sure to keep keys private -- unscrupulous developers use others' 
keys to get around usage limits.
'''