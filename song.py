class song:

    def __init__(self, title, artist, album, tracknumber, year):
        self.title = title
        self.artist = artist
        self.album = album
        self.tracknumber = tracknumber
        self.year = year

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getArtist(self):
        return self.artist

    def setArtist(self, artist):
        self.artist = artist

    def getAlbum(self):
        return self.album

    def setAlbum(self, album):
        self.title = album

    def getTrackNumber(self):
        return self.tracknumber

    def setTrackNumber(self, tracknumber):
        self.tracknumber = tracknumber

    def getYear(self):
        return self.year

    def setYear(self, year):
        self.year = year
