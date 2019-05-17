
"""
Code Challenge
  Name: 
    Population Counting
  Filename: 
    Population.py
  Problem Statement:
      
      The given input has a number of rows, each with four fields from a table, containing:

          Rank,City,Population,State or union territory
          1,Mumbai,"12,442,373",Maharashtra


    You are required to output:

        Country, State, Population of the state (obtained by summing up the population of each city in that state)  


    Sample Input

    1,Mumbai,"12,442,373",Maharashtra
    9,Pune,"3,124,458",Maharashtra
    13,Nagpur,"2,405,665",Maharashtra
    6,Chennai,"4,646,732",Tamil Nadu
    59,Salem,"831,038",Tamil Nadu


    Sample Output

    {"key":"India,Tamil Nadu","value":5477770}
    {"key":"India,Maharashtra","value":17972496}


    Explanation

    The population of India,Tamil Nadu is obtained by adding the population of 
    Chennai and Salem. 
    This process is repeated for India,Maharashtra and India,Maharashtra. 


    Refer to population.csv


"""
import csv
list1=[]
with open("population.csv")as f1:
    csv_reader=csv.reader(f1,delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        list1.append(row)
dict1=dict()        
for item in list1:
    item[2]=item[2].replace(",","")
    dict1[item[3]]=int(dict1.get(item[3],0)) + int(item[2])   
        


def f(x):
    return x.replace(",","")
    
list2=map(lambda x:[x[0],x[1],x[2].replace(",",""),x[3]],list1) 
dict1=dict()
def f1(item):
    dict1["india,"+ item[3]]=int(dict1.get("india,"+item[3],0)) + int(item[2])
    
filter(f1,list2)