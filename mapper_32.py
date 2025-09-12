#!/usr/bin/env python3
##This code is written by Maitreya Milind Kadam.
import sys
for each_line in sys.stdin: #reads each line from job1
    each_line=each_line.strip() #removes excess spaces
    taxi_comp,trip_count=each_line.split('\t') #splits the line into company and trip count no
    print(f"{taxi_comp}\t{trip_count}") #emits both the attributes to the reducer