from collections import Counter
from .token_utils import tokenize


class Document:
    def __init__(self, text):
        self.text = text
        # pre tokenize the document with non-public tokenize method
        self.tokens = self._tokenize()
        # pre tokenize the document with non-public count_words
        self.word_counts = self._count_words()

    def _tokenize(self):
        return tokenize(self.text)

    # non-public method to tally document's word counts with Counter
    def _count_words(self):
        return Counter(self.tokens)

datacamp_tweets = 'Some text'

# create a new document instance from datacamp_tweets
datacamp_doc = Document(datacamp_tweets)

# print the first 5 tokens from datacamp_doc
print(datacamp_doc.tokens[:5])

# print the top 5 most used words in datacamp_doc
print(datacamp_doc.word_counts.most_common(5))

'''
<script.py> output:
    ['[DataCamp]', 'Introduction', 'to', 'H', 'O']
    [('DataCamp', 322), ('to', 263), ('the', 251), ('in', 163), ('RT', 158)]

Thanks to the functionality you added to the __init__ method, 
your users get the benefits of tokenization and word counts without any extra effort.
'''