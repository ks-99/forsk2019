"""
Code Challenge
  Name: 
    SSA Analysis
  Filename: 
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available 
    data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip from Resources)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     
"""
import os
import pandas as pd
import numpy as np
list_files=os.listdir("baby")
df=pd.DataFrame()
year=1879
for files in list_files[:131]:
    year+=1
    with open(files) as fp:
        
        df[year]=pd.Series(fp.readlines())
    
list1=[]
males=[]
females=[]
df2=df[2010]
for item in df2:
    item=item.split(",")
    list1.append(item)

df3=pd.DataFrame(list1,columns=["Name","Sex","Birth"])

females=df3["Name"][df3["Sex"]=='F'].head(5)

birth_count=pd.pivot_table(df3,values='Birth',index=["Sex","Name"],aggfunc=np.sum)

pd.plot.bar(birth_count)