import pygame
from settings import Settings


class Ball:
    """Class for the pong ball"""

    def __init__(self, pong_game):
        """Initialize the ball and define its initial position"""
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = Settings()
        self.velocity = [self.settings.ball_initial_speed,
                         self.settings.ball_initial_speed]

        # Ball configuration
        self.radius = self.settings.ball_size
        self.color = self.settings.ball_color

        # creation of ball surface
        self.image = pygame.Surface((self.radius * 2, self.radius * 2),
                                    pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius),
                           self.radius)
        self.rect = self.image.get_rect()
        # Initial position
        self.rect.center = self.screen_rect.center

        # Moving flag
        self.moving = False

    def blitme(self):
        """Draw ball to its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving:
            # Initial ball direction
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]
            # Inverse horizontal direction
            if self.rect.left < self.settings.play_area_positionx or \
            self.rect.right > self.settings.play_area_width +\
            self.settings.play_area_positionx:
                self.velocity[0] = -self.velocity[0]
            # Inverse vertical direction
            if self.rect.top < self.settings.play_area_positiony or self.rect.bottom > self.settings.play_area_height + self.settings.play_area_positiony:
                self.velocity[1] = -self.velocity[1]
            
        
            

