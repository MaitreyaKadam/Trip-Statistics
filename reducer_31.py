#!/usr/bin/env python3
##This code is written by Maitreya Milind Kadam(s4087536) and Dhruvi Trivedi(s4146514) for A1(Task3): Big Data processing.
import sys
#variables to track the taxi, company, and number of trips that taxi had
taxi = None
comp_taxi = None
trip_no = 0
for each_line in sys.stdin: #reads each line which is emitted by the mapper
    each_line = each_line.strip() #the strip() method removes the whitespaces
    line = each_line.split('\t') #splits the line into desired attributes
    if len(line) != 3:
        continue
    taxi_id, tag, val = line #the desired attributes are extracted from the read input
    if taxi_id != taxi:
        if taxi is not None and comp_taxi is not None: #emits one line for every trip that the previous taxi had
            for _ in range(trip_no):
                print(f"{comp_taxi}\t1")
        taxi = taxi_id #updates the variables for the new taxi id
        comp_taxi = None
        trip_no = 0
    if tag == 'Taxi': #if the line from the mapper is a taxi record, it stores the company
        comp_taxi = val
    elif tag == 'Trip': #if the line from the mapper is a trip record, it increments the trip count number
        trip_no += 1
#it emits the remaining trips for the last taxi id when the loop ends
if taxi is not None and comp_taxi is not None:
    for _ in range(trip_no):
        print(f"{comp_taxi}\t1")
