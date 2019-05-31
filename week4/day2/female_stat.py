"""
Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

 

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_set=pd.read_csv("Female_Stats.csv")

features=data_set.iloc[:,1:].values
labels=data_set.iloc[:,0].values

feature_mother=data_set.iloc[:,1].values
feature_father=data_set.iloc[:,2].values
#****  Checking which feature is most important.
import statsmodels.api as sm
features = sm.add_constant(features)

features_opt = features[:,[0,1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

#*************************************************************************
Meanf=feature_father.mean()

from sklearn.linear_model import LinearRegression


data_set["momplus1"]=data_set["momheight"]+1
feature_mother=data_set.iloc[:,2:].values

lin_reg_1 = LinearRegression()
lin_reg_1.fit(features, labels)
Mean=(lin_reg_1.predict(features)).mean()#Average height of a child when father height is constant

Meanm=(lin_reg_1.predict(feature_mother)).mean()#Average height of a child when father height is constant


data_set["dadplus1"]=data_set["dadheight"]+1
feature_father=data_set.iloc[:,[-1,1]].values

Meanf=(lin_reg_1.predict(feature_father)).mean()#Average height of a child when mother height is constant
