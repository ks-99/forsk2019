"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi


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
 
    

import sqlite3
from pandas import DataFrame

conn=sqlite3.connect("db_cricket")
c=conn.cursor()
c.execute("DROP TABLE IF EXISTS rank")
c.execute("""CREATE TABLE rank(
        SN INTEGER,Team TEXT,Legis_Cap TEXT,Judi_Cap TEXT,Year TEXT,Points TEXT)""")

for i in range(1,10):
    c.execute("INSERT INTO rank VALUES({},'{}','{}', '{}', '{}', '{}')".format(i,A[i],B[i],C[i],D[i],E[i]))

c.execute("SELECT * FROM rank")
columns=["SN","Team","Legis_Cap","Judi_Cap","Year","Points"]
df=DataFrame(c.fetchall(),columns=columns)

conn.commit()
c.close()