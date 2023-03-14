import mysql.connector
import csv


def load_libraries_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        return list(reader)


def load_books_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        return list(reader)


connector = mysql.connector.connect(
    host="localhost",
    user="ADD_USERNAME",
    password="ADD_USER_PASSWORD",
    port=3306,
)

my_cursor = connector.cursor()

my_cursor.execute("CREATE DATABASE IF NOT EXISTS libraries_and_books")
my_cursor.execute("USE libraries_and_books")
my_cursor.execute('''
CREATE TABLE IF NOT EXISTS libraries (
    id INT AUTO_INCREMENT,
    name VARCHAR(100),
    location VARCHAR(100),
    PRIMARY KEY(id)
);
''')

my_cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT,
    title VARCHAR(200),
    author VARCHAR(100),
    genre VARCHAR(100),
    publisher VARCHAR(100),
    library_id INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(library_id) REFERENCES libraries(id)
);
''')

libraries = load_libraries_from_csv('../csv_files/libraries.csv')
sql_lib = "INSERT INTO libraries (id, name, location) VALUES (%s, %s, %s)"
books = load_libraries_from_csv('../csv_files/books.csv')
my_cursor.executemany(sql_lib, libraries)

sql_books = "INSERT INTO books (id, title, author, genre, publisher, library_id) VALUES (%s, %s, %s, %s, %s, %s)"
my_cursor.executemany(sql_books, books)
connector.commit()
