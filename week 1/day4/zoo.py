"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""
import csv




fp=open("zoo.csv")
print(fp.readlines())
fp.close()
dict1=dict()


with open("zoo.csv",'rU') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        #row=str(row)
        
        dict1[row[0]]=int(row[-1]) + int(dict1.get(row[0],0)) 



