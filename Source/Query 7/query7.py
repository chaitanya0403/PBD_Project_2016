from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext,functions
import json
import csv
import webbrowser
conf = SparkConf().setAppName('creattable').setMaster('local')
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load('colleges.csv')
df.registerTempTable("tweett")
abc=sqlContext.sql("SELECT Institution_State AS States,count(Institution_State) AS Colleges FROM tweett GROUP BY Institution_State ORDER BY count(Institution_State) DESC")
ls=[]
for a in abc.collect():
  b=a.asDict()
  ls.append(b)

with open('query7.csv', 'w') as outfile:
    fp = csv.DictWriter(outfile, ls[0].keys())
    fp.writeheader()
    fp.writerows(ls)
outfile.close()
webbrowser.get('firefox').open_new_tab('file:///usr/local/spark/spark-1.6.0/query7.html')
