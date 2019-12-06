from collections import Counter

# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')

'''
Counter({'Water': 66, 'Normal': 64, 'Bug': 51, 'Grass': 47, 'Psychic': 31, 'Rock': 29, 
'Fire': 27, 'Electric': 25, 'Ground': 23, 'Fighting': 23, 'Poison': 22, 'Steel': 18, 
'Ice': 16, 'Fairy': 16, 'Dragon': 16, 'Ghost': 13, 'Dark': 13}) 
'''

# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')

'''
Counter({5: 122, 3: 103, 1: 99, 4: 78, 2: 51, 6: 47}) 
'''

# Use list comprehension to get each Pokémon's starting letter
starting_letters = [name[0] for name in names]

# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)

'''
Counter({'S': 83, 'C': 46, 'D': 33, 'M': 32, 'L': 29, 'G': 29, 'B': 28, 
'P': 23, 'A': 22, 'K': 20, 'E': 19, 'W': 19, 'T': 19, 'F': 18, 'H': 15, 
'R': 14, 'N': 13, 'V': 10, 'Z': 8, 'J': 7, 'I': 4, 'O': 3, 'Y': 3, 'U': 2, 'X': 1})
'''

'''
You used Counter from the collections module to better understand 
the sample of 500 Pokémon that was generated. The sample's most common 
Pokémon type was 'Water' and the sample's least common Pokémon types were 'Ghost' and 'Dark'. 
Did you also notice that most of the Pokémon in the 
sample came from generation 5 and had a starting letter of 'S'
'''