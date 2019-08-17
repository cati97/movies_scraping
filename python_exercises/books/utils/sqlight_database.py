import sqlite3


def create_book_table():  # when running for the first time create an empty list
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
    connection.commit()
    connection.close()


def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    # not recommended !! - dangerous for injection attacks
    # cursor.execute(f'INSERT INTO books VALUES("{name}", "{author}", 0)')
    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    # books = cursor.fetchall() - returns a list of tuples - [(name, author, read), (..)]
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    # converts a list of tuples into a list of dictionaries
    connection.close()  # nothing new to save to the disc so no need of commit()

    return books


def mark_book_as_read(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name,))
    connection.commit()
    connection.close()


def delete_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE name = ?', (name,))
    connection.commit()
    connection.close()


