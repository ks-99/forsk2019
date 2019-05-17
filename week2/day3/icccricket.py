
"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""
from bs4 import BeautifulSoup
import requests
#import urllib

wiki="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source=requests.get(wiki).text

soup=BeautifulSoup(source,"lxml")
print(soup.prettify())

all_tables=soup.find('table',class_="table")
print(all_tables)
A=[]
B=[]
C=[]
D=[]
E=[]

for row in all_tables.findAll('tr'):
    cells = row.findAll('td')
    
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
 

import pandas as pd
from collections import OrderedDict

col_name = ["SN","Team","Legis Cap","Judi Cap","Year","Points"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))
df = pd.DataFrame(col_data) 
#df.to_csv("former.csv")
       



    