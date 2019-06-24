import pandas as pd
import numpy as np
df=pd.read_csv("train.csv")
df2=pd.read_csv("test.csv")
df3=pd.read_csv("sample_predictions.csv")
labels_test=df3.iloc[:,1]
features_test=df2.iloc[:,[1,2,8,12,13,19]]
features_train=df.iloc[:,[1,2,8,12,13,19]]
labels_train=df.iloc[:,0]

#************************************888
def labels(x):
    if(x<0.5):
        return 0
    else:
        return 1
labels_test=labels_test.apply(labels)    
#************************************************************************
#from sklearn.model_selection import train_test_split
 #features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
"""
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features_train=sc.fit_transform(features_train)

features_test=sc.transform(features_test)
"""
from sklearn.preprocessing import FunctionTransformer
sc=FunctionTransformer(np.log1p, validate=True)
features_train=sc.fit_transform(features_train)
features_test=sc.transform(features_test)

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression( random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)  

#******************************************************
import matplotlib.pyplot as plt 
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = features_test, y = labels_test, cv = 10)
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())

# Visualising the Training set results
# Plot the decision boundary. For that, we will assign a color to each
import numpy as np   

x_min, x_max = features_train[:, 0].min() - 1, features_train[:, 0].max() + 1
y_min, y_max = features_train[:, 1].min() - 1, features_train[:, 1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))
# Obtain labels for each point in mesh using the model.
# ravel() is equivalent to flatten method.
# data dimension must match training data dimension, hence using ravel
Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

# Plot the points
plt.plot(features_test[labels_test == 0, 0], features_test[labels_test == 0, 1], 'ro', label='Class 1')
plt.plot(features_test[labels_test == 1, 0], features_test[labels_test == 1, 1], 'bo', label='Class 2')
#plot the decision boundary
plt.contourf(xx, yy, Z, alpha=1.0)

plt.show()

#******************************************************
from sklearn.metrics import confusion_matrix
#************************************************************************
from bs4 import BeautifulSoup
import requests
handle = raw_input('Input your account name on Twitter: ') 
temp = requests.get('https://twitter.com/'+handle)
bs = BeautifulSoup(temp.text,'lxml')
try:
#    follow_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--followers'})
#    followers = follow_box.find('a').find('span',{'class':'ProfileNav-value'})
    all_tabs = bs.find_all("li",class_="ProfileNav-item")
    
    feature_dict = {}
    feature_req = ["Followers","Following","Tweets"]
    feature_dict = feature_dict.fromkeys(feature_req,0)
    
    for item in all_tabs:
        label = item.find("span",class_="ProfileNav-label")
        value = item.find("span",class_="ProfileNav-value")
        
        if label and value:
            label = str(label.text.strip())
            value = str(value.text.strip())
            if label in feature_req:
                feature_dict[label] = value
    
    
except:
    print('Account name not found...')
    

handle1 = raw_input('Input your account name on Twitter: ') 
temp = requests.get('https://twitter.com/'+handle1)
bs = BeautifulSoup(temp.text,'lxml')
try:
#    follow_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--followers'})
#    followers = follow_box.find('a').find('span',{'class':'ProfileNav-value'})
    all_tabs = bs.find_all("li",class_="ProfileNav-item")
    
    feature_dict1 = {}
    
    feature_dict1 = feature_dict1.fromkeys(feature_req,0)
    
    for item in all_tabs:
        label = item.find("span",class_="ProfileNav-label")
        value = item.find("span",class_="ProfileNav-value")
        
        if label and value:
            label = str(label.text.strip())
            value = str(value.text.strip())
            if label in feature_req:
                feature_dict1[label] = value
    
    
except:
    print('Account name not found...')
   
import re
for key,value in feature_dict.items():
    
    if(re.search(r'[,]',str(value))):
        value=value.replace(",","")
        
         
 
            
    if(re.search(r'M$',str(value))):
        value=float(value.replace("M",""))
        value=int(value*1000000)
    
    elif(re.search(r'K$',str(value))):
        value=float(value.replace("K",""))
        value=int(value*1000)
    feature_dict[key]=int(value)
            
for key,value in feature_dict1.items():
    if(re.search(r'[,]',str(value))):
        value=value.replace(",","")
         
 
            
    if(re.search(r'M$',str(value))):
        value=float(value.replace("M",""))
        value=int(value*1000000)
    
    if(re.search(r'K$',str(value))):
        value=float(value.replace("K",""))
        value=int(value*1000)
    feature_dict1[key]=int(value)

        
    

list1=[feature_dict["Followers"],feature_dict["Following"],feature_dict["Tweets"],feature_dict1["Followers"],feature_dict1["Following"],feature_dict1["Tweets"]]
import numpy as np
list2=np.array(list1)
list2=list2.reshape(1,-1)

list2=sc.transform(list2)

classifier.predict(list2)