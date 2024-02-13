from Library import *
from helpers import *



library_list = []

with open("library_list.txt", "a+") as library_list_source:
    library_list_source.seek(0)
    libraries = library_list_source.read().split(",")

    for lib in libraries:
        if lib == "":
            break
        library_list.append(BookLibrary(f"{lib}.txt", lib))

if len(library_list) == 0:
    library = BookLibrary("default_lib.txt")
    library_list = [library]
else:
    library = library_list[0]

while True:
    clear_screen()
    print(f"current library is: {library.name}")
    choice = input(
        """
    1- List Your Books
    2- Add A New Book
    3- Delete A Book
    
    4- Show Libraries
    5- Add A New Library
    6- Delete A Library

    7- Change Library

    q- Quit
    
    """
    )

    if choice == "q":
        print("Program shutting down")
        break
    elif choice == "1":
        clear_screen()
        print(f"{library.name}'s books: ")
        library.display_books()
        print("\nPress enter to continue...\n")
        input()
    elif choice == "2":
        clear_screen()
        while True:

            book = input(
                "Please enter the details of the new book: \nname, author, release date, number of page\nq: quit\n"
            )

            if book == "q":
                break

            try:
                library.add_book(book)
                clear_screen()
                print("New book saved!\n")
            except:
                print(
                    "Input must be common to this format: name, author, release date, number of page\n"
                )
        library.save_books()

    elif choice == "3":

        while True:

            book_title = input(
                "Please enter the title of the book you want to delete: \nq: quit\n"
            )
            if book_title == "q":
                clear_screen()
                break
            author_name = input(
                "Please enter the author's name of the book you want to delete: \nq: quit\n"
            )
            if author_name == "q":
                clear_screen()
                break

            clear_screen()
            library.remove_book(book_title, author_name)

        library.save_books()

    elif choice == "4":
        clear_screen()
        print_libraries(library_list)
        print("\nPress enter to continue...\n")
        input()

    elif choice == "5":
        clear_screen()
        print("Already available:")
        print_libraries(library_list)
        link = input("Enter your library name:\n")
        library = BookLibrary(f"{link}.txt", link)
        library_list.append(library)
        save_library_list(library_list)

    elif choice == "6":
        clear_screen()
        print("Already available:")
        print_libraries(library_list)
        name = input(
            "Please enter the title of the library you want to delete:\n q: Quit\n"
        )
        flag = False

        if name != "q":
            for lib in library_list:
                if lib.name == name:
                    library_list.remove(lib)
                    flag = True

        if flag == False:
            print("Library is does not exist\n")
        else:
            print("Library has been deleted\n")

        save_library_list(library_list)
    elif choice == "7":
        clear_screen()
        print("Already available:")
        print_libraries(library_list)

        name = input("Enter the name of the library you want to select\nq: Quit\n")
        flag = False

        if name != "q":
            for lib in library_list:
                if lib.name == name:
                    library = lib
                    flag == True
            if flag == False:
                print(f"There is no library named {name}!")
