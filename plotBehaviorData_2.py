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
#%%

time = np.arange(0,1500)/100
#%%
tonguex,tonguey = data.iloc[2:,10],data.iloc[2:,11]
l = data.iloc[2:,12]
like = l.astype(float)

y = tonguey.astype(float)
plt.plot(time,tonguey.astype(float))
plt.plot(time,like)
plt.show()
