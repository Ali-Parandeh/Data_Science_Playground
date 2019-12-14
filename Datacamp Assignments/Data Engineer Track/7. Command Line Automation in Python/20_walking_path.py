# Sweet pickle

# "It was the best of times, it was the worst of times..", 
# Charles Dickens said in a Tale of Two Cities. He could also be talking 
# about your startup. Initially things were amazing and you and your co-workers 
# laughed in delight as the CTO churned out machine learning models dozens by the day. 
# Often this would be at 2AM and you would arrive in the morning and find the serialized
#  sklearn models waiting for the Data Science team to deploy to production.

# Unfortunately, this was in fact too good to be true. Many of the models had serious 
# flaws and this ultimately led to the CTO stepping down. IT Auditors want to determine 
# how flawed these ML models were and back test the predictions for accuracy.

# Use the os.walk module to find serialized models and test them for accuracy.

# 1. Walk the the file system path my using os.walk.
# 2. Look for a file extension named .joblib and load the model into clf using joblib's load() function.
# 3. Use sklearn to predict from the unpickled model by loading it into clf.predict() 
# and pass the input data X_digits to it (X_digits is already in memory).
# 4. Print your predictions.

import os, joblib
# Walk the filesystem starting at the my path
for root, _, files in os.walk('my'):
    for name in files:
      	# Create the full path to the file by using os.path.join()
        fullpath = os.path.join(root, name)
        print(f"Processing file: {fullpath}")
        _, ext = os.path.splitext(fullpath)
        # Match the extension pattern .joblib
        if ext == ".joblib":
            clf = joblib.load(fullpath)
            break

# Predict from pickled model
print(clf.predict(X_digits))

# <script.py> output:
#     Processing file: my/models/badmodel.alsojunk
#     Processing file: my/models/anotherbadmodel.junk
#     Processing file: my/models/good/digits_prediction.joblib
#     [0 1 2 ... 8 9 8]

# Crunch! This is the sound of your python script biting into a pickled sklearn model. 
# By walking the filesystem and looking for joblib extensions you were able to speed up the auditing process.