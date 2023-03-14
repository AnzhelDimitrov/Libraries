import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='ADD_USERNAME',
    password='ADD_USER_PASSWORD',
    database='libraries_and_books'
)

cursor = mydb.cursor()
