# Run the help on all 4 functions
help(goldilocks)
help(rapunzel)
help(mary)
help(sleeping_beauty)

# Execute the function with most complete docstring
result = rapunzel(hair_len=20)

# Print the result
print(result)


''' Missing function description
Help on function goldilocks in module __main__:

goldilocks(bear=3)
    :param bear: which number bear's food are you trying to eat; valid numbers: [1, 2, 3]
    :return: description of how the food's temperature is
    
    >>> goldilocks(bear=1)
    'too hot'
'''

''' Perfect
Help on function rapunzel in module __main__:

rapunzel(hair_len=20)
    Lets down hair from tower to be used as climbing rope
    
    :param hair_len: length of hair (cannot be negative)
    :return: strand of hair that is hair_len characters long
    
    >>> rapunzel(hair_len=15)
    '~~~~~~~~~~~~~~~'
'''

''' Missing params and return description
Help on function mary in module __main__:

mary(white_as='snow')
    How white was mary's little lamb?
    
    >>> mary(white_as='salt')
    'Mary had a little lamb whose fleece was white as salt'
'''

''' Missing Function usage example
Help on function sleeping_beauty in module __main__:

sleeping_beauty(awake=False)
    Should Sleeping Beauty wake up?
    
    :param awake: if True then wake up; else snooze
    :return: string showing sleepiness or wakefulness
'''
