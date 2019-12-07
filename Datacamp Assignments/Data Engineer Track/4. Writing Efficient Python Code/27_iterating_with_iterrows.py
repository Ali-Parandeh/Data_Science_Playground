
# Iterate over pit_df and print each row
for i,row in pit_df.iterrows():
    print(row)

'''
    Team         PIT
    League        NL
    Year        2012
    RS           651
    RA           674
    W             79
    G            162
    Playoffs       0
    Name: 0, dtype: object
'''


# Iterate over pit_df and print each index variable and then each row
for i,row in pit_df.iterrows():
    print(i)
    print(row)
    print(type(row))


# Use one variable instead of two to store the result of .iterrows()
for row_tuple in pit_df.iterrows():
    print(row_tuple)


'''
   (4, Team         PIT
    League        NL
    Year        2008
    RS           735
    RA           884
    W             67
    G            162
    Playoffs       0
    Name: 4, dtype: object)
'''

# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(type(row_tuple))

'''
<class 'tuple'>
'''

'''
Since .iterrows() returns each DataFrame row as a tuple of 
(index, pandas Series) pairs, you can either split this 
tuple and use the index and row-values separately (as you 
did with for i,row in pit_df.iterrows()), or you can keep 
the result of .iterrows() in the tuple form (as you did 
with for row_tuple in pit_df.iterrows()).

If using i,row, you can access things from the row using 
square brackets (i.e., row['Team']). If using row_tuple, 
you would have to specify which element of the tuple you'd 
like to access before grabbing the team name (i.e., row_tuple[1]['Team']).

With either approach, using .iterrows() will still be 
substantially faster than using .iloc as you saw in the video.
'''