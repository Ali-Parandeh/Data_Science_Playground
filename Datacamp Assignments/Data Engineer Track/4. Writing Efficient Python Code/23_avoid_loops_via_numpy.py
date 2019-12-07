# Create a total stats array
total_stats_np = stats.sum(axis=1)

# Create an average stats array
avg_stats_np = stats.mean(axis=1)

# Combine names, total_stats_np, and avg_stats_np into a list
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]

print(poke_list_np == poke_list, '\n')

'''
True 
'''

print(poke_list_np[:3])

'''
[('Abomasnow', 494, 82.33333333333333), ('Abra', 310, 51.666666666666664), ('Absol', 465, 77.5)]
'''

print(poke_list[:3], '\n')

'''
[('Abomasnow', 494, 82.33333333333333), ('Abra', 310, 51.666666666666664), ('Absol', 465, 77.5)] 
'''

top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]
print('3 strongest Pokémon:\n{}'.format(top_3))

'''
3 strongest Pokémon:
[('GroudonPrimal Groudon', 770, 128.33333333333334), ('KyogrePrimal Kyogre', 770, 128.33333333333334), ('Arceus', 720, 120.0)]
'''

'''
You used NumPy's .sum() and .mean() methods with a 
specific axis to eliminate a for loop. With this approach, 
you were able to quickly see that 'GroudonPrimal Groudon', 
'KyogrePrimal Kyogre', and 'Arceus' were the strongest Pokémon in your list based on total stats.

If you were to gather run times, the for 
loop would have taken milliseconds to execute 
while the NumPy approach would have taken 
microseconds to execute. This is quite an improvement!
'''