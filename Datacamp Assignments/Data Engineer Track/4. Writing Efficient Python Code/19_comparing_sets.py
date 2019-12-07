ash_pokedex = ['Pikachu', 'Bulbasaur', 'Koffing', 'Spearow', 'Vulpix', 'Wigglytuff', 'Zubat', 'Rattata', 'Psyduck', 'Squirtle'] 
misty_pokedex = ['Krabby', 'Horsea', 'Slowbro', 'Tentacool', 'Vaporeon', 'Magikarp', 'Poliwag', 'Starmie', 'Psyduck', 'Squirtle']

# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
print(both)

'''
{'Psyduck', 'Squirtle'}
'''

# Find the Pokémon that Ash has and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only)

'''
{'Bulbasaur', 'Spearow', 'Wigglytuff', 'Koffing', 'Vulpix', 'Zubat', 'Rattata', 'Pikachu'}
'''

# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set)

'''
{'Bulbasaur', 'Spearow', 'Magikarp', 'Wigglytuff', 'Slowbro', 'Koffing', 'Vulpix', 'Krabby', 
'Starmie', 'Zubat', 'Rattata', 'Horsea', 'Pikachu', 'Poliwag', 'Tentacool', 'Vaporeon'}
'''


'''Using sets lets you do some cool comparisons between objects without 
the need to write a for loop. With a few lines of code, 
you were able to see that both Ash and Misty have 'Psyduck' and 'Squirtle' in their Pokédex. 
You were also able to see that Ash has 8 Pokémon that Misty does not have.
'''