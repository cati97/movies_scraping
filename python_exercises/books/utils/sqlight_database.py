from typing import List, Dict, Union
from .database_connection_with import DatabaseConnection


def create_book_table() -> None:  # when running for the first time create an empty list
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')


def add_book(name: str, author: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))


def get_all_books() -> List[Dict[str, Union[str, int]]]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        # books = cursor.fetchall() - returns a list of tuples - [(name, author, read), (..)]
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
        # converts a list of tuples into a list of dictionaries
    return books


def mark_book_as_read(name: str):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name,))


def delete_book(name: str):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name = ?', (name,))


