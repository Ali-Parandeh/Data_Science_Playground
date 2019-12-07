from itertools import combinations
pokemon_types = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 
'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']

# Collect all possible pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]

# Create an empty list called enumerated_tuples
enumerated_tuples = []

# Add a line to append each enumerated_pair_tuple to the empty list above
for i,pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_tuples.append(enumerated_pair_tuple)

# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerated_tuples)]
print(enumerated_pairs)

'''
[[1, 'Bug', 'Dark'], [2, 'Bug', 'Dragon'], [3, 'Bug', 'Electric'], 
[4, 'Bug', 'Fairy'], [5, 'Bug', 'Fighting'], [6, 'Bug', 'Fire'], 
[7, 'Bug', 'Flying'], [8, 'Bug', 'Ghost'], [9, 'Bug', 'Grass'], 
[10, 'Bug', 'Ground'], [11, 'Bug', 'Ice'], [12, 'Bug', 'Normal'], 
[13, 'Bug', 'Poison'], [14, 'Bug', 'Psychic'], [15, 'Bug', 'Rock'], 
[16, 'Bug', 'Steel'], [17, 'Bug', 'Water'], [18, 'Dark', 'Dragon'], 
[19, 'Dark', 'Electric'], [20, 'Dark', 'Fairy'], [21, 'Dark', 'Fighting'], 
[22, 'Dark', 'Fire'], [23, 'Dark', 'Flying'], 
[24, 'Dark', 'Ghost'], [25, 'Dark', 'Grass'], [26, 'Dark', 'Ground'], 
[27, 'Dark', 'Ice'], [28, 'Dark', 'Normal'], [29, 'Dark', 'Poison'] ...]
'''

'''
Rather than converting each tuple to a list within the loop, 
you used the map() function to convert tuples to lists all at 
once outside of a loop. You're getting the hang of writing efficient loops! 
Remember, you want to avoid looping as much as possible when writing Python code. 
In cases where looping is unavoidable, be sure to check your loops for one-time 
calculations and holistic conversions to make them more efficient.
'''