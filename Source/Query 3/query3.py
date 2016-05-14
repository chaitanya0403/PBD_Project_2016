from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext,functions
import csv
import webbrowser
conf = SparkConf().setAppName('creattable').setMaster('local')
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
df = sqlContext.read.json("data2.json")
df.registerTempTable("tweett")
abc=sqlContext.sql("SELECT SUBSTRING(user.created_at,27,4) AS date,count(SUBSTRING(user.created_at,27,4)) AS close FROM tweett GROUP BY SUBSTRING(user.created_at,27,4) ORDER BY SUBSTRING(user.created_at,27,4) DESC")
ls=[]
for a in abc.collect():
  b=a.asDict()
  ls.append(b)

with open('query3.csv', 'w') as outfile:
    fp = csv.DictWriter(outfile, ls[0].keys())
    fp.writeheader()
    fp.writerows(ls)
outfile.close()
webbrowser.get('firefox').open_new_tab('file:///usr/local/spark/spark-1.6.0/query3.html')
