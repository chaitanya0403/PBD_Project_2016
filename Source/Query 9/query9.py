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
abc=sqlContext.sql("SELECT encode(user.name,'UTF-8') AS Name,max(user.followers_count) AS Folloers_Count FROM tweett WHERE user.verified=True GROUP BY user.name ORDER BY max(user.followers_count) DESC LIMIT 10")
ls=[]
for a in abc.collect():
  b=a.asDict()
  ls.append(b)

with open('query9.csv', 'w') as outfile:
    fp = csv.DictWriter(outfile, ls[0].keys())
    fp.writeheader()
    fp.writerows(ls)
outfile.close()
webbrowser.get('firefox').open_new_tab('file:///usr/local/spark/spark-1.6.0/query9.html')
