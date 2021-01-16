import main
from Song import Song


class DJ:

    def __init__(self, queue=None):
        self.queue = []

    def __addSong(self, song=None):
        if isinstance(song, Song):
            self.queue.append(song)
            print('this is exe with')
        else:
            pass

    def playSong(self):
        song = self.queue.pop(0)
        song.formatPrint()
        pass
        # sends message to spotify API to play song

    def getNextSong(self):
        return self.queue.pop(0)

    # checks to see if song ID already exists in queue
    def addSong(self, thisSong):
        for song in self.queue:
            if thisSong.sid == song.sid:
                song.votes += 1
                self.sortQueue()
                del thisSong
                return True
        self.__addSong(thisSong)
        return

    def sortQueue(self):
        print('sorted')
        pass

    def printPlaylist(self):
        for song in self.queue:
            song.formatPrint()
