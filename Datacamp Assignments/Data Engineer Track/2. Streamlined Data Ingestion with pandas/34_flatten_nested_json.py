# Load json_normalize()
from pandas.io.json import json_normalize

# Isolate the JSON data from the API response
data = response.json()

'''
In [8]: data['businesses'][0:1]
Out[8]: 
[{'alias': 'white-noise-brooklyn-2',
  'categories': [{'alias': 'coffee', 'title': 'Coffee & Tea'}],
  'coordinates': {'latitude': 40.6893582571548,
   'longitude': -73.9884148165584},
  'display_phone': '',
  'distance': 1856.1270355932324,
  'id': 'CBmrwh7jHn88M4v8Q9Qyyg',
  'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/rcNRZr7mVv-vb-PKMMrsLw/o.jpg',
  'is_closed': False,
  'location': {'address1': '71 Smith St',
   'address2': '',
   'address3': None,
   'city': 'Brooklyn',
   'country': 'US',
   'display_address': ['71 Smith St', 'Brooklyn, NY 11201'],
   'state': 'NY',
   'zip_code': '11201'},
  'name': 'White Noise',
  'phone': '',
  'rating': 4.5,
  'review_count': 15,
  'transactions': [],
'''

# Flatten business data into a data frame, replace separator
cafes = json_normalize(data["businesses"],
             sep='_')

# View data
print(cafes.head())

'''
<script.py> output:
                             alias                                         categories  coordinates_latitude  coordinates_longitude   display_phone  ...  price rating review_count  transactions  \
    0       white-noise-brooklyn-2     [{'alias': 'coffee', 'title': 'Coffee & Tea'}]             40.689358             -73.988415                  ...    NaN    4.5           15            []   
    1          devocion-brooklyn-3  [{'alias': 'coffee', 'title': 'Coffee & Tea'},...             40.688570             -73.983340  (718) 285-6180  ...     $$    4.0           73            []   
    2   coffee-project-ny-new-york     [{'alias': 'coffee', 'title': 'Coffee & Tea'}]             40.726990             -73.989220  (212) 228-7888  ...     $$    4.5          630            []   
    3  spreadhouse-cafe-new-york-3  [{'alias': 'cafes', 'title': 'Cafes'}, {'alias...             40.718910             -73.985850  (646) 524-6353  ...      $    4.0          380            []   
    4             usagi-ny-dumbo-7  [{'alias': 'bookstores', 'title': 'Bookstores'...             40.703830             -73.986910  (718) 801-8037  ...     $$    4.5           57            []   
    
                                                     url  
    0  https://www.yelp.com/biz/white-noise-brooklyn-...  
    1  https://www.yelp.com/biz/devocion-brooklyn-3?a...  
    2  https://www.yelp.com/biz/coffee-project-ny-new...  
    3  https://www.yelp.com/biz/spreadhouse-cafe-new-...  
    4  https://www.yelp.com/biz/usagi-ny-dumbo-7?adju...  
    
    [5 rows x 24 columns]

Notice that by accessing data['businesses'] we're already working one level down the nested structure. 
data itself could be flattened with json_normalize()
'''

'''
In [6]: json_normalize?
Signature: json_normalize(data, record_path=None, meta=None, meta_prefix=None, record_prefix=None, errors='raise', sep='.')
Docstring:
Normalize semi-structured JSON data into a flat table.

Parameters
----------
data : dict or list of dicts
    Unserialized JSON objects
record_path : string or list of strings, default None
    Path in each object to list of records. If not passed, data will be
    assumed to be an array of records
meta : list of paths (string or list of strings), default None
    Fields to use as metadata for each record in resulting table
meta_prefix : string, default None
record_prefix : string, default None
    If True, prefix records with dotted (?) path, e.g. foo.bar.field if
    path to records is ['foo', 'bar']
errors : {'raise', 'ignore'}, default 'raise'

    * 'ignore' : will ignore KeyError if keys listed in meta are not
      always present
    * 'raise' : will raise KeyError if keys listed in meta are not
      always present

    .. versionadded:: 0.20.0

sep : string, default '.'
    Nested records will generate names separated by sep,
    e.g., for sep='.', { 'foo' : { 'bar' : 0 } } -> foo.bar

    .. versionadded:: 0.20.0

Returns
-------
frame : DataFrame

'''