import pygame
import random


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1920, 1080))


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
screen_width, screen_height = screen.get_size()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Capybara Invaders")
background_image = pygame.image.load("background_level.png")
scaled_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))
background = scaled_image.get_rect()
background.height = screen_height
background.width = screen_width
background.bottomright


class SpaceShip():
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 0
        self.speed_x = 0
        self.speed_y = 0
        self.lives = 3

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()


class Enemy():
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_x = random.choice([-2, 2])
        self.speed_y = random.randrange(1, 4)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1
            self.rect.y += self.speed_y
        if self.rect.top < 0:
            self.rect.y += self.speed_y
        elif self.rect.bottom > screen_height:
            self.rect.x = random.randrange(screen_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_x = random.choice([-2, 2])
            self.speed_y = random.randrange(1, 4)

    def drop_bomb(self):
        bomb = Bomb(self.rect.centerx, self.rect.bottom)
        all_sprites.add(bomb)
        bombs.add(bomb)


class Bomb():
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = 5

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > screen_height:
            self.kill()


all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bombs = pygame.sprite.Group()

player = SpaceShip()
all_sprites.add(player)

for _ in range(2):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -7
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 7
            elif event.key == pygame.K_UP:
                player.speed_y = -5
            elif event.key == pygame.K_DOWN:
                player.speed_y = 5
            elif event.key == pygame.K_SPACE:
                player.shoot()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.speed_y = 0

    all_sprites.update()

    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    hits = pygame.sprite.spritecollide(player, bombs, True)
    if hits:
        player.lives -= 1
        if player.lives <= 0:
            game_over = True

    if len(enemies) == 0:
        pass

    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
