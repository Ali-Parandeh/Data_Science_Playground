'''
In the file counter_utils.py, you will write 2 functions to be a part of your package: 
plot_counter and sum_counters. The structure of your package can be seen in the tree below. 
For the coding portions of this exercise, you will be working in the file counter_utils.py.

text_analyzer
├── __init__.py
└── counter_utils.py
'''

# INSIDE counter_utils.py
# ==============================

# Import needed functionality
from collections import Counter

def plot_counter(counter, n_most_common=5):
  # Subset the n_most_common items from the input counter
  top_items = counter.most_common(n_most_common)
  # Plot `top_items`
  plot_counter_most_common(top_items)


# Import needed functionality
from collections import Counter

def sum_counters(counters):
  # Sum the inputted counters
  return sum(counters, Counter())



# INSIDE __init__.py
# ==============================

'''
You just wrote two functions for your package in the file counter_utils.py named plot_counter & sum_counters. 
Which of the following lines would correctly import these functions in __init__.py using relative import syntax?

'''

from .counter_utils import plot_counter, sum_counters