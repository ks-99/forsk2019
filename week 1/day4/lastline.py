"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""
input1=raw_input("enter file name with .txt extension>")
count=0

try:
    file = open(input1,  "rt" )
    print(file.readlines()[-1])    
    
except IOError:
    print ( "File not Found")
except Exception:
    print ( "This is a general exception")
finally:
    #print ("this is called always")
    file.close() 
