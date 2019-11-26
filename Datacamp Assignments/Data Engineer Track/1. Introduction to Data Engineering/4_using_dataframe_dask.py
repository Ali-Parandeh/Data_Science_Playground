import dask.dataframe as dd

# Set the number of pratitions
athlete_events_dask = dd.from_pandas(athlete_events, npartitions = 4)

# Calculate the mean Age per Year
print(athlete_events_dask.groupby('Year').Age.mean().compute())

# <script.py> output:
#     Year
#     1896    23.580645
#     1900    29.034031
#     1904    26.698150
#     1906    27.125253
#     1908    26.970228
#     1912    27.538620
#     1920    29.290978
#     1924    28.373325
#     1928    29.112557
#     1932    32.582080
#     1936    27.530328
#     1948    28.783947
#     1952    26.161546
#     1956    25.926674
#     1960    25.168848
#     1964    24.944397
#     1968    24.248046
#     1972    24.308607
#     1976    23.841818
#     1980    23.694743
#     1984    23.898347
#     1988    24.079432
#     1992    24.318895
#     1994    24.422103
#     1996    24.915045
#     1998    25.163197
#     2000    25.422504
#     2002    25.916281
#     2004    25.639515
#     2006    25.959151
#     2008    25.734118
#     2010    26.124262
#     2012    25.961378
#     2014    25.987324
#     2016    26.207919
#     Name: Age, dtype: float64

# Using the DataFrame abstraction makes parallel computing easier. This abstraction is often used in the big data world, for example in Apache Spark.

