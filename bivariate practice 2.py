# -*- coding: utf-8 -*-
"""
Created on Sat Dec 27 18:06:40 2025

@author: savin
"""

import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/savin/OneDrive/Desktop/spreadsheets for spyder/WA_Fn-UseC_-Telco-Customer-Churn.csv")

data = data.fillna(-999)
data.isnull().sum()

#Base_Code 

#trying to calculate count and event rate for each band
pop = data.groupby('gender')['customerID'].count()
rate = data.groupby('gender')['Churn'].mean()

pop.to_csv("C:/Users/savin/OneDrive/Desktop/Spyder projects/for bivariate churn project/gender_pop_cnt.csv")
rate.to_csv("C:/Users/savin/OneDrive/Desktop/Spyder projects/for bivariate churn project/gender_rate.csv")

#end of base code

def categorical_bivariate(var):
    
    pop = data.groupby(var)['customerID'].count()
    rate = data.groupby(var)['Churn'].mean()

    pop.to_csv(f"C:/Users/savin/OneDrive/Desktop/Spyder projects/for bivariate churn project/{var}_pop_cnt.csv")
    rate.to_csv(f"C:/Users/savin/OneDrive/Desktop/Spyder projects/for bivariate churn project/{var}_rate.csv")

    return pop, rate

categorical_bivariate("InternetService")