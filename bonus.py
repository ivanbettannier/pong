import pygame
from settings import Settings
import random



class Feature:
    """Class for the pong ball"""

    def __init__(self, pong_game, feature_color='Black', feature_position=[0,0]):
        """Initialize the ball and define its initial position"""
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = Settings()
        self.limit_appearence_time = [100, 200] #"""problème à gérer"""
        self.appearence_time = random.randint(self.limit_appearence_time[0], self.limit_appearence_time[1])

        # feature copus definitio
        self.color = feature_color
   
    def random_position(self,limit_x, limit_y):
        return [random.randint(limit_x[0], limit_x[1]), random.randint(limit_y[0], limit_y[1])]

    def reinit(self):
        self.appearence = 0
        self.color = self.settings.secondary_color
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
            self.blitme()
            
    
    def blitme(self):
        """Draw feature"""
        
        self.screen.blit(self.image, self.rect)

   



class Bonus(Feature):
       
    def __init__(self, pong_game, feature_color='White', feature_position=[0, 0]):
        """Initialise le feature spécial en appelant le constructeur de la classe mère"""
        super().__init__(pong_game, feature_color, feature_position)
        self.limit_appearence_time = self.settings.limit_bonus_appearence_time
        self.appearence = 0
        self.position = feature_position
        self.size = self.settings.ball_size*5
        self.limit_x = [self.settings.play_area_positionx+int(self.settings.play_area_width*(1/6)), self.settings.play_area_positionx+int(self.settings.play_area_width*(5/6))]
        self.limit_y = [self.settings.play_area_positiony+self.size, self.settings.play_area_positiony+self.settings.play_area_height-self.size]
        self.color = feature_color
        self.multi_ball = False
        # creation of ball surface
        self.image = pygame.Surface((self.size * 2, self.size * 2),
                                    pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.size, self.size),
                           self.size)
        self.rect = self.image.get_rect()

    def bonus_triggering(self, ball):
        """Colision detection beetween the ball and the bonus"""
        if self.rect.colliderect(ball.rect):
            if self.color == 'Yellow':
                ball.change_color()
            if self.color == 'White':
                self.multi_ball = True
            self.reinit()
    
    def bonus_multi_ball(self, ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9, ball10):
        ball1.blitme()
        ball2.blitme()
        ball3.blitme()
        ball4.blitme()
        ball5.blitme()
        ball6.blitme()
        ball7.blitme()
        ball8.blitme()
        ball9.blitme()
        ball10.blitme()
        ball1.update()
        ball2.update()
        ball3.update()
        ball4.update()
        ball5.update()
        ball6.update()
        ball7.update()
        ball8.update()
        ball9.update()
        ball10.update()

class Portal(Feature):
       
    def __init__(self, pong_game, feature_color='Yellow', feature_position=[0, 0]):
        """Initialise le feature spécial en appelant le constructeur de la classe mère"""
        super().__init__(pong_game, feature_color, feature_position)
        self.limit_appearence_time = self.settings.limit_portal_appearence_time
        self.height = int(self.settings.play_area_height / 5)
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

        
    

        



#feature_dict = {'change_ball_color': {'color' : (0, 140, 0),'type': 'change_color'}}