class CD:
    def __init__(self):
        self.collect=[ ]
    def add(self,artist=input("ENTER ARTIST NAME: "),song=input("SONG NAME: "),playingtime=int(input("ENTER PLAYING TIME: ")),tracks=int(input("ENTER TRACKS: "))):
        self.artist=artist
        self.song=song
        self.playingtime=playingtime
        self.tracks=tracks
        return artist
        return song
        return playingtime
        return tracks
        addo="ARTIST NAME",self.artist,"SONG:",self.song,"PLAYING TIME",self.playingtime,"TRACKS:",self.playingtime
        self.collect.append(addo)


def main():
    CD1=CD()
    CD2=CD()
    CD1.add()
    CD2.add()

   

    print(CD1.collect[0])
    print(CD2.collect[0])

main()