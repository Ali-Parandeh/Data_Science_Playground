# Create the CountVectorizer DataFrame: count_df
count_df = pd.DataFrame(count_train.A, columns= count_vectorizer.get_feature_names())

# Create the TfidfVectorizer DataFrame: tfidf_df
tfidf_df = pd.DataFrame(tfidf_train.A, columns= tfidf_vectorizer.get_feature_names())

# Print the head of count_df
print(count_df.head())

"""        000  00am  0600  10  100  107  11  110  1100  12    ...      younger  \
    0    0     0     0   0    0    0   0    0     0   0    ...            0   
    1    0     0     0   3    0    0   0    0     0   0    ...            0   
    2    0     0     0   0    0    0   0    0     0   0    ...            0   
    3    0     0     0   0    0    0   0    0     0   0    ...            1   
    4    0     0     0   0    0    0   0    0     0   0    ...            0   
    
       youth  youths  youtube  ypg  yuan  zawahiri  zeitung  zero  zerohedge  
    0      0       0        0    0     0         0        0     1          0  
    1      0       0        0    0     0         0        0     0          0  
    2      0       0        0    0     0         0        0     0          0  
    3      0       0        0    0     0         0        0     0          0  
    4      0       0        0    0     0         0        0     0          0  
    
    [5 rows x 5111 columns] """

# Print the head of tfidf_df
print(tfidf_df.head())

"""        000  00am  0600        10  100  107   11  110  1100   12    ...      \
    0  0.0   0.0   0.0  0.000000  0.0  0.0  0.0  0.0   0.0  0.0    ...       
    1  0.0   0.0   0.0  0.105636  0.0  0.0  0.0  0.0   0.0  0.0    ...       
    2  0.0   0.0   0.0  0.000000  0.0  0.0  0.0  0.0   0.0  0.0    ...       
    3  0.0   0.0   0.0  0.000000  0.0  0.0  0.0  0.0   0.0  0.0    ...       
    4  0.0   0.0   0.0  0.000000  0.0  0.0  0.0  0.0   0.0  0.0    ...       
    
        younger  youth  youths  youtube  ypg  yuan  zawahiri  zeitung      zero  \
    0  0.000000    0.0     0.0      0.0  0.0   0.0       0.0      0.0  0.033579   
    1  0.000000    0.0     0.0      0.0  0.0   0.0       0.0      0.0  0.000000   
    2  0.000000    0.0     0.0      0.0  0.0   0.0       0.0      0.0  0.000000   
    3  0.015175    0.0     0.0      0.0  0.0   0.0       0.0      0.0  0.000000   
    4  0.000000    0.0     0.0      0.0  0.0   0.0       0.0      0.0  0.000000   
    
       zerohedge  
    0        0.0  
    1        0.0  
    2        0.0  
    3        0.0  
    4        0.0  
    
    [5 rows x 5111 columns] """

# Calculate the difference in columns: difference
difference = set(count_df.columns) - set(tfidf_df.columns)
print(difference)

# set()

# Check whether the DataFrames are equal
print(count_df.equals(tfidf_df))

# False