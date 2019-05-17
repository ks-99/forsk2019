"""
Code Challenge
  Name: 
    String Handling
  Filename: 
    string.py
  Problem Statement:
    Take first and last name in single command from the user and print  
    them in reverse order with a space between them, 
    find the index using find/index function and then print using slicing concept of the index
  Input:
      Sylvester Fernandes
  Output: 
      Fernandes Sylvester 
"""
str1=raw_input("Enter name:")
a=str1.find(" ")
str2=str1[:a]
str3=str1[a+1:]
str4 = str3 + " " + str2
print(str4)
len1=len(str1)

#len2=len(str2)
#str4 = str2[::-1]
#str6 = str2 + " " + str1
