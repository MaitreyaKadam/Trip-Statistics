#!/usr/bin/env python3
##This code is written by Maitreya Milind Kadam(s4087536) and Dhruvi Trivedi(s4146514) for A1(Task1): Big Data processing.
import sys
from collections import defaultdict
#final aggregated trip stats
f_t_stats=defaultdict(lambda:[0,float('-inf'),float('inf'),0.0])
#read the input from the mapper
for each_line in sys.stdin:
    each_line=each_line.strip()
    parts=each_line.split()
    t_id,t_type=parts[0],parts[1]
    p_key=(t_id,t_type) 
    n_trips=int(parts[2]) #extracts no of trips from the array.
    max_f=float(parts[3]) #takes the max fare of the trip
    min_f=float(parts[4]) #takes the min fare of the trip
    t_fare=float(parts[5]) #takes the total fare for the trip
    f_t_stats[p_key][0]+=n_trips #final trip stats
    f_t_stats[p_key][1]=max(f_t_stats[p_key][1],max_f) #updates the maximum fare after comparing it with the previous maximum fare
    f_t_stats[p_key][2]=min(f_t_stats[p_key][2],min_f) #updates the minimum fare after comparing it with the previous minimum fare
    f_t_stats[p_key][3]+=t_fare  #calculates the total fare
for (t_id,t_type), (n_trips,max_f,min_f,t_fare) in f_t_stats.items():
    avg_fare=t_fare/n_trips #calculates the average fare.
    print(f"{t_id}\t{t_type}\t{n_trips}\t{max_f:.2f}\t{min_f:.2f}\t{avg_fare:.2f}")
    