"""

Q2. Code Challenge
code challenge - election data

1. Fetch the top parties of each state within each constituency with their vote %.

2. Visualize the top parties vote % in each constituency for Rajasthan.

3. Visualize the total seats gained by each party in each states.

4. Visualize the total seats won by the parties in the whole country
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("election.csv")

#1. Fetch the top parties of each state within each constituency with their vote %.

data = df.sort_values("%").drop_duplicates(["State","Constituency"], keep="last")
data = data.sort_values("State")
data = data.sort_values("%")
data.index = [x for x in range(0,542)]
data=data[["Party","%","State","Constituency"]]

#2. Visualize the top parties vote % in each constituency for Rajasthan.

data=data[data["State"] == "Rajasthan"]

plt.title("top parties vote % in each constituency for Rajasthan.")
plt.bar(data["Constituency"],data["%"])
plt.xlabel("Constituency")
plt.ylabel("% Polulation")
plt.xticks(data["Constituency"],rotation=90)
plt.show()

#3. Visualize the total seats gained by each party in each states.


data = df.sort_values("Total Votes").drop_duplicates(["State","Constituency"], keep="last")
data = data.sort_values("State")
data=data[["Party","Total Votes","State","Constituency"]]

data=data.groupby("State")
data=dict(data["Party"].value_counts())
labels=data.keys()
state=[]
party=[]
for item in data.keys():
    x,y= item
    state.append(x)
    party.append(y)
list3=[]
for i in range(0,85):
    list3.append(state[i] + "," + party[i])


values=map(int,data.values())
plt.bar(list3,values,align='center', alpha=1.0)
plt.xlabel("State-Party")
plt.ylabel("Total Seats")
plt.xticks(list3,rotation=90)
plt.show()


#****************************************************
#4. Visualize the total seats won by the parties in the whole country
data = df.sort_values("Total Votes").drop_duplicates(["State","Constituency"], keep="last")
data1=data["Party"].value_counts()

plt.bar(data1.index,data1.values,align='center', alpha=1.0)
plt.xlabel("Party")
plt.ylabel("Total Seats")
plt.xticks(data1.index,rotation=90)
plt.show()
