"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""
list1 = raw_input("enter 1 inch bricks,5 inch bricks,target")
list1 = list1.split()
flag=0
for item in list1:
    list1[item]=int(list1[item])
    
if ((list1[0]*1 + list1[1]*5) < list1[2]):
    flag = 0
elif ((list1[0]*1 + list1[1]*5) == list1[2]):
    flag = 1
elif ()    
    