import pygame
import json

class Settings:
    """Class to stock pong's parameters"""

    def __init__(self):
        "initialize game parameter"
        
        with open('../../game_type.json', 'r') as file:
            game_type = json.load(file)

        # define colors
        self.principal_color = game_type['principal_color']   
        self.secondary_color = game_type['secondary_color'] 

        # screen parameter
        self.screen_width = 800
        self.screen_height = 450
        self.bg_color = self.secondary_color
        
        # Play area parameter
        self.play_area_width = game_type['play_area_width']
        self.play_area_height = game_type['play_area_height']
        self.play_area_positionx = (self.screen_width - self.play_area_width)/2
        self.play_area_positiony = (self.screen_height - self.play_area_height)/2
        self.play_area_color = self.secondary_color
        self.play_area_border_color = self.principal_color
        self.play_area_border_larger = 5
       
        # controler parameter
        self.controler_width = 5
        self.controler_height = game_type['controler_height']
        self.controler_color = self.principal_color
        self.controler_speed = game_type['controler_speed']
        self.automat_controler = game_type['automat_controler']

        
        # ball parameter
        self.ball_size = 5
        self.ball_color = self.principal_color
        self.ball_initial_speed = game_type['ball_initial_speed']

        # Score area
        self.scoreboard_width = (self.screen_width + self.play_area_width)/6
        self.scoreboard_height = (self.screen_height - self.play_area_height)/2 - 4
        self.scoreboard_positionx = (self.screen_width - self.scoreboard_width)/2
        self.scoreboard_positiony = 2
        self.score_text_color = self.principal_color
        self.score_font = pygame.font.SysFont(None, 48)

        # Bonus
        self.limit_bonus_appearence_time = [400, 800]
        self.nomber_bonus_ball = 50

        # Portal
        self.limit_portal_appearence_time = [300, 600]

        
        

       