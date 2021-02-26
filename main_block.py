from constants import *
import pygame

class Main_block(pygame.sprite.Sprite):

    """
        # TODO:

    """
    def __init__(self, x, y):
        super().__init__()
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE

        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill((255, 0, 0))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (x, y)
        self.speed = 1


    def update(self):
        self.rect.left += self.speed
