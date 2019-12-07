import numpy as np

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

# Display the first five rows of the DataFrame
print(dbacks_df.head())

'''
      Team League  Year   RS   RA   W    G  Playoffs
    0  ARI     NL  2012  734  688  81  162         0
    1  ARI     NL  2011  731  662  94  162         1
    2  ARI     NL  2010  713  836  65  162         0
    3  ARI     NL  2009  720  782  70  162         0
    4  ARI     NL  2008  720  706  82  162         0
'''

# Create a win percentage Series 
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

'''
    0     0.50
    1     0.58
    2     0.40
    3     0.43
    4     0.51
    5     0.56
    6     0.47
    7     0.48
    8     0.31
    9     0.52
    10    0.60
    11    0.57
    12    0.52
    13    0.62
    14    0.40
    dtype: float64
'''

# Append a new column to dbacks_df
dbacks_df['WP'] = win_percs
print(dbacks_df, '\n')

'''
       Team League  Year   RS   RA    W    G  Playoffs    WP
    0   ARI     NL  2012  734  688   81  162         0  0.50
    1   ARI     NL  2011  731  662   94  162         1  0.58
    2   ARI     NL  2010  713  836   65  162         0  0.40
    3   ARI     NL  2009  720  782   70  162         0  0.43
    4   ARI     NL  2008  720  706   82  162         0  0.51
'''

# Display dbacks_df where WP is greater than 0.50
print(dbacks_df[dbacks_df['WP'] >= 0.50])

'''
       Team League  Year   RS   RA    W    G  Playoffs    WP
    0   ARI     NL  2012  734  688   81  162         0  0.50
    1   ARI     NL  2011  731  662   94  162         1  0.58
    4   ARI     NL  2008  720  706   82  162         0  0.51
    5   ARI     NL  2007  712  732   90  162         1  0.56
    9   ARI     NL  2003  717  685   84  162         0  0.52
    10  ARI     NL  2002  819  674   98  162         1  0.60
    11  ARI     NL  2001  818  677   92  162         1  0.57
    12  ARI     NL  2000  792  754   85  162         0  0.52
    13  ARI     NL  1999  908  676  100  162         1  0.62
'''

'''
Using the .apply() method with a lambda function allows 
you to apply a function to a DataFrame without the need to write a for loop.

Sadly, the second manager was correct. In the year 2012, 2008, 2003, 
and 2000 the Arizona Diamondbacks had a win percentage greater 
than or equal to 0.50, but still did not make the playoffs.
'''