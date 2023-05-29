import pygame

class Text:
    def __init__(self, text, font_size, position, color=(255, 255, 255)):
        self.text = text
        self.font_size = font_size
        self.position = position
        self.color = color
        self.font = pygame.font.Font(None, self.font_size)
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect()
        self.rect.topleft = self.position

    def update_text(self, text):
        self.text = text
        self.surface = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.surface, self.rect)
