# Create a list using the formal name
formal_list = list()
print(formal_list)

'''
[]
'''

# Create a list using the literal syntax
literal_list = []
print(literal_list)

'''
[]
'''

# Print out the type of formal_list
print(type(formal_list))

'''
<class 'list'>
'''

# Print out the type of literal_list
print(type(literal_list))

'''
<class 'list'>
'''

%timeit list()

'''
106 ns +- 31.2 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)
'''

%timeit []

'''
28.9 ns +- 11.1 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)
'''

'''
Using Python's literal syntax to define a data structure can speed up your runtime. Consider using the literal syntaxes 
(like [] instead of list(), {} instead of dict(), or () instead of tuple()), where applicable, to gain some speed.
'''