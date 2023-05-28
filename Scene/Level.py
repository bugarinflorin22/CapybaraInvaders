import pygame
from Scripts.Entity import SpaceShip, Enemy, Bomb
from Scripts.Movement import Player_Movement
from Scripts.Button import Button

def run_game(screen, event):
    pygame.init()
    clock = pygame.time.Clock()

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)

    screen_width, screen_height = screen.get_size()
    pygame.display.set_caption("Capybara Invaders - Chapter 1")
    background_image = pygame.image.load("Art/level/background_level.png")
    scaled_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    background = scaled_image.get_rect()
    background.height = screen_height
    background.width = screen_width

    bullets_sprite = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bombs = pygame.sprite.Group()

    entity_sprites = pygame.sprite.Group()
    player_image = pygame.image.load("Art/player/spaceship.png")
    player = SpaceShip(screen, player_image)
    entity_sprites.add(player)

    for _ in range(2):
        enemy = Enemy(screen)
        entity_sprites.add(enemy)
        enemies.add(enemy)
        bomb = Bomb(10, 20, screen)
        entity_sprites.add(bomb)
        bombs.add(bomb)

    game_over = False
    done = True

    while not game_over:
        if done:
            screen.blit(scaled_image, background)
            pygame.display.flip()
            done = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot(entity_sprites, bullets_sprite)

        Player_Movement(event, player)
        entity_sprites.update()
        screen.blit(scaled_image, background)

        hits = pygame.sprite.groupcollide(enemies, bullets_sprite, True, True)
        for hit in hits:
            enemy = Enemy(screen)
            entity_sprites.add(enemy)
            enemies.add(enemy)

        hits = pygame.sprite.spritecollide(player, bombs, True)
        if hits:
            player.lives -= 1
            if player.lives <= 0:
                game_over = True

        if len(enemies) == 0:
            pass

        entity_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)