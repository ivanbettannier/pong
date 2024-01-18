import pygame
from settings import Settings
from object import Object

class Play_area(Object):
    """Class for the playing area"""

    def __init__(self, pong_game):
        """Initialize the ball and define its initial position"""
        super().__init__(pong_game)

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