import math

from models.colonies import Colony
from models.constants import Graphics


class Map:
    def __init__(self, game):
        self.game = game
        self.name = "world_1"
        self.height = Graphics.SCREEN_HEIGHT
        self.width = Graphics.SCREEN_WIDTH
        self.sprites = []
        self.colony = Colony(map=self)

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

    def get_nearest_object_by_type(self, object, type):
        smallest_distance = None
        nearest_object = None
        objects_to_check = [object for object in self.sprites if object.__class__.__name__ == type]
        for each in objects_to_check:
            distance = self.get_distance_between_objects(object, each)
            if not smallest_distance or distance < smallest_distance:
                smallest_distance = distance
                nearest_object = each
        return nearest_object

    @staticmethod
    def get_distance_between_objects(one, two):
        try:
            return math.hypot(one.x_pos - two.x_pos, one.y_pos - two.y_pos)
        except AttributeError as e:
            print(f"Error calculating distance between two objects. {e}. Objects are {one} and {two}.")

