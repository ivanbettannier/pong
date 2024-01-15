import pygame
import sys
from button import Button
from settings import Settings
from pong import Pong

pygame.init()

game_settings = Settings()
screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()
clock.tick(60)  # Adjust the value as needed (e.g., 60 frames per second)

first_button_espacement = game_settings.screen_height/4
button_espacement = game_settings.screen_height/7
button_espacement_width = game_settings.screen_width/48
second_button_espacement_width = game_settings.screen_width/48

easy_button_clicked = False

# Returns Press-Start-2P in the desired size (Press-Start-2P = Retro Arcade type font)
def get_font(size): 
    return pygame.font.Font("assets/PressStart2P-Regular.ttf", size)
ia_text_width, _ = get_font(int(game_settings.screen_height / 17)).size("IA")
easy_text_width, _ = get_font(int(game_settings.screen_height / 17)).size("EASY")
medium_text_width, _ = get_font(int(game_settings.screen_height / 17)).size("MEDIUM")
speed_text_width, _ = get_font(int(game_settings.screen_height / 20)).size("SPEED")
easy_speed_text_width, _ = get_font(int(game_settings.screen_height / 20)).size("EASY")
medium_speed_text_width, _ = get_font(int(game_settings.screen_height / 20)).size("MEDIUM")
def main_menu():
    MAIN_MENU_BUTTON = Button(
            image=None,
            pos=(0, 0), 
            anchors={'center','top'},
            text_input="Pong game",
            font= get_font(int(game_settings.screen_height/12)),
            base_color="White",
            hovering_color="White"
        )

    MAIN_PLAY_BUTTON = Button(
            image=None,
            pos=(0 ,MAIN_MENU_BUTTON.y_pos + first_button_espacement),
            anchors={'center','top'},
            text_input="Play",
            font=get_font(int(game_settings.screen_height/17)),
            base_color="White",
            hovering_color="Green"
        )
    
    MAIN_SETTINGS_BUTTON = Button(
            image=None,
            pos=(0 , MAIN_PLAY_BUTTON.y_pos + button_espacement),
            anchors={'center','top'},
            text_input="Settings",
            font=get_font(int(game_settings.screen_height/17)),
            base_color="White",
            hovering_color="Green"
        )
    DIFFICULTY_SETTINGS_BUTTON = Button(
        image=None,
        pos=(0,MAIN_SETTINGS_BUTTON.y_pos+button_espacement),
        anchors={'left','top'},
        text_input="IA",
        font=get_font(int(game_settings.screen_height/17)),
        base_color="White",
        hovering_color="Green"
    )
    EASY_IA_BUTTON = Button(
        image=None,
        pos=(DIFFICULTY_SETTINGS_BUTTON.x_pos+ia_text_width+button_espacement_width,DIFFICULTY_SETTINGS_BUTTON.y_pos),
        anchors={'left','top'},
        text_input="EASY",
        font=get_font(int(game_settings.screen_height/17)),
        base_color="White",
        hovering_color="Green"
    )
    MEDIUM_IA_BUTTON = Button(
        image=None,
        pos=(EASY_IA_BUTTON.x_pos+easy_text_width+button_espacement_width,DIFFICULTY_SETTINGS_BUTTON.y_pos),
        anchors={'left','top'},
        text_input="MEDIUM",
        font=get_font(int(game_settings.screen_height/17)),
        base_color="White",
        hovering_color="Green"
    )
    HARD_IA_BUTTON = Button(
        image=None,
        pos=(MEDIUM_IA_BUTTON.x_pos+medium_text_width+button_espacement_width,DIFFICULTY_SETTINGS_BUTTON.y_pos),
        anchors={'left','top'},
        text_input="HARD",
        font=get_font(int(game_settings.screen_height/17)),
        base_color="White",
        hovering_color="Green"
    )
    SPEED_SETTINGS_BUTTON = Button(
        image=None,
        pos=(0,DIFFICULTY_SETTINGS_BUTTON.y_pos+button_espacement),
        anchors={'left','top'},
        text_input="SPEED",
        font=get_font(int(game_settings.screen_height/20)),
        base_color="White",
        hovering_color="White"
    )
    EASY_SPEED_BUTTON = Button(
            image=None,
            pos=(SPEED_SETTINGS_BUTTON.x_pos+speed_text_width+second_button_espacement_width,SPEED_SETTINGS_BUTTON.y_pos),
            anchors={'left','top'},
            text_input="EASY",
            font=get_font(int(game_settings.screen_height/20)),
            base_color="White",
            hovering_color="Green"
    )
    MEDIUM_SPEED_BUTTON = Button(
            image=None,
            pos=(EASY_SPEED_BUTTON.x_pos+easy_speed_text_width+second_button_espacement_width,SPEED_SETTINGS_BUTTON.y_pos),
            anchors={'left','top'},
            text_input="MEDIUM",
            font=get_font(int(game_settings.screen_height/20)),
            base_color="White",
            hovering_color="Green"
    )
    HARD_SPEED_BUTTON = Button(
            image=None,
            pos=(MEDIUM_SPEED_BUTTON.x_pos+medium_speed_text_width+second_button_espacement_width,SPEED_SETTINGS_BUTTON.y_pos),
            anchors={'left','top'},
            text_input="HARD",
            font=get_font(int(game_settings.screen_height/20)),
            base_color="White",
            hovering_color="Green"
    )
    while True:
        MAIN_MOUSE_POS = pygame.mouse.get_pos()
        MAIN_PLAY_BUTTON.changeColor(MAIN_MOUSE_POS)
        MAIN_PLAY_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        
        MAIN_SETTINGS_BUTTON.changeColor(MAIN_MOUSE_POS)
        MAIN_SETTINGS_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        MAIN_MENU_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        
        DIFFICULTY_SETTINGS_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        DIFFICULTY_SETTINGS_BUTTON.changeColor(MAIN_MOUSE_POS)
        
        EASY_IA_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        EASY_IA_BUTTON.changeColor(MAIN_MOUSE_POS)

        MEDIUM_IA_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        MEDIUM_IA_BUTTON.changeColor(MAIN_MOUSE_POS)

        HARD_IA_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        HARD_IA_BUTTON.changeColor(MAIN_MOUSE_POS)

        SPEED_SETTINGS_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        SPEED_SETTINGS_BUTTON.changeColor(MAIN_MOUSE_POS)

        EASY_SPEED_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        EASY_SPEED_BUTTON.changeColor(MAIN_MOUSE_POS)

        MEDIUM_SPEED_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        MEDIUM_SPEED_BUTTON.changeColor(MAIN_MOUSE_POS)

        HARD_SPEED_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)
        HARD_SPEED_BUTTON.changeColor(MAIN_MOUSE_POS)

        MAIN_PLAY_BUTTON.update(screen)
        MAIN_MENU_BUTTON.update(screen)
        MAIN_SETTINGS_BUTTON.update(screen)
        DIFFICULTY_SETTINGS_BUTTON.update(screen)
        EASY_IA_BUTTON.update(screen)
        MEDIUM_IA_BUTTON.update(screen)
        HARD_IA_BUTTON.update(screen)
        SPEED_SETTINGS_BUTTON.update(screen)
        EASY_SPEED_BUTTON.update(screen)
        MEDIUM_SPEED_BUTTON.update(screen)
        HARD_SPEED_BUTTON.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_PLAY_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    pong_game = Pong()  # Créez une instance de la classe Pong
                    pong_game.run_game()  # Lancez le jeu
                #textbook pour chaque form on update l'élément sliders     
                elif MAIN_SETTINGS_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    settings_menu()
                elif EASY_IA_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    EASY_IA_BUTTON.base_color = "Green"
                    MEDIUM_IA_BUTTON.base_color = "White"
                    HARD_IA_BUTTON.base_color = "White"
                elif MEDIUM_IA_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    EASY_IA_BUTTON.base_color = "White"
                    MEDIUM_IA_BUTTON.base_color = "Green"
                    HARD_IA_BUTTON.base_color = "White"
                elif HARD_IA_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    EASY_IA_BUTTON.base_color = "White"
                    MEDIUM_IA_BUTTON.base_color = "White"
                    HARD_IA_BUTTON.base_color = "Green"
                elif EASY_SPEED_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    EASY_SPEED_BUTTON.base_color = "Green"
                    MEDIUM_SPEED_BUTTON.base_color = "White"
                    HARD_SPEED_BUTTON.base_color = "White"
                elif MEDIUM_SPEED_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    EASY_SPEED_BUTTON.base_color = "White"
                    MEDIUM_SPEED_BUTTON.base_color = "Green"
                    HARD_SPEED_BUTTON.base_color = "White"
                elif HARD_SPEED_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    EASY_SPEED_BUTTON.base_color = "White"
                    MEDIUM_SPEED_BUTTON.base_color = "White"
                    HARD_SPEED_BUTTON.base_color = "Green"
        pygame.display.update()
