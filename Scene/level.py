import pygame
import math
import random


# Player
player_Img = pygame.image.load("../Art/background.png")  # the player icon
playerX = 430  # the coordonates where we want the player to be on the weight (x axis)
playerY = 590  # the coordonates where we want the player to be on the height (y axis)
playerX_change = 0

# Enemy
enemy_Img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_enemies = 6
for i in range(number_enemies):
    enemy_Img.append(pygame.image.load("../Art/level/enemy.png"))
    enemyX.append(random.randint(0, 835))
    enemyY.append(random.randint(57, 130))
    enemyX_change.append(0.3)
    enemyY_change.append(30)