
"""
Q. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking into account a quadratic function of the age of the fish.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_set=pd.read_csv("bluegills.csv")

features=data_set.iloc[:,0].values
features=features.reshape(-1,1)
labels=data_set.iloc[:,1].values

#Linear regression
from sklearn.linear_model import LinearRegression

regressor=LinearRegression()
regressor.fit(features,labels)

regressor.predict(features)
plt.scatter(features,labels , color = 'red')
plt.plot(features,regressor.predict(features))
plt.xlabel("Age")
plt.ylabel("LEngth")
plt.show()



#Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 2)
features_poly = poly_object.fit_transform(features)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)
lin_reg_2.predict(poly_object.transform([[5]]))

plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poly_object.fit_transform(features)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()