def settings_menu():
    POlYGONS_PARAMETERS_BUTTON = Button( 
            image=None,
            pos=(0 ,first_button_espacement),
            anchors={'center','top'},
            text_input="POLYGONS SETTINGS",
            font= get_font(40),
            base_color="White",
            hovering_color="Green"
        )   
    BACK_TO_MAIN_BUTTON = Button( 
            image=None,
            pos=(0, POlYGONS_PARAMETERS_BUTTON.y_pos + button_espacement),
            anchors={'center','top'},
            text_input="Main Menu",
            font= get_font(40),
            base_color="White",
            hovering_color="Green"
        )
    while True:
        MAIN_MOUSE_POS = pygame.mouse.get_pos()
        POlYGONS_PARAMETERS_BUTTON.changeColor(MAIN_MOUSE_POS)
        POlYGONS_PARAMETERS_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)  # Ajoutez les parenthèses ici
        BACK_TO_MAIN_BUTTON.apply_anchors(game_settings.screen_width, game_settings.screen_height)  # Ajoutez les parenthèses ici
        BACK_TO_MAIN_BUTTON.changeColor(MAIN_MOUSE_POS)
        BACK_TO_MAIN_BUTTON.update(screen)
        POlYGONS_PARAMETERS_BUTTON.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_TO_MAIN_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    main_menu()  # Come back to the main  menu     

        pygame.display.update()
if __name__ == "__main__":
    main_menu()