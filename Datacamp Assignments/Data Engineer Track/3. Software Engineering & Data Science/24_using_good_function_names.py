'''
Give function the best possible name from the following options: 
do_stuff, 
hypotenuse_length, 
square_root_of_leg_a_squared_plus_leg_b_squared, 
pythagorean_theorem.
'''

def hypotenuse_length(leg_a, leg_b):
    """Find the length of a right triangle's hypotenuse

    :param leg_a: length of one leg of triangle
    :param leg_b: length of other leg of triangle
    :return: length of hypotenuse
    
    >>> hypotenuse_length(3, 4)
    5
    """
    return math.sqrt(leg_a**2 + leg_b**2)


# Print the length of the hypotenuse with legs 6 & 8
print(hypotenuse_length(6, 8))


'''
The name hypotenuse_length accurately describes what a user 
can expect when they use the function and won't hinder the readability of their code.

'''
