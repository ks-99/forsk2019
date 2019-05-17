"""
Code Challenge
  Name: 
    Pangram
  Filename: 
    pangram.py
  Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
  Hint:
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.
  Input: 
    The five boxing wizards jumps.
  Output:
    NOT PANGRAM
"""

str1 = raw_input("enter string")
list1=[]
for i in str1:
    list1.append(i)
    
list2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']    
flag=0    
for item in list2:
    if item not in list1:
        flag=1
        break
        
if(flag == 1):
   print("NOT PANGRAM")
else:
   print("PANGRAM")       