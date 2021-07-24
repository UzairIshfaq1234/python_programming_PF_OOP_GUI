class Videos:
    def __init__(self,title,director,playingTime):
        self.title=title
        self.director=director
        self.playingTime=playingTime
        self.got_it=False
        self.comment=""
    def set_comment(self,comment):
        self.comment=comment
    def get_comment(self):
        return self.comment
    def set_own(self,got_it):
        self.got_it=got_it
    def get_own(self):
        return self.got_it
    def printDVD(self):
        print("Title: ",self.title)
        print("Director: ",self.director)
        print("Playing Time:",self.playingTime)
        print("Available: ",self.get_own())
        print("Comments: ",self.get_comment())