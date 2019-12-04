import numpy as np
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
def welcome_guest(name, time):
    print("Welcome to Festivus {}... You're {} min late").format(name, time)

# Create a list of arrival times
arrival_times = [*range(10,60,10)]

print(arrival_times)

'''
[10, 20, 30, 40, 50]
'''

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3
print(new_times)

'''
[ 7 17 27 37 47]
'''

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]
print(guest_arrivals)

'''
[('Jerry', 7), ('Kramer', 17), ('Elaine', 27), ('George', 37), ('Newman', 47)]
'''

# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')

'''
Welcome to Festivus Jerry... You're 7 min late.
Welcome to Festivus Kramer... You're 17 min late.
Welcome to Festivus Elaine... You're 27 min late.
Welcome to Festivus George... You're 37 min late.
Welcome to Festivus Newman... You're 47 min late.
'''