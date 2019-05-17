"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop2.py
  Problem Statement:
    The same bookshop, but this time we work on a different list.
    
    The sublists of our lists look like this:
    [ordernumber, (article number, quantity, price per unit), 
    ... (article number, quantity, price per unit) ]
       
    [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
    
   Write a program which returns a list of list with 
    [order number, total amount of order].
    
   Write a Python program, You need to write a solution without using lambda,map,list comprehension first and then with lambda,map,reduce
      
  Hint: 
    use lambda, map and reduce concept to solve the problem  
    from functools import reduce
"""
list1= [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
   

list2=[] 
cost1=0 
for item in list1:
    for index in range(1,len(item)):
        temp = (item[index][1]*item[index][2])
        cost1+=temp
    
    list2.append([item[0],cost1])
    cost1=0    
    
ip1=map(lambda x: map(lambda x1:x1,x[1:]),list1)  
ip2=map(lambda x: map(lambda x1:x1[1]*x1[2],x),ip1)
ip3=map(lambda x: reduce(lambda x1,y1:x1+y1,x),ip2)
ip1=map(lambda x: x[0],list1)  

list2=zip(ip1,ip3)
