class Room:
    def __init__ (self, input_room_name, input_space,):

        self.room_name = input_room_name
        self.space = input_space
        self.guest = []
        self.song_list = []


    def number_of_guest_in_room(self):
        return len(self.guest)

    def add_guest(self, guest):
        self.guest.append(guest)
