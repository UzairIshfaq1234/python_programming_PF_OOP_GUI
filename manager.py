from library import Library
from patron import Patron
from book import Book


class Manager(Library):

    def __init__(self):

        self.choices = [1, 2]
        super().__init__()

    def run_menu(self):
        while True:

            print("""
      wellcome to uzairs library
1 - Borrow a book
2 - Return a book 
                """)

            choice = int(input("Enter your choice: "))

            if choice not in self.choices:
                print("Please enter a valid choice")

            if choice == 1:

                print("\nBorrowing a book...")
                patron_name = input("your name: ")
                patron = Patron(patron_name)
                self.add_patron(patron)

                book_name = input(" name: ")
                book_author = input("book author: ")
                print(super().get_books())
                for book in super().get_books():
                    if book.get_book_name() == book_name:
                        if book.is_checked_out():
                            print("Book already checked out")
                            print("Adding to waitlist...")
                            book.add_to_waitlist(patron)
                            break
                    else:
                        book = Book(book_name, book_author)
                        super().add_book(book)

                print(
                #using f string
                    f"-----\n"
                    f"Book borrowed: \nName: {book_name}\nBook author: {book_author}"
                )

            elif choice == 2:

                print("\nReturning a book...")
                patron_name = input(" your name: ")
                book_name = input("book name: ")

                for patrons in super().get_patrons():
                    if patron.get_name() == patron_name:

                        for book in super().get_books():
                            if book.get_book_name() == book_name:
                                patron.return_book(book)
                                super().remove_book(book)
                                print("Book returned ")
                                break
                            else:
                                print(" book not found!")
                    else:
                        print(
                            "please try again you are not registered!")


manager = Manager()
manager.run_menu()
