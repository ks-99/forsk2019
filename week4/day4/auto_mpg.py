"""
Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" respectively
    Display the Car Name with highest miles per gallon value
    Build the Decision Tree and Random Forest models and find out which of the two is more accurate in predicting the MPG value
    Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)

"""

import pandas as pd
import numpy as np

data_set=pd.read_table("Auto_mpg.txt",delim_whitespace=True)
data_set.columns=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]
data_set.isnull().any(axis=0)

data_set['horsepower']=data_set['horsepower'].replace("?",data_set['horsepower'].mode()[0])
car_name=data_set["car name"][data_set["mpg"]==max(data_set["mpg"])]

#
features=data_set.iloc[:,1:-1].values
labels=data_set.iloc[:,0].values


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0) 


from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)  


from sklearn.tree import DecisionTreeRegressor  
regressor = DecisionTreeRegressor()  
regressor.fit(features_train, labels_train)  

labels_pred = regressor.predict(features_test)
df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  

Score=regressor.score(features_train,labels_train)
Score1=regressor.score(features_test,labels_test)
labels_pred = regressor.predict(sc.transform([[6,215,100,2630,22.2,80,3]]))

#**********************************************************************************************

import pandas as pd  
import numpy as np  

data_set=pd.read_table("Auto_mpg.txt",delim_whitespace=True)
data_set.columns=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]
data_set.isnull().any(axis=0)

data_set['horsepower']=data_set['horsepower'].replace("?",data_set['horsepower'].mode()[0])
car_name=data_set["car name"][data_set["mpg"]==max(data_set["mpg"])]

features=data_set.iloc[:,1:-1].values
labels=data_set.iloc[:,0].values

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=0) 


from sklearn.preprocessing import StandardScaler

sc1 = StandardScaler()  
features_train = sc1.fit_transform(features_train)  
features_test = sc1.transform(features_test)  

from sklearn.ensemble import RandomForestRegressor

regressor1 = RandomForestRegressor(n_estimators=50, random_state=0)  
regressor1.fit(features_train, labels_train)  
labels_pred = regressor1.predict(features_test)  


Score=regressor1.score(features_train,labels_train)
Score1=regressor1.score(features_test,labels_test)
#**********************************************************************************************************

#Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)

labels_pred = regressor1.predict(sc1.transform([[6,215,100,2630,22.2,80,3]]))
