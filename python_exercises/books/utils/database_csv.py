books_file = 'books.txt'


def create_book_table():
    with open(books_file, 'a') as file:
        pass  # just to make sure the file is there


def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]


def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write(f'{name},{author},NO\n')


def _save_all_books(books):  # _ means private method - use only within this file
    with open(books_file, 'w') as file:  # overwrite the file
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = 'YES'
    _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)
