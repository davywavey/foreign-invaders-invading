import pygame

class GameStats:

    def __init__(self,ai_game):
        self.settings = ai_game.setting
        self.reset_status()

    def reset_status(self):
        self.ship_left = self.settings.ship_limit