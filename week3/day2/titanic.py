"""
Code Challenge
  Name: 
    Titanic Analysis
  Filename: 
    titanic.py
  Dataset:
    training_titanic.csv
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
"""
      
import pandas as pd

df=pd.read_csv("training_titanic.csv")
count=df["Survived"].value_counts()[1]#total survived
count=df["Survived"].value_counts()[0]#total died
count=df["Survived"].value_counts(1)[1] * 100.0
 # survived percentage



count=df['Sex'][(df["Sex"] == "male") & (df["Survived"] == 1)].value_counts()
count1=df['Sex'][(df["Sex"] == "male") & (df["Survived"] == 0)].value_counts()

print("Male Survived vs Male died are:" + str(count[0]) + ":" + str(count1[0]))# survival vs death rate of males

count=df['Sex'][(df["Sex"] == "female") & (df["Survived"] == 1)].value_counts()
count1=df['Sex'][(df["Sex"] == "female") & (df["Survived"] == 0)].value_counts()

print("Female Survived vs Female died are:" + str(count[0]) + ":" + str(count1[0]))# survival vs death rate of females

def age_code(age_string):  
    if (age_string < 18) :
        return 1
    elif (age_string >= 18) :
        return 0
    
df["child"]=df["Age"].apply(age_code)

count=df["child"][(df["child"] == 0) & (df["Survived"] == 1)].value_counts()#survival of child
count1=df["child"][(df["child"] == 1) & (df["Survived"] == 1)].value_counts()#surival od others

