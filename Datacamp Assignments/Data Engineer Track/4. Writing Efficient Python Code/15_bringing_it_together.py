import numpy as np

def get_publisher_heroes(heroes, publishers, desired_publisher):

    desired_heroes = []

    for i,pub in enumerate(publishers):
        if pub == desired_publisher:
            desired_heroes.append(heroes[i])

    return desired_heroes


def get_publisher_heroes_np(heroes, publishers, desired_publisher):

    heroes_np = np.array(heroes)
    pubs_np = np.array(publishers)

    desired_heroes = heroes_np[pubs_np == desired_publisher]

    return desired_heroes


In [3]: %load_ext line_profiler

In [4]: %lprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')

'''
Timer unit: 1e-06 s

Total time: 0.000313 s
File: <ipython-input-3-5a6bc05c1c55>
Function: get_publisher_heroes at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def get_publisher_heroes(heroes, publishers, desired_publisher):
     2                                           
     3         1          1.0      1.0      0.3      desired_heroes = []
     4                                           
     5       481        147.0      0.3     47.0      for i,pub in enumerate(publishers):
     6       480        150.0      0.3     47.9          if pub == desired_publisher:
     7         4         14.0      3.5      4.5              desired_heroes.append(heroes[i])
     8                                           
     9         1          1.0      1.0      0.3      return desired_heroes
'''


In [6]: %lprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')

'''
Timer unit: 1e-06 s

Total time: 0.000209 s
File: <ipython-input-3-5a6bc05c1c55>
Function: get_publisher_heroes_np at line 12

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    12                                           def get_publisher_heroes_np(heroes, publishers, desired_publisher):
    13                                           
    14         1        140.0    140.0     67.0      heroes_np = np.array(heroes)
    15         1         51.0     51.0     24.4      pubs_np = np.array(publishers)
    16                                           
    17         1         18.0     18.0      8.6      desired_heroes = heroes_np[pubs_np == desired_publisher]
    18                                           
    19         1          0.0      0.0      0.0      return desired_heroes
'''

In [8]: %load_ext memory_profiler

'''
The memory_profiler extension is already loaded. To reload it, use:
  %reload_ext memory_profiler
'''

In [9]: from hero_funcs import get_publisher_heroes, get_publisher_heroes_np

In [10]: %mprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')

'''
Filename: /tmp/tmpbgrbzvuq/hero_funcs.py

Line #    Mem usage    Increment   Line Contents
================================================
     4    109.4 MiB    109.4 MiB   def get_publisher_heroes(heroes, publishers, desired_publisher):
     5                             
     6    109.4 MiB      0.0 MiB       desired_heroes = []
     7                             
     8    109.4 MiB      0.0 MiB       for i,pub in enumerate(publishers):
     9    109.4 MiB      0.0 MiB           if pub == desired_publisher:
    10    109.4 MiB      0.0 MiB               desired_heroes.append(heroes[i])
    11                             
    12    109.4 MiB      0.0 MiB       return desired_heroes
'''

In [11]: %mprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')

'''
Filename: /tmp/tmpbgrbzvuq/hero_funcs.py

Line #    Mem usage    Increment   Line Contents
================================================
    15    109.4 MiB    109.4 MiB   def get_publisher_heroes_np(heroes, publishers, desired_publisher):
    16                             
    17    109.4 MiB      0.0 MiB       heroes_np = np.array(heroes)
    18    109.4 MiB      0.0 MiB       pubs_np = np.array(publishers)
    19                             
    20    109.4 MiB      0.0 MiB       desired_heroes = heroes_np[pubs_np == desired_publisher]
    21                             
    22    109.4 MiB      0.0 MiB       return desired_heroes
'''