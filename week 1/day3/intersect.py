
"""
\

Code Challenge
  Name: 
    Intersection
  Filename: 
    Intersection.py
  Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above given lists.  
"""
list1=input("enter list1>")
list2=input("enter list1>")
list3=[]
for item in list1:
    for item1 in list2:
        if(item == item1):
            list3.append(item)
            
   
list3=set(list3)
print(list3)    
         