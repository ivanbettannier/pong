import os, sys
parent_dir = os.path.abspath('../..')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import pygame
from game.settings import Settings
import random
from game.object.object import Object



class Feature(Object):
    """Class for the pong ball"""

    def __init__(self, pong_game, feature_color='Black', feature_position=[0,0]):
        """Initialize the ball and define its initial position"""
        super().__init__(pong_game)
        self.limit_appearence_time = [100,200]
        self.appearence_time = random.randint(self.limit_appearence_time[0], self.limit_appearence_time[1])

        # feature copus definitio
        self.color = feature_color
   
    def random_position(self,limit_x, limit_y):
        return [random.randint(limit_x[0], limit_x[1]), random.randint(limit_y[0], limit_y[1])]

    def reinit(self):
        self.appearence = 0
        self.rect.centerx = 0
        self.rect.centery = 0
        self.appearence_time = random.randint(self.limit_appearence_time[0], self.limit_appearence_time[1])
   
        
    def apperence(self, ball_moving):
        if ball_moving == True:
            self.appearence += 1
        if self.appearence >= self.appearence_time:
            if self.appearence == self.appearence_time:
                self.position = self.random_position(self.limit_x, self.limit_y)
            self.rect.centerx = self.position[0]
            self.rect.centery = self.position[1]
            self.color = random.choice(['Yellow', 'Pink', 'White'])
            self.blitme()
            
    
 
   



class Bonus(Feature):
       
    def __init__(self, pong_game, limit_bonus_appearence_time, feature_color='Yellow', feature_position=[0, 0]):
        """Initialise le feature spécial en appelant le constructeur de la classe mère"""
        super().__init__(pong_game, feature_color, feature_position)
        self.limit_appearence_time = limit_bonus_appearence_time
        self.appearence = 0
        self.position = feature_position
        self.size = self.settings.ball_size*3
        self.limit_x = [self.settings.play_area_positionx+int(self.settings.play_area_width*(1/6)), self.settings.play_area_positionx+int(self.settings.play_area_width*(5/6))]
        self.limit_y = [self.settings.play_area_positiony+self.size, self.settings.play_area_positiony+self.settings.play_area_height-self.size]
        self.color = random.choice(['Yellow', 'White', 'Brown', 'Midnightblue'])
        self.multi_ball = False
        self.bonus_inver_controler = False
        self.bonus_controler_position = False
        # creation of ball surface
        self.image = pygame.Surface((self.size * 2, self.size * 2),
                                    pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.size, self.size),
                           self.size)
        self.rect = self.image.get_rect()

    def apperence(self, ball_moving):
        if ball_moving == True:
            self.appearence += 1
        if self.appearence >= self.appearence_time:
            if self.appearence == self.appearence_time:
                self.position = self.random_position(self.limit_x, self.limit_y)
                self.color = random.choice(['Yellow', 'White', 'Brown', 'Midnightblue'])
                pygame.draw.circle(self.image, self.color, (self.size, self.size),
                             self.size)
            self.rect.centerx = self.position[0]
            self.rect.centery = self.position[1]
            self.blitme()

    def bonus_triggering(self, ball, controler1, controler2):
        """Colision detection beetween the ball and the bonus"""
        if self.rect.colliderect(ball):
            #if self.color == 'Yellow':
            #    ball.change_color()
            #    ball.velocity[0] += 3
            #    ball.velocity[1] += 3
            if self.color == 'White':
                self.multi_ball = True
            if self.color == 'Yellow':
                self.bonus_inver_controler = True
            if self.color == 'Brown':
                self.controler_position = True
                self.controler_change_position(controler1, controler2)
            if self.color == 'Midnightblue':
                self.controler_size = True
                self.controler_change_size(ball, controler1, controler2)
            self.reinit()

    def controler_change_position(self, controler1, controler2):
        if self.controler_position == True:
            controler1.rect.x = self.settings.play_area_positionx + self.settings.play_area_border_larger + self.settings.play_area_width*(1/6)
            controler2.rect.right = self.screen.get_rect().right - self.settings.play_area_positionx - (self.settings.play_area_border_larger + self.settings.play_area_width*(1/6))
        if self.controler_position == False:
            controler1.rect.x = self.settings.play_area_positionx + self.settings.play_area_border_larger + 5
            controler2.rect.right = self.screen.get_rect().right - self.settings.play_area_positionx - (self.settings.play_area_border_larger + 5)

    def controler_change_size(self, ball, controler1, controler2):
        if self.controler_size == True:
            if ball.velocity[0] <= 0:
                controler1.height = self.settings.controler_height/2
                controler1.image = pygame.Surface((controler1.width, controler1.height), pygame.SRCALPHA)
                pygame.draw.rect(controler1.image, controler1.color, (0, 0, controler1.width, controler1.height))
                #self.rect = self.image.get_rect()
            if ball.velocity[0] >= 0:
                controler2.height = self.settings.controler_height/2
                controler2.image = pygame.Surface((controler2.width, controler2.height), pygame.SRCALPHA)
                pygame.draw.rect(controler2.image, controler2.color, (0, 0, controler2.width, controler2.height))
        if self.controler_size == False:
            controler1.height = self.settings.controler_height
            controler1.image = pygame.Surface((controler1.width, controler1.height), pygame.SRCALPHA)
            pygame.draw.rect(controler1.image, controler1.color, (0, 0, controler1.width, controler1.height))
            controler2.height = self.settings.controler_height
            controler2.image = pygame.Surface((controler2.width, controler2.height), pygame.SRCALPHA)
            pygame.draw.rect(controler2.image, controler2.color, (0, 0, controler2.width, controler2.height))
    
                
    
    #def bonus_multi_ball(self, ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9, ball10):
        #for i in range(20):
        #    ball_name = f'ball{i}'
       #     ball_name.blitme()
       #     ball_name.update()

        

    

