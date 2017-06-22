from pyspark.sql import SQLContext
from pyspark.sql.functions import *
from pyspark.sql.functions import UserDefinedFunction
from pyspark import SparkConf,SparkContext
from pyspark.mllib.tree import RandomForest, RandomForestModel
from pyspark.mllib.util import MLUtils
from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD, LinearRegressionModel
from pyspark.sql.types import StringType
from pyspark.mllib.evaluation import RegressionMetrics
from pyspark.mllib.linalg import DenseVector
from functools import reduce
from pyspark.sql import DataFrame

def adddict(x):
    d = {}
    i = 0
    for k in x.rdd.collect():
        l = k.Code
        d2 = { l : i}
        d.update( d2 )
        i += 1

    return d

def appdict(x):
    d = {}
    i = 0
    for k in x.rdd.collect():
        l = k.iata
        d2 = { l : i}
        d.update( d2 )
        i += 1

    return d

def unionAll(*dfs):
    return reduce(DataFrame.unionAll, dfs)

# Config setting
conf = SparkConf().setAppName("Hw4").set("spark.yarn.driver.memoryOverhead" , "512").set("spark.yarn.executor.memoryOverhead" , "2048").set("spark.executor.memory","4g").set("spark.driver.memory","2g").set("spark.rpc.askTimeout","240s")

sc = SparkContext( conf = conf )

sqC = SQLContext(sc)

# data loading
df = sqC.read.format('com.databricks.spark.csv').options(header = 'true', inferschema = 'true').load('2003.csv')
df2 = sqC.read.format('com.databricks.spark.csv').options(header = 'true', inferschema = 'true').load('2004.csv')
df3 = sqC.read.format('com.databricks.spark.csv').options(header = 'true', inferschema = 'true').load('2005.csv')
df4 = sqC.read.format('com.databricks.spark.csv').options(header = 'true', inferschema = 'true').load('2006.csv')
df5 = sqC.read.format('com.databricks.spark.csv').options(header = 'true', inferschema = 'true').load('2007.csv')

valdata = sqC.read.format('com.databricks.spark.csv').options(header = 'true', inferschema = 'true').load('2008.csv')

df = unionAll( df , df2 , df3 , df4 , df5 )

UAC = sqC.read.format('com.databricks.spark.csv').options(header = 'true', inferschema = 'true').load('carriers.csv')
UAC = UAC.select("Code")
AP = sqC.read.format('com.databricks.spark.csv').options(header = 'true', inferschema = 'true').load('airports.csv')
AP = AP.select("iata")

acdict = adddict( UAC )
apdict = appdict( AP )

def ac(x):
    return acdict.get(x)

def ap(x):
    return apdict.get(x)

# select and switch stringtype into numeric value
dz = df.select("Month","UniqueCarrier","Diverted","ArrDelay","DepDelay","Distance","NASDelay","WeatherDelay").replace( "NA" , "0" )
trueData = valdata.select("Month","UniqueCarrier","Diverted","ArrDelay","DepDelay","Distance","NASDelay","WeatherDelay").replace( "NA" , "0" )

# dictionary check, value switching
name = 'UniqueCarrier'
udf = UserDefinedFunction(lambda x: acdict.get(x), StringType())
data3 = dz.select(*[udf(column).alias(name) if column == name else column for column in dz.columns])
data_post = trueData.select(*[udf(column).alias(name) if column == name else column for column in trueData.columns])
#name = 'Origin'
#udf2 = UserDefinedFunction(lambda x: apdict.get(x), StringType())
#data4 = data3.select(*[udf2(column).alias(name) if column == name else column for column in data3.columns])

#name = 'Dest'
#udf3 = UserDefinedFunction(lambda x: apdict.get(x), StringType())
#data5 = data4.select(*[udf3(column).alias(name) if column == name else column for column in data4.columns])

# debug
data3.show()
data_post.show()

data6 = data3.na.drop()
data_post2 = data_post.na.drop()

# data transformation
dk = data6.rdd
truetestData = data_post2.rdd
data = dk.map( lambda line: LabeledPoint( line[7] , line[0:7] ) )
val_data = truetestData.map( lambda line: LabeledPoint( line[7] , line[0:7] ) )

# debug
print( data.take(1) )
print( val_data.take(1) )

# for holdout validation
(trData, tData) = data.randomSplit([0.7 , 0.3])

# random forest training model
mod = RandomForest.trainRegressor(trData, categoricalFeaturesInfo={ 0:13 , 1:1499 , 2:2 },numTrees=4, featureSubsetStrategy="auto",impurity='variance', maxDepth=8, maxBins=1500)

# prediction and evaluation
predictions = mod.predict(tData.map(lambda x: x.features))
pred = mod.predict(val_data.map(lambda x: x.features))
labelsAndPredictions = tData.map(lambda lp: lp.label).zip(predictions)
truePred = val_data.map(lambda lp: lp.label).zip(pred)
metrics = RegressionMetrics(labelsAndPredictions)
met2 = RegressionMetrics(truePred)
# Squared Error
print("Validation MSE = %s" % metrics.meanSquaredError)
print("Validation RMSE = %s" % metrics.rootMeanSquaredError)
# Mean absolute error
print("Validation MAE = %s" % metrics.meanAbsoluteError)
# Explained variance
print("Explained variance = %s" % metrics.explainedVariance)

# Squared Error
print("Test MSE = %s" % met2.meanSquaredError)
print("Test RMSE = %s" % met2.rootMeanSquaredError)
# Mean absolute error
print("Test MAE = %s" % met2.meanAbsoluteError)
# Explained variance
print("Test Explained variance = %s" % met2.explainedVariance)


# spark-submit --packages com.databricks:spark-csv_2.10:1.5.0 --conf "spark.default.parallelism=50" --conf "spark.yarn.driver.memoryOverhead=400" --conf "spark.yarn.executor.memoryOverhead=2048" hw4.py > LRTT
