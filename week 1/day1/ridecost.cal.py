# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:07:54 2019

@author: User
"""

distance = input("enter distance between home and office:")
distance= distance * 2
cost = input("enter cost of diesel")
avg = input("enter average of the car")

total = str((distance/avg) * cost)
print('total cost per day is ' + total)
