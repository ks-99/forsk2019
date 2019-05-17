"""
Code Challenge
  Name: 
    Sorting
  Filename: 
    sorting.py
  Problem Statement:
    You are required to write a program to sort the (name, age, height) 
    tuples by ascending order where name is string, age and height are numbers. 
    The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score. 
    The priority is that name > age > score
  Input: 
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
  Output:
    [('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)]
"""


list1 = input("enter name,age and score")
list1=list(list1)
list1.sort()
list1=tuple(list1)
