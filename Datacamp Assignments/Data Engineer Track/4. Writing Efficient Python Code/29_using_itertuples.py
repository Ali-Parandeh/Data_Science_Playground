'''
Remember, .itertuples() returns each DataFrame row as a special data type called a namedtuple
'''

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
    print(row)

    '''
    Pandas(Index=0, Team='TEX', League='AL', Year=2012, RS=808, RA=707, W=93, G=162, Playoffs=1)
    Pandas(Index=1, Team='TEX', League='AL', Year=2011, RS=855, RA=677, W=96, G=162, Playoffs=1)
    '''

    i = row.Index
    year = row.Year
    wins = row.W
  
    # Check if rangers made Playoffs (1 means yes; 0 means no)
    if row.W == 1:
        print(i, year, wins)

        '''
        0 2012 93
        1 2011 96
        2 2010 90
        3 2009 87
        '''

'''
You're getting the hang of using .itertuples(). 
Remember, you need to use the dot syntax for referencing an attribute in a namedtuple.

You can create a new variable using a row's dot reference 
(as you did when storing row.Index as the variable i). 
Or you can use the row's dot reference directly to perform 
calculations and checks. Notice that you did not have to save row.
Playoffs to a new variable in your check statement (you were able to use row.Playoffs directly in your check).

Did you notice the pattern in the Texas Rangers playoff appearances? 
Only six appearances and two distinct sets of groupings 
(one from 2010 - 2012 and one from 1996 - 1999).
'''