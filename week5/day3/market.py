
"""
Code Challenge:
Datset: Market_Basket_Optimization.csv
Q2. In today's demo sesssion, we did not handle the null values before fitting the data to model, remove the null values from each row and perform the associations once again.
Also draw the bar chart of top 10 edibles.
"""
import pandas as pd
import numpy as np
from apyori import apriori
import matplotlib.pyplot as plt

dataset=pd.read_csv("Market_Basket_Optimisation.csv",header=None)
transactions = []
list1=[]
list2=[]
for i in range(0, 7501):
    for j in range(0,20):
        if(dataset.iloc[i,j] is not np.nan):
            list2.append(dataset.iloc[i,j])
            list1.append(dataset.iloc[i,j])
            
    transactions.append(list1)
    list1=[]
                
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

# Visualising the results
results = list(rules)
df=pd.DataFrame(list2)
a=df[0].value_counts()
a=a.head(15)
labels=list(a.index)
values=list(a.values)

plt.bar(labels,values)
plt.xticks(labels,rotation=90)
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
                    
