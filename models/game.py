import pygame
import sys

from models.constants import GameConstants
from models.foods import Leaf
from models.maps import Map
from models.players import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.bg_color = pygame.Color("white")
        self.all_sprites = pygame.sprite.Group()

        self.player = Player(game=self)

        self.map = Map(game=self)

        for i in range(10):
            leaf = Leaf()
            self.map.add_sprite(leaf)

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player.key_press("a")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.all_sprites.update()
        pygame.display.update()
        self.clock.tick(120)

        for ant in self.player.colony.ants:
            minimum_distance = 50000
            target_leaf = None
            for object in self.map.sprites:
                if object.__class__.__name__ != "Leaf":
                    continue
                distance = self.map.get_distance_between_objects(ant, object)
                if distance < minimum_distance:
                    minimum_distance = distance
                    target_leaf = object
            if minimum_distance <= ant.vision:
                ant.destination_coordinates = (target_leaf.x_pos, target_leaf.y_pos)
                if minimum_distance <= 10:
                    self.map.remove_sprite(target_leaf)
            else:
                ant.destination_coordinates = None

    def draw(self):
        self.screen.fill(self.bg_color)
        self.all_sprites.draw(self.screen)
