# Shopping List App 

"""
Challenge 1
    We are going to make a "Shopping List" app. 
    Run the script to start using it.
    Put new things into the list one at a time
    Enter the word DONE - in all CAPS - to QUIT the program
    And once i quit, I want the app to show me everything thats on my list.

Hint 1
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use the app

    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app with DONE

    Step 6: print out the list
"""


#   Make a list to hold onto our items.
shopping_list = []

# Print out instructions on how to use the app
print ("What should we pick up at the store ?")
print ("Enter 'DONE' to stop adding items.")

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break
    
    # add new items to our list
    shopping_list.append(new_item)

#  print out the list
print("Here’s your list")
for item in shopping_list:
    print ( item )



"""
Challenge 2
    If I type SHOW, 
    I should be able to see what is currently in the list

    If I type HELP, 
    I should be able to see all the help for these special commands

Hint 2
    Step 1: Have a HELP command
    Step 2: Have a SHOW command
    Step 3: Add a function for adding into the list 
    Step 4: Cleanup the code in general
"""

"""

Challenge 3
    User can enter SHOW or Show or show, 
    similar for DONE and HELP, but the program should do the required job

    Show the item in the list serially starting from 1

    Let us accept items using a comma separated string
        
    Also there should be a functionality to add an item at a specific index

    There should be a functionality to remove items from the list at a specific index using REMOVE
    
    Do all the exception handling for all the extreme use cases 
"""

"""
Challenge 4   
    Do all the exception handling for all the extreme use cases 
"""

"""
Challenge 5   
    Store the shopping list in a file. 
"""
print ("Enter items in list")
print ("Enter 'DONE' to stop adding items.")
shopping_list=[]
while True:
    
    new_item = raw_input("> ").upper()

    
    if new_item == 'DONE':
        break
    
    shopping_list.append(new_item)

print("Here’s your list")
for item in shopping_list:
    print ( item )
    

def add(shoppig_list):
    ch3=input('press 1 to add or 0 to append')
    if(ch3 == 1):
        while True:
            new_item =raw_input("> ")
            n1=input("enter index>")

    
            if new_item == 'DONE':
                break
            shopping_list.insert(n1,new_item)
        
    elif(ch3 == 0):
        while True:
            new_item =raw_input("> ")

    
            if new_item == 'DONE':
                break
            shopping_list.append(new_item)
        
    
    
def remove(shopping_list):
    ip=input('enter index of item to remove')
    for item in shopping_list:
        if(ip == shopping_list.index(item)):
            shopping_list.remove(item)
            print('item removed successfully')
        else:
            print("invalid indix")
    


def show(shopping_list):
    for item in shopping_list:
        print (item )
        
        
def help1():
    print('use SHOW to display list')
    print('use ADD to add item in list')
    print('use DONE to stop adding in list')
    print('use REMOVE to remove item from list')
            
        
print('Type SHOW to display list')
print('Type ADD to add item in list')
print('Type HELP to display special commands')
print('Type REMOVE to remove item from list')
ch2=raw_input('Enter your choice>').upper()

if(ch2 == 'SHOW'):
    show(shopping_list)
    
elif(ch2 == 'ADD'):
    add(shopping_list)

elif(ch2 == 'HELP'):
    help1()
    
elif(ch2 == 'REMOVE'):
    remove(shopping_list)
    
    
else:
    print('wrong choice')
       
    
    
    
    
        
    