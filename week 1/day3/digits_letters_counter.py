"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""
str1=list(raw_input("enter string>"))

dict1={'digits':0,'letters':0}

for item in str1:
    if(item.isdigit()):
        dict1['digits']=int(dict1.get('digits')) + 1
    elif(item.isalpha()):
        dict1['letters']=int(dict1.get('letters')) + 1

