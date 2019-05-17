"""
Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
"""
    a1=input("enter marks of assignment 1:")
    a2=input("enter marks of assignment 2:")
    a3=input("enter marks of assignment 3:")
    e1=input("enter marks of exam 1:")
    e2=input("enter marks of exam 2:")

wa=input("Enter weightage of assignments in %")
we=input("Enter weightage of exams in %")

total = str((a1+a2+a3)*(wa/100.0) + ( e1+e2)*(we/100.0))

print("total weighted score is :" + total)