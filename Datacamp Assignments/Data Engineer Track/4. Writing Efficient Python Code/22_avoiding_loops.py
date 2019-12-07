gen1_gen2_name_lengths_loop = []

for name,gen in zip(poke_names, poke_gens):
    if gen < 3:
        name_length = len(name)
        poke_tuple = (name, name_length)
        gen1_gen2_name_lengths_loop.append(poke_tuple)


# Collect Pokémon that belong to generation 1 or generation 2
gen1_gen2_pokemon = [name for name,gen in zip(poke_names, poke_gens) if gen < 3]

# Create a map object that stores the name lengths
name_lengths_map = map(len, gen1_gen2_pokemon)

# Combine gen1_gen2_pokemon and name_lengths_map into a list
gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]

print(gen1_gen2_name_lengths_loop[:5])
print(gen1_gen2_name_lengths[:5])

'''
[('Abra', 4), ('Aerodactyl', 10), ('Aipom', 5), ('Alakazam', 8), ('Ampharos', 8)]
[('Abra', 4), ('Aerodactyl', 10), ('Aipom', 5), ('Alakazam', 8), ('Ampharos', 8)]
'''

'''
You successfully used list comprehension and the map() function to 
eliminate a for loop. If you compared runtimes between the for loop 
and using list comprehension with a map() function, you'd see that 
the for loop took quite a bit longer.

If you're an experienced Pythonista, you may have noticed 
that you could replace the entire for loop with one list comprehension: 

[(name, len(name)) for name,gen in zip(poke_names, poke_gens) if gen < 3]
'''