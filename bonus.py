import pygame
from settings import Settings


class Bonus:
    """Class for the pong ball"""

    def __init__(self, pong_game, bonus_color='white', bonus_position=[0,0]):
        """Initialize the ball and define its initial position"""
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = Settings()



        # Bonus copus definitio
        self.size = self.settings.ball_size*10
        self.color = bonus_color

        # creation of ball surface
        self.image = pygame.Surface((self.size * 2, self.size * 2),
                                    pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.size, self.size),
                           self.size)
        self.rect = self.image.get_rect()

        # Initial position
        self.rect.center = bonus_position

    def blitme(self):
        """Draw bonus"""
        self.screen.blit(self.image, self.rect)


bonus_dict = {'change_ball_color': {'color' : (0, 140, 0),'type': 'change_color'}}