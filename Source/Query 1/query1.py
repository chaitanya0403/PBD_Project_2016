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
op=open('query1.csv','w')
op.write('method,count\n')
a=sqlContext.sql("SELECT count(text) AS Apple_Pay FROM tweett WHERE text LIKE '%Apple%Pay%' OR text LIKE '%Apple%pay%'").collect()
op.write('Apple_pay,'+str(a[0].Apple_Pay)+'\n')
b=sqlContext.sql("SELECT count(text) AS Paypal FROM tweett WHERE text LIKE '%Paypal%' OR text LIKE '%paypal%'").collect()
op.write('Paypal,'+str(b[0].Paypal)+'\n')
c=sqlContext.sql("SELECT count(text) AS Android_pay FROM tweett WHERE text LIKE '%Android%Pay%' OR text LIKE '%Google%wallet%'").collect()
op.write('Android_pay,'+str(c[0].Android_pay)+'\n')
d=sqlContext.sql("SELECT count(text) AS Samsung_Pay FROM tweett WHERE text LIKE '%Samsung%Pay%' OR text LIKE '%Samsung%pay%'").collect()
op.write('Samsung_pay,'+str(d[0].Samsung_Pay)+'\n')
e=sqlContext.sql("SELECT count(text) AS Bitcoin FROM tweett WHERE text LIKE '%Bitcoin%' OR text LIKE '%bitcoin%'").collect()
op.write('Bitcoin,'+str(e[0].Bitcoin)+'\n')
f=sqlContext.sql("SELECT count(text) AS Square FROM tweett WHERE text LIKE '%Square%' OR text LIKE '%square%'").collect()
op.write('Square,'+str(f[0].Square)+'\n')
g=sqlContext.sql("SELECT count(text) AS Amazon FROM tweett WHERE text LIKE '%Amazon%payments%' OR text LIKE '%amazon%payments%'").collect()
op.write('Amazon_payments,'+str(g[0].Amazon)+'\n')
op.close()
webbrowser.get('firefox').open_new_tab('file:///usr/local/spark/spark-1.6.0/query1.html')

