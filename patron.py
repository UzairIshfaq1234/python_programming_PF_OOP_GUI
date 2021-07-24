class Patron:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.number_of_books = len(self.books)

    def get_name(self):
        return self.name

    def borrow_book(self, book):
        if self.number_of_books > 3:
            print("Return the book first...than barrow!!")

        else:
            self.books.append(book)

    def return_book(self, book):
        self.books.remove(book)
