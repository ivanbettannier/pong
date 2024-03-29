import os, sys
parent_dir = os.path.abspath('../..')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import pygame
from  game.object.object import Object 

class Controler(Object):
    """Class for the pong ball"""

    def __init__(self, pong_game):
        """Initialize the ball and define its initial position"""
        super().__init__(pong_game)
        self.game_settings = pong_game.settings
        # controler configuration
        self.width = self.game_settings.controler_width
        self.height = self.game_settings.controler_height
        self.color = self.game_settings.ball_color
        self.speed = self.game_settings.controler_speed

 
        # creation of controler surface
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, self.color, (0, 0, self.width, self.height))
        
        self.rect = self.image.get_rect()
       
        self.rect = self.image.get_rect()

        # Moving flag
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update ball position with moving flag"""
        if self.moving_up:
            if self.rect.y > self.game_settings.play_area_positiony + self.game_settings.play_area_border_larger:
                self.rect.y -= self.speed
        if self.moving_down:
            if self.rect.y < self.game_settings.screen_height -  self.game_settings.play_area_positiony - self.height - self.game_settings.play_area_border_larger:
                self.rect.y += self.speed
    
        
   