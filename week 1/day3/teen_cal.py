"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""
from collection import orderedDict
dict1 = orderedDict()

ip1=input("enter item and price>")
sum1=0   
for item in ip1:
    value=ip1.get(item)
    if(value in range(13,20) and value == 15):
        sum1+=15
    elif(value in range(13,20) and value == 16):
         sum1+=16
    elif(value in range(13,20)):
        continue
    else:
        sum1+=value
                          
    

    
             
    