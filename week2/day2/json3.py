import json
import requests

Host =  "https://en9yfnvayzff.x.pipedream.net"

data = { "name": "Darth Vader" } 

headers = "Content-Type: application/json"

def post1():
    response=requests.post(Host,data,headers)
    return response

print(post1().text)

def get1():
    response=requests.get("https://en9yfnvayzff.x.pipedream.net/get?name: Darth Vader")
    return response

print(get1().text)

    