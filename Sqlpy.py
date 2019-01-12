
#for the data to display on image
def getData(id):
    import sqlite3
    conn = sqlite3.connect(r'students.db')
    cmd = "SELECT * FROM STUDENTS WHERE ID=" + str(id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
        print(row)
    conn.close()
    return profile
#to add a date column
def newDate(date):
    import sqlite3
    conn = sqlite3.connect(r'students.db')
    cmd = "ALTER TABLE STUDENTS ADD COLUMN [" + date + "]  TEXT"
    cursor = conn.execute(cmd)
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM STUDENTS")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
    conn.close()
#to check data availablity
def isavail(date):
    import sqlite3
    conn = sqlite3.connect(r'students.db')
    #cursor = conn.execute(cmd)
    cur = conn.cursor()
    md = "PRAGMA table_info('STUDENTS')"
    cur.execute(md)
    rows = cur.fetchall()
    for row in rows:
        if(date in row[1]):
            return True
#to set Present/Absent and update attendance
def updateAttedance(id,Date,status):
    import sqlite3
    conn = sqlite3.connect(r'students.db')
    cmd = "UPDATE STUDENTS SET ATTENDANCE = ATTENDANCE+1 WHERE ID="+str(id) 
    conn.execute(cmd)
    conn.commit()
    cmd = "UPDATE STUDENTS SET ["+Date+ "]= 'Present' WHERE ID =" + str(id) 
    conn.execute(cmd)
    conn.commit()
    conn.close()

def InsertorUpdate():
    id = input("Input the id")
    Name = input("Enter the name")
    import sqlite3
    conn = sqlite3.connect(r'students.db')
    cmd = "SELECT * FROM STUDENTS WHERE ID=" + str(id)
    cursor = conn.execute(cmd)
    exist = 0
    for row in cursor:
        exist += 1
    if(exist == 1):
        cmd = "UPDATE STUDENTS SET NAME ='"+str(Name)+"' WHERE ID="+str(id)
        print('hi')
    else:
        cmd = "INSERT INTO STUDENTS(ID,NAME) VALUES ("+str(id)+",'" + str(Name) + "')"
        print(cmd)
    conn.execute(cmd)
    conn.commit()
    conn.close()

