import pygame


class ScreenFader:

    def __init__(self, screen, screen_fade, width, height, alpha):
        self.screen = screen
        self.screen_fade = screen_fade
        self.width = width
        self.height = height
        self.alpha = alpha

    def create_fade_screen(self):
        fade_screen_color = (0, 0, 0, 255)
        pygame.draw.circle(self.screen_fade, fade_screen_color, (self.width/2, self.height/2), 1000)
        self.screen.blit(self.screen_fade, (0, 0))
        pygame.display.flip()

    def update_fade_screen(self):
        fade_screen_color = (0, 0, 0, self.alpha)
        pygame.draw.circle(self.screen_fade, fade_screen_color, (self.width / 2, self.height / 2), 1000)
        self.screen.blit(self.screen_fade, (0, 0))