"""
Code Challenge 01: (Prostate Dataset)

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.
(a) Train the unregularized model (linear regressor) and calculate the mean squared error.
(b) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.


"""
import pandas as pd
import numpy as np

dataset=pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",delimiter=" ")
dataset.isnull().any(axis=0)

features=dataset.iloc[:,:-1].values
labels=dataset.iloc[:,-1].values
#TRAin test split
from sklearn.model_selection import train_test_split

features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
#performing SCalling 
from sklearn.preprocessing import StandardScaler

sc=StandardScaler() 
features_train=sc.fit_transform(features_train)
features_test=sc.fit_transform(features_test)


#linear regression
from sklearn.linear_model import LinearRegression

regressor=LinearRegression()

regressor.fit(features_train,labels_train)
labels_pred=regressor.predict(features_test)
Score=regressor.score(features_train,labels_train)
Score1=regressor.score(features_test,labels_test)
df=pd.DataFrame({"Actual":labels_test,"Predicted":labels_pred})

#lassso
from sklearn.linear_model import Lasso

lasso=Lasso()

lasso.fit(features_train,labels_train)
labels_pred_lasso=regressor.predict(features_test)
Score_Lasso=regressor.score(features_train,labels_train)
Score1_lasso=regressor.score(features_test,labels_test)
df=pd.DataFrame({"Actual":labels_test,"Predicted":labels_pred})
print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 

from sklearn import metrics
print (np.round (metrics .mean_squared_error(labels_test, labels_pred_lasso),2))

#Ridge
from sklearn.linear_model import Ridge

ridge=Ridge()

ridge.fit(features_train,labels_train)
labels_pred_ridge=ridge.predict(features_test)
Score_ridge=ridge.score(features_train,labels_train)
Score1_ridge=ridge.score(features_test,labels_test)
df=pd.DataFrame({"Actual":labels_test,"Predicted":labels_pred})
print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 

from sklearn import metrics
print (np.round (metrics .mean_squared_error(labels_test, labels_pred_ridge),2))



#********************************************************************************************************************************
#PREDICATION OF LPSA IS LESS OR MORE
import pandas as pd
import numpy as np

dataset=pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",delimiter=" ")
dataset.isnull().any(axis=0)

dataset["lpsa_new"]=map(lambda x: 1 if (x>dataset["lpsa"].mean()) else 0,dataset["lpsa"])

features=dataset.iloc[:,:-2].values
labels=dataset.iloc[:,-1].values
#TRAin test split
from sklearn.model_selection import train_test_split

features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
#performing SCalling 
from sklearn.preprocessing import StandardScaler

sc=StandardScaler() 
features_train=sc.fit_transform(features_train)
features_test=sc.fit_transform(features_test)





from sklearn.linear_model import LogisticRegression

classifier=LogisticRegression()

classifier.fit(features_train,labels_train)
labels_pred=classifier.predict(features_test)
Score=classifier.score(features_train,labels_train)
Score1=classifier.score(features_test,labels_test)
df=pd.DataFrame({"Actual":labels_test,"Predicted":labels_pred})



from sklearn import metrics
print (np.round (metrics .mean_squared_error(labels_test, labels_pred),2))
