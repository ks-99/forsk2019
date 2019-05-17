
"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""

import sqlite3
from pandas import DataFrame

conn=sqlite3.connect("db_university")
c=conn.cursor()

c.execute("""CREATE TABLE students(
        name STRING,
        student_age INTEGER,
        student_roll_no INTEGER,
        student_branch)""")

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
columns=[]
columns=["Student_Name","Student_Age","Student_Roll_no","Student_Branch"]
df=DataFrame(c.fetchall(),columns=columns)

conn.commit()
c.close()