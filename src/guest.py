class Guest:
    def __init__(self, input_name, input_wallet, input_favorite_song):
        self.name = input_name
        self.wallet = input_wallet
        self.favorite_song = input_favorite_song


    def pay(self, input_song):
        self.wallet -= input_song.price