"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic2.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      You need to develop using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""
ip1=list(raw_input("Enter list>").split(" "))
list2=[]
if(all(int(item) > 0 for item in ip1)):
    print(any(str(item) == item[::-1] for item in ip1))


else:
    print("false")    
    
    
  
    