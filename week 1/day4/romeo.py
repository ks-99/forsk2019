"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""
f1=open("romeo.txt")
list1=[]
list2=[]
dict1=dict()
for item in f1:

    list1.append(item.split(" "))

    
for item in list1:
    for item1 in range(0,len(item)):
        dict1[item[item1]]=dict1.get(item[item1],0) + 1
    

f1.close()    