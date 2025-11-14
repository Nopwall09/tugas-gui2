import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="my_oop_database"
)
mycursor = mydb.cursor()

class barang:
    def get_data_by_id(val1):
        sql = "SELECT * FROM barang WHERE id = %s"
        val = (val1,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        return result
    def insert_data(val1, val2, val3, val4, val5):
        sql = "INSERT INTO barang (id, nama, stok, harga, kategori_nama) VALUES (%s, %s, %s, %s, %s)"
        val = (val1, val2, val3, val4, val5)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil ditambahkan...")
    def delete_data(val1):
        try:
            sql = "DELETE FROM barang WHERE id = %s"
            val = (val1,)
            mycursor.execute(sql, val)
            mydb.commit()
            if mycursor.rowcount > 0:
                print(f"Data dengan ID {val1} berhasil dihapus.")
            else:
                print(f"Tidak ada data yang diubah (ID {val1} tidak ditemukan).")
        except mysql.connector.Error as e:
            print("Gagal menghapus data:", e)

    def update_data(val1, val2, val3, val4, val5):
        try:
            sql = "UPDATE barang SET nama = %s, stok = %s, harga = %s, kategori_nama = %s WHERE id = %s"
            val = (val1, val2, val3, val4, val5)
            mycursor.execute(sql, val)
            mydb.commit()

            if mycursor.rowcount > 0:
                print(f"Data dengan ID {val5} berhasil diperbarui.")
            else:
                print(f"Tidak ada data yang diubah (ID {val5} tidak ditemukan).")

        except mysql.connector.Error as e:
            print("Gagal memperbarui data:", e)