'''
The object word_counts is loaded into your environment. 
It contains a list of Counter objects that contain word counts from a sample of DataCamp tweets.

The structure you've created can be seen in the tree below. 
You'll be working in my_script.py.

working_dir
├── text_analyzer
│    ├── __init__.py
│    ├── counter_utils.py
└── my_script.py
'''


# Import local package
import text_analyzer

# Sum word_counts using sum_counters from text_analyzer
word_count_totals = text_analyzer.sum_counters(word_counts)

# Plot word_count_totals using plot_counter from text_analyzer
text_analyzer.plot_counter(word_count_totals)


'''
Thanks to your package's functionality that we were easily able to import and use, 
our anaylsis script is able to be very concise, tidy, and readable.
'''