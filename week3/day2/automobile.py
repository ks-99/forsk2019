"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""

import pandas as pd
import numpy as np

df=pd.read_csv("Automobile.csv")

df["price"]=df["price"].fillna(df["price"].mean())#fill nan with mean in price column

arr=np.array(df["price"])#price into numpy array
#calculation mean ,median and std deviation
mean1=df["price"].mean()
median1=df["price"].median()
sd1=df["price"].std()
min1=df["price"].min()

