"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""
inp = input("enter number:")
i=1
while i!=inp+1:
    print("*"*i)
    i=i+1
    
i=inp
while i!=0:
    print("*"*i)
    i=i-1
    