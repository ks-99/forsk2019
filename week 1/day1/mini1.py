# Interactive Guess the Number Game 

"""
Challenge 1
    The computer will think of a random number from 1 to 10 as secret number
    Then ask you ( Player ) to guess the number and store as guess number

    Compare the guess number with the secret number 
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.

"""

"""
Challenge 2
    Print the secret number and guess number when Player loses using format function 
"""

"""
Challenge 3
    Print too HIGH or too LOW messages for bad guesses using elif. 
"""


"""
Challenge 4
    Let people play again and again until he guesses the right secret number
"""


"""
Challenge 5
Limit the number of guesses to maximum 6 tries 
"""


"""
Challenge 6
    Print the number of tries left 
"""


"""
Challenge 7
    Lets give user the option to play again
"""

"""
Challenge 8
    Catch when someone submits a non integer
"""
import random
count=0
while count <=6:
    count = count + 1
    num2=random.randint(1,10)
    num=input("choose no from 0 to 9:")
    num1=str(num)
    num3=str(num2)
    if(num == num2):
        print("Congratulations You beat computer")
        break
    elif (type(num) != int):
        print("Your choice is not appropriate , Try again")
        continue
    elif (num > num2):
        print("too high")
        print("Your choice is {}, correct answer is {}.".format(num1,num3))
    elif (num < num2):
        print("too Low")
        print("Your choice is {}, correct answer is {}.".format(num1,num3))
   
    else:
        print("Invalid choice")
        
    rem =str(6 - count)
    print("Remaining chances are " + rem )
    if(count == 6):
        print("Sorry you exceed the limit")
        break
    else:
         ch=raw_input("press Y to continue or any key to exit:")
         if(ch == 'y'):
             continue
         else:
             break
         
         

       