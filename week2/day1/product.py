"""
This Python function accepts a list of numbers and computes the product of all the odd numbers:
list1=[1,2,3,4,5,6,7]
def productOfOdds(list1):
    result = 1
    for i in list1:
        if i % 2 == 1:
            result *= i
    return result
print(productOfOdds(list1))  
    
Rewrite the Python code using map, filter, and reduce:

"""
list1=[1,2,3,4,5,6,7]

def f(x):
    if(x%2==1):
        return x
list2=reduce(lambda x,y:x*y,(filter(f,list1)))