import mysql.connector

def get_data():
    mydb = mysql.connector.connect(host ="localhost",user="root",password="MaNd",database = "testdb")
    mycursor =mydb.cursor()
    mycursor.execute("SELECT * FROM employee")
    result = mycursor.fetchmany()
    mycursor.close()
    mydb.close()
    return result