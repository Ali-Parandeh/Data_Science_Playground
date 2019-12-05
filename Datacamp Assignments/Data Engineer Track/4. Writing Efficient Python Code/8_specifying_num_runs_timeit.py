%timeit -r5 -n25 set(heroes)


'''
9.73 us +- 1.5 us per loop (mean +- std. dev. of 5 runs, 25 loops each)

%timeit lets you specify the number of runs and number of loops you 
want to consider with the -r and -n flags. You can use -r5 and -n25 
to specify 5 iterations each with 25 loops when calculating the average 
and standard deviation of runtime for your code.
'''