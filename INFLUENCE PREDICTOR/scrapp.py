with open("pick_pickle") as fp:
    classifier=pickle.load(fp)
    
with open("pick_pickle1") as fp:
    sc=pickle.load(fp)

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