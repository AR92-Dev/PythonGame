
import sys
import pygame

class MainInterface(pygame.sprite.Sprite):
    def __init__(self, cfg):
        pygame.sprite.Sprite.__init__(self)
        width, height = 800, 500
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((30, 30, 30, 20))
        font = pygame.font.Font(cfg.FONTPATHS['Calibri'], 48)
        text_surf = font.render("Game Over", True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=(width // 2, 80))
        self.image.blit(text_surf, text_rect)
        self.rect = self.image.get_rect()
        self.rect.center = cfg.SCREENSIZE[0] / 2, cfg.SCREENSIZE[1] / 2
    def update(self):
        pass

class ContinueButton(pygame.sprite.Sprite):
    def __init__(self, cfg, position=(700, 409)):
        pygame.sprite.Sprite.__init__(self)
        self.image_1 = pygame.image.load(cfg.IMAGEPATHS['start']['quit_black']).convert_alpha()
        self.image_2 = pygame.image.load(cfg.IMAGEPATHS['start']['quit_red']).convert_alpha()
        self.image = self.image_1
        self.rect = self.image.get_rect()
        self.rect.center = position
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image = self.image_2
        else:
            self.image = self.image_1

class EndInterface():
    def __init__(self, cfg):
        self.main_interface = MainInterface(cfg)
        self.continue_btn = ContinueButton(cfg)
        self.components = pygame.sprite.LayeredUpdates(self.main_interface, self.continue_btn)
    def update(self, screen):
        clock = pygame.time.Clock()
        background = pygame.Surface(screen.get_size())
        count = 0
        flag = True
        while True:
            clock.tick(60)
            self.components.update()
            self.components.draw(screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.continue_btn.rect.collidepoint(mouse_pos):
                            return True