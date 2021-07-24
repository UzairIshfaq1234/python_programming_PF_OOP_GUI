class item:
    def __init__(self,title,artist,playingTime,tracks):
        self.title=title
        self.artist=artist
        self.playingTime=playingTime
        self.tracks=tracks
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
    def printCD(self):
        print("Title: ",self.title)
        print("Artist: ",self.artist)
        print("Playing Time:",self.playingTime)
        print("Number of tracks: ",self.tracks)
        print("Available: ",self.get_own())
        print("Comments: ",self.get_comment())