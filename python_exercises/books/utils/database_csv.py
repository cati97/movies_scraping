with open("/home/cati/Desktop/python_exercises/books/utils/my_books_csv.txt", "r") as csv:
    lines = csv.readlines()
lines = [line.strip() for line in lines]


def add_book(name, author):
    lines.append(f"{name},{author},NO")
    with open("/home/cati/Desktop/python_exercises/books/utils/my_books_csv.txt", "w") as add:
        add.writelines("\n".join(lines))


def list_books():
    for line in lines:
        name, author, read = line.split(',')
        print(f"Book nr {lines.index(line) + 1}:")
        print(f"Title: {name}, Author: {author}, Read: {read}")


def mark_as_read(name_to_mark):
    for line in lines:
        name, author, read = line.split(',')
        if name_to_mark == name:
            lines.remove(line)
            lines.append(f"{name},{author},YES")
    with open("/home/cati/Desktop/python_exercises/books/utils/my_books_csv.txt", "w") as r:
        r.writelines("\n".join(lines))


def delete_book(name_to_delete):
    for line in lines:
        name, author, read = line.split(',')
        if name_to_delete == name:
            lines.remove(line)
    with open("/home/cati/Desktop/python_exercises/books/utils/my_books_csv.txt", "w") as delete:
        delete.writelines("\n".join(lines))

