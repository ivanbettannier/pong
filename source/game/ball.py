import os, sys
parent_dir = os.path.abspath('..')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import pygame
from game.settings import Settings
import math
import random 
from game.bonus import Portal
from game.object import Object

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

    def change_color(self):
        """Change the color of the ball"""
        #self.image.fill(new_color)  # Effacer l'ancienne couleur
        random_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        pygame.draw.circle(self.image, random_color, (self.radius, self.radius), self.radius)
        self.blitme()

class Ball_bonus(Ball):

    def __init__(self, pong_game):
        """Initialize the ball and define its initial position"""
        super().__init__(pong_game)
        self.color = [self.settings.ball_color[0] - 60, self.settings.ball_color[1] - 30, self.settings.ball_color[2] + 50]
        self.rect.x = self.screen_rect.center[0] + random.uniform(-90, 90)
        self.rect.y = self.screen_rect.center[1] + random.uniform(-90, 90)
        #self.speed = random.randint(6, 7)
        self.velocity[0] = random.choice([-1,1])*(self.velocity[0]) + random.randint(6, 7)
        self.velocity[1] = random.choice([-1,1])*(self.velocity[1]) + random.randint(6, 7)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius),
                           self.radius)
        

    def update(self):
        
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
