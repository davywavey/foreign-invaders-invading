import pygame
from pygame.sprite import Sprite
from setting import Setting

class Alien(Sprite):
    """定义外星人舰队的class"""
    def __init__(self, ai_game):
        super().__init__()
        self.image = pygame.image.load("image/alien.bmp")
        self.screen = ai_game.screen
        self.rect = self.image.get_rect()
        self.settings = Setting()

        self.rect_x = self.rect.width
        self.rect_y = self.rect.height

        self.x = float(self.rect_x)

    def update(self):
        self.x+=self.settings.alien_speed
        self.rect_x = self.x