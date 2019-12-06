# Combine names and primary_types
names_type1 = [*zip(names, primary_types)]

print(*names_type1[:5], sep='\n')

'''
<script.py> output:
    ('Abomasnow', 'Grass')
    ('Abra', 'Psychic')
    ('Absol', 'Dark')
    ('Accelgor', 'Bug')
    ('Aerodactyl', 'Rock')
'''

# Combine all three lists together
names_types = [*zip(names, primary_types, secondary_types)]

print(*names_types[:5], sep='\n')

'''
<script.py> output:
    ('Abomasnow', 'Grass', 'Ice')
    ('Abra', 'Psychic', nan)
    ('Absol', 'Dark', nan)
    ('Accelgor', 'Bug', nan)
    ('Aerodactyl', 'Rock', 'Flying')
'''

# Combine five items from names and three items from primary_types
differing_lengths = [*zip(names[:5], primary_types[:3])]

print(*differing_lengths, sep='\n')

'''
<script.py> output:
    ('Abomasnow', 'Grass')
    ('Abra', 'Psychic')
    ('Absol', 'Dark')
'''


'''
You practiced using zip() to combine multiple objects together. 
This is a nice function that allows you to easily combine two or more objects.

Did you notice that if you provide zip() with objects of differing lengths, 
it will only combine until the smallest lengthed object is exhausted
'''