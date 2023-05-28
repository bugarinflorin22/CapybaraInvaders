import sys

import pygame
from Scripts.Button import Button
from Scene.level import level
pygame.init()


class MainMenu:
    pygame.mixer.music.load("sounds/capybara.wav")
    pygame.mixer.music.play(-1)

    def __init__(self, screen, buttons_sprite):
        self.screen = screen
        self.buttons_sprite = buttons_sprite

    def setup(self, buttons):
        play_image = pygame.image.load("Art/butoane/buton play.png")
        play = Button(play_image, 960, 400)
        settings_image = pygame.image.load("Art/butoane/buton settings.png")
        settings = Button(settings_image, 960, 550)
        quit_image = pygame.image.load("Art/butoane/buton quit.png")
        quit = Button(quit_image, 960, 700)

        self.buttons_sprite.add(play)
        self.buttons_sprite.add(settings)
        self.buttons_sprite.add(quit)

        buttons.append(play)
        buttons.append(settings)
        buttons.append(quit)

    def update(self, event, buttons):
        mouse_position = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttons[0].check_pos(mouse_position):
                print("Play")
            if buttons[1].check_pos(mouse_position):
                print("Options")
            if buttons[2].check_pos(mouse_position):
                pygame.quit()
                sys.exit()



    '''while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("Art/butoane/buton play.png"), pos=(960, 400),
                             text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")


        OPTIONS_BUTTON = Button(image=pygame.image.load("Art/butoane/buton settings.png"), pos=(960, 550),
                                text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Art/butoane/buton quit.png"), pos=(960, 700),
                             text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")


        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            

        pygame.display.update()'''


