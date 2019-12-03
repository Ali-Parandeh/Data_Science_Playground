# Rewrite the for loop to use enumerate
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

'''
[(0, 'Jerry'), (1, 'Kramer'), (2, 'Elaine'), (3, 'George'), (4, 'Newman')]
'''

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)


'''
[(0, 'Jerry'), (1, 'Kramer'), (2, 'Elaine'), (3, 'George'), (4, 'Newman')]
'''

# Unpack an enumerate object with a starting index of one
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)

'''
[(1, 'Jerry'), (2, 'Kramer'), (3, 'Elaine'), (4, 'George'), (5, 'Newman')]
'''

'''
Using Python's built-in enumerate() function allows you to 
create an index for each item in the object you give it. 
You can use list comprehension, or even unpack the enumerate 
object directly into a list, to write a nice simple one-liner.
'''