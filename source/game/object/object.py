import os, sys
parent_dir = os.path.abspath('../..')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import pygame
from game.settings import Settings
import math
import random


class Object:
    """Class for the pong ball"""

    def __init__(self, pong_game):
        """Initialize the ball and define its initial position"""
        self.screen_rect = pong_game.screen.get_rect()
        self.screen = pong_game.screen
    def blitme(self):
        """Draw feature"""
        
        self.screen.blit(self.image, self.rect)    