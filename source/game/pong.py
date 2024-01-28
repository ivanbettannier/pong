import os, sys
parent_dir = os.path.abspath('..')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)


import sys
import pygame
from game.settings import Settings
from game.game_stats import Game_stats
from game.object.ball import Ball
from game.object.ball import Ball_bonus
from game.object.controler import Controler
from game.play_area import Play_area
from game.object.scoreboard import Scoreboard
from game.object.bonus import Bonus
from game.object.bonus import Portal
from game.object.bonus import Portal_horizon
import math
import numpy as np
from game.button import Button
from game.game_state_manager import GameStateManager

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

        # 
        self.game_state_manager = GameStateManager()   

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
        self.bonus = Bonus(self, self.settings.limit_bonus_appearence_time)
        self.bonus.reinit()
        self.bonus2 = Bonus(self, [self.settings.limit_portal_appearence_time[0]*3, self.settings.limit_portal_appearence_time[1]*3])
        self.bonus2.reinit()
        self.bonus3 = Bonus(self, [self.settings.limit_portal_appearence_time[0]*5, self.settings.limit_portal_appearence_time[1]*5])
        self.bonus3.reinit()
        # Create portal
        self.portal = Portal(self, [self.settings.limit_portal_appearence_time[0]*3, self.settings.limit_portal_appearence_time[1]*3])
        self.portal.reinit()
        self.portal1 = Portal_horizon(self, self.settings.limit_portal_appearence_time)
        self.portal1.reinit()

        # Multpiple balls bonus
        self.balls = []
        for i in range(self.settings.nomber_bonus_ball):
