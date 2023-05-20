import pygame
from Scripts.ScreenFader import ScreenFader


pygame.init()
running = True
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1024, 720))
screen_width, screen_height = screen.get_size()
background_image = pygame.image.load("Art/background.png")
scaled_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))
background = scaled_image.get_rect()
background.height = screen_height
background.width = screen_width
background.bottomright

fade_screen_color = (255, 0, 0, 255)
screen_width, screen_height = screen.get_size()
screen_fade = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

screenFader = ScreenFader(screen, screen_fade, screen_width, screen_height, 255)
screenFader.create_fade_screen()
screenFader.alpha = 255

done = True

while running:
    if done:
        screen.blit(scaled_image, background)
        screenFader.update_fade_screen()
        screenFader.alpha -= 0.5
        pygame.display.flip()
        if screenFader.alpha == 0:
            screen.blit(scaled_image, background)
            pygame.display.flip()
            done = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)


pygame.quit()
