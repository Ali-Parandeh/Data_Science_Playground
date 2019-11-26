#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
import numpy as np
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm
from sklearn.metrics import accuracy_score
small_training_set = True # Smaller Training Set (sample size = 1%)
if small_training_set:
    features_train = features_train[:int(len(features_train)/100)] 
    labels_train = labels_train[:int(len(labels_train)/100)] 
clf = svm.SVR(kernel = "rbf", gamma="auto", C= 3000.0) 
# If kernel is 'rbf' accuracy drops to 61% with 100 training samples
# To get an accuracy of 90% with 'rbf' kernel while mainting a fast training/prediction time,
# set C=3000
t0 = time() 
clf.fit(features_train, labels_train)
print ("training time:", round(time()-t0, 3), "s") 
# 0.083s when using 100 samples to train, 752s when using all data points
t1 = time()
pred = clf.predict(features_test)
print ("Predicting time:", round(time()-t1, 3), "s") 
# 0.84s when using 100 samples, 50s when using all data points 
# Need to round the predictions as they are continouous variables while testing labels are binary
accuracy = accuracy_score(labels_test, np.around(pred))
print(accuracy) # 90% when only using 100 samples. 98% when using all of the data points.11

# Checking how many of the emails have been written by Chris (label 1)
count = 0
for i in range(len(pred)):
    if round(pred[i]) == 1: 
        count += 1

print(count)
#########################################################


