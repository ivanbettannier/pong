import os, sys
parent_dir = os.path.abspath('..')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import pygame
from game.button import Button
from game.settings import Settings
from game.pong import Pong
import json
from game.game_state_manager import GameStateManager

with open('../../game_type.json', 'r') as file:
    game_type = json.load(file)

pygame.init()

game_settings = Settings()
screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()
clock.tick(60)  # Adjust the value as needed (e.g., 60 frames per second)

first_button_espacement = game_settings.screen_height/4
button_espacement = game_settings.screen_height/6
button_espacement_width = game_settings.screen_width/48
second_button_espacement_width = game_settings.screen_width/48

# Returns Press-Start-2P in the desired size (Press-Start-2P = Retro Arcade type font)
def get_font(size): 
    return pygame.font.Font("../../assets/PressStart2P-Regular.ttf", size)
ia_text_width, _ = get_font(int(game_settings.screen_width / 26)).size("DIFFICULTY")
easy_text_width, _ = get_font(int(game_settings.screen_width / 26)).size("EASY")
medium_text_width, _ = get_font(int(game_settings.screen_width / 26)).size("MEDIUM")
hard_text_widht, _ = get_font(int(game_settings.screen_width / 26)).size("HARD")
players_text_width, _ = get_font(int(game_settings.screen_width / 26)).size("PLAYERS")
one_player_text_width, _ = get_font(int(game_settings.screen_width / 26)).size("1 PLAYERS")
ambiance_text_width, _ = get_font(int(game_settings.screen_width / 26)).size("AMBIANCE")
arcade_text_width, _ = get_font(int(game_settings.screen_width / 26)).size("ARCADE")
sky_text_width, _ = get_font(int(game_settings.screen_width / 26)).size("SKY")
def main_menu():
    MAIN_MENU_BUTTON = Button(
            image=None,
            pos=(0, 0), 
            anchors={'center','top'},
            text_input="Pong game",
            font= get_font(int(game_settings.screen_width/10)),
            base_color="White",
            hovering_color="White"
    )

    MAIN_PLAY_BUTTON = Button(
            image=None,
            pos=(0 ,MAIN_MENU_BUTTON.y_pos + first_button_espacement),
            anchors={'center','top'},
            text_input="Play",
            font=get_font(int(game_settings.screen_width/20)),
            base_color="White",
            hovering_color="Green"
    )
    
    DIFFICULTY_SETTINGS_BUTTON = Button(
        image=None,
        pos=(0,MAIN_PLAY_BUTTON.y_pos+button_espacement),
        anchors={'left','top'},
        text_input="DIFFICULTY",
        font=get_font(int(game_settings.screen_width/26)),
        base_color="White",
        hovering_color="White"
    )
    EASY_IA_BUTTON = Button(
        image=None,
        pos=(DIFFICULTY_SETTINGS_BUTTON.x_pos+ia_text_width+button_espacement_width,DIFFICULTY_SETTINGS_BUTTON.y_pos),
        anchors={'left','top'},
        text_input="EASY",
        font=get_font(int(game_settings.screen_width/26)),
        base_color="White",
        hovering_color="Green"
    )
    MEDIUM_IA_BUTTON = Button(
        image=None,
        pos=(EASY_IA_BUTTON.x_pos+easy_text_width+button_espacement_width,DIFFICULTY_SETTINGS_BUTTON.y_pos),
        anchors={'left','top'},
        text_input="MEDIUM",
        font=get_font(int(game_settings.screen_width/26)),
        base_color="White",
        hovering_color="Orange"
    )
    HARD_IA_BUTTON = Button(
        image=None,
        pos=(MEDIUM_IA_BUTTON.x_pos+medium_text_width+button_espacement_width,DIFFICULTY_SETTINGS_BUTTON.y_pos),
        anchors={'left','top'},
        text_input="HARD",
        font=get_font(int(game_settings.screen_width/26)),
        base_color="White",
        hovering_color="Red"
    )
    PLAYERS_SETTINGS_BUTTON = Button(
        image=None,
        pos=(0,DIFFICULTY_SETTINGS_BUTTON.y_pos+button_espacement),
        anchors={'left','top'},
        text_input="PLAYERS",
        font=get_font(int(game_settings.screen_width/26)),
        base_color="White",
        hovering_color="White"
    )
    ONE_PLAYER_BUTTON = Button(
        image=None,
        pos=(PLAYERS_SETTINGS_BUTTON.x_pos+players_text_width+button_espacement_width,PLAYERS_SETTINGS_BUTTON.y_pos),
        anchors={'left','top'},
        text_input="1 PLAYER",
        font=get_font(int(game_settings.screen_width/26)),
        base_color="Green",
        hovering_color="Green"
    )
    TWO_PLAYERS_BUTTON = Button(
        image=None,
        pos=(ONE_PLAYER_BUTTON.x_pos+button_espacement_width+one_player_text_width,PLAYERS_SETTINGS_BUTTON.y_pos),
        anchors={'left','top'},
        text_input="2 PLAYERS",
        font=get_font(int(game_settings.screen_width/26)),
        base_color="White",
        hovering_color="Green"
    )
    AMBIANCE_SETTINGS_BUTTON = Button(
        image=None,
        pos=(0,PLAYERS_SETTINGS_BUTTON.y_pos+button_espacement),
        anchors={'left','top'},
        text_input="AMBIANCE",
        font=get_font(int(game_settings.screen_width/26)),
        base_color="White",
        hovering_color="White"
    )
    ARCADE_BUTTON = Button(
        image=None,
        pos=(AMBIANCE_SETTINGS_BUTTON.x_pos+ambiance_text_width+button_espacement_width,AMBIANCE_SETTINGS_BUTTON.y_pos),
        anchors={'left','top'},
        text_input="ARCADE",
        font=get_font(int(game_settings.screen_width/26)),
        base_color="White",
        hovering_color=[60, 140, 40]
    )
    SKY_BUTTON = Button(
        image=None,
        pos=(ARCADE_BUTTON.x_pos+arcade_text_width+button_espacement_width,AMBIANCE_SETTINGS_BUTTON.y_pos),
        anchors={'left','top'},
        text_input="SKY",
        font=get_font(int(game_settings.screen_width/26)),
        base_color="White",
        hovering_color=[92, 255, 255]
    )
    LAVA_BUTTON = Button(
        image=None,
        pos=(SKY_BUTTON.x_pos+sky_text_width+button_espacement_width,AMBIANCE_SETTINGS_BUTTON.y_pos),
        anchors={'left','top'},
        text_input="LAVA",
        font=get_font(int(game_settings.screen_width/26)),
        base_color="White",
        hovering_color=[255, 68, 25]
    )
    
    
    while True:
        MAIN_MOUSE_POS = pygame.mouse.get_pos()
        MAIN_PLAY_BUTTON.changeColor(MAIN_MOUSE_POS)
        MAIN_PLAY_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        
        MAIN_MENU_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        
        DIFFICULTY_SETTINGS_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        DIFFICULTY_SETTINGS_BUTTON.changeColor(MAIN_MOUSE_POS)
        
        EASY_IA_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        EASY_IA_BUTTON.changeColor(MAIN_MOUSE_POS)

        MEDIUM_IA_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        MEDIUM_IA_BUTTON.changeColor(MAIN_MOUSE_POS)

        HARD_IA_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        HARD_IA_BUTTON.changeColor(MAIN_MOUSE_POS)
        
        PLAYERS_SETTINGS_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        PLAYERS_SETTINGS_BUTTON.changeColor(MAIN_MOUSE_POS)
        
        ONE_PLAYER_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        ONE_PLAYER_BUTTON.changeColor(MAIN_MOUSE_POS)
        
        TWO_PLAYERS_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        TWO_PLAYERS_BUTTON.changeColor(MAIN_MOUSE_POS)

        AMBIANCE_SETTINGS_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        AMBIANCE_SETTINGS_BUTTON.changeColor(MAIN_MOUSE_POS)

        ARCADE_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        ARCADE_BUTTON.changeColor(MAIN_MOUSE_POS)

        SKY_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        SKY_BUTTON.changeColor(MAIN_MOUSE_POS)

        LAVA_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        LAVA_BUTTON.changeColor(MAIN_MOUSE_POS)

    

        MAIN_PLAY_BUTTON.update(screen)
        MAIN_MENU_BUTTON.update(screen)
        DIFFICULTY_SETTINGS_BUTTON.update(screen)
        EASY_IA_BUTTON.update(screen)
        MEDIUM_IA_BUTTON.update(screen)
        HARD_IA_BUTTON.update(screen)
        PLAYERS_SETTINGS_BUTTON.update(screen)
        ONE_PLAYER_BUTTON.update(screen)
        TWO_PLAYERS_BUTTON.update(screen)
        AMBIANCE_SETTINGS_BUTTON.update(screen)
        ARCADE_BUTTON.update(screen)
        SKY_BUTTON.update(screen)
        LAVA_BUTTON.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_PLAY_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    if ONE_PLAYER_BUTTON.base_color == "Green" or [0, 250, 0]:
                        game_type['automat_controler'] = "True"
                        if EASY_IA_BUTTON.base_color == "Green":
                            game_type['controler_speed'] = 5
                            game_type['ball_initial_speed'] = 5
                            game_type['controler_height'] = 50
                            game_type['play_area_height'] = 300
                            game_type['play_area_width'] = 700
                            if ARCADE_BUTTON.base_color == [60, 140, 40]:
                                game_type['principal_color'] = [60, 140, 40]
                                game_type['secondary_color'] = [0, 0, 0]
                            if SKY_BUTTON.base_color == [92, 255, 255]:
                                game_type['principal_color'] = [255, 220, 1]
                                game_type['secondary_color'] = [92, 255, 255]
                            if LAVA_BUTTON.base_color == [255, 68, 25]:
                                game_type['principal_color'] = [128, 36, 123]
                                game_type['secondary_color'] = [255, 68, 25]

                        if MEDIUM_IA_BUTTON.base_color == "Orange":
                            game_type['controler_speed'] = 5
                            game_type['ball_initial_speed'] = 5
                            game_type['controler_height'] = 40
                            game_type['play_area_height'] = 200
                            game_type['play_area_width'] = 400
                            if ARCADE_BUTTON.base_color == [60, 140, 40]:
                                game_type['principal_color'] = [60, 140, 40]
                                game_type['secondary_color'] = [0, 0, 0]
                            if SKY_BUTTON.base_color == [92, 255, 255]:
                                game_type['principal_color'] = [255, 220, 1]
                                game_type['secondary_color'] = [92, 255, 255]
                            if LAVA_BUTTON.base_color == [255, 68, 25]:
                                game_type['principal_color'] = [128, 36, 123]
                                game_type['secondary_color'] = [255, 68, 25]
        
                        if HARD_IA_BUTTON.base_color == "Red":
                            game_type['controler_speed'] = 8
                            game_type['ball_initial_speed'] = 10
                            game_type['controler_height'] = 50
                            game_type['play_area_height'] = 300
                            game_type['play_area_width'] = 700
                            if ARCADE_BUTTON.base_color == [60, 140, 40]:
                                game_type['principal_color'] = [60, 140, 40]
                                game_type['secondary_color'] = [0, 0, 0]
                            if SKY_BUTTON.base_color == [92, 255, 255]:
                                game_type['principal_color'] = [255, 220, 1]
                                game_type['secondary_color'] = [92, 255, 255]
                            if LAVA_BUTTON.base_color == [255, 68, 25]:
                                game_type['principal_color'] = [128, 36, 123]
                                game_type['secondary_color'] = [255, 68, 25]
                        
                        else:
                            if ARCADE_BUTTON.base_color == [60, 140, 40]:
                                game_type['principal_color'] = [60, 140, 40]
                                game_type['secondary_color'] = [0, 0, 0]
                            if SKY_BUTTON.base_color == [92, 255, 255]:
                                game_type['principal_color'] = [255, 220, 1]
                                game_type['secondary_color'] = [92, 255, 255]
                            if LAVA_BUTTON.base_color == [255, 68, 25]:
                                game_type['principal_color'] = [128, 36, 123]
                                game_type['secondary_color'] = [255, 68, 25]
                    
                    if TWO_PLAYERS_BUTTON.base_color == "Green":
                        game_type['automat_controler'] = "False"
                        with open('../../game_type.json', 'w') as file:
                            json.dump(game_type, file)
                        if EASY_IA_BUTTON.base_color == "Green":
                            game_type['controler_speed'] = 5
                            game_type['ball_initial_speed'] = 5
                            game_type['controler_height'] = 50
                            game_type['play_area_height'] = 300
                            game_type['play_area_width'] = 700
                            if ARCADE_BUTTON.base_color == [60, 140, 40]:
                                game_type['principal_color'] = [60, 140, 40]
                                game_type['secondary_color'] = [0, 0, 0]
                            if SKY_BUTTON.base_color == [92, 255, 255]:
                                game_type['principal_color'] = [255, 220, 1]
                                game_type['secondary_color'] = [92, 255, 255]
                            if LAVA_BUTTON.base_color == [255, 68, 25]:
                                game_type['principal_color'] = [128, 36, 123]
                                game_type['secondary_color'] = [255, 68, 25]

                        if MEDIUM_IA_BUTTON.base_color == "Orange":
                            game_type['controler_speed'] = 5
                            game_type['ball_initial_speed'] = 5
                            game_type['controler_height'] = 40
                            game_type['play_area_height'] = 200
                            game_type['play_area_width'] = 400
                            if ARCADE_BUTTON.base_color == [60, 140, 40]:
                                game_type['principal_color'] = [60, 140, 40]
                                game_type['secondary_color'] = [0, 0, 0]
                            if SKY_BUTTON.base_color == [92, 255, 255]:
                                game_type['principal_color'] = [255, 220, 1]
                                game_type['secondary_color'] = [92, 255, 255]
                            if LAVA_BUTTON.base_color == [255, 68, 25]:
                                game_type['principal_color'] = [128, 36, 123]
                                game_type['secondary_color'] = [255, 68, 25]
        
                        if HARD_IA_BUTTON.base_color == "Red":
                            game_type['controler_speed'] = 8
                            game_type['ball_initial_speed'] = 10
                            game_type['controler_height'] = 50
                            game_type['play_area_height'] = 300
                            game_type['play_area_width'] = 700
                            if ARCADE_BUTTON.base_color == [60, 140, 40]:
                                game_type['principal_color'] = [60, 140, 40]
                                game_type['secondary_color'] = [0, 0, 0]
                            if SKY_BUTTON.base_color == [92, 255, 255]:
                                game_type['principal_color'] = [255, 220, 1]
                                game_type['secondary_color'] = [92, 255, 255]
                            if LAVA_BUTTON.base_color == [255, 68, 25]:
                                game_type['principal_color'] = [128, 36, 123]
                                game_type['secondary_color'] = [255, 68, 25]
                        
                        else:
                            if ARCADE_BUTTON.base_color == [60, 140, 40]:
                                game_type['principal_color'] = [60, 140, 40]
                                game_type['secondary_color'] = [0, 0, 0]
                            if SKY_BUTTON.base_color == [92, 255, 255]:
                                game_type['principal_color'] = [255, 220, 1]
                                game_type['secondary_color'] = [92, 255, 255]
                            if LAVA_BUTTON.base_color == [255, 68, 25]:
                                game_type['principal_color'] = [128, 36, 123]
                                game_type['secondary_color'] = [255, 68, 25]
                    with open('../../game_type.json', 'w') as file:
                        json.dump(game_type, file)
                    pong_game = Pong()  # Créez une instance de la classe Pong
                    pong_game.run_game()  # Lancez le jeu
                #textbook pour chaque form on update l'élément sliders     
                elif EASY_IA_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    EASY_IA_BUTTON.base_color = "Green"
                    MEDIUM_IA_BUTTON.base_color = "White"
                    HARD_IA_BUTTON.base_color = "White"

                elif MEDIUM_IA_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    EASY_IA_BUTTON.base_color = "White"
                    MEDIUM_IA_BUTTON.base_color = "Orange"
                    HARD_IA_BUTTON.base_color = "White"
                    

                elif HARD_IA_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    EASY_IA_BUTTON.base_color = "White"
                    MEDIUM_IA_BUTTON.base_color = "White"
                    HARD_IA_BUTTON.base_color = "Red"

                elif ONE_PLAYER_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    TWO_PLAYERS_BUTTON.base_color = "White"
                    ONE_PLAYER_BUTTON.base_color = [0, 250, 0]
                    
                elif TWO_PLAYERS_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    TWO_PLAYERS_BUTTON.base_color = "Green"
                    ONE_PLAYER_BUTTON.base_color = "White"

                elif ARCADE_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    ARCADE_BUTTON.base_color = [60, 140, 40]
                    SKY_BUTTON.base_color = "White"
                    LAVA_BUTTON.base_color = "White"

                elif SKY_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    ARCADE_BUTTON.base_color = "White"
                    SKY_BUTTON.base_color = [92, 255, 255]
                    LAVA_BUTTON.base_color = "White"

                elif LAVA_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    ARCADE_BUTTON.base_color = "White"
                    SKY_BUTTON.base_color = "White"
                    LAVA_BUTTON.base_color = [255, 68, 25]
        pygame.display.update()



        

if __name__ == "__main__":
    main_menu()
    game_state_manager = GameStateManager()
    while game_state_manager.get_state() == "menu_principal":
        main_menu(game_state_manager)
