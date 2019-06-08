"""
 Code Challenge - 
 This is a pre-crawled dataset, taken as subset of a bigger dataset 
 (more than 4.7 million job listings) that was created by extracting data 
 from Monster.com, a leading job board.
 
 Remove location from Organization column?
 Remove organization from Location column?
 
 In Location column, instead of city name, zip code is given, deal with it?
 
 Seperate the salary column on hourly and yearly basis and after modification
 salary should not be in range form , handle the ranges with their average
 
 Which organization has highest, lowest, and average salary?
 
 which Sector has how many jobs?
 Which organization has how many jobs
 Which Location has how many jobs?
"""
import pandas as pd
import numpy as np

dataset=pd.read_csv("monster_com-job_sample.csv")
dataset1=dataset[['location','organization','salary','sector']]
import re

def salary_year(x):
    if(re.search(r'year',str(x))):
        return x
    else:
        return np.nan
    


def salary_hour(x):
    if(re.search(r'hour',str(x))):
        return x
    else:
        return np.nan    
    
dataset1["sal_new_year($)"]=dataset1["salary"].apply(salary_year)
dataset1["sal_new_hour($)"]=dataset1["salary"].apply(salary_hour)
dataset1["sal_new_year($)"]=dataset1["sal_new_year($)"].str.replace(",","")
dataset1["sal_new_hour($)"]=dataset1["sal_new_hour($)"].str.replace(",","")

    
#x="70000.00 - 100000.00 $ /year"
def sal(x):
    count=0
    
    list1=re.findall(r'\d+\.\d+',str(x))
    if(len(list1)!=0):
        for item in list1:
            count+=float(item)
        return count/len(list1)
    else:
        return np.nan
            
    
dataset1["sal_new_year($)"]=dataset1["sal_new_year($)"].apply(sal)

dataset1["sal_new_hour($)"]=dataset1["sal_new_hour($)"].apply(sal)

x="Madison, WI 53702"

def loc(x):
    if(re.search(r'[a-zA-Z\s]*\,?\s?[A-Z]{2}',str(x))):
        return x
    else:
        return np.nan


def org(x):
     if(not re.match(r'[a-zA-Z\s]*[,]?[\s]?[A-Z]{2}',str(x))):
        return x
     else:
        return np.nan
   
    
dataset1["loc"]=dataset["organization"].apply(loc)
dataset1["loc"]=dataset["location"].apply(loc)



dataset1["org"]=dataset["organization"].apply(org)
list1=dataset["location"].apply(org)

""""
# Which organization has highest, lowest, and average salary?
print(dataset1["organization"][dataset1["sal_new_year($)"]==dataset1["sal_new_year($)"].max()])
print(dataset1["organization"][dataset1["sal_new_year($)"]==dataset1["sal_new_year($)"].min()])
print(dataset1["organization"][dataset1["sal_new_year($)"]==round(dataset1["sal_new_year($)"].mean())])

"""
x=dataset1.groupby('organization')["sal_new_year($)"].sum()
x=pd.DataFrame(x)
x.index[x['sal_new_year($)']==x['sal_new_year($)'].max()]
x.index[x['sal_new_year($)']==x['sal_new_year($)'].min()]
x.index[x['sal_new_year($)']==x['sal_new_year($)'].max()]



# which Sector has how many jobs?
dataset1["sector"].value_counts()
# which Location has how many jobs?

dataset1["loc"].value_counts()