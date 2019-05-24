

"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""
# with numpy
import numpy as np
arr1= -10*np.random.random((40)) + 15
arr1=np.array(arr1,dtype=int)

np.bincount(arr1).argmax()# returns the most occured value

# without numpy

from collections import Counter

print(Counter(arr1).most_common()[0][0])

