# Import necessary modules
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# Split scene_one into sentences: sentences
sentences = sent_tokenize(scene_one)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[3])

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(scene_one))

# Print the unique tokens result
print(unique_tokens)

# <script.py> output:
#     {'covered', 'It', 'speak', 'this', 'zone', 'Mercea', 'ratios', 'all', 'from', 'to', 'an', 'grips',
# 'second', 'he', 'kingdom', ']', 'ridden', 'using', 'weight', 'every', 'Wait', 'Ridden', 'since',
# "'ve", 'minute', 'order', 'does', '!', 'may', "'m", 'search', 'coconut', 'warmer', 'KING',
# 'that', 'Whoa', 'point', 'We', 'there', 'halves', '...', 'swallows', 'it', 'must', 'got',
# "'", 'wants', 'other', 'here', 'ask', 'question', 'SCENE', '.', 'Camelot', 'and', 'on',
# 'snows', 'tell', 'bird', 'go', 'its', 'So', 'not', "'em", 'beat', 'African', 'dorsal',
# 'maybe', 'horse', 'empty', 'clop', 'What', 'King', 'them'}
