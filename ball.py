import pygame
from settings import Settings
import math
import random 


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

        self.portal = pong_game.portal

    def blitme(self):
        """Draw ball to its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving:
            # Initial ball direction
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]
            # Vérifie si la balle touche le portail
            if self.portal.rect.colliderect(self.rect):
                self.portal.handle_collision(self)  

            # Inverse horizontal direction
            if self.rect.left < self.settings.play_area_positionx or \
            self.rect.right > self.settings.play_area_width +\
            self.settings.play_area_positionx:
                self.velocity[0] = -self.velocity[0]
            # Inverse vertical direction
            if self.rect.top < self.settings.play_area_positiony or self.rect.bottom > self.settings.play_area_height + self.settings.play_area_positiony:
                self.velocity[1] = -self.velocity[1]
            
        
    def teleport(self):
        """Téléporte la balle vers une direction aléatoire"""
        # Réinitialise la position de la balle
        self.rect.center = self.portal.rect.center

        # Choix aléatoire d'un angle entre 0 et 360 degrés
        random_angle = math.radians(random.uniform(0, 360))

        # Définition de la nouvelle direction de la balle
        self.velocity[0] = self.settings.ball_initial_speed * math.cos(random_angle)
        self.velocity[1] = self.settings.ball_initial_speed * math.sin(random_angle)

    def change_color(self, new_color):
        """Change the color of the ball"""
        self.image.fill((0, 0, 0, 0))  # Effacer l'ancienne couleur
        pygame.draw.circle(self.image, new_color, (self.radius, self.radius), self.radius)
            

