from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext,functions
import json
import csv
import webbrowser
conf = SparkConf().setAppName('creattable').setMaster('local')
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
df = sqlContext.read.json("bmsm.json")
df.registerTempTable("tweett")
abc=sqlContext.sql("SELECT lang AS Language,count(lang) AS count FROM tweett GROUP BY lang ORDER BY count(lang) DESC")
ls=[]
for a in abc.collect():
  b=a.asDict()
  ls.append(b)

with open('query5.csv', 'w') as outfile:
    fp = csv.DictWriter(outfile, ls[0].keys())
    fp.writeheader()
    fp.writerows(ls)
outfile.close()
webbrowser.get('firefox').open_new_tab('file:///usr/local/spark/spark-1.6.0/query5.html')
