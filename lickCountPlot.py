#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:51:24 2020

@author: sgupta
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/sgupta/Desktop/CSHLResearch/BehaviorData/20190912_VgatChr2_c7m1")

laserOff = [1, 2, 3, 6, 7, 10, 11, 13, 14, 17, 18, 21, 22, 24, 26, 27, 30, 31, 32, 35, 55, 56]
laserOn = [38, 39, 42, 43, 45, 46, 48, 49, 52]
lickCount = []

for x in range(0, len(laserOn)):
#for x in range(0, len(laserOff)):
    #data = pd.read_csv('20190912_VgatChr2_c7m1_c1_T_' + str(laserOff[x]) + 'DeepCut_resnet50_FrontView_v2Feb12shuffle1_1030000.csv')
    data = pd.read_csv('20190912_VgatChr2_c7m1_c1_T_' + str(laserOn[x]) + 'DeepCut_resnet50_FrontView_v2Feb12shuffle1_1030000.csv')
    
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
            
    lickCount.append(count)

max = 0;
lickCountNormal = [];

for x in range(0, len(lickCount)):
    if(max < lickCount[x]):
        max = lickCount[x]

for x in range(0, len(lickCount)):
    lickCountNormal.append(lickCount[x]/max)

print(lickCountNormal)

#plt.boxplot(lickCountNormal)
#plt.show()
