# Define a Tweet class that inherits from SocialMedia
from collections import Counter
from .utils import tokenize, filter_lines


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

class SocialMedia(Document):
    def __init__(self, text):
        super().__init__(self, text) # can also use Document.__init(self, text)


class Tweets(SocialMedia):
    def __init__(self, text):
        # Call parent's __init__ with super()
        super().__init__(self, text)
        # Define retweets attribute with non-public method
        self.retweets = self._process_retweets()

    def _process_retweets(self):
        # Filter tweet text to only include retweets
        retweet_text = filter_lines(self.text, first_chars='RT')
        # Return retweet_text as a SocialMedia object
        return SocialMedia(retweet_text)



help(filter_lines)

'''
Help on function filter_lines in module text_analyzer.text_utils:

filter_lines(text, first_chars)
    Filter lines by beginning characters (case sensitive)
    
    :param text:  multi-line text to filter
    :param first_chars: required characters for line to start with to be returned
    :return: text with only lines starting with first_chars included
    
    >>> text = 'humpty dumpty\nsat on a wall\nhumpty dumpty\nhad a great fall'
    >>> filter_lines(text, 'h')
    'humpty dumpty\nhumpty dumpty\nhad a great fall'
    
    >>> filter_lines(text, 'humpty')
    'humpty dumpty\nhumpty dumpty'
'''