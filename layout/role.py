import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="my_oop_database"
)
mycursor = mydb.cursor()

class role:
    def select_data():
        sql = "SELECT role FROM role"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        data = []
        for x in myresult:
            data.append(x[0])
        return data
