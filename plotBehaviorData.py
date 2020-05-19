#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:45:26 2019

@author: sgupta
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/sgupta/Desktop/CSHLResearch/BehaviorData/20190911_VgatChr2_c7m1")
data = pd.read_csv('20190911_VgatChr2_c7m1_c1_T_1DeepCut_resnet50_FrontView_v2Feb12shuffle1_1030000.csv')
print(data.loc[0][1])
xData = []
yData = []
for i in range(2,10):
    try:
        xData.append(data.loc[i][1])
        yData.append(data.loc[i][2])
    except:
        print('a')
plt.plot(xData, yData)
plt.title('Nose')
plt.show()
#%%

time = np.arange(0,1500)/100
#%%
nosex,nosey = data.iloc[2:,1],data.iloc[2:,2]

plt.plot(time,np.array(nosey))
plt.show()
