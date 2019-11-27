# Load csv with no additional arguments
data = pd.read_csv("vt_tax_data_2016.csv")

# Print the data types
print(data.dtypes)

''' 
<script.py> output:
    STATEFIPS      int64
    N00700         int64
                   ...  
    N85770         int64
    A85770         int64

    Length: 147, dtype: object
'''

# Create dict specifying data types for agi_stub and zipcode
data_types = {'agi_stub': 'category',
			  'zipcode': str}

# Load csv using dtype to set correct data types
data = pd.read_csv("vt_tax_data_2016.csv", dtype = data_types)

# Print data types of resulting frame
print(data.dtypes.head())


''' 
<script.py> output:
    STATEFIPS       int64
    STATE          object
    zipcode        object
    agi_stub     category
    N1              int64
    dtype: object

Setting data types at import requires becoming familiar with the data first, 
but it can save effort later on. A common workflow is to load the data and explore it, 
then write code that sets data types at import to share with colleagues or other audiences.
 '''