<<<<<<< HEAD
            ball = Ball_bonus(self)  # Créez un nouvel objet de balle
            self.balls.append(ball)  # Ajoutez la balle à la liste
        # Balles multiplimes bonus 
        #for i in range(20):
        #    ball_name = f'ball{i}'
        #    setattr(self, ball_name, Ball_bonus(self))


    
    def pygame_step(self):
            """Step in the game"""
            self.controler1.update()
            self.controler2.update()
            self.ball.update()
            got_collision = self.check_collisions(self.controler1)
            self.check_collisions(self.controler2)
            self.bonus.bonus_triggering(self.ball, self.controler1, self.controler2)
            self.bonus2.bonus_triggering(self.ball, self.controler1, self.controler2)
            self.bonus3.bonus_triggering(self.ball, self.controler1, self.controler2)
            self.portal.portal_triggering(self.ball)
            self.portal1.portal_triggering(self.ball)
            if self.settings.automat_controler == "True":
                self.automat_controler(self.controler2)
            self._self_update_screen()
            return got_collision
    
    def step(self,action):
        """Step in the sense of Reinforcment Learing"""
        if action == 0:
            self.controler1.moving_down = False
            self.controler1.moving_up = True
        
        if action == 1:
            self.controler1.moving_up = False
            self.controler1.moving_down = True
            
        return self.pygame_step()

    def run_game(self):
        """Begin the principal loop of the game."""
        while True:
            self._check_events()
            self.pygame_step()
            self.clock.tick(60)
            if self._check_events():
                self.game_state_manager.set_state("menu_principal")
                self.screen.fill("Black")
                return "menu" 
            if self.game_over:
                self._game_over()

            
    def _game_over(self):
        game_over_button = Button(
                image=None,
                pos=(0,0),
                anchors={'center', 'center'},
                text_input="Game Over",
                font=pygame.font.SysFont(None, 60),
                base_color="White",
                hovering_color="White"
            )
        game_over_button.apply_anchors(self.settings.screen_width, self.settings.screen_height)
        game_over_button.update(self.screen)
        pygame.display.flip()
        pygame.time.delay(3000)
        self.screen.fill("Black")
        self.game_state_manager.set_state("menu_principal")

    def _check_events(self):
        MAIN_MOUSE_POS = pygame.mouse.get_pos()
        """Monitor keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Moving controler
            elif event.type == pygame.KEYDOWN:
                if self.bonus.bonus_inver_controler == False:
                    self._check_keydown_controler_event(event)
                if self.bonus.bonus_inver_controler == True:
                    self._check_keydown_controler_event_inver(event)
            elif event.type == pygame.KEYUP:
                if self.bonus.bonus_inver_controler == False:
                    self._check_keyup_controler_event(event)
                if self.bonus.bonus_inver_controler == True:
                    self._check_keyup_controler_event_inver(event)


            
            
    def _self_update_screen(self):
        """Update the screen images and go to the next screen"""
        self.screen.fill(self.bg_color)
        self.play_area.blitme()
        self.BACK_MAIN_MENU.update(self.screen)
        if self.bonus.multi_ball == True:
            self.bonus_multi_ball()
        if self.bonus2.multi_ball == True:
            self.bonus_multi_ball()
        self.ball.blitme()
        self.scoreboard.blitme()
        self.controler1.blitme()
        self.controler2.blitme()
        self.bonus.apperence(self.ball.moving)
        self.bonus2.apperence(self.ball.moving)
        self.bonus3.apperence(self.ball.moving)
        self.portal.apperence(self.ball.moving)
        self.portal1.apperence(self.ball.moving)
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
    
  
    def check_collisions(self, controler):
        """Détection de collision entre la balle et un contrôleur"""
        if self.ball.rect.colliderect(controler.rect):
            # Calculation of the angle of incidence in radians
            angle_incidence = math.atan2(self.ball.rect.centery - controler.rect.centery,
                                         self.ball.rect.centerx - controler.rect.centerx)
            
            # If the ball hits the center of the controller, impose a return angle of 15 degrees
            if controler.rect.collidepoint(self.ball.rect.center):
                angle_incidence = math.radians(35)
            
            # Inversion of the horizontal component of the ball's velocity
            self.ball.velocity[0] = -self.ball.velocity[0]
            
            #Calculation of the new vertical component of velocity as a function of the incidence angle
            self.ball.velocity[1] = self.settings.ball_initial_speed * math.sin(angle_incidence)
            return True
        else :
            return False

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
    
    def _check_keydown_controler_event_inver(self, event):
        """Continue moving controler if key is down"""
        # Controler 1
        if event.key == pygame.K_DOWN:
            self.controler1.moving_up = True
        elif event.key == pygame.K_UP:
            self.controler1.moving_down = True
        # Controler 2
        elif event.key == pygame.K_x:
            self.controler2.moving_down = True
        elif event.key == pygame.K_z:
            self.controler2.moving_down = True
        # Start a pong exchange
        elif event.key == pygame.K_SPACE:
            self.ball.moving = True 
        # Quit game
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_controler_event_inver(self, event):
        """Stop moving controler if key is up"""
        # Controler 1
        if event.key == pygame.K_DOWN:
            self.controler1.moving_up = False
        elif event.key == pygame.K_UP:
            self.controler1.moving_down = False
        # Controler 2
        elif event.key == pygame.K_x:
            self.controler2.moving_up = False
        elif event.key == pygame.K_z:
            self.controler2.moving_down = False

    def bonus_multi_ball(self):
        for ball in self.balls:
            ball.blitme() 
            ball.update() 


    def exchange_end(self):
        player1_point = self.ball.rect.left <= self.settings.play_area_positionx
        player2_point = self.ball.rect.right >= self.settings.play_area_positionx + self.settings.play_area_width
        if player1_point or player2_point:
            self.ball.rect.center = self.ball.screen_rect.center
            self.ball.moving = False
            self.stats.increment_score = False
            self.portal.reinit()
            self.portal1.reinit()
            self.bonus.reinit()
            self.bonus.bonus_inver_controler = False
            self.bonus.multi_ball = False
            self.bonus.controler_position = False
            self.bonus.controler_size = False
            self.bonus.controler_change_position(self.controler1, self.controler2)
            self.bonus.controler_change_size(self.ball, self.controler1, self.controler2)
            self.bonus2.reinit()
            self.bonus2.bonus_inver_controler = False
            self.bonus2.multi_ball = False
            self.bonus2.controler_position = False
            self.bonus2.controler_size = False
            self.bonus2.controler_change_position(self.controler1, self.controler2)
            self.bonus2.controler_change_size(self.ball, self.controler1, self.controler2)
            self.bonus3.reinit()
            self.bonus3.bonus_inver_controler = False
            self.bonus3.multi_ball = False
            self.bonus3.controler_position = False
            self.bonus3.controler_size = False
            self.bonus3.controler_change_position(self.controler1, self.controler2)
            self.bonus3.controler_change_size(self.ball, self.controler1, self.controler2)
            if player1_point:
                self.stats.increment_score = True
                self.ball.velocity[0] = self.settings.ball_initial_speed
                self.ball.velocity[1] = self.settings.ball_initial_speed
                self.stats.count_point(2)
                            
            if player2_point:
                self.stats.increment_score = True
                self.ball.velocity[0] = -self.settings.ball_initial_speed
                self.ball.velocity[1] = self.settings.ball_initial_speed
                self.stats.count_point(1)
            self.check_game_over()
        pygame.display.flip()
    def check_game_over(self):
        if self.stats.player1_point == 1 or self.stats.player2_point == 1:
            self.game_over = True
            game_over_button = Button(
                image=None,
                pos=(0,0),
                anchors={'center', 'center'},
                text_input="Game Over",
                font=pygame.font.SysFont(None, 60),
                base_color="White",
                hovering_color="White"
            )
            game_over_button.apply_anchors(self.settings.screen_width, self.settings.screen_height)
            game_over_button.update(self.screen)
            pygame.display.flip()
            pygame.time.delay(3000)  # Affiche le bouton "Game Over" pendant 3 secondes
            self.game_state_manager.set_state("menu_principal")



if __name__ == '__main__':
    # create an instance and start a game 
    pong = Pong()
    pong.run_game()