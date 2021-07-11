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
    print("Please enter the below details to add student details:  \n 1. Name \n 2. Department \n 3. Tamil Mark \n 4. English Mark \n 5. Maths Mark \n 6. Science Mark \n 7. Social Science Mark ")
    inp_A,inp_B,inp_C,inp_D,inp_E,inp_F,inp_G=input().split()
    inp_C=int(inp_C)
    inp_D=int(inp_D)
    inp_E=int(inp_E)
    inp_F=int(inp_F)
    inp_G=int(inp_G)

    totalmark=(inp_C+inp_D+inp_E+inp_F+inp_G)
    average=(inp_C+inp_D+inp_E+inp_F+inp_G)/5
    gradeper=grade(average)
    

    connection=sql_connection()
    sql_insert(connection,inp_A,inp_B,inp_C,inp_D,inp_E,inp_F,inp_G,totalmark,average,gradeper)

else:
    print("exit")