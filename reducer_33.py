#!/usr/bin/env python3
##This code is written by Maitreya Milind Kadam.
import sys
for each_line in sys.stdin: #reads each line from the mapper for job3
    each_line=each_line.strip() #removes excess space from the line from the mapper
    each_line=each_line.split('\t') #splits the line using the \t separator
    taxi_comp=each_line[2] #extracts the taxi company
    trip_count=each_line[3] #extracts the trip count for each taxi_comp
    print(f"{taxi_comp}\t{int(trip_count)}") #prints the sorted taxi_comp along with trip count