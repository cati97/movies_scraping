"""
The app can do 4 things:
[x] show python_exercises
[x] add a movie to the collection
[x] find a particular movie
[x] quit

Movies will be stored in lists

"""
movies = []


def menu():

    user_input = input("""
a - add a movie
s - show all python_exercises
f - find movie 
q - quit

>> """)

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 's':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print("Unknown command, please try again ")

        user_input = input("""
a - add a movie
s - show all python_exercises
f - find movie 
q - quit 

>> """)
    else:
        print("Bye now")


def add_movie():
    title = input("Enter the movie's title: ")
    year = input("Enter the year: ")
    genre = input("Enter the genre: ")
    movie = {
        "title": title,
        "year": year,
        "genre": genre
    }
    movies.append(movie)


def show_movies(movies_list):
    for movie in movies_list:
        print("\nMovie " + str(movies_list.index(movie) + 1) + ": ")
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Title: {movie['title']}")
    print(f"Year: {movie['year']}")
    print(f"Genre: {movie['genre']}")


def find_movie():
    find_by = input("What property are you looking for (title, year, genre)? ")
    find_this = input("What specific value are you searching for? ")
    found = []

    for movie in movies:
        if find_this == movie[find_by]:
            found.append(movie)

    show_movies(found)


menu()
