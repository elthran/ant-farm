import pygame
import sys

from models.constants import Graphics
from models.users import User


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Graphics.SCREEN_WIDTH, Graphics.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.bg_color = pygame.Color("white")
        self.all_sprites = pygame.sprite.Group()
        self.map = None
        self.user = User()

        self.display_screen_surface = None
        self.display_screen = pygame.font.SysFont('Comic Sans MS', 45)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.user.keyboard_mapping.key_change(event.key, "pressed")
            elif event.type == pygame.KEYUP:
                self.user.keyboard_mapping.key_change(event.key, "released")

    def update(self):
        self.all_sprites.update()
        pygame.display.update()
        self.clock.tick(120)

        self.map.update()

        self.display_screen_surface = self.display_screen.render(f"{self.map.colonies[0].name}"
                                                                 f"Ants: {len(self.map.colonies[0].ants)}"
                                                                 "                                  "
                                                                 f"{self.map.colonies[1].name}"
                                                                 f"Ants: {len(self.map.colonies[1].ants)}",
                                                                 False, (0, 0, 0))

    def draw(self):
        self.screen.fill(self.bg_color)
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.display_screen_surface, (0, 0))
