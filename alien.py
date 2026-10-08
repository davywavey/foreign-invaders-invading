import pygame
from pygame.sprite import Sprite
from setting import Setting
from pathlib import Path

class Alien(Sprite):
    """定义外星人舰队的class"""
    def __init__(self, ai_game):
        super().__init__()
        image_path = Path(__file__).resolve().parent / "image" / "alien.bmp"
        self.image = pygame.image.load(str(image_path))
        self.screen = ai_game.screen
        self.rect = self.image.get_rect()
        self.settings = ai_game.setting

        self.rect_x = self.rect.width
        self.rect_y = self.rect.height

        self.x = float(self.rect_x)

    def update(self):
        self.x+=self.settings.alien_speed*self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right>screen_rect.right) or (self.rect.left<0)