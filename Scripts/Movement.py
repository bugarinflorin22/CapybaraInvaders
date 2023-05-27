import pygame


class Player_Movement:
    def __init__(self, event, player):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -7
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 7
            elif event.key == pygame.K_UP:
                player.speed_y = -5
            elif event.key == pygame.K_DOWN:
                player.speed_y = 5

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.speed_y = 0
