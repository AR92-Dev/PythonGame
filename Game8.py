
import cfg
import pygame
from modules import *



def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(cfg.AUDIOPATHS['bgm'])
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.25)
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption("AR92 Tower Defense")
    
    start_interface = StartInterface(cfg)
    is_play = start_interface.update(screen)
    if not is_play:
        return
    
    while True:
        choice_interface = ChoiceInterface(cfg)
        map_choice, difficulty_choice = choice_interface.update(screen,cfg)
        game_interface = GamingInterface(cfg)
        game_interface.start(screen, map_path=cfg.MAPPATHS[str(map_choice)], difficulty_path=cfg.DIFFICULTYPATHS[str(difficulty_choice)])
        end_interface = EndInterface(cfg)
        end_interface.update(screen)


'''run'''
if __name__ == '__main__':
    main()