from models.ants import Worker


class Colony:
    def __init__(self, game):
        self.game = game
        self.ants = []
        for i in range(3):
            self.birth_ant()

    def birth_ant(self):
        new_ant = Worker()
        self.ants.append(new_ant)
        self.game.all_sprites.add(new_ant)
