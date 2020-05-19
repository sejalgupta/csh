# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import scipy.io
import os
import numpy as np

os.chdir("/Users/sgupta/Desktop/CSHLResearch/LaserScanningData/20190912_VgatChr2_c7m1")
number = sum([len(files) for r, d, files in os.walk(os.getcwd())]) #determine the number of files in the directory
frontal = ""
frontal1 = ""
parietal = ""
parietal1 = ""
fla = ""
fla1 = ""
alp = ""
alp1 = ""
arr = ""
arr1 = ""
 
for x in range(1,number):
    trial = 'Trial: ' + str(x)
    try:
        filename = '20190912_VgatChr2_c7m1_' + str(x) + '.mat'
        file = scipy.io.loadmat(filename) #load file
        data = file['data'] #extract the data table
        array = np.array(data) #convert into numpy array
        part = array[[1]]
        #laser status
        laserStatus = part[0][0] #extract the specific component for LaserOn
        if (laserStatus == 0): #conditional to determine on and off
            laserStatus = 0
            status = 'Laser Status: Off'
        else:
            laserStatus = 1
            status = 'Laser Status: On'
        #ML Location
        MLlocation = part[0][1] #extract the specific component for MLlocation
        #AP Location
        APlocation = part[0][2] #extract the specific component for APlocation
        if ((0.5 <= abs(MLlocation) <= 1.5) and (-2.5 <= APlocation <= -1.5)): #FRONTAL 
            if (laserStatus == 0):
                frontal = str(frontal) + str(x) +  ", " 
            if (laserStatus == 1):
                frontal1 = str(frontal1) + str(x) +  ", " 
        elif ((0.7 <= abs(MLlocation) <= 1.7) and (0.7 <= APlocation <= 1.7)): #PARIETAL
            if (laserStatus == 0):
                parietal = str(parietal) + str(x) +  ", " 
            if (laserStatus == 1):
                parietal1 = str(parietal1) + str(x) +  ", " 
        elif ((1.85 <= abs(MLlocation) <= 2.85) and (-2.1 <= APlocation <= -1.1)): #FLA
            if (laserStatus == 0):
                fla = str(fla) + str(x) +  ", " 
            if (laserStatus == 1):
                fla1 = str(fla1) + str(x) +  ", " 
        elif ((3.0 <= abs(MLlocation) <= 4.0) and (-1.0 <= APlocation <= 0)): #ALP
            if (laserStatus == 0):
                alp = str(alp) + str(x) +  ", " 
            if (laserStatus == 1):
                alp1 = str(alp1) + str(x) +  ", " 
        else: #OUTLIERS
            if (laserStatus == 0):
                arr = str(arr) + str(x) +  ", " 
            if (laserStatus == 1):
                arr1 = str(arr1) + str(x) +  ", " 
    except:
        print(x)

print("FRONTAL NORMAL")             
print(frontal)
print("FRONTAL INHIBITION")             
print(frontal1)
print("PARIETAL")
print(parietal)
print("PARIETAL INHIBITION")             
print(parietal1)
print("FLA")
print(fla)
print("FLA INHIBITION")
print(fla1)
print("ALP")
print(alp)
print("OUTLIERS")
print(arr)
print("OUTLIERS INHIBITION")
print(arr1)
    
    