from db.connections import cursor, mydb
from utilities.utility import convert_tuple_to_str, header_to_str, print_blank_line


class BookController:
    @staticmethod
    def show_books_in_library(lib_id) -> bool:
        val = (lib_id,)
        sql = "SELECT id, title FROM books WHERE library_id = %s"
        cursor.execute(sql, val)
        books = cursor.fetchall()

        if books:
            print(f'{header_to_str(cursor.description)}:')
            for book in books:
                print(convert_tuple_to_str(book))
            print_blank_line()
            return True
        else:
            print('Currently, there are no books in the library!')
            return False

    @staticmethod
    def view_book(book_id):
        val = (book_id,)
        sql = "SELECT id, title, author, genre, publisher FROM books WHERE id = %s"
        cursor.execute(sql, val)
        book = cursor.fetchone()
        print(f'{header_to_str(cursor.description)}:')
        print(convert_tuple_to_str(book))

    @staticmethod
    def edit_book_title(title, book_id):
        if title == '' or len(title) > 200:
            print('Title must be between 1 and 200 characters!')
        else:
            val = (title, book_id)
            sql = "UPDATE books SET title = %s WHERE id = %s"
            cursor.execute(sql, val)
            print('Title successfully updated!')
            mydb.commit()

    @staticmethod
    def edit_book_author(author, book_id):
        if author == '' or len(author) > 100:
            print('Author must be between 1 and 100 characters!')
        else:
            val = (author, book_id)
            sql = "UPDATE books SET author = %s WHERE id = %s"
            cursor.execute(sql, val)
            print('Author successfully updated!')
            mydb.commit()

    @staticmethod
    def edit_book_genre(genre, book_id):
        if genre == '' or len(genre) > 100:
            print('Genre must be between 1 and 100 characters!')
        else:
            val = (genre, book_id)
            sql = "UPDATE books SET genre = %s WHERE id = %s"
            cursor.execute(sql, val)
            print('Genre successfully updated!')
            mydb.commit()

    @staticmethod
    def edit_book_publisher(publisher, book_id):
        if publisher == '' or len(publisher) > 100:
            print('Publisher must be between 1 and 100 characters!')
        else:
            val = (publisher, book_id)
            sql = "UPDATE books SET publisher = %s WHERE id = %s"
            cursor.execute(sql, val)
            print('Publisher successfully updated!')
            mydb.commit()

    @staticmethod
    def create_new_book(title, author, genre, publisher, lib_id):
        if len(title) > 200 or len(title) == 0 or \
                len(author) > 100 or len(author) == 0 or \
                len(genre) > 100 or len(genre) == 0 or \
                len(publisher) > 100 or len(publisher) == 0:
            print('Invalid book details!')
        else:
            sql = "INSERT INTO books (title, author, genre, publisher, library_id) VALUES (%s, %s, %s, %s, %s)"
            val = (title, author, genre, publisher, lib_id)
            cursor.execute(sql, val)
            mydb.commit()
            print('Book was added successfully!')

    @staticmethod
    def remove_book(book_id):
        sql = "SELECT * FROM books WHERE id = %s"
        val = (book_id,)
        cursor.execute(sql, val)
        if cursor.fetchone():
            sql = "DELETE FROM books WHERE id = %s"
            cursor.execute(sql, val)
            mydb.commit()
            print('Book deleted successfully!')
        else:
            print('Invalid book id!')
