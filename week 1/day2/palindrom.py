"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""
list1 =raw_input("enter list:")
list1=list1.split()
len1=len(list1)
for item in range(0,len1):
    list1[item]=int(list1[item])
    
    
    
flag=0
for item in list1:
    item1=str(item)
    if(item < 0):
        flag = 0
        break
    elif(item > 0 and item1 == item1[::-1]):
        flag =1
        continue
    elif(item > 0 and item1 != item1[::-1]):
        continue
    else:
        continue

    
if(flag == 1):
    print('true')
    
else:
 print("false")    
    
                          