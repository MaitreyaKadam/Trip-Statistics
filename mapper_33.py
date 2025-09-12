#!/usr/bin/env python3
##This code is written by Maitreya Milind Kadam
import sys
for each_line in sys.stdin: #reads each line from the job 2
    each_line=each_line.strip() #removes excess spaces from the line
    taxi_comp, trip_count=each_line.split('\t') #splits the line from job 2 into taxi company and trip count for that company so that it can be sorted
    print(f"0\t{trip_count.zfill(6)}\t{taxi_comp}\t{trip_count}") #we have emitted a composite key so as to partition properly and sort it for job3
