# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 09:33:01 2021
#Data Cleaning for Water level
@author: Chanwit Chanton
"""
import pandas as pd 
import numpy as np




water_list = []
for i in range(0,14,1):
    df=pd.read_excel("W.xlsx", header=[7],sheet_name=i)
    df.waterlevel = (df.iloc[[11,44,13,46],[1,6,7,8,9,10,11,12]])
    df=df.waterlevel.set_index('สถานี')
    water= df.T
    water_list.append(water)
result = pd.concat(water_list)
print(result)
Final_result=result.reset_index().rename({'สถานี':'Date'},axis='columns')

##### To be continue adding rain fall data