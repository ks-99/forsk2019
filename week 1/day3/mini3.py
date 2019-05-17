# Hangman Letter Game App

"""
Challenge 1

    We are going to make a "Hangman Letter" game 
    The computer will pick a word
    The player can guess it letter by letter or run out of chances.
    But if they make too many wrong guesses, they loose.
    If the player makes the right guesses he wins
    Cleaner interface and option to quit the game

Hint 1

    Step 1: Make a list of words, may be Fruits or vegetables 
    Step 2: Pick a random word from the list
    Step 3: Get a guess from the player 
    Step 4: Compare the guess to the secret number
    Step 5: If the player guesses the right number print player wins and computer lose.
    Step 6: If the player guesses the wrong number print player lose and computer wins.

Algorithm

    # import external libraries
    # make a list of word

    # pick a random word

    # draw  spaces
    # take guess
    # draw guessed letters, spaces and strikes
    # print out win / lose

"""

"""
Challenge 2
    Screen is messy and rolls ups
    Convert the code into function 

    MAJOR REFACTORING OF THE CODE
"""

"""
Challenge 3
Read the words from a file

"""

"""
Challenge 4
    Get the list of Internet after web scrapping
"""
import random
list1=['apple','banana','cow','dog','elepahnt']

count=0

while count<=3:
    count1=0
    count+=1
    r1=random.randint(0,len(list1)-1)
    str1=list1[r1]
    for i in range(0,len(str1)):
        guess1=raw_input("Guess a letter>")
        if(guess1 == str1[i]):
            continue
            print('you win')
            break
            
        elif(guess1 is not str1[i]):
            print('you loss')
            break
            
        else:
            break
        
    if(i == len(str1)):
        print('you win')
        break
    
    rem=str(3-count)
    print('remaining chances are:' + rem)
    
    if(count == 3):
        print('sorry you exceed the limit')
        break
    else:
        ch=raw_input('press y to conntinue:').lower()
        if(ch == 'y'):
            continue
        else:
            break
      
         
            
    