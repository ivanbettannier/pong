import pygame
from settings import Settings
import math
import random 
from bonus import Portal
from object import Object

class Ball(Object):
    """Class for the pong ball"""

    def __init__(self, pong_game):
        """Initialize the ball and define its initial position"""
        super().__init__(pong_game)
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

        self.portal = Portal(self)

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

    def change_color(self):
        """Change the color of the ball"""
        #self.image.fill(new_color)  # Effacer l'ancienne couleur
        random_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        pygame.draw.circle(self.image, random_color, (self.radius, self.radius), self.radius)
        self.blitme()
        
        
            

