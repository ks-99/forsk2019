"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""
import json
import requests
url1 = "http://free.currencyconverterapi.com/api/v5/convert"
url2 = "?q=USD_INR"
url3 = "&apiKey=e25c3be3d761b250440d"

url = url1 + url2 + url3
response=requests.get(url)
json_convert=response.json()
j1=response.content
print(json_convert["results"]["USD_INR"])