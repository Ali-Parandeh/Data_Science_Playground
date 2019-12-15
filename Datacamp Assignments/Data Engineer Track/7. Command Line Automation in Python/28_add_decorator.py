# Hello decorator

# You are working more and more with decorators and you want to ensure 
# that decorators you write remember to use the @wraps functionality to
# preserve the name of the function and the docstring. One idea 
# you have to verify this is to create an integration test that loops over decorators you 
# reate and prints out the names of the decorated functions. 
# Use this approach to verify two decorated function names.


# Decorate two functions with the decorator @nothing 
# which has been imported for you.
# Put both uncalled functions into a list.
# Print the name of each function by using a for 
# loop to pull them out of a list.

# decorate first function
@nothing
def something():
    pass

# decorate second function
@nothing
def another():
    pass

# Put uncalled function into a list and print name  
funcs = [something, another]
for func in funcs:
    print(f"function name: {func.__name__}")

# <script.py> output:
#     function name: something
#     function name: another


# You were able to use the __name__ method to print out the preserved name of each decorated function.