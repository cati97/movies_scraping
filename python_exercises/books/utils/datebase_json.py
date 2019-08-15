import json

book_file = 'books.json'


def create_book_table():  # when running for the first time create an empty list
    with open(book_file, 'w') as file:
        json.dump([], file)


def add_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)


def get_all_books():
    with open(book_file, "r") as content:
        return json.load(content)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if name == book['name']:
            book['read'] = True
    _save_all_books(books)


def _save_all_books(books):
    with open(book_file, 'w') as file:
        json.dump(books, file)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if name != book['name']]
    _save_all_books(books)
