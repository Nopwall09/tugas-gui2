import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="my_oop_database"
)
mycursor = mydb.cursor()

class user:
    def lihat_user():
        sql = "SELECT nama, username, level FROM user"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result  

    def login(username, password):
        sql = "SELECT level FROM user WHERE username = %s AND password = %s"
        val = (username, password)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        return result[0] if result else None
    def buat_user(nama, username, password, level):
        sql = "INSERT INTO user (nama, username, password, level) VALUES (%s, %s, %s, %s)"
        val = (nama, username, password, level)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, f"{nama} berhasil ditambahkan...")
    def update_user(nama, username, password, level):
        sql = "UPDATE user SET nama = %s, password = %s, level = %s WHERE username = %s"
        val = (nama, password, level, username)
        mycursor.execute(sql, val)
        mydb.commit()

        if mycursor.rowcount > 0:
            print(f"User {username} berhasil diperbarui.")
        else:
            print(f"User {username} tidak ditemukan.")
    def cari_user(username):
        sql = "SELECT nama, password, level FROM user WHERE username = %s"
        val = (username,)
        mycursor.execute(sql, val)
        return mycursor.fetchone()
    def get_data_by_id(val1):
        sql = "SELECT * FROM user WHERE nama = %s"
        val = (val1,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        return result
    def hapus_user(username):
        sql = "DELETE FROM user WHERE username = %s"
        val = (username,)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, f"User {username} berhasil dihapus.")
    def lihat_user():
        sql = "SELECT nama, username, level FROM user"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for row in result:
            print(f"Nama: {row[0]}, Username: {row[1]}, Level: {row[2]}")
