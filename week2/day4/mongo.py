
"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""

import pymongo
client = pymongo.MongoClient("mongodb://kunalsrivastava365:kunal%402599@cluster0-shard-00-00-cj3z0.mongodb.net:27017,cluster0-shard-00-01-cj3z0.mongodb.net:27017,cluster0-shard-00-02-cj3z0.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
mydb = client.yourdbname

def add_students(Student_Name, Student_Age, Student_Roll_no, Student_Branch):
    mydb.yourcollectionname.insert_one(
            {
            "Student_Name" : Student_Name,
            "Student_Age" : Student_Age,
            "Student_Roll_no" : Student_Roll_no,
            "Student_Branch" : Student_Branch
            })
    return "Employee added successfully"

def fetch_all_students():
    user = mydb.yourcollectionname.find()
    for i in user:
        print (i)


add_students('Sylvester',20, 101,'cse')
add_students('Yogendra', 71,102,'cse')
add_students('Yogendra', 70,102,'cse')

fetch_all_students()

