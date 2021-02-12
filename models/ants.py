import math
import random

import pygame

from models.sprites import Sprite


class Ant(Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = None
        self._direction = random.randint(0, 360)
        self.max_speed = 0.5
        self.speed = 0.5
        self.vision = 300

        # Experimenting with collisions
        self.id = random.randint(1, 1000)

        self.hunger = 0

    def move(self):
        if self.destination_coordinates:
            if self.x_pos == self.destination_coordinates[0] and self.y_pos == self.destination_coordinates[1]:
                self.speed = 0
            else:
                self.direction = math.degrees(math.atan2(self.y_pos - self.destination_coordinates[1], self.destination_coordinates[0] - self.x_pos))
        else:
            self.direction += random.randint(-1, 1)
        self.image = pygame.transform.rotate(self.original_image, int(self.direction)+270)
        self.hunger += 1

    def collide(self, object):
        if object.__class__.__name__ == "Leaf":
            self.hunger = 0
        elif object.__class__.__name__ == "Worker":
            self.speed = 0



# class Queen(Ant):
#     def __init__(self):
#         super().__init__()
#         self.original_image = pygame.image.load("assets/queen-ant.png").convert_alpha()
#
#     def update(self):
#         self.move()
#         super(Queen, self).update()


class Worker(Ant):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("assets/black-ant.png").convert_alpha()
        self.image = self.original_image
        self.initialize()

    def update(self):
        self.move()
        super(Worker, self).update()


# class Soldier(Ant):
#     def __init__(self):
#         self.original_image = pygame.image.load("assets/black-ant.png").convert_alpha()
#         super().__init__()
#
#     def update(self):
#         self.move()
#         super(Soldier, self).update()


# class Drone(Ant):
#     """Has wings. Purpose is mating."""
#     def __init__(self):
#         self.original_image = pygame.image.load("assets/black-ant.png").convert_alpha()
#         super().__init__()
#
#     def update(self):
#         self.move()
#         super(Drone, self).update()
