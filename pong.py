import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import Game_stats
from ball import Ball
from ball import Ball_bonus
from controler import Controler
#from portal import Portal
from play_area import Play_area
from scoreboard import Scoreboard
from bonus import Bonus
from bonus import Portal
import random
import math
import numpy as np

class Pong:
    """
    Global class to manage ressources and game comportment
    """

    def __init__(self):
        """Initialise game and its ressources"""
        pygame.init()
        self.settings = Settings()
        # Window size
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,
             self.settings.screen_height))
        pygame.display.set_caption("[Pont]g")
        self.bg_color = self.settings.bg_color

        # Print score
        self.stats = Game_stats(self)

        # Create playing area
        self.play_area = Play_area(self)

           

        # Create the ball
        self.ball = Ball(self)

        # Create the first controller on the left
        self.controler1 = Controler(self)
        self.controler1.rect.centery = self.screen.get_rect().centery
        self.controler1.rect.x = self.settings.play_area_positionx + self.settings.play_area_border_larger + 5
       

        # Create the second controller on the right
        self.controler2 = Controler(self)
        self.controler2.rect.centery = self.screen.get_rect().centery
        self.controler2.rect.right = self.screen.get_rect().right - self.settings.play_area_positionx - (self.settings.play_area_border_larger + 5)

        # Creat scorer area
        self.game_stats = Game_stats(self)

        # Creat score board
        self.scoreboard = Scoreboard(self)

        self.clock = pygame.time.Clock()    

        # Creat bonus
        self.bonus = Bonus(self)
        
        # Création du portail
        self.portal = Portal(self)

        # Balles multiplimes bonus 
        self.ball1 = Ball_bonus(self)
        self.ball2 = Ball_bonus(self)
        self.ball3 = Ball_bonus(self)
        self.ball4 = Ball_bonus(self)
        self.ball5 = Ball_bonus(self)
        self.ball6 = Ball_bonus(self)
        self.ball7 = Ball_bonus(self)
        self.ball8 = Ball_bonus(self)
        self.ball9 = Ball_bonus(self)
        self.ball10 = Ball_bonus(self)


  
        

    def run_game(self):
        """Begin the principal ligne of the game."""
        while True:
            self._check_events()
            self.controler1.update()
            self.controler2.update()
            self.ball.update()
            self.check_collisions(self.controler1)
            self.check_collisions(self.controler2)
            self.bonus.bonus_triggering(self.ball)
            self.portal.portal_triggering(self.ball)
            if self.settings.automat_controler == "True":
                self.automat_controler(self.controler2)
            self._self_update_screen()
            self.clock.tick(60)
            
            
            
            
    def _check_events(self):
        """Monitor keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Moving controler
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_controler_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_controler_event(event)

            
            
    def _self_update_screen(self):
        """Update the screen images and go to the next screen"""
        self.screen.fill(self.bg_color)
        self.play_area.blitme()
        #self.portal_appear()
        if self.bonus.multi_ball == True:
            self.bonus.bonus_multi_ball(self.ball1, self.ball2, self.ball3, self.ball4, self.ball5, self.ball6, self.ball7, self.ball8, self.ball9, self.ball10)
        self.ball.blitme()
        self.scoreboard.blitme()
        self.controler1.blitme()
        self.controler2.blitme()
        #self.bonus_appear(self.ball.moving)
        self.bonus.apperence(self.ball.moving)
        self.portal.apperence(self.ball.moving)
        self.scoreboard.prep_score() 
        self.exchange_end()
        
        

    def _check_keydown_controler_event(self, event):
        """Continue moving controler if key is down"""
        # Controler 1
        if event.key == pygame.K_UP:
            self.controler1.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.controler1.moving_down = True
        # Controler 2
        elif event.key == pygame.K_z:
            self.controler2.moving_up = True
        elif event.key == pygame.K_x:
            self.controler2.moving_down = True
        # Start a pong exchange
        elif event.key == pygame.K_SPACE:
            self.ball.moving = True 
        # Quit game
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_controler_event(self, event):
        """Stop moving controler if key is up"""
        # Controler 1
        if event.key == pygame.K_UP:
            self.controler1.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.controler1.moving_down = False
        # Controler 2
        elif event.key == pygame.K_z:
            self.controler2.moving_up = False
        elif event.key == pygame.K_x:
            self.controler2.moving_down = False
    
    ### PARTIE ARTHUR 
    #def check_collisions(self,controler):
    #    """Colision detection beetween the ball and a controler"""
    #    if self.ball.rect.colliderect(controler.rect):
    #        self.ball.velocity[0] = -self.ball.velocity[0]
      
    ### PARTIE CAMILLE 1    
    #def check_collisions(self, controler):
    #    """Détection de collision entre la balle et un contrôleur"""
    #    if self.ball.rect.colliderect(controler.rect):
    #        # Calcul de l'angle d'incidence en radians
    #        angle_incidence = math.atan2(self.ball.rect.centery - controler.rect.centery,
    #                                     self.ball.rect.centerx - controler.rect.centerx)
    #        
    #        # Inversion de la composante horizontale de la vitesse de la balle
    #        self.ball.velocity[0] = -self.ball.velocity[0]
    #        
    #        # Calcul de la nouvelle composante verticale de la vitesse en fonction de l'angle d'incidence
    #        self.ball.velocity[1] = self.settings.ball_initial_speed * math.sin(angle_incidence)
    
    def check_collisions(self, controler):
        """Détection de collision entre la balle et un contrôleur"""
        if self.ball.rect.colliderect(controler.rect):
            # Calcul de l'angle d'incidence en radians
            angle_incidence = math.atan2(self.ball.rect.centery - controler.rect.centery,
                                         self.ball.rect.centerx - controler.rect.centerx)
            
            # Si la balle touche le centre du contrôleur, imposer un angle de retour de 15 degrés
            if controler.rect.collidepoint(self.ball.rect.center):
                angle_incidence = math.radians(35)
            
            # Inversion de la composante horizontale de la vitesse de la balle
            self.ball.velocity[0] = -self.ball.velocity[0]
            
            # Calcul de la nouvelle composante verticale de la vitesse en fonction de l'angle d'incidence
            self.ball.velocity[1] = self.settings.ball_initial_speed * math.sin(angle_incidence)

    def automat_controler(self, controler):
        """Setting invinsible adversary"""
        # Controler exceeds the top of play area
        controler_hight = self.ball.rect.y <= self.settings.play_area_positiony + self.settings.play_area_border_larger + self.settings.controler_height/2
        # Controler exceeds the bottom of play area
        controler_low = self.ball.rect.y >= self.settings.screen_height -  self.settings.play_area_positiony - self.settings.controler_height - self.settings.play_area_border_larger + self.settings.controler_height/2
        # Stay controler in play area
        if not controler_hight and not controler_low:
            controler.rect.y = self.ball.rect.y - self.settings.controler_height/2
        elif controler_hight and not controler_low:
            controler.rect.y = self.settings.play_area_positiony + self.settings.play_area_border_larger
        elif not controler_hight and controler_low: 
            controler.rect.y = self.settings.screen_height -  self.settings.play_area_positiony - self.settings.controler_height - self.settings.play_area_border_larger

    def exchange_end(self):
        player1_point = self.ball.rect.left <= self.settings.play_area_positionx
        player2_point = self.ball.rect.right >= self.settings.play_area_positionx + self.settings.play_area_width
        if player1_point or player2_point:
            self.ball.rect.center = self.ball.screen_rect.center
            self.ball.moving = False
            self.stats.increment_score = False
            if player1_point:
                self.bonus.reinit()
                self.portal.reinit()
                self.stats.increment_score = True
                self.ball.velocity[0] = self.settings.ball_initial_speed
                self.ball.velocity[1] = self.settings.ball_initial_speed
                self.stats.count_point(2)
                            
            if player2_point:
                self.bonus.reinit()
                self.portal.reinit()
                self.stats.increment_score = True
                self.ball.velocity[0] = -self.settings.ball_initial_speed
                self.ball.velocity[1] = self.settings.ball_initial_speed
                self.stats.count_point(1)

        pygame.display.flip()

    
        
    

   
#    def portal_appear(self):
#        portal_position = self.portal_position
#        self.portal = Portal(self, portal_position)
#        self.portal.blitme()

if __name__ == '__main__':
    # create an instance and start a game 
    pong = Pong()
    pong.run_game()