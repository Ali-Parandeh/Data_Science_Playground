run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    
    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    run_diffs.append(run_diff)

# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df)

'''
  Team League  Year   RS   RA    W    G  Playoffs   RD
0  NYY     AL  2012  804  668   95  162         1  136
1  NYY     AL  2011  867  657   97  162         1  210
2  NYY     AL  2010  859  693   95  162         1  166
3  NYY     AL  2009  915  753  103  162         1  162
4  NYY     AL  2008  789  727   89  162         0   62
'''


# In what year within your DataFrame did the New York Yankees have the highest run differential?

In [1]: yankees_df[yankees_df.RD  == yankees_df.RD.max()]

'''
   Team League  Year   RS   RA    W    G  Playoffs   RD
14  NYY     AL  1998  965  656  114  162         1  309
'''

'''
You used .itertuples() to help the Yankees calculate run differentials. 
Remember, using .itertuples() is just like using .iterrows() except it tends to be faster. 
You also have to use a dot reference when looking up attributes with .itertuples().

You found that the Yankees' highest run differential was in 1998. 
Did you know they actually hold the record for the highest run differential 
in an MLB season (411 in the year 1939 where they scored 967 runs and allowed 556)? Wow!
'''