"""
Code Challenge: Simple Linear Regression
  Name: 
    Food Truck Profit Prediction Tool
  Filename: 
    Foodtruck.py
  Dataset:
    Foodtruck.csv
  Problem Statement:
    Suppose you are the CEO of a restaurant franchise and are considering 
    different cities for opening a new outlet. 
    
    The chain already has food-trucks in various cities and you have data for profits 
    and populations from the cities. 
    
    You would like to use this data to help you select which city to expand to next.
    
    Perform Simple Linear regression to predict the profit based on the 
    population observed and visualize the result.
    
    Based on the above trained results, what will be your estimated profit, 
    
    If you set up your outlet in Jaipur? 
    (Current population in Jaipur is 3.073 million)
        
  Hint: 
    You will implement linear regression to predict the profits for a 
    food chain company.
    Foodtruck.csv contains the dataset for our linear regression problem. 
    The first column is the population of a city and the second column is the 
    profit of a food truck in that city. 
    A negative value for profit indicates a loss.
"""
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

data_frame=pd.read_csv("Foodtruck.csv")
features=data_frame.iloc[:,:-1].values
labels=data_frame.iloc[:,-1].values

# Vizualizing population and Profit
plt.boxplot(data_frame.values)

data_frame.plot(x='Population', y='Profit', style='o')  
plt.title('Population  vs Profit')  
plt.xlabel('Population')  
plt.ylabel('Profit')  
plt.show()

#test splitting
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  

#train the algo
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train) 


#predictions

labels_pred = regressor.predict(features_test) 
df=pd.DataFrame({"Prediction":labels_pred,"Actual":labels_test})
#performing linear regression
from sklearn.linear_model import LinearRegression

regressor=LinearRegression()
val=np.array(3.072)
val=val.reshape(1,1)
regressor.fit(features,labels)
profit = regressor.predict(val)

if(profit < 0):
    print("Loss by :" + str(profit))
else:
        print("Profit by :" + str(profit))
        
#***********************************************************

        