# Rogue founder code

# Working as employee number 10 at a small startup with millions in 
# funding seemed like a dream job. Now it seems like a nightmare. 
# There are constant outages in production and during the middle of 
# those outages one of the founders builds Java .jar files on their 
# laptop and via ssh loads the .jar files into production servers 
# thinking this will fix the problem. You have mentioned that all 
# software should go through a continuous deployment system.

# After a several day continuous outage that caused permanent customer 
# data loss caused by the founder's rogue coding practices, the founder 
# finally listens to you. They ask you to help them identify all of the 
# .jar files located on servers in the prod directory. Make sure you 
# use the powerful recursive glob technique.


import pathlib
import os

path = pathlib.Path('prod')
matches = sorted(path.glob('*.jar'))
for match in matches:
  print(f"Found rogue .jar file in production: {match}")

# <script.py> output:
#     Found rogue .jar file in production: prod/hope_this_works.jar
#     Found rogue .jar file in production: prod/no_no_no.jar
#     Found rogue .jar file in production: prod/please_please_work.jar
#     Found rogue .jar file in production: prod/why_me.jar

# You used a Path object with the glob method to search for the pattern you were looking for. 
# The recursive glob method saved quite a bit of code!