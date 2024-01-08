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

# Returns Press-Start-2P in the desired size (Press-Start-2P = Retro Arcade type font)
def get_font(size): 
    return pygame.font.Font("assets/PressStart2P-Regular.ttf", size)

def main_menu():
    MAIN_MENU_BUTTON = Button(
            image=None,
            pos=(game_settings.screen_width // 2, 100),
            text_input="Pong game",
            font= get_font(60),
            base_color="White",
            hovering_color="Green"
        )

    MAIN_PLAY_BUTTON = Button(
            image=None,
            pos=(game_settings.screen_width // 2 - 100 , 300),
            text_input="Play",
            font=get_font(45),
            base_color="White",
            hovering_color="Green"
        )
    while True:
        MAIN_MOUSE_POS = pygame.mouse.get_pos()
        MAIN_PLAY_BUTTON.changeColor(MAIN_MOUSE_POS)
        MAIN_PLAY_BUTTON.update(screen)
        MAIN_MENU_BUTTON.update(screen)
    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_PLAY_BUTTON.checkForInput(MAIN_MOUSE_POS):
                    pong_game = Pong()  # Créez une instance de la classe Pong
                    pong_game.run_game()  # Lancez le jeu


        pygame.display.update()
if __name__ == "__main__":
    main_menu()