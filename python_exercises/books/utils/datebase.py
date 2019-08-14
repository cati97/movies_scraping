import json

with open("/home/cati/Desktop/python_exercises/books/utils/my_books.txt", "r") as content:
    books = json.load(content)


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})
    with open("/home/cati/Desktop/python_exercises/books/utils/my_books.txt", "w") as add:
        json.dump(books, add)


def list_books():
    print(books)


def mark_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True
    with open("/home/cati/Desktop/python_exercises/books/utils/my_books.txt", "w") as read:
        json.dump(books, read)


def delete_book(name):
    books_update = [book for book in books if name != book['name']]
    with open("/home/cati/Desktop/python_exercises/books/utils/my_books.txt", "w") as delete:
        json.dump(books_update, delete)


''' not recommended practice to remove from list while iterating over it
def delete_book(name):
    for book in books:
        if book['name'] == name:
            books.remove(book)
    with open("/home/cati/Desktop/python_exercises/books/utils/my_books.txt", "w") as delete:
        json.dump(books, delete)
'''