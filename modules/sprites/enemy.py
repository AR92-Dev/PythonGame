
import pygame
import os
import cfg
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type, cfg,map_path):
        assert enemy_type in range(4)
        pygame.sprite.Sprite.__init__(self)
        self.enemy_type = enemy_type
        self.CurrentAnim = 0
        self.sprites = []
        if enemy_type == 0:
            self.sprites.append(cfg.IMAGEPATHS['game']['enemy_1_1'])
            self.sprites.append(cfg.IMAGEPATHS['game']['enemy_1_2'])
            self.sprites.append(cfg.IMAGEPATHS['game']['enemy_1_3'])
            self.sprites.append(cfg.IMAGEPATHS['game']['enemy_1_4'])
        elif enemy_type ==1:
            self.sprites.append(cfg.IMAGEPATHS['game']['enemy_2_1'])
            self.sprites.append(cfg.IMAGEPATHS['game']['enemy_2_2'])
            self.sprites.append(cfg.IMAGEPATHS['game']['enemy_2_3'])
            self.sprites.append(cfg.IMAGEPATHS['game']['enemy_2_4'])
        elif enemy_type ==2:
            self.sprites.append(cfg.IMAGEPATHS['game']['enemy_3_1'])
            self.sprites.append(cfg.IMAGEPATHS['game']['enemy_3_2'])
            self.sprites.append(cfg.IMAGEPATHS['game']['enemy_3_3'])
            self.sprites.append(cfg.IMAGEPATHS['game']['enemy_3_4'])
        elif enemy_type ==3:
            self.sprites.append(cfg.IMAGEPATHS['game']['enemy_4_1'])
            self.sprites.append(cfg.IMAGEPATHS['game']['enemy_4_2'])
            self.sprites.append(cfg.IMAGEPATHS['game']['enemy_4_3'])
            self.sprites.append(cfg.IMAGEPATHS['game']['enemy_4_4'])
        self.image = pygame.image.load(self.sprites[self.CurrentAnim])
        self.rect = self.image.get_rect()
        self.reached_path = []
        self.cell_move_dis = 0
        map_name = os.path.basename(map_path)   
        Enemy_pos = cfg.Enemy_positions.get(map_name, (740, 400))
        self.coord = 3, 2
        self.position = Enemy_pos
        self.rect.left, self.rect.top = self.position
        if enemy_type == 0:
            self.max_life_value = 20
            self.life_value = 20
            self.speed = 2
            self.reward = 100
            self.damage = 1
        elif enemy_type == 1:
            self.max_life_value = 40
            self.life_value = 40
            self.speed = 1
            self.reward = 200
            self.damage = 1
        elif enemy_type == 2:
            self.max_life_value = 60
            self.life_value = 60
            self.speed = 0.5
            self.reward = 300
            self.damage = 2
        elif enemy_type == 3:
            self.max_life_value = 100
            self.life_value = 100
            self.speed = 0.2
            self.reward = 500
            self.damage = 4
    def move(self, cell_len):
        is_next_cell = False
        self.cell_move_dis += self.speed
        if self.cell_move_dis > cell_len:
            self.cell_move_dis = 0
            is_next_cell = True
        return is_next_cell
    def update(self):
        self.CurrentAnim+=0.2
        if self.CurrentAnim >=len(self.sprites):
            self.CurrentAnim=0
        self.image = pygame.image.load(self.sprites[int(self.CurrentAnim)])
