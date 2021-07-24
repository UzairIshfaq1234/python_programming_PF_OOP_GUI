from datetime import date, datetime

class Notebook:

    def __init__(self, subject):
        self.subject = subject
        self.pages = 0
        self.notes = []
    
    def get_author(self):
        return self.subject

    def get_pages(self):
        return self.pages

    def notebook_new_note(self, note):
        self.pages += 1
        page_number = self.pages
        note_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        new_note = Note(note, note_date, page_number)

        self.notes.append(new_note)

        return new_note

    def get_note(self, page_number):
        if page_number <= self.pages:
            return self.notes[page_number]

    def get_notes(self):
        return self.notes

class Note:

    def __init__(self, note, time, page):
        self.note = note
        self.time = time
        self.page = page

    def get_note_time(self):
        return self.time

    def get_note_text(self):
        return self.note

    def get_note_page_number(self):
        return self.page

print("\n")
print("\n")
notebook = Notebook("OOP")
print("_________________________________")
print("OBJECT ORIENTED PROGRAMMING NOTES")
print("_________________________________")
print("\n")

note1 = notebook.notebook_new_note("CHAPTER 1:INTRODUCTION")
note2 = notebook.notebook_new_note("CHAPTER 2:PYHTON PROGRAMMING FUNDAMENTAL")
note3 = notebook.notebook_new_note("CHAPTER 3:OOP IN PYTHON")
note4 = notebook.notebook_new_note("CHAPTER 4:PROGRAMS IN PYTHON")


print("Number of notebook pages: ", notebook.get_pages())
print("_______________________________________")

for note in notebook.get_notes():
    print(note.get_note_text())
