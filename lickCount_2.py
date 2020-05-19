#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:42:12 2020

@author: sgupta
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/sgupta/Desktop/CSHLResearch/BehaviorData/20190911_VgatChr2_c7m1")
data = pd.read_csv('20190911_VgatChr2_c7m1_c1_T_1DeepCut_resnet50_FrontView_v2Feb12shuffle1_1030000.csv')

tonguex,tonguey = data.iloc[2:,10],data.iloc[2:,11]
y = tonguey.astype(float)
x = tonguex.astype(float)
l = data.iloc[2:,12]
like = l.astype(float)
tongue = []
time = []
largest = 0
normal = []
count = 0
up = 1
value = 0

for x in range(0, len(l)):
    if (like.iat[x] > 0.9):
        tongue.append(y.iat[x])
        time.append(x/100)
        if (largest < y.iat[x]):
            largest = y.iat[x]

for x in range(0, len(tongue)):
    normal.append(tongue[x]/largest)
    
for x in range(0, len(normal)):
    if (normal[x] >= .85)
        if (value > 1):
            if (normal[x] >= value):
                value = normal[x]
            else:
                count = count + 1
                up = 0
        if (up == 0):
            if (normal[x] <= value):
                value = normal[x]
            else:
                count = count + 1
                up = 1
        
print(count)
plt.plot(time,normal)
plt.show()
