
"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""


#tips

"""
Database handling using MySQL on Cloud
"""


"""
https://www.db4free.net
https://www.db4free.net/phpMyAdmin/
MySQL Host Name : db4free.net
Port : 3306
MySQL database name:  yourdbname
MySQL username: yourusername
MySQL user password: dbpassword 
Email address:  your emailid
MYSQL URL : mysql://yourusername:dbpassword@db4free.net/yourdbname

"""

#work start

import mysql.connector 
from pandas import DataFrame
import mysql.connector

conn =mysql.connector .connect(user='kunal99',password='kunal2599',host='db4free.net', database = 'kunal99')

c = conn.cursor()
c.execute("DROP TABLE IF EXISTS students")

c.execute("""CREATE TABLE students(
        name TEXT,
        student_age INTEGER,
        student_roll_no INTEGER,
        student_branch TEXT)""")

c.execute("INSERT INTO students VALUES('KUNAL',20,101,'CSE')")
c.execute("INSERT INTO students VALUES('LAKSHYA',20,102,'CSE')")
c.execute("INSERT INTO students VALUES('GAURAV',20,103,'CSE')")
c.execute("INSERT INTO students VALUES('GUNJAN',20,104,'CSE')")
c.execute("INSERT INTO students VALUES('KASHISH',20,105,'CSE')")
c.execute("INSERT INTO students VALUES('KIRAN',20,106,'CSE')")
c.execute("INSERT INTO students VALUES('BHARAT',20,107,'CSE')")
c.execute("INSERT INTO students VALUES('ISHITA',20,108,'CSE')")
c.execute("INSERT INTO students VALUES('KHUSHBU',20,109,'CSE')")
c.execute("INSERT INTO students VALUES('MAYANK',20,110,'CSE')")
c.execute("SELECT * FROM students")
print(c.fetchall())
columns=[]
columns=["Student_Name", "Student_Age", "Student_Roll_no", "Student_Branch"]

db=DataFrame(c.fetchall(),columns=columns)

conn.commit()

conn.close()