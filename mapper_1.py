#!/usr/bin/env python3
##This code is written by Maitreya Milind Kadam
import sys
from collections import defaultdict
# Initialize a dictionary to store trip statistics
t_stats = defaultdict(lambda: [0, float('-inf'), float('inf'), 0.0])
# Process each line of the input
for each_line in sys.stdin:
    each_line = each_line.strip()  # Remove any leading or trailing spaces
    parts = each_line.split(',')  # Split the line into parts by commas
    taxi_id = parts[1]  # Extract the taxi ID
    fare = float(parts[2])  # Convert the fare to a float
    trip_d = float(parts[3])  # Convert the distance to a float
    # Classify the trip type based on the distance
    if trip_d>=200:
        trip_type='long'
    elif trip_d>=100:
        trip_type='medium'
    else:
        trip_type='short'
    # Create a unique key using taxi ID and trip type
    primary_k=(taxi_id, trip_type)
    # Update the trip statistics for this key
    t_stats[primary_k][0]+=1  # Increment the number of trips
    t_stats[primary_k][1]=max(t_stats[primary_k][1], fare)  # Update the max fare
    t_stats[primary_k][2]=min(t_stats[primary_k][2], fare)  # Update the min fare
    t_stats[primary_k][3]+=fare  # Add the fare to the total fare
#prints the desired results by iterating through the dictionary
for (taxi_id, trip_type), (num_trips, max_fare, min_fare, total_fare) in t_stats.items():
    print(f"{taxi_id}\t{trip_type}\t{num_trips}\t{max_fare:.2f}\t{min_fare:.2f}\t{total_fare:.2f}")
