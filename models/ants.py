import math
import random

import pygame

from models.sprites import Sprite


class Ant(Sprite):
    def __init__(self, colony=None, colour=None):
        super().__init__()
        self.original_image = None
        self._direction = random.randint(0, 360)
        self.colony = colony
        self.max_speed = 0.5
        self.speed = 0.5
        self.vision = 300

        self.hunger = 0

    def move(self):
        if self.destination_coordinates:
            if self.x_pos == self.destination_coordinates[0] and self.y_pos == self.destination_coordinates[1]:
                self.speed = 0
            else:
                self.direction = math.degrees(math.atan2(self.y_pos - self.destination_coordinates[1],
                                                         self.destination_coordinates[0] - self.x_pos))
        else:
            self.direction += random.randint(-3, 3)
        self.image = pygame.transform.rotate(self.original_image, int(self.direction) + 270)
        self.hunger += 1

    def collide(self, object):
        if object.__class__.__name__ == "Leaf":
            self.hunger = 0
            self.colony.birth_ant()
        elif object.__class__.__name__ == "Worker":
            self.speed = 0


class Worker(Ant):
    def __init__(self, *args, colour=None, **kwargs):
        super().__init__(*args, colour=None, **kwargs)
        self.original_image = pygame.image.load(f"assets/{colour}-ant.png").convert_alpha()
        self.image = self.original_image
        self.initialize()

    def update(self):
        self.move()
        super(Worker, self).update()
