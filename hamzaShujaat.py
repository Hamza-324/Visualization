#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 00:34:54 2017

@author: hamza
"""
import matplotlib.pyplot as plt
import pandas as pd




#Data import
newFile = pd.ExcelFile("/home/hamza/Downloads/Product_analytics_sample_data_timline.xlsx")
datasetPersona = pd.read_excel(newFile,"Persona")
datasetTopic = pd.read_excel(newFile,"Topic")
datasetConversions = pd.read_excel(newFile,"Conversions")
garlicChickenPersonaData = datasetPersona.loc[(datasetPersona['Product'] == 'Garlic Chicken Pops')]
classicChickenPersonaData = datasetPersona.loc[
                            (datasetPersona['Product'] == 'Classic Chicken Nuggets')]                            


#Plotting Overall Conversions against  Date                         
X= datasetConversions.iloc[:,0]
YNugget = datasetConversions.iloc[:,1]
YChickenPop = datasetConversions.iloc[:,2]

plt.gca().set_color_cycle(['red', 'blue'])
plt.plot(X, YNugget,X, YChickenPop )
plt.title('Garlic Chicken Pops and nuggets conversion trends')
plt.xlabel('Date')
plt.ylabel('Conversions')
plt.legend()
plt.show()

#plotting the Persona Dataset
X1Persona = garlicChickenPersonaData.iloc[: , 3]
L1Aspect = garlicChickenPersonaData.iloc[:,2]
YReach  = garlicChickenPersonaData.iloc[:,4]

fig, ax = plt.subplots()

ax.plot(X1Persona, YReach)
ax.title('Garlic Chicken Persona Aspect Reach data')
ax.xlabel('Persona')
ax.ylabel('unknowm')
ax.legend()
plt.show()