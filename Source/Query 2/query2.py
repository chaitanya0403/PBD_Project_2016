from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext,functions
import json
import csv
import webbrowser
conf = SparkConf().setAppName('creattable').setMaster('local')
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
df = sqlContext.read.json("data2.json")
df.registerTempTable("tweett")
abc=sqlContext.sql("SELECT SUBSTRING(created_at,1,3) AS day,count(SUBSTRING(created_at,1,3)) AS daycount FROM tweett GROUP BY SUBSTRING(created_at,1,3) ORDER BY count(SUBSTRING(created_at,1,3)) DESC")
ls=[]
for a in abc.collect():
  b=a.asDict()
  ls.append(b)

with open('query2.csv', 'w') as outfile:
    fp = csv.DictWriter(outfile, ls[0].keys())
    fp.writeheader()
    fp.writerows(ls)
outfile.close()
webbrowser.get('firefox').open_new_tab('file:///usr/local/spark/spark-1.6.0/query2.html')

