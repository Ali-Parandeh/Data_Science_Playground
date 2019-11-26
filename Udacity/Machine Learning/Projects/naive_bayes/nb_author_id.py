#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
from sklearn.naive_bayes import GaussianNB
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

clf = GaussianNB()
t0 = time()
clf.fit(features_train, labels_train)
print ("training time:", round(time()-t0, 3), "s") # training time: 1.382 s
t1 = time()
predict = clf.predict(features_test)
print ("Predicting time:", round(time()-t1, 3), "s") # Predicting time: 0.233 s
print(type(predict)) #<class 'numpy.ndarray'>
print(type(labels_test)) # <class 'list'>
accuracy = accuracy_score(predict, labels_test)
print(accuracy) # 0.9732650739476678


#########################################################


