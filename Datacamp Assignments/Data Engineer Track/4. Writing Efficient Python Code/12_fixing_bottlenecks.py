def convert_units_broadcast(heroes, heights, weights):

    # Array broadcasting instead of list comprehension
    new_hts = heights * 0.39370
    new_wts = weights * 2.20462

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data


In [1]: %load_ext line_profiler

'''
The line_profiler extension is already loaded. To reload it, use:
  %reload_ext line_profiler
'''

In [2]: %lprun -f convert_units_broadcast convert_units_broadcast(heroes, hts, wts)

'''
Timer unit: 1e-06 s

Total time: 0.000674 s
File: <ipython-input-11-84e44a6b12f5>
Function: convert_units_broadcast at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def convert_units_broadcast(heroes, heights, weights):
     2                                           
     3                                               # Array broadcasting instead of list comprehension
     4         1         28.0     28.0      4.2      new_hts = heights * 0.39370
     5         1          5.0      5.0      0.7      new_wts = weights * 2.20462
     6                                           
     7         1          1.0      1.0      0.1      hero_data = {}
     8                                           
     9       481        269.0      0.6     39.9      for i,hero in enumerate(heroes):
    10       480        370.0      0.8     54.9          hero_data[hero] = (new_hts[i], new_wts[i])
    11                                                   
    12         1          1.0      1.0      0.1      return hero_data

'''

'''
By profiling the convert_units() function, you were able to see that 
using list comprehension was not the most efficient solution for creating 
the new_hts and new_wts objects. You also saw that using array broadcasting 
in the convert_units_broadcast() function dramatically decreased the percentage 
of time spent executing these lines of code. You may have noticed that your function still 
takes a while to iterate through the for loop. Don't worry; you'll cover how to make 
this loop more efficient in a later chapter.
'''