# Debugging decorator

# Your company has an internship program that involves training non-developers 
# how to program in Python. One of the challenges is that it is often difficult to 
# explain how to debug code to the interns. You have an idea to write a debugging 
# decorator that interns can use that will print out both the arguments and the 
# keyword arguments when they are applied to a function. You are confident this 
# will be a very useful skill to teach them because of how much you use decorators 
# to debug code and enhance automation tasks.

# Write a decorator that will wrap a function and print any *args or **kw arguments out. 
# Remember a decorator must return the the function is wraps. This is the last line of a decorator.

# 1. Create a decorator that prints the *args and **kw arguments passed into it.
# 2. Apply that decorator to the mult function and run it.

from functools import wraps

# create decorator
def debug(f):
	@wraps(f)
	def wrap(*args, **kw):
		result = f(*args, **kw)
		print(f"function name: {f.__name__}, args: [{args}], kwargs: [{kw}]")
		return result
	return wrap
  
# apply decorator
@debug
def mult(x, y=10):
	return x*y
print(mult(5, y=5))


# <script.py> output:
#     function name: mult, args: [(5,)], kwargs: [{'y': 5}]
#     25

# Decorators or useful not just in instrumentation, but also automation workflows. 
# You were able to intercept argument and keyword argument calls 
# and print them out which will enhance your ability to debug production code.

