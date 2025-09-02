# MADE BY V. PASINDU RANSIKA 

# headers
print("\n< < < < Pasindu Cinema > > > > \n")
print("Welcome to the Cinema World !")


# movie class
class Movie:
    def __init__(self, movie_id, title, director, year, genre):
        self.MovieID = movie_id
        self.Title = title
        self.Director = director
        self.Year = year
        self.Genre = genre
# how to display when we call
    def __str__(self):
        return f"MovieID: {self.MovieID}, Title: {self.Title}, Director: {self.Director}, Year: {self.Year}, Genre: {self.Genre}"


# guiding users by correct inputs
def id_only(): 
    print("(** Please ENTER Movie ID only with numbers! \"ex-1234\" **)\n")

def year_only():
    print("\n(** Please ENTER YEAR with numbers ! \"ex-2025\" **)\n")

def invalid():
    print("\n# Invalid number #")    


# menu function
def menu():
    print("\n< : : : : MENU : : : : >\n")
    print("Enter [1] to < ADD A NEW MOVIE >")
    print("Enter [2] to < VIEW ALL MOVIES >")
    print("Enter [3] to < SEARCH A MOVIE >")
    print("Enter [4] to < DELETE MOVIE >")
    print("Enter [5] to < UPDATE MOVIES >")
    print("Enter [0] to < EXIT >\n")

    choice = int(input("ENTER: ")) #getting choice from users

    if choice == 1:
        first_Menu() # add a movie menu
    elif choice == 2:
        second_Menu() # view all movies
    elif choice == 3:
        third_Menu() # search movie
    elif choice == 4:
        forth_Menu() # delete movie
    elif choice == 5:
        fifth_Menu() # update movie
    elif choice == 0:
        print("\n<<< Thank you ! Have a nice day! >>>\n")
    else:
        invalid()
        menu() # again direct to menu


# Exit function
def exit_fun():
    print("\n<< Enter 0 to BACK >>\n")
    choice = int(input("ENTER: "))
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
    id_only() #guiding
    movieid = int(input("Enter Movie ID: "))
    
    for movie in movies:
        if movie.MovieID == movieid:
            print("\n!!! Movie ID already exists !!!")
            exit_fun()
            return

    title = input("Enter Title: ")
    director = input("Enter Director: ")
    year_only() #guiding
    year = int(input("Enter Release Year: "))
    genre = input("Enter Genre: ")
    
    new_movie = Movie(movieid, title, director, year, genre)
    movies.append(new_movie) #movies will be added 

    print("\n*** Successfully added to the system ***")
    exit_fun()


# View all movies
def second_Menu():
    print("\n< : : : : Our Movies : : : : >\n")
    if not movies:
        print("\n!!! No movies added yet !!!")
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
        return

    for movie in movies:
        if movie.Title == title:
            print("Found:", movie)
            exit_fun()
            return
    else:
        print("\n!!! Movie not found !!!")
        third_Menu()


# Delete movie
def forth_Menu():
    print("\n< : : : : Delete Movie by ID : : : : >\n")
    id_only() #guiding
    movie_id = int(input("Enter Movie ID to delete: "))

    for movie in movies:
        if movie.MovieID == movie_id:
            print("\nMovie Info:", movie) # print relevent movie info
            print("\n?? Do You Need To Delete ??\n")
            confirm = int(input("1 - confirm | 0 - cancel: ")) # delete confirmation 
            if confirm == 1:
                movies.remove(movie) # deleted
                print("\n*** Movie deleted successfully ***")
            else:
                print("\n*** Cancelled ***")
            exit_fun()
            return
    else:
        print("\n!!! Movie ID not found !!!")
        exit_fun()


# Update movie
def fifth_Menu():
    print("\n< : : : : Update Movie by ID : : : : >\n")
    id_only() #guiding
    movie_id = int(input("Enter Movie ID to update: "))

    for movie in movies:
        if movie.MovieID == movie_id:
            print("Current Movie Info:", movie) # print relevent movie info
            confirm = int(input("\n1 - confirm | 0 - cancel:\n ")) # update confirmation
            if confirm == 1:
                movie.Title = input("Enter new title: ")
                movie.Director = input("Enter new director: ")
                year_only() #guiding
                movie.Year = int(input("Enter new release year: "))
                movie.Genre = input("Enter new genre: ")
                print("\n*** Movie updated successfully ***")
            else:
                print("\n!!! Cancelled !!!")
            exit_fun()
            return

    print("\n!!! Movie ID not found !!!")
    exit_fun()


# Start program
menu()
