import pandas as pd


# Create data frame of next 500 rows with labeled columns
vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv", 
                       		  nrows = 500,
                       		  skiprows = 500,
                       		  header = None,
                       		  names = vt_data_first500.columns)

# View the Vermont data frames to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())

'''
The techniques you used here can also be employed to explore data before 
committing to loading all of it, to skip rows you know don't contain useful data,
or to relabel all columns in a dataset
'''

'''
In [1]: vt_data_first500.columns
Out[1]: 
Index(['STATEFIPS', 'STATE', 'zipcode', 'agi_stub', 'N1', 'mars1', 'MARS2', 'MARS4', 'PREP', 'N2',
       ...
       'N10300', 'A10300', 'N85530', 'A85530', 'N85300', 'A85300', 'N11901', 'A11901', 'N11902', 'A11902'],
      dtype='object', length=147)
'''

'''
In [2]: print(vt_data_first500.head())
   STATEFIPS STATE  zipcode  agi_stub      N1  ...  A85300  N11901  A11901  N11902  A11902
0         50    VT        0         1  111580  ...       0   10820    9734   88260  138337
1         50    VT        0         2   82760  ...       0   12820   20029   68760  151729
2         50    VT        0         3   46270  ...       0   10810   24499   34600   90583
3         50    VT        0         4   30070  ...       0    7320   21573   21300   67045
4         50    VT        0         5   39530  ...       0   12500   67761   23320  103034

[5 rows x 147 columns]
'''

'''
In [3]: print(vt_data_next500.head())
[5 rows x 147 columns]
   STATEFIPS STATE  zipcode  agi_stub   N1  ...  A85300  N11901  A11901  N11902  A11902
0         50    VT     5356         2  180  ...       0      50      76     130     212
1         50    VT     5356         3   80  ...       0      40     142      50     148
2         50    VT     5356         4   50  ...       0       0       0      30      87
3         50    VT     5356         5   80  ...       0      30     531      30     246
4         50    VT     5356         6    0  ...       0       0       0       0       0

[5 rows x 147 columns]
'''