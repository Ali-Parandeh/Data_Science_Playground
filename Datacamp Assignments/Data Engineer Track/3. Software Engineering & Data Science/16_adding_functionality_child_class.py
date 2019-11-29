from collections import Counter
# from .token_utils import tokenize
# from .filter_utils import filter_word_counts


class Document:
    def __init__(self, text):
        print('DOCUMENT CLASS')
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

# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        print('CHILD CLASS')
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()
        
    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts, first_char='#')      
    
    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return filter_word_counts(self.word_counts, first_char='@')


SocialMedia('some text')

'''
CHILD CLASS
DOCUMENT CLASS
'''


help(filter_word_counts)

'''
Help on function filter_word_counts in module __main__:

filter_word_counts(word_counts, first_char)
    Filter Document.word_counts by the first character of the word
    
    :param word_counts: the word_counts attribute of a Document class instance
    :param first_char: only keep word counts that start with this character
    
    >>> # How to filter to only words that start with 'A'
    >>> filter_word_counts(document.word_counts, 'A')
'''