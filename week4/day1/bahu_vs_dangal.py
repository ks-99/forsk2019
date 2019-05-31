
"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""


import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

data_frame=pd.read_csv("Bahubali2_vs_Dangal.csv")

#for bahubali
features=data_frame.iloc[:,0].values
features=features.reshape(-1,1)
labels=data_frame.iloc[:,1].values

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  

#train the algo
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train) 

#predictions

labels_pred = regressor.predict(features_test) 
df=pd.DataFrame({"Prediction":labels_pred,"Actual":labels_test})

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()  

regressor.fit(features,labels.reshape(-1,1))
day=np.array(10)
day=day.reshape(1,1)
regressor.predict(day)

#******************************************************************************************
#for dangal

features=data_frame.iloc[:,0].values
features=features.reshape(-1,1)
labels=data_frame.iloc[:,2].values

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  

#train the algo
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train) 

#predictions

labels_pred = regressor.predict(features_test) 
df=pd.DataFrame({"Prediction":labels_pred,"Actual":labels_test})

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()  

regressor.fit(features,labels.reshape(-1,1))
day=np.array(10)
day=day.reshape(1,1)
regressor.predict(day)


#**************************************************************************************

#both together

features=data_frame.iloc[:,0].values
features=features.reshape(-1,1)
labels=data_frame.iloc[:,1:].values

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  

#train the algo
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train) 

#predictions

labels_pred = regressor.predict(features_test) 
df=pd.DataFrame({"Prediction_Bahubali":labels_pred[0],"Prediction_Dangal":labels_pred[1],"Actual_Bahubali":labels_test[0],"Actual_Dangal":labels_test[1]})

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()  

regressor.fit(features,labels.reshape(-1,2))
day=np.array(10)
day=day.reshape(1,1)
regressor.predict(day)

