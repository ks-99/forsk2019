# Dungeon Game

"""
Challenge 1
    It would be a 2 dimensional maze game 
    We would put the player in a random room in the grid 
    We would also put a monster in a random room in the grid
    We would out a door in a random room in the grid 
    The player would then move around the grid to find the door
    Don’t let he player go out of the edges of the grid 
    If they hit the monster room they are eaten by the monster 
    or if they reach the gate they win 
    Grid of Room = Collection of Coordinates 
    Player is a tuple, it contains two values  

"""


"""
Challenge 2
Welcome message is getting printed every-time
Can we display the grid for the visual  

"""
import random
list1=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

def choose(list1):
    print('hello')
    r1=random.randint(0,9)
    user=list1[r1]
    
    r2=random.randint(0,9)
    dragon=list1[r2]
    r3=random.randint(0,9)
    gate=list1[r3]
    if(user == dragon or dragon == gate or user == gate):
        return choose(list1)
    list3=[user,dragon,gate]
    print(list3)
    return list3

list3=choose(list1)
user=list3[0]
dragon=list3[1]
gate=list3[2]
row,column=user

print("*****  RULES  *********")
print("You will be given only 6 moves to reach at Gate")
print("If you strike with dragon,you will be immediately out of the game")
print('If reach the gate ,You Won')

count=0
while count<=6:
    list2=['left','right','up','down']
    if(row == 0):
        list2.remove('up')
    if(column == 0):
        list2.remove('left')
    if(row == 2):
        list2.remove('down')
    if(column == 2):
        list2.remove('right')
    print(list2)
    ch=raw_input("choose move or enter to exit>")
    
    if(not ch):
        break
    if(ch == 'left'):
        column-=1
    
    if(ch == 'right'):
        column+=1

    if(ch == 'up'):
        row-=1
 
    if(ch == 'down'):
        row+=1

    count+=1
    user=row,column
    if(user == dragon):
        print("Sorry You loss")
        break
    elif(user == gate):
        print("Congratulation You Won")
        break
    else:
        continue
        
if(count == 7):
    print("Sorry Your moves are over")
    print("You loss the game")        

        
    