#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 19:49:47 2020

@author: sgupta
"""
from tkinter import filedialog
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.io

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("mat files","*.mat"),("all files","*.*")))
file = scipy.io.loadmat(root.filename) #load file
root.destroy()
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
    location = 'FRONTAL'
elif ((0.7 <= abs(MLlocation) <= 1.7) and (0.7 <= APlocation <= 1.7)): #PARIETAL
    location = 'PARIETAL'
elif ((1.85 <= abs(MLlocation) <= 2.85) and (-2.1 <= APlocation <= -1.1)): #FLA
    location = 'FLA'
elif ((3.0 <= abs(MLlocation) <= 4.0) and (-1.0 <= APlocation <= 0)): #ALP
    location = 'ALP'
else: #OUTLIERS
    location = 'OUTLIERS'

print('Location: ' + str(location))    
print(status)