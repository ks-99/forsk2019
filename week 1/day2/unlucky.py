"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
"""
 
list1 = input("enter items>")
len1=len(list1)
i=0
sum1=0
while i<= len1:
    if(list1[i] == 13):
        i = i + 2
    else:
        sum1 = sum1 + list1[i]
        i = i  + 1
    
print(sum1)    