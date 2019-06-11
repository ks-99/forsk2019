"""
        
Q2. Code Challenge

#Online Marketing

(Click Here To Download Resource File) : http://openedx.forsk.in/c4x/Manipal_University/FL007/asset/online_marketing.sql

Objective of this case study is to explore Online Lead Conversion for a Life Insurance company. Some people are interested in buying insurance products from this company hence they visit the site of this Life Insurance Company and fill out a survey asking about attributes like income, age etc. These people are then followed and some of them become customers from leads. Company have all the past data of who became customers from lead. Idea is to learn something from this data and when

some new lead comes, assign a propensity of him/her converting to a customer based on attributes asked in the survey. This sort of problem is called as Predictive Modelling

Concept:

Predictive modelling is being used by companies and individuals all over the world to extract value from historical data. These are the mathematical algorithms, which are used to "learn" the patterns hidden on all this data. The term supervised learning or classification is also used which means you have past cases tagged or classified (Converted to Customer or Not) and you want to use this learning on new data. (machine learning)

Here are the attributes of the survey:

Attribute

age (Age of the Lead)

Job (Job Category e.g. Management)

marital (Marital Status)

education (Education of Lead)

smoker (Is Lead smoker or not (Binary – Yes / No))

monthlyincome (Monthly Income)

houseowner (Is home owner or not (Binary – Yes / No))

loan (Is having loan or not (Binary – Yes / No))

contact (Contact type e.g. Cellphone)

mod (Days elapsed since survey was filled)

monthlyhouseholdincome (Monthly Income of all family member)

target_buy (altogether Is converted to customer or not (Binary –Yes /No). This is known as Target or Responseand this is what we are modelling.)



Activities you need to perform:


a. Handle the missing data and perform necessary data pre-processing.
b. Summarise the data.
c. Perform feature selection and train using prediction model.
d. For a new lead, predict if it will convert to a successful lead or not.
e. Use different classification techniques and compare accuracy score and also plot them in a bar graph.
"""

import pandas as pd
import numpy as np

import mysql.connector


conn =mysql.connector .connect(user='kunal99',password='kunal2599',host='db4free.net', database = 'kunal99')
query="SELECT * FROM online_marketing"
df=pd.read_sql(query,conn)

df.isnull().any(0)
features=df.iloc[:,:-1].values
labels=df.iloc[:,-1].values

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
features_train[:,1]=le.fit_transform(features_train[:,1])
features_test[:,1]=le.fit_transform(features_test[:,1])

le1=LabelEncoder()
features_train[:,2]=le.fit_transform(features_train[:,2])
features_test[:,2]=le.fit_transform(features_test[:,2])

le2=LabelEncoder()
features_train[:,3]=le2.fit_transform(features_train[:,3])
features_test[:,3]=le2.fit_transform(features_test[:,3])


le3=LabelEncoder()
features_train[:,4]=le3.fit_transform(features_train[:,4])
features_test[:,4]=le3.fit_transform(features_test[:,4])

le4=LabelEncoder()
features_train[:,6]=le4.fit_transform(features_train[:,6])
features_test[:,6]=le4.fit_transform(features_test[:,6])

le5=LabelEncoder()
features_train[:,7]=le5.fit_transform(features_train[:,7])
features_test[:,7]=le5.fit_transform(features_test[:,7])

le6=LabelEncoder()
features_train[:,8]=le2.fit_transform(features_train[:,8])
features_test[:,8]=le2.fit_transform(features_test[:,8])

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
features_train=sc.fit_transform(features_train)
features_test=sc.transform(features_test)

le=LabelEncoder()
labels_train=le.fit_transform(labels_train)

labels_test=le.transform(labels_test)

import statsmodels.api as sm
list1=[]
list2=[]

for i in range(0,12):
    list1.append(i)
    list2.append(i)


features_train=sm.add_constant(features_train)

features_opt=features_train[:,list1]

regressor_OLS=sm.OLS(endog = labels_train, exog = features_opt).fit()
list1=[]
list1=list(regressor_OLS.pvalues)
while (max(list1)) > 0.05:
    index=list1.index(max(list1))
    list2.remove(list2[index])
    features_opt=features_train[:,list2]
    regressor_OLS=sm.OLS(endog = labels_train, exog = features_opt).fit()
    list1=list(regressor_OLS.pvalues)


list1=[]
list2.remove(0)
for item in list2:
    list1.append(item-1)
    
    

features_train=pd.DataFrame(features_train)
features_train=features_train.iloc[:,1:]
features_train=features_train.iloc[:,list1].values
    
features_test=pd.DataFrame(features_test)
features_test=features_test.iloc[:,list1].values

#***********************************************************************

from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 

#Evaluating score
#For classification tasks some commonly used metrics are confusion matrix, precision, recall, and F1 score.

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  

Score_d=classifier.score(features_train,labels_train)#1.0
Score1_d=classifier.score(features_test,labels_test)#32.33


#***************************************************************

#random forest
from sklearn.ensemble import RandomForestClassifier  
classifier = RandomForestClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 

#Evaluating score
#For classification tasks some commonly used metrics are confusion matrix, precision, recall, and F1 score.

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  

Score_rf=classifier.score(features_train,labels_train)#97.0
Score1_rf=classifier.score(features_test,labels_test)#34.23

#*******************************************************************

#Logistic Regression
from sklearn.linear_model import LogisticRegression  
classifier = LogisticRegression()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 

#Evaluating score
#For classification tasks some commonly used metrics are confusion matrix, precision, recall, and F1 score.

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  

Score_lr=classifier.score(features_train,labels_train)#43.8
Score1_lr=classifier.score(features_test,labels_test)#43.6

#**********************************************I***************

#kNN
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)


Score_k=classifier.score(features_train,labels_train)#74.8
Score1_k=classifier.score(features_test,labels_test)#34.6

#************************************************************

list1=['Decision_Tree','Random_Forest','Logistic_Regression','kNN']
list2=[Score1_d,Score1_rf,Score1_lr,Score1_k]

import matplotlib.pyplot as plt

plt.title("Accuracy Of Different Models")
plt.bar(list1,list2)
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.xticks(list1,rotation=90)
plt.show()

