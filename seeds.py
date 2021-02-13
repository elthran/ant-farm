import pygame

from models.ants import Worker
from models.colonies import Colony
from models.foods import Leaf
from models.game import Game
from models.maps import Map

game = Game()
game.map = Map(game=game)

for i in range(20):
    leaf = Leaf()
    game.map.add_sprite(leaf)

game.map.colonies = [Colony(map=game.map, name="Colony1", ant_colour="black"),
                     Colony(map=game.map, name="Colony2", ant_colour="red")]

for colony in game.map.colonies:
    colony.birth_ant(ant_class=Worker)