class Portal(Feature):
       
    def __init__(self, pong_game, limit_portal_appearence_time, feature_color='Yellow', feature_position=[0, 0]):
        """Initialise le feature spécial en appelant le constructeur de la classe mère"""
        super().__init__(pong_game, feature_color, feature_position)
        self.limit_appearence_time = limit_portal_appearence_time
        self.height = int(self.settings.play_area_height / 7)
        self.limit_x = [self.settings.play_area_positionx+int(self.settings.play_area_width*(7/16)), self.settings.play_area_positionx+int(self.settings.play_area_width*(9/16))]
        self.limit_y = [self.settings.play_area_positiony+self.height, self.settings.play_area_positiony+self.settings.play_area_height-self.height]
        self.appearence = 0
        self.width = 5
        # Couleur du portail
        self.color = (255, 0, 0)  # Rouge pour le portail
        # Coordonnées aléatoires du portail
        self.image = pygame.Surface((self.width, self.height),
                                    pygame.SRCALPHA)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        pygame.draw.rect(self.image, self.color, self.rect)
        # Initial position
        #self.rect.center = portal_position

    def portal_triggering(self, ball):
        """Gère la collision entre la balle et le portail"""            
        while self.rect.colliderect(ball.rect):    
            ball.rect.y = random.randint(self.settings.play_area_positiony+self.height, self.settings.play_area_positiony+self.settings.play_area_height-self.height)

class Portal_horizon(Portal):
       
    def __init__(self, pong_game, limit_portal_appearence_time, feature_color='Yellow', feature_position=[0, 0]):
        """Initialise le feature spécial en appelant le constructeur de la classe mère"""
        super().__init__(pong_game, feature_color, feature_position)
        self.limit_appearence_time = limit_portal_appearence_time
        self.height = 5
        self.limit_x = [self.settings.play_area_positionx+int(self.settings.play_area_width*(7/16)), self.settings.play_area_positionx+int(self.settings.play_area_width*(9/16))]
        self.limit_y = [self.settings.play_area_positiony+self.height, self.settings.play_area_positiony+self.height]
        self.appearence = 0
        self.width = int(self.settings.play_area_width / 7)
        # Couleur du portail
        self.color = (255, 0, 0)  # Rouge pour le portail
        # Coordonnées aléatoires du portail
        self.image = pygame.Surface((self.width, self.height),
                                    pygame.SRCALPHA)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        pygame.draw.rect(self.image, self.color, self.rect)
        # Initial position
        #self.rect.center = portal_position

    def portal_triggering(self, ball):
        """Gère la collision entre la balle et le portail"""            
        while self.rect.colliderect(ball.rect):    
            ball.rect.y = self.settings.play_area_positiony + self.settings.play_area_height - 10

        
    

        



#feature_dict = {'change_ball_color': {'color' : (0, 140, 0),'type': 'change_color'}}