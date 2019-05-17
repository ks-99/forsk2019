"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""

list1 = raw_input("enter string:")
len1=len(list1)
list1=list(list1)
#list2=[]
list3 = ['a','e','i','o','u']
item=0
while item <= len1:
    if (list1[item] not in list3):
        list1.insert(item + 1,'o')
        len1=len1 + 1
        list1.insert(item + 2,list1[item])
        len1=len1 + 1
        item = item + 3
    else:
        item = item + 1
       
list1=str(list1)
t2="".join(list1)        
            
            
           
            
            
    
    



