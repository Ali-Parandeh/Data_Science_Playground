# Use find_unique_items() to collect unique Pokémon names
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))

'''
368
'''

# Convert the names list to a set to collect unique Pokémon names
uniq_names_set = set(names)
print(len(uniq_names_set))

'''
368
'''

# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))

'''
True
'''

# Use the best approach to collect unique primary types and generations
uniq_types = set(primary_types) 
uniq_gens = set(generations)
print(uniq_types, uniq_gens, sep='\n') 

'''
{'Dragon', 'Ice', 'Electric', 'Dark', 'Fighting', 'Ghost', 'Normal', 'Fire', 'Steel', 'Fairy', 'Poison', 'Water', 'Bug', 'Ground', 'Rock', 'Grass', 'Psychic'}
{1, 2, 3, 4, 5, 6}
'''


In [1]: %timeit find_unique_items(names)
# 2.03 ms +- 285 us per loop (mean +- std. dev. of 7 runs, 1000 loops each)

In [2]: %timeit set(names)
# 8.53 us +- 172 ns per loop (mean +- std. dev. of 7 runs, 100000 loops each)

'''
Using a set data type to collect unique values is much faster than using a for loop 
(like in the find_unique_items() function). Since a set is defined as a collection of distinct elements, 
it is an efficient way to collect unique items from an existing object. Here you took advantage of a set 
to find the distinct Pokémon from the sample (eliminating duplicate Pokémon) 
and saw what unique Pokémon types and generations were included in the sample.
'''