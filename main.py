import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1960,1080))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    background_image = pygame.image.load("Art/background.png")
    scaled_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))
    screen.blit(scaled_image, [0,0])

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()