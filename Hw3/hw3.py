from pyspark import SparkConf, SparkContext

# spark configuration setting
conf = (SparkConf().setAppName("Hw3"))
sc = SparkContext( conf = conf )

# read text file in spark program
ttf = sc.textFile("IhaveaDream.txt")

# map the word and reduce it, then sort
cc = ttf.flatMap(lambda line: line.split(" ")) \
	.map(lambda word: (word , 1)) \
	.reduceByKey(lambda a, b: a + b) \
	.map(lambda (a,b) : (b,a)) \
	.sortByKey(0)

# print every word's frequency
for x in cc.collect():
	print x
