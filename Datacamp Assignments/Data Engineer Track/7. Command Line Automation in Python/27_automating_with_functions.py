# Funky clusters

# You need to write an integration test that verifies that your cloud environment 
# can run KMeans clustering algorithms. One issue you have had in the past is that 
# it gets tedious to keep rewriting code that needs minor changes. You have learned 
# that you can accomplish these small changes by creating a command line tool instead. 
# To prepare your code to become a command line tool, first you must refactor it into 
# functions. Write two functions that make your code ready to be run by a command line tool library.

from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans

# create sample blobs from sklearn datasets
def blobs():
    X, y = make_blobs(n_samples=10, centers=3, n_features=2,random_state=0)

    # (array([[ 1.12031365,  5.75806083],
    #     [ 1.7373078 ,  4.42546234],
    #     [ 2.36833522,  0.04356792],
    #     [ 0.87305123,  4.71438583],
    #     [-0.66246781,  2.17571724],
    #     [ 0.74285061,  1.46351659],
    #     [-4.07989383,  3.57150086],
    #     [ 3.54934659,  0.6925054 ],
    #     [ 2.49913075,  1.23133799],
    #     [ 1.9263585 ,  4.15243012]]), array([0, 0, 1, 0, 2, 2, 2, 1, 1, 0]))

    return X,y
  
# Perform KMeans cluster
def cluster(X, random_state=170, num=2):
    return KMeans(n_clusters=num, random_state=random_state).fit_predict(X) # Returns cluster assignment

#Run everything:  Call both functions. `X` creates the data and `cluster`, clusters the data.
def main():
    X,_ = blobs()
    return cluster(X)

print(main()) #print the KMeans cluster assignments

# Great job at getting this code organized into functions. 
# This will save you time when you turn this into a command line tool. 
# You were able to write two functions that each performed separate actions 
# and then use a main function to call them both.