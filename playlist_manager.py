class SongInfo:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_song(self, title, artist):
        new_song = SongInfo(title, artist)
        new_song.next = self.head
        self.head = new_song

    def remove_song(self):
        if self.head:
            self.head = self.head.next

    def get_next_song(self):
        return self.head.title if self.head else None

playlist = LinkedList()
playlist.add_song("song1", "artist1")
print(playlist.get_next_song())
playlist.remove_song()
print(playlist.get_next_song())