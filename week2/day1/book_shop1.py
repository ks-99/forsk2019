

"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number  Book Title  Author Quantity  Price per Item
    34587 Learning Python, Mark Lutz  4 40.95
    98762 Programming Python, Mark Lutz 5 56.80
    77226 Head First Python, Paul Barry 3 32.95
    88112 Einführung in Python3, Bernd Klein  3 24.99    
    
    Write a Python program, You need to write a solution without using lambda,map,list comprehension first and then with lambda,map,reduce
    
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.

  Hint: 
    Write a Python program using lambda and map.

"""
list1=[]
list1=[[34587,'Learning Python','Mark Lutz',4,40.95],[98762,'Programming Python','Mark Lutz',5,56.80],[77226,'Head First Python','Paul Barry',3,32.95],[77226,'Head First Python','Paul Barry',3,32.95]]
list2=[]    
for item in list1:
    t1=[item[0],item[3]*item[4]]
    if(t1[1]<100):
        t1[1]+=10
        
    list2.append(tuple(t1))

t1=map(lambda x:(x[0],x[3]*x[4]),list1)
t1=map(lambda x: x if x[1]>=100 else (x[0],x[1]+10),t1)


