# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:18:06 2020

@author: SivaniDwarampudi
"""

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 pyspark-shell'
#    Spark
from pyspark import SparkContext
#    Spark Streaming
from pyspark.streaming import StreamingContext
#    Kafka
from pyspark.streaming.kafka import KafkaUtils
#    json parsing
import json
sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
sc.setLogLevel("WARN")
ssc = StreamingContext(sc, 60)
kafkaStream = KafkaUtils.createStream(ssc, 'cdh57-01-node-01.moffatt.me:2181', 'spark-streaming', {'twitter':1})
parsed = kafkaStream.map(lambda v: json.loads(v[1]))
authors_dstream = parsed.map(lambda tweet: tweet['user']['screen_name'])
#
author_counts = authors_dstream.countByValue()
author_counts.pprint()
author_counts_sorted_dstream = author_counts.transform(\
  (lambda foo:foo\
   .sortBy(lambda x:( -x[1]))))
author_counts_sorted_dstream.pprint()
top_five_authors = author_counts_sorted_dstream.transform\
  (lambda rdd:sc.parallelize(rdd.take(5)))
top_five_authors.pprint()
filtered_authors = author_counts.filter(lambda x:\
                                                x[1]>1 \
                                                or \
                                                x[0].lower().startswith('rm'))

parsed.\
    flatMap(lambda tweet:tweet['text'].split(" "))\
    .countByValue()\
    .transform\
      (lambda rdd:rdd.sortBy(lambda x:-x[1]))\
    .pprint()
ssc.start()
ssc.awaitTermination()