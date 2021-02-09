import pygame

from models.sprites import Sprite


class Food(Sprite):
    def __init__(self):
        super().__init__()


class Leaf(Food):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("assets/leaf.png").convert_alpha()
        self.image = self.original_image
        self.initialize()

