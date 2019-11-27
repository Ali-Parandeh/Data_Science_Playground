try:
  # Set warn_bad_lines to issue warnings about bad records
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv", 
                     error_bad_lines=False, 
                     warn_bad_lines = True)
  
  # View first 5 records
  print(data.head())
  
except pd.io.common.CParserError:
    print("Your data contained rows that could not be parsed.")


'''
<script.py> output:
    Skipping line 5: expected 147 fields, saw 148
    Skipping line 9: expected 147 fields, saw 148
    Skipping line 51: expected 147 fields, saw 148
    
       STATEFIPS STATE  zipcode  agi_stub      N1  ...  A85300  N11901  A11901  N11902  A11902
    0         50    VT        0         1  111580  ...       0   10820    9734   88260  138337
    1         50    VT        0         2   82760  ...       0   12820   20029   68760  151729
    2         50    VT        0         3   46270  ...       0   10810   24499   34600   90583
    3         50    VT        0         5   39530  ...       0   12500   67761   23320  103034
    4         50    VT        0         6    9620  ...   20428    3900   93123    2870   39425
    
    [5 rows x 147 columns]
'''