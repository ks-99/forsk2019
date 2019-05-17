
"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""
ip1 = raw_input("enter values>")
ip1 =list(ip1)
for item in ip1:
    if(item == ','):
        ip1.remove(item)
        
ip2=tuple(ip1)      
