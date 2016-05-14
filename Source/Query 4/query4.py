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
abc=sqlContext.sql("SELECT encode(text,'UTF-8') AS text,MAX(retweeted_status.favorite_count) AS Favorite FROM tweett GROUP BY text ORDER BY MAX(retweeted_status.favorite_count) DESC LIMIT 10").collect()
ls=[]
print(abc)
for a in abc:
  b=a.asDict()
  ls.append(b)

with open('query4.csv', 'w') as outfile:
    fp = csv.DictWriter(outfile, ls[0].keys())
    fp.writeheader()
    fp.writerows(ls)
outfile.close()
webbrowser.get('firefox').open_new_tab('file:///usr/local/spark/spark-1.6.0/query4.html')
