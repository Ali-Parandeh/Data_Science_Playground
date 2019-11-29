# Import needed package
import text_analyzer

# Create instance of document
my_doc = text_analyzer.Document(datacamp_tweets)

# Run help on my_doc's plot method
help(my_doc.plot_counts)

# Plot the word_counts of my_doc
my_doc.plot_counts('word_counts')


dir(my_doc)

'''
Out[1]: 
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_count_words',
 '_tokenize',
 'plot_counts',
 'text',
 'tokens',
 'word_counts']
'''



help(my_doc)

'''
Help on Document in module text_analyzer.document object:

class Document(builtins.object)
 |  Methods defined here:
 |  
 |  __init__(self, text)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  plot_counts(self, attribute='word_counts', n_most_common=5)
 |      Plot most common elements of a ``collections.Counter`` instance attribute
 |      
 |      :param attribute: name of ``Counter`` attribute to use as object to plot
 |      :param n_most_common: number of elements to plot (using ``Counter.most_common()``)
 |      :return: None; a plot is shown using matplotlib
 |      
 |      >>> doc = Document("duck duck goose is fun when you're the goose")
 |      >>> doc.plot_counts('word_counts', n_most_common=5)  # same as default call
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

<script.py> output:
    Help on method plot_counts in module text_analyzer.document:
    
    plot_counts(attribute='word_counts', n_most_common=5) method of text_analyzer.document.Document instance
        Plot most common elements of a ``collections.Counter`` instance attribute
        
        :param attribute: name of ``Counter`` attribute to use as object to plot
        :param n_most_common: number of elements to plot (using ``Counter.most_common()``)
        :return: None; a plot is shown using matplotlib
        
        >>> doc = Document("duck duck goose is fun when you're the goose")
        >>> doc.plot_counts('word_counts', n_most_common=5)  # same as default call
'''