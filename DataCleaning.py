# -*- coding: utf-8 -*-
"""
#Data Cleaning for Water level and Rainfall
@author: Chanwit Chanton
"""
import pandas as pd 

rain_list=[]
for i in range(0,16,1):
    df=pd.read_excel("R.xlsx", header=[6],sheet_name=i) #Rainfall loop data extraction by sheet No.
    df.rainfalllevel = (df.iloc[[2,9],[2,7,8,9,10,11,12,13]]) # Specify the station 
    dfr= df.rainfalllevel.set_index('สถานี')
    rain= dfr.T # Transpose dataframe for the right way 
    rain_list.append(rain)
result_rain = pd.concat(rain_list)
print(result_rain)
Final_result_rain=result_rain.reset_index().rename({'สถานี':'Date'},axis='columns') #Insert data downup 

water_list = []
for i in range(0,14,1):
    df=pd.read_excel("W.xlsx", header=[7],sheet_name=i) #Water level loop data extraction by sheet No.
    df.waterlevel = (df.iloc[[11,44,13,46],[1,6,7,8,9,10,11,12]]) # Specify the station 
    dfw=df.waterlevel.set_index('สถานี')
    water= dfw.T # Transpose dataframe for the right way
    water_list.append(water)
result_water = pd.concat(water_list)
print(result_water)
Final_result_water=result_water.reset_index().rename({'สถานี':'Date'},axis='columns') #Insert data downup 

##### To be continue merge two dataframe 

#combination=
#data = pd.concat(combination)