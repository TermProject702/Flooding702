# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 09:33:01 2021
#Data Cleaning for Water level
@author: Chanwit Chanton
"""
import pandas as pd 
import numpy as np

df=pd.read_excel("W.xlsx", header=[7],sheet_name=0)

df.waterlevel = (df.iloc[[11,44,13,46],[1,6,7,8,9,10,11,12]])
print(df.waterlevel)

df=df.waterlevel.set_index('สถานี')
print(df)

water_origin = df.T
print(water_origin)

for i in range(1,14):
    print(i)
    df=pd.read_excel("W.xlsx", header=[7],sheet_name=i)
    df.waterlevel = (df.iloc[[11,44,13,46],[1,6,7,8,9,10,11,12]])
    df=df.waterlevel.set_index('สถานี')
    water= df.T
    print(water)

### To be continued on appending

frames = [water_origin,water]
result = pd.concat(frames)
