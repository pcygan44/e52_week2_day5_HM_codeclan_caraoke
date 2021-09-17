import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Song1", 4.00)
        self.song_2 = Song("Song2", 7.00) 
        self.room_1 = Room("Room1", 1)
        self.guest_1 = Guest("Jim", 40, self.song_2.name)
        self.guest_2 = Guest("Tom", 35, self.song_1.name)


    def test_room_name(self):
        self.assertEqual("Room1",self.room_1.room_name)

    def test_add_guest_to_room(self,):
        self.room_1.add_guest(self.guest_1)
        self.assertEqual(1, self.room_1.number_of_guest_in_room())

    def test_add_song_to_room(self):
        self.room_1.add_song(self.song_2)
        self.assertEqual(1, self.room_1.number_of_song_in_room())

    def test_remove_guest_from_room(self):
        self.room_1.add_guest(self.guest_1)
        self.assertEqual(1, self.room_1.number_of_guest_in_room())
        self.room_1.remove_guest(self.guest_1)
        self.assertEqual(0,self.room_1.number_of_guest_in_room() )

    def test_guest_pay_entry_fee(self):
        self.room_1.check_entry_fee(self.guest_1)
        self.assertEqual(True, self.room_1.check_entry_fee(self.guest_1))
        self.guest_1.pay(self.room_1.fee)
        self.assertEqual(30, self.guest_1.wallet)

    def test_avalable_space_in_room(self):
        # self.room1.check_avalable_space_in_room(self.guest_2)
        self.assertEqual(True, self.room_1.check_avalable_space_in_room())

    def test_avalable_space_in_room(self):
        self.room_1.add_guest(self.guest_1)
        self.assertEqual(False, self.room_1.check_avalable_space_in_room())


