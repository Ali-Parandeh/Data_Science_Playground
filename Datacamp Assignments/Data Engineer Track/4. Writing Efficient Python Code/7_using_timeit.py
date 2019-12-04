# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
nums_unpack = [*range(0,51)]


%timeit [num for num in range(51)]
"""
2.92 us +- 27.6 ns per loop (mean +- std. dev. of 7 runs, 100000 loops each)
"""

%timeit  [*range(0,51)]

'''
502 ns +- 43 ns per loop (mean +- std. dev. of 7 runs, 1000000 loops each)
'''

'''
You used %timeit to gather and compare runtimes! Although list 
comprehension is a useful and powerful tool, 
sometimes unpacking an object can save time and looks a little cleaner.
'''