"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""

input1=raw_input("enter file name with .txt extension>")
words=0
lines=0
char=0
list1=[]
list2=[]
dict1=dict()
uwords=0
try:
    file = open(input1,  "rt" )
    for item in file:
        char+=len(item)
        list1.append(item.split(" "))
        lines+=1
        
    
    for item in list1:
        words+=len(item)
        
    for item in list1:
        for item1 in range(0,len(item)):
            dict1[item[item1]]=dict1.get(item[item1],0) + 1
   
    for key in dict1:
        
        if(int(dict1.get(key)) == 1):
            
            list2.append(key)
        
    uwords = len(list2)

    
    
    
    print("Number of characters (including whitespace):" + str(char))
    print("Number of words (separated by whitespace:" + str(words))
    print("Number of lines:" + str(lines))
    print("Number of unique words:" + str(uwords));
                                          
        
except IOError:
    print ( "File not Found")
except Exception:
    print ( "This is a general exception")
finally:
    #print ("this is called always")
    file.close() 
