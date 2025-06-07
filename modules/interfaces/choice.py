
import sys
import pygame



class MainInterface(pygame.sprite.Sprite):
    def __init__(self, cfg):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(cfg.IMAGEPATHS['choice']['load_game']).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
   
    def update(self):
        pass



class MapButton1(pygame.sprite.Sprite):
    def __init__(self, cfg, position=(175, 140)):
        pygame.sprite.Sprite.__init__(self)
        self.image_1 = pygame.image.load(cfg.IMAGEPATHS['choice']['map1_black']).convert()
        self.image_2 = pygame.image.load(cfg.IMAGEPATHS['choice']['map1_red']).convert()
        self.image_3 = pygame.image.load(cfg.IMAGEPATHS['choice']['map1']).convert()
        self.image = self.image_1
        self.rect = self.image.get_rect()
        self.rect.center = position
   
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image = self.image_2
        else:
            self.image = self.image_1



class MapButton2(pygame.sprite.Sprite):
    def __init__(self, cfg, position=(175, 340)):
        pygame.sprite.Sprite.__init__(self)
        self.image_1 = pygame.image.load(cfg.IMAGEPATHS['choice']['map2_black']).convert()
        self.image_2 = pygame.image.load(cfg.IMAGEPATHS['choice']['map2_red']).convert()
        self.image_3 = pygame.image.load(cfg.IMAGEPATHS['choice']['map2']).convert()
        self.image = self.image_1
        self.rect = self.image.get_rect()
        self.rect.center = position
 
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image = self.image_2
        else:
            self.image = self.image_1



class MapButton3(pygame.sprite.Sprite):
    def __init__(self, cfg, position=(175, 540)):
        pygame.sprite.Sprite.__init__(self)
        self.image_1 = pygame.image.load(cfg.IMAGEPATHS['choice']['map3_black']).convert()
        self.image_2 = pygame.image.load(cfg.IMAGEPATHS['choice']['map3_red']).convert()
        self.image_3 = pygame.image.load(cfg.IMAGEPATHS['choice']['map3']).convert()
        self.image = self.image_1
        self.rect = self.image.get_rect()
        self.rect.center = position
    
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image = self.image_2
        else:
            self.image = self.image_1



class InfoBox(pygame.sprite.Sprite):
    def __init__(self, position=(800, 400)):
        pygame.sprite.Sprite.__init__(self)
        self.ori_image = pygame.Surface((800, 600))
        self.ori_image.fill((255, 255, 255))
        self.ori_image_front = pygame.Surface((795, 595))
        self.ori_image_front.fill((0, 0, 0))
        self.ori_image.blit(self.ori_image_front, (2, 2))
        self.rect = self.ori_image.get_rect()
        self.rect.center = position
    
    def update(self, btns):
        self.image = self.ori_image
        mouse_pos = pygame.mouse.get_pos()
        for btn in btns:
            if btn.rect.collidepoint(mouse_pos):
                self.image.blit(btn.image_3, (225, 255))
                break



class EasyButton(pygame.sprite.Sprite):
    def __init__(self, cfg, position=(700, 150)):
        pygame.sprite.Sprite.__init__(self)
        self.image_1 = pygame.image.load(cfg.IMAGEPATHS['choice']['easy_1']).convert()
        self.image_2 = pygame.image.load(cfg.IMAGEPATHS['choice']['easy_2']).convert()
        self.image_3 = pygame.image.load(cfg.IMAGEPATHS['choice']['Easy_B']).convert()
        self.text = "easy"
        self.image = self.image_1
        self.rect = self.image.get_rect()
        self.rect.center = position
    
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image = self.image_2
        else:
            self.image = self.image_1



