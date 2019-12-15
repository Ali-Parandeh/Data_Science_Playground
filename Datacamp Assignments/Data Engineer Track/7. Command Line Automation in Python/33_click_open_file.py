# Take a few random words that come to mind and 
# write them out via click. 

# Setup
import click
words = ["Asset", "Bubble", "10", "Year"]
filename = "words.txt"

# Write with click.open()
with click.open_file(filename, 'w') as f:

# Loop over words with a for loop
    for word in words:
        f.write(f'{word}\n')

# Read it back
with open(filename) as output_file:
    print(output_file.read())

# <script.py> output:
#     Asset
#     Bubble
#     10
#     Year

# Great work using click.open_file() to write content out to a file. 
# You have discovered how powerful click is as a centralized automation framework.

