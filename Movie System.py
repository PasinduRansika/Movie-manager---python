# Created by : V.P Ransika


print("\n< < < < Pasindu Cinema > > > > \n")
print("Welcome to the Cinema World !")

# Movie class
class Movie:
    def __init__(self, Movie_id, title, director, year, genre):
        self.Movie_id = Movie_id
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        
# this is how display movies when we call them
    def __str__(self):
        return f"Movie-ID: {self.Movie_id}, Title: {self.title}, Director: {self.director}, Year: {self.year}, Genre: {self.genre}"

# Guiding users how to enter 
def id_only():
    print("(** Please ENTER Movie ID only with numbers! \"ex-1234\" **)\n")

def year_only():
    print("\n(** Please ENTER YEAR with numbers! \"ex-2025\" **)\n")

def invalid():
    print("\n# Invalid Please Enter Correctly #")    

# Menu function
def menu():
    print("\n< : : : : MENU : : : : >\n")
    print("Enter [1] to < ADD A NEW MOVIE >")
    print("Enter [2] to < VIEW ALL MOVIES >")
    print("Enter [3] to < SEARCH A MOVIE >")
    print("Enter [4] to < DELETE MOVIE >")
    print("Enter [5] to < UPDATE MOVIES >")
    print("Enter [0] to < EXIT >\n")

    try:
        choice = int(input("ENTER: "))
    except ValueError:
        invalid()
        menu()
        

    if choice == 1: 
        first_Menu() # add movie menu
    elif choice == 2:
        second_Menu() # view movie menu
    elif choice == 3:
        third_Menu() # search movie menu
    elif choice == 4:
        fourth_Menu() # delete movie menu
    elif choice == 5:
        fifth_Menu() # movie update menu
    elif choice == 0:
        print("\n<<< Thank you ! Have a nice day! >>>\n") # exit from menu
    else:
        invalid()
        menu()

# Exit function
def exit_fun():
    print("\n<< Enter 0 to BACK >>\n")
    try:
        choice = int(input("ENTER: "))
    except ValueError:
        invalid()
        exit_fun()
    
    if choice == 0: 
        menu()
    else:
        invalid()
        exit_fun()

# Movie list
movies = []

# Add movie
def first_Menu():
    print("\n< : : : : Add a New Movie : : : : >\n")
    id_only() # enter number only
    try:
        movieid = int(input("Enter Movie ID: "))
    except ValueError:
        invalid()
        exit_fun()

    for movie in movies:
        if movie.Movie_id == movieid:
            print("\n!!! Movie ID already exists !!!")
            exit_fun()
            return # exit function if Movie_id == movieid  

# if it is not it will start here
    title = input("Enter Title: ")
    director = input("Enter Director: ")
    year_only() # enter number only
    try:
        year = int(input("Enter Release Year: "))
    except ValueError:
        invalid()
        exit_fun()

    genre = input("Enter Genre: ")
    new_movie = Movie(movieid, title, director, year, genre)
    movies.append(new_movie) # movie added

    print("\n*** Successfully added to the system ***")
    exit_fun()

# View all movies
def second_Menu():
    print("\n< : : : : Our Movies : : : : >\n")
    if not movies:
        print("\n!!! No movies added yet !!!")
    else:
        for movie in movies:
            print(movie) # print all movies
    exit_fun()

# Search movie
def third_Menu():
    print("\n< : : : : Search Movie by the TITLE : : : : >\n")
    print("\n~ Enter - 0 to exit ~")
    title = input("\nEnter Title to search: ")
    if title == "0": # another exit
        menu()
        return # exit function if title == "0"

    for movie in movies:
        if movie.title == title:
            print("|**Found**|", movie)
            exit_fun()
            return # exit function 
    else:
        print("\n!!! Movie not found !!!")
        third_Menu()

# Delete movie
def fourth_Menu():
    print("\n< : : : : Delete Movie by ID : : : : >\n")
    id_only() # enter number only
    try:
        movie_id = int(input("Enter Movie ID to delete: "))
    except ValueError:
        invalid()
        exit_fun()

    for movie in movies:
        if movie.Movie_id == movie_id:
            print("\nMovie Info:", movie)
            print("\n?? Do You Need To Delete ??\n")
            try:
                confirm = int(input("1 - confirm | 0 - cancel: "))
            except ValueError:
                invalid()
                exit_fun()

            if confirm == 1: # movie delete confirmation
                movies.remove(movie)
                print("\n*** Movie deleted successfully ***")
            else: # 0
                print("\n*** Cancelled ***")
            exit_fun()
            
    else:
        print("\n!!! Movie ID not found !!!")
        exit_fun()

# Update movie
def fifth_Menu():
    print("\n< : : : : Update Movie by ID : : : : >\n")
    id_only() # enter number only
    try:
        movie_id = int(input("Enter Movie ID to update: "))
    except ValueError:
        invalid()
        exit_fun()
        

    for movie in movies:
        if movie.Movie_id == movie_id:
            print("Current Movie Info:", movie)
            try:
                confirm = int(input("\n1 - confirm | 0 - cancel:\n ")) # movie update confirmation
            except ValueError:
                invalid()
                exit_fun()

            if confirm == 1:
                movie.title = input("Enter new title: ")
                movie.director = input("Enter new director: ")
                year_only() # enter number only
                try:
                    movie.year = int(input("Enter new release year: "))
                except ValueError:
                    invalid()
                    exit_fun()
                 
                movie.genre = input("Enter new genre: ")
                print("\n*** Movie updated successfully ***")
            else: # 0
                print("\n!!! Cancelled !!!")
            exit_fun()
            
    else: # Movie_id != movie_id:
        print("\n!!! Movie ID not found !!!")
        exit_fun()

# Start program
menu()