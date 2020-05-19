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

count = 0
tonguex,tonguey = data.iloc[2:,10],data.iloc[2:,11]
y = tonguey.astype(float)
x = tonguex.astype(float)
l = data.iloc[2:,12]
like = l.astype(float)
time = np.arange(0,len(l))/100
largest = 0
normalized = []
lick = []
normalized2 = []


for x in range(0, len(l)):
    if (like.iat[x] < 0.9):
        y.iat[x] = np.nan
    if (like.iat[x] > 0.9):
        if (largest < y.iat[x]):
            largest = y.iat[x]

for x in range(0, len(l)):
    if(y.iat[x] == np.nan):
        normalized.append(np.nan)
    else:
        normalized.append(y.iat[x]/largest)
        
for x in range(0, len(l)):
    if(np.isnan(normalized[x]) == True):
        normalized2.append(0)
    if(np.isnan(normalized[x]) == False):
        normalized2.append(1)

for x in range(0, len(l)):
    if ((normalized2[x] - normalized2[x-1]) == 1):
        lick.append(x/100)
        count = count + 1
        
#%%
print(count)
yy = np.ones([len(lick),1])*0.85
plt.plot(time,normalized)
plt.plot(lick,yy,'*')
plt.show()
