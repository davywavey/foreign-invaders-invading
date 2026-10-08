import pygame
from setting import Setting

class ship:
    """Manage the ship"""
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.setting

        #加载图像并且获得其外部的矩形
        self.image = pygame.image.load("image/ship.bmp").convert_alpha()
        original_width = self.image.get_width()
        original_height = self.image.get_height()
        target_width = 60
        scale_ratio = target_width / original_width
        target_height = int(original_height * scale_ratio)
        self.image = pygame.transform.smoothscale(
            self.image,
            (target_width, target_height)
            )
        self.rect = self.image.get_rect()

        #每搜飞船都放在屏幕的中下方
        self.rect.midbottom = self.screen_rect.midbottom

        #让飞船的速度变成浮点数
        self.x=float(self.rect.x)


        self.keep_move_right = False
        self.keep_move_left = False
    
    def update(self):
        if self.keep_move_right and self.rect.right<self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.keep_move_left and self.rect.left>0:
            self.x -= self.settings.ship_speed

        self.rect.x=self.x
        

        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
