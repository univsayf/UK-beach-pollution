#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 22:27:16 2022

@author: atmsayfuddin
"""

import pandas as pd
import numpy as np

# Loading data sets: (a) beach sample and (b) hotel sample
beachSample = pd.read_csv("https://raw.githubusercontent.com/univsayf/UK-beach-pollution/main/SelectingBeaches/BeachIDs.csv?token=GHSAT0AAAAAABUOBQ65VCBNJMMSDHP4LXKWYUBYAVA")
del beachSample['Unnamed: 0']

## Note: the hotelSammple data below contains hotels within 30 miles of each 
# beach from the original beach polllution data set shared by Yong
hotelSample= pd.read_csv("https://raw.githubusercontent.com/univsayf/UK-beach-pollution/main/SelectingHotels/hotelsWithin30Miles.csv?token=GHSAT0AAAAAABUOBQ65HYCL2EDRMV64GPHCYUBYD5A")
del hotelSample['Unnamed: 0']

# Selecting hotels for the 225 pre-identified beaches from the beachSample data above
hotels30 = hotelSample[hotelSample['BeachID'].isin(beachSample['BeachID'])]

# hotels30 contains 1017hotels
len(hotels30)

# hotels30 has 120 beaches
len(np.unique(hotels30['BeachID']))

# hotels30 is the final sample of hotels that are within a 30-mile radius from the nearest beach