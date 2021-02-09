import math
import random

import pygame

from models.constants import GameConstants


class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = None
        self._x_pos = random.randint(200, GameConstants.SCREEN_WIDTH - 200)
        self._y_pos = random.randint(200, GameConstants.SCREEN_HEIGHT - 200)
        self._direction = 0  # Direction of travel in degrees
        self.max_speed = 0  # In pixels per frame
        self.speed = 0
        self.vision = 0  # Pixels away it can detect things
        self.destination_coordinates = None  # Where sprite is trying to move to (if set, will overwrite direction)

    def initialize(self):
        self.rect = self.original_image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        if direction >= 360:
            direction -= 360
        elif direction < 0:
            direction += 360
        self._direction = direction

    @property
    def x_pos(self):
        return self._x_pos

    @x_pos.setter
    def x_pos(self, x_pos):
        if x_pos > GameConstants.SCREEN_WIDTH:
            x_pos = GameConstants.SCREEN_WIDTH
        elif x_pos < 0:
            x_pos = 0
        self._x_pos = x_pos

    @property
    def y_pos(self):
        return self._y_pos

    @y_pos.setter
    def y_pos(self, y_pos):
        if y_pos > GameConstants.SCREEN_HEIGHT:
            y_pos = GameConstants.SCREEN_HEIGHT
        elif y_pos < 0:
            y_pos = 0
        self._y_pos = y_pos

    def update(self):
        if self.speed != 0:
            self.x_pos += self.speed * math.cos(self.direction * math.pi / 180)
            self.y_pos += self.speed * math.sin(-self.direction * math.pi / 180)
            pygame.transform.rotate(self.image, self.direction)
            self.rect.center = (self.x_pos, self.y_pos)

    def reset(self):
        pass
