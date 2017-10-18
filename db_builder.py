import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#Create the student table
student_table = 'CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);'
c.execute(student_table)

#Create the course table
course_table = 'CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);'
c.execute(course_table)

#Populate student table
student_reader = csv.DictReader(open('peeps.csv'))
for row in student_reader:
    c.execute("INSERT INTO students VALUES (?,?,?)", [row["name"], row["age"], row["id"]])

#Populate course table
course_reader = csv.DictReader(open('courses.csv'))
for row in course_reader:
    c.execute("INSERT INTO courses VALUES (?,?,?)", [row["code"], row["mark"], row["id"]])

#==========================================================
db.commit() #save changes
db.close()  #close database


