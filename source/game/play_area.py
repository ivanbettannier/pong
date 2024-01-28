import os, sys
parent_dir = os.path.abspath('..')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import pygame
from game.settings import Settings
from game.object.object import Object

class Play_area():
    """Class for the playing area"""

    def __init__(self, pong_game):
        """Initialize the ball and define its initial position"""
        self.settings = pong_game.settings
        self.screen = pong_game.screen

        # Play area size
        self.play_area = pygame.Surface(
            (self.settings.play_area_width, 
             self.settings.play_area_height))
        self.play_area.fill(self.settings.play_area_color)

        # Create the outline area
        pygame.draw.rect(self.play_area, self.settings.play_area_border_color, self.play_area.get_rect(), self.settings.play_area_border_larger)

    def blitme(self):
        """Draw playing area"""
        self.screen.blit(self.play_area, (self.settings.play_area_positionx, self.settings.play_area_positiony))