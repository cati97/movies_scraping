# [x] create an empty list to store books
# [x] create add book method
# [x] create list all books method
# [x] create mark as read
# [x] create remove a book from books


books = []  # list of dictionaries


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


def list_books():
    for book in books:
        print(f"name: {book['name']}")
        print(f"author: {book['author']}")
        print(f"read: {str(book['read'])}")


def mark_as_read(name):
    for book in books:
        if name == book['name']:
            book['read'] = True


def delete_book(name):
    for book in books:
        if name == book['name']:
            books.remove(book)
