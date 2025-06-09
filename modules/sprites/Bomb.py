import math
import random
import pygame


class Bomb(pygame.sprite.Sprite):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        self.image = pygame.image.load(cfg.IMAGEPATHS['game']['Bomb'])
        self.rect = self.image.get_rect()
        self.explode_radius = 60
        self.damage = 200
        self.position = (0, 0)
        self.rect.left, self.rect.top = self.position
        self.price = 100
        self.explode_delay = 3000 
        self.explode_time = None
    def reset(self):
        self.explode_time = pygame.time.get_ticks() + self.explode_delay

    def explode(self, enemies_group):
        for enemy in enemies_group:
            distance = math.hypot(enemy.rect.centerx - self.rect.centerx, enemy.rect.centery - self.rect.centery)
            if distance <= self.explode_radius:
                enemy.life_value -= self.damage
    