class MediumButton(pygame.sprite.Sprite):
    def __init__(self, cfg, position=(700, 350)):
        pygame.sprite.Sprite.__init__(self)
        self.image_1 = pygame.image.load(cfg.IMAGEPATHS['choice']['mid_1']).convert()
        self.image_2 = pygame.image.load(cfg.IMAGEPATHS['choice']['mid_2']).convert()
        self.image_3 = pygame.image.load(cfg.IMAGEPATHS['choice']['Mid_B']).convert()
        self.text = "medium"
        self.image = self.image_1
        self.rect = self.image.get_rect()
        self.rect.center = position
    
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image = self.image_2
        else:
            self.image = self.image_1



class HardButton(pygame.sprite.Sprite):
    def __init__(self, cfg, position=(700, 550)):
        pygame.sprite.Sprite.__init__(self)
        self.image_1 = pygame.image.load(cfg.IMAGEPATHS['choice']['hard_1']).convert()
        self.image_2 = pygame.image.load(cfg.IMAGEPATHS['choice']['hard_2']).convert()
        self.image_3 = pygame.image.load(cfg.IMAGEPATHS['choice']['Hard_B']).convert()
        self.text = "hard"
        self.image = self.image_1
        self.rect = self.image.get_rect()
        self.rect.center = position
    
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image = self.image_2
        else:
            self.image = self.image_1



class ChoiceInterface():
    def __init__(self, cfg):
        # part1
        self.main_interface = MainInterface(cfg)
        self.map_btn1 = MapButton1(cfg)
        self.map_btn2 = MapButton2(cfg)
        self.map_btn3 = MapButton3(cfg)
        self.info_box = InfoBox()
        # part2
        self.easy_btn = EasyButton(cfg)
        self.medium_btn = MediumButton(cfg)
        self.hard_btn = HardButton(cfg)
    
    def update(self, screen,cfg):
        clock = pygame.time.Clock()
        # part1
        self.map_btns = pygame.sprite.Group(self.map_btn1, self.map_btn2, self.map_btn3)
        
        map_choice, difficulty_choice = None, None
        while True:
            clock.tick(60)
            self.main_interface.update()
            self.map_btns.update()
            self.info_box.update(self.map_btns)
            screen.blit(self.main_interface.image, self.main_interface.rect)
            self.map_btns.draw(screen)
            screen.blit(self.info_box.image, self.info_box.rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        idx = 0
                        for btn in self.map_btns:
                            idx += 1
                            if btn.rect.collidepoint(mouse_pos):
                                map_choice = idx
            if map_choice:
                break
        # part2
        self.Background1 = pygame.image.load(cfg.IMAGEPATHS['choice']['Easy_B']).convert()
        self.Background2 = pygame.image.load(cfg.IMAGEPATHS['choice']['Mid_B']).convert()
        self.Background3 = pygame.image.load(cfg.IMAGEPATHS['choice']['Hard_B']).convert()
        self.Background=self.Background1
        self.Background_rect = self.Background.get_rect()
        self.Background_rect.topleft = (0, 0)
       
        self.difficulty_btns = pygame.sprite.Group(self.easy_btn, self.medium_btn, self.hard_btn)
        self.Background = self.Background1
        while True:
            clock.tick(60)
            mouse_pos = pygame.mouse.get_pos()
            
            for btn in self.difficulty_btns:
                if btn.rect.collidepoint(mouse_pos):
                    if btn.text == "easy":
                        self.Background = self.Background1
                    elif btn.text == "medium":
                        self.Background = self.Background2
                    elif btn.text == "hard":
                        self.Background = self.Background3
                    break
            screen.blit(self.Background, self.Background_rect)
            self.difficulty_btns.update()
            self.difficulty_btns.draw(screen)
            for btn in self.difficulty_btns:
                if btn.rect.collidepoint(mouse_pos):
                    self.Background.blit(btn.image_3, (0, 0))
                break
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        idx = 0
                        for btn in self.difficulty_btns:
                            idx += 1
                            if btn.rect.collidepoint(mouse_pos):
                                difficulty_choice = btn.text
            if difficulty_choice:
                break
        return map_choice, difficulty_choice