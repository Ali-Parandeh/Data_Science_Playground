ash_pokedex = ['Pikachu',
 'Bulbasaur',
 'Koffing',
 'Spearow',
 'Vulpix',
 'Wigglytuff',
 'Zubat',
 'Rattata',
 'Psyduck',
 'Squirtle']

brock_pokedex = ['Onix',
 'Geodude',
 'Zubat',
 'Golem',
 'Vulpix',
 'Tauros',
 'Kabutops',
 'Omastar',
 'Machop',
 'Dugtrio']


# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

'''
{'Tauros', 'Golem', 'Onix', 'Omastar', 'Vulpix', 'Dugtrio', 'Zubat', 'Geodude', 'Kabutops', 'Machop'}
'''

# Check if Psyduck is in Ash's list and Brock's set
print('Psyduck' in ash_pokedex)
print('Psyduck' in brock_pokedex_set)

'''
True
False
'''

# Check if Machop is in Ash's list and Brock's set
print('Machop' in ash_pokedex)
print('Machop' in brock_pokedex_set)

'''
False
True
'''


'''
Membership testing is much faster when you use sets. 
Did you notice that using a set for member testing is 
faster than using a list regardless if the item you are 
checking is in the set? Checking for 'Psyduck' 
(which was not in Brock's set) is still faster than checking 
for 'Psyduck' in Ash's list!
'''