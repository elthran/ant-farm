import math

from models.constants import GameConstants


class Map:
    def __init__(self, game):
        self.game = game
        self.name = "world_1"
        self.height = GameConstants.SCREEN_HEIGHT
        self.width = GameConstants.SCREEN_WIDTH
        self.sprites = []

    def add_sprite(self, sprite):
        self.sprites.append(sprite)
        self.game.all_sprites.add(sprite)

    def remove_sprite(self, sprite):
        self.sprites.remove(sprite)
        self.game.all_sprites.remove(sprite)

    def get_object_at_coordinates(self, x, y):
        for object in self.sprites:
            if object.x_pos == x and object.y_pos == y:
                return object
        return None

    @staticmethod
    def get_distance_between_objects(one, two):
        return math.hypot(one.x_pos - two.x_pos, one.y_pos - two.y_pos)

