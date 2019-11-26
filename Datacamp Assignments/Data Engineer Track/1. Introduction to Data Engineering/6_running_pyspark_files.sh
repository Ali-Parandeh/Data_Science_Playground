cat /home/repl/spark-script.py

# from pyspark.sql import SparkSession

# if __name__ == "__main__":
#     spark = SparkSession.builder.getOrCreate()
#     athlete_events_spark = (spark
#         .read
#         .csv("/home/repl/datasets/athlete_events.csv",
#              header=True,
#              inferSchema=True,
#              escape='"'))

#     athlete_events_spark = (athlete_events_spark
#         .withColumn("Height",
#                     athlete_events_spark.Height.cast("integer")))

#     print(athlete_events_spark
#         .groupBy('Year')
#         .mean('Height')
#         .orderBy('Year')
#         .show())

spark-submit --master local[4] /home/repl/spark-script.py

# Picked up _JAVA_OPTIONS: -Xmx512m
# Picked up _JAVA_OPTIONS: -Xmx512m
# 19/11/26 02:56:19 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
# +----+------------------+
# |Year|       avg(Height)|
# +----+------------------+
# |1896| 172.7391304347826|
# |1900|176.63793103448276|
# |1904| 175.7887323943662|
# |1906|178.20622568093384|
# |1908|177.54315789473685|
# |1912| 177.4479889042996|
# |1920| 175.7522816166884|
# |1924|174.96303901437372|
# |1928| 175.1620512820513|
# |1932|174.22011541632315|
# |1936| 175.7239932885906|
# |1948|176.17279726261762|
# |1952|174.13893967093236|
# |1956|173.90096798212957|
# |1960|173.14128595600675|
# |1964|  173.448573701557|
# |1968| 173.9458648072826|
# |1972|174.56536284096757|
# |1976|174.92052773737794|
# |1980|175.52748832195473|
# +----+------------------+
# only showing top 20 rows

# None