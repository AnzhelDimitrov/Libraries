from db.connections import cursor
from utilities.utility import convert_tuple_to_str, header_to_str


class LibraryController:
    @staticmethod
    def show_all_libraries():
        sql = "SELECT * FROM libraries"
        cursor.execute(sql)
        libraries = cursor.fetchall()
        if libraries:
            print('Here is a list of all available libraries!')
            print(f'{header_to_str(cursor.description)}:')

            for library in libraries:
                print(convert_tuple_to_str(library))

    @staticmethod
    def show_library(lib_id) -> bool:
        val = (lib_id,)
        sql = "SELECT name FROM libraries WHERE ID = %s"
        cursor.execute(sql, val)
        lib_value = cursor.fetchone()
        if lib_value:
            print(f'{header_to_str(cursor.description)}: {convert_tuple_to_str(lib_value)}')
            print('Excellent choice!')
            return True
        else:
            print('Invalid library id!')
            return False
