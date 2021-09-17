import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Room1", 1)
        self.guest_1 = Guest("Jim", 40, "Song1")
        self.guest_2 = Guest("Tom", 35, "Song2")

    def test_room_name(self):
        self.assertEqual("Room1",self.room_1.room_name)

    def test_add_guest_to_room(self,):
        self.room_1.add_guest(self.guest_1)
        self.assertEqual(1, self.room_1.number_of_guest_in_room())
