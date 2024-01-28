import os, sys
parent_dir = os.path.abspath('../..')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import pygame
from game.settings import Settings
from game.game_stats import Game_stats
from game.object.object import Object 

class Scoreboard(Object):
    """Follow score of the game"""

    def __init__(self, pong_game):
        """Initialize game_settings"""
        super().__init__(pong_game)
        self.stats = pong_game.stats
        self.game_settings = pong_game.settings
    
        # Score board size
        self.scoreboard = pygame.Surface(
            (self.game_settings.scoreboard_width, 
                self.game_settings.scoreboard_height))
        self.scoreboard.fill(self.game_settings.bg_color)
        self.scoreboard_rect = self.scoreboard.get_rect()
        # Parameter score text font
        self.text_color = self.game_settings.score_text_color
        self.font = self.game_settings.score_font
       

    def blitme(self):
        """Draw score board"""
        self.screen.blit(self.scoreboard, (self.game_settings.scoreboard_positionx, self.game_settings.scoreboard_positiony))

    def prep_score(self):
        """Transform score to an image"""
        score1_str = str(self.stats.player1_point)
        score2_str = str(self.stats.player2_point)
        self.score1_image = self.font.render(score1_str, True, self.text_color, self.game_settings.bg_color)
        self.score2_image = self.font.render(score2_str, True, self.text_color, self.game_settings.bg_color)
        """Draw score"""
        self.screen.blit(self.score1_image, (self.game_settings.scoreboard_positionx+5, self.scoreboard_rect.centery + 5))
        self.screen.blit(self.score2_image, (self.game_settings.scoreboard_positionx+self.game_settings.scoreboard_width-25, self.scoreboard_rect.centery + 5))
    