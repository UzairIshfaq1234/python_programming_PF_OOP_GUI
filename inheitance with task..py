class item:
    def __init__(self,title,playingtime):
        self.title=title
        self.playingtime=playingtime
        self.gotit=False
        self.comment=""

    def set_comment(self,comment):
        self.comment=comment
    def get_comment(self):
        return self.comment

    def set_own(self,goit):
        self.gotit=gotit
    def get_own(self):
        return self.gotit

    def printDVD(self):
        print("TITLE: ",self.title)
        print("PLAYING TIME: ",self.playingtime)
        print("OWN STATUS: ",self.gotit)
        print("COMMENTS: ",self.commenT)