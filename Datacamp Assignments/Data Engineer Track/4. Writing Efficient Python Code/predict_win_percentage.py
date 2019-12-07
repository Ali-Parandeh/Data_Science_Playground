def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)


In [1]: %%timeit win_perc_preds_loop = []
... 
... # Use a loop and .itertuples() to collect each row's predicted win percentage
... for row in baseball_df.itertuples():
...     runs_scored = row.RS
...     runs_allowed = row.RA
...     win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
...     win_perc_preds_loop.append(win_perc_pred)
... 

'''
51.5 ms +- 633 us per loop (mean +- std. dev. of 7 runs, 10 loops each)
'''

In [2]: %%timeit # Apply predict_win_perc to each row of the DataFrame
... win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

'''
242 ms +- 3.29 ms per loop (mean +- std. dev. of 7 runs, 1 loop each)
'''

In [4]: %%timeit # Calculate the win percentage predictions using NumPy arrays
... win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
... baseball_df['WP_preds'] = win_perc_preds_np

'''
800 us +- 35.7 us per loop (mean +- std. dev. of 7 runs, 1000 loops each)
'''

'''
That's a home run! You practiced using three different approaches to iterate over a pandas DataFrame and perform calculations. 
Did you notice that the .itertuples() approach beat the .apply() approach? 
Even though both these implementations can be useful, 
you should default to using a DataFrame's underlying arrays to perform calculations.

Take a look at your win percentage predictions 
(column 'WP_preds') and compare them to the actual win percentages (column 'WP'). Not bad!
'''