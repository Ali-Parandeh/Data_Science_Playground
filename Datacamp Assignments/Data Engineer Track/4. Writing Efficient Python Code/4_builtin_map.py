names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

'''
<class 'map'>
'''

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)

'''
['JERRY', 'KRAMER', 'ELAINE', 'GEORGE', 'NEWMAN']
'''

'''
You used Python's built-in map() function to apply the str.upper() 
method to each element in the names object. 
'''