import pygame

class Miner(pygame.sprite.Sprite):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        # Use a Miner-specific image
        miner_image_path = self.cfg.IMAGEPATHS['game']['T4']
        self.image = pygame.image.load(miner_image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.coord = (0, 0)
        self.position = (0, 0)
        self.Mining_Time = 0
        self.price = 500
        self.reset()
        
    def Min(self):
        pass
    
    def reset(self):
        self.Mining_Time = pygame.time.get_ticks() + 20000
