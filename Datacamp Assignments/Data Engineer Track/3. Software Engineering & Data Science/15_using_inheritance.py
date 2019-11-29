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

class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text) # can also use super().__init(text)?

'''
Thanks to inheritance your SocialMedia class already has all the functionality 
of the Document class, and you were able to accomplish this by staying DRY.
'''