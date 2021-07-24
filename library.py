class Library:

    def __init__(self):

        self.books = []
        self.patrons = []

    def get_books(self):
        return self.books

    def get_patrons(self):
        return self.patrons

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)
        book.checked_out = False

    def add_patron(self, patron):
        self.patrons.append(patron)
