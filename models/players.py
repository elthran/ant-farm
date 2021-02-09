from models.colonies import Colony


class Player:
    def __init__(self, game):
        self.game = game
        self.colony = Colony(game=game)

    def key_press(self, key):
        print(f"You have pressed the {key} key.")


