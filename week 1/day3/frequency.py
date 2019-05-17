"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""
str1=list(raw_input("enter string>"))
set1=set(str1)
dict1={}

for item in set1:
    for item1 in str1:
        if(item1 == item):
            dict1[item]=int(dict1.get(item,0)) + 1
        
        
            
            