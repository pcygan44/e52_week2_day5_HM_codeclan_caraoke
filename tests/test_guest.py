import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Jim", 40, "Song1")
        self.guest_2 = Guest("Tom", 35, "Song2")

    def test_guest_name(self):
        self.assertEqual("Jim",self.guest_1.name)

    def test_guest_wallet(self):
        self.assertEqual(35, self.guest_2.wallet)
    
