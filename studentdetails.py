import mysql.connector
from mysql.connector import Error
import sys

def sql_connection():

    try:
       connection=mysql.connector.connect(host="localhost",user="root",password="root",database="test")
       return connection
    except Error:
        print(Error)

def sql_insert(connection,inp_A,inp_B,inp_C,inp_D,inp_E,inp_F,inp_G,totalmark,average,gradeper):
    try:
        cursor=connection.cursor()
        sql="INSERT INTO test.student_mark (NAME,department,mark1,mark2,mark3,mark4,mark5,totalmark,average,grade) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data=[inp_A,inp_B,inp_C,inp_D,inp_E,inp_F,inp_G,totalmark,average,gradeper]
        cursor.execute(sql,data)
        connection.commit()
        connection.close()
        print("DETAILS ADDED")
    except Error as e:
        connection.rollback()
        print("ERROR PRINING ", e)

def sql_select(connection,student_id):
    cursor=connection.cursor()
    
    if(student_id==-1):
        cursor.execute("SELECT * FROM test.student_mark")
    else:
        sql="SELECT * FROM test.student_mark where StudId=%s"
        data=[student_id]
        cursor.execute(sql,data)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)

def sql_update(connection,inp_A,inp_B,inp_C,inp_D,inp_E,inp_F,inp_G,totalmark,average,gradeper,inp_H):
    try:
        cursor=connection.cursor()
        sql="update test.student_mark set NAME=%s,department=%s,mark1=%s,mark2=%s,mark3=%s,mark4=%s,mark5=%s,totalmark=%s,average=%s,grade=%s where StudId=%s"
        data=[inp_A,inp_B,inp_C,inp_D,inp_E,inp_F,inp_G,totalmark,average,gradeper,inp_H]
        cursor.execute(sql,data)
        connection.commit()
        connection.close()
        print("DETAILS UPDATED for ",inp_H)

    except Error as e:
        connection.rollback()
        print("ERROR Updating ", e)

def sql_delete(connection,inp_H):
    try:
        cursor=connection.cursor()
        sql="delete from test.student_mark  where StudId=%s"
        data=[inp_H]
        cursor.execute(sql,data)
        connection.commit()
        connection.close()
        print("DETAILS DELETED for ",inp_H)

    except Error as e:
        connection.rollback()
        print("ERROR PRINING ", e)        

def grade(average):
    if(average>=95):
        return "A+"
    elif(average>=90):
        return "A"
    elif(average>=75):
        return "B"
    elif(average>=60):
        return "C"
    else:
        return "D"
    
print("Please enter the below option \n 1. add new student \n 2. get student \n 3. get all student \n 4. edit a student \n 5. delete a student \n 6. exit")

inp_1 = int(input("Enter the Value to continue : "))

if(inp_1==6 or inp_1<0 or inp_1>6):
    print("Thanks for Connecting")
    sys.exit()
    
elif(inp_1==1):    
 
    inp_A=input("Enter the Name : ")
    inp_B=input("Enter the Dept : ")
    inp_C=int(input("Enter the Tamil Mark : "))
    inp_D=int(input("Enter the English Mark : "))
    inp_E=int(input("Enter the Maths Mark : "))
    inp_F=int(input("Enter the Science Mark : "))
    inp_G=int(input("Enter the S.Science Mark : "))
 
    totalmark=(inp_C+inp_D+inp_E+inp_F+inp_G)
    average=(inp_C+inp_D+inp_E+inp_F+inp_G)/5
    gradeper=grade(average)
    
    connection=sql_connection()
    sql_insert(connection,inp_A,inp_B,inp_C,inp_D,inp_E,inp_F,inp_G,totalmark,average,gradeper)

elif(inp_1==2):

    inp_A=input(" Please Enter the Student Id : ")


elif(inp_1==3):

    print(" Getting All Student Details from DataBase ")

    connection=sql_connection()
    sql_select(connection,-1)

elif(inp_1==4):     

    inp_H=input("Enter Student Id : ")
    inp_A=input("Enter the Name : ")
    inp_B=input("Enter the Dept : ")
    inp_C=int(input("Enter the Tamil Mark : "))
    inp_D=int(input("Enter the English Mark : "))
    inp_E=int(input("Enter the Maths Mark : "))
    inp_F=int(input("Enter the Science Mark : "))
    inp_G=int(input("Enter the S.Science Mark : "))
 
    totalmark=(inp_C+inp_D+inp_E+inp_F+inp_G)
    average=(inp_C+inp_D+inp_E+inp_F+inp_G)/5
    gradeper=grade(average)
    
    connection=sql_connection()
    sql_update(connection,inp_A,inp_B,inp_C,inp_D,inp_E,inp_F,inp_G,totalmark,average,gradeper,inp_H)

elif(inp_1==5):     

    inp_H=input("Enter Student Id to Delete : ")
    connection=sql_connection()
    sql_delete(connection,inp_H)


else:
    print("exit")