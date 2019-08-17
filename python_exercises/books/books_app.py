from books.utils.sqlight_database import *

user_choice = """
Enter:
- 'a' to add a new book
- 'l' to list all the books
- 'r' to mark a book as read
- 'd' to delete a book 
- 'q' to quit

Your choice: """


def menu():
    create_book_table()
    user_input = input(user_choice)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_mark_as_read()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("I don't understand your command, please try again.")
            user_input = input(user_choice)
        print("Well done! Now let's do something different :) ")
        user_input = input(user_choice)
    else:
        print("Byeeee")


def prompt_add_book():
    book_name = input("Enter the book's name: ")
    book_author = input("Enter the book's author: ")
    add_book(book_name, book_author)


def list_books():
    for book in get_all_books():
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']} — Read: {read}")


def prompt_mark_as_read():
    book_name = input("Name of the book that you want to mark as read: ")
    mark_book_as_read(book_name)


def prompt_delete_book():
    book_name = input("Name of the book that you want to delete: ")
    delete_book(book_name)


menu()
