In [1]: %load_ext line_profiler

In [2]: %lprun -f convert_units convert_units(heroes, hts, wts)

'''
Timer unit: 1e-06 s

Total time: 0.001484 s
File: <ipython-input-7-2ae8c0194a47>
Function: convert_units at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def convert_units(heroes, heights, weights):
     2                                           
     3         1        232.0    232.0     15.6      new_hts = [ht * 0.39370  for ht in heights]
     4         1        218.0    218.0     14.7      new_wts = [wt * 2.20462  for wt in weights]
     5                                           
     6         1          2.0      2.0      0.1      hero_data = {}
     7                                           
     8       481        501.0      1.0     33.8      for i,hero in enumerate(heroes):
     9       480        530.0      1.1     35.7          hero_data[hero] = (new_hts[i], new_wts[i])
    10                                                   
    11         1          1.0      1.0      0.1      return hero_data
'''

In [3]: %timeit convert_units(heroes, hts, wts)

'''
215 us +- 659 ns per loop (mean +- std. dev. of 7 runs, 1000 loops each)
'''

'''
Line 3 seems like it may be a potential bottleneck in the above function.
Did you notice that the new_wts list comprehension also accounted for a similar percentage of the runtime? 
This is an indication that you may want to create the new_hts and new_wts objects using a different technique.
Since the height and weight of each hero is stored in a numpy array, 
you can use array broadcasting rather than list comprehension to convert the heights and weights.
'''