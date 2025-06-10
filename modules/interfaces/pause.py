import sys
import pygame

pygame.init()
B_Hover = pygame.mixer.Sound('resources/audios/ButtonHover.mp3')
B_Press = pygame.mixer.Sound('resources/audios/unpause-106278.mp3')
hovered = False
class MainInterface(pygame.sprite.Sprite):
    def __init__(self, cfg):
        pygame.sprite.Sprite.__init__(self)
        width, height = 800, 500
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((30, 30, 30, 20))
        font = pygame.font.Font(cfg.FONTPATHS['Calibri'], 48)
        text_surf = font.render("Game Paused", True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=(width // 2, 80))
        self.image.blit(text_surf, text_rect)
        self.rect = self.image.get_rect()
        self.rect.center = (cfg.SCREENSIZE[0] // 2, cfg.SCREENSIZE[1] // 2)

    def update(self):
        pass

class Button1(pygame.sprite.Sprite):
    def __init__(self, cfg, position):
        pygame.sprite.Sprite.__init__(self)
        self.image_1 = pygame.image.load(cfg.IMAGEPATHS['start']['quit_black']).convert_alpha()
        self.image_2 = pygame.image.load(cfg.IMAGEPATHS['start']['quit_red']).convert_alpha()
        self.image = self.image_1
        self.rect = self.image.get_rect()
        self.rect.center = position
    def update(self):
        global hovered
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.rect.collidepoint(mouse_pos)
        
        if is_hovered:
            self.image = self.image_2
            if not self.hovered:
                B_Hover.play()
                self.hovered = True
        else:
            self.image = self.image_1
            self.hovered = False
class Button2(pygame.sprite.Sprite):
    def __init__(self, cfg, position):
        pygame.sprite.Sprite.__init__(self)
        self.image_1 = pygame.image.load(cfg.IMAGEPATHS['choice']['Resume_1']).convert_alpha()
        self.image_2 = pygame.image.load(cfg.IMAGEPATHS['choice']['Resume_2']).convert_alpha()
        self.image = self.image_1
        self.rect = self.image.get_rect()
        self.rect.center = position
    def update(self):
        global hovered
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.rect.collidepoint(mouse_pos)
        
        if is_hovered:
            self.image = self.image_2
            if not self.hovered:
                B_Hover.play()
                self.hovered = True
        else:
            self.image = self.image_1
            self.hovered = False

class PauseInterface():
    def __init__(self, cfg):
        self.main_interface = MainInterface(cfg)
        self.resume_btn = Button2(cfg, (cfg.SCREENSIZE[0] // 2-200, cfg.SCREENSIZE[1] // 2 + 50))
        self.quit_btn = Button1(cfg, (cfg.SCREENSIZE[0] // 2+200, cfg.SCREENSIZE[1] // 2 +50))
        self.components = pygame.sprite.LayeredUpdates(self.main_interface, self.resume_btn, self.quit_btn)

    def update(self, screen):
        clock = pygame.time.Clock()

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
                        if self.resume_btn.rect.collidepoint(mouse_pos):
                            B_Press.play()
                            return True
                        elif self.quit_btn.rect.collidepoint(mouse_pos):
                            pygame.quit()
                            sys.exit(0)
