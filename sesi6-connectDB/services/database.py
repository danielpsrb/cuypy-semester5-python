import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='your_dbname'
)

def insert_item(kode_barang, nama_barang, stock_barang):
    cursor = database.cursor()
    insert = cursor.execute("INSERT INTO tbl_barang (kode_barang, nama_barang, stock_barang) VALUES (%s, %s, %s)", (kode_barang, nama_barang, stock_barang))
    database.commit()
    return insert
