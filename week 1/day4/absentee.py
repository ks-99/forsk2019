"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""
fp =open("absentee.txt","w+")
for item in range(0,25):
    input1=raw_input("enter name>")
    if(not input1):
        break
    fp.write(input1 + '\n')
fp.seek(0,0)    
print(fp.readlines())    
fp.close()
    