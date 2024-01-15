import pygame
import random

class Portal:
    """Classe pour le portail de téléportation"""

    def __init__(self, pong_game):
        """Initialise le portail avec des coordonnées aléatoires"""
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = pong_game.settings

        # Taille du portail (environ 1/5 de la hauteur de l'aire de jeu)
        self.width = 5
        self.height = int(self.settings.play_area_height / 5)

        # Couleur du portail
        self.color = (255, 0, 0)  # Rouge pour le portail

        # Coordonnées aléatoires du portail
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.randomize_position()

    def randomize_position(self):
        """Place le portail à des coordonnées aléatoires"""
        
        self.rect.left = random.randint(self.settings.play_area_positionx + 50, self.settings.play_area_positionx + self.settings.play_area_width - self.width - 50)
        
        self.rect.top = random.randint(self.settings.play_area_positiony + self.settings.play_area_border_larger, self.settings.screen_height - self.settings.play_area_positiony - self.height - self.settings.play_area_border_larger)
        
        
        #self.rect.center = self.screen_rect.center

    def blitme(self):
        """Dessine le portail"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def handle_collision(self, ball):
        """Gère la collision entre la balle et le portail"""            
            
        # Assurez-vous que la balle ne reste pas coincée sur le portail
        while self.rect.colliderect(ball.rect):
            
            #ball.rect.x = random.randint(self.settings.play_area_positionx, self.settings.play_area_positionx + self.settings.play_area_width - ball.radius * 2)
            ball.rect.y = random.randint(self.settings.play_area_positiony + self.settings.play_area_border_larger, self.settings.screen_height - self.settings.play_area_positiony - ball.radius * 2 - self.settings.play_area_border_larger) 