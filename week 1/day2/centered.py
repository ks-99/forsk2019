"""
Code Challenge
  Name: 
    Centered Average
  Filename: 
    centered.py
  Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is 
    the mean average of the values, except ignoring the largest and 
    smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. 
    Use int division to produce the final average. You may assume that the 
    array is length 3 or more.
    Take input from user  
  Input: 
    1, 2, 3, 4, 100
  Output:
    3
"""
list1 = input("enter values>")
len1=len(list1)
len1 = (len1-1)/2
max1=max(list1)
min1=min(list1)

result = list1[len1]
if(result == max1 or result == min1):
    len1=len1-1
    result = list[len1]

a=0
for item in list1:
    a=a+item
    
result = (a-(max1+min1))/(len1 - 2 )   