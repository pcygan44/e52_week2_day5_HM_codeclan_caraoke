import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Song1", 4.00)
        self.song_2 = Song("Song2", 7.00) 

    def test_song_name(self):
        self.assertEqual("Song1",self.song_1.name)

    def test_song_price(self):
        self.assertEqual(7.00, self.song_2.price)