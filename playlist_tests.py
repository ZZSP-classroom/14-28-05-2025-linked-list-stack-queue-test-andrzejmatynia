import unittest
from playlist_manager import SongInfo, LinkedList

class TestPlaylistManager(unittest.TestCase):
    def setUp(self):
        self.playlist = LinkedList()

    def test_add_song(self):
        self.playlist.add_song("song1", "artist1")
        self.playlist.add_song("song2", "artist2")
        self.assertEqual(self.playlist.get_next_song(), "song2")

    def test_remove_song(self):
        self.playlist.add_song("song1", "artist1")
        self.playlist.add_song("song2", "artist2")
        self.playlist.remove_song()
        self.assertEqual(self.playlist.get_next_song(), "song1")

if __name__ == "__main__":
    unittest.main()