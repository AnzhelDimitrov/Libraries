from controllers.libraries_controller import LibraryController
from controllers.books_controller import BookController
from db.connections import mydb
from utilities.utility import print_blank_line

librariesController = LibraryController()
books = BookController()

librariesController.show_all_libraries()
print_blank_line()

lib_id = 0

while True:
    lib_id = input(f"Which library would you like to visit today? Enter library id: ").strip()
    if librariesController.show_library(lib_id):
        print_blank_line()
        break


while True:
    book_cmd = input('You have the following options: View all books(1), Add a new book(2), delete an existing book('
                     '3), choose a different library/exit(0): ').strip()

    if book_cmd == '0':
        mydb.close()
        print('Have a nice day!')
        break

    elif book_cmd == '1':
        print_blank_line()
        print(f'Here is a list of all the books!')
        if books.show_books_in_library(lib_id):
            book_id = input('Would you like to see any of the books? Enter a book id or go back to the main menu(00): '
                            ).strip()

            if book_id != '00':
                books.view_book(book_id)
            else:
                continue
        else:
            continue

        print_blank_line()

        while True:
            edit_cmd = input(
                'You can change the book\'s title(1), author(2), genre(3), publisher(4), or go back to the '
                'main menu(00): ').strip()

            match edit_cmd:
                case '1':
                    edit_title = input('Add the new title here: ').strip()
                    books.edit_book_title(edit_title, book_id)
                case '2':
                    edit_author = input('Add the new author here: ').strip()
                    books.edit_book_author(edit_author, book_id)
                case '3':
                    edit_genre = input('Add the new genre here: ').strip()
                    books.edit_book_genre(edit_genre, book_id)
                case '4':
                    edit_publisher = input('Add the new publisher here: ').strip()
                    books.edit_book_publisher(edit_publisher, book_id)
                case '00':
                    break
                case _:
                    print('Invalid command!')
                    continue

    elif book_cmd == '2':
        print_blank_line()
        book_val_arr = input('Add book details in the following order separated by commas: title, author, '
                             'genre, publisher: ').split(',')

        if len(book_val_arr) == 4:
            title = book_val_arr[0].strip()
            author = book_val_arr[1].strip()
            genre = book_val_arr[2].strip()
            publisher = book_val_arr[3].strip()

            books.create_new_book(title, author, genre, publisher, lib_id)
        else:
            print_blank_line()
            print('Invalid input!')

    elif book_cmd == '3':
        books.show_books_in_library(lib_id)
        book_id = input('Enter id of the book you wish to delete: ').strip()
        books.remove_book(book_id)
