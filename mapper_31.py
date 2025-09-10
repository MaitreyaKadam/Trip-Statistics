#!/usr/bin/env python3
##This code is written by Maitreya Milind Kadam(s4087536) and Dhruvi Trivedi(s4146514) for A1(Task3): Big Data processing.
import sys
for each_line in sys.stdin: #reads each line from the input files
    each_line=each_line.strip() #the strip() method removes the whitespaces
    trips_taxis=each_line.split(',') #the variables are separated by ','
    if len(trips_taxis)==4: #if the file is taxis.txt 
        t_number,taxi_comp,taxi_model,year=trips_taxis
        print(f"{t_number}\tTaxi\t{taxi_comp}") #emits the taxi_id and company to the mapper
    elif len(trips_taxis)==8: #if the file is trips.txt
        trip_id,t_number,fare,trip_d,pickx,picky,dropx,dropy=trips_taxis
        print(f"{t_number}\tTrip\t1") #emits the taxi_id from the trips.txt file to the mapper.

