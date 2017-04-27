from pyspark.sql import SQLContext
from pyspark import SparkConf,SparkContext

# setting up spark config, SQLContext
conf = SparkConf().setAppName("Hw3_2")
sc = SparkContext( conf = conf )
sqC = SQLContext(sc)

# construct spark SQL context and select needed column
# filter several info
df = sqC.read.format('com.databricks.spark.csv').options(header = 'true', inferschema = 'true').load('yellow_tripdata_2016-01.csv')
dz = df.select("passenger_count","payment_type").filter( df.passenger_count > 0 )

# group up data and get average
dc = dz.groupBy("payment_type").mean()
dc.show()
