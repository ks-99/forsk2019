
"""
Code Challenge
  Filename: 
    height.py
  Problem Statement:

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

    print (average_height)
    
Try rewriting the code below using map, reduce and filter. 
Filter takes a function and a collection. 
It returns a collection of every item for which the function returned True.
    

"""
"""
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

    print (average_height)
"""
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]


height_total = 0
height_count = 0
#print (reduce (lambda x,y : x + y,[2,18,9,22,17,24,8,12,27]))
#my_filter_list = filter ( lambda x:x%3==0 or x%5==0, my_list)

people=filter(lambda x: 'height' in x, people)

people=map(lambda x:x.get('height'),people)
print(reduce(lambda x,y:x+y,people)/len(people))


