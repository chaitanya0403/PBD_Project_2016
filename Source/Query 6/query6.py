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
abc=sqlContext.sql("SELECT count(entities.urls[0])*100/count(id) AS percent FROM tweett").collect()
b=abc[0].asDict()
print(b)
with open('query6.csv', 'w') as outfile:
    fp = csv.DictWriter(outfile, b.keys())
    fp.writeheader()
    fp.writerow(b)
outfile.close()
message="""<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <script src="http://d3js.org/d3.v3.min.js" language="JavaScript"></script>
    <script src="liquidFillGauge.js" language="JavaScript"></script>
    <style>
        .liquidFillGaugeText { font-family: Helvetica; font-weight: bold; }
    </style>
</head>
<body>
<svg id="fillgauge1" width="97%" height="250"></svg>
<script language="JavaScript">
    
    
    var config1 = liquidFillGaugeDefaultSettings();
    config1.circleThickness = 0.2;
    config1.textVertPosition = 0.2;
    config1.waveAnimateTime = 2000;
    config1.waveHeight = 0.05;
    config1.waveAnimate = true;
    config1.waveRise = false;
    config1.waveHeightScaling = false;
    config1.waveOffset = 0.25;
    config1.textSize = 0.75;
    config1.waveCount = 3;
    var gauge1 = loadLiquidFillGauge("fillgauge1","""+str(int(b['percent']))+""",config1);

</script>
</body>
</html>"""
x=open("query6.html","w")
x.write(message)
x.close()
webbrowser.get('firefox').open_new_tab('file:///usr/local/spark/spark-1.6.0/query6.html')
