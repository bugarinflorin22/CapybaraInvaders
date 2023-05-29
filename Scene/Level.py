import pygame
from Scripts.Entity import SpaceShip, Enemy, Bomb
from Scripts.Movement import Player_Movement
from Scripts.Text import Text


class Level:

    def __init__(self, screen, event, bg_img):
        self.screen = screen
        self.event = event
        self.bg_img = bg_img
        self.react_bg_img = bg_img.get_rect()
        player_image = pygame.image.load("Art/player/spaceship.png")
        self.player = SpaceShip(self.screen, player_image)
        self.player_sprite = pygame.sprite.Group()
        self.player_sprite.add(self.player)
        self.enemy = Enemy(screen)
        self.bomb = Bomb(screen)
        self.entity = pygame.sprite.Group()
        self.bullet = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.points = 0
        self.bomb_power = 1
        self.text = Text("Points: ", 36, (10, 10))
        self.text2 = Text("Points: ", 36, (10, 40))
        self.text3 = Text(f"GAME OVER - {self.points} points", 36, (850, 500))

    def create(self):
        self.screen.blit(self.bg_img, self.react_bg_img)
        self.entity.add(self.player)

    def update(self, space_key, event):
        if space_key:
            self.player.shoot(self.entity, self.bullet)

        self.screen.blit(self.bg_img, self.react_bg_img)

        if len(self.enemies) < 1:
            if 2 + int(self.points/2) < 20:
                for _ in range(2 + int(self.points/2)):
                    enemy = Enemy(self.screen)
                    self.entity.add(enemy)
                    self.enemies.add(enemy)
            else:
                for _ in range(20):
                    enemy = Enemy(self.screen)
                    self.entity.add(enemy)
                    self.enemies.add(enemy)

            if self.points > 30:
                for _ in range(self.bomb_power):
                    bomb = Bomb(self.screen)
                    if self.bomb_power < 9:
                        self.bomb_power += 1
                    self.entity.add(bomb)
                    self.bombs.add(bomb)

        if self.player.lives > 0:
            hits = pygame.sprite.groupcollide(self.enemies, self.bullet, True, True)
            for hit in hits:
                self.enemy = Enemy(self.screen)
                self.entity.remove(self.enemy)
                self.enemies.remove(self.enemy)
                self.points += 1

        if self.player.lives > 0:
            hits = pygame.sprite.groupcollide(self.enemies, self.player_sprite, True, False)
            for hit in hits:
                self.enemy = Enemy(self.screen)
                self.entity.remove(self.enemy)
                self.enemies.remove(self.enemy)
                self.points -= 1
                self.player.lives -= 1

        if self.player.lives > 0:
            hits = pygame.sprite.groupcollide(self.bombs, self.player_sprite, True, False)
            for hit in hits:
                self.points -= 1
                self.player.lives -= 1

        if self.player.lives > 0:
            Player_Movement(event, self.player)
        self.entity.draw(self.screen)
        self.bullet.draw(self.screen)
        self.bullet.update()
        self.entity.update()
        self.text.update_text(f"Points: {self.points}")
        self.text.draw(self.screen)
        self.text2.update_text(f"Lives: {self.player.lives}")
        self.text2.draw(self.screen)
        self.text3.update_text(f"Game Over - {self.points} points")

        if self.player.lives == 0:
            pygame.draw.rect(self.screen, "black", pygame.Rect((360, 250), (1200, 600)))
            self.text3.draw(self.screen)

        pygame.display.flip()
