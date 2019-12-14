# You have an existing bash script that you need to run in a hurry and 
# then capture the output to continue working on it in Python. 
# You remember that you can use %%bash magic syntax to capture the
# output of a script in IPython. What is the proper way to run this 
# script and capture the output as a Python variable?


In [1]: %%bash --out output
# ... ls

In [2]: output
# Out[2]: 'test_dir\n'


# %%bash --out output will allow you to run a code block with 
# output stored in the variable output. Being able to run a full 
# bash script in Jupyter notebooks or IPython can be very helpful. 
# One good use case is needing to download machine learning 
# training data using wget, then uncompressing it.