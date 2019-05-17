
"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""
import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)

response=requests.get(url)
j1=response.content

jsondata = response.json()
print(type(jsondata))

print (type(response.content))

print(jsondata["coord"])
print(jsondata["weather"])
print(jsondata["wind"]["speed"])
print(jsondata["sys"]["sunrise"])
print(jsondata["sys"]["sunset"])

