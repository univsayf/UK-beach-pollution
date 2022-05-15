#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 12:39:31 2021

@author: atmsayfuddin
"""

import pandas as pd
import math

#%%
# Distance function
def distance(origin, destination):
    """
    Calculate the Haversine distance in miles.
    
    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)
    Returns
    -------
    distance_in_km : float
    Examples
    --------
    >>> origin = (48.1372, 11.5756)  # Munich
    >>> destination = (52.5186, 13.4083)  # Berlin
    >>> round(distance(origin, destination), 1)
    504.2
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 3959  # change radius value to 6371 for distance in kilometer.
    # Note: some algorithms use radious = 3956 or 6367 for mile or kilometer, respectively.
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c
    return d


#%%
beach = pd.read_excel (r'Beachwatch_AllData_1994-23.01.21inc Public Source Litter YChen.xlsx')
hotel = pd.read_excel (r'UKCensusDatabaseFromSTR.xlsx')

# In the beach data, keeping each unique beach 
beach = beach.drop_duplicates(subset=['BeachID'])
beach = beach.reset_index(drop = True)

# Creating a tuple for each coordinates in the beach data and hotel data
beach['coordinates'] = beach[['Beach Latitude','Beach Longitude']].apply(tuple, axis=1)
hotel['coordinates'] = hotel[['Latitude','Longitude']].apply(tuple, axis=1)

# Filtering out closed hotels
hotel = hotel[hotel['Rooms']>0]
hotel = hotel.reset_index(drop = True)

# Checking the distance function 
distance(beach['coordinates'][1], hotel['coordinates'][1])

# Creating a new, empty column in the hotel dataset for entering the closest beach later
hotel['nearBeach'] = '0'


#%%
'''
Description of the algorithm: 
    for each beach, I compare the distance between the beach (from the beach data)
    and the hotel (from STR's data). If a hotel is within 15 miles from the 
    beach then I record the beach ID and the distance in the "nearBeach" column
    of the hotel data. Once all rows/hotels of the hotel dataset have been evaluated,
    I move on to the next beach.
    
    For the next beach, I first check if a given hotel has already paired with an 
    earlier beach. If no, then algorithm from the first paragraph is used. Otherwise,
    I check whether the distance from the current beach is shorter than the distance 
    from the earlier beach. If so, I update the corresponding value on the "nearBeach"
    column by the current beachID and distance. 
'''
for i in range(len(beach)):
    for j in range(len(hotel)):
        durotto = distance(beach['coordinates'][i], hotel['coordinates'][j])
        if hotel['nearBeach'][j]=='0':    
            if durotto <= 30:
                hotel.at[j, 'nearBeach'] = [beach['BeachID'][i], durotto]
        else:
            if durotto < hotel['nearBeach'][j][1]:
                hotel.at[j, 'nearBeach'] = [beach['BeachID'][i], durotto]
                

#%%

# New dataframe with the hotels that are paired with a beach (filtering out the hotels
# that are more than 30 miles away from the nearest beach)        
hotel1 = hotel[hotel['nearBeach']!='0']

# Creating new columns for the BeachID and distance
hotel1['BeachID'] = hotel1['nearBeach'].apply(lambda x: x[0])
hotel1['distance'] = hotel1['nearBeach'].apply(lambda x: x[1])

# Resetting index
hotel1 = hotel1.reset_index(drop = True)
# Producing a csv file of hotel1
hotel1.to_csv("hotelsWithin30Miles.csv")










