from models.ants import Worker


class Colony:
    def __init__(self, map, name, ant_colour):
        self.map = map
        self.name = name
        self.ant_colour = ant_colour
        self.ants = []

    def birth_ant(self, ant_class=Worker):
        new_ant = ant_class(colony=self, colour=self.ant_colour)
        self.ants.append(new_ant)
        self.map.add_sprite(new_ant)
