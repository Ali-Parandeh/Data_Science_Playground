# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

# Use list comprehension with the same logic as the highest_hp_pokemon code block
highest_hp_pokemon = [(names, hps, z_scores) for names, hps, z_scores in poke_zscores2 if z_scores > 2]
print(*highest_hp_pokemon, sep='\n')


In [1]: %%timeit poke_zscores = []
... 
... for name,hp in zip(names, hps):
...     hp_avg = hps.mean()
...     hp_std = hps.std()
...     z_score = (hp - hp_avg)/hp_std
...     poke_zscores.append((name, hp, z_score))
... high_hp_pokemon = []
... 
... for name,hp,zscore in poke_zscores:
...     if zscore > 2:
...         high_hp_pokemon.append((name, hp, zscore))

'''
69.9 ms +- 10.5 ms per loop (mean +- std. dev. of 7 runs, 10 loops each)
'''

In [2]: %%timeit # Calculate the total HP avg and total HP standard deviation
... hp_avg = hps.mean()
... hp_std = hps.std()
... 
... z_scores = (hps - hp_avg)/hp_std
... 
... # Combine names, hps, and z_scores
... poke_zscores2 = [*zip(names, hps, z_scores)]
... 
... # Use list comprehension with the same logic as the highest_hp_pokemon code block
... highest_hp_pokemon = [(names, hps, z_scores) for names, hps, z_scores in poke_zscores2 if z_scores > 2]

'''
304 us +- 26.3 us per loop (mean +- std. dev. of 7 runs, 1000 loops each)
'''

'''
You're Catching 'Em All (efficiencies that is). 
You eliminated two loops using NumPy broadcasting and list comprehension. 
Did you notice how much faster the approach you developed was compared to the original loops? What a great improvement!

Remember the techniques you've learned throughout this chapter as 
you continue writing Python code outside this course. Keep in mind 
the built-in functions and modules you covered to eliminate loops 
and remember to check your unavoidable loops for things that can be moved outside.
'''