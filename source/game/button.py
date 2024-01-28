
import os, sys
parent_dir = os.path.abspath('../..')
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import pygame
from game.settings import Settings

class Button:
	"""Class to use button in the game"""

	def __init__(self, image, font, pos, anchors, text_input, base_color, hovering_color):
		"""Initialize the game_settings parameters"""

		pygame.init()
		self.game_settings = Settings()
		# Window size
		self.screen = pygame.display.set_mode(
			(self.game_settings.screen_width,
			 self.game_settings.screen_height))
		pygame.display.set_caption("[Pont]g")
		self.bg_color = self.game_settings.bg_color

		self.image = image
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color

		# Position of the button
		self.pos = pos
		self.x_pos, self.y_pos = pos


		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

		#Default anchors 
		self.anchors = set(anchors)
		
		# Case where we just want the text as the button
		if self.image is None:
			self.image = self.text

		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	# Put in image on the screen
	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	# Verification of the position of the mouse
	def checkForInput(self, position):
		if (position[0] in range(self.rect.left, self.rect.right) and
				position[1] in range(self.rect.top, self.rect.bottom)):
			return True
		return False

	# Enable the change of color if we are positioned over the button
	def changeColor(self, position):
		if (position[0] in range(self.rect.left, self.rect.right) and
				position[1] in range(self.rect.top, self.rect.bottom)):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
	def apply_anchors(self, screen_width, screen_height):
		if 'left' in self.anchors:
			self.x_pos = 0
		elif 'right' in self.anchors:
			self.x_pos = screen_width - self.text_rect.width
		elif 'center' in self.anchors:
			self.x_pos = (screen_width - self.text_rect.width) // 2

		if 'top' in self.anchors:
			self.y_pos = 0
		elif 'bottom' in self.anchors:
			self.y_pos = screen_height - self.text_rect.height
		elif 'center' in self.anchors:
			self.y_pos = (screen_height - self.text_rect.height) // 2

		self.x_pos += self.pos[0]
		self.y_pos += self.pos[1]

		self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=self.rect.center)