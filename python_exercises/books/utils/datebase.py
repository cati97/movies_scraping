import json

with open("/home/cati/Desktop/python_exercises/books/utils/my_books.txt", "r") as content:
    books = json.load(content)


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})
    with open("/home/cati/Desktop/python_exercises/books/utils/my_books.txt", "w") as add:
        json.dump(books, add)


def list_books():
    for book in books:
        print(f"Book nr {books.index(book) + 1}:")
        print(f"Title: {book['name']}, Author: {book['author']}, Read: {book['read']}")


def mark_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True
    with open("/home/cati/Desktop/python_exercises/books/utils/my_books.txt", "w") as read:
        json.dump(books, read)


def delete_book(name):
    global books  # don't create a local new variable but change the global one
    books = [book for book in books if name != book['name']]
    with open("/home/cati/Desktop/python_exercises/books/utils/my_books.txt", "w") as delete:
        json.dump(books, delete)


''' not recommended practice to remove from list while iterating over it
def delete_book(name):
    for book in books:
        if book['name'] == name:
            books.remove(book)
    with open("/home/cati/Desktop/python_exercises/books/utils/my_books.txt", "w") as delete:
        json.dump(books, delete)
'''