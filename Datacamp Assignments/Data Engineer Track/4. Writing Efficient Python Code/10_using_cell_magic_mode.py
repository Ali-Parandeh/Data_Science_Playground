%%timeit
hero_wts_lbs = []
for wt in wts:
    hero_wts_lbs.append(wt * 2.20462)

'''
975 us +- 29.8 us per loop (mean +- std. dev. of 7 runs, 1000 loops each)
'''

%%timeit
wts_np = np.array(wts)
hero_wts_lbs_np = wts_np * 2.20462

'''
15.5 us +- 450 ns per loop (mean +- std. dev. of 7 runs, 100000 loops each)
'''

'''
You used %%timeit (cell magic mode) to time multiple lines of code. 
Converting the wts list into a NumPy array and taking advantage of 
NumPy array broadcasting saved you some time! Moving forward, 
remember that you can use %timeit to gather runtime for a single line of 
code (line magic mode) and %%timeit to get the runtime for multiple lines of code.
'''