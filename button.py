import pygame
from settings import Settings

class Button:
	"""Class to use button in the game"""

	def __init__(self, image, font, pos, text_input, base_color, hovering_color):
		"""Initialize the settings parameters"""

		pygame.init()
		self.settings = Settings()
		# Window size
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width,
			 self.settings.screen_height))
		pygame.display.set_caption("[Pont]g")
		self.bg_color = self.settings.bg_color

		self.image = image
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color

		# Position of the button
		self.x_pos = pos[0]
		self.y_pos = pos[1]

		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

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