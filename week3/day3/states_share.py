
"""
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area


Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""

import pandas as pd
from selenium import webdriver
from time import sleep

url="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"

driver = webdriver.Chrome("C:/Users/User/Downloads/chromedriver.exe")
driver.get(url) 
sleep(1)
#df=pd.DataFrame()

states=[]
shares=[]

for i in range(1,7):
    state=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(i)+']/td[2]/a').text
    states.append(state)
    share=driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(i)+']/td[5]').text
    shares.append(share)
    
 
from collections import OrderedDict
columns=[]
columns=["state","National Share"]

col_data = OrderedDict(zip(columns,[states,shares]))
df=pd.DataFrame(col_data)    

import matplotlib.pyplot as plt

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
plt.pie( shares,labels=states, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)    