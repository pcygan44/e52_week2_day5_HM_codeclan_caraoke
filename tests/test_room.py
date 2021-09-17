import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Room1", 1)

    def test_room_name(self):
        self.assertEqual("Room1",self.room_1.room_name)
