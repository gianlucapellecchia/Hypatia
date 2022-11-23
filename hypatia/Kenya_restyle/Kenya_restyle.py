# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:40:01 2022
Kenya restructured input
@author: GP
"""

import pandas as pd
import numpy as np

NBOR = pd.read_excel("Demand_2019-2040.xlsx",sheet_name="NBOR").set_index("Timesteps")
CSTR = pd.read_excel("Demand_2019-2040.xlsx",sheet_name="CSTR").set_index("Timesteps")
WSTR = pd.read_excel("Demand_2019-2040.xlsx",sheet_name="WSTR").set_index("Timesteps")
MTKR = pd.read_excel("Demand_2019-2040.xlsx",sheet_name="MTKR").set_index("Timesteps")

num_rows, num_col = NBOR.shape
years = num_col

NBOR_yearly = []
for i in range(0,num_col):
    NBOR_yearly.append(NBOR.iloc[:,i])
NBOR_new = np.hstack(NBOR_yearly) 
NBOR_new = pd.DataFrame(NBOR_new)

CSTR_yearly = []
for i in range(0,num_col):
    CSTR_yearly.append(CSTR.iloc[:,i])
CSTR_new = np.hstack(CSTR_yearly) 
CSTR_new = pd.DataFrame(CSTR_new)

WSTR_yearly = []
for i in range(0,num_col):
    WSTR_yearly.append(WSTR.iloc[:,i])
WSTR_new = np.hstack(WSTR_yearly) 
WSTR_new = pd.DataFrame(WSTR_new)

MTKR_yearly = []
for i in range(0,num_col):
    MTKR_yearly.append(MTKR.iloc[:,i])
MTKR_new = np.hstack(MTKR_yearly) 
MTKR_new = pd.DataFrame(MTKR_new)

NewDemand = pd.concat([NBOR_new, CSTR_new, WSTR_new, MTKR_new], axis=1)
NewDemand.reset_index()
NewDemand_final = NewDemand.set_axis(['NBOR', 'CSTR', 'WSTR', 'MTKR'], axis=1, inplace=False)
NewDemand_final.to_excel("NewDemand.xlsx")

hours, regions = NewDemand.shape
average_dem= []
for h in range(0,hours,8760):
    demand_year = NewDemand.iloc[h:(h+8760),:]
    for r in range(0,24,1):
        d = np.zeros((1,regions))
        for i in range(r,8760,24):
            d += demand_year.iloc[i,:].values.reshape((1,regions))
        avg = d/365
        average_dem.append(avg)
average_demand = np.vstack(average_dem)

average_dem = pd.DataFrame(average_demand)
average_dem = average_dem.set_axis(['NBOR', 'CSTR', 'WSTR', 'MTKR'], axis=1, inplace=False)
average_dem.to_excel('Average_demand.xlsx')

#%%
RES = pd.read_excel("RES.xlsx", sheet_name="Sheet1")

RES_new = pd.concat([RES]*years)

RES_new = pd.DataFrame(RES_new)
RES_new.to_excel('Res_complete.xlsx')

row, col = RES.shape
avg = np.zeros((24,col))

for r in range (0,24,1):
    d = np.zeros((1,col))
    for i in range(r,8760,24):
        d += RES.iloc[i,:].values.reshape((1,col))
    avg[r,:] = d/365
        
avg = pd.DataFrame(avg).set_axis([RES.columns], axis=1, inplace=False)
RES_avg = pd.concat([avg]*years)
RES_avg.to_excel('Average_RES.xlsx')