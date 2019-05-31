"""

Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
    Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.



"""

import pandas as pd
import numpy as np

data_set=pd.read_csv("PastHires.csv")

features=data_set.iloc[:,:-1].values
labels=data_set.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
le1=LabelEncoder()
le3=LabelEncoder()
le4=LabelEncoder()
le5=LabelEncoder()
le=LabelEncoder()
features[:,1] = le1.fit_transform(features[:, 1])
features[:,3] = le3.fit_transform(features[:, 3])
features[:,4] = le4.fit_transform(features[:, 4])
features[:,5] = le5.fit_transform(features[:, 5])
labels=le.fit_transform(labels)

features = features.astype("float")



from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0) 

#feature scaling
# Feature Scaling
#from sklearn.preprocessing import StandardScaler
#
#sc = StandardScaler()  
#features_train = sc.fit_transform(features_train)  
#features_test = sc.transform(features_test)  



from sklearn.tree import DecisionTreeClassifier  
regressor = DecisionTreeClassifier()  
regressor.fit(features_train, labels_train)  

labels_pred = regressor.predict(features_test)
df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
df  

Score=regressor.score(features_train,labels_train)
Score1=regressor.score(features_test,labels_test)

from sklearn.ensemble import RandomForestClassifier  
regressor = RandomForestClassifier(n_estimators=10,random_state=0) 
regressor.fit(features_train, labels_train)  

labels_pred = regressor.predict(features_test)
df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
  

Score=regressor.score(features_train,labels_train)
Score1=regressor.score(features_test,labels_test)


# Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
# Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.

x=[10,'Y',4,'BS','Y','N']
x=np.array(x)
x=x.reshape(1,-1)

x[:,1]=le1.transform(x[:,1])
x[:,3]=le3.transform(x[:,3])
x[:,4]=le4.transform(x[:,4])
x[:,5]=le5.transform(x[:,5])

labels_pred = regressor.predict(x)

x=[10,'N',4,'MS','N','Y']
x=np.array(x)
x=x.reshape(1,-1)

x[:,1]=le1.transform(x[:,1])
x[:,3]=le3.transform(x[:,3])
x[:,4]=le4.transform(x[:,4])
x[:,5]=le5.transform(x[:,5])

labels_pred = regressor.predict(x)
