
class Song:

    songNum = 0

    def __init__(self, name=None, artist=None, length=None, sid=None):
        self.name = name
        self.artist = artist
        self.length = length
        self.sid = sid
        self.songNum = self.uniqueIdentifier()
        self.votes = 1


    def getLength(self):
        return self.length

    def getSongName(self):
        return self.name

    def getArtist(self):
        return self.artist

    def getsid(self):
        return self.sid

    def formatPrint(self):
        print(f'Song: {self.name}')
        print(f'Artist: {self.artist}')
        print(f'Song length: {self.length}')
        print(f'Song ID: {self.sid} ')
        print(f'Song number: {self.songNum}')
        print(f'Number votes {self.votes}\n')

    @staticmethod
    def uniqueIdentifier():
        var = Song.songNum
        Song.songNum += 1
        return var




