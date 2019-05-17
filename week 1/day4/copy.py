"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""
fp=open("wordsc.txt","wt")
fp1=open("words.txt","rt")
for item in fp1:
       fp.write(item)
fp.close()
fp1.close()     
    