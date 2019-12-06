# Import combinations from itertools
from itertools import combinations

pokemon = ['Geodude', 'Cubone', 'Lickitung', 'Persian', 'Diglett']

# Create a combination object with pairs of Pokémon
combos_obj = combinations(iter(pokemon), 2)
print(type(combos_obj), '\n')

'''
class 'itertools.combinations'>
'''

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
print(combos_2, '\n')

'''
[('Geodude', 'Cubone'), ('Geodude', 'Lickitung'), ('Geodude', 'Persian'), ('Geodude', 'Diglett'), ('Cubone', 'Lickitung'), 
('Cubone', 'Persian'), ('Cubone', 'Diglett'), ('Lickitung', 'Persian'), ('Lickitung', 'Diglett'), ('Persian', 'Diglett')]
'''

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(iter(pokemon), 4)]
print(combos_4)

''' 
    [('Geodude', 'Cubone'), ('Geodude', 'Lickitung'), ('Geodude', 'Persian'), 
    ('Geodude', 'Diglett'), ('Cubone', 'Lickitung'), ('Cubone', 'Persian'), 
    ('Cubone', 'Diglett'), ('Lickitung', 'Persian'), ('Lickitung', 'Diglett'), ('Persian', 'Diglett')] 
'''

'''
You used combinations() from itertools to collect various combination-tuples 
from a list. combinations() allows you to specify any size of combinations by 
passing an integer as the second argument. Ash has 10 combination options when his Pokédex can store only two Pokémon. 
He has 5 combination options when his Pokédex can store four Pokémon.
'''