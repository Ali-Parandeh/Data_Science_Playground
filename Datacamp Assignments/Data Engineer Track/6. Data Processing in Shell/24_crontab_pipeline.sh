# Preview both Python script and requirements text file
cat create_model.py

# import pandas as pd
# import pickle
# from sklearn.ensemble import RandomForestClassifier

# df_train = pd.read_csv("trainexit.csv")
# df_train.dropna(inplace=True)
# df_train = df_train.drop(['PassengerId', 'Name', 'Cabin', 'Ticket'], axis=1)

# df_train = pd.get_dummies(df_train)
# df_train = df_train.drop(['Sex_female', 'Embarked_C'], axis=1)

# X = df_train.drop('Survived', axis = 1)
# y = df_train['Survived']

# model = RandomForestClassifier()
# model.fit(X, y)

# model_filename = 'model.pkl'
# with open(model_filename, 'wb') as f:
#     pickle.dump(model, f)

cat requirements.txt
# scikit-learn==0.20.2
# scipy==1.2.0
# sklearn==0.0Collecting scikit-learn==0.20.2

# Pip install Python dependencies in requirements file
pip install -r requirements.txt
#   Downloading https://files.pythonhosted.org/packages/18/d9/bea927c86
#   bf78d583d517f24cbc87606cb333bfb3a5c99cb85b547305f0f/scikit_learn-0.20.2-cp35-cp35m-manylinux1_x86_64.whl (5.3MB)
#      |████████████████████████████████| 5.3MB 27.2MB/s
# Collecting scipy==1.2.0
#   Downloading https://files.pythonhosted.org/packages/ab/19/c0ad5b9183ef
#   97030edd6297d1726525ff2c369a09fbb6ea52a1e616ffd6/scipy-1.2.0-cp35-cp35m-manylinux1_x86_64.whl (26.5MB)
#      |████████████████████████████████| 26.5MB 46.6MB/s
# Collecting sklearn==0.0
#   Downloading https://files.pythonhosted.org/packages/1e/7a/dbb3be0ce9b
#   d5c8b7e3d87328e79063f8b263b2b1bfa4774cb1147bfcd3f/sklearn-0.0.tar.gz
# Requirement already satisfied: numpy>=1.8.2 in /usr/local/lib/python3.
# 5/dist-packages (from scikit-learn==0.20.2->-r requirements.txt (line 1)) (1.17.4)
# Building wheels for collected packages: sklearn
#   Building wheel for sklearn (setup.py) ... done
#   Created wheel for sklearn: filename=sklearn-0.0-py2.py3-none-any.whl
#    size=2397 sha256=71007f0bd2c97bccb750c0167f7adac1979bd623e833b16c37e21ed89b2a7877
#   Stored in directory: /home/repl/.cache/pip/wheels/76/03/bb/589d421d
#   27431bcd2c6da284d5f2286c8e3b2ea3cf1594c074
# Successfully built sklearn
# Installing collected packages: scipy, scikit-learn, sklearn
# Successfully installed scikit-learn-0.20.2 scipy-1.2.0 sklearn-0.0
# /home/repl/.local/lib/python3.5/site-packages/sklearn/ensemble/forest.py:246: FutureWarning: The default value of n_estimators will change from 10 in version 0.20 to 100 in 0.22.
#   "10 in version 0.20 to 100 in 0.22.", FutureWarning)

# Run Python script on command line
python create_model.py

# Add CRON job that runs create_model.py every minute
echo "* * * * * python create_model.py" | crontab

# Verify that the CRON job has been scheduled via CRONTAB
crontab -l
# * * * * * python create_model.py