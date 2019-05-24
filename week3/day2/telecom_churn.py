
"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
    Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
    problem Statement:
To perfrom analysis on the Telecom industry churn dataset -
1. Predict the count of Churned customer availing both voice mail plan and international plan schema
2. Total charges for international calls made by churned and non-churned customer and visualize it
3. Predict the state having highest night call minutes for churned customer
4. Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
5. Which category of customer having maximum account lenght? Predict and print it
6. Predict a relation between the customer and customer care service that whether churned customer have shown their concern to inform the customer care service about their problem or not
7. In which area code the international plan is most availed?
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("Telecom_churn.csv")

count=df["voice mail plan"][(df["international plan"] == 'yes') & (df["voice mail plan"] == 'yes') & (df["churn"] == True)].value_counts()#both voice and internet


x=df["total intl charge"][(df["churn"]==True)]
y=x.sum()

x1=df["total intl charge"][(df["churn"]==False)]
y1=x1.sum()

plt.hist(x, bins=10, facecolor='g')
plt.xlabel('total intl charge')
plt.ylabel('Frequency')
plt.title('charge distribution for churn')
plt.grid(True)
plt.show()

plt.hist(x1, bins=10, facecolor='g')
plt.xlabel('total intl charge')
plt.ylabel('Frequency')
plt.title('charge distribution for non churn')
plt.grid(True)
plt.show()
#Predict the state having highest night call minutes for churned customer

df['state'][df["total night minutes"].max()]
new_df=df[df["churn"]==True]
statemax=new_df['state'][new_df["total night minutes"]==new_df["total night minutes"].max()]


x=new_df["total night minutes"].max()
state_max_night_Call=new_df[['state','total night minutes']][new_df["total night minutes"]==new_df["total night minutes"].max()]#state having max night call minutes for churns

#4a. the most popular call type among churned user
labels=['total day calls','total eve calls','total night calls','total intl calls']
size=[df['total day calls'].sum(),df['total eve calls'].sum(),df['total night calls'].sum(),df['total intl calls'].sum()]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
plt.pie(size, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)

#4b b. the minimum charges among all call type among churned user
labels=['total day charge','total eve charge','total night charge','total intl charge']
size=[df['total day charge'].sum(),df['total eve charge'].sum(),df['total night charge'].sum(),df['total intl charge'].sum()]
plt.pie(size, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)


#5. Which category of customer having maximum account lenght? Predict and print it
df['churn'][df["account length"].max()]
new_df_true=df[df["churn"]==True]
new_df_false=df[df["churn"]==False]

#7. In which area code the international plan is most availed?

df["area code"][df["international plan"] == 'yes'].value_counts().idxmax()#max availed international call

df_area=df[["area code","international plan"]][df["international plan"] == 'yes'].groupby("area code").groups