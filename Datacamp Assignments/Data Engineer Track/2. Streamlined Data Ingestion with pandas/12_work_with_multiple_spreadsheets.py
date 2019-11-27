# Create an empty data frame
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for df in responses.values():
  # Print the number of rows being added
  print("Adding {} rows".format(df.shape[0]))
  # Append df to all_responses, assign result
  all_responses = all_responses.append(df)

# Graph employment statusesw in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()

'''
<script.py> output:
    Adding 1000 rows
    Adding 1000 rows

You compiled similar spreadsheets into one dataset. 
This method works well when you know your spreadsheets use the same column names. 
If they don't, you can end up with lots of NA values where column names don't align.


In [7]: responses.keys()
Out[7]: odict_keys(['2016', '2017'])
'''