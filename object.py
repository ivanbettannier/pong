import pygame
from settings import Settings
import math
import random


class Object:
    """Class for the pong ball"""

    def __init__(self, pong_game):
        """Initialize the ball and define its initial position"""
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = Settings()
    
    def blitme(self):
        """Draw feature"""
        
        self.screen.blit(self.image, self.rect)    