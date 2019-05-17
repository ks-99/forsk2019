"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""
"""dict1= 0{'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday' : 5, 'Sunday' : 6}
dict2= {}
input1 =input("enter values>")
counter=0
for item in input1:
    dict2[item] = counter
    counter+=1
for item in dict1:
    if (item in dict2):
        dict2[item].values = dict1[item].values()
    else:
        dict2[item] = dict1[item]
 """
       
input1 =list(input("enter values>"))
list1=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for item in range(0,len(list1)):
    for item1 in range(item,len(input1)):
        if(list1[item] is not input1[item]):
            input1.insert(item,list1[item1])
        break
    
