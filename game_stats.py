import pygame
from settings import Settings

class Game_stats:
    """Follow score of the game"""

    def __init__(self, pong):
        """Initialize settings"""
        self.settings = pong.settings
        self.player1_point = 0
        self.player2_point = 0
        self.increment_score1 = False
        self.increment_score2 = False
        
        

        
       
    #def reset_stats(self):
     #   self.start_point1 = 0
      #  self.start_point2 = 0 

    def count_point1(self):
        if self.increment_score1:
            self.player1_point += 1
        self.increment_score1 = False

    def count_point2(self):
        if self.increment_score2:
            self.player2_point += 1
        self.increment_score2 = False


    

    