#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:15:41 2019

@author: sgupta
"""

import scipy.io
import os
import numpy as np

os.chdir("/Users/sgupta/Desktop/CSHLResearch/LaserScanningData/20190911_VgatChr2_c7m1")

#First get user to input the location and index number of which sequence
#So bascially the function will call on temp.py to retrieve the location
# and the first column will have the trial number

#then the program will go to the csv file to extract the y data sets for each body part

#plot time by y