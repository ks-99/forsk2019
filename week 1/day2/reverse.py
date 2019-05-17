
"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""
str1 = raw_input("enter string")

def reverse1(str1):
    return str1[::-1]

print(reverse1(str1))