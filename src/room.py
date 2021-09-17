class Room:
    def __init__ (self, input_room_name, input_space,):

        self.room_name = input_room_name
        self.space = input_space
        self.guest = []
        self.song_list = []
        self.fee = 10


    def number_of_guest_in_room(self):
        return len(self.guest)

    def add_guest(self, guest):
        self.guest.append(guest)

    def number_of_song_in_room(self):
        return len(self.song_list)

    def add_song(self, song):
        self.song_list.append(song)

    def remove_guest(self, guest):
        self.guest.remove(guest)

    