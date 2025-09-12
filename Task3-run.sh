#!/bin/bash
##This bash script is written by Maitreya Milind Kadam.
hadoop fs -rm -f -r /input  
hadoop fs -rm -f -f /output
hadoop fs -mkdir /Input
hadoop fs -mkdir /Output
hadoop fs -copyFromLocal ./Trips.txt /Input/Trips.txt
hadoop fs -copyFromLocal ./Taxis.txt /Input/Taxis.txt
chmod +x mapper_31.py
chmod +x reducer_31.py
chmod +x mapper_32.py
chmod +x reducer_32.py
chmod +x mapper_33.py
chmod +x reducer_33.py
#Job1: Join
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D stream.map.output.field.separator=\t \
-D stream.num.map.output.key.fields=1 \
-D mapred.text.key.partitioner.options=-k1,1 \
-D mapred.reduce.tasks=3 \
-file ./mapper_31.py \
-mapper "python3 mapper_31.py" \
-file ./reducer_31.py \
-reducer "python3 reducer_31.py" \
-input /Input/Trips.txt \
-input /Input/Taxis.txt \
-output /Output/Job1_Join \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
#Job2: Counting
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D stream.map.output.field.separator=\t \
-D stream.num.map.output.key.fields=1 \
-D mapred.text.key.partitioner.options=-k1,1 \
-D mapred.reduce.tasks=3 \
-file ./mapper_32.py \
-mapper "python3 mapper_32.py" \
-file ./reducer_32.py \
-reducer "python3 reducer_32.py" \
-input /Output/Job1_Join \
-output /Output/Job2_Count \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
#Job3: Sorting
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D stream.map.output.field.separator=\t \
-D stream.num.map.output.key.fields=3 \
-D mapred.text.key.partitioner.options=-k1,1 \
-D mapred.reduce.tasks=3 \
-file ./mapper_33.py \
-mapper "python3 mapper_33.py" \
-file ./reducer_33.py \
-reducer "python3 reducer_33.py" \
-input /Output/Job2_Count \
-output /Output/Task3 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner