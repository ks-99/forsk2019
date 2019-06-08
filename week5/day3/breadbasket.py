"""
Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.
"""

import pandas as pd
import numpy as np
from apyori import apriori
import matplotlib.pyplot as plt
df=pd.read_csv("BreadBasket_DMS.csv")
a=df["Item"].value_counts()
a=a.head(15)

plt.pie(a.values,labels=a.index)
transactions=[]
y=[]
with open("BreadBasket_DMS.csv") as fp:
    for item in fp:
        x=item.split(",")
        y.append(x[2])
        y.append(x[3])
        transactions.append(y)
        y=[]
        
        

#transactions.remove(transactions[0])
list1=[]
list2=[]
count=1
for item in transactions:
    if( not item):
        continue
    if(item[0] == str(count)):
        list1.append(item[1])
    else:
        count=item[0]
        list2.append(list1)
        list1=[]
        list1.append(item[1])
        
list2.remove(list2[0])       
rules = apriori(list2, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

# Visualising the results
results = list(rules)

for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")

    

    
    
