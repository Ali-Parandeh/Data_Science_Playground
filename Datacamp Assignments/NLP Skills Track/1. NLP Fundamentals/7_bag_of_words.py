# Import Counter
from collections import Counter

# Tokenize the article: tokens
tokens = word_tokenize(article)

# Convert the tokens into lowercase: lower_tokens
lower_tokens = [token.lower() for token in tokens]

# Create a Counter with the lowercase tokens: bow_simple
bow_simple = Counter(lower_tokens)

# Print the 10 most common tokens
print(bow_simple.most_common(10))
# <script.py> output:
#     [(',', 151), ('the', 150), ('.', 89), ('of', 81), ("''", 68),
#     ('to', 63), ('a', 60), ('in', 44), ('and', 41), ('debugging', 40)]
