import json


def add_book(name, author):
    with open('my_books.txt', 'a') as f:
        json.dump({'name': name, 'author': author, 'read': False}, f)


def list_books():
    pass


def mark_as_read(name):
    pass


def delete_book(name):
    pass
