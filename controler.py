import pygame
from settings import Settings

class Controler:
    """Class for the pong ball"""

    def __init__(self, pong_game):
        """Initialize the ball and define its initial position"""
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = Settings()
        
        # controler configuration
        self.width = self.settings.controler_width
        self.height = self.settings.controler_height
        self.color = self.settings.ball_color
        self.speed = self.settings.controler_speed

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
            if self.rect.y > self.settings.play_area_positiony + self.settings.play_area_border_larger:
                self.rect.y -= self.speed
        if self.moving_down:
            if self.rect.y < self.settings.screen_height -  self.settings.play_area_positiony - self.height - self.settings.play_area_border_larger:
                self.rect.y += self.speed
    
    def blitme(self):
        """Draw ball to its current location"""
        self.screen.blit(self.image, self.rect)
        
   