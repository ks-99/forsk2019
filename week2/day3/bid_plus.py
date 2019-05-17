
"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
import pandas as pd
from selenium import webdriver
from time import sleep
wiki="https://bidplus.gem.gov.in/bidlists"
driver = webdriver.Chrome("C:/Users/User/Downloads/chromedriver.exe")
driver.get(wiki) 
right_table=driver.find_element_by_id("pagi_content")

bd=[]
name=[]
quantity=[]
dname=[]
sdate=[]
edate=[]
for i in range(1,11):
    item=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text
    bd.append(item)
    item=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text
    name.append(item)
    item=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text
    quantity.append(item)
    item=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text
    dname.append(item)
    item=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text
    sdate.append(item)
    item=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text
    edate.append(item)
    
import pandas as pd
from collections import OrderedDict

col_name = ["BID_NO","ITEM","Quantity Required","Departname Name And Address","Start Date","End Date"]
col_data = OrderedDict(zip(col_name,[bd,name,quantity,dname,sdate,edate]))
df = pd.DataFrame(col_data) 
df.to_csv("bidplus.csv")
    