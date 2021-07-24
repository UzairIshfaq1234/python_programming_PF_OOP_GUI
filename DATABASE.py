import CD
import DVD
class DoME:
    def __init__(self):
        self.DBCD=[]
        self.DBDVD=[]
    def add_CD(self):
        print("--------------------------")
        title=input("Title of Your CD:")
        artist=input("Artist Name:")
        playingTime=int(input("Playing Time:"))
        tracks=int(input("Number of Tracks"))
        print("--------------------------")
        cd=CD.CDs(title,artist,playingTime,tracks)
        self.DBCD.append(cd)
    def add_DVD(self):
        print("--------------------------")
        title=input("Title of Your DVD:")
        director=input("Director Name:")
        playingTime=int(input("Playing Time:"))
        print("--------------------------")
        dvd=DVD.Videos(title,director,playingTime)
        self.DBDVD.append(dvd)
    def print_CD(self,i):
        self.DBCD[i].printCD()
    def print_DVD(self,i):
        self.DBDVD[i].printDVD()
    def all_CDs(self):
        for i in range(len(self.DBCD)):
            self.print_CD(i)
            print("============")
    def all_DVDs(self):
        for i in range(len(self.DBDVD)):
            self.print_DVD(i)
            print("============")
def testing():
    db=DoME()
    db.add_CD()
    db.add_CD()
    db.add_CD()
    db.add_DVD()
    db.add_DVD()
    db.add_DVD()
    print("________________________")
    print("All CDs")
    print("________________________")
    db.all_CDs()
    print("________________________")
    print("All DVDs")
    print("________________________")
    db.all_DVDs()

testing()