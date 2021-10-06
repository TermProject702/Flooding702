# -*- coding: utf-8 -*-
"""
#Data Cleaning for Water level and Rainfall
@author: Chanwit Chanton
"""
import pandas as pd 

rain_list=[]
for ir in range(0,16,1):
    df=pd.read_excel("R.xlsx", header=[6],sheet_name=ir) #Rainfall loop data extraction by sheet No.
    df.rainfalllevel = (df.iloc[[2,9],[2,7,8,9,10,11,12,13]]) # Specify the station 
    dfr= df.rainfalllevel.set_index('สถานี')
    rain= dfr.T # Transpose dataframe for the right way 
    rain_list.append(rain)
result_rain = pd.concat(rain_list) #Insert data downup 
print(result_rain)
Final_result_rain=result_rain.reset_index().rename({'สถานี':'index'},axis='columns') 
unique_Final_result_rain = Final_result_rain.drop_duplicates(subset=["index"]) # data in original excel file have duplicate problem -> unique it by using the date 
dfr2 = unique_Final_result_rain.set_index("index") # set date as index for merge two dataframe which different shape

water_list = []
for iw in range(0,14,1):
    df=pd.read_excel("W.xlsx", header=[7],sheet_name=iw) #Water level loop data extraction by sheet No.
    df.waterlevel = (df.iloc[[13,46,11,44],[1,6,7,8,9,10,11,12]]) # Specify the station 
    dfw=df.waterlevel.set_index('สถานี')
    water= dfw.T # Transpose dataframe for the right way
    water_list.append(water)
result_water = pd.concat(water_list) #Insert data downup 
print(result_water)
Final_result_water=result_water.reset_index().rename({'สถานี':'index'},axis='columns') 
unique_Final_result_water = Final_result_water.drop_duplicates(subset=["index"]) # data in original excel file have duplicate problem -> unique it by using the date
dfw2 = unique_Final_result_water.set_index("index") # set date as index for merge two dataframe which different shape

Final_result = pd.concat([dfw2, dfr2], axis=1) #merge two dataframe which different shape by same index

##### To be continue final check