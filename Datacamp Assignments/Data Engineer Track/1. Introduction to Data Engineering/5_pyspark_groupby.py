# Print the type of athlete_events_spark
print(type(athlete_events_spark))

# Print the schema of athlete_events_spark
print(athlete_events_spark.printSchema())

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean("Age"))

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean("Age").show())


# In [4]: athlete_events_spark
# Out[4]: DataFrame[ID: int, Name: string, Sex: string, Age: int, Height: string, Weight: string, Team: string, NOC: string, Games: string, Year: int, Season: string, City: string, Sport: string, Event: string, Medal: string]

# In [7]: print(type(athlete_events_spark))
# <class 'pyspark.sql.dataframe.DataFrame'>

# In [8]: print(athlete_events_spark.printSchema())
# root
#  |-- ID: integer (nullable = true)
#  |-- Name: string (nullable = true)
#  |-- Sex: string (nullable = true)
#  |-- Age: integer (nullable = true)
#  |-- Height: string (nullable = true)
#  |-- Weight: string (nullable = true)
#  |-- Team: string (nullable = true)
#  |-- NOC: string (nullable = true)
#  |-- Games: string (nullable = true)
#  |-- Year: integer (nullable = true)
#  |-- Season: string (nullable = true)
#  |-- City: string (nullable = true)
#  |-- Sport: string (nullable = true)
#  |-- Event: string (nullable = true)
#  |-- Medal: string (nullable = true)

# None


# In [9]: print(athlete_events_spark.groupBy('Year').mean("Age"))
# DataFrame[Year: int, avg(Age): double]

# In [10]: print(athlete_events_spark.groupBy('Year').mean("Age").show())
# +----+------------------+
# |Year|          avg(Age)|
# +----+------------------+
# |1896|23.580645161290324|
# |1924|28.373324544056253|
# |2006|25.959151072569604|
# |1908|26.970228384991845|
# |1952|26.161546085232903|
# |1956|25.926673567977915|
# |1988|24.079431552931485|
# |1994|24.422102596580114|
# |1968|24.248045555448314|
# |2014|25.987323655694134|
# |1904| 26.69814995131451|
# |2004|25.639514989213716|
# |1932| 32.58207957204948|
# |1996|24.915045018878885|
# |1998|25.163197335553704|
# |1960|25.168848457954294|
# |2012| 25.96137770897833|
# |1912| 27.53861997940268|
# |2016| 26.20791934541204|
# |1936|27.530328324986087|
# +----+------------------+
# only showing top 20 rows

# None