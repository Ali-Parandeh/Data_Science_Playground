# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)

# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np

print(baseball_df.head())

%%timeit # Use the W array and G array to calculate win percentages
... win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)
... 
... # Append a new column to baseball_df that stores all win percentages
... baseball_df['WP'] = win_percs_np

'''
785 us +- 43.3 us per loop (mean +- std. dev. of 7 runs, 1000 loops each)
'''

%%timeit win_percs_list = []
... 
... for i in range(len(baseball_df)):
...     row = baseball_df.iloc[i]
... 
...     wins = row['W']
...     games_played = row['G']
... 
...     win_perc = calc_win_perc(wins, games_played)
... 
...     win_percs_list.append(win_perc)
... 
... baseball_df['WP'] = win_percs_list

'''
1.73 s +- 195 ms per loop (mean +- std. dev. of 7 runs, 1 loop each)
'''