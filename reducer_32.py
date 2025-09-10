#!/usr/bin/env python3
##This code is written by Maitreya Milind Kadam(s4087536) and Dhruvi Trivedi(s4146514) for A1(Task3): Big Data processing.
import sys
from collections import defaultdict
count_record = defaultdict(int) #the dictionary helps to record count of each trips of each company
for each_line in sys.stdin: #reads each line from the mapper
    each_line = each_line.strip() #removes excess spaces
    taxi_comp, trip_count = each_line.split('\t') #splits the line from the mapper into taxi company and trip count
    count_record[taxi_comp] += int(trip_count)
for taxi_comp in count_record: #emits to the 3rd job for each record in the dictionary emit the total trip count number for each company
    print(f"{taxi_comp}\t{count_record[taxi_comp]}")
