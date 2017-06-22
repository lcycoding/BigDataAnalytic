#!/usr/bin/env python
"""
Masked wordcloud
================

Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

from wordcloud import (WordCloud, get_single_color_func)
import nltk
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.sql.functions import UserDefinedFunction
from pyspark.sql.types import StringType
from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark.mllib.util import MLUtils
from pyspark.mllib.regression import LabeledPoint
from functools import reduce
from pyspark.sql import DataFrame

conf = SparkConf().setAppName("dataProcessor")
sc = SparkContext(conf = conf)
sqc = SQLContext(sc)



d = path.dirname(__file__)




print "step 1"

text = open('../../jr_new_.txt').read()
text_split = text.split(" ")
false_words = []
words = []

show_text = ""
i = 1 
for t in text_split:
	temp = t.lower()
	i += 1
	if i < 1500000:
		if temp in words:
			show_text += " "
			show_text += temp
		elif temp in false_words:
			continue
		
		
		elif len(temp) >1:
			if temp != 'much' and temp != 'last' and temp != 'next' and temp != 'green' and temp != 'many' :  
				if pos_tag(word_tokenize(temp))[0][1] == 'JJ'  :
					show_text += " "
					show_text += temp
					words.append(temp)
				else:
					false_words.append(temp)
					print i , len(text_split) ,  i*100 / len(text_split) 
	else:
		break

print "step 2"
# words = []
# words_count = []
#for f in filtered_words:
#  for t in f :
#    temp = t.lower()
#    if temp != 'much' and temp != 'last' and temp != 'next' and temp != 'green' :  
#      if pos_tag(word_tokenize(temp))[0][1] == 'JJ'  :
#            text += " "
#            text += temp




print "step 3"

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = np.array(Image.open(path.join(d, "names/JR5.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=3000, mask=alice_mask,
               stopwords=stopwords)
# generate word cloud
wc.generate(show_text)

# store to file
wc.to_file(path.join(d, "JR.png"))

