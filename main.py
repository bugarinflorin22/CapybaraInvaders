import pygame
from Scripts.ScreenFader import ScreenFader
from Scripts.MainMenu import MainMenu


pygame.init()
running = True
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1920, 1080))
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("Capybara Invaders")
background_image = pygame.image.load("Art/background.png")
scaled_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))
background = scaled_image.get_rect()
background.height = screen_height
background.width = screen_width
background.bottomright
fade_screen_color = (255, 0, 0, 255)
screen_width, screen_height = screen.get_size()
screen_fade = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

buttons_sprites = pygame.sprite.Group()
buttons = []
obj = []

screenFader = ScreenFader(screen, screen_fade, screen_width, screen_height, 255)
screenFader.create_fade_screen()
main_menu = MainMenu(screen, buttons_sprites)

done = True
space_key = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space_key = True

    if done:
        screen.blit(scaled_image, background)
        screenFader.update_fade_screen()
        screenFader.alpha -= 1.2 * 2
        pygame.display.flip()
        if screenFader.alpha < 10:
            screen.blit(scaled_image, background)
            main_menu.setup(buttons)
            buttons_sprites.draw(screen)
            pygame.display.flip()
            done = False

    if screenFader.alpha < 10:
        main_menu.update(event, buttons, obj)
    for ch in obj:
        ch.update(space_key, event)
    if space_key:
        space_key = False
    clock.tick(60)

pygame.quit()
