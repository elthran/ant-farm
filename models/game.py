from random import randint

import pygame
import sys

from models.constants import GameConstants
from models.maps import Map
from models.foods import Leaf


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.bg_color = pygame.Color("white")
        self.all_sprites = pygame.sprite.Group()

        self.map = Map(game=self)

        for i in range(10):
            leaf = Leaf()
            self.map.add_sprite(leaf)

    @staticmethod
    def handle_events():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            print(f"You have pressed the 'a' key.")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.all_sprites.update()
        pygame.display.update()
        self.clock.tick(120)

        for ant in self.map.colony.ants:
            nearest_leaf = self.map.get_nearest_object_by_type(ant, "Leaf")
            distance_to_nearest_leaf = self.map.get_distance_between_objects(ant, nearest_leaf)
            if distance_to_nearest_leaf <= 10:  # The ant is close enough to simply eat the leaf
                self.map.remove_sprite(nearest_leaf)
                ant.hunger = 0
            elif distance_to_nearest_leaf <= ant.vision:  # The ant is close enough to see the leaf
                ant.destination_coordinates = (nearest_leaf.x_pos, nearest_leaf.y_pos)
            else:  # The ant can't see any leaf. It has no specific destination
                ant.destination_coordinates = None

            if randint(0, 100) == 100:
                print(f"Ant is at {ant.hunger} hunger.")

    def draw(self):
        self.screen.fill(self.bg_color)
        self.all_sprites.draw(self.screen)
