"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""

list1=input("enter list1>")
list2=[]
for item in list1:
    if(item not in list2):
        list2.append(item)
    
    