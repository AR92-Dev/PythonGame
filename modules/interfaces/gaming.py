

import sys
import json
import math
import random
import pygame
from ..sprites import Enemy
from ..sprites import Turret
from ..sprites.Bomb import Bomb
from .pause import PauseInterface
from collections import namedtuple
import cfg
import os
class GamingInterface():
    def __init__(self, cfg):
        self.rightinfo_rect = pygame.Rect(1100, 0, 200, 600)
        self.cfg = cfg
        map_w = self.cfg.SCREENSIZE[0]
        map_h = self.cfg.SCREENSIZE[1]
        button_w = 80
        button_h = 80
        button_y = self.cfg.SCREENSIZE[0]-100
        gap = 100
        toolbar_w = 1000
        info_w = (self.cfg.SCREENSIZE[0] - toolbar_w) // 2
        info_h = self.cfg.SCREENSIZE[1] - map_h
        toolbar_h = self.cfg.SCREENSIZE[1] - map_h
        self.map_rect = pygame.Rect(0, 0, map_w, map_h)
        self.map_surface = pygame.Surface((map_w, map_h))
        self.grass = pygame.image.load(cfg.IMAGEPATHS['game']['grass_1'])
        self.rock = pygame.image.load(cfg.IMAGEPATHS['game']['Ground_1'])
        self.dirt = pygame.image.load(cfg.IMAGEPATHS['game']['dirt'])
        self.water = pygame.image.load(cfg.IMAGEPATHS['game']['water'])
        self.bush = pygame.image.load(cfg.IMAGEPATHS['game']['bush'])
        self.nexus = pygame.image.load(cfg.IMAGEPATHS['game']['Castle_Easy'])
        self.cave = pygame.image.load(cfg.IMAGEPATHS['game']['cave'])
        self.element_size = int(self.grass.get_rect().width)
        self.info_font = pygame.font.Font(cfg.FONTPATHS['Calibri'], 14)
        self.button_font = pygame.font.Font(cfg.FONTPATHS['Calibri'], 20)
        self.placeable = {0: self.grass,3:self.water}
        self.placeable_Bomb = {1: self.rock}
        self.map_elements = {
            0: self.grass,
            1: self.rock,
            2: self.dirt,
            3: self.water,
            4: self.bush,
            5: self.nexus,
            6: self.cave
        }
        self.path_list = []
        self.current_map = dict()
        self.mouse_carried = []
        self.built_turret_group = pygame.sprite.Group()
        self.built_Bomb_group = pygame.sprite.Group()
        self.enemies_group = pygame.sprite.Group()
        self.arrows_group = pygame.sprite.Group()
        Button = namedtuple('Button', ['rect', 'text', 'onClick', 'image'])
        self.button_images = {
            'T1': pygame.image.load(cfg.IMAGEPATHS['game']['T1']).convert_alpha(),
            'T2': pygame.image.load(cfg.IMAGEPATHS['game']['T2']).convert_alpha(),
            'T3': pygame.image.load(cfg.IMAGEPATHS['game']['T3']).convert_alpha(),
            'Bomb': pygame.image.load(cfg.IMAGEPATHS['game']['Bomb']).convert_alpha(),
            'XXX': pygame.image.load(cfg.IMAGEPATHS['game']['T1']).convert_alpha(),
            'Pause': pygame.image.load(cfg.IMAGEPATHS['game']['pause']).convert_alpha(),
            'Quit': pygame.image.load(cfg.IMAGEPATHS['game']['T1']).convert_alpha()
}
        self.buttons = [
            Button(pygame.Rect(button_y, gap, button_w, button_h), 'T1', self.takeT1, self.button_images['T1']),
            Button(pygame.Rect(button_y, gap*2 , button_w, button_h), 'T2', self.takeT2, self.button_images['T2']),
            Button(pygame.Rect(button_y, gap*3 , button_w, button_h), 'T3', self.takeT3, self.button_images['T3']),
            Button(pygame.Rect(button_y, gap*4 , button_w, button_h), 'Bomb', self.takeBomb, self.button_images['Bomb']),
            Button(pygame.Rect(button_y, gap*5 , button_w, button_h), 'Remove', self.takeXXX, self.button_images['XXX']),
            
]

    def start(self, screen, map_path=None, difficulty_path=None):
        with open(difficulty_path, 'r') as f:
            difficulty_dict = json.load(f)
        self.money = difficulty_dict.get('money')
        self.health = difficulty_dict.get('health')
        self.max_health = difficulty_dict.get('health')
        difficulty_dict = difficulty_dict.get('enemy')
        generate_enemies_event = pygame.constants.USEREVENT + 0
        pygame.time.set_timer(generate_enemies_event, 500)
        generate_enemies_flag = False
        num_generate_enemies = 0
        generate_enemy_event = pygame.constants.USEREVENT + 1
        pygame.time.set_timer(generate_enemy_event, 500)
        generate_enemy_flag = False
        enemy_range = None
        num_enemy = None
        manual_shot = False
        has_control = False
        while True:
            if self.health <= 0:
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if self.map_rect.collidepoint(event.pos):
                            if self.mouse_carried:
                                if self.mouse_carried[0] == 'turret':
                                    self.buildTurret(event.pos)
                                elif self.mouse_carried[0] == 'bomb':
                                    self.buildBomb(event.pos)
                                elif self.mouse_carried[0] == 'XXX':
                                    self.sellTurret(event.pos)
                        
                        for button in self.buttons:
                            if button.rect.collidepoint(event.pos):
                                if button.text == 'T1':
                                    button.onClick()
                                elif button.text == 'T2':
                                    button.onClick()
                                elif button.text == 'T3':
                                    button.onClick()
                                elif button.text == 'Bomb':
                                    button.onClick()
                                elif button.text == 'Remove':
                                    button.onClick()
                                elif button.text == 'Pause':
                                    button.onClick(screen)
                                elif button.text == 'Quit':
                                    button.onClick()
                                break
                        if self.Pause_rect.collidepoint(event.pos):
                            self.pauseGame(screen)
                    if event.button == 3:
                        self.mouse_carried = []
                    if event.button == 2:
                        manual_shot = True
                if event.type == generate_enemies_event:
                    generate_enemies_flag = True
                if event.type == generate_enemy_event:
                    generate_enemy_flag = True
            if generate_enemies_flag:
                generate_enemies_flag = False
                num_generate_enemies += 1
                idx = 0
                for key, value in difficulty_dict.items():
                    idx += 1
                    if idx == len(difficulty_dict.keys()):
                        enemy_range = value['enemy_range']
                        num_enemy = value['num_enemy']
                        break
                    if num_generate_enemies <= int(key):
                        enemy_range = value['enemy_range']
                        num_enemy = value['num_enemy']
                        break
            if generate_enemy_flag and num_enemy:
                generate_enemy_flag = False
                num_enemy -= 1
                enemy = Enemy(random.choice(range(enemy_range)), self.cfg)
                self.enemies_group.add(enemy)
            for turret in self.built_turret_group:
                if not manual_shot:
                    position = turret.position[0] + self.element_size // 2, turret.position[1]
                    arrow = turret.shot(position)
                else:
                    position = turret.position[0] + self.element_size // 2, turret.position[1]
                    mouse_pos = pygame.mouse.get_pos()
                    angle = math.atan((mouse_pos[1] - position[1]) / (mouse_pos[0] - position[0] + 1e-6))
                    arrow = turret.shot(position, angle)
                    has_control = True
                if arrow:
                    self.arrows_group.add(arrow)
                else:
                    has_control = False
            for bomb in self.built_Bomb_group.copy():
                current_time = pygame.time.get_ticks()
                if bomb.explode_time and current_time >= bomb.explode_time:
                    bomb.explode(self.enemies_group)
                    self.built_Bomb_group.remove(bomb)
                    del bomb
                    
            if has_control:
                has_control = False
                manual_shot = False
            for arrow in self.arrows_group:
                arrow.move()
                points = [(arrow.rect.left, arrow.rect.top), (arrow.rect.left, arrow.rect.bottom), (arrow.rect.right, arrow.rect.top), (arrow.rect.right, arrow.rect.bottom)]
                if (not self.map_rect.collidepoint(points[0])) and (not self.map_rect.collidepoint(points[1])) and \
                   (not self.map_rect.collidepoint(points[2])) and (not self.map_rect.collidepoint(points[3])):
                    self.arrows_group.remove(arrow)
                    del arrow
                    continue
                for enemy in self.enemies_group:
                    if pygame.sprite.collide_rect(arrow, enemy):
                        enemy.life_value -= arrow.attack_power
                        self.arrows_group.remove(arrow)
                        del arrow
                        break
            self.draw(screen, map_path)
    def draw(self, screen, map_path):
        
        self.loadMap(screen, map_path)
        self.drawMouseCarried(screen)
        self.drawBuiltTurret(screen)
        self.drawBuiltBomb(screen)
        self.drawEnemies(screen)
        self.drawArrows(screen)
        self.drawButtons(screen)
        self.drawMoney(screen) 
        self.drawPauseButton(screen,self.button_images['Pause'])
        pygame.display.flip()
    def drawArrows(self, screen):
        for arrow in self.arrows_group:
            screen.blit(arrow.image, arrow.rect)
    def drawEnemies(self, screen):
        for enemy in self.enemies_group:
            if enemy.life_value <= 0:
                self.money += enemy.reward
                self.enemies_group.remove(enemy)
                del enemy
                continue
            enemy.update()
            res = enemy.move(self.element_size)
            if res:
                coord = self.find_next_path(enemy)
                if coord:
                    enemy.reached_path.append(enemy.coord)
                    enemy.coord = coord
                    enemy.position = self.coord2pos(coord)
                    enemy.rect.left, enemy.rect.top = enemy.position
                else:
                    self.health -= enemy.damage
                    self.enemies_group.remove(enemy)
                    del enemy
                    continue
            green_len = max(0, enemy.life_value / enemy.max_life_value) * self.element_size
            if green_len > 0:
                pygame.draw.line(screen, (0, 255, 0), (enemy.position), (enemy.position[0] + green_len, enemy.position[1]), 1)
            if green_len < self.element_size:
                pygame.draw.line(screen, (255, 0, 0), (enemy.position[0] + green_len, enemy.position[1]), (enemy.position[0] + self.element_size, enemy.position[1]), 1)
            screen.blit(enemy.image, enemy.rect)
    def drawBuiltTurret(self, screen):
        for turret in self.built_turret_group:
            screen.blit(turret.image, turret.rect)
    def drawBuiltBomb(self, screen):
        for bomb in self.built_Bomb_group:
            screen.blit(bomb.image, bomb.rect)
    def drawMouseCarried(self, screen):
        if self.mouse_carried:
            mouse_pos = pygame.mouse.get_pos()
            if self.mouse_carried[0] == 'turret' or self.mouse_carried[0] == 'bomb':
                image = self.mouse_carried[1].image
            else:
                image = self.mouse_carried[1]
            rect = image.get_rect(center=mouse_pos)
            if self.map_rect.collidepoint(mouse_pos):
                screen.blit(image, rect.topleft)

                if self.mouse_carried[0] == 'turret' or self.mouse_carried[0] == 'bomb':
                    self.mouse_carried[1].rect = rect
                    self.mouse_carried[1].position = rect.topleft

    
    def showSelectedInfo(self, screen, button):
        if button.text in ['T1', 'T2', 'T3']:
            turret = Turret({'T1': 0, 'T2': 1, 'T3': 2}[button.text], self.cfg)
            selected_info1 = self.info_font.render('Cost: ' + str(turret.price), True, (255, 255, 255))
            selected_info2 = self.info_font.render('Damage: ' + str(turret.arrow.attack_power), True, (255, 255, 255))
            selected_info3 = self.info_font.render('Affordable: ' + str(self.money >= turret.price), True, (255, 255, 255))
            screen.blit(selected_info1, (self.rightinfo_rect.left + 5, self.rightinfo_rect.top + 35))
            screen.blit(selected_info2, (self.rightinfo_rect.left + 5, self.rightinfo_rect.top + 55))
            screen.blit(selected_info3, (self.rightinfo_rect.left + 5, self.rightinfo_rect.top + 75))
        elif button.text == 'Bomb':
            selected_info = self.info_font.render('Place a bomb in a enemy road', True, (255, 255, 255))
            screen.blit(selected_info, (self.rightinfo_rect.left + 5, self.rightinfo_rect.top + 35))
        elif button.text == 'Remove':
            selected_info = self.info_font.render('Sell a turret', True, (255, 255, 255))
            screen.blit(selected_info, (self.rightinfo_rect.left + 5, self.rightinfo_rect.top + 35))
        elif button.text == 'Pause':
            selected_info = self.info_font.render('Pause game', True, (255, 255, 255))
            screen.blit(selected_info, (self.rightinfo_rect.left + 5, self.rightinfo_rect.top + 35))
        elif button.text == 'Quit':
            selected_info = self.info_font.render('Quit game', True, (255, 255, 255))
            screen.blit(selected_info, (self.rightinfo_rect.left + 5, self.rightinfo_rect.top + 35))
    def sellTurret(self, position):
        coord = self.pos2coord(position)
        for turret in self.built_turret_group:
            if coord == turret.coord:
                self.built_turret_group.remove(turret)
                self.money += int(turret.price * 0.5)
                del turret
                break
    def buildTurret(self, position):
        turret = self.mouse_carried[1]
        coord = self.pos2coord(position)
        position = self.coord2pos(coord)
        turret.position = position
        turret.coord = coord
        turret.rect.left, turret.rect.top = position
        if self.money - turret.price >= 0:
            if self.current_map.get(turret.coord) in self.placeable.keys():
                self.money -= turret.price
                self.built_turret_group.add(turret)
                if self.mouse_carried[1].turret_type == 0:
                    self.mouse_carried = []
                    self.takeT1()
                elif self.mouse_carried[1].turret_type == 1:
                    self.mouse_carried = []
                    self.takeT2()
                elif self.mouse_carried[1].turret_type == 2:
                    self.mouse_carried = []
                    self.takeT3()


    def buildBomb(self, position):
        bomb = self.mouse_carried[1]
        coord = self.pos2coord(position)
        position = self.coord2pos(coord)
        bomb.position = position
        bomb.coord = coord
        bomb.rect.left, bomb.rect.top = position
        if self.money - bomb.price >= 0:
            if self.current_map.get(bomb.coord) in self.placeable_Bomb.keys():
                self.money -= bomb.price
                self.built_Bomb_group.add(bomb)
                self.mouse_carried = []
                self.takeBomb()
                bomb.reset()


    def takeT1(self):
        T1 = Turret(0, self.cfg)
        if self.money >= T1.price:
            self.mouse_carried = ['turret', T1]

    def takeT2(self):
        T2 = Turret(1, self.cfg)
        if self.money >= T2.price:
            self.mouse_carried = ['turret', T2]
    def takeT3(self):
        T3 = Turret(2, self.cfg)
        if self.money >= T3.price:
            self.mouse_carried = ['turret', T3]
    def takeBomb(self):
        bomb = Bomb(self.cfg)
        if self.money >= bomb.price:
            self.mouse_carried = ['bomb', bomb]
    def takeXXX(self):
        XXX = pygame.image.load(self.cfg.IMAGEPATHS['game']['x'])
        self.mouse_carried = ['XXX', XXX]
    def find_next_path(self, enemy):
        x, y = enemy.coord
        neighbours = [(x, y+1), (x+1, y), (x-1, y), (x, y-1)]
        for neighbour in neighbours:
            if (neighbour in self.path_list) and (neighbour not in enemy.reached_path):
                return neighbour
        return None
    def pos2coord(self, position):
        return (position[0] // self.element_size, position[1] // self.element_size)
    def coord2pos(self, coord):
        return (coord[0] * self.element_size, coord[1] * self.element_size)
    def loadMap(self, screen, map_path):
        
        map_file = open(map_path, 'r')
        idx_j = -1
        for line in map_file.readlines():
            line = line.strip()
            if not line:
                continue
            idx_j += 1
            idx_i = -1
            for col in line:
                try:
                    element_type = int(col)
                    element_img = self.map_elements.get(element_type)
                    element_img = pygame.transform.scale(element_img, (self.element_size, self.element_size))
                    element_rect = element_img.get_rect()
                    idx_i += 1
                    element_rect.left, element_rect.top = self.element_size * idx_i, self.element_size * idx_j
                    self.map_surface.blit(element_img, element_rect)
                    self.current_map[idx_i, idx_j] = element_type
                    if element_type == 1:
                        self.path_list.append((idx_i, idx_j))
                except:
                    continue
        map_name = os.path.basename(map_path)   
        nexus_pos = cfg.nexus_positions.get(map_name, (740, 400))         
        self.map_surface.blit(self.nexus, nexus_pos)
        nexus_width = self.nexus.get_rect().width
        green_len = max(0, self.health / self.max_health) * nexus_width
        if green_len > 0:
            pygame.draw.line(self.map_surface, (0, 0, 255), (nexus_pos[0],nexus_pos[1]-10), (nexus_pos[0] + green_len, nexus_pos[1]-10), 3)
        if green_len < nexus_width:
            pygame.draw.line(self.map_surface, (255, 0, 0), (740 + green_len, 400), (740 + nexus_width, 400), 3)
        screen.blit(self.map_surface, (0, 0))
        map_file.close()
    def pauseGame(self, screen):
        pause_interface = PauseInterface(self.cfg)
        pause_interface.update(screen)
    def quitGame(self):
        pygame.quit()
        sys.exit(0)
    def drawButtons(self, screen):
        for button in self.buttons:
            mouse_pos = pygame.mouse.get_pos()
            button_surface = pygame.Surface((button.rect.width, button.rect.height), pygame.SRCALPHA)
            base_color = (30, 30, 30, 180)
            hover_color = (50, 50, 50, 220)
            color = hover_color if button.rect.collidepoint(mouse_pos) else base_color
            button_surface.fill(color)
            screen.blit(button_surface, button.rect.topleft)
            is_hovered = button.rect.collidepoint(mouse_pos)
            if button.image:
                image_size = (33, 33)
                image = pygame.transform.scale(button.image, image_size)
                image_rect = image.get_rect(center=(button.rect.centerx, button.rect.centery - 15))
                screen.blit(image, image_rect)
            button_text = self.button_font.render(button.text, True, (255, 255, 255))
            button_text_rect = button_text.get_rect(center=(button.rect.centerx, button.rect.centery + 20))
            screen.blit(button_text, button_text_rect)
            if is_hovered:
                self.drawInfoPanel(screen)

    def drawInfoPanel(self, screen):
        info_surface = pygame.Surface((self.rightinfo_rect.width, self.rightinfo_rect.height), pygame.SRCALPHA)
        info_surface.fill((30, 30, 30, 180))
        screen.blit(info_surface, self.rightinfo_rect.topleft)
        title = self.button_font.render("INFO", True, (255, 255, 255))
        screen.blit(title, (self.rightinfo_rect.left + 10, self.rightinfo_rect.top + 10))
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                self.showSelectedInfo(screen, button)
                break

    def drawMoney(self, screen):
        money_surface = pygame.Surface((150, 40), pygame.SRCALPHA)
        money_surface.fill((0, 0, 0, 120))
        money_text = self.button_font.render(f"Money: ${self.money}", True, (255, 215, 0))
        money_rect = money_text.get_rect(center=(75, 20))
        money_surface.blit(money_text, money_rect)
        screen.blit(money_surface, (10, 10))
    def drawPauseButton(self, screen, image):
        mouse_pos = pygame.mouse.get_pos()
        button_surface = pygame.Surface((33, 33), pygame.SRCALPHA)
        base_color = (30, 30, 30, 180)
        hover_color = (50, 50, 50, 220)
        button_x, button_y = screen.get_width() - 40, 10
        self.Pause_rect = pygame.Rect(button_x, button_y, 500, 500)
        color = hover_color if self.Pause_rect.collidepoint(mouse_pos) else base_color
        button_surface.fill(color)
        image_rect = image.get_rect(center=(button_surface.get_width() // 2, button_surface.get_height() // 2))
        button_surface.blit(image, image_rect)
        screen.blit(button_surface, (button_x, button_y))
        


