"""
Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_set=pd.read_csv("iq_size.csv")

features=data_set.iloc[:,1:].values

labels=data_set.iloc[:,0].values

from sklearn.linear_model import LinearRegression

regressor=LinearRegression()

regressor.fit(features,labels)

#What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ?
regressor.predict([[90,70,150]])

# Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.
import statsmodels.api as sm
list2=[]
features=sm.add_constant(features)
features_opt=features[:,[0,1,2,3]]
list2=[0,1,2,3]
regressor_OLS=sm.OLS(endog = labels, exog = features_opt).fit()
list1=list(regressor_OLS.pvalues)
while (max(list1)) > 0.005:
    index=list1.index(max(list1))
    list2.remove(list2[index])
    features_opt=features[:,list2]
    regressor_OLS=sm.OLS(endog = labels, exog = features_opt).fit()
    list1=list(regressor_OLS.pvalues)
    
    
        
    

