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
Final_result_water=result_water.reset_index().rename({'สถานี':'index'},axis='columns') 
unique_Final_result_water = Final_result_water.drop_duplicates(subset=["index"]) # data in original excel file have duplicate problem -> unique it by using the date
dfw2 = unique_Final_result_water.set_index("index") # set date as index for merge two dataframe which different shape

Final_result = pd.concat([dfw2, dfr2], axis=1) #merge two dataframe which different shape by same index
Final_result = Final_result.dropna() # drop not match date of two dataframe

# genarate new feature of ระดับน้ำเทียบตลิ่ง from fixed value of ระดับตลิ่ง in each station compare with the real water level in each day for flooding assessment 
Final_result['C.35 river/brae']=Final_result['C.35']/4.58 
Final_result['S.5 river/brae']=Final_result['S.5']/4.7
Final_result['C.7A river/brae']=Final_result['C.7A']/10
Final_result['S.26 river/brae']=Final_result['S.26']/8
Final_result.rename(columns={'C.35': 'C.35 Ayutthaya (Chao Phraya R.)', 'S.5': 'S.5 Ayutthaya (Pa Sak R.)', 'C.7A': 'C.7A Ang Thong (Chao Phraya R.)', 'S.26': 'S.26 Tha Ruea (Pa Sak R.)', 'C.13': 'C.13 Sapphaya (Chao Phraya r.)', 'S.9': 'S.9 Kaeng Khoi (Pa Sak r.)'}, inplace=True) #Rename column's names

# Due to the original dates are not completed (lack year), so generate new time stamp
Final_result20=Final_result.head(44) # 18/08 - 30/09 on 2020
Final_result20['date']=pd.date_range(start='18/08/2020', periods=44, freq='D')
Final_result21=Final_result.tail(44) # 18/08 - 30/09 on 2021
Final_result21['date']=pd.date_range(start='18/08/2021', periods=44, freq='D')
frames=[Final_result20,Final_result21]
Cleandata = pd.concat(frames) # merge split data for each year time stamp (2020,2021)
Cleandata = Cleandata.reset_index().rename({'index':'old date'},axis='columns') 
Cleandata = Cleandata.drop(['old date'], axis=1) #Drop old date which lack of year
Cleandata.to_csv("FloodingCleaned.csv", index=False)