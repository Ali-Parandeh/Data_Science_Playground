# Import needed package
import text_analyzer

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets)

# Plot the most used hashtags in the retweets
my_tweets.retweets.plot_counts('hashtag_counts')



dir(text_analyzer.Tweets)

'''

Out[8]: 
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
 '_count_hashtags',
 '_count_mentions',
 '_count_words',
 '_process_retweets',
 '_tokenize',
 'plot_counts']
'''


help(text_analyzer.Tweets)
'''
Help on class Tweets in module text_analyzer.tweets:

class Tweets(text_analyzer.social_media.SocialMedia)
 |  # Define a Tweet class that is a child of the SocialMedia class
 |  
 |  Method resolution order:
 |      Tweets
 |      text_analyzer.social_media.SocialMedia
 |      text_analyzer.document.Document
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, text)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from text_analyzer.document.Document:
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
 |  Data descriptors inherited from text_analyzer.document.Document:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
'''