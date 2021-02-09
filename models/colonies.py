from models.ants import Worker


class Colony:
    def __init__(self, map):
        self.map = map
        self.ants = []
        for i in range(1):
            self.birth_ant()

    def birth_ant(self):
        new_ant = Worker()
        self.ants.append(new_ant)
        self.map.add_sprite(new_ant)
