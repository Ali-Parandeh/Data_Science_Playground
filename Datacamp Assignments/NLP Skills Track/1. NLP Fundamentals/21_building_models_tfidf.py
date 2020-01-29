# Calculate the accuracy score and confusion matrix of
# Multinomial Naive Bayes classifier predictions trained on 
# tfidf_train, y_train and tested against tfidf_test and 
# y_test

model = MultinomialNB()
model.fit(tfidf_train, y_train)
pred = model.predict(tfidf_test)
score = metrics.accuracy_score(y_test, pred)
print(score)

# 0.8565279770444764

cm = metrics.confusion_matrix(y_test, pred, labels=['FAKE', 'REAL'])
print(cm)

""" <script.py> output:
    [[ 739  269]
     [  31 1052]] """