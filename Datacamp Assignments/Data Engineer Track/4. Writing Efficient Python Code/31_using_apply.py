def text_playoffs(num_playoffs): 
    if num_playoffs == 1:
        return 'Yes'
    else:
        return 'No' 


rays_df.head()
'''
       RS   RA   W  Playoffs
2012  697  577  90         0
2011  707  614  91         1
2010  802  649  96         1
2009  803  754  84         0
2008  774  671  97         1
'''

# Gather sum of all columns
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)

'''
RS          3783
RA          3265
W            458
Playoffs       3
dtype: int64
'''

# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)

'''
2012    1274
2011    1321
2010    1451
2009    1557
2008    1445
dtype: int64
'''

# Convert numeric playoffs to text
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)

'''
2012     No
2011    Yes
2010    Yes
2009     No
2008    Yes
dtype: object
'''

'''
The .apply() method let's you apply functions to 
all rows or columns of a DataFrame by specifying an axis.

If you've been using pandas for some time, 
you may have noticed that a better way to find 
these stats would use the pandas built-in .sum() method.

You could have used rays_df.sum(axis=0) to get 
columnar sums and rays_df[['RS', 'RA']].sum(axis=1) to get row sums.

You could have also used .apply() directly on a 
Series (or column) of the DataFrame. For example, 
you could use rays_df['Playoffs'].apply(text_playoffs) 
to convert the 'Playoffs' column to text.
'''