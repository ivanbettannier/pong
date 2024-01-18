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
button_espacement = game_settings.screen_height/6
button_espacement_width = game_settings.screen_width/48
second_button_espacement_width = game_settings.screen_width/48

# Returns Press-Start-2P in the desired size (Press-Start-2P = Retro Arcade type font)
def get_font(size): 
    return pygame.font.Font("assets/PressStart2P-Regular.ttf", size)
ia_text_width, _ = get_font(int(game_settings.screen_width / 26)).size("DIFFICULTY")
easy_text_width, _ = get_font(int(game_settings.screen_width / 26)).size("EASY")
medium_text_width, _ = get_font(int(game_settings.screen_width / 26)).size("MEDIUM")
hard_text_widht, _ = get_font(int(game_settings.screen_width / 26)).size("HARD")
players_text_width, _ = get_font(int(game_settings.screen_width / 26)).size("PLAYERS")
one_player_text_width, _ = get_font(int(game_settings.screen_width / 26)).size("1 PLAYERS")
def main_menu():
    MAIN_MENU_BUTTON = Button(
            image=None,
            pos=(0, 0), 
            anchors={'center','top'},
            text_input="Pong game",
            font= get_font(int(game_settings.screen_width/12)),
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
        hovering_color="Green"
    )
    HARD_IA_BUTTON = Button(
        image=None,
        pos=(MEDIUM_IA_BUTTON.x_pos+medium_text_width+button_espacement_width,DIFFICULTY_SETTINGS_BUTTON.y_pos),
        anchors={'left','top'},
        text_input="HARD",
        font=get_font(int(game_settings.screen_width/26)),
        base_color="White",
        hovering_color="Green"
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
        base_color="White",
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

        MAIN_PLAY_BUTTON.update(screen)
        MAIN_MENU_BUTTON.update(screen)
        DIFFICULTY_SETTINGS_BUTTON.update(screen)
        EASY_IA_BUTTON.update(screen)
        MEDIUM_IA_BUTTON.update(screen)
        HARD_IA_BUTTON.update(screen)
        PLAYERS_SETTINGS_BUTTON.update(screen)
        ONE_PLAYER_BUTTON.update(screen)
        TWO_PLAYERS_BUTTON.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_PLAY_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    pong_game = Pong()  # Créez une instance de la classe Pong
                    pong_game.settings = game_settings
                    pong_game.run_game()  # Lancez le jeu
                #textbook pour chaque form on update l'élément sliders     
                elif EASY_IA_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    EASY_IA_BUTTON.base_color = "Green"
                    MEDIUM_IA_BUTTON.base_color = "White"
                    HARD_IA_BUTTON.base_color = "White"
                elif MEDIUM_IA_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    EASY_IA_BUTTON.base_color = "White"
                    MEDIUM_IA_BUTTON.base_color = "Green"
                    HARD_IA_BUTTON.base_color = "White"
                    game_settings.controler_height = 40
                    game_settings.ball_initial_speed = 6

                elif HARD_IA_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    EASY_IA_BUTTON.base_color = "White"
                    MEDIUM_IA_BUTTON.base_color = "White"
                    HARD_IA_BUTTON.base_color = "Green"
                    game_settings.controler_height = 25
                    game_settings.ball_initial_speed = 7
        pygame.display.update()

if __name__ == "__main__":
    main_menu()