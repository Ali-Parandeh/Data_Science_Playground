# Import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize a TfidfVectorizer object: tfidf_vectorizer
# max_df: When building the vocabulary ignore terms that 
# have a document frequency strictly lower than the given threshold. This value is also called cut-off in the literature.
tfidf_vectorizer = TfidfVectorizer(stop_words= 'english', max_df= 0.7)

# Transform the training data: tfidf_train 
tfidf_train = tfidf_vectorizer.fit_transform(X_train, y_train)

# Transform the test data: tfidf_test 
tfidf_test = tfidf_vectorizer.transform(X_test)

# Print the first 10 features
print(tfidf_vectorizer.get_feature_names()[:10])
    # ['00', '000', '001', '008s', '00am', '00pm', '01', '01am', '02', '024']

# Print the first 5 vectors of the tfidf training data
# A: array
print(tfidf_train.A[:5])

""" <script.py> output:
    [[0.         0.01928563 0.         ... 0.         0.         0.        ]
     [0.         0.         0.         ... 0.         0.         0.        ]
     [0.         0.02895055 0.         ... 0.         0.         0.        ]
     [0.         0.03056734 0.         ... 0.         0.         0.        ]
     [0.         0.         0.         ... 0.         0.         0.        ]] """