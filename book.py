class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = True
        self.waitlist = []

    def get_book_name(self):
        return self.title

    def get_book_author(self):
        return self.author

    def is_checked_out(self):
        return self.checked_out

    def add_to_waitlist(self, patron):
        self.waitlist.append(patron)

    def remove_from_waitlist(self, patron):
        self.waitlist.remove(patron)
