# Simple yet true

# You need to convince your company to both use the click command-line tool 
# and to open their new headquarters in an affordable city. 
# Use this opportunity to create a random city selector and 
# then print the results to stdout using click.


import click
import random

# Create random values to choose from
values = ["Nashville", "Austin", "Denver", "Cleveland"]

# Select a random choice
result = random.choice(values)

# Print the random choice using click echo
click.echo(f"My choice is: {result}")

# <script.py> output:
#     My choice is: Nashville