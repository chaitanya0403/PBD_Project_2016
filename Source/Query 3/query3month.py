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
abc=sqlContext.sql("SELECT CONCAT(SUBSTRING(user.created_at,27,4),SUBSTRING(user.created_at,5,3)) AS date,count(SUBSTRING(user.created_at,5,3)) AS close FROM tweett GROUP BY SUBSTRING(user.created_at,27,4),SUBSTRING(user.created_at,5,3) ORDER BY SUBSTRING(user.created_at,27,4) DESC,CASE SUBSTRING(user.created_at,5,3) when 'Jan' then 1 when 'Feb' then 2 when 'Mar' then 3 when 'Apr' then 4 when 'May' then 5 when 'Jun' then 6 when 'Jul' then 7 when 'Aug' then 8 when 'Sep' then 9 when 'Oct' then 10 when 'Nov' then 11 when 'Dec' then 12 END DESC")
ls=[]
for a in abc.collect():
  b=a.asDict()
  ls.append(b)

with open('query3month.csv', 'w') as outfile:
    fp = csv.DictWriter(outfile, ls[0].keys())
    fp.writeheader()
    fp.writerows(ls)
outfile.close()
webbrowser.get('firefox').open_new_tab('file:///usr/local/spark/spark-1.6.0/query3month.html')
