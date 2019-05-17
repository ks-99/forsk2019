"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""
list1=[]
while(True):
    ip1=raw_input("enter item and price>")
    list1.append(ip1)
    
    if (not ip1):
        break
len1=len(list1)
list2=[]
    
for item in range(0,len1):
    list2.append(list1[item].split())
list2.pop()
list3=[]    
for item in list2:
    list3.append(item[-1])
list4=[]
for item in list2:
  list4.append(" ".join(item[:-1]))
  
dict1={}  
for item in range(0,len(list4)):
    dict1[list4[item]]=list3[item]
    

count=0
for item in dict1:
    if (item in list4):
        var=list4.index(item)

    dict1[item]=int(dict1.get(item)) + int(list3[var])    
    
print(dict1)    
    
n=0
for a in list3:
    a*list3[n]
    n+=1
        
            
    