import pygame
from settings import *


class Level:
    def __init__(self) -> None:
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            print(row_index, row)

    def run(self):
        # update and draw the game
        pass
