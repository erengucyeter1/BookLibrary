from Library import *
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear_screen')

library = BookLibrary("books.txt")

while (True):
    clear_screen()
    choice  = input(
    '''
    1- List Your Books
    2- Add A New Book
    3- Delete A Book
    q- Quit
    
    ''')


    if choice  == "q":
        print("Program shutting down")
        break
    elif choice  == "1":
        
        library.display_books()
        print("\nPress enter to continue...\n")
        input()
    elif choice  == "2":
        clear_screen()
        while True:
            
            book = input("Please enter the details of the new book: \nname, author, release date, number of page\nq: quit\n")

            if book == "q":
                break

            try:
                library.add_book(book)
                clear_screen()
                print("New book saved!\n")
            except:
                print("Input must be common to this format: name, author, release date, number of page\n")
        library.save_books()

    elif choice  == "3":
       
        while True:
            
            book_title = input("Please enter the title of the book you want to delete: \nq: quit\n")
            if book_title == "q":
                clear_screen()
                break
            author_name = input("Please enter the author's name of the book you want to delete: \nq: quit\n")
            if author_name == "q":
                clear_screen()
                break
            
            clear_screen()
            library.remove_book(book_title,author_name)

        library.save_books()
