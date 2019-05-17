"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""
list1 = raw_input("Enter list")
list1=list1.split()
len1=len(list1)

for item in range(0,len1):
    list1[item] = int(list1[item])
    
 def add(list1):
        a=0
        for item in list1:
            a=a+item
        return str(a)    
    
 def multiply(list1):
        a=1
        for item in list1:
            a=a*item
        return str(a)    
    
 def sorted1(list1):
     
        list1.sort()
        return str(list1)
    
 def largest(list1):
      max1 = list1[0]
      for item in list1:
            if (item > max1):
                max1=item
             
      return str(max1)    
 def smallest(list1):
     min1=list1[0]
     for item in list1:
            if(item < min1):
                min1=item
     return str(min1)    
 def duplicate(list1):
       list1.sort()
       for item in range(0,len1):
           for item1 in range(item+1,len1-1):
               if (list1[item] == list1[item1]):
                   list1.remove(list1[item])
                   break
       return str(list1)
      
 def print1(list1):
       print("sum =" + add(list1))
       print("multiply =" + multiply(list1))
       print("max =" + largest(list1))
       print("min =" + smallest(list1))
       print("sorted =" + sorted1(list1))
       print("duplicate =" + duplicate(list1))
       
 print1(list1)      