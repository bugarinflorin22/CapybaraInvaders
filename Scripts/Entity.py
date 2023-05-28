import pygame
import random


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill("black")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = 5
        self.screen = screen

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > self.screen.get_height():
            self.kill()


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, screen, image):
        super().__init__()
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen.get_width() // 2
        self.rect.bottom = self.screen.get_height() - 0
        self.speed_x = 0
        self.speed_y = 0
        self.lives = 3

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.screen.get_width():
            self.rect.right = self.screen.get_width()
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > self.screen.get_height():
            self.rect.bottom = self.screen.get_height()

    def shoot(self, sprites, bullet_sprite):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        sprites.add(bullet)
        bullet_sprite.add(bullet)

        
class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("../Art/level/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen.get_width() - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_x = random.choice([-2, 2])
        self.speed_y = random.randrange(1, 4)
        self.screen = screen

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0 or self.rect.right > self.screen.get_width():
            self.speed_x *= -1
            self.rect.y += self.speed_y
        if self.rect.top < 0:
            self.rect.y += self.speed_y
        elif self.rect.bottom > self.screen.get_height():
            self.rect.x = random.randrange(self.screen.get_width() - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_x = random.choice([-2, 2])
            self.speed_y = random.randrange(1, 4)

    def drop_bomb(self, sprites, bomb_sprite):
        bomb = Bomb(self.rect.centerx, self.rect.bottom)
        sprites.add(bomb)
        bomb_sprite.add(bomb)

    def generate_extra_enemies():
         for _ in range(len(enemies) * 4):
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)