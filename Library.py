class Book:
    def __init__(self, book):
        self.name = book[0]
        self.author = book[1]
        self.realese = book[2]
        self.page = book[3]


class BookLibrary:
    def __init__(self, source, name="default"):
        self.name = name
        self.book_list = []
        self.source = source
        with open(source, "a+") as file:  # r
            file.seek(0)
            data = file.read().splitlines()

            for book in data:
                self.book_list.append(Book(book.split(",")))
        file.close()

    def display_books(self):

        if len(self.book_list) == 0:
            print("\nYou do not have any book yet!\n")
            return

        for book in self.book_list:
            print(
                f"Name: {book.name}, Author: {book.author}, Realese date: {book.realese}, Page: {book.page}\n"
            )

    def is_book_duplicate(self, newBook):

        for book in self.book_list:
            if book.name == newBook[0] and book.author == newBook[1]:
                return book
        return 0

    def find_book(self, name, author):

        for book in self.book_list:
            if book.name == name and book.author == author:
                return book
        return 0

    def convert_book_to_string(self, book):

        text = f"{book.name}, {book.author}, {book.realese}, {book.page}\n"
        return text

    def remove_book(self, name, author):
        currBook = self.find_book(name, author)

        if currBook == 0:
            print("This book does not exist.")
            return

        self.book_list.remove(currBook)
        print("Book has been removed!\n")

    def save_books(self):

        self.book_list = sorted(self.book_list, key=lambda x: x.name)

        with open(self.source, "a+") as file:
            file.seek(0)
            file.truncate(0)

            for book in self.book_list:
                file.write(self.convert_book_to_string(book))

    def add_book(self, info):  # info bir txt ve sonradan parçalanmalı
        book = info.split(",")

        if self.is_book_duplicate(book):
            print("This book is already exist!")
        else:
            self.book_list.append(Book(book))

            with open("books.txt", "a") as file:
                file.write(info + "\n")
