
import pygame
from .arrow import Arrow



class Turret(pygame.sprite.Sprite):
    def __init__(self, turret_type, cfg):
        assert turret_type in range(5)
        pygame.sprite.Sprite.__init__(self)
        self.cfg = cfg
        self.turret_type = turret_type
        self.imagepaths = [cfg.IMAGEPATHS['game']['T1'], cfg.IMAGEPATHS['game']['T2'], cfg.IMAGEPATHS['game']['T3'],cfg.IMAGEPATHS['game']['T5']]
        self.image = pygame.image.load(self.imagepaths[turret_type])
        self.rect = self.image.get_rect()
        
        self.arrow = Arrow(turret_type, cfg)
       
        self.coord = 0, 0
        self.position = 0, 0
        self.rect.left, self.rect.top = self.position
        self.reset()
    
    def shot(self, position, angle=None):
        Shot_Sound = pygame.mixer.Sound('resources/audios/TowerShot.mp3')
        arrow = None
        if not self.is_cooling:
            arrow = Arrow(self.turret_type, self.cfg)
            Shot_Sound.play()
            arrow.reset(position, angle)
            self.is_cooling = True
        if self.is_cooling:
            self.cool_time -= 1
            if self.cool_time == 0:
                self.reset()
        return arrow
    
    def reset(self):
        if self.turret_type == 0:
            
            self.price = 500
            
            self.cool_time = 30
           
            self.is_cooling = False
        elif self.turret_type == 1:
            self.price = 1000
            self.cool_time = 50
            self.is_cooling = False
        elif self.turret_type == 2:
            self.price = 1500
            self.cool_time = 100
            self.is_cooling = False
        elif self.turret_type == 3:
            self.price = 100
            self.cool_time = 100
            self.is_cooling = False