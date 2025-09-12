#!/bin/bash
##This bash script is written by Maitreya Milind Kadam.
hadoop fs -rm -f -r /input  
hadoop fs -rm -f -f /output
hadoop fs -mkdir /Input
hadoop fs -mkdir /Output
hadoop fs -copyFromLocal ./Trips.txt /Input/Trips.txt
chmod +x mapper_1.py
chmod +x reducer_1.py
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D stream.map.output.field.separator=\t \
-D stream.num.map.output.key.fields=2 \
-D mapred.text.key.partitioner.options=-k1,2 \
-D mapred.reduce.tasks=3 \
-file ./mapper_1.py \
-mapper "python3 mapper_1.py" \
-file ./reducer_1.py \
-reducer "python3 reducer_1.py" \
-input /Input/Trips.txt \
-output /Output/Task1 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
hadoop fs -cat /Output/Task1/part-00000
hadoop fs -cat /Output/Task1/part-00001
hadoop fs -cat /Output/Task1/part-00002
