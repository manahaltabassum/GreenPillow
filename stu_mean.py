import sqlite3

f = "discobandit.db"

db = sqlite3.connect(f)
c = db.cursor()

avg_dict = {}

#==========================================================

#creates a dictionary with key = ID and value = average
def createDict():
    stu_grades = c.execute('SELECT students.id, mark FROM students, courses WHERE students.id = courses.id;')
    for row in stu_grades: #adds ID's as keys to dict, value as list of grades
        print row
        if not(avg_dict.has_key(row[0])):
            avg_dict[row[0]] = [row[1]]
        else:
            avg_dict[row[0]].append(row[1])
    #prints avg_dict before averages
    print "Before averaging..."
    print avg_dict
    #replaces value of key with average of grades
    for key in avg_dict:
        avg_dict[key] = getAvg(avg_dict[key])
    #prints avg_dict after averaging
    print "After averaging..."
    print avg_dict


#calculates the average of a list of grades
def getAvg(arr):
    sum = 0
    num = 0
    for val in arr:
        sum += val
        num += 1
    return (sum*1.0)/num


#prints name, id, and average of eacg student
def display():
    '''print "The names of all students..."
    for key in avg_dict:
        print getName(key)'''
    print "The averages of all students..."
    for key in avg_dict:
        ret = "Name: " + getName(key) + " ID: " + str(key) + " Average: " + str(avg_dict.get(key))
        print ret

        
#obtains name of student based on ID
def getName(stu_ID):
    name = c.execute('SELECT name FROM students WHERE id = ' + str(stu_ID) + ';')
    stu_name = ''
    for x in name:
        stu_name = x[0]
    return stu_name


#creates table with ID and average
def createAvgTable():
    avg_table= 'CREATE TABLE peeps_avg (id INTEGER, average INTEGER);'
    c.execute(avg_table)
    for key in avg_dict:
        c.execute('INSERT INTO peeps_avg VALUES (?,?)',[key,avg_dict.get(key)])


#prints average for student
def avg(stu_ID):
    table = c.execute('SELECT * FROM peeps_avg WHERE id= ' + str(stu_ID) + ';')
    for x in table:
        print x


#updates the average based on ID     
def updateAvg(stu_ID, new_avg):
    print "Old Average..."
    avg(stu_ID)
    c.execute('UPDATE peeps_avg SET average =' + str(new_avg) + ' WHERE id = ' + str(stu_ID) + ';')
    print "New Average..."
    avg(stu_ID)


#adds course grade to course table
def addCourse(new_code, new_mark, new_id):
    c.execute('INSERT INTO courses VALUES ("%s",%d,%d)'%(new_code, new_mark, new_id))
    
createDict()
display()
createAvgTable()
updateAvg(2, 100)
updateAvg(4, 50)
addCourse('spanishfilms', 95, 3)

db.commit()
db.close()
